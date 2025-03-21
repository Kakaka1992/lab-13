print("задание 1")
rept = {"python" : " питон",
 "anaconda" : "анаконда",
 "tortoize" : " черепаха" }
rept["snake"] = "змея"
rept["tortoise"]=rept["tortoize"]
del rept["tortoize"]
for key, value in rept.items():
    print(f"{rept[key]}  по англиски будет {key}")

print("задание 2")
cnt = ["Andorra", "Belarus", "Denmark",
 "Kenya", "Jamaica", "Romania"]
fh = [1.0, 6.0, 1.0, 4.0, 2.5, 2.0]
obj = dict()
for n in range(len(fh)):
    obj[fh[n]]=cnt[n]
print(obj)

print("задание 3")
pairs = [(2, 4), (4, 6), (0, 1), (5, 2), (9, 1), (3, 8)]
calc={}
for n in pairs:
    calc[n]=n[0]*n[1]
print(calc)

print("задание 4")
grades = {'Anna': 4, 'Bob': 3, 'Claire': 5, 'Dick': 2, 'Elena': 5,
 'Fred': 5, 'George': 4, 'Kristina': 3, 'Nick': 2,
 'Ursula': 4, 'Viktor': 5}
excel=[]
good=[]
satisf=[]
bad=[]
for n in grades:
    if grades[n]==5:
        excel.append({n})
    if grades[n]==4:
        good.append({n})
    if grades[n]==3:
        satisf.append({n})
    if grades[n]==2:
        bad.append({n})
print("отлично", excel)
print("хорошо", good)
print("удвлетворительно", satisf)
print("плохо", bad) 
