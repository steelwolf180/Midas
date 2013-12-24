from cx_Freeze import setup, Executable

setup(
    name = "Midas" ,
    version = "0.1" ,
    description = "Personal Financial Plan Program" ,
    executables = [Executable("Financial_Plan.py")] ,
    )
