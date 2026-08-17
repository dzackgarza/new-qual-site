---
schema: qual/card@1
id: P-W6TOK
kind: problem
title: "$\\displaystyle \\int \\frac {x}{x^4-16} ~dx = \\color{blue} {\\frac {1}{16} (\\ln (x^2 - 4) - \\ln (x^2 + 4))}$ Solution: $u =x^2$, $du = 2x ~dx$ Solution\u2026"
classification:
  areas:
  - prelim
  topics:
  - integrals
  - u-substitution
  - partial-fractions
relations: []
review: draft
solved: false
---

::: problem
1. $\displaystyle \int \frac {x}{x^4-16} ~dx = \color{blue} {\frac {1}{16} (\ln (x^2 - 4) - \ln (x^2 + 4))}$

- **Solution:** $u =x^2$, $du = 2x ~dx$

- **Solution:** $\frac {1}{2} \cdot  \frac {2x ~dx}{x^4 - 16} = \frac {1}{2} \frac {du}{u^2 - 16} = \frac {1}{16} (\frac {1}{u - 4} - \frac {1}{u + 4}) ~du$

2. $\displaystyle \int \frac {x\tan^{-1}(x)}{(x^2+1)^2} ~dx = \color {blue} {- \frac {1}{2 (1 + x^2)} \tan^{-1}(x) + \frac {1}{4 (1 + x^2)} + \frac {1}{4} \tan ^{-1} (x)}$

- **Solution:** $u_1 = \tan ^{-1} (x)$, $v_1 = - \frac {1}{2(x^2 + 1)}$, $du_1 = \frac {1}{x^2 + 1} ~dx$,$dv_1 = \frac {x}{(x^2+1)^2} ~dx$

- **Solution:** $u_2 = \tan ^{-1} (x)$, $\tan (u_2) = x$, $\sec ^2 (u_2) ~du_2 = dx$

- **Solution:** $- \frac {1}{2(x^2 + 1)} \tan ^{-1} (x) - \int - \frac {1}{2(x^2 + 1)^2} ~dx = - \frac {1}{2(x^2 + 1)} \tan ^{-1} (x) + \int \frac {1}{(\sec ^2 (u_2))^2} \cdot \sec ^2 (u_2) ~du_2 = - \frac {1}{2(x^2 + 1)} \tan ^{-1} (x) + \int \cos ^2 (u_2) ~du_2$

- **Used 2019**
:::
