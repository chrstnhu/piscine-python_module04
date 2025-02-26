from FileLoader import FileLoader

loader = FileLoader()
data = loader.load('../data/athlete_events.csv')
# Output
# Loading dataset of dimensions 271116 x 15

from SpatioTemporalData import SpatioTemporalData
sp = SpatioTemporalData(data)

result = sp.where(1896)
print(f"Year(1896): {result}")
# Output
# [’Athina’]

result = sp.where(2016)
print(f"Year(2016): {result}")
# Output
# [’Rio de Janeiro’]

result = sp.when('Athina')
print(f"City(Athina): {result}")
# Output
# [2004, 1906, 1896]

result = sp.when('Paris')
print(f"City(Paris): {result}")
# Output
# [1900, 1924]