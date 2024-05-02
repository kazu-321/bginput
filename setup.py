from setuptools import find_packages, setup

package_name = 'bginput'

setup(
    name=package_name,
    version='1.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='kazu',
    maintainer_email='kzs321kzs@gmail.com',
    description='Get keyboard input (background)',
    license='apache',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'bginput = bginput.bginput:main'
        ],
    },
)
