# R7 simulation input research — 2026-11-01

Manufacturer source:
https://shop.mikado-heli.de/LOGO-Helicopters/LOGO-200/LOGO-200-Bind-Fly-Combo-orange-blue.htm?ProdNr=05495&a=article&p=1003&shop=k_mikado_e
The Mikado product page lists VTX173 mm main blades,400 mm rotor diameter and approximately310 g ready-to-fly model mass. These are stock helicopter specifications; the user's200 g target is separate. Rotor radius200 mm is NOT the blade balance-point radius.

Earlier official manual:
https://www.mikado-heli.de/downloads/anleitungen/200/Logo%20200%20Manual%20V4.pdf
Lists replacement blades as VTX177, part05406. The173/177 naming difference is unresolved. Do not treat the earlier product designation as a precise measured length.

Search result:
No verified primary-source individual blade mass or spanwise center-of-mass location was found. Neither follows from blade length, rotor diameter or total aircraft mass. The earlier5 g/100 mm example remains hypothetical and was not approved as an actual measurement.

Supplier identification:
Searches for Vayu3D, Vayu3D PETG, and Vayu3D Bangalore did not identify a matching public PETG supplier technical data sheet. Do not assign the properties of another supplier to the user's intended print service. A supplier URL or exact company name is needed to resolve it.

Simulation status:
No structural FEA solve has run. Fusion preview simulation product remains unavailable through the MCP API. Most recent material inspection found the default Steel material on the model; it has not been replaced with an invented PETG material. No Steel-based strength or mass result should be used for the intended PETG print.

Request for the intended print service (draft only, not sent):
Please identify the PETG manufacturer and grade, share the technical data sheet and any printed XY/Z tensile/modulus data, and state the proposed printer, build orientation, nozzle/layer size, extrusion settings, wall count, infill and operating temperature limits. Please print a bearing-seat tolerance coupon before the grip. This item is an unpowered dimensional prototype; no flight qualification is claimed.

Blade data needed from manufacturer or measured hardware:
Mass of each blade; blade balance point relative to mounting-bolt center; mounting-bolt radius from main rotor axis; root thickness/width and sleeve dimensions. Sum bolt radius and outward spanwise balance distance to obtain the radius for centrifugal load calculation. Manufacturer-specific fatigue and proof-load requirements are also not established.
