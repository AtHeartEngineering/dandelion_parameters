# Dandelion Constants

# GossipsubStemMin should be at minimum 1, but recommend setting it to 2 or 3
GossipsubStemMin = 3

# GossipsubStemMax should be set to at least GossipsubStemMin + 1, and would highly discourage setting this to above 10 or 12.
GossipsubStemMax = 8

# Determines how many peers to send a dandelion message to.
# In an ideal case, this should be set to 1, but for redundancy we recommend setting it to 2 in case a peer is malicious or malfunctioning.
numberOfStemPeers = 2

# Highly recommend stemReductionMin be 1, but it could be set to 0
StemReductionMin = 1

# stemReductionMax could be the same value as stemReductionMin if you want a more deterministic, but recommend it be set to stemReductionMin + 1
StemReductionMax = 2