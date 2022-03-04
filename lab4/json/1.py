import json
print("Interface Status\n")
print("================================================================================\n")
print("DN                                                 Description           Speed    MTU ")
print("-------------------------------------------------- --------------------  ------  ------")
with open ('sample-data.json') as j: 
    a = json.load(j)
for i in a["imdata"]:
    print(i["l1PhysIf"]["attributes"]["dn"], (70 - len(i["l1PhysIf"]["attributes"]["dn"]))*" ",
    i["l1PhysIf"]["attributes"]["speed"], " ", i["l1PhysIf"]["attributes"]["mtu"])