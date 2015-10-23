## DC_to_AC_derate_factor [![IMAGE](images/icons/DC_to_AC_derate_factor.png)]

![IMAGE](images/components/DC_to_AC_derate_factor.png)

Use this component to calculate overall DC to AC derate factor for Photovoltaics Surface's "DCtoACderateFactor_" input.

#### Inputs
* annualShading_ <Optional>: Losses due to buildings, structures, trees, mountains or other objects that prevent solar radiation from reaching the cells.
* age_ <Optional>: Losses over time due to weathering of the PV modules. The loss in performance is typically 1% per year. Example: for the 20th year of operation, an age loss of 19% would be appropriate. 
* snow_ <Optional>: Losses due to snow covering the array. The default value is zero, assuming either that there is never snow on the array, or that the array is kept clear of snow.
* wiring_ <Optional>: Resistive losses in the DC and AC wires connecting modules, inverters, and other parts of the system.
* soiling_ <Optional>: Losses due to dust, dirt, leaves, other wildlife droppings, snow, and other foreign matter on the surface of the PV module that prevent solar radiation from reaching the cells. Soiling is location- and weather-dependent. There are greater soiling losses in high-traffic, high-pollution areas with infrequent rain.
* mismatch_ <Optional>: Electrical losses due to slight differences caused by manufacturing imperfections between modules in the array that cause the modules to have slightly different current-voltage characteristics.
* availability_ <Optional>: Losses due to scheduled and unscheduled system shutdown for maintenance, grid outages, and other operational factors.
* connections_ <Optional>: Resistive losses in electrical connectors in the system.
* nameplateRating_ <Optional>: Losses due to accuracy of the manufacturer's nameplate rating. Field measurements of the electrical characteristics of photovoltaic modules in the array may show that they differ from their nameplate rating. Example: a nameplate rating loss of 5% indicates that testing yielded power measurements at STC that were 5% less than the manufacturer's nameplate rating.
* lightInducedDegradation_ <Optional>: Effect of the reduction in the array's power during the first few months of its operation caused by light-induced degradation of photovoltaic cells.

#### Outputs
* readMe!: ...
* totalLosses: PVWatts v5 representation of DCtoACderateFactor factor.
* DCtoACderateFactor: Factor which accounts for various locations and instances in a PV system where power is lost from DC system nameplate to AC power.


[Check Hydra Example Files for DC_to_AC_derate_factor](https://hydrashare.github.io/hydra/index.html?keywords=DC_to_AC_derate_factor)