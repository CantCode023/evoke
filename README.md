![Header](./assets/header.png)

# About
Evoke is a simple Multi-AI Agent to suggest project ideas based on user's prompts.
Evoke first generates a search query based on the user's prompts, Then, it uses the search query to query the relevant repositories and recommends the repositories that best fit the user's prompts.
Evoke aims to help users find a project idea to relieve the coding itch, therefore, **evoking excitement**.

# 💡 Key Features
- 🤖 Query generation using Gemini 2.0 Flash
- 🔎 Searches repositories based on user's prompts
- 💡 Recommends repositories that best fit the user's prompts
- 📈 Give detailed reports of a specified repository

> [!WARNING]
> Evoke is still a work in progress!

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

---

Made with ❤️ by [**@CantCode023**](https://github.com/CantCode023)