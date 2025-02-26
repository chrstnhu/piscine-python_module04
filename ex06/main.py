from FileLoader import FileLoader

loader = FileLoader()
data = loader.load('../data/athlete_events.csv')
# Output
# Loading dataset of dimensions 271116 x 15

from MyPlotLib import MyPlotLib

features = ['Weight', 'Height']
mpl = MyPlotLib()
# mpl.histogram(data, features)
mpl.density(data, features)
