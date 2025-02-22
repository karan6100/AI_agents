# AI_agents

### Prerequisites

- Python 3.8+
- pip
- API Keys for **Groq** and **OpenAI** (stored in a `.env` file)

### Steps

1. Clone this repository:
   ```sh
   git clone https://github.com/yourusername/BlogGenerator.git
   cd BlogGenerator
   ```
2. Create a virtual environment and activate it:
   ```sh
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Create a `.env` file and add your API keys:
   ```
   GROQ_API_KEY=your_groq_api_key
   OPENAI_API_KEY=your_openai_api_key
   ```

## Usage

Run the script with:

```sh
python Blog_generator.py
```

### Input

- The script prompts the user for a keyword, which serves as the basis for the blog generation.

### Output

- A well-structured blog post is generated and displayed in the console.
- The LangGraph workflow graph is saved as an image (`blog_creator_workflow_graph.png`).

## Dependencies

- `langchain`
- `langgraph`
- `langchain_groq`
- `langchain_openai`
- `python-dotenv`
- `IPython`

Install them using:

```sh
pip install -r requirements.txt
```

## License

This project is licensed under the MIT License.

## Author

Karan Bari


