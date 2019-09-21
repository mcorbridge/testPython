
# Import classes from your brand new package
from animals.mammals.mammals import Mammals
from animals.birds.accipitriformes import Order
from animals.birds.falconiformes import Order
from animals.utils.taxonomyTools import Tools
 
accipitriformes = Order()
accipitriformes.printFamilies()

falconiformes = Order()
falconSpecies = falconiformes.getSpecies()

searchItem = "thigh"

print("search for: " + searchItem)
speciesSearchResult = Tools.searchSpecies(searchItem,falconSpecies)


print("sort by " + Tools.COMMON_NAME + " name, " + Tools.DESC)
Tools.iterateSpecies(Tools.sortSpecies(speciesSearchResult,Tools.COMMON_NAME))