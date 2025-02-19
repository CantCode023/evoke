![Header](./assets/header.png)

# About
Evoke is a simple Multi-AI Agent to suggest project ideas based on user's prompts.
Evoke first generates a search query based on the user's prompts, Then, it uses the search query to query the relevant repositories and recommends the repositories that best fit the user's prompts.
Evoke aims to help users find a project idea to relieve the coding itch, therefore, **evoking excitement**.

# 💡 Key Features
- 🤖 Query generation using Gemini 2.0 Flash Experimental
- 🔎 Searches repositories based on user's prompts
- 💡 Recommends repositories that best fit the user's prompts
- 📈 Give detailed reports of a specified repository

# Table of Contents
- [About](#about)
- [💡 Key Features](#-key-features)
- [🚀 Getting Started](#-getting-started)
  - [📄 Cloning the repository](#-cloning-the-repository)
  - [📦 Installation](#-installation)
  - [🔑 Environment variables](#-environment-variables)
  - [🚀 Usage](#-usage)
  - [📝 License](#-license)
  - [🖊️ TODO-List](#️-todo-list)
  - [📷 Video walkthrough](#-video-walkthrough)
- [Made with ❤️ by @CantCode023](#made-with-❤️-by-cancode023)

---

# 🚀 Getting Started

## 📄 Cloning the repository

```bash
git clone https://github.com/CantCode023/evoke.git
```

## 📦 Installation

```bash
pip install -r requirements.txt
```

## 🔑 Environment variables

You can get your API key from [OpenRouter](https://openrouter.ai/settings/keys).
Create a `.env` file in the project directory and add the following variables:

```bash
OPENROUTER_API_KEY="YOUR_API_KEY"
```

## 🚀 Usage

```bash
python main.py
```

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🖊️ TODO-List
- [x] ~🤖 Fine-tune **query generation** to avoid hallucinations.~
- [x] ~🤖 Fine-tune **recommend agent** to prioritize project repositories than package repositories.~
- [x] ~⌨️ Add loop-support to allow agent to change suggestions.~
- [x] ~📈 Add CLI implementation using Rich.~
- [x] ~🐑 Use OpenRouter instead of Google AI Studio to avoid rate limits.~
- [x] ~⚠️ Add support to respect rate limits.~
- [x] ~✨ Refactor and optimize codebase.~
- [ ] 💻 Use Streamlit for better readability
- [ ] 🤖 Add **project generation** to generate unique projects based on saved repositories.

## 📷 Video walkthrough
[![Watch the video walkthrough](https://img.youtube.com/vi/5pRpD6zeyUQ/maxresdefault.jpg)](https://youtu.be/5pRpD6zeyUQ)

---

Made with ❤️ by [**@CantCode023**](https://github.com/CantCode023)