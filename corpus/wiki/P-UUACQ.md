---
schema: qual/card@1
id: P-UUACQ
kind: problem
title: Antiderivative of $\frac{x}{\sqrt{4-x^4}}$
classification:
  areas:
  - prelim
  topics:
  - integrals
  - u-substitution
  - trigonometric-substitution
relations: []
review: draft
solved: false
---

::: problem
4. $\displaystyle \int \frac {x}{\sqrt {4-x^4}} ~dx = \color {blue} {\frac {1}{2} \sin ^{-1} (\frac {x^2}{2})}$

- **Solution:** $2 \sin (u) = x^2$, $\cos (u) ~du = x ~dx$

- **Solution:** $\frac {1}{\sqrt {4-x^4}} \cdot x ~dx = \frac {1}{2 \cos (u)} \cdot \cos (u) ~du \frac {1}{2} ~du$

- **Another Solution:** $u = \frac {1}{2} x^2$, $du = x ~dx$

- **Another Solution:** $\frac {1}{\sqrt {4-x^4}} \cdot x ~dx = \frac {1}{2 \sqrt {1-u^2}} ~du$
:::
