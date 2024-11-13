import os
import requests
import json
from dotenv import load_dotenv


load_dotenv()


if __name__ == "__main__":
    
    hostname = "https://api.notification.canada.ca/"
    
    status = requests.get(
        f"{hostname}/v2/notifications?include_jobs=true",  # <-- undocumented param needed
        headers={"Authorization": f"ApiKey-v1 {os.getenv('API_KEY')}"},
    )

    print(f"responds status code: {status.status_code}")
    print(json.dumps(status.json(), indent=4, sort_keys=True))
