import dearpygui.dearpygui as dpg
import app

def add_viewmatrix_tab():
    with dpg.tab(label='ViewMatrix Test'):
        dpg.add_text("Enter ViewMatrix offset (hex, e.g., 7c2568)")
        dpg.add_input_text(label='Offset', tag='vm_offset', default_value='7c2568')
        dpg.add_button(label='Apply Offset', callback=lambda: setattr(app.Offsets, 'ViewMatrix', int(dpg.get_value('vm_offset'), 16)))
        dpg.add_checkbox(label='Enable Test Circles', tag='vm_test')
        dpg.add_color_edit(default_value=(255, 0, 0), tag='vm_color', label="Circle Color", display_type=dpg.mvColorEdit_uint8, no_inputs=True, no_alpha=True)