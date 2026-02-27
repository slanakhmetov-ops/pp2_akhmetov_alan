import json
with open("sample-data.json") as f:
    data = json.load(f)
print("Interface Status")
print("="*80)
print(f"{'DN':50} {'Description':20} {'Speed':8} {'MTU':6}")
print("-"*80)
for i in data["imdata"]:
    a = i["l1PhysIf"]["attributes"]
    print(f"{a['dn']:50} {a.get('descr',''):20} {a['speed']:8} {a['mtu']:6}")