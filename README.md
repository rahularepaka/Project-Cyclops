# Project-Cyclops : Introducing Laser Tool for Killing Weeds ☘️
This Project is an attachment to destroy weeds faster by using 500mW Laser on the FarmBot v1.3

## Aknowledgement 💙
The Project Cyclops was possible due to our own hard work and the help and support of friends, family and members of the Farmbot and Center of
Excellence of Ai and Robotics. We take this opportunity to acknowledge their help and thank them for their assistance.

We would like to thank Director of Robotics & Artificial Intelligence at GEMS Education, Mr. Sreejit Chakrabarty, for his never-ending support and trust in our capabili􀆟es. He has been a great person throughout the history of the Project and gave us access to the farmbots to work on the project

Huge thanks to Mr.Ram Kumar who has helped us throughout the Project by sourcing the parts and helped us in teaching us on how to use different prototyping machines such as 3D printing

Special thanks to Marc from Farmbot who believed in us and helped us on working on this project and Farmbot Community

Team of Project Cyclops thanks each and every one of you for your valuable contribtioons.

## FarmBot Genesis v1.3 🧑‍🌾
We have tested Project Cyclops Laser Mount in Center of Excellence Artificial Intelligence and Robotics , GEMS Dubai American Academy

<img src="https://user-images.githubusercontent.com/10435564/121002144-14f00800-c79d-11eb-8d74-b2a611faf76d.jpg" width="700" height="500">

## FarmBot : Laser Weeder Tool ⚡
This is all-new laser killing weed removal for the Farmbot designed by our team. This tool is designed to destroy weeds using Thermal Technique : Laser by detecting weeds using Camera and weed detection

The Camera will detect for weeds and give those coordiantes to the farmbot and give add/subtract the off-set of the laser mount location and turn on the laser for 500ms and spray water on the location to complete the sequence

<img src="https://user-images.githubusercontent.com/10435564/121002727-b11a0f00-c79d-11eb-937e-5f4f70b7ab0f.jpg" width="350" height="600">      <img src="https://user-images.githubusercontent.com/10435564/121003590-c3e11380-c79e-11eb-8473-a690c3c9fd8b.jpg" width="350" height="600">

## Laser Details ⚡:
|     Laser     |    Details    |
| ------------- | ------------- |
| Model         | FB03-500      |
| Laser Power   | 500mW         |
| Wavelength    | 405nm         |
| Voltage       | 12V DC        |
| Beam Shape    | Dot           |

## Wiring of the Laser to the Farmdunio 🔌

<img src="https://user-images.githubusercontent.com/10435564/121004918-4a4a2500-c7a0-11eb-8fed-2a3c91473cd0.PNG" width="700" height="600">

## Programming Ardunio 💻

```
int relaypin = 6;

void setup(){
  pinMode(relaypin,OUTPUT);
}

void loop(){
  digitalWrite(relaypin, LOW);
}
```

## Weed Detection ☘️

<img src="https://user-images.githubusercontent.com/10435564/121005425-de1bf100-c7a0-11eb-8384-cee85e87f43e.png" width="400" height="400"> <img src="https://user-images.githubusercontent.com/10435564/121005493-ef64fd80-c7a0-11eb-9ebf-03b5c79b4f6a.png" width="400" height="400">

```
7 plants detected in image.

4 known plants inputted.
Plants at the following machine coordinates ( X Y ) with R = radius are to be saved:
    (   600   400 ) R = 45
    (   600   500 ) R = 45
    (   700   400 ) R = 25
    (   700   500 ) R = 25

2 plants marked for removal.
Plants at the following machine coordinates ( X Y ) with R = radius are to be removed:
    (   743   541 ) R = 6
    (   654   447 ) R = 6

2 plants marked for safe removal.
Plants at the following machine coordinates ( X Y ) with R = radius were too close to the known plant to remove completely:
    (   651   446 ) R = 7
    (   676   512 ) R = 3

4 detected plants are known or have escaped removal.
Plants at the following machine coordinates ( X Y ) with R = radius have been saved:
    (   700   410 ) R = 31
    (   596   396 ) R = 53
    (   698   485 ) R = 29
    (   600   499 ) R = 42
    
https://software.farm.bot/v14/The-FarmBot-Web-App/photos/weed-detection.html
```

## How Does it Work ?

```
Step 1 : On the Farmbot WebApp and click on sequences and create a sequence called “Weed Detection”
Step 2 : Select “Add Command” and choose Find Home to calibrate the farmbot location to home
Step 3 : Upon clicking on the new sequence,then click on “Add Command” and then select “Take a Photo” and choose “All Plants” from the drop-down list
Step 4 : Click on “Add Command” and then select “Detect Weeds” and then automtically the weeds points will be created on the Farmbot Webapp
Step 5 : Select on the “Weeds” from the WebApp and you can find list of active weeds
Step 6 : Run the New Sequence Created to kill the weeds using laser
```

## Test Runs

[![Laser Test 1](http://i.imgur.com/Ot5DWAW.png)](https://youtu.be/38SfoGEeuGA "Everything Is AWESOME")













