import cx_Freeze

executables = [cx_Freeze.Executable("app.py",
                                   base = "Win32GUI",
                                   icon = None)]

build_exe_options = {"packages": [],
                     "include_files":[]}

cx_Freeze.setup(
    name = "Prueba",
    version = "1.0",
    description = "Prueba",
    options = {"build_exe": build_exe_options},
    executables = executables
    )