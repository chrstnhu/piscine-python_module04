from FileLoader import FileLoader

loader = FileLoader()
data = loader.load("../data/adult_data1.csv")
# Output
# Loading dataset of dimensions 32561 x 15

loader.display(data, 12)
# Output
#     age          workclass    fnlwgt ...    hours-per-week  native-country salary
# 0   39              State-gov 77516 ...                 40  United-States <=50K
# 1   50       Self-emp-not-inc 83311 ...                 13  United-States <=50K
# 2   38                Private 215646 ...                40  United-States <=50K
# 3   53                Private 234721 ...                40  United-States <=50K
# 4   28                Private 338409 ...                40           Cuba <=50K
# 5   37                Private 284582 ...                40  United-States <=50K
# 6   49                Private 160187 ...                16        Jamaica <=50K
# 7   52       Self-emp-not-inc 209642 ...                45  United-States  >50K
# 8   31                Private 45781 ...                 50  United-States  >50K
# 9   42                Private 159449 ...                40  United-States  >50K
# 10  37                Private 280464 ...                80  United-States  >50K
# 11  30              State-gov 141297 ...                40          India  >50K

# [12 rows x 15 columns]