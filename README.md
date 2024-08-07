
## Architecture
The main idea is to run "planner" and "execution" agents, whereas the planner generates questions to research, and the execution agents seek the most related information based on each generated research question. Finally, the planner filters and aggregates all related information and creates a research report. <br /> <br /> 
The agents leverage both `gpt-4o-mini` and `gpt-4o` (128K context) to complete a research task. We optimize for costs using each only when necessary.


More specifically:
* Create a domain specific agent based on research query or task.
* Generate a set of research questions that together form an objective opinion on any given task. 
* For each research question, trigger a crawler agent that scrapes online resources for information relevant to the given task.
* For each scraped resources, summarize based on relevant information and keep track of its sources.
* Finally, filter and aggregate all summarized sources and generate a final research report.

## Features
- 📝 Generate research, outlines, resources and lessons reports with local documents and web sources
- 📜 Can generate long and detailed research reports (over 2K words)
- 🌐 Aggregates over 20 web sources per research to form objective and factual conclusions
- 🖥️ Includes an easy-to-use web interface (HTML/CSS/JS)
- 🔍 Scrapes web sources with javascript support
- 📂 Keeps track and context of visited and used web sources
- 📄 Export research reports to PDF, Word and more...


## ⚙️ Getting Started
### Installation
> **Step 0** - Install Python 3.11 or later.

> **Step 1** - Download the project and navigate to its directory

```bash
git clone https://github.com/Batterii/vurvey-researcher.git
cd vurvey-researcher
```

> **Step 3** - Set up API keys using two methods: exporting them directly or storing them in a `.env` file.

For Linux/Windows temporary setup, use the export method:

```bash
export OPENAI_API_KEY={Your OpenAI API Key here}
export TAVILY_API_KEY={Your Tavily API Key here}
```

For a more permanent setup, create a `.env` file in the current `vurvey-researcher` directory and input the env vars (without `export`).

### Quickstart

> **Step 1** - Install dependencies

```bash
pip install -r requirements.txt
```

> **Step 2** - Run the agent with FastAPI

```bash
python -m uvicorn main:app --reload
```

> **Step 3** - Go to http://localhost:8000 on any browser and enter a research task

<br />


## 📄 **WIP** Research on Local Documents

You can instruct the Vurvey Researcher to run research tasks based on your local documents. Currently supported file formats are: PDF, plain text, CSV, Excel, Markdown, PowerPoint, and Word documents.

Step 1: Add the env variable `DOC_PATH` pointing to the folder where your documents are located.

```bash
export DOC_PATH="./my-docs"
```

Step 2: 
 - If you're running the frontend app on localhost:8000, simply select "My Documents" from the the "Report Source" Dropdown Options.


## 👪 **WIP** Multi-Agent Assistant 
As AI evolves from prompt engineering and RAG to multi-agent systems, I've started to work on adding a new multi-agent assistant built with [LangGraph](https://python.langchain.com/v0.1/docs/langgraph/).

By using LangGraph, the research process can be significantly improved in depth and quality by leveraging multiple agents with specialized skills.

An average run generates a 5-6 page research report in multiple formats such as PDF, Docx and Markdown.
