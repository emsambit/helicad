# R7 bottom-loaded metal stack

Assembly-access correction to R6. Outside appearance is retained, one solid plastic body. The former intermediate housing shoulder at z=2.5..3.9 mm has been removed. A continuous 6.15 mm pocket extends from z=0 to9.3 mm. A terminal shoulder at z=9.3..10.7 mm has a4.8 mm center opening; a relief pocket follows it. The spacer now separates the radial-bearing inner races without an intermediate plastic shoulder.

Nominal hardware envelope positions remain:
inner radial z=0..2.5; spacer2.5..3.9; outer radial3.9..6.4; washer6.4..6.5; thrust assembly6.5..9.3 mm.
Total nominal stack length9.3 mm. Pocket diametral allowance over6 mm hardware is0.15 mm (0.075 mm radial), uncalibrated for the user's printer. Axial stack is nominal with no established endplay/preload allowance; actual tolerances and shaft hardware determine the final design.

Insert FROM THE BOTTOM/circular bearing opening, deepest part first:
1. Complete thrust bearing assembly, oriented according to the hardware manufacturer's instructions, to the terminal shoulder.
2. 3.1 x4.5 x0.1 mm washer.
3. Outer3 x6 x2.5 mm radial bearing.
4. 3 x4.4 x1.4 mm metal spacer (4 mm OD alternative also clears).
5. Inner3 x6 x2.5 mm radial bearing, flush with the bottom mouth at nominal dimensions.

All five nominal part envelopes passed continuous annular swept-volume Boolean intersection checks from the bottom, with zero positive plastic overlap at their seats and along their insertion paths. Raw results: r7-top-bottom-audit.json. This checks straight nominal geometry, not physical print tolerances, tools, bearing race details, or shaft/retention hardware. Nominal final hardware intervals are adjacent and non-overlapping; keep this deepest-first assembly order. Top insertion is still obstructed by the narrow blade slot and is not required for this revised sequence.

Retention is not complete: the open bottom end still needs a verified metal shaft/fastener/washer retention and preload scheme. The relocated plastic thrust shoulder and its contact with the correct thrust race have not been structurally validated. The actual thrust-race groove/land dimensions are not supplied by the ID/OD/width envelope. This is an assembly-clearance prototype, not a flight-ready redesign. Do not run powered rotor tests.

Fusion verification: one solid body, volume1.725231 cm^3. Preview visually inspected. No FEA or printed-fit test completed. Blade-root and pitch-link interfaces remain provisional.
