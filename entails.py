# Simple example to determine if something is entailed

# Preliminaries:
# Facts *must* be a single character
# Rules are horn clauses
# Rules are represented as a 2-tuple with the first element being th
#   ... antecedent and the second element being the consequent.
# Rules clauses are strings
# Example:
#   ("ac","b") indicates A and C imply B
# KB is string of implied variables
# Rules are an array of two-tuples

# The most naive implementation will use a lot of Python mechanics to implement
# the following:
#   Keep poping rules from the set of rules
#       Check if it entailed something, if so put it in KB
#   Break if there are no changes after looking at the whole set of rules

# Knowledgebase is stored as a string. Implied facts/clauses are stored as a 
# char in the string. Thus, "ad" indicates that a and d are true in the KB
KB = "a"
# Rules are represented as a 2-tuple with the first element being the antecedent# and the second element being the consequent.
# Example:
#   ("ac","b") indicates A and C imply B
# There is an assumption that a consequent contains only one clause
rules = [("a","b"),("b","c"),("c","d"),("d","a")] # Initial rule set
count = 1   
# Keep track of the number of times we have iterated over the whole rule set

while True:
    # Set the flag that there have been no changes to false
    changes = False
    print( "Starting iteration " + str(count) )
    # For each rule in the set of rules ...
    for p in rules:
        antecedent, consequent = p
        print( "Considering rule " + antecedent + " implies " + consequent )
        # Determine if all chars in antecedent are also in KB
        anteInKB = True # Flag for the antecedent in the KB
        for q in antecedent:    # q is a char
            if q not in KB:    # KB is a string
                anteInKB = False    # Flag as false, all clauses must be implied
        # If it passes the above, then antecedent should be entailed
        if anteInKB and consequent not in KB:
            KB = KB + consequent
            changes = True
            print( "Antecedent is in KB, " + consequent + " is implied, KB is now " + KB )
        elif anteInKB and consequent in KB:
            print( "Consequent is implied, but was already in KB")
        else:
            print( "Consequent is not implied" )

    if not changes:
        print( "No more changes. KB is: " + KB )
        break

    count = count + 1
