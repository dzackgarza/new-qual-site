---
schema: qual/card@1
id: P-WESCA10-II6
kind: problem
title: 'Quadratic derivative-bound estimate and equality case'
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problems, problem 6 in the deterministic MinerU Flash extraction assets/attachments/analysis_2008-2013_extracted.md.
---

::: {.problem}
Suppose $f$ is analytic in the unit disk, $f(0)=f'(0)=0$, and
$$
\abs{f'(z)}\le1
$$
for every $\abs{z}<1$.
Prove
$$
\abs{f(z)}\le \frac{\abs{z}^2}{2}.
$$
Determine the functions for which equality can hold at some nonzero $z$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For every $z$ in the unit disk,
$$
\abs{f'(z)}\le \abs{z}.
$$


::: pf-proof

The function $h=f'$ is analytic in the unit disk, satisfies $h(0)=0$, and
$\abs{h(z)}\le1$. Schwarz's lemma therefore gives
$$
\abs{h(z)}\le\abs{z},
$$
which is the stated estimate.

:::

:::

::: {.pf-step #s1-2}

For every $z$ in the unit disk,
$$
\boxed{\abs{f(z)}\le\frac{\abs{z}^2}{2}}.
$$


::: pf-proof

Using $f(0)=0$, integrate along the radial segment from $0$ to $z$:
$$
f(z)=\int_0^1 f'(tz)z\,dt.
$$
By step [](#s1-1){.pf-ref},
$$
\abs{f'(tz)}\le t\abs{z}.
$$
Hence
$$
\abs{f(z)}
\le\int_0^1 \abs{f'(tz)}\,\abs{z}\,dt
\le\int_0^1 t\abs{z}^2\,dt
=\frac{\abs{z}^2}{2}.
$$

:::

:::

::: {.pf-step #s1-3}

If equality in step [](#s1-2){.pf-ref} holds at some $z_0\ne0$, then
$$
f'(z)=\lambda z
$$
for some constant $\lambda$ with $\abs{\lambda}=1$.


::: pf-proof

Assume
$$
\abs{f(z_0)}=\frac{\abs{z_0}^2}{2}.
$$
The two inequalities in the proof of step [](#s1-2){.pf-ref} must then both be equalities.
In particular,
$$
\int_0^1 \abs{f'(tz_0)}\,\abs{z_0}\,dt
=\int_0^1 t\abs{z_0}^2\,dt.
$$
By step [](#s1-1){.pf-ref}, the continuous function
$$
t\longmapsto t\abs{z_0}-\abs{f'(tz_0)}
$$
is nonnegative on $[0,1]$. Its integral is zero, so it vanishes identically.
Thus, for every $0<t<1$,
$$
\abs{f'(tz_0)}=\abs{tz_0}.
$$
Applying the equality case of Schwarz's lemma to $h=f'$ at any nonzero point
$tz_0$ gives
$$
f'(z)=\lambda z
$$
throughout the unit disk for some $\abs{\lambda}=1$.

:::

:::

::: {.pf-step #s1-4}

Equality can hold at a nonzero point exactly for the functions
$$
\boxed{f(z)=\frac{\lambda}{2}z^2,\qquad \abs{\lambda}=1}.
$$


::: pf-proof

By step [](#s1-3){.pf-ref}, equality at a nonzero point implies
$f'(z)=\lambda z$ with $\abs{\lambda}=1$. Since $f(0)=0$, integration gives
$$
f(z)=\frac{\lambda}{2}z^2.
$$
Conversely, each such function satisfies
$$
f(0)=f'(0)=0,
\qquad
\abs{f'(z)}=\abs{z}\le1
$$
on the unit disk, and
$$
\abs{f(z)}=\frac{\abs{z}^2}{2}
$$
for every $z$.

:::

:::

::: pf-qed

Step [](#s1-2){.pf-ref} proves the estimate, and step [](#s1-4){.pf-ref} determines precisely its equality
cases.

:::

:::

:::
