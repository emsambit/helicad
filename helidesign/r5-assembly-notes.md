# R5 metal hardware fit and assembly access

R5 remains one continuous round printed grip. The printable file contains plastic only.

Per-grip hardware (the image quantities are for two grips):
- 2 radial bearings, 3 x 6 x 2.5 mm.
- 1 metal spacer, 3 mm ID x up to 4.4 mm OD x 1.4 mm long. Image list says 4 mm OD but callout says 4.4; the larger envelope was checked.
- 1 washer, 3.1 x 4.5 x 0.1 mm.
- 1 thrust bearing assembly, 3 x 6 x 2.8 mm total envelope.

Nominal axial placement, measured from the bottom bearing opening:
- Inner radial bearing: z=0 to 2.5 mm.
- Spacer: z=2.5 to 3.9 mm.
- Outer radial bearing: z=3.9 to 6.4 mm.
- Washer: z=6.4 to 6.5 mm.
- Thrust bearing: z=6.5 to 9.3 mm.

Assembly before fitting the rotor blade:
1. Insert the inner radial bearing from the bottom opening.
2. Insert the spacer through the side window, move it to the bearing axis, and slide it down to its nominal position.
3. Insert the outer radial bearing through that window and slide it down.
4. Insert the washer, then the thrust bearing through the window. Keep the thrust races and cage in the manufacturer-specified orientation; the 2.8 mm value is the full assembly width, not each race.
5. Complete shaft, metal retention hardware and preload setup using a verified assembly design. These have not been defined or validated here. Do not rely on the PETG bearing fit to retain blades.

Access geometry:
- Side window diameter 7.2 mm at z=15.8 mm, through the Y direction.
- Outer pocket/assembly passage diameter 6.15 mm, z=3.9 to 17.6 mm.
- Bottom radial pocket diameter 6.15 mm, z=0 to 2.5 mm.
- Shoulder relief bore diameter 4.8 mm, z=2.5 to 3.9 mm.
- Top blade slot remains 4 mm; bearings enter from the SIDE, not straight down from the top.
- A 6 mm OD x 2.8 mm thick bearing has a 6.62 mm diagonal in its side-window projection, below the 7.2 mm opening diameter.

Verification:
Fusion returned one solid body. Sampled nominal insertion paths for all five hardware envelopes found zero points inside the plastic; results are in r5-clearance-sampling.json. This is a finite sampling check, not a continuous collision proof, a tolerance analysis, or a physical assembly test. It checks hardware against plastic only, without shaft, tools, retention fasteners, or already installed hardware. CAD radial clearance for 6 mm OD parts is 0.075 mm per side before printing errors; calibrate bearing-fit allowance on the intended printer.

Limitations:
Blade-root and sleeve dimensions remain provisional. Bearing seating/retention and preload require verification. The access windows reduce the fork section; no strength improvement or adequate fatigue life has been established. The earlier load-screening plate equations do not validate this revision. Unpowered fit prototype only, not approved for powered rotor operation.
