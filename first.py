dob="22/06/2006".split("/")
curr="17/08/2023".split("/")
dob_date=(int)(dob[0])
dob_month=(int)(dob[1])
dob_year=(int)(dob[2])
curr_date=(int)(curr[0])
curr_month=(int)(curr[1])
curr_year=(int)(curr[2])
days=[31,28,31,30,31,30,31,31,30,31,30,31]
dob_days=(dob_year-1)*365.25
for i in range(dob_month-1):
    dob_days+=days[i]
dob_days+=dob_date
curr_days=(curr_year-1)*365.25
for i in range(curr_month-1):
    curr_days+=days[i]
curr_days+=curr_date
print(int(curr_days-dob_days))

