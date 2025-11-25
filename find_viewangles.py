import pyMeow as pm

gmod_exe = pm.open_process("gmod.exe")
engine_dll = pm.get_module(gmod_exe, "engine.dll")

# Range for ViewAngles offset (direct)
start_offset = 0x650000
end_offset = 0x670000

print("Scanning for ViewAngles offset... (Move your mouse to change angles)")

# Read initial angles
initial_yaw = None
initial_pitch = None

for offset in range(start_offset, end_offset, 0x4):  # Step by 4 for floats
    try:
        yaw = pm.r_float(gmod_exe, engine_dll["base"] + offset)
        pitch = pm.r_float(gmod_exe, engine_dll["base"] + offset + 4)
        if -180 <= yaw <= 180 and -90 <= pitch <= 90:
            if initial_yaw is None:
                initial_yaw = yaw
                initial_pitch = pitch
                print(f"Initial angles at 0x{offset:06X}: yaw={yaw:.2f}, pitch={pitch:.2f}")
            else:
                if abs(yaw - initial_yaw) > 5 or abs(pitch - initial_pitch) > 5:  # Changed
                    print(f"Found ViewAngles offset: 0x{offset:06X}")
                    print(f"Angles: yaw={yaw:.2f}, pitch={pitch:.2f}")
                    break
    except:
        pass

print("Scan complete.")