# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 02:33:34 2017

@author: Jordy
"""

guests = ['Jimmy', 'Sarah', 'Doe']

def show_guests():
    print("These are all the people invited over:" + str(guests[:]))
    make_party()

def new_guest():
    new_guest = input("Who would you like to add? ")
    if new_guest in guests:
        print("Not valid")
        make_party()
    else:
        guests.append(new_guest)
        print(new_guest + " has been added to the party")
        print("The party now consists of " + str(guests))
        make_party()
    
def del_guest():
    bad_guest = input("Who would you like to remove? ")
    if bad_guest in guests:
        guests.remove(bad_guest)
        print(bad_guest + " has been removed from the party")
        print("The party now consists of " + str(guests))
        make_party()
    else: 
        print("Not valid")
        make_party()
    
def inv_guests():
    for name in guests:
        print("Dear " + str(name) + " Please Arrive Around 9PM")
    make_party()
        
def make_party():
    choice = input("\nParty Sort App\nWhat would you like to do? ")
    if str(choice) == "show":
        show_guests()
    if str(choice) == "inv":
        inv_guests()
    if str(choice) == "del":
        del_guest()
    if str(choice) == "new":
        new_guest()
    else:
        print("not an option")
        make_party()
        
make_party()