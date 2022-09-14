# Dandelion Constants

# dandelionStemMin should be at minimum 1, but recommend setting it to 2 or 3
DandelionStemMin = 2

# dandelionStemMax should be set to at least dandelionStemMin + 1, and would highly discourage setting this to above 10 or 12.
DandelionStemMax = 6

# Determines how many peers to send a dandelion message to.
# In an ideal case, this should be set to 1, but for redundancy we recommend setting it to 2 in case a peer is malicious or malfunctioning.
numberOfStemPeers = 2

# Highly recommend stemReductionMin be 1, but it could be set to 0
StemReductionMin = 0

# stemReductionMax could be the same value as stemReductionMin if you want a more deterministic, but recommend it be set to stemReductionMin + 1
StemReductionMax = 1