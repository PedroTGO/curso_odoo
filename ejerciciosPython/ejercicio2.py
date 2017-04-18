INVENTORY={
'gold':500,
'pouch':['flint','twine','gemstone'],
'backpack':['xylophone','dagger','bedroll','bread loaf']
}
print INVENTORY['backpack']
INVENTORY['backpack'].sort()
print INVENTORY['backpack']
INVENTORY['backpack'].remove('dagger')

print INVENTORY['backpack']
