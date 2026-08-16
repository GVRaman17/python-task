def gross(s,hra,da):
  t_s=s+((s/100)*hra)+((s/100)*da)
  return t_s
salary=int(input('enter your salary:'))
if salary<=20000:
  total_sal=gross(salary,20,50)
elif salary<=40000:
  total_sal=gross(salary,25,60)
else:
  total_sal=gross(salary,30,70)
print('your salary is',salary,'your gross is ',total_sal)
