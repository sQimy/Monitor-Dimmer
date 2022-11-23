import monitorcontrol

monitors = monitorcontrol.get_monitors()

with monitors[0] as monitor:
    info = monitor.get_vcp_capabilities()

print(info["model"])