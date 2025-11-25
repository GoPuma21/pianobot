import pyMeow as pm

gmod_exe = pm.open_process("gmod.exe")
engine_dll = pm.get_module(gmod_exe, "engine.dll")

# Range for ViewMatrix offset (direct)
start_offset = 0x700000
end_offset = 0x800000

for offset in range(start_offset, end_offset, 0x100):  # Step by 256 for speed
    try:
        view_matrix_base = engine_dll["base"] + offset
        matrix = pm.r_floats(gmod_exe, view_matrix_base, 16)
        if len(matrix) == 16 and abs(matrix[15] - 1.0) < 0.01 and abs(matrix[14]) < 0.01 and abs(matrix[13]) < 0.01 and abs(matrix[12]) < 0.01:
            print(f"Found ViewMatrix offset: 0x{offset:06X}")
            break
    except:
        pass

print("Scan complete.")