#!/usr/bin/env python3

import pandas as pd

excel_file = "Pandas_serial.xlsx"

devices_on = pd.read_excel(excel_file, sheet_name=0, index_col=None)

# print(type(devices_on))
#
# print(devices_on)
# print(devices_on['Serial'][0])
# print(devices_on['Serial'][9])
# print(type(devices_on['Serial']))

# for device in devices_on['Serial']:
#     print(device)


devices_delivered = pd.read_excel(excel_file, sheet_name=1, index_col=None)
#
# print(devices_delivered.columns)
# print(devices_delivered)

on = []
off = []
dev_on_serial = [d for d in devices_on['Serial']]
#print(dev_on_serial)


for dev in devices_delivered['Serial']:
    if dev in dev_on_serial:
    #if dev in list(devices_on['Serial']):
        on.append(dev)
    else:
        off.append(dev)

print(f"The devices that are on are: {on}")
print(f"The devices that are off are: {off}")


for delivered in off:
    d = devices_delivered.index[devices_delivered['Serial'] == delivered].tolist()
    #print(delivered, d)
    print(devices_delivered.loc[d])
