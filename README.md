# AiChatBot

A self-learning Python chatbot that understands user questions using fuzzy matching and learns new responses in real-time.

## Quick Start

```bash
git clone https://github.com/Naman-Manudi/AiChatBot.git
cd AiChatBot
python main.py
```

## How It Works

1. **Understand**: Matches your question against the knowledge base using fuzzy string matching
2. **Respond**: Returns the most relevant answer if found
3. **Learn**: If unsure, asks you to teach it—and remembers for next time
4. **Persist**: Saves all learned responses to `knowledge_base.json`

## Example

```
You: What is Python?
Bot: Python is a programming language.

You: What's AI?
Bot: I dont know the answer can you teach me?
Type the answer or "skip" to skip: AI is artificial intelligence.
Bot: Thank you! I learned a new Response!

You: quit
```

## Features

✅ No external dependencies (pure Python standard library)  
✅ Fuzzy matching for flexible question understanding  
✅ Self-learning from user interactions  
✅ Persistent JSON-based memory  
✅ Simple, readable codebase  

## Files

| File | Purpose |
|------|---------|
| `main.py` | Core chatbot logic |
| `knowledge_base.json` | Stores Q&A pairs |

## Customization

**Change matching sensitivity** (line 23 in `main.py`):
```python
matches = get_close_matches(user_question, question, n=1, cutoff=0.6)  # 0-1 range
```

**Pre-populate knowledge base**:
```json
{
  "questions": [
    {
      "question": "What is Python?",
      "answer": "A high-level programming language."
    }
  ]
}
```

## Requirements

- Python 3.9+

## License

MIT License - Open source and free to use

---

Made with ❤️ by [Naman-Manudi](https://github.com/Naman-Manudi)
