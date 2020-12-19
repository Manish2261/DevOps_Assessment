# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 16:09:00 2020

@author: Lenovo
"""

import os
class Contact:
    def __init__(self,name,email,phone):
        self.name=name
        self.email=email
        self.phone=phone
        
    def __str__(self):
        return "Name:{0}\nEmail address:{1}\nPhone:{2}".format(self.name,self.email,self.phone)
        

def add_contact():
    list_contact =[]
    try:
        contact=get_contact_info_from_user()
        list_contact.append(contact)
        print("\nContact Added")
        print("\n" + str(list_contact[0]))
    except  KeyboardInterrupt:
        print("\nContact not added")
  
def get_contact_info_from_user():
    try:
        contact_name=input("Enter contact name\n")
        contact_email=input("Enter contact email\n")
        contact_phone=input("Enter contact phone number\n")
        contact=Contact(contact_name,contact_email,contact_phone)
        return contact
    except EOFError as e:
        #print "You entered end of file. Contact not added"
        raise e
    except KeyboardInterrupt as e:
        #print "Keyboard interrupt. Contact not added"
        raise e

print("Please provide the suitable choice for the operation")
print("a --> For Adding Contact")
print("q --> Quit the Application")

while True:
    choice=input("Enter your choice\n")
    if choice == 'q':
        break
    elif(choice=='a'):
        add_contact()
    
    else:
        print("Incorrect choice. Need to enter the choice again")