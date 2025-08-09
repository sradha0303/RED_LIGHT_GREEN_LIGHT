Red Light Green light

Developer: Sradha S - [College of Engineering and Management Punnapra, KTU University]

Project Description
Red Light Green light is an adrenaline-pumping Pygame recreation of the Squid Game’s "Red Light, Green Light" challenge. Guide a tracksuit-clad character through a playground littered with obstacles, dodging a 50-second timer and a doll that flips between Green Light (go!) and Red Light (freeze!). With vibrant images and full-screen chaos, it’s a test of nerves and precision.

The Problem
In a tragically calm world where people saunter without fear, there’s a catastrophic shortage of life-or-death movement games. Why stroll peacefully when you could be paralyzed by a doll’s stare, risking elimination for a single misstep? Humanity’s lack of panic is a crisis only we can fix!

The Solution
Left Right Left throws you into a digital Squid Game arena! Dodge cones, sprint under a 50-second guillotine, and freeze when the doll screams “Red Light!” With a playground backdrop, a custom player, and a creepy doll, we’re curing the non-existent epidemic of excessive chill. Embrace the terror—nobody asked for it, but you’re getting it!

Technical Details
Technologies/Components Used
For Software:
Languages Used: Python 3.9+
Frameworks Used: Pygame
Libraries Used:
pygame: Handles graphics, input, and game loop.
asyncio: Ensures a smooth game loop with consistent frame rate.
random: Generates random obstacle positions and light switch intervals.
math: Rounds up timer display.
os: Loads images from the assets/ folder.

Tools Used:
Visual Studio Code (or preferred IDE) for coding.
File Explorer to manage assets/ folder.
Image editors (e.g., GIMP, Photopea) for preparing PNGs.
Terminal/Command Prompt for running the game and installing dependencies.

Implementation
For Software
Installation:
Ensure Python 3.9+ is installed:
python --version
Install Pygame:
pip install pygame
Set up the project directory in C:\Users\sradha s\Desktop\chronomancers_gambit:
hackathon/
├── red_light_green_light.py
├── assets/
│   ├── background.png
│   ├── player.png
│   ├── obstacle.png
│   ├── doll_green.png
│   └── doll_red.png

Place images in the assets/ folder:
Background: Playground/field (e.g., from Wallpapers.com).
Player: Tracksuit character (e.g., from PNGPlay.com).
Obstacle: Cone/barrier (e.g., from CleanPNG.com).
Doll: Squid Game doll (Young-hee) for green/red light (e.g., from PNGArts.com).

Run:
Navigate to the project directory:
cd C:\Users\sradha s\Desktop\hackathon
Run the game:
python red_light_green_light.py

Gameplay:
Use arrow keys to move the player (speed: 2 pixels/frame) during Green Light.
Freeze during Red Light to avoid elimination.
Dodge 5 obstacles to prevent game over.
Reach the finish line (white line at y = HEIGHT // 4) within 50 seconds to win.
Press R to restart after win/loss; press ESC to quit.



Project Documentation For Software

Project Location: C:\Users\sradha s\Desktop\hackathon
Main Script: red_light_green_light.py
Features:
Full-Screen Display: Adapts to monitor resolution (e.g., 1920x1080) via pygame.display.Info().
Images: Loads background.png (full-screen playground), player.png (50x50 character), obstacle.png (50x50 cones), doll_green.png, and doll_red.png (100x100 Young-hee) from assets/.
Fallback Drawings: Uses shapes (rectangles, circles, triangles) if images fail, with a Squid Game-themed doll (head, eyes, green/red body).
Gameplay Mechanics:
50-second timer; game over if time expires.
5 randomly placed obstacles; collision triggers game over.
Doll switches between Green Light (move) and Red Light (stop) every 2-5 seconds.
Moving during Red Light triggers game over.
Player moves at 2 pixels/frame with arrow keys.
Win by reaching the finish line within 50 seconds.
Game over reasons: “Time’s Up!”, “Moved During Red Light”, “Hit Obstacle”.
Controls: Arrow keys to move, R to restart, ESC to quit.


Image Credits:
Background: Wallpapers.com
Doll: PNGArts.com
Player: PNGPlay.com
Obstacle: CleanPNG.com


Dependencies: Python 3.9+, Pygame (pip install pygame).
How to Test:
Verify images are in assets/ with correct names.
Run python red_light_green_light.py.
Check full-screen visuals, timer, obstacle collisions, and light switching.
If images don’t load, check terminal for errors (e.g., file not found).


Troubleshooting:
Images Missing: Ensure assets/background.png, etc., exist. Verify paths/names.
Lag: Try fixed resolution (e.g., pygame.display.set_mode((1280, 720))).
Font Issues: Replace arial with pygame.font.SysFont(None, 48).

Sceenshots:
https://drive.google.com/drive/folders/1tsiVeCA0QoWOUbYkg2OUsP0KUpzvVsZ_

Video:
https://drive.google.com/drive/folders/1u-C84s0BTPgP6Gm5Rz0Ndt4AiwlK49tC







