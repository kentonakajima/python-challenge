#!/usr/bin/env python
# coding: utf-8

# In[44]:


#Financial Analysis
#----------------------------
#Total Months: 86
#Total: $22564198
#Average Change: $-8311.11
#Greatest Increase in Profits: Aug-16 ($1862002)
#Greatest Decrease in Profits: Feb-14 ($-1825558)


# To import os module
import csv

# To import csv module
import os

# To access the file
datafile = os.path.join(".", "Resources", "budget_data.csv")

fAnalysis = os.path.join(".", "fAnalysis.txt")

# To set variables

total_months = 0
total_net = 0
net_change_list = []
month_of_changes = []

greatest_increase = [" ", 0]
greatest_decrease = ["", 9999999999999999]

# To read the file
with open(datafile) as datafile:
    reader = csv.reader(datafile, delimiter=",")

    # To read header row
    header = next(datafile)
    
    # To print header
    first_row = next(reader)
    #print(int(first_row[1]))
    
    total_net += int(first_row[1])
    #print(total_net)
   
    previous_net = int(first_row[1])
    
    total_months += 1
    
    
    for row in reader:
        
        # To calculate total months
        total_months += 1
        
        # To calculate total net
        total_net += int(row[1])
        
   
        # To calculate net change
        net_change = int(row[1]) - previous_net
        previous_net = int(row[1])
        net_change_list.append(net_change)
        

        
        # To calculate greatest increase
        if(net_change > greatest_increase[1]):
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change
            
            
        # To calculate greatest decrease
        if(net_change < greatest_decrease[1]):
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change
        
#print(net_change_list)
#print(greatest_increase)
#print(greatest_decrease)

net_monthly_average = sum(net_change_list) / len(net_change_list)

    
output = (
     f"Financial Analysis\n"
     f"------------------------\n" 
     f"Total Months: {total_months}\n" 
     f"Total: ${total_net}\n"
     f"Average Change ${net_monthly_average:.2f}\n"
     f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
     f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")
    
print(output)

#To creat output fAnalysis file
with open(fAnalysis, "w") as txt_file:
    txt_file.write(output)
    
      






# In[ ]:





# In[ ]:




