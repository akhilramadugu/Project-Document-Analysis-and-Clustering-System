import math

# Sample term weights for a document
term_weights = {'apple': 3, 'banana': 5, 'orange': 2}

# Compute the L2 norm
norm = math.sqrt(sum(w ** 2 for w in term_weights.values()))

# Normalize the term weights
for term in term_weights:
    term_weights[term] /= norm

# Print the normalized term weights
print(term_weights)
