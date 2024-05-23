import os
import requests
import json
from dotenv import load_dotenv


load_dotenv()


if __name__ == "__main__":
    
    hostname = "https://api.notification.canada.ca/"
    
    data = {
        "name": "bulk name",
        "template_id": os.getenv("TEMPLATE_ID"),
        "rows": [
            ["email address", "var"],
            ["stephen.astels@cds-snc.ca", "test 1"],
            ["stephen.astels@cds-snc.ca", "test 2"]
        ],
    }
    
    response = requests.post(
        f"{hostname}/v2/notifications/bulk",
        headers={"Authorization": f"ApiKey-v1 {os.getenv('API_KEY')}"},
        json=data,
    )

    print(f"Response status code: {response.status_code}")
    print(json.dumps(response.json(), indent=4, sort_keys=True))
