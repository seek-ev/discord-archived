from modules.database import initFirebase, setVal, checkExist

initFirebase()
# Generate example application
if not checkExist("/config/application", "applicationExample"):
    setVal("/config/application", "applicationExample", "Example Application...")
# Generate Developer Role fields
if not checkExist("/config/developer", "id"):
    setVal("/config/developer", "id", "role_id")
