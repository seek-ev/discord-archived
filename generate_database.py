from modules.database import initFirebase, setVal

initFirebase()
# Generate example application
setVal("/config/application", "applicationExample", "Example Application...")
# Generate Developer Role fields
setVal("/config/developer", "id", "role_id")
