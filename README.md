# AI Legal Assistant

An AI-powered legal assistant built with CrewAI. It analyzes a client's legal dispute and generates a summary note for a lawyer.

## How It Works

The application uses three specialized agents:

- `extracteur`: extracts the key information from the dispute;
- `analyste_rag`: analyzes the extracted information using a RAG-based approach;
- `redacteur`: writes the final legal summary.

The agents run sequentially through CrewAI.

## Project Structure

```text
.
├── src/
│   ├── main.py
│   ├── crewai_agents.py
│   └── tasks.py
├── README.md
└── requirements.txt
```

## Requirements

- Python 3.10 or later;
- The required API key for the configured language model;
- The dependencies listed in `requirements.txt`.

## Installation

Create a virtual environment from the project root:

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

Create a `.env` file in the project root and add the required environment variables.

Example:

```env
OPENAI_API_KEY=your_api_key
```

Do not commit the `.env` file to version control.

## Usage

Run the application from the project root:

```bash
python src/main.py
```

Enter the client's legal dispute when prompted.

To exit the application, type one of the following commands:

```text
quitter
q
exit
```

The commands `q` and `exit` are also supported.

## Example

```text
Describe the client's legal dispute:
> A client is contesting the termination of their contract...
```

The application then displays the final summary prepared for the lawyer.

## Disclaimer

The generated content is provided for assistance only and does not constitute legal advice. It must be reviewed by a qualified legal professional before use.

## Troubleshooting

### Missing module

Make sure the virtual environment is activated and the dependencies are installed:

```bash
pip install -r requirements.txt
```

### Missing API key

Check that the `.env` file exists and contains the API key required by the model configuration.

### Import errors

Run the application from the project root:

```bash
python src/main.py
```