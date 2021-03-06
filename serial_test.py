import serial_control as sc
import numpy as np
import time

# sc.serial_example()
# sc.test_serial()

belt_drive = sc.motor_communication('/dev/ttyS4', 'belt_drive', 'belt', 2940)

litposmm = np.linspace(0, 2500, 11)
print (str(litposmm))

belt_drive.open_port()
belt_drive.start_manual_mode()
belt_drive.initialize_home_pos()
belt_drive.initialize_extreme_pos()

for tposmm in litposmm:

    belt_drive.go_to_pos_mm(tposmm)
    barrived = False
    while barrived is False:
        time.sleep(0.5)
        barrived = belt_drive.check_arrival()

    time.sleep(2)

belt_drive.get_status()
time.sleep(1.0)
belt_drive.close_port()



