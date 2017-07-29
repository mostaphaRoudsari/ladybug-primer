## ![](../../images/icons/Terrain_Generator.png) Terrain Generator - [[source code]](https://github.com/mostaphaRoudsari/ladybug/tree/master/src/Ladybug_Terrain%20Generator.py)

![](../../images/components/Terrain_Generator.png)

This component uses Google Maps API to achieve elevation data and satellite images of the terrain generated. - This component requires an internet connection and it runs for free up to 2,500 requests per day. Once you go over this limit the component doesn't work. Note that each surface is a request, for example if you use a surface made by sub-surfaces 6x6, this will be 36 requests. For informations about the rules of use of Google Maps API, take a look at this link: https://developers.google.com/maps/pricing-and-plans/#details - Special thanks goes to Google Maps and the authors of gHowl. - 

#### Inputs
* ##### location [Required]
It accepts two type of inputs. a) latitude, longitude and elevation that represent WSG84 coordinates of the base point. You can achieve these type of coordinates from Google Maps or similar. e.g. 40.821796, 14.426439, 990 - b) location, you can obtain this type of input from "Ladybug_Construct Location", "Ladybug_Location Finder", "Ladybug_Import epw", "Ladybug_Import Location".
* ##### basePoint [Default]
Input a point here to georeference the terrain model.
* ##### radius [Default]
A radius to make the terrain 3D model in Rhino model units. The default is set to 100. - If you provide a big radius, this could require lots of time (also a couple of minutes).
* ##### type [Optional]
Select the type of output: 0 = rectangular mesh 1 = rectangular surface - The default value is 0.
* ##### numOfTiles [Default]
Set the number of tiles (e.g. 4, that means 4x4). If no input is connected this will be 3 (tiles: 3x3).
* ##### numDivision [Default]
Set the number of points for each tile. If no input is connected this will be 12 (grid: 13x13).
* ##### imgResolution [Default]
Connect an integer number which manage the quality of single satellite image. - The following list shows the approximate level of detail you can expect to see at each _imgResolution_ level: 1 = World 5 = Landmass/continent 10 = City 15 = Streets 20 = Buildings - The default value is 18.
* ##### mapType [Optional]
Connect an integer number, from 0 to 3, which manages the formats of map. - 0 = Satellite (default) 1 = Roadmap, specifies a standard roadmap image 2 = Terrain, it shows terrain and vegetation 3 = Hybrid, it specifies a hybrid of the satellite and roadmap image
* ##### folder [Optional]
The folder into which you would like to write the image file. This should be a complete file path to the folder.  If no folder is provided, the images will be written to C:/USERNAME/AppData/Roaming/Ladybug/IMG_Google.
* ##### runIt [Required]
Set to "True" to run the component and generate the 3D terrain model. 

#### Outputs
* ##### readMe!
...
* ##### pointsGeo
WSG84 coordinates of the grid points (longitude, latitude).
* ##### pointsXY
Cartesian coordinates of the grid points (X, Y).
* ##### pointsZ
Z values of the grid points. Connect this output to a Z vector to move the pointsXY in the right positions.
* ##### tiles
The area which will be calculated. If you want to visualize Satellite images connect this output to 'G' input of 'Human Custom Preview Material'.
* ##### imagePath
Satellite images from Google Static Maps API. Connect it to 'DB' input of 'Human Custom Preview Material' to apply textures to the 3d model or to the list of input surfaces.
* ##### terrain
3D terrain model.
* ##### origin
The origin (center) point of the "terrain" geometry.
* ##### elevation
Elevation of the origin_ input.


[Check Hydra Example Files for Terrain Generator](https://hydrashare.github.io/hydra/index.html?keywords=Ladybug_Terrain Generator)