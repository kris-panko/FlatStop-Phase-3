# FlatStop: phase-3-project

FlatStop is a CLI application where users can access a store, where they can buy and sell video games.

## Functionality:

/LOGIN AND ACCOUNT/

- User will be able to create a new account or login to an existing one.
- Username, password, and age constraints are mandatory to create an account.
- User can choose between buying and selling games.
- User can view all information associated with the account. From this screen, users can update account fields (username, password, and age) and delete their account.
- Users will have three attempts to login with a correct password before being kicked out.
- MEMBERSHIP: Users can become a member of the store which will give them discounts on bought games, and additional money back on sold games.

/BUY/

- Shows the users the name, price, and rating for all available games.
- Users can add multiple games to their shopping cart and buy more than one game per transaction.
- Age filtering for games - users can search for games and only see games based on checking games' age constraint against a game's rating.
- Buying an inventory item updates or deletes it from stock and persists (if it gets to 0, it disappears from SQL database).
- Inventory discounts for used items bought from users.

/SELL/

- Users can sell games back to the store at a consigned rate.
- Users can attempt to haggle with store staff for additional money back.
- When a user sells an item, it is added to the store inventory database.

/STRETCH GOALS/

- STORE CREDIT: Users can recieve store credit for games sold to the store.
- CHAT: Users can chat with our CLI cashier!
- HAGGLE: Users can attempt to bargain for more credits when selling games.

## CRUD Actions

- GAME CREATE: When a user sells an item, it is added to the store inventory.
- USER CREATE: When a user creates an account, it is added to the store's user database.
- GAME READ: Shows all available inventory and can see name, price, rating.
- USER READ: User can view the username, password, and age affiliated with their account.
- GAME UPDATE/DELETE: Buying an inventory item updates or deletes it from stock and persists (if the inventory is 0, it is deleted from SQL database.)
- USER UPDATE/DELETE: Users can update information associated with their account and delete their account.

<!-- UPDATE THESE IMAGES EXCEPT KANBAN-->

## User Stories Decision Tree:

![Screenshot_2023-09-22_104331](https://github.com/kris-panko/phase-3-project/assets/136921157/22e1741b-00d4-4bea-be7e-d3685782a8f4)

## Object Relationship

![image](https://github.com/kris-panko/flatStop/assets/106281281/04344984-a17a-4959-8a51-8733c3a88aba)

## Kanban:

![Screenshot 2023-09-22 at 1 44 12 PM](https://github.com/kris-panko/phase-3-project/assets/136921157/ca44ce0b-efcf-477b-80ae-4a62b77d9501)

---

## Resources

- [Markdown Cheat Sheet](https://www.markdownguide.org/cheat-sheet/)
