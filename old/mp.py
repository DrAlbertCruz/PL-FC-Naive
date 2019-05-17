# Modus ponens:
#	a => b, a
#	________
#	b
# That is, if a implies b, and a is true, then b is true. This lab is designed 
# to make a simple modus ponens function and highlight some Python mechanics.

# Modus Ponens. Inputs:
#	- KB. A disjunction of literals and complex sentences connected by 
#		conjunctions specificed as follows:
#		("ibex",("elk","moose"),"ape") 
#		Would be read as:
#		ibex OR elk AND moose OR ape
#	- Clause. An implication specified by:
#		(antecedent, consequent)
#		For example:
#		("ibex","civet")
#		Is read as ibex => civet. 
#	The goal of Modus Ponens is to return to consequent if the antecedent
#	is true in the KB, otherwise return false. Note that the KB represented
#	as a disjunction of conjunctions is a strict requirement and this may
#	not be generalizable.
# This is the start of a function. Blocks are defined by indentation.
def mp( KB, clause ):
	"""Python provides a interface for providing documentation of a function. You do this by placing a comment with three quotation marks at the start of the function. The following command: >>> mp.__doc__, in the Python command line interface will display this text. This comment is read literally and will display escape tokens, rather than cause new lines and carriage returns."""
	
