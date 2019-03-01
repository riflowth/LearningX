# RiFlowTH (CodeR)

# 1 Equal to Black pixel
# 0 Equal to White pixel (empty)

# Model of numbers
number1 = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
number2 = [[1, 1, 1], [0, 0, 1], [0, 0, 1]]
modelLists = [number1, number2]

template = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# -- Functions -- #
# Print model
def read(model):
    for child in model:
        print(child)

# Train model (Weight calculate)
def train(models):
    for buf1 in models:
        for x in range(len(buf1)):
            for y in range(len(buf1[0])):
                template[x][y] += buf1[x][y]
    read(template)
    print(weightsum())

# Calculate weight sum of the template
def weightsum():
    buf = 0
    for powerChild in template:
        for subChild in powerChild:
            buf += subChild
    return buf

# Takenote: 10 = 0, 13 = 1

# Main work
train(modelLists)