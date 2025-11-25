import pyMeow as pm

gmod_exe = pm.open_process("gmod.exe")
client_dll = pm.get_module(gmod_exe, "client.dll")

local_player_addr = pm.r_int64(gmod_exe, client_dll["base"] + 0x94b8d0)

print(f"Local player address: {hex(local_player_addr)}")

# Range for position offset
start_offset = 0x2E0
end_offset = 0x320

print("Scanning for position offset... (Move around to change position)")

# Read initial pos
initial_x = None
initial_y = None
initial_z = None

for offset in range(start_offset, end_offset, 0x4):  # Step by 4 for floats
    try:
        x = pm.r_float(gmod_exe, local_player_addr + offset)
        y = pm.r_float(gmod_exe, local_player_addr + offset + 4)
        z = pm.r_float(gmod_exe, local_player_addr + offset + 8)
        if -10000 < x < 10000 and -10000 < y < 10000 and -10000 < z < 10000:  # Reasonable range
            if initial_x is None:
                initial_x = x
                initial_y = y
                initial_z = z
                print(f"Initial pos at 0x{offset:03X}: x={x:.2f}, y={y:.2f}, z={z:.2f}")
            else:
                if abs(x - initial_x) > 10 or abs(y - initial_y) > 10 or abs(z - initial_z) > 10:  # Changed
                    print(f"Found position offset: 0x{offset:03X}")
                    print(f"Pos: x={x:.2f}, y={y:.2f}, z={z:.2f}")
                    break
    except:
        pass

print("Scan complete.")