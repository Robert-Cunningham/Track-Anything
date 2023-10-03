from setuptools import find_packages, setup

setup(
    name="track_anything",
    version="0.3.0",
    description="Track Anything, Refactored",
    packages=find_packages(),
    install_requires=["numpy", "opencv-python", "pyyaml", "tqdm"],
    package_data={"track_anything": ["xmem/config/config.yaml"]},
)
