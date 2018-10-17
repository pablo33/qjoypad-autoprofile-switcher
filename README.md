# qjoypad-autoprofile-switcher
Change qjoypad profile depending on a running process


This script launchs and kills automatically qjoypad process when a joystick device is plugged or unplugged.  

## Functionalities:  
- Launch or kill qjoypad process.
- Change/apply qjoypad profile on-live when a defined process is running.


## Why did I coded this script?
I recently moved to Kodi, and started using a wireless joypad by mapping buttons into qjoypad keystrokes for manage the Kodi fron-end.  
I noticed that unplugging and plugging the joystick cause qjoypad to stop working on Kodi, and I needed to manually update qjoypad's joysticks.  
With this script I do not care about launching/killing or update qjoypad process. Because it is automatically done.  


## How it works
Load the script at system startup or simply run it when needed.  
The script keeps running in memory and iterates every 10 seconds to check for the device joystick0 (_/dev/input/js0_) and it launches qjoypad if it is found.  
When a predefined process is found, the script update qjoypad to the desired layout/profile.  
Process and profiles relationship is stored inside the code and can be easily edited.  
If the script does not found any predefined process, the script just apply the default layout/profile.  

## How to run the code and keep it working
Just clone/copy or download the code and configure user variables to fit your needings.  
Obviously you have to install qjoypad by yourself before run this code and define at least one layout/profile (default profile).  
Once installed, you must open de code and configure with your needs.  

to run the code just type:  

    python3 qjoypad-autoprofile-switcher.py
