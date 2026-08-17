---
schema: qual/card@1
id: P-VYOWN
kind: problem
title: "$\\displaystyle \\int \\frac {x + \\sin(x)}{1 + \\cos(x)}~dx = \\color {blue} {\\frac {x \\sin (x)}{1 + \\cos (x)}} = \\color {blue} {x \\tan \\frac {x}{2}}$ Solution: $u = x$, $v = \\frac {\\sin (x)}{1 + \\cos (x)}$, $du = dx$\u2026"
classification:
  areas:
  - prelim
  topics:
  - integrals
  - trigonometry
relations: []
review: draft
solved: false
---

::: problem
1. $\displaystyle \int \frac {x + \sin(x)}{1 + \cos(x)}~dx = \color {blue} {\frac {x \sin (x)}{1 + \cos (x)}} = \color {blue} {x \tan \frac {x}{2}}$

- **Solution:** $u = x$, $v = \frac {\sin (x)}{1 + \cos (x)}$, $du = dx$, $dv = \frac {\cos (x) + \cos ^2 (x) + \sin ^2 (x)}{(1 + \cos (x))^2} = \frac {1}{1 + \cos (x)} ~dx$

- **Solution:** $\int \frac {x + \sin(x)}{1 + \cos(x)}~dx = \int \frac {x}{1 + \cos(x)} ~dx + \int \frac {\sin (x)}{1 + \cos(x)} ~dx = x \cdot \frac {\sin (x)}{1 + \cos (x)} - \int \frac {\sin (x)}{1 + \cos(x)} ~dx  + \int \frac {\sin (x)}{1 + \cos(x)} ~dx$

2. $\displaystyle \int \frac {xe^x}{(e^x + 1)^2}~dx = \color {blue} {- \frac {x}{e^x+1} + x  - \ln(e^x+1)} = \color {blue} {\frac {xe^x}{e^x+1} - \ln(e^x  + 1)}$

- **Solution:** $u = x$, $v = - \frac {1}{e^x + 1}$, $du = dx$, $dv = \frac {e^x}{(e^x + 1)^2} ~dx$

- **Solution:** $- \frac {x}{e^x + 1} - \int - \frac {1}{e^x + 1} ~dx = - \frac {x}{e^x + 1} + \int (1 - \frac {e^x}{e^x + 1}) ~dx$
:::
