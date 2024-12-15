@echo off
pyinstaller "solar_system\教具版\引力模拟 - 第一、二宇宙速度.py" -i solar_system\dist\图标.ico -w --hidden-import tkinter.simpledialog --exclude-module solar_system --exclude-module turtle --noconfirm
pyinstaller "solar_system\教具版\引力模拟 - 开普勒第一定律.py" -i solar_system\dist\图标.ico -w --hidden-import tkinter.simpledialog --exclude-module solar_system --exclude-module turtle --noconfirm
pyinstaller "solar_system\教具版\引力模拟 - 开普勒第二定律.py" -i solar_system\dist\图标.ico -w --hidden-import tkinter.simpledialog --exclude-module solar_system --exclude-module turtle --noconfirm
pyinstaller "solar_system\教具版\引力模拟 - 开普勒第三定律.py" -i solar_system\dist\图标.ico -w --hidden-import tkinter.simpledialog --exclude-module solar_system --exclude-module turtle --noconfirm
pyinstaller "solar_system\教具版\引力模拟 - 日地月.py" -i solar_system\dist\图标.ico -w --hidden-import tkinter.simpledialog --exclude-module solar_system --exclude-module turtle --noconfirm
pyinstaller "solar_system\教具版\引力模拟 - 太阳系.py" -i solar_system\dist\图标.ico -w --hidden-import tkinter.simpledialog --exclude-module solar_system --exclude-module turtle --noconfirm
pyinstaller "solar_system\教具版\引力模拟 - 卫星变轨.py" -i solar_system\dist\图标.ico -w --hidden-import tkinter.simpledialog --exclude-module solar_system --exclude-module turtle --noconfirm
pyinstaller "solar_system\ENG\cosmic_velocities.py" -i solar_system\ENG\dist\icon.ico -w --hidden-import tkinter.simpledialog --exclude-module solar_system --exclude-module turtle --noconfirm
pyinstaller "solar_system\ENG\kepler_1st.py" -i solar_system\ENG\dist\icon.ico -w --hidden-import tkinter.simpledialog --exclude-module solar_system --exclude-module turtle --noconfirm
pyinstaller "solar_system\ENG\kepler_2nd.py" -i solar_system\ENG\dist\icon.ico -w --hidden-import tkinter.simpledialog --exclude-module solar_system --exclude-module turtle --noconfirm
pyinstaller "solar_system\ENG\kepler_3rd.py" -i solar_system\ENG\dist\icon.ico -w --hidden-import tkinter.simpledialog --exclude-module solar_system --exclude-module turtle --noconfirm
pyinstaller "solar_system\ENG\satellite_orbit_change.py" -i solar_system\ENG\dist\icon.ico -w --hidden-import tkinter.simpledialog --exclude-module solar_system --exclude-module turtle --noconfirm
pyinstaller "solar_system\ENG\solar_system_with_controls.py" -i solar_system\ENG\dist\icon.ico -w --hidden-import tkinter.simpledialog --exclude-module solar_system --exclude-module turtle --noconfirm
pyinstaller "solar_system\ENG\sun_earth_moon.py" -i solar_system\ENG\dist\icon.ico -w --hidden-import tkinter.simpledialog --exclude-module solar_system --exclude-module turtle --noconfirm