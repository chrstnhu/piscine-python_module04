import pandas as pd

def youngest_fellah(data, year):
    df = pd.DataFrame(data)

    # Check the column names
    result = df.loc[df['Year'] == year]
    # print(f"Find same year: {result}")

    # Filter the feminine and masculine athletes
    feminine = result.loc[result['Sex'] == 'F']
    masculine = result.loc[result['Sex'] == 'M']
    # print(f"Find feminine: {feminine}")
    # print(f"Find masculine {masculine}")

    # Get the youngest athletes
    youngest_f = feminine['Age'].min()
    youngest_m = masculine['Age'].min()
    # print(f"Find youngest feminine: {youngest_f}")
    # print(f"Find youngest masculine: {youngest_m}")

    return {'f': youngest_f, 'm': youngest_m}