monthly_expenses=[343,344,343,644,735,674,664,544,456,353,745,776]
first_semester=0
second_semester=0
for i in range(0,12):
    if(i<6):
        first_semester=first_semester+monthly_expenses[i]
    else :
        second_semester=second_semester+monthly_expenses[i]
print("first semester expenses:",first_semester)
print("first semester expenses:",second_semester)
average_expense_for_first_semester=first_semester/6
average_expense_for_second_semester=second_semester/6
print("Average Expenses for first semester",round(average_expense_for_first_semester) )
print("Average Expenses for second semester",round(average_expense_for_second_semester))
