---
schema: qual/card@1
id: P-TRIV-CA31
kind: problem
title: Analytic continuation of $\int_0^\infty t e^{-zt}\,dt$
classification:
  areas: [complex-analysis]
  topics:
  - Analytic Continuation
  - Laplace Transform
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Complex Analysis, Problem 31, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Find an analytic continuation $g(z)$ of the function $f(z) = \int_0^{\infty} te^{-zt}\, dt$. $f(z)$ is defined only for $z > 0$. What is the domain of $g(z)$?
:::

::: {.solution}

::: pf

::: pf-step

The integral
$$
F(z)
=
\int_0^\infty
t e^{-zt}\,dt
$$
converges for every
$$
\operatorname{Re}z>0.
$$


::: pf-proof

If
$$
\operatorname{Re}z=a>0,
$$
then
$$
\abs{t e^{-zt}}
=
t e^{-at}.
$$
The real integral
$$
\int_0^\infty t e^{-at}\,dt
$$
converges.

:::

:::

::: {.pf-step #s1-2}

For
$$
\operatorname{Re}z>0,
$$
one has
$$
F(z)=\frac1{z^2}.
$$


::: pf-proof

Integrate by parts:
$$
u=t,
\qquad
dv=e^{-zt}\,dt,
$$
so
$$
du=dt,
\qquad
v=-\frac1z e^{-zt}.
$$
Thus
$$
\begin{aligned}
F(z)
&=
\left[
-\frac{t}{z}e^{-zt}
\right]_0^\infty
+
\frac1z
\int_0^\infty e^{-zt}\,dt\\
&=
0
+
\frac1z
\left[
-\frac1z e^{-zt}
\right]_0^\infty\\
&=
\frac1{z^2}.
\end{aligned}
$$
The boundary terms vanish because $\operatorname{Re}z>0$.

:::

:::

::: {.pf-step #s1-3}

Define
$$
g(z)=\frac1{z^2}.
$$
Then $g$ is analytic on
$$
\CC\setminus\{0\}.
$$


::: pf-proof

The rational function $1/z^2$ is holomorphic at every nonzero complex number.

:::

:::

::: {.pf-step #s1-4}

The function $g$ analytically continues the original function $f$.


::: pf-proof

For positive real $z$, step [](#s1-2){.pf-ref} gives
$$
f(z)
=
\int_0^\infty t e^{-zt}\,dt
=
\frac1{z^2}
=
g(z).
$$
Thus $g$ agrees with $f$ on the original domain.

:::

:::

::: {.pf-step #s1-5}

The maximal domain of this analytic continuation is
$$
\boxed{\CC\setminus\{0\}}.
$$


::: pf-proof

Step [](#s1-3){.pf-ref} gives analyticity on $\CC\setminus\{0\}$. At $z=0$,
$$
g(z)=\frac1{z^2}
$$
has a pole of order $2$, so no holomorphic extension through $0$ exists.

:::

:::

::: pf-qed

Steps [](#s1-4){.pf-ref} through [](#s1-5){.pf-ref} give the analytic continuation and its maximal domain.

:::

:::

:::
