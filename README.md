# Project-Cyclops : Laser Tool for Killing Weeds ☘️
This Project is an attachment to destroy weeds faster by using 500mW Laser on the FarmBot v1.3

❤️ This Project is in collaboration between Farmbot Inc and the Center of Excellence of Artificial Intelligence and Robotics ❤️

## Aknowledgement 💙
The Project Cyclops was possible due to our own hard work and the help and support of friends, family and members of the Farmbot and Center of
Excellence of Ai and Robotics. We take this opportunity to acknowledge their help and thank them for their assistance.

We would like to thank Director of Robotics & Artificial Intelligence at GEMS Education, Mr. Sreejit Chakrabarty, for his never-ending support and trust in our capabili􀆟es. He has been a great person throughout the history of the Project and gave us access to the farmbots to work on the project

Huge thanks to Mr.Ram Kumar who has helped us throughout the Project by sourcing the parts and helped us in teaching us on how to use different prototyping machines such as 3D printing

Special thanks to Marc from Farmbot who believed in us and helped us on working on this project and Farmbot Community

Team of Project Cyclops thanks each and every one of you for your valuable contribtioons.

## FarmBot Genesis v1.3 🧑‍🌾
We have tested Project Cyclops Laser Mount in Center of Excellence Artificial Intelligence and Robotics , GEMS Dubai American Academy

<img src="https://user-images.githubusercontent.com/10435564/121002144-14f00800-c79d-11eb-8d74-b2a611faf76d.jpg" width="800" height="500" align="center">

## FarmBot : Laser Weeder Tool ⚡
This is all-new laser killing weed removal for the Farmbot designed by our team. This tool is designed to destroy weeds using Thermal Technique : Laser by detecting weeds using Camera and weed detection

The Camera will detect for weeds and give those coordiantes to the farmbot and give add/subtract the off-set of the laser mount location and turn on the laser for 500ms and spray water on the location to complete the sequence

<img src="https://user-images.githubusercontent.com/10435564/121002727-b11a0f00-c79d-11eb-937e-5f4f70b7ab0f.jpg" width="400" height="600" align="center">      <img src="https://user-images.githubusercontent.com/10435564/121003590-c3e11380-c79e-11eb-8473-a690c3c9fd8b.jpg" width="400" height="600" align="center">

## Laser Details ⚡:
|     Laser     |    Details    |
| ------------- | ------------- |
| Model         | FB03-500      |
| Laser Power   | 500mW         |
| Wavelength    | 405nm         |
| Voltage       | 12V DC        |
| Beam Shape    | Dot           |

## Wiring of the Laser to the Farmdunio 🔌

<img src="https://user-images.githubusercontent.com/10435564/121004918-4a4a2500-c7a0-11eb-8fed-2a3c91473cd0.PNG" width="600" height="600" align="center">

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

<img src="https://user-images.githubusercontent.com/10435564/121005425-de1bf100-c7a0-11eb-8384-cee85e87f43e.png" width="400" height="400" align="center"> <img src="https://user-images.githubusercontent.com/10435564/121005493-ef64fd80-c7a0-11eb-9ebf-03b5c79b4f6a.png" width="400" height="400" align="center">

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

## How Does it Work ? 🤔

```
Step 1 : On the Farmbot WebApp and click on sequences and create a sequence called “Weed Detection”
Step 2 : Select “Add Command” and choose Find Home to calibrate the farmbot location to home
Step 3 : Upon clicking on the new sequence,then click on “Add Command” and then select “Take a Photo” and choose “All Plants” from the drop-down list
Step 4 : Click on “Add Command” and then select “Detect Weeds” and then automtically the weeds points will be created on the Farmbot Webapp
Step 5 : Select on the “Weeds” from the WebApp and you can find list of active weeds
Step 6 : Run the New Sequence Created to kill the weeds using laser
```

## Report 📚

[Report_C.pdf](https://github.com/rahularepaka/Project-Cyclops/files/6608697/Report_C.pdf)


## Test Runs 🧪

[![Laser Test 1](https://res.cloudinary.com/marcomontalbano/image/upload/v1623064366/video_to_markdown/images/youtube--38SfoGEeuGA-c05b58ac6eb4c4700831b2b3070cd403.jpg)](https://youtu.be/38SfoGEeuGA "Laser Test 1")

[![Laser + Water Test](https://res.cloudinary.com/marcomontalbano/image/upload/v1623064412/video_to_markdown/images/youtube--uzuAaT0RbTk-c05b58ac6eb4c4700831b2b3070cd403.jpg)](https://www.youtube.com/watch?v=uzuAaT0RbTk&list=PLmqQlLNnAZeNxKtvdTFGKsISi_beS0jqv&index=5 "Laser + Water Test")

[![Plant Test 1 + Water](https://res.cloudinary.com/marcomontalbano/image/upload/v1623064460/video_to_markdown/images/youtube--hvryX2yWKMo-c05b58ac6eb4c4700831b2b3070cd403.jpg)](https://www.youtube.com/watch?v=hvryX2yWKMo&list=PLmqQlLNnAZeNxKtvdTFGKsISi_beS0jqv&index=6 "Plant Test 1 + Water")

[![Plant Test 2 + Water](https://res.cloudinary.com/marcomontalbano/image/upload/v1623064481/video_to_markdown/images/youtube--CZevGsG4VxA-c05b58ac6eb4c4700831b2b3070cd403.jpg)](https://www.youtube.com/watch?v=CZevGsG4VxA&list=PLmqQlLNnAZeNxKtvdTFGKsISi_beS0jqv&index=3 "Plant Test 2 + Water")

[![Plant Test 3 + Water](https://res.cloudinary.com/marcomontalbano/image/upload/v1623064501/video_to_markdown/images/youtube--4mvnTx-ELzc-c05b58ac6eb4c4700831b2b3070cd403.jpg)](https://www.youtube.com/watch?v=4mvnTx-ELzc&list=PLmqQlLNnAZeNxKtvdTFGKsISi_beS0jqv&index=7 "Plant Test 3 + Water")

[![Plant Test 4 + Water](https://res.cloudinary.com/marcomontalbano/image/upload/v1623064528/video_to_markdown/images/youtube--tyxHVaaTqK8-c05b58ac6eb4c4700831b2b3070cd403.jpg)](https://www.youtube.com/watch?v=tyxHVaaTqK8&list=PLmqQlLNnAZeNxKtvdTFGKsISi_beS0jqv&index=1 "Plant Test 4 + Water")

[![Top View Laser Test ](https://res.cloudinary.com/marcomontalbano/image/upload/v1623064559/video_to_markdown/images/youtube--y0UsBOgl0RE-c05b58ac6eb4c4700831b2b3070cd403.jpg)](https://www.youtube.com/watch?v=y0UsBOgl0RE&list=PLmqQlLNnAZeNxKtvdTFGKsISi_beS0jqv&index=8 "Top View Laser Test ")

[![Laser Test 3](https://res.cloudinary.com/marcomontalbano/image/upload/v1623064592/video_to_markdown/images/youtube--mm0UvqF8U7o-c05b58ac6eb4c4700831b2b3070cd403.jpg)](https://www.youtube.com/watch?v=mm0UvqF8U7o&list=PLmqQlLNnAZeNxKtvdTFGKsISi_beS0jqv&index=9 "Laser Test 3")


## Team Members 👷‍♂️
- Rahul Arepaka - Project Lead and Designer
- Ethan Hadimani - 3D Mount Designer
- Sanjay Pramod - Farmbot Sequence Programmer
- Atin Sakkeer - Programmer

 

