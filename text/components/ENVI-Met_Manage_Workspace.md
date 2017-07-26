## ![](../../images/icons/ENVI-Met_Manage_Workspace.png) ENVI-Met Manage Workspace

![](../../images/components/ENVI-Met_Manage_Workspace.png)

Use this component to create a Workspace folder. - Connect "folder" output to ENVI-Met Spaces. - 

#### Inputs
* ##### workspaceFolder [Required]
Main folder where you have to save an Envimet project.
* ##### projectName [Default]
Name of Envimet project folder where you have to save: 1) EnviMet geometry file (*.INX) 2) Configuration file (*.SIM)
* ##### ENVImetInstallFolder [Optional]
Optional folder path for ENVImet4 installation folder.

#### Outputs
* ##### readMe!
...
* ##### folder
Envimet project folder. Connect it to "_folder" input of ENVI-Met Spaces


[Check Hydra Example Files for ENVI-Met Manage Workspace](https://hydrashare.github.io/hydra/index.html?keywords=Ladybug_ENVI-Met Manage Workspace)