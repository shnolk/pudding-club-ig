import random
import string
import sys

# ---- ONLY OBJECTS THAT CAN BE PLURAL with S at the end ----
objectsThingsList = {
    "song": ["music-1"],
    "tree": ["tree-1", "tree-2", "tree-3", "tree-4", "palms-1"],
    "purse": ["purse-1"],
    "bear": ["bear-1"],
    "hand": ["hand-1", "hand-2"],
    "flower": ["flower-1", "flower-2"],
    "sun" : ["sun-1"],
    "gumball" : ["sprite-1"],
    "quiz" : ["puzzle-1"],
    "recycle bin": ["recycle"],
    "cart": ["cart-1"],
    "spirit": ["buddy-1","buddy-2","buddy-3","buddy-4","buddy-5","buddy-6","buddy-7",
                "buddy-8","buddy-9","buddy-10","buddy-11","buddy-12","buddy-13","buddy-14",
                "buddy-15", "buddy-16", "buddy-17"],
    "emotions": ["emoji-1","emoji-2","emoji-3","emoji-4","emoji-5","emoji-6","emoji-7",
                "emoji-8"],
    "scissor" : ["scissor-1"],
    "skippie" : ["computer-1"],
    "banana" : ["computer-2", "banana-1"],
    "green apple" : ["buddy-16"],
    "boot" : ["boot-1"],
    "shoe" : ["sneaker-1"],
    "sneaker" : ["sneaker-1"]
}

objectsPersonsList = {
    "runner": ["woman-1"],
    "pedestrian": ["man-1"],
    "sully": ["man-2"],
    "lillian": ["face-1"],
    "roderick": ["face-5"],
    "rob": ["face-3"],
    "eddie": ["face-4"],
    "sprite": ["buddy-1","buddy-2","buddy-3","buddy-4","buddy-5","buddy-6","buddy-7",
                "buddy-8","buddy-9","buddy-10","buddy-11","buddy-12","buddy-13","buddy-14",
                "buddy-15", "buddy-16", "buddy-17"],
    "sloppie":["buddy-16"],
    "grump":["buddy-17"]
}

objectsPlacesList = {
    # be able to select like objects if plural query
    "forest": ["tree-1", "tree-2", "tree-3", "tree-4"],
    "house": ["house-1"],
    "texas": ["texas"],
    "new york" : ["new-york"],
    "garden": ["flower-1", "flower-2"],
    "desert": ["sun-1"],
    "mountain": ["mountain-1","mountain-2","mountain-3"],
    "vortex" : ["vortex"],
    "store" : ["cart-1", "boot-1", "purse-1", "sneaker-1"],
    "beach" : ["palms-1"],
    "temple": ["buddy-1","buddy-2","buddy-3","buddy-4","buddy-5","buddy-6","buddy-7",
                "buddy-8","buddy-9","buddy-10","buddy-11","buddy-12","buddy-13","buddy-14",
                "buddy-15"],
    "party" : ["emoji-1","emoji-2","emoji-3","emoji-4","emoji-5","emoji-6","emoji-7",
                "emoji-8"],
    "ice castle" : ["buddy-17"],
    "shoe store" : ["boot-1", "sneaker-1"]

}

def importTextList(filePath):
    s = open(filePath, "r")
    m = s.readlines()
    l = []
    for k in range(0, len(m) - 1):
        x = m[k]
        z = len(x)
        a = x[:z - 1]
        l.append(a)
    l.append(m[k + 1])
    return l


def generateNouns(nounType = random.choice(["person", "place", "thing"])):
    # pick noun(s)
    # pick actions "in a"
    # pick a place

    # for each noun
    pluralMax = 4
    objectsPrimaryList = []
    nounString = ""
    isPlural = random.choice([True, False])
    if nounType is "person":
        noun = random.sample(list(objectsPersonsList), 1)[0]
        if isPlural:
            for i in range(random.randint(2, pluralMax)):
                objectsPrimaryList.append(
                    objectsPersonsList[noun][
                        random.randint(0, len(objectsPersonsList[noun])-1)
                        ]
                )
        else:
            objectsPrimaryList.append(
                objectsPersonsList[noun][
                    random.randint(0, len(objectsPersonsList[noun])-1)
                    ]
            )
    if nounType is "place":
        noun = random.sample(list(objectsPlacesList), 1)[0]
        if isPlural:
               for i in range(random.randint(2, pluralMax)):
                objectsPrimaryList.append(
                    objectsPlacesList[noun][
                        random.randint(0, len(objectsPlacesList[noun])-1)
                        ]
                )
        else:
            objectsPrimaryList.append(
                objectsPlacesList[noun][
                    random.randint(0, len(objectsPlacesList[noun])-1)
                    ]
            )
    if nounType is "thing":
        noun = random.sample(list(objectsThingsList), 1)[0]
        if isPlural:
            for i in range(random.randint(2, pluralMax)):
                objectsPrimaryList.append(
                    objectsThingsList[noun][
                        random.randint(0, len(objectsThingsList[noun])-1)
                        ]
                )
        else:
            objectsPrimaryList.append(
                objectsThingsList[noun][
                    random.randint(0, len(objectsThingsList[noun])-1)
                    ]
            )
    nounString += noun
    if isPlural:
        nounString += "s"

    return [nounString, objectsPrimaryList]

def generateFromList(list):
    return random.choice(list)

def generateScene():
    objectsPrimaryList = []
    finalString = ""

    nounCount = random.randint(1,3)
    prepositions = importTextList("positional-prepositions.txt")
    verbs = importTextList("verbs.txt")
    while nounCount > 0:
        # Start sentence
        if finalString != "": finalString += " "
        finalString += random.choice(("","the "))
        # generate nouns
        nouns = generateNouns(random.choice(["person","thing"]))
        # is it plural?
        # if nouns[0][-1] == "s":
        finalString += nouns[0]
        # add nouns to objects primary list
        for i in nouns[1]:
            objectsPrimaryList.append(i)
        if nounCount <= 1:
            break
        else:
            finalString += " " + generateFromList(prepositions)
        nounCount -= 1

    # verbs
    finalString += " " + generateFromList(verbs)
    # prepositions
    finalString += " " + generateFromList(prepositions)
    # place
    place = generateNouns("place")
    finalString += " " + place[0]
    # add nouns to objects primary list
    for i in place[1]:
        objectsPrimaryList.append(i)

    return [finalString, objectsPrimaryList]


print(generateScene())
