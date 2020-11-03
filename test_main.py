import unittest
from main import *

class UnitTests(unittest.TestCase) :
      def test_plot(self) :
          fighand=plt.gca()
          figdat = fighand.get_lines()[0].get_xydata()
          this_x, this_y = zip(*figdat)
          self.assertTrue( len(this_x)==100 and len(this_y)==100, "you have plotted the wrong number of coordinates" )
          for i in range(len(this_x)) :
              self.assertTrue( np.fabs(this_y[i] - this_x[i] )>1e-7, "One or more of your coordinates falls outside of the region of interest" )  
              self.assertTrue( this_y[i]<2*this_x[i]+0.5 and this_y[i]>2*this_x[i]-0.5, "One or more of your coordinates falls outside of the region of interest" )
