## ![](../../images/icons/Open_EPW_And_STAT_Weather_Files.png) Open EPW And STAT Weather Files - [[source code]](https://github.com/mostaphaRoudsari/ladybug/tree/master/src/Ladybug_Open%20EPW%20And%20STAT%20Weather%20Files.py)

![](../../images/components/Open_EPW_And_STAT_Weather_Files.png)

Use this component to automatically download a .zip file from the Department of Energy's (DOE) database, unzip the file, and open both the .epw and .stat weather files into Grasshopper. The component requires the URL of the zipped file for the specific climate that you want to import from the DOE's website.  To open the DOE's website, use the Ladybug_download EPW Weather File component. Note that you can copy the zip file URL to your clipboard by right-clicking on the "ZIP" link for the climate that you want on the DOE's website and choosing "Copy Link Address." - 

#### Inputs
* ##### weatherFileURL [Required]
A text string representing the .zip file URL from the Department of Energy's (DOE's) website. To open the DOE's website, use the Ladybug_download EPW Weather File component. Note that you can copy the zip file URL to your clipboard by right-clicking on the "ZIP" link for the climate that you want on the DOE's website and choosing "Copy Link Address."
* ##### workingDir [Optional]
An optional text string representing a file path to a working directory on your computer where you would like to download and unzip the file.  If nothing is set, the weather files will be downloaded to C:/ladybug/ and placed in a folder with the name of the weather file location.

#### Outputs
* ##### epwFile
The file path of the downloaded epw file.
* ##### statFile
The file path of the downloaded stat file.


[Check Hydra Example Files for Open EPW And STAT Weather Files](https://hydrashare.github.io/hydra/index.html?keywords=Ladybug_Open EPW And STAT Weather Files)