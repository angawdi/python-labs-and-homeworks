spices_needed = set({"salt", "pepper", "ginger", "oregano", "paprika", "basil", "curry powder", "cumin", "cayenne", "lemon pepper", "chili powder", "nutmeg", "cinammon", "star anise", "garlic salt", "coriander", "cardamom", "thyme"})

spices_onhand = ['cumin', 'nutmeg', 'salt', 'cumin', 'star anise', 'salt', 'basil', 'nutmeg', 'cumin', 'paprika', 'curry powder', 'pepper', 'curry powder', 'curry powder', 'cayenne', 'cumin', 'star anise', 'star anise', 'curry powder', 'salt', 'salt', 'cardamom', 'cayenne', 'star anise', 'chili powder', 'curry powder', 'thyme', 'thyme', 'cayenne', 'nutmeg', 'basil', 'star anise', 'chili powder', 'oregano', 'coriander', 'nutmeg', 'chili powder', 'coriander', 'paprika', 'pepper', 'thyme', 'nutmeg', 'paprika', 'cayenne', 'basil', 'cinammon', 'curry powder', 'cardamom', 'star anise', 'pepper', 'salt', 'curry powder', 'thyme', 'cardamom', 'salt', 'pepper', 'paprika', 'salt', 'cinammon', 'cumin', 'curry powder', 'cardamom', 'cumin', 'cardamom', 'oregano', 'cardamom', 'pepper', 'star anise', 'pepper', 'cayenne', 'chili powder', 'cardamom', 'nutmeg', 'pepper', 'cardamom', 'curry powder', 'thyme', 'basil', 'nutmeg', 'coriander', 'paprika', 'curry powder', 'cayenne', 'cumin', 'nutmeg', 'paprika', 'star anise', 'thyme', 'curry powder', 'cardamom', 'oregano', 'basil', 'cinammon', 'oregano', 'coriander', 'curry powder', 'cumin', 'thyme', 'pepper', 'thyme', 'cardamom', 'cayenne', 'chili powder', 'basil', 'pepper', 'cumin', 'thyme', 'cardamom', 'star anise', 'cayenne', 'cinammon', 'cinammon', 'cinammon', 'cardamom', 'curry powder', 'curry powder', 'pepper', 'chili powder', 'pepper', 'cinammon', 'cardamom', 'basil', 'thyme', 'cinammon', 'cumin', 'nutmeg', 'cinammon', 'cayenne', 'cardamom', 'nutmeg', 'cardamom', 'paprika', 'cumin', 'cayenne', 'chili powder', 'cinammon', 'cumin', 'star anise', 'cardamom', 'thyme', 'basil', 'paprika', 'basil', 'oregano', 'cardamom', 'pepper', 'oregano', 'nutmeg', 'nutmeg', 'salt', 'basil', 'cayenne', 'oregano', 'star anise', 'star anise', 'oregano', 'salt', 'pepper', 'cinammon', 'basil', 'salt', 'cardamom', 'cayenne', 'oregano', 'cinammon', 'pepper', 'cumin', 'thyme', 'thyme', 'oregano', 'oregano', 'star anise', 'paprika', 'thyme', 'cinammon', 'cinammon', 'oregano', 'star anise', 'oregano', 'chili powder', 'cayenne', 'oregano', 'cumin', 'paprika', 'nutmeg', 'star anise', 'coriander', 'star anise', 'nutmeg', 'chili powder', 'star anise', 'paprika', 'salt', 'salt', 'cayenne', 'curry powder', 'thyme', 'oregano', 'curry powder', 'curry powder']

# Convert the huge list into a set to remove all duplicates
spice_list = set(spices_onhand)

# Use the difference between the sets to find out what you are shopping for
spices_to_buy = spices_needed - spice_list

print('Go shopping for:', spices_to_buy)
