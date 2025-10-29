### End to End Project Agentic AI Chatbots

# 🤖 LangGraph Agentic AI — Basic Chatbot

This project demonstrates how to build a **stateful AI Chatbot** using **LangGraph**, **Groq LLM**, and **Streamlit**.  
It follows a modular architecture — separating UI, LLM configuration, state, and graph nodes — making it easy to extend for future use cases.

---

## 🛠 What We Are Building

- **Basic Chatbot** → Chat with the bot  
- **Chatbot with Tools** → Bot can use extra utilities  
- **AI News Bot** → Bot fetches AI news  
- **Stateful & Modular** → Bot remembers conversation & easy to extend

---

## 📦 What We Are Using

| Component          | Purpose |
|-------------------|---------|
| **Python**         | Main programming language |
| **Streamlit**      | Frontend UI for chat |
| **Groq LLM**       | Language model (brain) |
| **LangGraph**      | Organize conversation as a graph (nodes + state) |
| **Nodes**          | Separate tasks like chatbot, tools, news |
| **State**          | Keeps track of all messages |

---

## 📂 Project Structure

*(your existing project structure can go here)*

---

## 🧱 Build Order (Step-by-Step)

If you’re building this project **from scratch**, follow this order carefully 👇

| Step | Folder / File | Description |
|------|----------------|-------------|
| 1️⃣ | `state/state.py` | Defines the structure of the chatbot state (stores messages). |
| 2️⃣ | `nodes/basic_chatbot_node.py` | Implements chatbot logic using the selected LLM. |
| 3️⃣ | `LLMS/groqllm.py` | Sets up and initializes the **Groq LLM**. |
| 4️⃣ | `graph/graph_builder.py` | Builds the **LangGraph flow** (START → chatbot → END). |
| 5️⃣ | `ui/uiconfigfile.ini` | Configuration file for UI (page title, model options). |
| 6️⃣ | `ui/uiconfigfile.py` | Reads configuration using `ConfigParser`. |
| 7️⃣ | `ui/streamlitui/loadui.py` | Streamlit sidebar input fields for user controls. |
| 8️⃣ | `ui/streamlitui/display_result.py` | Displays the chatbot messages on the Streamlit UI. |
| 9️⃣ | `main.py` | Main controller — connects UI, LLM, Graph, and Display. |
| 🔟 | `app.py` | Final entry point to run the entire chatbot app. |

---

## ⚙️ Execution Flow

```text
User → Streamlit UI → Graph → Node → LLM → Node → Graph → UI → Response

User types → UI sends message

Graph routes → Node processes → LLM generates answer

Graph updates state → UI shows reply

📝 Example

User: "Hi, my name is Chris"

Bot: "Nice to meet you Chris. How are you today?"

User: "Give me Python code for Snake game"

Bot: Outputs Python code