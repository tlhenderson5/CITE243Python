#Initial inventory
stuff = {'arrow': 12, 'gold coin': 42, 'rope': 1, 'torch': 6, 'dagger': 1}

def displayInventory(inventory):
    print('Inventory:')
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + str(k))
        item_total += v
    print('Total number of items: ' + str(item_total))

#displat inventory of stuff
displayInventory(stuff)

print('\n')

def display_inventory(inventory):
    print("Inventory:")
    total_items = 0
    for item, count in inventory.items():
        print(f"{count} {item}")
        total_items += count
    print("Total number of items:", total_items)


def add_to_inventory(inventory, added_items):
    for item in added_items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1
    return inventory


# Initial inventory
inv = {'gold coin': 42, 'rope': 1}

# Loot from the dragon
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

# Update inventory with dragon loot
inv = add_to_inventory(inv, dragon_loot)

# Display updated inventory
display_inventory(inv)
