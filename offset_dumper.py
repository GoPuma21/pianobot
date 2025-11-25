import pyMeow as pm

gmod_exe = pm.open_process("gmod.exe")
client_dll = pm.get_module(gmod_exe, "client.dll")
engine_dll = pm.get_module(gmod_exe, "engine.dll")

offsets = {}

# Find LocalPlayer (scan for position)
print("Finding LocalPlayer...")
# Assume position offset 0x308, scan for X position
# This is simplified; in practice, you'd scan Cheat Engine style
# For now, placeholder
offsets['LocalPlayer'] = 0x86EE60  # Already found

# Find EntityList (pointer scan on local_player_addr)
print("Finding EntityList...")
local_player_addr = client_dll["base"] + offsets['LocalPlayer']
# Placeholder for pointer scan logic
offsets['EntityList'] = 0xA58100  # Already found

# Find ViewMatrix (scan for matrix as pointer)
print("Finding ViewMatrix...")
# Since scan not finding, use known offset
offsets['ViewMatrix'] = 0x7C3568

# Find ViewAngles (scan for angles)
print("Finding ViewAngles...")
# Placeholder: scan for yaw
offsets['ViewAngles'] = 0x6591FC  # Assume or find

# Other offsets (placeholders, as they require more complex scans)
offsets['ForceJump'] = 0xa3a9d0
offsets['Crosshair'] = 0x3700
offsets['BoneMatrix'] = 0x1A98
offsets['m_hObserverTarget'] = 0x2CC8
offsets['m_hActiveWeapon'] = 0x2940
offsets['Weaponname'] = 0x1D00
offsets['Playername'] = 0x3750
offsets['SteamID'] = 0x37C8

print("Offsets found:")
for key, value in offsets.items():
    print(f"{key} = 0x{value:06X}")

# Generate the class
class_code = "class Offsets:\n"
for key, value in offsets.items():
    class_code += f"    {key} = 0x{value:06X}\n"

print("\nGenerated Offsets class:")
print(class_code)