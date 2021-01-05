# Lightsaber-script
Scripting to automatically generate the lightsaber effect in Blender.

Use motion tracking to create markers that follow the bottom and top of the hilt of your "lightsaber". After motion tracking, open a new script in Blender and copy paste the code under **generate_blade.py**, and click 'Run'. A 3D blade should now follow the motion of the hilt of your "lightsaber" in the video. Next, open a new script in Blender and copy paste the code under **compositing.py**, and click 'Run'. Make sure the settings of the RenderLayers node are set to 'scene' and 'RenderLayer'. Make sure the relevant original movie clip that you would like the lightsaber effect to be placed on is selected in the MovieClip node. Mess with the RGB curves node to change the color of your lightsaber!
