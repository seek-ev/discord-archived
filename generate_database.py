import json
from modules.database import initFirebase, setVal, checkExist

initFirebase()
# Generate example application
if not checkExist("/config/application", "applicationExample"):
    setVal("/config/application", "applicationExample", "Example Application...")
# Generate Developer Role fields
if not checkExist("/config/roles/developer", "id"):
    setVal("/config/roles/developer", "id", "role_id")
# Generate Reaction Roles fields
j = [
    {
        "message": "123",
        "reactions": [
            {"emoji": "434444919", "role": "developer"},
            {"emoji": "5553216725", "role": "12313382829"},
        ],
    }
]
if not checkExist("/config/", "reaction_roles"):
    setVal(
        "/config/roles/",
        "reaction_roles",
        j,
    )
