from flask import Flask, jsonify
import json
import re

app = Flask(__name__)

URL_PATTERN = re.compile(r"^https?://", re.IGNORECASE)

def load_datasets():
    with open("all_datasets.json", "r", encoding="utf-8") as f:
        raw = json.load(f)

    #list to store cleaned data
    cleaned = []

    for item in raw:
        metadata = item.get("metadata", {})
        summary = metadata.get("summary", {})
        access = metadata.get("accessibility", {}).get("access", {})

        title = summary.get("title")
        description = summary.get("description") or summary.get("abstract")
        access_service_category = access.get("accessServiceCategory")
        access_rights = access.get("accessRights")

        access_rights_link = (
            access_rights
            if isinstance(access_rights, str) and URL_PATTERN.match(access_rights)
            else None
        )

        cleaned.append({
            "title": title or "No title provided",
            "description": description or "No description provided",
            "accessServiceCategory": access_service_category or "Not provided",
            "accessRights": access_rights_link
        })

    return cleaned

@app.route("/api/datasets", methods=["GET"])
def get_datasets():
    return jsonify(load_datasets())

if __name__ == "__main__":
    app.run(debug=True)
