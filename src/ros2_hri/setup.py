from setuptools import find_packages, setup

package_name = 'ros2_hri'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/launch.py']),
        ('share/' + package_name + '/world', ['world/Scene10.world']),
        ('share/' + package_name + '/urdf', [
            'urdf/urdf.urdf',
            'urdf/urdf2.urdf',
            'urdf/urdf3.urdf',
            'urdf/urdf4.urdf',
            'urdf/ur5.urdf.xacro',  # Adicionando o arquivo ur5.urdf.xacro
        ]),
        ('share/' + package_name + '/ros2_hri', ['ros2_hri/camera_viewer_node.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='dtu1990',
    maintainer_email='dtu1990@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'camera_viewer_node = ros2_hri.camera_viewer_node:main',
        ],
    },
)

