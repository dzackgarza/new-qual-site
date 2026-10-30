---
schema: qual/card@1
id: P-UCLARA15S-08
kind: problem
title: Entire functions of exponential type bounded on the axes are constant
classification:
  areas:
  - complex-analysis
  topics:
  - Entire Functions
  - Liouville's Theorem
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Transcribed from the official UCLA Analysis Qualifying Exam, Spring 2015, and reconciled with the retained UCLA Analysis Qualifying Exam Solutions compendium.
---

::: {.problem}
Let $f:\CC\to\CC$ be holomorphic and suppose
$$
\sup_{x\in\RR}\bigl(\abs{f(x)}^2+\abs{f(ix)}^2\bigr)<\infty
$$
and
$$
\abs{f(z)}\le e^{\abs{z}}\qquad\text{for all }z\in\CC.
$$
Deduce that $f(z)$ is constant.
:::

::: {.solution}

Choose $M\ge0$ such that
$$
\abs{f(x)}\le M,
\qquad
\abs{f(ix)}\le M
\qquad
(x\in\RR).
$$

::: pf

::: {.pf-step #s1}

If $M=0$, then $f\equiv0$.


::: pf-proof

If $M=0$, then $f(x)=0$ for every real $x$. The real axis has accumulation points in $\CC$, so the identity theorem gives $f\equiv0$.

:::

:::

::: {.pf-step #s2}

Assume $M>0$. In the first quadrant
$$
Q
\coloneqq
\{z:0<\arg z<\pi/2\},
$$
one has
$$
\abs{f(z)}\le M.
$$


::: pf-proof

::: pf-step

Fix $\varepsilon>0$ and define
$$
g_\varepsilon(z)
\coloneqq
f(z)
\exp\!\left(
-\varepsilon
(e^{-i\pi/4}z)^{3/2}
\right),
\qquad z\in Q,
$$
where the principal branch of the $3/2$-power is used.


::: pf-proof

For $z\in Q$, the number
$$
e^{-i\pi/4}z
$$
has argument in $(-\pi/4,\pi/4)$, so it avoids the negative real axis. The principal $3/2$-power is therefore holomorphic on this rotated quadrant, and hence $g_\varepsilon$ is holomorphic on $Q$ and continuous on its closure.

:::

:::

::: {.pf-step #s2-2}

There is a constant
$$
\delta
\coloneqq
\cos(3\pi/8)>0
$$
such that, for $z=Re^{i\theta}\in\overline Q$,
$$
\abs{g_\varepsilon(z)}
\le
\exp\!\left(
R-\varepsilon\delta R^{3/2}
\right).
$$


::: pf-proof

The growth hypothesis gives
$$
\abs{f(z)}\le e^R.
$$
Also,
$$
(e^{-i\pi/4}z)^{3/2}
=
R^{3/2}
e^{i(3\theta/2-3\pi/8)}.
$$
For $0\le\theta\le\pi/2$,
$$
-\frac{3\pi}{8}
\le
\frac{3\theta}{2}-\frac{3\pi}{8}
\le
\frac{3\pi}{8},
$$
so
$$
\operatorname{Re}
(e^{-i\pi/4}z)^{3/2}
\ge
\delta R^{3/2}.
$$
Taking absolute values in the definition of $g_\varepsilon$ gives the estimate.

:::

:::

::: {.pf-step #s2-3}

There exists $R_\varepsilon>0$ such that
$$
\abs{g_\varepsilon(z)}\le M
$$
whenever $z\in\overline Q$ and $\abs{z}\ge R_\varepsilon$.


::: pf-proof

By step [](#s2-2){.pf-ref},
$$
\abs{g_\varepsilon(z)}
\le
\exp\!\left(
R-\varepsilon\delta R^{3/2}
\right).
$$
The exponent tends to $-\infty$ as $R\to\infty$, so the right-hand side tends to $0$. Since $M>0$, it is at most $M$ for all sufficiently large $R$.

:::

:::

::: {.pf-step #s2-4}

On the two boundary rays of $Q$,
$$
\abs{g_\varepsilon(z)}\le M.
$$


::: pf-proof

On either boundary ray, $\abs{f(z)}\le M$ by the definition of $M$. Moreover,
$$
\operatorname{Re}
(e^{-i\pi/4}z)^{3/2}
\ge0,
$$
so the exponential multiplier in $g_\varepsilon$ has modulus at most $1$.

:::

:::

::: {.pf-step #s2-5}

One has
$$
\abs{g_\varepsilon(z)}\le M
\qquad
(z\in Q).
$$


::: pf-proof

Choose $R\ge R_\varepsilon$ and apply the maximum-modulus principle to the bounded quarter-disk
$$
Q\cap\{\abs{z}<R\}.
$$
Step [](#s2-4){.pf-ref} bounds $\abs{g_\varepsilon}$ by $M$ on the two radial sides, and step [](#s2-3){.pf-ref} bounds it by $M$ on the circular side. Hence the same bound holds throughout that quarter-disk. Letting $R\to\infty$ proves the claim on all of $Q$.

:::

:::

::: {.pf-step #s2-6}

For every $z\in Q$,
$$
\abs{f(z)}\le M.
$$


::: pf-proof

Step [](#s2-5){.pf-ref} gives
$$
\abs{f(z)}
\le
M
\exp\!\left(
\varepsilon
\operatorname{Re}
(e^{-i\pi/4}z)^{3/2}
\right).
$$
For fixed $z$, the real number in the exponent is finite. Letting $\varepsilon\downarrow0$ yields
$$
\abs{f(z)}\le M.
$$

:::

:::

::: pf-qed

Step [](#s2-6){.pf-ref} proves the claim of step [](#s2){.pf-ref}.

:::

:::

:::

::: {.pf-step #s3}

The bound
$$
\abs{f(z)}\le M
$$
holds for every $z\in\CC$.


::: pf-proof

The argument of step [](#s2){.pf-ref} depends only on a quadrant being bounded by two rays on which $\abs{f}\le M$. Rotate the construction by $\pi/2$, $\pi$, and $3\pi/2$ to treat the other three quadrants. The real and imaginary axes themselves already satisfy the bound by definition of $M$.

:::

:::

::: {.pf-step #s4}

The function $f$ is constant.


::: pf-proof

By step [](#s3){.pf-ref}, $f$ is a bounded entire function. Liouville's theorem therefore implies that $f$ is constant.

:::

:::

::: pf-qed

Step [](#s1){.pf-ref} handles the case $M=0$, and step [](#s4){.pf-ref} handles the case $M>0$.

:::

:::

:::
