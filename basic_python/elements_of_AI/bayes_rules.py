# The Bayes rule
# We will not go too far into the details of probability calculus and all
# the ways in which it can be used in various AI applications, but we will
# discuss one very important formula.We will do this because this particular
# formula is both simple and elegant as well as incredibly powerful. It can be
# used to weigh conflicting pieces of evidence in medicine, in a court of law,
# and in many (if not all) scientific disciplines. The formula is called the Bayes
# rule (or the Bayes formula).

# Likelihood ratio
# The above ratio (nine times as high chances of clouds on a rainy day compared to a
# rainless day) is called the likelihood ratio. More generally, the
# likelihood ratio is the probability of the observation in case the event of interest
# (in the above, rain), divided by the probability of the observation in case of no event
# (in the above, no rain). Please read the previous sentence a few times. It may look a little
# intimidating, but it’s not impossible to digest if you just focus carefully. We will walk you
# through the steps in detail, just don’t lose your nerve. We’re almost there.

# So we concluded that on a cloudy morning, we have: likelihood ratio = (9/10) / (1/10) = 9
# The mighty Bayes rule for converting prior odds into posterior odds is – ta-daa! – as follows:
# posterior odds = likelihood ratio × prior odds

# Consider mammographic screening for breast cancer. Using made up percentages for the sake of
# simplifying the numbers, let’s assume that 5 in 100 women have breast cancer. Suppose that if
# a person has breast cancer, then the mammograph test will find it 80 times out of 100. When the
# test comes out suggesting that breast cancer is present, we say that the result is positive,
# although of course there is nothing positive about this for the person being tested
# (a technical way of saying this is that the sensitivity of the test is 80%).

# The test may also fail in the other direction, namely to indicate breast cancer when none exists.
# This is called a false positive finding. Suppose that if the person being tested actually doesn’t
# have breast cancer, the chances that the test nevertheless comes out positive are 10 in 100.
# (In technical terms, we would say that the specificity of the test is 90%.)

# Based on the above probabilities, you are able to calculate the likelihood ratio.
# You’ll find use for it in the next exercise. If you forgot how the likelihood ratio is calculated,
# you may wish to check the terminology box earlier in this section and revisit the rain example.

# Note: You can use the above diagram with stick figures to validate that your result is in the ballpark
# (about right) but note that diagram isn’t quite precise. Out of the 95 women who don’t have cancer
# (the gray figures in the top panel), about nine and a half are expected to get a (false) positive result.
# The remaining 85 and a half are expected to get a (true) negative result. We didn’t want to be so cruel
# as to cut people – even stick figures – in half, so we used 9 and 86 as an approximation.

# Consider the above breast cancer scenario. An average woman takes the mammograph test and gets a
# positive test result suggesting breast cancer. What do you think are the odds that she has breast
# cancer given the observation that the test is positive?

# First, use your intuition without applying the Bayes rule, and write down on a piece of paper
# (not in the answer box below) what you think the chances of having breast cancer are after a positive test result.
# The intuitive answer will not be a part of your answer. It will be just for your own information.

# Next, calculate the posterior odds for her having breast cancer using the Bayes rule. This will be your answer.

# Hints:
# Start by calculating the prior odds.
# Determine the probability of the observation in case of the event (cancer).
# Determine the probability of the observation in case of no event (no cancer).
# Obtain the likelihood ratio as the ratio of the above two probabilities.
# Finally, multiply the prior odds by the likelihood ratio.
# Enter the posterior odds as your solution below. Give the answer in the form xx:yy where xx and yy are numbers,
# without simplifying the expression even if both sides have a common factor.

# Correct. The prior odds describe the situation before getting the test result.
# Since five out of 100 women have breast cancer, there is on the average five women with
# breast cancer for every 95 women without breast cancer, and therefore, the prior odds are 5:95.
# The likelihood ratio is the probability of a positive result in case of cancer divided by the
# probability of a positive result in case of no cancer. With the above numbers, this is given by 80/100
# divided by 10/100, which is 8. The Bayes rule now gives the posterior odds of breast cancer given the
# positive test result: posterior odds = 8 × 5:95 = 40:95, which is the correct answer. So despite the
# positive test result, the odds are actually against the person having breast cancer: among the women
# who are tested positive, there are on the average 40 women with breast cancer for every 95 women
# without breast cancer. Note: If we would like to express the chances of breast cancer given the
# positive test result as a probability (even though this is not what the exercise asked for), we
# would consider the 40 cases with cancer and the 95 cases without cancer together, and calculate
# what portion of the total 40 + 95 = 135 individuals have cancer. This gives the result 40 out of 135,
# or about 30%. This is much higher than the prevalence of breast cancer, 5 in 100, or 5%, but still the
# chances are that the person has no cancer. If you compare the solution to your intuitive answer, they
# tend to be quite different for most people. This demonstrates how poorly suited out intuition is for
# handling uncertain and conflicting information.