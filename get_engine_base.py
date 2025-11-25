import pyMeow as pm

gmod_exe = pm.open_process("gmod.exe")
engine_dll = pm.get_module(gmod_exe, "engine.dll")
print(f"engine.dll base: {hex(engine_dll['base'])}")