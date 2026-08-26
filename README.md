# 🚀 AI Requirements Analyzer

The AI Requirements Analyzer and Test Case Generator is an intelligent system designed to analyze software requirements written in natural language. The application automatically extracts functional requirements, identifies ambiguities, and generates comprehensive positive, negative, and edge-case test cases. The system provides an interactive web interface and supports exporting the complete analysis into a structured, multi-sheet Excel report for practical use.

## 🌟 Features
* **Natural Language Analysis:** Natural language software requirement analysis
* **Automatic Extraction:** Automated extraction of functional requirements
* **Ambiguity Detection:** Detection of ambiguous or incomplete requirement statements
* **Automated Test Case Generation:**
    * ✅ Positive Test Cases
    * ❌ Negative Test Cases
    * ⚠️ Edge-case Test Cases
* **High Performance:** Parallel execution of independent AI processing chains for improved performance
* **Interactive UI:** Interactive Streamlit-based web interface
* **Excel Reports:** Downloadable Excel report with multiple categorized sheets
* **Scalable Architecture:** Modular and maintainable project architecture

## 🧠 System Workflow

* User enters a software requirement through the Streamlit UI
* The requirement is analyzed using AI-based processing
* The system extracts functional requirements and detects ambiguities
* Positive, negative, and edge test cases are generated in parallel
* Results are displayed as a summary in the UI
* A detailed Excel report is generated for download

## ⚡ Performance Optimizations

* Parallel AI Execution using LangChain RunnableParallel
* Prompt Optimization to reduce token usage
* Streamlit Caching to avoid duplicate analysis
* Python-Based Report Generation (no AI usage for Excel export)

## 🛠️ Installation & Setup

```bash
# Clone the Repository
git clone <repository-url>
cd AI_Requirements_Analyzer

# Create and Activate Virtual Environment
python -m venv venv
venv .\venv\Scripts\Activate.ps1   # Windows

# Install Dependencies
python -m pip install -r requirements.txt

# Create .env file
OPENAI_API_KEY=your_api_key_here

# Run the application
python -m streamlit run ui/app.py
```

## 🧪 Sample Requirement Input
"The system shall allow a registered user to book an appointment by selecting a service type, preferred date, and available time slot, after which the system shall confirm the booking by displaying a unique appointment ID and sending a confirmation notification to the user’s registered email, while preventing double booking of the same time slot."

## 📊 Excel Report Details
The generated Excel file contains the following sheets:
* Functional Requirements
* Ambiguities
* Positive Test Cases
* Negative Test Cases
* Edge Case Test Cases
Each sheet contains structured and numbered entries for clarity.

## 🧰 Technologies Used

* Python
* LangChain
* Large Language Models (LLMs)
* Streamlit
* Pydantic
* OpenPyXL

## 🔮 Future Enhancements

* Ambiguity severity classification
* Requirement-to-test traceability matrix (RTM)
* PDF report generation
* Confidence scoring for requirements
* Enhanced UI and dashboard view

## 👤 Author
Vikas [AI & Software Engineering Enthusiast]
