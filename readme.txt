This is a thematic encounter display for Pathfinder, D&D, and other tabletop games.

This program is designed to fullscreen overtop a display. Create a folder in the "Encounters" directory to be your encounter, entering the plain name of the folder when starting the program to access it. Add phases labeled "Phase_1.txt" and up with dialogue to add to the length. .pngs labeled in the same style will be pulled up along with the next phase's text as you advance phases. In the upper left-hand corner there is an encounter round tracker.

In addition, to finish the encounter in a spectacular way, there is a "rainbow_text.txt" file in which you can put a phrase for usage in a shifting rainbow of color. You will need to configure "r_text_point" in the config.py file in order to adjust where the rainbow text begins.

Delay in the config folder controls how fast the text types out.

Controls are mapped as follows:

Tab - enable or disable fullscreen
Return - Next text line
Space Bar - Phase change
Left Shift - Rainbow Text Activation (replaces and locks "Next text line" entirely, only able to be used during the final phase)
Right Shift - increase round
Back Space - Decrease round
Right Control - enable or disable round visibility
Escape - exit program

Included is the 5-phase encounter this was built for as an example.

To access in your console use: python3 main.py "The Ruby Knight"