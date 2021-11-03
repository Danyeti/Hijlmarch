class Player:

    """ This class contains everything required for the player to function. 
        
        :param health: The amount of health that the player has remaining.
        :param inventory: The items that the player is holding onto.
        :param equipped_item: The item the player is holding onto.
        
        :type health: Integer
        :type inventory: List
        :type equipped_item: Item

        Example
        >> non_existing_class = Item()
        >> player_obj = Player(100, [], non_exisiting_class)
    """


    def __init__(self, health, inventory, equipped_item):
        self.health = health
        self.inventory = inventory
        self.equipped_item = equipped_item

    
    def add_item_to_inventory(self, item):
        """ Adds an item to the Player object inventory.
            
            :param item: The item in question.

            :type item: Item
        """
        self.inventory.append(item)

    
    def equip_item(self, item):
        """ Equips an item for the player. 

            :param item: The item that the player wants to equip.

            :type item: Item
        """
        self.equipped_item = item

    
    def increase_health(self, amount_to_add_health):
        """ Increases the health of the player by amount_to_add_health.

            :type amount_to_add_health: Integer
        """
        self.health += amount_to_add_health
    
    
    def decrease_health(self, amount_to_subtract_health):
        """ Decrease the health of the player by amount_to_subtract_health.

            :type amount_to_subtract_health: Integer 
        """
        self.health -= amount_to_sub_health



