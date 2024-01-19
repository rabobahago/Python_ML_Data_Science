# In the previous section, we discussed search and its application
# where there is perfect information – such as in games like chess.
# However, in the real world things are rarely so clear cut.

# Probability
# One of the reasons why modern AI methods actually work in real-world
# problems – as opposed to most of the earlier “good old-fashioned"
# methods in the 1960-1980s – is their ability to deal with uncertainty.

# The history of dealing with uncertainty
# The history of AI has seen various competing paradigms for handling uncertain
# and imprecise information. For example, you may have heard of fuzzy logic.
# Fuzzy logic was for a while a contender for the best approach to handle uncertain
# and imprecise information and used in many customer-applications such as washing machines
# where the machine could detect the dirtiness (a matter of degrees, not only dirty or clean)
# and adjust the program accordingly.
# However, probability has turned out to be the best approach for reasoning under uncertainty,
# and almost all current AI applications are based, to at least some degree, on probabilities.

# Odds
# Probably the easiest way to represent uncertainty is through odds. They make it particularly
# easy to update beliefs when more information becomes available (we will return to this in the next section).

# Before we proceed any further, we should make sure you are comfortable with doing basic manipulations
# on ratios (or fractions). As you probably recall, fractions are numbers like 3/4 or 21/365. We will
# need to multiply and divide such things, so it’s good to refresh these operations if you feel unsure
# about them. A compact presentation for those who just need a quick reminder is Wikibooks: Multiplying Fractions.
# Another fun animated presentation of the basic operations is Math is Fun: Using Rational Numbers. Feel free to
# consult your favorite source if necessary.

# By odds, we mean an expression like 3:1 (three to one), which means that we expect that for every three cases of
# an outcome, for example winning a bet, there is one case of the opposite outcome, not winning the bet. (In gambling
# terms, the odds are usually given from the bookmakers point of view, so 3:1 usually means that your chances of winning
# are 1:3.) The other way to express the same would be to say that the chances of winning are 3/4 (three in four).
# These are called natural frequencies since they involve only whole numbers. With whole numbers, it is easy to
# imagine, for example, four people out of whom, three have brown eyes. Or four days out of which it rains on three
# (if you’re in Helsinki).