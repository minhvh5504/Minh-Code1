S = str(input("Nhap S: "))
if S.endswith("!!!"):
  smoi = S
elif S.endswith("!!"):
    smoi = S+"!"
elif S.endswith("!"):
    smoi = S+"!!"
elif S.endswith(""):
    smoi = S+"!!!"
else: 
    smoi = S
print("Chuoi S sau khi xu ly:",smoi)    
    
