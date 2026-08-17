---
schema: qual/card@1
id: P-XRZVW
kind: problem
title: "$\\displaystyle \\int \\frac {1}{\\sqrt {x^2 + 25}} ~dx = \\ln (\\frac {x}{5} + \\sec (\\tan ^ {-1} (\\frac {x}{5}))) = \\color {blue} {\\ln(x + \\sqrt {x^2+25})}$ Solution: $\\tan (u) = \\frac {1}{5} x$\u2026"
classification:
  areas:
  - prelim
  topics:
  - integrals
  - trigonometric-substitution
relations: []
review: draft
solved: false
---

::: problem
8. $\displaystyle \int \frac {1}{\sqrt {x^2 + 25}} ~dx = \ln (\frac {x}{5} + \sec (\tan ^ {-1} (\frac {x}{5}))) = \color {blue} {\ln(x + \sqrt {x^2+25})}$

- **Solution:** $\tan (u) = \frac {1}{5} x$, $\sec ^2 (u) ~du = \frac {1}{5} ~dx$

- **Solution:** $\frac {1}{\sec (u)} \cdot \sec ^2 (u) ~du = \sec (u) ~du$

- **Used 2018**, *Unsolved*

9. $\displaystyle \int \frac {1}{(1+x^2)^{\frac {3}{2}}} ~dx = \sin (\tan ^{-1} (x)) = \color {blue} {\frac {x}{\sqrt {1+x^2}}}$

- **Solution:** $\tan (u) = x$, $\sec ^2 (u) ~du = dx$

- **Solution:** $\frac {1}{(1+x^2)^{\frac {3}{2}}} ~dx = \frac {1}{\sec ^3 (u)} \cdot \sec ^2 (u) ~du = \cos (u) ~du$
:::
