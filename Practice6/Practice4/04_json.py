# Filter only the three specified networks
import json

with open("sample-data.json") as f:
    data = json.load(f)

print("Interface Status")
print("=" * 80)
print(f"{'DN':50} {'Description':15} {'Speed':10} {'MTU'}")
print("-" * 80)

for item in data["imdata"][:3]:
    attrs = item["l1PhysIf"]["attributes"]

    dn = attrs["dn"]
    descr = attrs.get("descr", "")
    speed = attrs.get("speed", "")
    mtu = attrs.get("mtu", "")

    print(f"{dn:50} {descr:15} {speed:10} {mtu:5}")

#all networks
# with open("sample-data.json") as f:
#     data = json.load(f)
# print("Interface Status")
# print("="*80)
# print(f"{'DN':50} {'Description':20} {'Speed':8} {'MTU':6}")
# print("-"*80)
# for i in data["imdata"]:
#     a = i["l1PhysIf"]["attributes"]
#     print(f"{a['dn']:50} {a.get('descr',''):20} {a['speed']:8} {a['mtu']:6}")



# with open("sample-data.json") as f:
#     data = json.load(f)

# networks = ["eth1/33", "eth1/34", "eth1/35"]

# print("Interface Status")
# print("="*80)
# print(f"{'DN':50} {'Description':20} {'Speed':8} {'MTU':6}")
# print("-"*80)

