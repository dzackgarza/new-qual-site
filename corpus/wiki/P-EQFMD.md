---
schema: qual/card@1
id: P-EQFMD
kind: problem
title: "$\\displaystyle \\int \\frac {1-\\sin(x)}{1 + \\cos(x)} ~dx = \\color {blue} {\\tan (\\frac {x}{2}) - \\ln (1 + \\tan ^2 (\\frac {x}{2}))} = \\color {blue} {\\tan (\\frac {x}{2}) - 2 \\ln (\\sec (\\frac {x}{2}))} = \\color {blue} {\\tan (\\frac {x}{2}) + 2 \\ln (\\cos (\\frac {x}{2}))} = \\color {blue} {\\tan (\\frac {x}{2}) + \\ln (1+\\cos (x))}\u200b$\u2026"
classification:
  areas:
  - prelim
  topics:
  - integrals
  - trigonometry
relations: []
review: draft
---

::: problem
1. $\displaystyle \int \frac {1-\sin(x)}{1 + \cos(x)} ~dx = \color {blue} {\tan (\frac {x}{2}) - \ln (1 + \tan ^2 (\frac {x}{2}))} = \color {blue} {\tan (\frac {x}{2}) - 2 \ln (\sec (\frac {x}{2}))} = \color {blue} {\tan (\frac {x}{2}) + 2 \ln (\cos (\frac {x}{2}))} = \color {blue} {\tan (\frac {x}{2}) + \ln (1+\cos (x))}​$

- **Solution:** $\frac {1-\sin(x)}{1 + \cos(x)} ~dx = \frac {1 - \frac {2u}{1 + u^2}}{1 + \frac {1 - u^2}{1 + u^2}} \cdot \frac {2}{1 + u^2} ~du = \frac {1 + u^2 - 2u}{1 + u^2 + 1 - u^2} \cdot \frac {2}{1 + u^2} ~du = \frac {1 + u^2 - 2u}{1 + u^2} ~du = 1 - \frac {2u}{1 + u^2} ~du$

2. $\displaystyle \int \frac {1+ \sin (x)}{1+\cos (x)} ~dx = \color {blue} {\tan (\frac {x}{2}) + \ln (1 + \tan ^2 (\frac {x}{2}))} = \color {blue} {\tan (\frac {x}{2}) + 2 \ln (\sec (\frac {x}{2}))} = \color {blue} {\tan (\frac {x}{2}) - 2 \ln (\cos (\frac {x}{2}))} = \color {blue} {\tan (\frac {x}{2}) - \ln (1+\cos (x))}$

- **Solution:** $\frac {1+ \sin (x)}{1+\cos (x)} ~dx = \frac {1 + \frac {2u}{1 + u^2}}{1 + \frac {1 - u^2}{1 + u^2}} \cdot \frac {2}{1 + u^2} ~du = \frac {1 + u^2 + 2u}{1 + u^2 + 1 - u^2} \cdot \frac {2}{1 + u^2} ~du = 1 + \frac {2u}{1 + u^2} ~du$

3. $\displaystyle \int \frac {1}{1 + \sin(x) + \cos(x)}~dx = \color {blue} {\ln(\tan(\frac {x}{2}) + 1)}$

- **Solution:** $\frac {1}{1 + \sin (x) + \cos (x)} ~dx = \frac {1}{1 + \frac {2u}{1 + u^2} + \frac {1 - u^2}{1 + u^2}} \cdot  \frac {2}{1 + u^2} ~du = \frac {1 + u^2}{1 + u^2 + 2u + 1 - u^2} \cdot  \frac {2}{1 + u^2} ~du = \frac {1}{1 + u} ~du​$

- **Used 2018**, *Unsolved*
:::
