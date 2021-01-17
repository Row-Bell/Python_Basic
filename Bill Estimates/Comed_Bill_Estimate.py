#Quick script to calculate estimate cost of energy bill
import matplotlib.pyplot as plt

supp = .05847+0.01220
delivery = 0.02854+0.00122
tax_fee = 0.00038+0.00189+0.00195+0.00132

energy_dict = [supp, delivery, tax_fee]

print(energy_dict)

estimated_watts = {'jan': 205,
                       'feb': 189,
                       'mar': 180,
                       'apr': 179,
                       'may': 179,
                       'jun': 284,
                       'jul': 751,
                       'aug': 601,
                       'sep': 545,
                       'oct': 200,
                       'nov': 178,
                       'dec': 207}

watts_hour = list(estimated_watts.values())
watt_hour = [float(ele) for ele in watts_hour]
estimated_supp_tot = [ele*supp for ele in watt_hour]
estimated_del_tot = [ele*delivery for ele in watt_hour]
estimated_tax_and_fee_tot = [ele*tax_fee for ele in watt_hour]

estimated_tot = list(map(sum, zip(estimated_supp_tot,estimated_del_tot,estimated_tax_and_fee_tot)))
######

# x- coordinates of left sides of bars
left = list(estimated_watts.keys())

#heights fo bars
height = estimated_tot

#labels for bars
tick_labels = list(estimated_watts.keys())

#plotting a bar chart
plt.bar(left, height, tick_label = tick_labels, width = 0.8, color = ['r','g'])

plt.xlabel('month')
plt.ylabel('price $')

#giving a title to my graph
plt.title('COMED BILLS EXTIMATE!')

#function to show the plot
plt.show()