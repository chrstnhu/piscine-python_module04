from FileLoader import FileLoader
from YoungestFellah import youngest_fellah

loader = FileLoader()
data = loader.load("../data/athlete_events.csv")
# Output
# Loading dataset of dimensions 271116 x 15

# from YoungestFellah import youngest_fellah
result = youngest_fellah(data, 2004)
print(result)
# Output
# {’f’: 13.0, ’m’: 14.0}