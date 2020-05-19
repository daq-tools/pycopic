#######
pycopic
#######


*****
About
*****
An attempt to mix Pycom's `pycoproc`_ with `pypic`_ in order to
control the PIC through the serial interface and use extended
functionalities even on the expansion board, where the PIC
is not connected to the I2C bus of the ESP32.

This is essentially a hack, YMMV.

.. note:: This is still a work-in-progress and didn't work out successfully yet.


********
Synopsis
********
::

    export MCU_PORT=/dev/cu.usbmodemPy001711

    pycopic --port $MCU_PORT --sleep 30
    pycopic --port $MCU_PORT --reset


*********
Resources
*********

.. todo:: Add some links to the Pycom user forum here.


.. _pycoproc: https://github.com/pycom/pycom-libraries/blob/master/lib/pycoproc/pycoproc.py
.. _pypic: https://github.com/pycom/pycom-micropython-sigfox/blob/Dev/esp32/tools/pypic.py
