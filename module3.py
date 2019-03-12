
import mypackage.messenger
print(mypackage)

m = mypackage.messenger.Messenger()
print(m.name)

print(m.send_message("Привет").time)

mypackage.messenger.Messenger.send_message("Привет2")
