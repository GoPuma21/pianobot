import pyMeow as pm

gmod_exe = pm.open_process("gmod.exe")
client_dll = pm.get_module(gmod_exe, "client.dll")
print(f"client.dll base: {hex(client_dll['base'])}")