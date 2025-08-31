# Meeting & Office Task Assistant

A comprehensive secretarial automation system built with LangChain, OpenAI, and Google Gemini that automates meeting-related tasks and document generation.

## 🎯 Overview

This system automates the complete workflow for secretarial tasks related to meetings:

1. **Step 1 (OpenAI)**: Generate professional meeting schedules/notices
2. **Step 2 (Gemini)**: Create polite, formal email summaries for staff
3. **Step 3 (OpenAI)**: Generate Minutes of Meeting (MOM) templates
4. **Step 4 (Gemini)**: Create follow-up task lists with assignments

## 🚀 Features

- **Multi-LLM Integration**: Uses both OpenAI GPT-4 and Google Gemini Pro
- **Professional Document Generation**: Creates corporate-quality documents
- **Automated Workflow**: Complete 4-step process automation
- **File Management**: Automatic document saving and organization
- **Environment Configuration**: Secure API key management
- **Interactive Interface**: Both programmatic and interactive usage

## 📋 Requirements

- Python 3.8+
- OpenAI API Key
- Google Gemini API Key
- Virtual environment (recommended)

## 🛠️ Installation

### Quick Setup
Run the automated setup script:
```bash
python setup.py
```

### Manual Setup
1. **Clone or download the project**
2. **Create and activate virtual environment**:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure API keys**:
   - Copy `.env.example` to `.env`:
     ```bash
     cp .env.example .env
     ```
   - Edit `.env` file and add your API keys:
     ```env
     OPENAI_API_KEY=your_actual_openai_key_here
     GOOGLE_API_KEY=your_actual_google_key_here
     ```

## 🎮 Usage

### Basic Usage

```python
from meeting_assistant import MeetingAssistant, MeetingDetails

# Initialize the assistant
assistant = MeetingAssistant()

# Create meeting details
meeting = MeetingDetails(
    date="2024-02-15",
    time="10:00 AM",
    agenda="Q1 Strategy Review, Budget Planning",
    attendees=["CEO", "CFO", "CTO"],
    location="Conference Room",
    duration="2 hours",
    organizer="CEO"
)

# Process the meeting request
results = assistant.process_meeting_request(meeting)

# Print results
assistant.print_results(results)

# Save documents
assistant.save_documents(results)
```

### Command Line Usage

**Run the demo**:
```bash
python demo.py
```

**Run interactive demo**:
```bash
python demo.py --interactive
```

**Run the main assistant**:
```bash
python meeting_assistant.py
```

## 📁 Project Structure

```
langchain task/
├── .env                          # Environment variables (create this)
├── .gitignore                    # Git ignore file
├── config.py                     # Configuration management
├── meeting_assistant.py          # Main assistant class
├── demo.py                       # Demo scripts
├── example.py                    # Environment variables example
├── env_utils.py                  # Environment utilities
├── requirements.txt              # Python dependencies
├── README.md                     # This file
└── meeting_documents/            # Generated documents (auto-created)
    ├── meeting_schedule_*.txt
    ├── email_summary_*.txt
    ├── mom_template_*.txt
    └── task_list_*.txt
```

## 🔧 Configuration

### Environment Variables

The system uses the following environment variables:

- `OPENAI_API_KEY`: Your OpenAI API key
- `GOOGLE_API_KEY`: Your Google Gemini API key

### API Keys Setup

1. **OpenAI API Key**:
   - Visit [OpenAI Platform](https://platform.openai.com/)
   - Create an account and get your API key
   - Add to `.env` file

2. **Google Gemini API Key**:
   - Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Create an API key
   - Add to `.env` file

## 📊 Workflow Steps

### Step 1: Meeting Schedule/Notice (OpenAI)
- Generates professional meeting notices
- Includes all essential details
- Corporate formatting and structure

### Step 2: Staff Email Summary (Gemini)
- Creates concise, polite emails
- Formal business language
- Encourages attendance

### Step 3: Minutes of Meeting Template (OpenAI)
- Structured MOM template
- Space for notes and decisions
- Professional format

### Step 4: Follow-up Task List (Gemini)
- Assigns responsibilities
- Sets deadlines
- Tracks accountability

## 🎨 Example Output

### Meeting Schedule
```
MEETING NOTICE
==============

Subject: Q1 2024 Strategy Review Meeting
Date: February 15, 2024
Time: 10:00 AM - 12:00 PM
Location: Main Conference Room
Organizer: John Smith

Attendees:
- John Smith (CEO)
- Sarah Johnson (CTO)
- Mike Davis (CFO)
- Lisa Brown (HR Manager)
- David Wilson (Project Manager)

Agenda:
1. Q1 2024 Strategy Review
2. Budget Planning
3. Team Performance Assessment
4. New Project Proposals

Preparation Required:
- Please review Q1 performance metrics
- Prepare budget proposals
- Bring any relevant project updates

Contact: john.smith@company.com for questions
```

### Staff Email
```
Subject: Invitation: Q1 Strategy Review Meeting

Dear Team,

You are cordially invited to attend our Q1 2024 Strategy Review Meeting scheduled for February 15, 2024, at 10:00 AM in the Main Conference Room.

This important meeting will cover our quarterly performance review, budget planning, and strategic initiatives for the upcoming quarter. Your participation and input are valuable to our team's success.

Please come prepared with any relevant updates or suggestions. We look forward to your attendance.

Best regards,
John Smith
CEO
```

## 🔒 Security

- **API Keys Protection**: API keys are stored in `.env` file (never committed to version control)
- **Template System**: `.env.example` provides a template without real keys
- **Secure Configuration**: `secure_config.py` handles API keys safely with validation
- **Git Protection**: `.gitignore` excludes all sensitive files
- **Masked Output**: Sensitive information is masked in logs and output
- **Environment Validation**: API keys are validated before use

### 🔑 API Key Security
- Never commit your `.env` file to version control
- Use `.env.example` as a template for new users
- The system will warn you if API keys are not properly configured

## 🐛 Troubleshooting

### Common Issues

1. **API Key Errors**:
   - Ensure API keys are correctly set in `.env` file
   - Verify API keys are valid and have sufficient credits

2. **Import Errors**:
   - Make sure virtual environment is activated
   - Install all requirements: `pip install -r requirements.txt`

3. **Permission Errors**:
   - Ensure write permissions for document saving
   - Check directory permissions

### Debug Mode

Enable debug mode by setting `DEBUG=True` in your `.env` file for detailed logging.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is open source and available under the MIT License.

## 🆘 Support

For issues and questions:
1. Check the troubleshooting section
2. Review the documentation
3. Create an issue in the repository

## 🎉 Acknowledgments

- Built with [LangChain](https://langchain.com/)
- Powered by [OpenAI](https://openai.com/) and [Google Gemini](https://ai.google.dev/)
- Environment management with [python-dotenv](https://github.com/theskumar/python-dotenv) 