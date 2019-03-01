# RiFlowTH (CodeR)

# 1 Equal to Black pixel
# 0 Equal to White pixel (empty)

# Model of numbers
model_0 = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
model_1 = [[1, 1, 1], [0, 0, 1], [0, 0, 1]]
modelLists = [model_0, model_1]

template1 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
test_template = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

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
                template1[x][y] += buf1[x][y]
    read(template1)

# Takenote: 10 = 0, 13 = 1

# Main work
train(modelLists)