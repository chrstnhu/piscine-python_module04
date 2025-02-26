from FileLoader import FileLoader

loader = FileLoader()
data = loader.load('../data/athlete_events.csv')
# Output
# Loading dataset of dimensions 271116 x 15

def print_prettier(result):
    print(f"========== China ===========")
    for key, value in result.items():
        print(f"{key}")
        for k, v in value.items():
            print(f"  {k}: {v}")
        print()

from HowManyMedalsByCountry import how_many_medals_by_country

result = how_many_medals_by_country(data, 'China')
print_prettier(result)
