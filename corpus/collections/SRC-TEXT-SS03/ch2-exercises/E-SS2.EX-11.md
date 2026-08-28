---
schema: qual/card@1
id: E-SS2.EX-11
kind: exercise
title: "Cauchy estimates on a smaller disk"
classification:
  areas:
  - complex-analysis
  topics: ["Cauchy's Theorem", 'Contour Integration', 'Residues']
relations: []
review: draft
---

::: exercise
11. Let f be a holomorphic function on the disc $D _ { R _ { 0 } }$ centered at the origin and of radius $R _ { 0 }$

(a) Prove that whenever $0 < R < R _ { 0 }$ and $| z | < R ,$ , then

$$
f (z) = \frac {1}{2 \pi} \int_ {0} ^ {2 \pi} f (R e ^ {i \varphi}) \mathrm{Re} \left(\frac {R e ^ {i \varphi} + z}{R e ^ {i \varphi} - z}\right) d \varphi .
$$

(b) Show that

$$
\mathrm{Re} \left(\frac {R e ^ {i \gamma} + r}{R e ^ {i \gamma} - r}\right) = \frac {R ^ {2} - r ^ {2}}{R ^ {2} - 2 R r \cos \gamma + r ^ {2}}.
$$

[Hint: For the first part, note that if $w = R ^ { 2 } / \overline { { z } } ,$ , then the integral of $f ( \zeta ) / ( \zeta - w )$ around the circle of radius R centered at the origin is zero. Use this, together with the usual Cauchy integral formula, to deduce the desired identity.]
:::
