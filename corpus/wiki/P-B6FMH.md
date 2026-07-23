---
schema: qual/card@1
id: P-B6FMH
kind: problem
title: "13. $\\displaystyle \\int_{0}^{1} \\frac {1}{\\sqrt {x(1-x)}} ~dx = 2 \\sin\u2026"
classification:
  areas: []
  topics: []
relations: []
review: draft
---
13. $\displaystyle \int_{0}^{1} \frac {1}{\sqrt {x(1-x)}} ~dx = 2 \sin ^{-1} (\sqrt {x}) |_{0}^{1} = \color {blue} {\pi}$

- **Solution:** $u = \sqrt {x}$, $du = \frac {1}{2 \sqrt {x}} ~dx$

- **Solution:** $\frac {1}{\sqrt {x(1-x)}} ~dx = \frac {2}{\sqrt {1 - u^2}} ~du$

  1. $\displaystyle \int_{e^{\frac {1}{2}}}^{e^{\frac {3}{4}}} \frac {1}{x\sqrt {\ln(x)(1-\ln(x))}} ~dx = \color {blue} {\frac {\pi}{6}}$

  - **Solution:** $u = \ln (x)$, $du = \frac {1}{x} ~dx$
  - **Solution:** $\int_{e^{\frac {1}{2}}}^{e^{\frac {3}{4}}} \frac {1}{x\sqrt {\ln(x)(1-\ln(x))}} ~dx = \int_{\frac {1}{2}}^{\frac {3}{4}} \frac {1}{\sqrt {x(1-x)}} ~dx = 2 \sin ^{-1} (\sqrt {x}) |_{\frac {1}{2}}^{\frac {3}{4}} = 2(\frac {\pi}{3} - \frac {\pi}{4})$
  - **Used 2019**, *Unsolved*

14. $\displaystyle \int \frac {x}{1-x^2 + \sqrt {1- x^2}} ~dx = \color {blue} {- \ln (\sqrt {1-x^2}+1)}$

- **Solution:** $u^2 = 1 - x^2$, $u ~du = - x ~dx$
- **Solution:** $\frac {x}{1-x^2 + \sqrt {1- x^2}} ~dx = \frac {1}{1-x^2 + \sqrt {1- x^2}} \cdot x ~dx = \frac {1}{u^2 + u} \cdot (-u) ~du = - \frac {1}{u + 1} ~du$

15. $\displaystyle \int_{1}^{\infty} \frac {1}{x(x^2+1)} ~dx = \frac {1}{2} \ln (\frac {1}{x^2} + 1) |_{1}^{\infty} = \color {blue} {\frac {1}{2} \ln (2)}$

- **Solution:** $u = \frac {1}{x^2} + 1​$, $du = -2 \frac {1}{x^3} ~dx​$
- **Solution:** $\frac {1}{x(x^2+1)} ~dx = \frac {1}{(\frac {1}{x^2} + 1)} \cdot \frac {1}{x^3} ~dx = - \frac {1}{2u} du$
- **Used 2019**


