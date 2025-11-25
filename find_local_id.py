import pyMeow as pm

class Offsets:
    LocalPlayer = 0x94B8D0
    EntityList = 0x96d8a8

gmod_exe = pm.open_process("gmod.exe")
client_dll = pm.get_module(gmod_exe, "client.dll")

local_player_addr = pm.r_int64(gmod_exe, client_dll["base"] + Offsets.LocalPlayer)

entity_list_base = pm.r_int64(gmod_exe, client_dll["base"] + Offsets.EntityList)
for i in range(0, 128):
    ent_addr = pm.r_int64(gmod_exe, entity_list_base + i * 0x20)
    if ent_addr == local_player_addr:
        print(f"Local ID: {i}")
        break