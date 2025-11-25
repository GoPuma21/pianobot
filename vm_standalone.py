import pyMeow as pm
import dearpygui.dearpygui as dpg
import threading
import os

class Offsets:
    ViewMatrix = 0x7c2568

def main():
    if not pm.process_exists("gmod.exe"):
        print("GMod not found")
        return
    gmod_exe = pm.open_process("gmod.exe")
    client_dll = pm.get_module(gmod_exe, "client.dll")
    engine_dll = pm.get_module(gmod_exe, "engine.dll")

    pm.overlay_init("ViewMatrix Test", fps=60)

    while pm.overlay_loop():
        if not pm.process_running(gmod_exe):
            break
        pm.begin_drawing()
        if dpg.get_value('vm_test'):
            try:
                view_matrix_base = pm.r_int64(gmod_exe, engine_dll["base"] + Offsets.ViewMatrix) + 0x2D4
                view_matrix = pm.r_floats(gmod_exe, view_matrix_base, 16)
                pm.draw_text("Matrix OK", 10, 10, 20, pm.get_color("white"))
                screen_center_x = pm.get_screen_width() // 2
                screen_center_y = pm.get_screen_height() // 2
                radius = 100
                color = dpg.get_value('vm_color')
                r, g, b = color[:3]
                pm.draw_circle_lines(screen_center_x, screen_center_y, radius, pm.get_color(f"#{r:02X}{g:02X}{b:02X}"), 1)
            except:
                pass  # If offset wrong, don't draw
        pm.end_drawing()

def start():
    dpg.create_context()
    dpg.create_viewport(title="ViewMatrix Test", decorated=True, width=400, height=200)
    with dpg.window(tag='w_main'):
        with dpg.tab_bar():
            with dpg.tab(label='ViewMatrix Test'):
                dpg.add_text("Enter ViewMatrix offset (hex, e.g., 7c2568)")
                dpg.add_input_text(label='Offset', tag='vm_offset', default_value='7c2568')
                dpg.add_button(label='Apply Offset', callback=lambda: setattr(Offsets, 'ViewMatrix', int(dpg.get_value('vm_offset'), 16)))
                dpg.add_checkbox(label='Enable Test Circles', tag='vm_test')
                dpg.add_color_edit(default_value=(255, 0, 0), tag='vm_color', label="Circle Color", display_type=dpg.mvColorEdit_uint8, no_inputs=True, no_alpha=True)

    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.set_primary_window("w_main", True)

    threading.Thread(target=main, daemon=True).start()
    dpg.start_dearpygui()

if __name__ == "__main__": 
    start()