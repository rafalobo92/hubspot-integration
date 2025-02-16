# Contact Sync Service

## Requirements
Ensure you have **Python 3.7+** and **pip** installed. You can install the required dependencies using the following commands:

```sh
sudo apt install python3-pip -y
pip install requests==2.28.2
pip install --upgrade hubspot-api-client
pip install python-dotenv
```

## Batch Limits
HubSpot batch operations are limited to **100 records at a time**. For more details, check the official documentation:
[HubSpot API Batch Limits](https://developers.hubspot.com/docs/guides/api/crm/objects/contacts#limits)

## Rate Limits
- **100 private app requests every 10 seconds** (lowest tier).
- If the rate limit is reached, the system implements an **exponential backoff retry mechanism**.

For more details, refer to the official HubSpot API rate limits:
[HubSpot API Rate Limits](https://developers.hubspot.com/docs/guides/apps/api-usage/usage-details#request-limits)
