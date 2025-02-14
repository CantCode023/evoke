![Header](./assets/header.png)

> [!WARNING]
> Evoke is still a work in progress!

# About
Evoke is a simple Multi-AI Agent to suggest project ideas based on user's prompts.
Evoke first generates a search query based on the user's prompts, Then, it uses the search query to query the relevant repositories and recommends the repositories that best fit the user's prompts.
Evoke aims to help users find a project idea to relieve the coding itch, therefore, **evoking excitement**.

# 💡 Key Features
- 🤖 Query generation using Gemini 1.5 Flash 8B
- 🔎 Searches repositories based on user's prompts
- 💡 Recommends repositories that best fit the user's prompts
- 📈 Give detailed reports of a specified repository using Gemini 2.0 Pro

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

Create a `.env` file in the project directory and add the following variables:

```bash
GEMINI_API_KEY="YOUR_API_KEY"
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
- [ ] 📈 Add CLI implementation using Rich.
- [ ] ⚠️ Add support to respect rate limits.
- [ ] ✨ Refactor and optimize codebase.

---

Made with ❤️ by [**@CantCode023**](https://github.com/CantCode023)