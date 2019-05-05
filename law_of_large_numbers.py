#Law of Large Numbers

#The purpose of this particular file is to get us accustomed to some
#Python basics.  And to review some math, because yay math!

#This is great!  To start with, a single comment line is denoted using #

"""
This is a multi-line comment.
Just remember to close the comment.
"""

#Best practices say you should just use multiple of these comments though!
#I would highly recommend not using multi-line comments.
#Technically the interpreter still reads and parses the comment.
#This causes a ton of problems!

#Anaconda comes with essentially every package/library we will need.  I use 
#package/library interchangeably to try and make this more comfortable if you know
#other languages.  
#Package (preferred name) is a collection of Modules.  Much like libraries elsewhere.
#Modules are a collection of functions we can use (essentially).
#Are there more subtle details?  Of course!  Are they important?  Not really now.
#
#Just because we have all of the packages does not mean they are all loaded.
#We need to "load" or import packages to use.  Alternatively, if we will need
#multiple packages we should probably just import what we need.  Let us look further.
#
#First off, if we were missing a package we would need to download it.  The exact
#details of that can be for another discussion, but the easiest way is probably
#using conda install "package name" in the anaconda command line.
#If the package is not installing then it may not be suitable for the current
#conda environment, but we will not have that problem with the things I post!

#Second, we look at the wording and the impact that wording has.
#(Quick aside, a list is just essentially a vector that can have mixed data types).
#We will be making a list of numbers and storing them in memory, hence the mention.

#Importing an entire package, literally everything:
#import numpy

#That imports the entire package numpy, all of the modules, EVERYTHING.
#Numpy is enormous, and certainly has overlapping names with other packages.
#Also, we may still need to refer to numpy by name.  A more convenient way to 
#import numpy is:

import numpy as np

#If we run that line then we have numpy, great!  Now we can use it to call
#randn(i) which will produce i numbers at random.

# list1 = randn(1000)    #This is commented out so we can run the code as one block.

#Yep, we got an error.  That is because python does not know what the heck 
#we are talking about.  There could be a billion randn!  How do we know
#which one?  The one in the "random" module!

# list1 = random.randn(1000)    #This is commented out so we can run the code as one block.

#WHAT THE HECK!!  Yeah, what if there is more than one random module?  We
#want the one in the numpy package!  So, we add that on.

list1 = np.random.randn(1000) #Remember we use np because that's how we imported numpy.

#Also of note, when you type np. Spyder gives you options.  When you pick 
#random it gives you more options.  Also, yay it worked!

#Instead we could have just imported the entire random module to have at hand.
#We can do that using this code:

from numpy import random

#Great!  So now we try again.

# list2 = randn(1000)    #This is commented out so we can run the code as one block.

#Again, there could be more than one randn!  How does Python know?

list2 = random.randn(1000)

#Great!  But what if we want something a bit less large?
#What if we only want to use randn?  Well, that is easy enough!
#We can import ONLY randn.  We do so as such:

from numpy.random import randn

#Great!  Third list please:

list3 = randn(1000)

#Beautiful!  Now we know how to make our function work exactly as intended.
#I know it may seem complicated, but the more we do this the easier it will be.
#No one has EVERY function in every package in every library/module memorized.
#The more commonly used ones will become second nature.  Others are easily
#located in documentation and/or internet searches.  I promise!

#Something interesting to notice, you did not need to declare the variable as
#being a list.  Just like in R, Python figures out your variable type.  If you
#are experienced with other languages, this is a nice change!

#Let us celebrate by defining six variables to count for us.  We will use 
#these to do some bookkeeping work in a bit.

s0 = 0 #Why s0?  Details below!
s1 = 0
s2 = 0
s3 = 0
s4 = 0
s5 = 0

#Something to notice if you are coming from R.  Indices start at 0.  Watch:

test_list = ["mistakes", "are", "inevitable"]

#Two things.  First, that's sort of an Endgame quote, because I love that movie.
#Second, notice naming convenion.  R is fine with ".".  Python most definitely
#is not.  You will see that quite a bit later.  Side note, Java has camelCase, 
#Python has snake_case with underscores, all lower case.  Picky?  Yes.  I know.

len(test_list) #Gives us the length.  We see 3, so far, so good.
#We can call specific elements by number.
test_list[0] #Actually gives us the first element.
# test_list[3] #MUST give an error, because there are 0,1,2 indices.    #This is commented out so we can run the code as one block.
#That is something we need to be mindful of!  Furthermore, that is why I
#started at s0 earlier!

#OK.  Now the fun/boring stuff, depending on your outlook.  That is right.  MATH.
#So, there is a guiding rule that tells us how data is broken down.  The rule
#tells us that if we took the average (mean) of some data, and found the 
#standard deviation (the average distance from the mean for the dataset)
#then this rule tells us where percentages of our data should be found.

#SO, we make an assumption.  We assume our mean is zero.  That is shockingly easy
#to make happen I promise (for people with a stat background, the z-score).
#Our standard deviation we will assume to be one, again, easy to make happen.
#We thus define that rule I mention above, the empirical rule.
#-2 two standard deviations left of the mean.
#-1 one standard deviation left of the mean.
#0 the mean, right in the center.
#1 one standard deviation right of the mean.
#2 two standard deviations right of the mean.
#Let us use a bit of logic.  If the mean is in the center, then ~half the data
#is above and half below.  So 50% of the data is on each side.
#The further from the mean we go, the less likely those values are to occur.
#So, logically, the closer we are to the mean, the higher portion of the data
#we should find.  The true empirical rule gives us this breakdown:

#x < -2; -2<x<-1; -1<x<0; 0<x<1; 1<x<2; x>2 #We ignore exact values, those are very unlikely.
#2.5%;     13.5%;    34%;   34%;   13.5%; 2.5% #These are the percentages of data in each block.

#So, if we had 1000 values, 25 should be in the first group, and so on.
#Let us do a quick test run!

for num in list1: #We loop through the numbers in list1.
    if num < -2: #Notice no parenthesis, blocks of code use common indentation.
        s0 = s0 + 1 #This is a separate block of code, so it has a deeper indent.
    elif num < -1: #elif is our shorter "else if" statement.  Only happens if the first condition is false.
        s1 = s1 + 1 #Notice we only count up when the statement is true, and the number is in this interval.
    elif num < 0:
        s2 = s2 + 1 #Are there other notations?  Sure!  We use this one for now for clarity.
    elif num < 1:
        s3 = s3 + 1
    elif num < 2:
        s4 = s4 + 1
    else: #This is our last option.  Number is larger than 2, falls here, so just else!
        s5 = s5 + 1
        
print("Should be roughly: 2.5, 12.5, 34, 34, 12.5, 2.5") #This is true!  These are what percentages we should have.
print("Actually is:", s0/10, s1/10, s2/10, s3/10, s4/10, s5/10) #We print the actual results.

#We see that we arrive at something pretty close to what we would expect!
#What happens if we change the list to be longer?  Shorter?
#Should things be more or less accurate?  Do we want to keep coding all that again and again?
#I do not!  Let us try something different instead.  Maybe we can create some functions?
#Also, we should talk about my first two questions.  And a new theory.
#But we should do all of that next time, as it is Sunday, and I hear other things calling me.
#Hearthstone, in case you were curious!