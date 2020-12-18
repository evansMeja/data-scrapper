def processInitial(s):
    res = s.split()
    names = res[1:-2]
    data = {'email':res[-1],'phone':"254" + str(int(res[-2])),'default_password':"thespianswa@2020"}
    l = len(res[1:-2])
    if l == 2:
        data['first_name'] = names[0]
        data['middle_name'] = ""
        data['last_name'] = names[1]
    else:
        data['first_name'] = names[0]
        data['middle_name'] = names[1]
        data['last_name'] = names[2]   
    return data

with open("data.txt") as d:
    c = d.readlines()
 
c = [x.strip() for x in c]
for i in c:
    res = processInitial(i)
    print(res)
