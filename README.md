# Generating linearly correlated random variables

What you should have found was that you could generate the random variables for the previous exercise something like this:

````
xdata[i] = np.random.uniform(0,1)
ydata[i] = xdata[i] - 1 + 2*np.random.uniform(0,1)
````

If the variables are set in this way value of `ydata` is correlated but importantly each Y value you generate is still random as it is the sum of the random variable X and a (so-called) noise term (the  `-1 + 2*np.random.uniform(0,1)`.

Try the new exercise in the panel on the left to see if you have got the idea.  As always if you press you will see a graph with some lines on. Your task, once again, is to generate 100 random points that fall between the lines.  This time though the equations of the two lines are:

y = 2x + 0.5
y = 2x - 0.5

As always you should not need to use any conditional (if) statements to complete this task. 
