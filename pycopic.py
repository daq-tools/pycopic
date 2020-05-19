import sys
import argparse
import time

from mock import MagicMock
from pypic import Pypic


def patch_python():

    import builtins
    builtins.const = int

    sys.modules['pycom'] = MagicMock()
    sys.modules['machine'] = MagicMock()


def patch_pycoproc():

    global PycoprocForSerial

    from pycoproc import Pycoproc
    class PycoprocForSerial(Pycoproc):

        def __init__(self, pypic, *args, **kwargs):
            self.pypic = pypic
            self.board_type = None
            self.clk_cal_factor = 1
            self.reg = bytearray(6)
            self.wake_int = True
            self.wake_int_pin = False
            self.wake_int_pin_rising_edge = True

        def _write(self, data, wait=True):
            self.pypic._write(data, read=False)
            if wait:
                time.sleep(100 / 1000.0 / 1000.0)

        def _read(self, size):
            return [None]
            #return self.pypic._read(size)
            r_data = self.pypic.serial.read(2)
            #if not r_data:
            #    raise Exception('Timeout while waiting for Rx data')
            if r_data:
                return [r_data[0]]
            else:
                return [None]

        def calibrate_rtc___(self):
            # the 1.024 factor is because the PIC LF operates at 31 KHz
            # WDT has a frequency divider to generate 1 ms
            # and then there is a binary prescaler, e.g., 1, 2, 4 ... 512, 1024 ms
            # hence the need for the constant
            self._write(bytes([self.CMD_CALIBRATE]), wait=False)

        def setup_sleep(self, time_s):
            time_s = int((time_s * self.clk_cal_factor) + 0.5)  # round to the nearest integer
            if time_s >= 2 ** (8 * 3):
                time_s = 2 ** (8 * 3) - 1
            self._write(bytes([self.CMD_SETUP_SLEEP, time_s & 0xFF, (time_s >> 8) & 0xFF, (time_s >> 16) & 0xFF]))

        def go_to_sleep__(self, gps=True):
            self.poke_memory(self.ANSELB_ADDR, 0xFF)
            self._write(bytes([self.CMD_GO_SLEEP]), wait=False)


def main():

    # Monkeypatch Pycom modules.
    patch_python()
    patch_pycoproc()

    # Parse command line arguments.
    parser = argparse.ArgumentParser(description='Sends commands to the PIC on Pycom modules')
    parser.add_argument('-p', '--port', metavar='PORT', required=True, help='The serial port used to communicate with the PIC')
    parser.add_argument('-s', '--sleep', type=int, metavar='SLEEP', help='Send device to sleep mode for N seconds')
    parser.add_argument('-r', '--reset', action='store_true', help='Reset device')
    args = parser.parse_args()

    pypic = Pypic(args.port)
    pycoproc = PycoprocForSerial(pypic)

    if pypic.isdetected():
        if args.sleep:
            pycoproc.setup_sleep(args.sleep)
            pycoproc.go_to_sleep(gps=False)
        elif args.reset:
            pypic.reset_pycom_module()
    else:
        raise KeyError('No PIC detected')

    pypic.close()


if __name__ == "__main__":
    main()
