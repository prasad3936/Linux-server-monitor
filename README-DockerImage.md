Hello ! Welcome to my apllication 

The apllication is designed To Monitor the linux server (especially ubuntu ) . The application is tailored with technologies like flask , psutil module ,Dpcker etc.
To Start with Execution , 

**1.Install Docker** 
#sudo apt install docker.io -y 

**2.To Access The application . you have to launch a container , Steps are followed ,**

_a) Build Container Image_ 
#Go to the linux-server-monitor directory 

#docker build . 

_b).run a container from the image_ 

#docker run -p 5000:5000 -it <image_id>

HIT http://localhost:5000 o your favourite browser ! You have your application ready!

![image](https://github.com/prasad3936/Linux-server-monitor/assets/63768420/f3dfd400-cd0e-4568-9694-42d3475375c6)
