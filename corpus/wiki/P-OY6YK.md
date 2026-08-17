---
schema: qual/card@1
id: P-OY6YK
kind: problem
title: Integrals of $\frac{x^2+2x+1}{x\sqrt{x^2-1}}$ and $\frac{x+16}{\sqrt{x^2-4x+8}}$
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
1. $\displaystyle \int \frac {x^2 + 2x + 1}{x\sqrt {x^2-1}}~dx = \color {blue} {2\ln(\sqrt {x^2-1}+x)+\sqrt {x^2-1}+\sec ^{-1} (x)}$

- **Solution:** $\sec (u) = x$, $\tan (u) \sec (u) ~du = dx$

- **Solution:** $\frac {x^2 + 2x + 1}{x\sqrt {x^2-1}} ~dx = (\frac {x^2}{x\sqrt {x^2-1}} + \frac {2x + 1}{x\sqrt {x^2-1}}) ~dx = \frac {2}{\tan (u)} \cdot \tan (u) \sec (u) ~du + (\frac {2}{\sqrt {x^2-1}} + \frac {1}{x\sqrt {x^2-1}}) ~dx$

- **Used 2019**

2. $\displaystyle \int \frac {x+16}{\sqrt {x^2-4x+8}} ~dx = \color {blue} {\sqrt {x^2-4x+8} + 18 \ln (\sqrt {x^2-4x+8} + x - 2)}$

- **Solution:** $2 \tan (u) = x - 2$, $ \sec ^2 (u) ~du = dx$

- **Solution:** $\frac {x+16}{\sqrt {x^2-4x+8}} ~dx = \frac {2 \tan (u) + 18}{2 \sec (u)} \cdot 2 \sec ^2 (u) ~du = 2 (\tan (u) \sec (u) + 9 \sec (u)) ~du$

- **Used 2019**, *Unsolved*
:::
