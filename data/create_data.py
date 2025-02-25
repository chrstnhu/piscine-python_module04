import csv
import random

# Exemple de données possibles pour chaque colonne
ages = [random.randint(18, 90) for _ in range(32561)]
workclasses = ['Private', 'Self-emp-not-inc', 'State-gov', 'Federal-gov', 'Local-gov', 'Without-pay', 'Never-worked']
educations = ['Bachelors', 'Masters', 'HS-grad', 'Assoc-acdm', 'Assoc-voc', '11th', '10th', '7th-8th', 'Some-college']
marital_statuses = ['Married-civ-spouse', 'Never-married', 'Divorced', 'Separated', 'Widowed']
occupations = ['Tech-support', 'Craft-repair', 'Other-service', 'Sales', 'Exec-managerial', 'Prof-specialty']
relationships = ['Husband', 'Not-in-family', 'Own-child', 'Unmarried', 'Wife']
races = ['White', 'Asian-Pac-Islander', 'Amer-Indian-Eskimo', 'Other', 'Black']
sexes = ['Male', 'Female']
native_countries = ['United-States', 'Cuba', 'Jamaica', 'India', 'Mexico', 'Germany', 'Canada']
salaries = ['<=50K', '>50K']

# Créer le fichier CSV
with open('adult_data1.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    
    # Écrire l'en-tête
    writer.writerow(['age', 'workclass', 'fnlwgt', 'education', 'education-num', 'marital-status', 'occupation', 'relationship', 'race', 'sex', 'capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'salary'])
    
    # Écrire les données
    for _ in range(32561):
        row = [
            random.choice(ages),
            random.choice(workclasses),
            random.randint(15000, 500000),
            random.choice(educations),
            random.randint(1, 16),  # education-num : entre 1 et 16
            random.choice(marital_statuses),
            random.choice(occupations),
            random.choice(relationships),
            random.choice(races),
            random.choice(sexes),
            random.randint(0, 99999),  # capital-gain
            random.randint(0, 9999),   # capital-loss
            random.randint(1, 99),     # hours-per-week
            random.choice(native_countries),
            random.choice(salaries)
        ]
        writer.writerow(row)

print("Fichier CSV 'adult_data.csv' généré avec succès.")
