import platform
import subprocess

current_machine_id = str(subprocess.check_output('wmic bios get serialnumber'), 'utf-8').split('\n')[1].strip()


print("="*40, "System Information", "="*40)
uname = platform.uname()
print(f"System: {uname.system}")
print(f"Node Name: {uname.node}")
print(f"Release: {uname.release}")
print(f"Version: {uname.version}")
print(f"Machine: {uname.machine}")
print(f"Processor: {uname.processor}")
print(f"Mac Adress: {current_machine_id}")