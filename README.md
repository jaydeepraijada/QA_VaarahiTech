# Q&A Application

This is a simple Question and Answering application built using Streamlit and OpenAI's language model. The application allows users to input questions based on either direct text or Wikipedia articles, providing context for the model to generate relevant answers.

## Features

- **Direct Text Input**: Users can enter their own context and ask questions based on that context.
- **Wikipedia Topic Input**: Users can enter a topic, and the application will fetch relevant information from Wikipedia to provide context for their questions.
- **OpenAI Integration**: Utilizes OpenAI's language model to generate answers based on the provided context.

## Requirements

- Python 3.7 or higher
- Streamlit
- langchain
- langchain_openai
- python-dotenv

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

5. Create a `.env` file in the root directory and add your OpenAI API key:
   ```plaintext
   OPENAI_API_KEY=your_openai_api_key_here
   ```

## Usage

1. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```

2. Open your web browser and go to `http://localhost:8501` to access the application.

3. Select the input type (Direct Text Input or Wikipedia Topic) and enter your question.

4. The application will provide answers based on the context you provided.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.

