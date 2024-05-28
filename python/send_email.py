import os
import requests
import json
import time

from dotenv import load_dotenv


load_dotenv()


if __name__ == "__main__":
    
    hostname = "https://api.notification.canada.ca/"
    
    data = {
           "email_address": "stephen.astels@cds-snc.ca",
            "template_id": os.getenv("TEMPLATE_ID"),
            "personalisation": {
                "var": "api demo!",
            },
    }
    
    response = requests.post(
        f"{hostname}/v2/notifications/email",
        headers={"Authorization": f"ApiKey {os.getenv('API_KEY')}"},
        json=data,
    )


    # Always check the response
    # print(f"responds status code: {response.status_code}")
    # print(json.dumps(response.json(), indent=4, sort_keys=True))











    # Check status - better to setup a callback though
    # status = requests.get(
    #     response.json()["uri"],
    #     headers={"Authorization": f"ApiKey-v1 {os.getenv('API_KEY')}"},
    # )
    # print("\n\nEmail Status")
    # print(f"responds status code: {status.status_code}")
    # print(json.dumps(status.json(), indent=4, sort_keys=True))

