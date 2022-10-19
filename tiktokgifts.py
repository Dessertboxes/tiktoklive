import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from TikTokLive import TikTokLiveClient
from TikTokLive.types.events import GiftEvent

# Fetch the service account key JSON file contents
cred = credentials.Certificate('dessertboxes-20373-firebase-adminsdk-bu07i-27a3587b6f.json')
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://dessertboxes-20373-default-rtdb.firebaseio.com"
})

ref = db.reference('boxes')

client = TikTokLiveClient("@woainimsy")

print("All set here!")

@client.on("gift")
async def on_gift(event: GiftEvent):
    # If it's type 1 and the streak is over
    if event.gift.gift_type == 1:
        if event.gift.repeat_end == 1:
            (ref.set({'gift': f"{event.user.uniqueId} : {event.gift.repeat_count} : {event.gift.extended_gift.name}"})), print(f"{event.user.uniqueId} sent {event.gift.repeat_count}x \"{event.gift.extended_gift.name}\"")

    # It's not type 1, which means it can't have a streak & is automatically over
    elif event.gift.gift_type != 1:
        (ref.set({'gift': f"{event.user.uniqueId} : {event.gift.repeat_count} : {event.gift.extended_gift.name}"})), print(f"{event.user.uniqueId} sent \"{event.gift.extended_gift.name}\"")

client.run()