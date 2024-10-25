import solar_system,sys,os
from setuptools import setup,Extension

try:os.chdir(os.path.split(__file__)[0])
except:pass

desc="""Python模拟万有引力、太阳系行星运动的库，模拟天体轨道，验证开普勒三大定律。\
Computer simulation of gravity and planetary motion in the solar system,\
emulating the orbits of celestial bodies and verifying Kepler's three laws."""

# 打包前后重命名文件
try:
    with open("README.rst",encoding="utf-8") as f:
        long_desc=f.read()
except OSError:
    long_desc=''

setup(
    name='solar-system',
    version=solar_system.__version__,
    description=desc,
    long_description=long_desc,
    author=solar_system.__author__,
    author_email=solar_system.__email__,
    url="https://github.com/qfcy/python-gravity-simulation",
    packages=['solar_system'],
    include_package_data=True,
    ext_modules=[Extension(
        "solar_system_accelerate_util",["solar_system/TESTs/solar_system_accelerate_util.c"]
    )],
    keywords=["solar","system","solarsys","turtle","graphics",
              "astronomy","gravity","physics",
              "太阳系","引力","模拟","物理","天文",
              "mercury","venus","earth","mars","jupiter",
              "saturn","uranus","neptune","pluto"],
    classifiers=[
        'Programming Language :: Python',
        "Topic :: Scientific/Engineering :: Astronomy",
        "Topic :: Multimedia :: Graphics",
        "Natural Language :: Chinese (Simplified)",
        "Topic :: Education"],
)