## ![](../../images/icons/ENVI-Met_Building_Terrain.png) ENVI-Met Building Terrain

![](../../images/components/ENVI-Met_Building_Terrain.png)

Use this component to generate inputs for "LB ENVI-Met Spaces".

#### Inputs
* ##### buildings [Required]
Geometry that represent ENVI-Met buildings.
* ##### terrain [Optional]
Optional geometry that represent 
* ##### defaultMaterialsld [Default]
Default wall/roof property. Use this input to set default building materials.
* ##### wallMaterialsId [Optional]
Use this input to change wall materials.
* ##### roofMaterialsId [Optional]
Use this input to change roof materials.
* ##### runIt [Required]
Set to "True" to run the component and generate envimetBuildings and envimetTerrain.

#### Outputs
* ##### readMe!
...
* ##### envimetBuildings
Connect this output to "ENVI-Met Spaces" in order to add buildings to ENVI-Met model.
* ##### envimetTerrain
Connect this output to "ENVI-Met Spaces" in order to add a terrain to ENVI-Met model.


[Check Hydra Example Files for ENVI-Met Building Terrain](https://hydrashare.github.io/hydra/index.html?keywords=Ladybug_ENVI-Met Building Terrain)