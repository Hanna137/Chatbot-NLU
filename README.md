# Chatbot App

This is a simple chatbot application built with Flask and deployed as Docker. Users can send messages from the web interface and receive responses from the chatbot.

Technology used
- Python 3.9
- Flask
- HTML (with template `index.html`)
- Docker

# Directory structure
```
chatbot-app/
│
├── app.py # Flask app source code
├── chat.py # Get_response() function to handle chatbot responses
├── templates/
│ └── index.html # Main interface
├── requirements.txt # Required libraries
└── Dockerfile # Docker packaging
```

#Running instructions
Open all files, in app.py click Run, a local link will appear, click on it to display the chatbot

# Chatbot processing logic
- Interface sends POST request to '/get' with user input content.
- The server calls the 'get_response()' function from the 'chat.py' file to generate the response.

- The response is sent back as JSON and displayed on the interface.

#There is also a Docker file to build on GG Cloud.
