import pandas as pd

def youngest_fellah(data, year):
    df = pd.DataFrame(data)

    # Check the column names
    result = df.loc[df['Year'] == year]
    # print(f"Find same year: {result}")

    # Filter the feminine and masculine athletes
    feminine = result.loc[result['Sex'] == 'F']
    # print(f"Find feminine: {feminine}")
    masculine = result.loc[result['Sex'] == 'M']
    # print(f"Find masculine {masculine}")

    # Get the youngest athletes
    youngest_f = feminine['Age'].min()
    # print(f"Find youngest feminine: {youngest_f}")
    youngest_m = masculine['Age'].min()
    # print(f"Find youngest masculine: {youngest_m}")

    return {'f': youngest_f, 'm': youngest_m}