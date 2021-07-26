# 1). Initialize a set
emptySet = set()
dataScientist = {'Python', 'R', 'SQL', 'Git', 'Tableau', 'SAS'}
dataEngineer = {'Python', 'Java', 'Scala', 'Git', 'SQL', 'Hadoop'}
print(f"data scientist:\n {dataScientist}")
print(f"data engineer:\n {dataEngineer}")

# 2). Add or remove values from sets
graphic_designer = {'InDesign', 'Photoshop', 'Acrobat', 'Premiere', 'Bridge'}
graphic_designer.add('Illustrator')  # only possible with one addition, not with lists
graphic_designer.discard("Premiere")

# 3). Looping through all the elements in a set
for skill in dataScientist:
    print(skill)
