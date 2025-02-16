Make sure you have Python 3.7+ and pip installed
sudo apt install python3-pip -y
pip install requests==2.28.2
pip install --upgrade hubspot-api-client
pip install python-dotenv


Batch Limits
Batch operations are limited to 100 records at a time.  >>> https://developers.hubspot.com/docs/guides/api/crm/objects/contacts#limits

Rate Limits
100 / private app requests every 10 seconds (lowest tier) >>> https://developers.hubspot.com/docs/guides/apps/api-usage/usage-details#request-limits
