---
schema: qual/card@1
id: E-QF7KI
kind: exercise
title: Residues at infinity
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Contour Integration
  - Singularities
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

:::{.exercise}
Use residues at infinity to evaluate
\[
\int_{|z|=1} \frac{1}{(z-2)(1+2 z)^{4}(1-3 z)^{7}} \dz
.\]

:::

::: {.solution}
**Goal.** Evaluate $\oint_{|z|=1} \frac{1}{(z-2)(1+2z)^4(1-3z)^7}\,dz$ using residues at infinity.

<1>1. The integrand $f(z) = \frac{1}{(z-2)(1+2z)^4(1-3z)^7}$ has poles inside $|z| = 1$ at $z = -1/2$ (order $4$) and $z = 1/3$ (order $7$), and a simple pole at $z = 2$ outside.
Proof: $1 + 2z = 0$ at $z = -1/2$ and $1 - 3z = 0$ at $z = 1/3$, both inside the unit circle; $z = 2$ is outside.

<1>2. The sum of all residues over the extended plane is $0$.
Proof: for a rational function, $\sum_{\text{finite poles}} \operatorname{Res}(f, z_j) + \operatorname{Res}(f, \infty) = 0$.

<1>3. Compute $\operatorname{Res}(f, \infty)$.
<2>1. $\operatorname{Res}(f, \infty) = -\operatorname{Res}\qty(\frac{1}{z^2} f(1/z), 0)$.
Proof: definition of the residue at infinity.
<2>2. $\frac{1}{z^2} f(1/z) = \frac{1}{z^2} \cdot \frac{1}{(1/z - 2)(1 + 2/z)^4(1 - 3/z)^7} = \frac{z^{10}}{(1-2z)(z+2)^4(z-3)^7}$.
Proof: substitute $z \mapsto 1/z$ and simplify (multiply numerator and denominator by $z^{12}$).
<2>3. This is analytic at $z = 0$ (numerator has $z^{10}$), so $\operatorname{Res}\qty(\frac{1}{z^2}f(1/z), 0) = 0$.
Proof: no $1/z$ term in the Laurent expansion at $0$.
<2>4. Hence $\operatorname{Res}(f, \infty) = 0$.
Proof: <1>3.1 and <1>3.3.

<1>4. Compute $\operatorname{Res}(f, 2)$.
<2>1. $z = 2$ is a simple pole, so $\operatorname{Res}(f, 2) = \lim_{z \to 2} (z-2) f(z) = \frac{1}{(1+2\cdot 2)^4 (1 - 3\cdot 2)^7} = \frac{1}{5^4 \cdot (-5)^7} = -\frac{1}{5^{11}}$.
Proof: the residue at a simple pole is the limit of $(z-2)f(z)$.

<1>5. Sum of residues inside $|z| = 1$.
<2>1. $\sum_{\text{inside}} \operatorname{Res} = -(\operatorname{Res}(f, 2) + \operatorname{Res}(f, \infty))$.
Proof: by <1>2, the total is zero, and the poles outside are $z = 2$ and $\infty$.
<2>2. $= -\qty(-\frac{1}{5^{11}} + 0) = \frac{1}{5^{11}}$.
Proof: substitute <1>3.4 and <1>4.1.

<1>6. $\oint_{|z|=1} f(z)\,dz = 2\pi i \cdot \frac{1}{5^{11}}$.
Proof: the residue theorem.

<1>7. Q.E.D.
Proof: the integral equals $\frac{2\pi i}{5^{11}}$.
:::

