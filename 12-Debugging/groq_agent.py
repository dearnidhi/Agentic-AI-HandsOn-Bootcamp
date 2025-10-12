from typing import Annotated
from typing_extensions import TypedDict
from langchain_groq import ChatGroq  # <-- Use Groq model
from langgraph.graph import END, START
from langgraph.graph.state import StateGraph
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode
from langchain_core.tools import tool
from langchain_core.messages import BaseMessage
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set Groq API key from .env
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

# ---- Define Graph State ----
class State(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]

# ---- Initialize Groq model ----
model = ChatGroq(model="llama-3.1-8b-instant", temperature=0)

# ---- Simple agent graph (default) ----
def make_default_graph():
    graph_workflow = StateGraph(State)

    def call_model(state):
        return {"messages": [model.invoke(state["messages"])]}
    
    graph_workflow.add_node("agent", call_model)
    graph_workflow.add_edge("agent", END)
    graph_workflow.add_edge(START, "agent")

    agent = graph_workflow.compile()
    return agent

# ---- Tool-using agent graph ----
def make_alternative_graph():
    """Make a tool-calling agent"""

    @tool
    def add(a: float, b: float):
        """Adds two numbers."""
        return a + b

    # Initialize tool node and bind to model
    tool_node = ToolNode([add])
    model_with_tools = model.bind_tools([add])

    # Model call function
    def call_model(state):
        return {"messages": [model_with_tools.invoke(state["messages"])]}

    # Fixed conditional function
    def should_continue(state: State):
        last_msg = state["messages"][-1]
        if getattr(last_msg, "tool_calls", None):
            return "tools"
        return END

    # Build workflow
    graph_workflow = StateGraph(State)
    graph_workflow.add_node("agent", call_model)
    graph_workflow.add_node("tools", tool_node)
    graph_workflow.add_edge("tools", "agent")
    graph_workflow.add_edge(START, "agent")
    graph_workflow.add_conditional_edges("agent", should_continue)

    agent = graph_workflow.compile()
    return agent

# ---- Compile the agent ----
agent = make_alternative_graph()
