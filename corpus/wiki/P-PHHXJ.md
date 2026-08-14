---
schema: qual/card@1
id: P-PHHXJ
kind: problem
title: "$\\displaystyle \\int \\sqrt {1 -x^2} ~dx = \\frac {1}{2} (\\sin ^{-1} (x) + \\frac {1}{2} \\sin (2 \\sin ^{-1} (x))) = \\color {blue} {\\frac {1}{2} (\\sin ^{-1} (x) + x \\sqrt {1 - x^2})}$ Solution: $\\sin (u) = x\u200b$\u2026"
classification:
  areas:
  - prelim
  topics:
  - integrals
  - trigonometric-substitution
relations: []
review: draft
---

1. $\displaystyle \int \sqrt {1 -x^2} ~dx = \frac {1}{2} (\sin ^{-1} (x) + \frac {1}{2} \sin (2 \sin ^{-1} (x))) = \color {blue} {\frac {1}{2} (\sin ^{-1} (x) + x \sqrt {1 - x^2})}$

- **Solution:** $\sin (u) = x​$, $\cos (u) ~du = dx​$

- **Solution:** $\sqrt {1 -x^2} ~dx = \sqrt {1 - (\sin (u))^2} \cos (u) ~du = \cos ^2 (u) ~du = \frac {1}{2} (1 + \cos (u)) ~du​$

  1. $\displaystyle \int_{-4}^{4} \sqrt {16 - x^2} ~dx = \color {blue} {8\pi}$

  - **Solution:** the area of semi-circle

  - **Used 2019**

  2. $\displaystyle \int_{-1}^{1} (1+x)\sqrt {1-x^2} ~dx = \color {blue} {\frac {1}{2} \pi}$

  - **Solution:** $\int_{-1}^{1} (1+x)\sqrt {1-x^2} ~dx = \int_{-1}^{1} \sqrt {1-x^2} ~dx + \int_{-1}^{1} \sqrt {1-x^2} x ~dx = \frac {1}{2} \pi + \frac {2}{3} (1-x^2)^{\frac {3}{2}} |_{-1}^{1}$

  - **Used 2019**
