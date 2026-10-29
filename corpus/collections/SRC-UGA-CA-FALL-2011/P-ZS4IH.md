---
schema: qual/card@1
id: P-ZS4IH
kind: problem
title: A bound on the difference quotient of a holomorphic function on a half-radius
  disc
classification:
  areas:
  - complex-analysis
  topics:
  - Cauchy Estimates
  - Schwarz Lemma
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---
::: {.problem}
Let $\bar{B}(a, r)$ denote the closed disk of radius $r > 0$ centered at $a \in \CC$. Let $f$ be holomorphic on an open neighborhood containing $\bar{B}(a, r)$, and define
$$
M = \sup_{z \in \bar{B}(a, r)} |f(z)|.
$$
Prove that for all $z \in \bar{B}(a, r/2)$ with $z \ne a$:
$$
\frac{|f(z) - f(a)|}{|z - a|} \le \frac{2M}{r}.
$$
:::

::: {.solution}
Fix $z\in\bar B(a,r/2)$ with $z\ne a$, and let
$$
C=\{\zeta:|\zeta-a|=r\}
$$
with positive orientation.

::: pf

::: {.pf-step #s1}

One has
$$
\frac{f(z)-f(a)}{z-a}
=\frac{1}{2\pi i}
\int_C
\frac{f(\zeta)}{(\zeta-z)(\zeta-a)}\,d\zeta.
$$

::: pf-proof

Cauchy's formula gives
$$
f(z)=\frac{1}{2\pi i}\int_C\frac{f(\zeta)}{\zeta-z}\,d\zeta,
\qquad
f(a)=\frac{1}{2\pi i}\int_C\frac{f(\zeta)}{\zeta-a}\,d\zeta,
$$
because both $z$ and $a$ lie inside $C$. Subtracting,
$$
f(z)-f(a)
=\frac{1}{2\pi i}
\int_C
f(\zeta)
\left(
\frac1{\zeta-z}-\frac1{\zeta-a}
\right)d\zeta.
$$
Since
$$
\frac1{\zeta-z}-\frac1{\zeta-a}
=\frac{z-a}{(\zeta-z)(\zeta-a)},
$$
division by $z-a\ne0$ gives the formula.

:::

:::

::: {.pf-step #s2}

For every $\zeta\in C$,
$$
|\zeta-a|=r,
\qquad
|\zeta-z|\ge\frac r2.
$$

::: pf-proof

The first identity is the definition of $C$. For the second, the reverse
triangle inequality gives
$$
|\zeta-z|
\ge |\zeta-a|-|z-a|
\ge r-\frac r2
=\frac r2.
$$

:::

:::

::: {.pf-step #s3}

The desired estimate holds:
$$
\boxed{
\frac{|f(z)-f(a)|}{|z-a|}
\le\frac{2M}{r}}.
$$

::: pf-proof

By step [](#s1){.pf-ref} and the ML estimate,
$$
\begin{aligned}
\frac{|f(z)-f(a)|}{|z-a|}
&\le
\frac1{2\pi}
\int_C
\frac{|f(\zeta)|}{|\zeta-z|\,|\zeta-a|}
\,|d\zeta|\\
&\le
\frac1{2\pi}
(2\pi r)
\frac{M}{(r/2)r}\\
&=\frac{2M}{r},
\end{aligned}
$$
where step [](#s2){.pf-ref} supplies the denominator bounds and the circumference of
$C$ is $2\pi r$.

:::

:::

::: pf-qed

Step [](#s3){.pf-ref} is exactly the claimed inequality.

:::

:::

:::
