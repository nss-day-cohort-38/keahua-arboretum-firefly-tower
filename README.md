![Keahua Landscape](./keahua.jpeg)

# Keahua Arboretum

You and your friends have decided to connect with the earth again and abandon your reliance on technology and urban vices. You have decided to move to Hawaii and join the land management team for the Keahua Arboretum.

You have met with other foresters and land managers and have decided on the animals and plants below to focus on growing and maintaining for the arboretum.

A group project by:

- [Sofia Candiani](https://github.com/sncandiani)
- [Matthew Kroeger](https://github.com/mKroogz)
- [Matt Crook](https://github.com/MattCrook)
- [Keith Potempa](https://github.com/keithrpotempa)

## 
1. Clone the repository
1. `cd` to the project directory
1. Run the command `pip install -r requirements.txt`
1. Run the command `python index.py` to start application 

## Features

* Add habitats such as mountain, grassland, river, etc. 
* Add plants and animals to habitats. 
* Extensive checks performed through duck typing to assure users can only add plants and animals that meet all specific qualifications of a habitat.
* Many ways to navigate back to the main menu if the user has not selected a habitat.
* View report of the plants and animals within each habitat.
* Secret Option 7 which allows users to fill the application with tester data for easier initial navigation.


## Keahua Inventory and Land Lifeline Electronic Repository (KILLER)

Fancy web applications are so 2018. Command line applications provide a much more hands-on, personal, bespoke, artisinal experience when managing an arboretum like Keahua. Therefore, even though you are casting off your digital personas to lead a life connected with the land, you still want to use your hard-earned skills as developers to make management of the land as efficient as possible.

### Main Menu

When the user first executes KILLER, they should be welcomed to the system and be presented with the following menu.

```sh
 +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+
 |  K  e  a  h  u  a    A  r  b  o  r  e  t  u  m  |
 +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+

1. Annex Biome
2. Release New Animal
3. Feed Animal
4. Cultivate New Plant
5. Show Arboretum Report
6. Exit
> _
```

### Biome Annex Sub-Menu

If the user chooses option 1, then the following menu should be displayed

```sh
1. Mountain
2. Swamp
3. Grassland
4. Forest
5. River

Choose a KILLER habitat
> _
```

When the user makes a choice, a new instance of that type of biome should be added to list on the arboretum object that contains those biomes.

### Animal Menu

If the user chooses 2 from the main menu, then she should see the following menu, with the animals listed.

```html
1. Gold Dust Day Gecko
2. River Dolphin
3. Nene Goose
4. Kīkākapu
5. Pueo
6. 'Ulae
7. Ope'ape'a
8. Happy-Face Spider

Choose animal to release
> _
```

When the user enters in what to buy, then the user will be prompted to define the age and name of the animal. Next, all of the locations in which the animals can be stored will be displayed along with the current number of animals for each location.

```sh
1. Mountain [id] (2 animals)
2. Forest [id] (4 animals)
2. Forest [id] (0 animals)

Choose environment to release *specified animal name* the *general animal type*
> _
```

### Animal Feeding Menu

If the user chooses 3 from the main menu, then they should see the following menu, with the animals listed.

```html
1. Gold Dust Day Gecko
2. River Dolphin
3. Nene Goose
4. Kīkākapu
5. Pueo
6. 'Ulae
7. Ope'ape'a
8. Happy-Face Spider

Choose animal to feed
> _
```
When the user chooses an animal, another prompt shoulder appear asking the user to choose which of their animals they'd like to feed. 
```
River the River Dolphin
Choose which individual to feed 
> _
```
When the user chooses their animal, another menu should appear showing the specific food that you have in stock to feed it.

```html
1. trout
2. mackarel
3. salmon
4. sardine

Choose what to feed it
> _
```

Once the user chooses a food item, she should be presented with a message.

```html
River the River Dolphin ate salmon for a meal.

Press enter key to continue...
```

### Plant Cultivation Menu

If the user chooses 4 from the main menu, then she should see the following menu, with the plants listed.

```html
1. Mountain Apple Tree
2. Silversword
3. Rainbow Eucalyptus Tree
4. Blue Jade Vine

Choose plant to cultivate
> _
```

When the user makes a choice, then display all of the locations in which the plants can be planted. The current number of plant rows should be displayed for each location.

```sh
1. Grassland (5 plants)
2. Swamp (2 plants)
3. Swamp (9 plants)
4. Swamp (0 plants)

Where would you like to plant the Sun Jade Vine?
> _
```

If the user chose to place them in a location that they did not belong they'd receive an error message.

```html
There are no appropriate environments for that plant. Press ENTER to choose a new plant.
> _
```

### Arboretum Report Menu

Choosing this option will list all existing biomes, and then list all animals and plants in that biome. Only display the first 8 characters of the id in the report.

```html
River [157b2efe]
    River Dolphin (133619c4)

Mountain [bdf33960]
    Ope'ape'a (bf9ad976)
    Ope'ape'a (f9dd0afa)
    Mountain Apple Tree (h91d77a0)


Press any key to continue...
```
### Planning Process
[Sketchboard](https://sketchboard.me/rB63PJFAWKFL#/)