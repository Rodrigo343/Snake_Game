import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"], "includes": ["pygame"]}

# GUI applications require a different base on Windows (the default is for
# a console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="jogoCobra",
    version="0.1",
    description="Executavel",
    options={"build_exe": build_exe_options},
    executables=[Executable("jogoCobra.py", base=base)]
)