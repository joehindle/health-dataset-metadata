# Dataset Metadata API

A simple Flask API that reads dataset metadata from `all_datasets.json` and returns the required fields as JSON.

## Features

This API exposes the following information for each dataset:

- title
- description
- accessServiceCategory
- accessRights

## Project Structure

Place the files in the same folder like this:

project-folder/
├── app.py
├── all_datasets.json
└── README.md

## Requirements

You need:

- Python 3
- Flask

## Installation

Open a terminal in the project folder and install Flask:

pip install flask

## How to Run

Run the Flask app with:

python app.py

Once the server starts, open this URL in your browser:

http://127.0.0.1:5000/api/datasets

## API Endpoint

### GET /api/datasets

Returns a JSON array of dataset objects.

## Example Response

[
  {
    "title": "Cystic Fibrosis Patient Microbiology Cultures",
    "description": "The UK CF Registry is a centralised database of all 60 CF centres across the UK...",
    "accessServiceCategory": "Varies based on project",
    "accessRights": "https://www.cysticfibrosis.org.uk/the-work-we-do/uk-cf-registry/apply-for-data-from-the-uk-cf-registry"
  }
]

## Notes

- `app.py` and `all_datasets.json` must be in the same directory.
- The API reads the JSON file, extracts the required fields, and returns them in JSON format.
- If the server does not start, check that Flask is installed correctly.
- If you get a file error, make sure `all_datasets.json` is in the same folder as `app.py`.

## Summary

This project is a lightweight Flask web application that exposes selected dataset metadata through a JSON API endpoint.
