employee_id=1001
basic_salary=15000
allowance=6000
monthly_gross_salary=basic_salary+allowance
print("monthly gross salary=",monthly_gross_salary)
if monthly_gross_salary <5000:
	print("NIL")
elif 5001 >=10000 :
	income_tax=monthly_gross_salary*0.10
	net_salary=monthly_gross_salary-income_tax
	print("net salary=",net_salary)
elif 10001 >=20000:
	income_tax=monthly_gross_salary*0.20
	net_salary=monthly_gross_salary-income_tax
	print("net salary=",net_salary)
else:
	income_tax=monthly_gross_salary*0.30
	net_salary=monthly_gross_salary-income_tax
	print("net salary=",net_salary)
