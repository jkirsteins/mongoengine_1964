import datetime
import mongoengine as me
from pymongo.read_preferences import ReadPreference

class TestModel(me.DynamicDocument):
    meta = {
        "auto_create_index": False,
        "index_background": True,
        "indexes": [
            "application"
        ],
    }

    application = me.StringField()

    risk_inputs = me.DictField()

    date_created = me.DateTimeField(required=True)

now = datetime.datetime.utcnow()

me.connect("testdb", host="localhost", port=27017, replicaset="rs", read_preference=ReadPreference.SECONDARY)


while True: # Looping, because it's frequent but not 100%
    for obj in TestModel.objects().read_preference(ReadPreference.PRIMARY):
        obj.delete()

    # Fails even though we specify read pref PRIMARY (and the object gets created)
    #
    # If we specify ReadPreference.PRIMARY when connecting to the replicaset,
    # then it does not fail.
    new_object = TestModel.objects(application="test").read_preference(ReadPreference.PRIMARY).upsert_one(set_on_insert__date_created=now)
    if new_object is None:
        raise Exception("Didn't get an object")

    print("Got object: ")
    for obj in TestModel.objects().read_preference(ReadPreference.PRIMARY):
        print("   - %s" % obj.date_created)
