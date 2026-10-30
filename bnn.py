
# Simple Binary Neural Network (BNN)

def bnn_neuron(inputs, weights, threshold):

    # Step 1: XNOR comparison
    matches = []

    for i in range(len(inputs)):
        if inputs[i] == weights[i]:
            matches.append(1)
        else:
            matches.append(0)

    # Step 2: Count matching bits
    popcount = sum(matches)

    # Step 3: Threshold comparison
    output = 1 if popcount >= threshold else 0

    return matches, popcount, output


# Input data
inputs = "1011010010110101"

# Neuron weights
weights = "1010010010010111"

# Threshold
threshold = 10

# Run neuron
matches, count, result = bnn_neuron(
    inputs, weights, threshold
)

# Display results
print("BINARY NEURAL NETWORK")
print("---------------------")

print("Input:       ", inputs)
print("Weights:     ", weights)
print("XNOR Output: ", ''.join(map(str, matches)))

print("Popcount:    ", count)
print("Threshold:   ", threshold)

print("Neuron Output:", result)

if result == 1:
    print("Neuron ACTIVATED")
else:
    print("Neuron NOT ACTIVATED")
