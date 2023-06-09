########################################################################################################################################################################################################################################################################################################################################################################################################################

## 1
## Verifying that the data is available:
# f = open("Kilo/fakeSmokerData.csv")
# print(f.readlines())
# f.close()

########################################################################################################################################################################################################################################################################################################################################################################################################################

## 2
## Setup
import pandas as pd
fakeSmokerData = pd.read_csv("Kilo/fakeSmokerData.csv")
print()

########################################################################################################################################################################################################################################################################################################################################################################################################################

## 3
## Try this:
# print(fakeSmokerData)
# print()

# ########################################################################################################################################################################################################################################################################################################################################################################################################################

# ## 4
# ## This is just the index of those who started smoking before age 20.

# print(fakeSmokerData["ageStartedSmoking"] < 20)
# print()

# ########################################################################################################################################################################################################################################################################################################################################################################################################################

# ## 5
# ## If we want to see the rest of the data for those rows, we do this.
# print(fakeSmokerData[fakeSmokerData["ageStartedSmoking"] < 20])
# print()

# ########################################################################################################################################################################################################################################################################################################################################################################################################################

## 6
## We can see how many people strted smoking before 20:
# below20 = fakeSmokerData[fakeSmokerData["ageStartedSmoking"] < 20]
# print(len(below20))
# print()

########################################################################################################################################################################################################################################################################################################################################################################################################################

## 7
## Print the rows of people who are currently older than 50.

# print(fakeSmokerData[fakeSmokerData["currentAge"] > 50])
# print()

########################################################################################################################################################################################################################################################################################################################################################################################################################

## 8
## Try this:

# print(fakeSmokerData.sort_values("currentAge"))
# print()

########################################################################################################################################################################################################################################################################################################################################################################################################################

## 9
## Try this:

# print(fakeSmokerData.sort_values("ageStartedSmoking"))
# print()

########################################################################################################################################################################################################################################################################################################################################################################################################################

###### Appendix
###### For those who are interested:
###### This is the code that I used to generate the fake smoker data.
# import random
# for unused in range(20):
#     st = random.randrange(18, 23)
#     curr = random.randrange(20, 65)
#     g = random.choice("FM")
#     print(f"{st},{curr},{g}")

########################################################################################################################################################################################################################################################################################################################################################################################################################
########################################################################################################################################################################################################################################################################################################################################################################################################################