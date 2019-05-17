# A better example of entailment in propositional logic with forward chaining. Based on the example given in Russel and Norvig
# AI 2e in Pg. 219, Figure 7.14.

### INPUTS
# Agenda. A list of symbols known to be true.
agenda = ["barks","hoots","looks","swims","quacks"]
# Goal. The proposition that we need to determine
goal = "duck"
# Rules. A set of propositional horn clauses. Ordered.
rules = [(["looks","swims","quacks"],"duck"),(["barks"],"dog"),(["hoots","flies"],"owl")]
# Inferred. A list of symbols, initially empty.
inferred = []
# Count. A table indexed by rule initially the number of premises. Ordered, corresponds to rules.
count = [ 3, 1, 2 ]
# There is most likely a python way to do this procedurally

### LOCAL VARIABLES
# Count. Indexed by clause. Initially the number of premises.

# Passing a list as an expression will return true if the list has elements in it
while agenda:
	# p <- POP(agenda)
	p = agenda.pop(0) # I guess pop first element?

	# unless inferred[p] do
	if p not in inferred:
		# inferred[p] <- true
		inferred.append( p )

		# for each horn clause c in whose premise p appears do
		for c in range(0,len(rules)):
			premise, consequent = rules[c]
			if p in premise:
				# decrement count[c]
				count[c] -= 1
				# if count[c] is zero
				if count[c] == 0:
					# if the consequent is the goal return true
					if consequent == goal:
						print( "Goal " + goal + " is true" )
						break
					# Otherwise push the consequent into agenda
					agenda.append( consequent )							

print( "Goal " + goal + " is false" )
