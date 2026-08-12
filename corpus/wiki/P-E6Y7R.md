---
schema: qual/card@1
id: P-E6Y7R
kind: problem
title: "$\\displaystyle \\int x\\sin^{-1}(\\frac {1}{x}) ~dx = \\color {blue} {\\frac {1}{2} (x^2 \\csc ^{-1} (x) + \\sqrt {x^2 - 1})} = \\color {blue} {\\frac {1}{2} (x^2 \\sin ^{-1} (\\frac {1}{x}) + \\sqrt {x^2 - 1})}$ Solution: $x \\sin ^{-1} (\\frac {1}{x}) = x \\csc ^{-1} (x)$\u2026"
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

1. $\displaystyle \int x\sin^{-1}(\frac {1}{x}) ~dx = \color {blue} {\frac {1}{2} (x^2 \csc ^{-1} (x) + \sqrt {x^2 - 1})} = \color {blue} {\frac {1}{2} (x^2 \sin ^{-1} (\frac {1}{x}) + \sqrt {x^2 - 1})}$

- **Solution:** $x \sin ^{-1} (\frac {1}{x}) = x \csc ^{-1} (x)$

3. $\displaystyle \int x\tan ^{-1} (x) ~dx = \color {blue} {\frac {1}{2} (x^2 \tan^{-1}(x) - x +\tan^{-1}(x))}$

- **Solution:** $u = \tan ^{-1} (x)$, $v = \frac {1}{2} x^2$, $du = \frac {1}{x^2 + 1} ~dx$, $dv = x ~dx$

- **Solution:** $\frac {1}{2} x^2 \tan ^{-1} (x) - \int \frac {1}{x^2 + 1} \cdot \frac {1}{2} x^2 ~dx = \frac {1}{2} x^2 \tan ^{-1} (x) - \frac {1}{2} \int (1 - \frac {1}{x^2 + 1}) ~dx$

  1. $\displaystyle \int_{0}^{1} x \tan ^{-1} (x) ~dx = \color {blue} {\frac {\pi}{4}-\frac {1}{2}}$

  - **Solution:** $\frac {1}{2} ((x^2 +1) \tan^{-1}(x) - x) |_{0}^{1} = (\tan ^{-1} (1) - \frac {1}{2}) - (0 - 0)​$

4. $\displaystyle \int x \sin(2x) ~dx = \color {blue} {\frac {1}{2} x \cos (2x) + \frac {1}{4} \sin (2x)}$

- **Solution:** $u = x$, $v = - \frac {1}{2} \cos (2x)$, $du = dx$, $dv = \sin (2x) ~dx$

- **Solution:** $- \frac {1}{2} x \cos (2x) - \int \sin (2x) ~dx$

- **Used 2018**
