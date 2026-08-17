---
schema: qual/card@1
id: P-Z45BG
kind: problem
title: "Prove that $z^4 + 2z^3 -2z + 10$ has exactly one root in each open"
classification:
  areas:
  - complex-analysis
  topics:
  - rouche
  - zeros
  - polynomials
  - argument-principle
relations: []
review: draft
solved: true
---

::: problem
Prove that $z^4 + 2z^3 -2z + 10$ has exactly one root in each open quadrant.
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** Prove that $z^4 + 2z^3 - 2z + 10$ has exactly one root in each open quadrant.

<1>1. Factor the polynomial as $f(z) + g(z)$ with $f(z) := z^4 + 10$ and $g(z) := 2z^3 - 2z$.
Proof: $z^4 + 2z^3 - 2z + 10 = (z^4 + 10) + (2z^3 - 2z)$.

<1>2. On the axes: $\abs{g(z)} < \abs{f(z)}$.
<2>1. On the real axis $z = x$: $\abs{2x^3 - 2x} \leq \abs{2x^3} + \abs{2x} = 2\abs x^3 + 2\abs x$, and $\abs{x^4 + 10} = x^4 + 10$.
Proof: Triangle inequality and $x^4 + 10 > 0$.
<2>2. $2\abs x^3 + 2\abs x < x^4 + 10$ for all real $x$.
Proof: Let $t = \abs x \geq 0$ and set $h(t) := t^4 + 10 - 2t^3 - 2t$.

- For $0 \leq t \leq 2$: $h(t) = (t^2 - t)^2 + (10 - t^2 - 2t) \geq 0 + (10 - 4 - 4) = 2 > 0$.

- For $t \geq 2$: $h(t) = t^3(t-2) - 2t + 10 \geq 8(t-2) - 2t + 10 = 6t - 6 > 0$.
  Hence $h(t) > 0$ for all $t \geq 0$, i.e. $2t^3 + 2t < t^4 + 10$.
  <2>3. On the imaginary axis $z = iy$: $\abs{g(iy)} = \abs{2(iy)^3 - 2iy} = \abs{-2iy^3 - 2iy} = 2\abs y(y^2 + 1)$ and $\abs{f(iy)} = \abs{y^4 + 10} = y^4 + 10$.
  Proof: $(iy)^4 = y^4$, $(iy)^3 = -iy^3$; $y^4 + 10 > 0$.
  <2>4. $2\abs y(y^2 + 1) < y^4 + 10$ for all real $y$.
  Proof: Same inequality as <2>2 with $t = \abs y$: need $2t^3 + 2t < t^4 + 10$, which is $h(t) > 0$ as shown in <2>2.

<1>3. On a large circle $\abs z = R$: $\abs{g(z)} < \abs{f(z)}$.
Proof: $\abs{g(z)} \leq 2R^3 + 2R$ and $\abs{f(z)} \geq R^4 - 10$; for $R$ large enough, $2R^3 + 2R < R^4 - 10$ (e.g. $R \geq 5$).

<1>4. By Rouch\'e's theorem, $z^4 + 2z^3 - 2z + 10$ and $z^4 + 10$ have the same number of zeros in each quadrant.
Proof: Apply Rouch\'e on the boundary of each quadrant (the two axes and the quarter-circle $\abs z = R$ in that quadrant): <1>2 and <1>3 give $\abs g < \abs f$ on the entire boundary, and $f + g$ is the given polynomial.

<1>5. $z^4 + 10$ has exactly one root in each open quadrant.
<2>1. Its roots are $10^{1/4} e^{i(\pi + 2\pi k)/4}$ for $k = 0, 1, 2, 3$.
Proof: Solve $z^4 = -10 = 10 e^{i\pi}$.
<2>2. These four roots have arguments $\pi/4, 3\pi/4, 5\pi/4, 7\pi/4$, one in each open quadrant.
Proof: Direct computation of arguments; none lies on an axis.

<1>6. Q.E.D. Proof: <1>4 and <1>5 give that $z^4 + 2z^3 - 2z + 10$ has exactly one root in each open quadrant.
:::
