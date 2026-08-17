---
schema: qual/card@1
id: P-SQVNA
kind: problem
title: Antiderivatives of $x^n\ln x$
classification:
  areas:
  - prelim
  topics:
  - integrals
  - integration-by-parts
relations: []
review: draft
solved: false
---

::: problem
- **Solution:** $\ln (x^2 - 1) = \ln (x + 1)(x - 1) = \ln (x + 1) + \ln (x - 1)​$

2. $\displaystyle \int x^n \ln(x) ~dx =  \color{blue} { \frac {x^{n + 1}}{n + 1} (\ln (x) - \frac {1}{n + 1})}​$

- **Solution:** $u = \ln (x)​$, $v = \frac {x^{n + 1}}{n + 1}​$, $du = \frac {1}{x} ~dx​$, $dv = x^n ~dx​$

  1. $\displaystyle \int_{1}^{\infty} \frac {\ln(x)}{x^2} ~dx = \color{blue} {1}​$

  - **Solution:** $\frac {x^{(-2) + 1}}{(-2) + 1} (\ln (x) - \frac {1}{(-2) + 1}) = - \frac {\ln (x) + 1}{x}​$

  - **Solution:** $\lim_{x \to \infty} \frac {\ln (x) + 1}{x} = \lim_{x \to \infty} \frac {\frac {1}{x} + 0}{1} = 0​$ (L'Hospital Rule)

  2. $\displaystyle \int \sqrt {x} \ln(x) ~dx = \color{blue} {\frac {2}{3} x^{\frac {3}{2}} \ln (x) - \frac {4}{9} x^{\frac {3}{2}}}​$

  - **Solution:** $\frac {x^{\frac {1}{2} + 1}}{\frac {1}{2} + 1} (\ln (x) - \frac {1}{\frac {1}{2} + 1}) = \frac {2}{3} x^{\frac {3}{2}} (\ln (x) - \frac {2}{3}) ​$

  3. $\displaystyle \int x^2\ln(x) ~dx = \color{blue} {\frac {1}{3} x^3 \ln (x) - \frac {1}{9} x^3}​$

  - **Solution:** $\frac {x^{2 + 1}}{2 + 1} (\ln (x) - \frac {1}{2 + 1}) = \frac {x^3}{3} (\ln (x) - \frac {1}{3})​$

  4. $\displaystyle \int x \ln(x) ~dx = \color{blue} {\frac {1}{2} x^2 \ln (x) - \frac {1}{4} x^2}$

  - **Solution:** $\frac {x^{1 + 1}}{1 + 1} (\ln (x) - \frac {1}{1 + 1}) = \frac {x^2}{2} (\ln (x) - \frac {1}{2})$

  - **Used 2018**

  5. $\displaystyle \int \frac {\ln(x)}{x} ~dx = \color {blue} {\frac {1}{2} \ln ^2 (x)}$

  - **Solution:** $u = \ln (x)$, $du = \frac {1}{x} ~dx$

  - THIS IS DIFFERENT FROM THE REST (u-sub)
:::
