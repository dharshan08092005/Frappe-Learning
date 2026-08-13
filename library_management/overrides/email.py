import frappe

def send(self, sender, recipient, msg):
    self.update_status("Sending")

def get_sender_details():
    print("Custom get_sender_details called")
    return "VP", "kdfibpgnpng@gmail.com"


