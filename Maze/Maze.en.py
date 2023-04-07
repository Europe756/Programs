#!/bin/python3

def showInstructions():
    #show a main menu and the possible commands
    print('''
RPG Game (Labyrinth)
========

Find the key and the potion, then try to escape to the garden.
Don't let the monsters eat you!

Connections:
  [room]->([direction], [direction])

Commands:
  go [w(Forward),a(Left),s(Backward),d(Right),q(Down),e(Up)]
  take [item]
  help
''')

def showState():
  #show the current state of the player
  print('---------------------------')
  print('You are in the room: ' + currentRoom)
  #show the current inventory
  print('Inventory : ' + str(inventory))
  #Display an item if there is one in the room
  if "item" in room[currentRoom]:
      print('You see an ' + room[currentRoom]['item'])
  print("---------------------------")

#The inventory is empty at startup
inventory = []
gone = 0
#A dictionary connects a room with other rooms
room = {
#Ground Floor
            'Corridor (Left, Right)' : {
                  's' : 'Door (Backward, Forward)',
                  'a' : 'Hallway (Left, Right)',
                  'd' : 'Staircase (Ground Floor)(Up, Left)'},        
                
            'Hallway (Left, Right)' : {
                  'd' : 'Corridor (Left, Right)',
                  'a' : 'Dining Room (Right, Backward)',
                  'item' : 'Monster'},        
                
            'Dining Room (Right, Backward)' : {
                  'd' : 'Hallway (Left, Right)',
                  's' : 'Garden (Forward)',
                  'item' : 'Potion'},
                
            'Garden (Forward)' : {
                  'w' : 'Dining Room (Right, Backward)'},
                
            'Staircase (Ground Floor)(Up, Left)' : {
                  'a' : 'Corridor (Left, Right)',
                  'e' : 'Staircase (Upstairs)(Down, Left)'},
            
            'Ladder (Ground Floor)(Down, Forward)' : {
                  'w' : 'Door (Backward, Forward)',
                  'q' : 'Ladder (Basement)(Up, Right)',
                  'item' : 'Monster'},
            
            'Door (Backward, Forward)' : {
                  'w' : 'Corridor (Left, Right)',
                  's' : 'Ladder (Ground Floor)(Down, Forward)'},

#Upstairs                
            'Staircase (Upstairs)(Down, Left)' : {
                  'q' : 'Staircase (Ground Floor)(Up, Left)',
                  'a' : 'Hallway 1 (Left, Right, Backward)'},
            
            'Hallway 1 (Left, Right, Backward)' : {
                  'a' : 'Hallway 2 (Left, Right, Forward, Backward)',
                  's' : 'Hallway 4 (Left, Right, Forward)',
                  'd' : 'Staircase (Upstairs)(Down, Left)'},
                        
            'Hallway 2 (Left, Right, Forward, Backward)' : {
                  'a' : 'Hallway 3 (Left, Right, Forward)',
                  'd' : 'Hallway 1 (Left, Right, Backward)',
                  's' : 'Hallway 5 (Left, Right, Backward)',
                  'w' : 'Cloakroom (Backward, Forward)'},
            
            
            'Cloakroom (Backward, Forward)' : {
                  'w' : 'Balcony (Backward)',
                  's' : 'Hallway 2 (Left, Right, Forward, Backward)',
                  'item' : 'Monster'},
            
            'Balcony (Backward)' : {
                  's' : 'Cloakroom (Backward, Forward)',
                  'item' : 'Mysterious Shard 1/3'},
            
            'Hallway 3 (Left, Right, Forward)' : {
                  'a' : 'Hallway 4 (Left, Right, Forward)' ,
                  'd' : 'Hallway 2 (Left, Right, Forward, Backward)',
                  'w' : 'Hallway 6 (Left, Right, Backward)'},
            
            'Hallway 4 (Left, Right, Forward)' : {
                  'a' : 'Hallway 5 (Left, Right, Backward)',
                  'd' : 'Hallway 3 (Left, Right, Forward)',
                  'w' : 'Hallway 2 (Left, Right, Forward, Backward)'},
            
            'Hallway 5 (Left, Right, Backward)' : {
                  'a' : 'Hallway 6 (Left, Right, Backward)',
                  'd' : 'Hallway 4 (Left, Right, Forward)',
                  's' : 'Attic (Forward)'},
            
            'Attic (Forward)' : {
                  'w' : 'Hallway 5 (Left, Right, Backward)',
                  'item' : 'Sword'},
            
            'Hallway 6 (Left, Right, Backward)' : {
                  'a' : 'Hallway 7 (Left, Right, Forward)',
                  'd' : 'Hallway 5 (Left, Right, Backward)',
                  's' : 'Vault (Forward)'},
            
            'Vault (Forward)' : {
                  'w' : 'Hallway 6 (Left, Right, Backward)',
                  'item' : 'Monster'},
            
            'Hallway 7 (Left, Right, Forward)' : {
                  'd' : 'Hallway 6 (Left, Right, Backward)',
                  'a' : 'Bedroom (Right)',
                  'w' : 'Hallway 3 (Left, Right, Forward)'},
            
            'Bedroom (Right)' : {
                  'd' : 'Hallway 7 (Left, Right, Forward)',
                  'item' : 'Key'},

#basement            
            'Ladder (Basement)(Up, Right)' : {
                  'e' : 'Ladder (Ground Floor)(Down, Forward)',
                  'd' : 'Basement (Left, Right)'},
            
            'Basement (Left, Right)' : {
                  'a' : 'Ladder (Basement)(Up, Right)',
                  'd' : 'Bicycle Garage (Left)',
                  'item' : 'Mysterious Shard 2/3'},
            
            'Bicycle Garage (Left)' : {
                  'a' : 'Basement (Left, Right)'},
#???
            '§$%%&$%@ (Up)' : { 'e' : 'Corridor (Left, Right)'},
         }

#At the start the player is in the Corridor
currentRoom = 'Corridor (Left, Right)'

showInstructions()

#Eternal loop

while True:

  showState()

  #Wait for the 'next move' of the player
  #.split() splits it into an array
  #For example, if you type 'go to east', you will get the following list:
  #['goto','east']
  move = ''
  while move == '':  
    move = input('>')
    
  move = move.split()
#please do not change - in German the item names start with uppercase letter

  #if the input starts with 'gehenach
  if move[0] == 'go':
    #check if the player can go where he wants to go
    if move[1] in room[currentRoom]:
      #make the new room the current room
      currentRoom = room[currentRoom][move[1]]
    #There is no door (connection) to the new room
    else:
      print("You can't go that way!")
  elif move[0] == 'help':
      showInstructions()
  #If the typed begins with 'nimm'.
  elif move[0] == 'take' :
    #If the room contains an item, and you want to take exactly this item
    if move[1] == 'Monster':
        print('The monster is too heavy!')
    elif "item" in room[currentRoom] and move[1] in room[currentRoom]['item']:
      #add the item to the player's inventory
      inventory += [move[1]]
      #show a helpful message
      print(move[1] + ' has been taken!')
      #delete the item from the room
      del room[currentRoom]['item']
    #Otherwise, the item is not present and cannot be taken.
    else:
      #Tell the player that he can't take this item.
      print("You can't take " + move[1] + '!')
      
  #The player loses when he enters a room with a monster
  if 'item' in room[currentRoom] and 'Monster' in room[currentRoom]['item'] and 'Sword' in inventory:
    print('You made the monster faint, but it will wake up soon!')
  elif "item" in room[currentRoom] and 'Monster' in room[currentRoom]['item']:  
    print('You have been eaten by a hungry monster... GAME OVER!')
    currentRoom = 'Corridor (Left, Right)'
    inventory =[]

#The player wins if he reaches the garden with the key and the potion.
  if currentRoom == 'Garden (Forward)' and 'Key' in inventory and 'Potion' in inventory:
    showState()
    print('You escaped from the house... YOU WON!')
    break
  
  if currentRoom == 'Door (backward, forward)' and not 'Key' in inventory: 
    print("You need a key")
    current
    Room = 'Corridor (Left, Right)'
    
if 'Mysterious Shard 1/3' in inventory and 'Mysterious Shard 2/3' in inventory and 'Mysterious Shard 3/3' in inventory and not gone == 1:
    print('All Shards have been found! You have discovered a new room!')
    print('You can only come here once, if you leave there is no way back')
    print('"e" is the only exit')
    print('You have to find out the other ways yourself')
    currentRoom = '§$%%&$%@ (Up)'
    gone = 1
