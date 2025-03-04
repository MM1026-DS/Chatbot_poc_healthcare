# Chatbot_poc_healthcare
# Healthcare Chatbot PoC

![License](https://img.shields.io/badge/license-MIT-blue.svg)

## Overview

This project is a Proof of Concept (PoC) for a healthcare chatbot. The chatbot is designed to assist users with healthcare-related queries, provide symptom analysis, and suggest possible actions based on machine learning and natural language processing (NLP) techniques.

## Features

- **Conversational AI**: Uses NLP to understand and respond to user queries.
- **Healthcare Insights**: Provides symptom-based suggestions and information.
- **Machine Learning Integration**: Utilizes trained models to offer personalized recommendations.
- **User-Friendly Interface**: A simple and interactive chatbot experience.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Installation

Ensure that Python is installed on your system before running the chatbot.

1. **Clone the repository**:

   ```bash
   git clone https://github.com/MM1026-DS/Chatbot_poc_healthcare.git
   ```

2. **Navigate to the project directory**:

   ```bash
   cd Chatbot_poc_healthcare
   ```

3. **Create and activate a virtual environment**:

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows, use 'env\Scripts\activate'
   ```

4. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the chatbot application**:

   ```bash
   python app.py
   ```

2. **Interact with the chatbot**:

   - Open `http://127.0.0.1:5000/` in your browser.
   - Enter healthcare-related queries and receive responses from the chatbot.

## Project Structure

```
Chatbot_poc_healthcare/
├── static/
│   ├── css/
│   ├── js/
│   └── images/
├── templates/
│   ├── index.html
│   ├── chatbot.html
├── models/
│   ├── chatbot_model.pkl
├── app.py
├── requirements.txt
└── README.md
```

- **static/**: Contains CSS, JavaScript, and images for styling.
- **templates/**: HTML templates for chatbot interaction.
- **models/**: Pre-trained machine learning model for NLP-based chatbot.
- **app.py**: Main Flask application script.

## Contributing

Contributions are welcome! If you'd like to enhance this chatbot, fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

