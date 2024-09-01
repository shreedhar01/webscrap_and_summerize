# Wikipedia Scraper and Summarizer

This project is a Python-based tool that scrapes content from a Wikipedia page, processes it into sections, and then summarizes a selected section using a pre-trained BART model. It also calculates ROUGE scores to evaluate the quality of the summary against a pre-existing labeled dataset.

## Project Structure

The project consists of three main Python files:

1. `main.py`: The entry point of the application.
2. `webscrap.py`: Contains functions for scraping and processing Wikipedia content.
3. `summerize.py`: Handles the summarization of content and calculation of ROUGE scores.

## Dependencies

- beautifulsoup4
- requests
- torch
- transformers
- evaluate

You can install these dependencies using pip:

```
pip install beautifulsoup4 requests torch transformers evaluate
```

## Usage

1. Run `main.py`:

```
python main.py
```

2. The script will scrape the Wikipedia page for Alexander the Great.
3. You will be prompted to input an index for the section you want to summarize.
4. The script will then display the title of the section, a summary, and ROUGE scores.

## File Descriptions

### main.py

This is the main script that orchestrates the workflow:

1. It imports the necessary modules (`webscrap` and `summerize`).
2. Calls `webscrap.scrape_wikipedia()` to scrape the Wikipedia page.
3. Prompts the user for an index to summarize.
4. Calls `summerize.print_summary()` to generate and display the summary and scores.

### webscrap.py

This script handles the web scraping and data processing:

- `clean_text()`: Cleans the scraped text by removing citations, extra newlines, and Unicode characters.
- `scrape_wikipedia()`: Scrapes the specified Wikipedia URL, processes the content into sections, and saves the data to a JSON file (`summerize_data.json`).

### summerize.py

This script handles the summarization and evaluation:

- It uses the `facebook/bart-base` model for summarization.
- Loads the scraped data from `summerize_data.json` and labels from `label_data.json`.
- `print_summary()`: Generates a summary for the specified section, calculates ROUGE scores, and prints the results.

## Data Files

- `summerize_data.json`: Contains the scraped and processed Wikipedia content.
- `label_data.json`: Contains labels for evaluating summaries which i creat my self.

## Note

This project assumes that the `label_data.json` file exists and contains appropriate reference summaries for ROUGE score calculation. Make sure this file is present in the same directory as the Python scripts.