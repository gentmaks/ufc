import requests as req

URL = "https://mma-fights-api-production.up.railway.app/"

def get_events():
    response = req.get(URL)
    events = response.json()['data']
    ufc_events = [
       event for event in events
        if event['title'].strip().lower().startswith('ufc')
    ]
    return ufc_events

def get_events_titles():
    ufc_events = get_events()
    return [event['title'] for event in ufc_events]

print((get_events_titles()))