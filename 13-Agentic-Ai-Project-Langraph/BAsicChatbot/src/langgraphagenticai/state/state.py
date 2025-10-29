#C:\Users\window 11\Desktop\Agentic AI\16-Agentic-Ai-Project-Langraph\BAsicChatbot\src\langgraphagenticai\state\state.py
from typing_extensions import TypedDict,List
from langgraph.graph.message import add_messages
from typing import Annotated


class State(TypedDict):
    """
    Represent the structure of the state used in graph
    """
    messages: Annotated[List,add_messages]