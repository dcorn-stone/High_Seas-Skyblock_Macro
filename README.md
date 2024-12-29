# High_Seas-Skyblock_Macro


**Describtion**

A Macro made for skyblock farming(basically auto farming tool).

**Set up**

1.Install python

2.Open terminal and navigate to your working directory

3.create virtual environment:
 python3 -m venv env
  
4.activate virtual environment:
For Windows:
  .\env\Scripts\activate
For Mac/Linux:
  source env/bin/activate
  
5.install dependencies:
  pip install -r requirements.txt
or
  pip3 install -r requirements.txt
  
6.The program is now ready to start, click on the Farming_Macro.py file to start it.

7.After finished,type this command to deactivate the virtual environment:
  deactivate
  


**Instructions**

Time before the macro starts(seconds):
  The time before this program to start(set a time for yourself to get ready, otherwise it will be a mess).
  <If the program doesn't respond after you have pressed the start button, it's normal, because thie value is time that the program needs to sleep for>

  
press 'w':
  If your farm needs you to farm with 'w' and other keys pressed at the same time, tick this, otherwise just leave it blank.

  
Initial button/Change to:
  For example, if you need to farm to the right and farm back to the left after you changed your lane, set the 'initial button' to 'd' and set the 'change to' button to 'a'. -- If you only need to go forwards and backwards, set press 'w' to false and input 'w' and 's' as your 'initial button' and
  'change to' button.


wait for(s):
  set this number to the time that you take to get to the other end of the lane, this value is the time for the program to change from your 'initial button'     to the 'change to' button.


Lane change button(if needed):
 If you need to change lane with a different button, set this to the key needed. This will automatically press the button you entered while lane changing.


Cycle times:
  One cycle = With 'initial button' pressed + farm to the other end of the lane; change lane; press lane change button(if it is filled); with 'change to' button pressed + farm back to the side where you started farming
  This value depends how many lanes you have, e.g.  8 lanes = cycle 4 times.
