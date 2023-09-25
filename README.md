# FlatStop: phase-3-project

FlatStop is a CLI program where users can log in to a store, buy, and sell video games, accessories, and video game consoles. 

## Functionality:

/LOGIN/

* User will be able to create a new account
* Username and age constraints mandatory
* User can choose between buy and sell

/BUY/
* Select between games, consoles, and accessories
* Shows all available inventory, name, price, rating
* Age filtering for games - only see games based on checking age constraint against game rating
* Buying an inventory item updates or deletes it from stock and persists (if it gets to 0, it disappears from SQL database)
* Inventory discounts for used items

/SELL/
* Users can sell items either for money or store credit 
* Users will receive more store credit than cash for items
* When a user sells an item, it is added to inventory

## CRUD Actions
* CREATE: When a user sells an item, it is added to the store inventory
* READ: Shows all available inventory and can see name, price, rating
* UPDATE/DELETE: Buying an inventory item updates or deletes it from stock and persists (if the inventory is 0, it is deleted from SQL database)

## User Stories Decision Tree: 
![Screenshot_2023-09-22_104331](https://github.com/kris-panko/phase-3-project/assets/136921157/22e1741b-00d4-4bea-be7e-d3685782a8f4)

## Object Relationship
![image](https://github.com/kris-panko/flatStop/assets/106281281/04344984-a17a-4959-8a51-8733c3a88aba)

## Kanban:
![Screenshot 2023-09-22 at 1 44 12 PM](https://github.com/kris-panko/phase-3-project/assets/136921157/ca44ce0b-efcf-477b-80ae-4a62b77d9501)


---

## Resources

- [Markdown Cheat Sheet](https://www.markdownguide.org/cheat-sheet/)
