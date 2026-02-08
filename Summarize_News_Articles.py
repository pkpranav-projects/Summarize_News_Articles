import tkinter as tk
import nltk
from textblob import TextBlob
from nltk.tokenize import sent_tokenize

nltk.download('punkt')
nltk.download('punkt_tab')

def summarize():
    raw_text = utext.get('1.0', 'end').strip()
    
    if not raw_text:
        return

    sentences = sent_tokenize(raw_text)
    summary_text = " ".join(sentences[:3]) if len(sentences) > 3 else raw_text

    summary_box.config(state='normal')
    sentiment_box.config(state='normal')

    summary_box.delete('1.0', 'end')
    sentiment_box.delete('1.0', 'end')

    summary_box.insert('1.0', summary_text)

    analysis = TextBlob(raw_text)
    sentiment_str = f'Polarity: {analysis.polarity:.2f}, Sentiment: {"positive" if analysis.polarity > 0 else "negative" if analysis.polarity < 0 else "neutral"}'
    sentiment_box.insert('1.0', sentiment_str)

    summary_box.config(state='disabled', bg='#f0f0f0')
    sentiment_box.config(state='disabled', bg='#f0f0f0')

root = tk.Tk()
root.title("Text Summarizer - Direct Paste")
root.geometry('1000x800')

tk.Label(root, text="SUMMARY OUTPUT", font=('Arial', 10, 'bold')).pack(pady=5)
summary_box = tk.Text(root, height=12, width=120)
summary_box.config(state='disabled', bg='#f0f0f0')
summary_box.pack(pady=5)

tk.Label(root, text="SENTIMENT ANALYSIS", font=('Arial', 10, 'bold')).pack(pady=5)
sentiment_box = tk.Text(root, height=2, width=120)
sentiment_box.config(state='disabled', bg='#f0f0f0')
sentiment_box.pack(pady=5)

tk.Label(root, text="PASTE YOUR TEXT HERE", font=('Arial', 10, 'bold')).pack(pady=10)
utext = tk.Text(root, height=20, width=120)
utext.pack(pady=5)

btn = tk.Button(root, text="SUMMARIZE NOW", command=summarize, bg='#2196F3', fg='white', font=('Arial', 12, 'bold'))
btn.pack(pady=20)

root.mainloop()
