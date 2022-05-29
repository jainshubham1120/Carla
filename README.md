# Carla

[RGB+Sem.zip](https://github.com/jainshubham1120/Carla/files/8792919/RGB%2BSem.zip)


I am working with Carla 0.9.11. Download and Install Carla from [here.](https://carla.readthedocs.io/en/0.9.11/start_quickstart/)

Above installation includes 5 maps only. 2 more maps can be downloaded from [here.](https://github.com/carla-simulator/carla/releases/tag/0.9.11)

Run **manualcontrol.py** file. It is present in "examples" folder by default upon installation. I have modified the code of this file according to the requirement.

All Camera locations:

(Coordinate axis is pre-defined in Carla)

- Cam1 - Location(x=1.0,z=0.37))
- Cam2 - Location(x=1.0,y=0.265,z=0.56))
- Cam3 - Location(x=1.0,y=-0.265,z=0.56))
- Cam4 - Location(x=-1.0,z=0.38), Rotation(pitch=0.0, yaw=180.0, roll=0.0))

In the simulator, at each of these location 2 cameras are placed. 1 captures RGB images, other captures Semantic ground truth. In Carla, all the data regarding semantic ground truth is saved in the red channel by default.

Carla saves images only from one camera at a time. So, to save images from the 'semantic camera' I wrote the function "process_img".

Function process_img:

- starts saving images when recording is turned on.
- does not shows the output on pygame window because it becomes computationally expensive to have multiple pygame surfaces.
- image.convert(cc) is not used since we need only the ground truth.

See class "KeyboardControl" to learn keyboard settings for various operation. I have added some keyboard settings since 2 cameras will be operated simultaneously.

`bp.set_attribute("fov","150")`  -> FOV = 150 degrees Horizontal

`IM_HEIGHT = 512, IM_WIDTH = 1024`  -> Output image dimensions: 512*1024

`bp.set_attribute("sensor_tick","3.0")`  -> Takes image after every 3 seconds. It is set to 0 seconds by default.

## Format of Saved Images

.npy format is taking more space than a PNG image. JPEG images are prone to data loss while reading and writing the image. Hence, PNG format have been used to save the images.

## AWS

Before starting your AWS instance:

- Set the location to the geographically closest AWS centre to avoid any latency issues.
- Switch from wifi to lan to avoid any latency issues.

I used [this](https://github.com/jbnunn/CARLADesktop) Github repo for installing Carla on a Linux 18.04 supported g4dn.xlarge EC2 instance.

In the above Github repo,

1. Generally, Carla is used for training ML models. But I am using it to generate dataset. Hence I require more CPU centric system than a GPU centric system. So, use g4dn.2xlarge instance instead of .xlarge. .xlarge instance gives 3-4 FPS speed and .2xlarge instance gives 11-12 FPS speed.
2. change the line:

`wget https://download.nomachine.com/download/6.11/Linux/nomachine_6.11.2_1_amd64.deb`

with the latest version of NoMachine. I used:

`wget https://download.nomachine.com/download/7.6/Linux/nomachine_7.6.2_4_amd64.deb`.

1. Refer to Carla's [documentation](https://carla.readthedocs.io/en/0.9.11/start_quickstart/) for downloading the Carla version of your choice and install the corresponding python version to create a virtual environment for Carla.

On your system, in NoMachine, go to Settings -> Server -> Performance -> uncheck "Use a specific frame rate". This will help to reduce latency issues.

After installing Carla, update the Nvidia drivers using [this.](https://www.itzgeek.com/post/how-to-install-nvidia-drivers-on-ubuntu-20-04-ubuntu-18-04.html)

## References:

- You can refer to [this](https://youtube.com/playlist?list=PLQVvvaa0QuDeI12McNQdnTlWz9XlCa0uo) playlist on Youtube to have a better understanding of Carla.
- Carla [documentation](https://carla.readthedocs.io/en/0.9.11/).
- Check out [this](https://sagnibak.github.io/blog/how-to-use-carla/) article.
