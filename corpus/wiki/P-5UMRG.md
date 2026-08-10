---
schema: qual/card@1
id: P-5UMRG
kind: problem
title: "5. $\\displaystyle \\int \\frac {\\sqrt {x^2-a^2}}{x} ~dx = \\tan (\\sec ^{-\u2026"
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

5. $\displaystyle \int \frac {\sqrt {x^2-a^2}}{x} ~dx = \tan (\sec ^{-1} (\frac {x}{a})) - a \sec ^{-1} (\frac {x}{a}) = \color {blue} {\sqrt {x^2-a^2} - a \sec ^{-1} (\frac {x}{a})} = \color {blue} {\sqrt {x^2-a^2} - a \tan ^{-1} (\frac {\sqrt {x^2 - a^2}}{a})}​$

- **Solution:** $\sec (u) = \frac {1}{a} x$, $\tan (u) \sec (u) ~du = \frac {1}{a} ~dx$

- **Solution:** $\frac {\sqrt {x^2-a^2}}{x} ~dx = \frac {a \tan (u)}{a \sec (u)} \cdot a \tan (u) \sec (u) ~du = a \tan ^2 (u) ~du = a (\sec ^2 (u) - 1) ~du$

  1. $\displaystyle \int \frac {\sqrt {x^2-1}}{x} ~dx = \color {blue} {\sqrt {x^2-1} - \sec ^{-1} (x)} = \color {blue} {\sqrt {x^2-1} - \tan ^{-1} (\sqrt {x^2-1})}$

  2. $\displaystyle \int \frac {\sqrt {x^2-9}}{x} ~dx = \color {blue} {\sqrt {x^2-9} - 3 \sec ^{-1} (\frac {x}{3})} = \color {blue} {\sqrt {x^2-9} - 3 \tan ^{-1} (\frac {\sqrt {x^2-9}}{3})}$

  - **Used 2019**, *Unsolved*
