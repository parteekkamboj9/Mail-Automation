# Email-Automation

### Revolutionizing inbox mastery with intelligent, seamless automation
Transform your email management with our intelligent automation tool! Seamlessly integrated with Outlook, this platform allows you to effortlessly automate email replies, personalize responses with dynamic templates, and schedule campaigns—taking your productivity to new heights.


### Features to be implement

* Use dynamic email templates.
* Use existing templates.
* Use custom Agents for email response.
* Make use of parameters and if statements in your email template.
* Schedule email.
* Specify follow-up rule.


### How It Works:

1. **Authenticate & Connect**: Log in securely with your Microsoft account and accept the terms and conditions to get started.
  
2. **Personalize Your Experience**: Customize your settings, preferences, and notification options to tailor the platform to your unique needs.

3. **Create Your Agent**: Set up an intelligent assistant to handle email responses, selecting dynamic or static templates for personalized communication.

4. **Automate & Schedule**: Effortlessly schedule replies, manage responses across different time zones, and send campaigns to engage with your audience.

5. **Monitor & Optimize**: Use the dashboard to track your email activities, adjust settings, and improve your automated workflows for maximum efficiency.


# How to Run:

Follow these steps to get the project up and running:

### 1. Clone the Repository

First, clone the repository to your local machine.

```bash
git clone <repository_url>
cd <project_directory>
```

### 2. Set Up the Environment

Create a virtual environment to keep your dependencies isolated.

```bash
python3.10 -m venv venv
```

Activate the virtual environment:

- On **Windows**:
  
  ```bash
  venv\Scripts\activate
  ```

- On **Mac/Linux**:
  
  ```bash
  source venv/bin/activate
  ```

### 3. Install Dependencies

Install the required dependencies by using the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

You’ll need to set up your application credentials and API keys. Get the necessary credentials from the following sources:

- **Azure Console Application**:
  - **CLIENT_ID**
  - **CLIENT_SECRET**
  - **Scope**: `Mail.Read`, `Mail.Send`

- **Pinecone**:
  - **PINECONE_INDEX_NAME**
  - **PINECONE_API_KEY**

- **OpenAI**:
  - **OPENAI_API_KEY**

Create a `.env` file in the root directory of your project and add the following:

```env
CLIENT_ID=<your_azure_client_id>
CLIENT_SECRET=<your_azure_client_secret>
MAIL_SCOPE=Mail.Read,Mail.Send
PINECONE_INDEX_NAME=<your_pinecone_index_name>
PINECONE_API_KEY=<your_pinecone_api_key>
OPENAI_API_KEY=<your_openai_api_key>
```

### 5. Run the Application

Start the Flask server on localhost by running:

```bash
python3 app.py
```

Your application should now be live on `http://localhost:5000`.

### 6. Access the UI

Open your web browser and go to `http://localhost:5000` to access the application's homepage, log in, and begin configuring your email automation.


# Project Technologies

- **Python 3.10**: The core programming language for the project.
- **Flask**: A lightweight framework for creating the web application.
- **Pinecone**: A vector database used to store and search data.
- **OpenAI API**: Used for generating AI-powered responses and enhancements.
- **Microsoft Graph API**: For authenticating and interacting with Outlook email.

# Future Integrations

- **Gmail and Yahoo Integration**: We are working on extending support for Gmail, Yahoo, and other email services in the near future.


---
**Note**: Ensure you have Python 3.10 and all required dependencies installed to avoid compatibility issues.
