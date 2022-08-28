<a name="project-name"></a>
<div align="center">
  <img src="https://github.com/Ayanghosh-agno/AI_GarAge/blob/main/Images/garage.png" height=150px>
</div>
<div align="center">
  

  >New Technology, New evolution.
</div> 



## What is AI-GARAGE?

The AI GARAGE is a prototype of the smart garage system, which is one of the essential needs of a smart home. These doors not only help from burglars but also closes on its own as soon as it senses that someone took the car out. Unlike a manual garage door, the smart garage door gives a tough time to the thieves for entering the house. Similarly It also gives the owner a hassle free entry to the garage as soon as the System recognizes either the car number plate or the face. The project provides the user with a simple monitoring system that enables them to act more security conscious, effectively increasing the safety and security of their home with the use of some latest technology Like AI,ML and IoT implemented in the IBM cloud.

## Contents 
- [AI GARAGE](#project-name)
  01. [Short Description](#Short-Description)
      - [What's the problem?](#whats-the-problem)
      - [Proposed Solution](#Proposed-Solution)
  2. [Demo Video](#Demo-Video)
  3. [Architecture](#Architecture)
  4. [Long Description](#Long-Description)
      - [More about the UI](#More-about-the-UI)
      - [About the hardware setup](#hardware-part)
  5. [Hardware Requirements](#Hardware-Requirements)
  6. [Software/Access Requirements](#Software/Access-Requirements)
  7. [Project Roadmap](#Project-Roadmap)
  8. [Circuit Setup](#Circuit-Setup)
  9. [Development/Code Setup](#Development/Code-Setup)
  10. [Planned for Future](#Planned-for-Future)
  11. [Authors](#Authors)




<h2 align="center"> Short Description <a name="Short-Description"></a> </h2>

### What's the problem? <a name="whats-the-problem"></a>

The major issue in now a days are the busy life of the human mankind, due to which many of us forget to close the garage door in hurry and the consequences is very well known to us. Securing homes has become one of the concerning issues. Today homes are being more vulnerable for several threats especially being burgled. For this manner home security is needed. Home security implicitly means a secured mechanism for the door Also, there might be way to check if our garage door is open or close remotely form the CCTV installed in the garage but it is difficult for us to operate the door remotely. Moreover in this world where technology is taking over in a rocket speed we need to open the garage door every time manually while entering with our car.



### Proposed Solution <a name="Proposed-Solution"></a>

In this AI-GARAGE we had tried to eliminate the manual interaction as much as we can, using some latest technology like IoT, AI and ML to control and operate the garage door automatically or through our smartphones. The IoT-based smart garage door eliminates the need for carrying bulky keychains. All we need is to configure and integrate with smartphone with the home IoT network and with our facial image and car’s number plate and we can effortlessly open or close your garage door with just a few clicks of a button or automatically through the facial recognition and number/license plate detection!Along with some extra features like predicting the resell value of our car and also SMS alert for extra security.

AI-GARAGE contains the following features:- 

* Garage door opening with Facial-Recognition.

* Garage door opening with Car number plate detection using OCR.

* Automatic closing of the garage door after 5mins. 

* Live preview of the garage door.

* Controlling the Garage Lights using our Smart Phone.

* Controlling the Garage door using our Smart-Phone.

* Last image when the garage door was opened sent to the app.

* SMS alert whenever the gargae door is opened.

* We can also check each and every pic captured while opening the garage door stored securely in the IBM cloud’s Object-Storage.

* We can also check our car's resell value using IBM watson Studio.

<h2 align="center">Demo Video</h1><a name="Demo-Video"></a>

[![Demo Video](https://github.com/Ayanghosh-agno/AI_GarAge/blob/main/Images/Thumbnail.png)](https://youtu.be/AaOKyM1qtgM)

<h2 align="center">Architecture</h1><a name="Architecture"></a>

![Architecture Image](https://github.com/Ayanghosh-agno/AI_GarAge/blob/main/Images/AI-Garage_Archi%20.png)


## Long Description <a name="Long-Description"></a>
[Long Description Document Link](https://github.com/Ayanghosh-agno/AI_GarAge/blob/main/DOCUMENTATION/AI-GARAGE.pdf)

### More about the UI <a name="More-about-the-UI"></a>
*Sample of the APP UI:*
<div align="center">
<img src="https://github.com/Ayanghosh-agno/AI_GarAge/blob/main/Images/UI_.png">
</div>


### About the hardware setup <a name="hardware-part"></a>
<div align="center">
  <img src="https://github.com/Ayanghosh-agno/AI_GarAge/blob/main/Images/Hardware-Setup.jpg">
</div>

## Hardware Requirements <a name="Hardware-Requirements"> </a> 

* Jetson Nano
* 8-channel relay module
* Raspi V 2.0 camera
* Garage door actuators(for opening and closing the door mechanically)


![Hardware](https://github.com/Ayanghosh-agno/AI_GarAge/blob/main/Images/Hardware.png)

## Software/Access Requirements<a name="Software/Access-Requirements"></a> 
 * [IBM developer account](https://cloud.ibm.com/login)
 * [IBM Watson IoT](https://cloud.ibm.com/login)
 * [IBM Watson Studio](https://cloud.ibm.com/login) 
 * [IBM Watson Services](https://cloud.ibm.com/login) 
 * [Node Red](https://cloud.ibm.com/login)
 * [IBM Cloudant DB](https://cloud.ibm.com/login)
 * [IBM Object Storage](https://cloud.ibm.com/login)
 * [Twilio](https://www.twilio.com/) API access- for SMS notifications.
 * [Python3](https://www.python.org)- for programming the raspberry pi.
 * [MIT APP INVENTOR](https://appinventor.mit.edu/)-For making the app.
 * [Open CV](https://opencv.org)
 * [Tesseract](https://pypi.org/project/pytesseract)
 * [Face recognition package](https://face-recognition.readthedocs.io/en/latest/readme.html)


## Project Roadmap <a name="Project-Roadmap"></a>
![picture alt](https://github.com/Ayanghosh-agno/AI_GarAge/blob/main/Images/roadmap.png)

    
## Circuit Setup <a name="Circuit-Setup"></a>
 ![picture alt](https://github.com/Ayanghosh-agno/AI_GarAge/blob/main/Images/circuit.jpg)

 ## Development/Code-Setup <a name="Development/Code-Setup"></a>
  
  ### Upload the python files to Jetson-Nano
  
* After uploading change the credentials.py file with your own credential of IBM Cloud services.
* Chnage the Twillo credentials with your own credentials.
* Insert a training image for the faial recognition in the project directory and change the variables in the train_face.py. Also change input their name which you want to hover after successfully recognising them in Face_rec.py.
* Do the connecting as shown above with the relay module and Jetson-nano.

* Install the following libraries

```
pip3 install face_recognition
pip3 install pytesseract

```
* Now run all the python files

### Import the APP

* Import the App to your smartphone.
* Now you will be ready to use AI-Garage after connecting the circuit as given. 

## Planned for Future <a name="Planned-for-Future"></a>

1. Improve the facial-recognition part and the number plate recognition part to work it flawlessly.

2. Improve the UI of the app to make more attractive and easy to use.

3. To make a different segment in the app where the admin can check the history of the captured image along with the date and time.

4. Implementing a setting section for the system to train the face and the admin's vehicle number plate to make it super convenient. 

5. Predicting best car over a given price range of the admin.

## Contributor<a name="Authors"></a>
* Ayan Ghosh- Final Year Under-Graduate Student in University Institute of Technology, Burdwan [*See Linkedin*](https://www.linkedin.com/in/ayan-ghosh-4743841a1/)
