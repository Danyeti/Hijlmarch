class Player:

    """ This class contains everything required for the player to function. """

    def __init__(self, health, inventory, equipped_item):
        self.health = health
        self.inventory = inventory
        self.equipped_item = equipped_item

    
    def add_item_to_inventory(self, item):
        """ Adds an item to the Player object inventory. """
        self.inventory.append(item)

    
    def equip_item(self, item):
        """ Equips an item for the player. """
        self.equipped_item = item

    
    def increase_health(self, amount_to_add_health):
        """ Increases the health of the player. """
        self.health += amount_to_add_health
    
    
    def decrease_health(self, amount_to_sub_health):
        """ Decrease the health of the player. """
        self.health -= amount_to_sub_health

