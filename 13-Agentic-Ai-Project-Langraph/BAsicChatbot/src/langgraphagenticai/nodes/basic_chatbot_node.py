#C:\Users\window 11\Desktop\Agentic AI\16-Agentic-Ai-Project-Langraph\BAsicChatbot\src\langgraphagenticai\nodes\basic_chatbot_node.py
from src.langgraphagenticai.state.state import State
class BasicChatbotNode:
    """
    Basic Chatbot login implementation
    """
    def __init__(self,model):
        self.llm=model

    def process(self,state:State)->dict:
        """
        Processes the input state and generates a chatbot response.
        """
        return {"messages":self.llm.invoke(state['messages'])}

