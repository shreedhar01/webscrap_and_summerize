import json
import torch
import evaluate
from transformers import pipeline

device = 0 if torch.cuda.is_available() else -1

hub_model= "facebook/bart-base"
summarizer = pipeline("summarization", model=hub_model, device=device)

rouge_score = evaluate.load("rouge")


file_path = 'summerize_data.json'
with open(file_path, 'r') as file:
    alexander_data = json.load(file)

file_path = 'label_data.json'
with open(file_path, 'r') as file:
    label_data = json.load(file)


def print_summary(idx):
    for i in range(len(alexander_data)):
        alexander_data[i]['label'] = label_data[i]


    content = alexander_data[idx]["content"]
    title = alexander_data[idx]["title"]
    summary = summarizer(alexander_data[idx]["content"])[0]["summary_text"]

    scores = rouge_score.compute(
      predictions=[summary], references=[alexander_data[idx]['label']]
    )
    print(f"\n'>>> Title: {title}'")
    print(f"\n'>>> Summary: {summary}'")
    print(f"\n'>>> Scores: {scores}")