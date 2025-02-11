import json
import os
import tkinter as tk
from tkinter import messagebox, simpledialog

CONTACTS_FILE = "contacts.json"

def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    return []

def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

def add_contact():
    name = simpledialog.askstring("Add Contact", "Enter Store Name:")
    phone = simpledialog.askstring("Add Contact", "Enter Phone Number:")
    email = simpledialog.askstring("Add Contact", "Enter Email Address:")
    address = simpledialog.askstring("Add Contact", "Enter Address:")
    
    if name and phone:
        contacts = load_contacts()
        contacts.append({"name": name, "phone": phone, "email": email, "address": address})
        save_contacts(contacts)
        messagebox.showinfo("Success", "Contact added successfully!")
    else:
        messagebox.showerror("Error", "Name and Phone Number are required!")

def view_contacts():
    contacts = load_contacts()
    contact_list.delete(0, tk.END)
    for contact in contacts:
        contact_list.insert(tk.END, f"{contact['name']} - {contact['phone']}")

def search_contact():
    query = simpledialog.askstring("Search Contact", "Enter Name or Phone Number:")
    contacts = load_contacts()
    contact_list.delete(0, tk.END)
    for contact in contacts:
        if query.lower() in contact['name'].lower() or query in contact['phone']:
            contact_list.insert(tk.END, f"{contact['name']} - {contact['phone']}")

def update_contact():
    query = simpledialog.askstring("Update Contact", "Enter Name of Contact to Update:")
    contacts = load_contacts()
    for contact in contacts:
        if contact['name'].lower() == query.lower():
            contact['phone'] = simpledialog.askstring("Update Contact", "Enter New Phone Number:", initialvalue=contact['phone'])
            contact['email'] = simpledialog.askstring("Update Contact", "Enter New Email:", initialvalue=contact['email'])
            contact['address'] = simpledialog.askstring("Update Contact", "Enter New Address:", initialvalue=contact['address'])
            save_contacts(contacts)
            messagebox.showinfo("Success", "Contact updated successfully!")
            return
    messagebox.showerror("Error", "Contact not found!")

def delete_contact():
    query = simpledialog.askstring("Delete Contact", "Enter Name of Contact to Delete:")
    contacts = load_contacts()
    updated_contacts = [contact for contact in contacts if contact['name'].lower() != query.lower()]
    
    if len(updated_contacts) < len(contacts):
        save_contacts(updated_contacts)
        messagebox.showinfo("Success", "Contact deleted successfully!")
        view_contacts()
    else:
        messagebox.showerror("Error", "Contact not found!")

# GUI Setup
root = tk.Tk()
root.title("Contact Management System")
root.geometry("400x400")

contact_list = tk.Listbox(root, width=50)
contact_list.pack(pady=10)

btn_add = tk.Button(root, text="Add Contact", command=add_contact, bg="lightblue", fg="black")
btn_add.pack()\

btn_view = tk.Button(root, text="View Contacts", command=view_contacts, bg="lightgreen", fg="black")
btn_view.pack()\

btn_search = tk.Button(root, text="Search Contact", command=search_contact, bg="lightyellow", fg="black")
btn_search.pack()\
                   
btn_update = tk.Button(root, text="Update Contact", command=update_contact, bg="lightcoral", fg="black")
btn_update.pack()\

btn_delete = tk.Button(root, text="Delete Contact", command=delete_contact, bg="lightgray", fg="black")
btn_delete.pack()\

root.mainloop()
