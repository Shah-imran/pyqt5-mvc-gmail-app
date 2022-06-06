import subprocess
import os
from customexceptions.base import DeniedAccessError


class SystemInfo:
    def __init__(self):
        self.machine_uuid_command = 'wmic csproduct get uuid'
        self.processor_id_command = 'wmic cpu get ProcessorId'
        self._machine_uuid = ''
        self._processor_id = ''

    @property
    def machine_uuid(self):
        self._machine_uuid = subprocess.check_output(self.machine_uuid_command,
                                                     shell=False, **subprocess_args(False)).decode()
        self._machine_uuid = self._machine_uuid.split('\n')[1].strip()

        return self._machine_uuid

    @machine_uuid.setter
    def machine_uuid(self):
        raise DeniedAccessError('Access Restricted to this variable')

    @property
    def processor_id(self):
        self._processor_id = subprocess.check_output(self.processor_id_command,
                                                     shell=False, **subprocess_args(False)).decode()
        self._processor_id = self._processor_id.split('\n')[1].strip()

        return self._processor_id

    @processor_id.setter
    def processor_id(self):
        raise DeniedAccessError('Access Restricted to this variable')


def subprocess_args(include_stdout=True):
    # The following is true only on Windows.
    if hasattr(subprocess, 'STARTUPINFO'):
        # On Windows, subprocess calls will pop up a command window by default
        # when run from Pyinstaller with the ``--noconsole`` option. Avoid this
        # distraction.
        si = subprocess.STARTUPINFO()
        si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        # Windows doesn't search the path by default. Pass it an environment so
        # it will.
        env = os.environ
    else:
        si = None
        env = None

    # ``subprocess.check_output`` doesn't allow specifying ``stdout``::
    #
    #   Traceback (most recent call last):
    #     File "test_subprocess.py", line 58, in <module>
    #       **subprocess_args(stdout=None))
    #     File "C:\Python27\lib\subprocess.py", line 567, in check_output
    #       raise ValueError('stdout argument not allowed, it will be overridden.')
    #   ValueError: stdout argument not allowed, it will be overridden.
    #
    # So, add it only if it's needed.
    if include_stdout:
        ret = {'stdout': subprocess.PIPE}
    else:
        ret = {}

    # On Windows, running this from the binary produced by Pyinstaller
    # with the ``--noconsole`` option requires redirecting everything
    # (stdin, stdout, stderr) to avoid an OSError exception
    # "[Error 6] the handle is invalid."
    ret.update({'stdin': subprocess.PIPE,
                'stderr': subprocess.PIPE,
                'startupinfo': si,
                'env': env})
    return ret


if __name__ == "__main__":
    sd = SystemInfo()
    print(sd.machine_uuid, sd.processor_id)
