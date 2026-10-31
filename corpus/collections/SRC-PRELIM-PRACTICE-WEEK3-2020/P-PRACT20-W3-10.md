---
schema: qual/card@1
id: P-PRACT20-W3-10
kind: problem
title: Error of the quadratic Taylor approximation to $\sqrt{1.01}$
classification:
  areas:
  - prelim
  topics:
  - Taylor Series
relations: []
review: draft
---

::: {.problem}
The polynomial $p(x) = 1 + \frac{1}{2}(x - 1) - \frac{1}{8}(x - 1)^{2}$ is used to approximate $\sqrt{1.01}$. Which of the following best approximates the error $\sqrt{1.01} - p(1.01)$?

(A) $\frac{1}{16} \times 10^{-6}$

(B) $\frac{1}{48} \times 10^{-8}$

(C) $\frac{3}{8} \times 10^{-10}$

(D) $-\frac{3}{8} \times 10^{-10}$

(E) $-\frac{1}{16} \times 10^{-6}$
:::

::: {.solution}
By the binomial series ([[P-PRACT20-W3-04]]) with $\alpha = \frac12$,

$$
\sqrt{1+\varepsilon}\approx1+\frac12\cdot\frac{\varepsilon}{1!}+\frac12\left(-\frac12\right)\frac{\varepsilon^2}{2!}+\frac12\left(-\frac12\right)\left(-\frac32\right)\frac{\varepsilon^3}{3!}=1+\frac{\varepsilon}{2}-\frac{\varepsilon^2}{8}+\frac{\varepsilon^3}{16}
$$

when $\abs{\varepsilon}\ll1$, with an error of order $\varepsilon^4$. Thus

$$
\sqrt{1+\varepsilon}-p(1+\varepsilon)\approx\frac{\varepsilon^3}{16}.
$$

With $\varepsilon = 0.01$ the error is approximately $\frac{1}{16}\times 10^{-6}$, which is (A).
Alternatively, $p$ is the second-order Taylor polynomial, so the error has order $\varepsilon^3 = 10^{-6}$, which excludes (B), (C), (D); the sign of the error is the sign of the third derivative of $f(x) = \sqrt{x}$ at $x = 1$, which is positive.
:::
