# EasyPolishApplication

Welcome to the EasyPolishApplication repository! This application provides an AI-supported educational platform for learning and writing in Polish. The project is divided into three main parts: Backend, Frontend, and the By5-polishCorrector-LLM-Server.

## Table of Contents
- [EasyPolishApplication](#easypolishapplication)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Features](#features)
  - [Installation](#installation)
    - [Backend](#backend)
    - [Frontend](#frontend)
    - [By5-polishCorrector-LLM-Server](#by5-polishcorrector-llm-server)
  - [Usage](#usage)
    - [Running the Application](#running-the-application)
    - [Using the Application](#using-the-application)
  - [Contributing](#contributing)

## Overview
EasyPolishApplication is an AI-powered platform designed to enhance Polish language learning and writing. The platform assists users in various writing tasks such as essays, emails, journals, reports, proposals, reviews, invoices, and resumes, providing corrections and feedback through an AI model.

## Features
- AI-powered correction and feedback for Polish language writing
- Supports multiple writing formats: essays, emails, journals, reports, proposals, reviews, invoices, and resumes
- User-friendly editor with formatting tools
- Save and load functionality for user writings

## Installation

### Backend
The backend is responsible for handling API requests and processing data. It should be set up to handle communication with the By5-polishCorrector-LLM-Server.

1. **Clone the repository**
   ```sh
   git clone https://github.com/Senegalion/EasyPolishApplication.git
   cd EasyPolishApplication/backend

2. **Install dependencies**
   ```sh
   npm install

3. **Start the backend server**
   ```sh
   npm start

## Frontend
The frontend is the user interface of the application, providing an editor and integration with the backend for processing user writings.

1. **Navigate to the frontend directory**
   ```sh
   cd ../frontend

2. **Install dependencies**
   ```sh
   npm install

3. **Start the frontend server**
   ```sh
   npm start

## By5-polishCorrector-LLM-Server
The By5-polishCorrector-LLM-Server hosts the AI model for correcting and providing feedback on Polish writings.

1. **Navigate to the By5-polishCorrector-LLM-Server directory**
   ```sh
   cd ../By5-polishCorrector-LLM-Server

2. **Install dependencies**
   ```sh
   pip install -r requirements.txt

3. **Start the LLM server**
   ```sh
   python server.py

## Usage
## Running the Application
To run the full application, ensure all three components (Backend, Frontend, and By5-polishCorrector-LLM-Server) are running simultaneously.

## Using the Application
1. Open your web browser and navigate to http://localhost:3000.
2. Choose the type of writing you want to work on (e.g., Essay, E-mail, Journal).
3. Use the editor to write your text. Use the toolbar for text formatting.
4. Click "Save" to save your work. The file will be saved with a name corresponding to the type of writing (e.g., essay.txt, journal.txt).
5. Click "Check" to submit your writing for AI-powered correction and feedback.

## Contributing
1. Fork the repository
2. Create a new branch (git checkout -b feature-branch)
3. Make your changes
4. Commit your changes (git commit -m 'Add some feature')
5. Push to the branch (git push origin feature-branch)
6. Open a pull request
