# 🚀 AI Legal Assistant

**License**: [![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

An elegant fusion of **Python**, **FastAPI**, and **Next.js** to empower SMEs with AI-driven legal guidance.

---

## 🌟 Overview

The **AI Legal Assistant** revolutionizes legal support for small and medium enterprises by delivering instant, context-aware legal insights. Powered by IBM Granite's NLP and Pinecone's semantic search, this platform democratizes legal knowledge while minimizing risks.

![Architecture Diagram](https://via.placeholder.com/800x400?text=AI+Legal+Assistant+Architecture+Diagram+Placeholder)

---

## 🔑 Key Features

- ⚡ **Instant Legal Guidance** - AI-generated actionable responses
- 🔍 **Semantic Search** - Pinecone-powered document retrieval
- 🏗️ **Scalable Architecture** - FastAPI backend + Next.js frontend
- 🎨 **Intuitive Interface** - Responsive design with Tailwind CSS
- 🔒 **Enterprise Security** - Industry-standard data protection

---

## 🛠️ Technologies Used

### **Backend Stack**
| Technology | Purpose | Badge |
|------------|---------|-------|
| FastAPI    | API Framework | ![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=flat&logo=fastapi) |
| PostgreSQL | Database | ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=flat&logo=postgresql) |
| Pinecone   | Vector Search | ![Pinecone](https://img.shields.io/badge/Pinecone-430098?style=flat&logo=pinecone) |
| IBM Granite | NLP Engine | ![IBM](https://img.shields.io/badge/IBM%20Granite-052FAD?style=flat&logo=ibm) |

### **Frontend Stack**
| Technology | Purpose | Badge |
|------------|---------|-------|
| Next.js    | React Framework | ![Next.js](https://img.shields.io/badge/Next.js-000000?style=flat&logo=nextdotjs) |
| Tailwind CSS | Styling | ![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=flat&logo=tailwind-css) |

---

## 🏗 System Architecture

```plaintext
+-------------------+       +-------------------+       +-------------------+
|    Frontend       | ----> |     Backend       | ----> |   PostgreSQL DB    |
|   (Next.js)       |       |   (FastAPI)       |       |                   |
+-------------------+       +-------------------+       +-------------------+
                                    |
                                    v
                            +-------------------+
                            |   Pinecone Index  |
                            +-------------------+
                                    |
                                    v
                            +-------------------+
                            |   IBM Granite     |
                            |   (NLP Model)     |
                            +-------------------+

```
# 🚀 Getting Started

## 📋 Prerequisites

Before diving into the setup, ensure you have the following installed and configured:

### 1. **Python 3.10+**
![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)  
Python is the backbone of our backend. Make sure you have Python 3.10 or higher installed.  
📥 [Download Python](https://www.python.org/downloads/)

---

### 2. **Node.js 18.x+**
![Node.js](https://img.shields.io/badge/Node.js-18.x%2B-green?logo=node.js&logoColor=white)  
Node.js powers the frontend. Ensure you have Node.js 18.x or higher installed.  
📥 [Download Node.js](https://nodejs.org/)

---

### 3. **PostgreSQL**
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-13%2B-blue?logo=postgresql&logoColor=white)  
PostgreSQL is used for database management. Install and configure it on your system.  
📥 [Download PostgreSQL](https://www.postgresql.org/download/)

---

### 4. **Pinecone API Key**
![Pinecone](https://img.shields.io/badge/Pinecone-API%20Key-orange?logo=pinecone&logoColor=white)  
Pinecone enables semantic search. Sign up and get your API key.  
🔑 [Get Pinecone API Key](https://www.pinecone.io/)

---

### 5. **IBM Granite Token**
![IBM Granite](https://img.shields.io/badge/IBM%20Granite-Token-blue?logo=ibm&logoColor=white)  
IBM Granite powers the NLP capabilities. Obtain your access token.  
🔑 [Get IBM Granite Token](https://www.ibm.com/cloud/watson-natural-language-understanding)

---

## 🛠️ Backend Setup

```bash```
# Clone repository
git clone https://github.com/your-repo/ai-legal-assistant.git
cd ai-legal-assistant/backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac

# Install dependencies
pip install -r requirements.txt

# Legal AI Assistant - Documentation

This document provides a comprehensive guide to setting up and using the Legal AI Assistant, an application designed to empower businesses with AI-driven legal analysis. Follow the steps below to get started.

## Getting Started

This section outlines the steps for setting up both the backend and frontend components of the application.

### Backend Setup

#### Environment Configuration (.env)

To configure the backend environment, you need to create a `.env` file in the `backend` directory. Add the following environment variables to this file, replacing the placeholder values with your actual API keys, access tokens, and database credentials:

```env`
PINECONE_API_KEY=your_api_key
IBM_GRANITE_ACCESS_TOKEN=your_token
DATABASE_URL=postgresql://user:pass@localhost:5432/dbname
