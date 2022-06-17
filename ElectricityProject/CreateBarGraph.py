
import numpy as np
import matplotlib.pyplot as plt


class CreateBarGraph:

    def priceVsYear(self, yearSet , predictedPrice):
       x = np.arange(len(yearSet))
       width = 0.40

       fig, ax = plt.subplots()

       ax.set_ylabel('Predicted Price (in rupee)')
       ax.set_title('Years')
       ax.set_xticks(x)
       ax.set_xticklabels(yearSet)

       pps = ax.bar(x - width / 2, predictedPrice, width, label='Price')
       for p in pps:
          height = p.get_height()
          ax.annotate('{}'.format(height),
                      xy=(p.get_x() + p.get_width() / 2, height),
                      xytext=(0, 3),
                      textcoords="offset points",
                      ha='center', va='bottom')
       plt.savefig('Files/PriceVsYearGraph.png', dpi=400)
       plt.show()





