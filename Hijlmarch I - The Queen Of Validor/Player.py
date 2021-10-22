class Player: 

    def init(self, Health: int, Inventory: list, ):
        self.Health = Health
        self.Inventory = Inventory
        self.EquippedItem
        return self
    
    def AddItemToInventory(self, Item):
        self.Inventory.append(Item)
    
    def EquipItem(self, Item):
        self.EquippedItem = Item
    
    def IncreaseHealth(self, AmountToAddToHealth: int):
        self.Health += AmountToAddToHealth
    
    def DecreaseHealth(self, AmountToSubtractFromHealth: int):
        self.Health -= AmountToSubtractFromHealth
