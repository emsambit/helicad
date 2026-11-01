# R6 top and bottom dimensional audit

Definitions: bottom = circular bearing opening at axial z=0; top = blade/fork end at z=29.5 mm. This is independent of the orientation of the preview image.

Method: Fusion temporary BRep boolean intersections between the plastic and continuous coaxial annular swept volumes. Each part was moved straight along the bearing axis, without tilt, from outside the grip to its designated seat. The test uses ideal nominal cylindrical/annular hardware envelopes and the empty plastic grip, not printed parts or installed hardware. It is a continuous geometry test within Fusion kernel tolerances, rather than the earlier finite point sampling. No design changes were made.

Measured/model dimensions in mm:
- Bottom radial pocket diameter 6.15, z=0..2.5.
- Shoulder bore diameter 4.8, z=2.5..3.9; shoulder axial thickness 1.4.
- Outer bearing passage nominal diameter 6.15, starts z=3.9; source cut extends to17.6 but is interrupted/opened by the oval window and fork slot above the housing.
- Top fork gap 4.0; cheek thickness 3.0 each; outer width across cheeks 10.0; cheek width 9.0.
- Oval access width 6.8; total axial length8.4, z=11.6..20.
- Housing OD12; cylindrical outer section z=0..8, followed by loft to z=12.
- Blade bolt hole diameter2.2 at z=25; pitch hole diameter1.8.

For each nominal seated part, the plastic intersection volume was zero:
| Part | ID x OD x width (mm) | Axial seat z (mm) | Straight from top | Straight from bottom |
|---|---|---|---|---|
| Inner radial |3 x 6 x 2.5|0..2.5|Blocked|Clear|
| Spacer, larger callout|3 x 4.4 x 1.4|2.5..3.9|Blocked|Clear in empty grip|
| Outer radial|3 x 6 x 2.5|3.9..6.4|Blocked|Blocked|
| Washer|3.1 x 4.5 x0.1|6.4..6.5|Blocked|Clear in empty grip|
| Thrust assembly envelope|3 x 6 x2.8|6.5..9.3|Blocked|Blocked|

6 mm parts have0.15 mm nominal diametral clearance in6.15 mm pockets (0.075 mm per side). The4.4 mm spacer has0.4 mm diametral clearance through the4.8 mm shoulder bore. The4.5 mm washer has0.3 mm diametral clearance through that bore. The4 mm fork slot obstructs all of these parts with OD greater than4 mm during straight insertion from above.

The image contains conflicting spacer ODs:4 mm in the list and4.4 mm in the callout. The4 mm alternative was also checked; see raw audit JSON. Even if the nominal4 mm spacer has no volumetric collision through the4 mm top slot, that is zero assembly clearance, not an acceptable printed-fit allowance.

Bottom passage clearance for a spacer or washer does NOT mean it can pass through an already installed radial bearing, whose nominal ID is3 mm. Assembly order matters. R6 therefore relies on the oval side openings to install the outer stack before fitting the rotor blade; it does not provide top/bottom-only assembly of the full stack. R6 is not suitable if every component must be installed exclusively from those two axial ends.

Retention fasteners, shaft and preload are not validated. Printed tolerances and flight strength remain unverified. The image dimensions do not include hardware manufacturing tolerances, so an exact as-built fit cannot be established here.
