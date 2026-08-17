---
schema: qual/card@1
id: P-RVMWA
kind: problem
title: Antiderivatives of powers of $\sin x$ and $\cos x$
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
1. $\displaystyle \int \sin ^2 (x) ~dx = \color {blue} {\frac {1}{2} (x - \sin (x) \cos (x))}$

- **Solution:** $\sin ^2 (x) = \frac {1 - \cos (2x)}{2}$

2. $\displaystyle \int \cos ^2 (x) ~dx = \color {blue} {\frac {1}{2} (x + \sin (x) \cos (x))}$

- **Solution:** $\cos ^2 (x) = \frac {1 + \cos (2x)}{2}$

3. $\displaystyle \int \sin ^3 (x) ~dx = \color {blue} {\frac {1}{3} \cos ^3 (x) - \cos (x)} = \color {blue} {\frac {1}{12} \cos (3x) - \frac {3}{4} \cos (x)}$

- **Solution:** $\sin ^3 (x) ~dx = (1 - \cos ^2 (x)) \sin (x) ~dx = (\cos ^2 (x) - 1) ~d\cos(x)$

- **Another Solution:** $\sin ^3 (x) = \frac {1}{4} (3 \sin (x) - \sin (3x))$

  1. $\displaystyle\int \frac {\sin ^3 {\sqrt {x}}}{2\sqrt {x}} ~dx  = \color {blue} {\frac {1}{3} \cos ^3 (\sqrt {x}) - \cos (\sqrt {x})} = \color {blue} {\frac {1}{12} \cos (3\sqrt {x}) - \frac {3}{4} \cos (\sqrt {x})}$

  - **Solution:** $\frac {\sin ^3 {\sqrt {x}}}{2\sqrt {x}} ~dx = \sin^3{\sqrt {x}} ~d\sqrt {x}​$

4. $\displaystyle \int \cos ^3 (x) ~dx = \color {blue} {\sin (x) - \frac {1}{3} \sin ^3 (x)} = \color {blue} {\frac {1}{12} \sin (3x) + \frac {3}{4} \sin (x)}$

- **Solution:** $\cos ^3 (x) ~dx = (1 - \sin ^2 (x)) \cos (x) ~dx = (1 - \sin ^2 (x)) ~d\sin(x)$

- **Another Solution:** $\cos ^3 (x) = \frac {1}{4} (3 \cos (x) + \cos (3x))$

5. $\displaystyle \int (\sin(x)+1)^3 ~dx = \color {blue} {\frac {5}{2}x+\frac {1}{3}\cos ^3(x)-4\cos (x)-\frac {3}{4}\sin (2x)}$

- **Solution:** $(\sin(x)+1)^3 = \sin ^3 (x) + 3 \sin ^2 (x) + 3 \sin (x) + 1$

6. $\displaystyle \int (\cos(x)+1)^3 ~dx = \color {blue} {\frac {5}{2}x-\frac {1}{3}\sin ^3(x)+4\sin (x)+\frac {3}{4}\sin (2x)}$

- **Solution:** $(\cos(x)+1)^3 = \cos ^3 (x) + 3 \cos ^2 (x) + 3 \cos (x) + 1$

7. $\displaystyle \int \sin ^4 (x) ~dx = \color {blue} {\frac {3}{8} x - \frac {3}{8} \sin (x) \cos (x) - \frac {1}{4} \sin ^3 (x) \cos (x)}​$

- **Solution:** $\frac {4 - 1}{4} \int \sin ^{4 - 2} (x) ~dx - \frac {1}{4} \cos (x) \sin ^{4 - 1} (x) = \frac {3}{4} (\frac {1}{2} (x - \sin (x) \cos (x))) - \frac {1}{4} \cos (x) \sin ^3 (x)$

8. $\displaystyle \int \cos ^4 (x) ~dx = \color {blue} {\frac {3}{8} x + \frac {3}{8} \sin (x) \cos (x) + \frac {1}{4} \sin (x)\cos ^3 (x)}​$

- **Solution:** $\frac {4 - 1}{4} \int \cos ^{4 - 2} (x) ~dx + \frac {1}{4} \sin (x) \cos ^{4 - 1} (x) = \frac {3}{4} (\frac {1}{2} (x + \sin (x) \cos (x))) + \frac {1}{4} \sin (x) \cos ^3 (x)$

9. $\displaystyle \int \cos^4(x) - \sin^4(x) dx = \color {blue} {\frac {1}{2}\sin{2x}}$

- **Solution:** $\cos ^4 (x) - \sin ^4 (x) = (\cos ^2 (x) - \sin ^2 (x)) (\cos ^2 (x) + \sin ^2 (x)) = \cos ^2 (x) - \sin ^2 (x) = \cos (2x)$

- **Used 2019**
:::
