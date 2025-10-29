#16-Agentic-Ai-Project-Langraph\BAsicChatbot\src\langgraphagenticai\ui\uiconfigfile.py


from configparser import ConfigParser  # To read .ini configuration files

# ================================
# Config Class — Handles UI config
# ================================
class Config:
    def __init__(self, config_file="./src/langgraphagenticai/ui/uiconfigfile.ini"):
        """
        Initializes the Config class and loads the configuration file.
        """
        self.config = ConfigParser()           # Create parser object
        self.config.read(config_file)          # Read .ini file content

    def get_llm_options(self):
        """
        Returns list of LLM model options from the .ini file.
        Example: ['Groq']
        """
        return self.config["DEFAULT"].get("LLM_OPTIONS").split(", ")
    
    def get_usecase_options(self):
        """
        Returns list of available chatbot use-cases.
        Example: ['Basic Chatbot']
        """
        return self.config["DEFAULT"].get("USECASE_OPTIONS").split(", ")

    def get_groq_model_options(self):
        """
        Returns list of available Groq model names.
        Example: ['llama-3.1-8b-instant']
        """
        return self.config["DEFAULT"].get("GROQ_MODEL_OPTIONS").split(", ")
    
    def get_page_title(self):
        """
        Returns the Streamlit page title.
        Example: 'LangGraph: Build Stateful Agentic AI graph'
        """
        return self.config["DEFAULT"].get("PAGE_TITLE")
