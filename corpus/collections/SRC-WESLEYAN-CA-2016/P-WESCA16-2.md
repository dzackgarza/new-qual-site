---
schema: qual/card@1
id: P-WESCA16-2
kind: problem
title: 'Holomorphic functions are infinitely differentiable'
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 2 in the deterministic MinerU Flash extraction assets/attachments/analysis_2014-2016_extracted.md.
---

::: {.problem}
Prove that every holomorphic function is infinitely complex-differentiable.
:::

::: {.solution}
<1>1. Let $f$ be holomorphic on an open set $D$, and let $z_0\in D$.
There is a positively oriented circle $\Gamma$ centered at $z_0$ whose closed
disk lies in $D$.

::: {.proof}
Because $D$ is open, there is $R>0$ such that
\[
\overline{B(z_0,R)}\subseteq D.
\]
Take
\[
\Gamma=\{\zeta:|\zeta-z_0|=R\}
\]
with positive orientation.
:::

<1>2. For every $z$ with $|z-z_0|<R$,
\[
f(z)=\frac1{2\pi i}\int_\Gamma\frac{f(\zeta)}{\zeta-z}\,d\zeta.
\]

::: {.proof}
This is Cauchy's integral formula, since $f$ is holomorphic on a neighborhood
of the closed disk bounded by $\Gamma$.
:::

<1>3. For every integer $n\ge0$ and every $z$ with $|z-z_0|<R$,
\[
\boxed{
f^{(n)}(z)
=\frac{n!}{2\pi i}
\int_\Gamma\frac{f(\zeta)}{(\zeta-z)^{n+1}}\,d\zeta }.
\]

::: {.proof}
For $z$ in any smaller closed disk
\[
|z-z_0|\le r<R,
\]
the distance from $z$ to $\Gamma$ is at least $R-r>0$. Hence, as a function
of $z$, the integrand
\[
\frac{f(\zeta)}{\zeta-z}
\]
and all of its $z$-derivatives are continuous on the compact product of
$\Gamma$ with that smaller disk, and are uniformly bounded there.
Consequently differentiation under the contour integral is valid.

Differentiating step <1>2 once gives
\[
f'(z)=\frac1{2\pi i}
\int_\Gamma\frac{f(\zeta)}{(\zeta-z)^2}\,d\zeta.
\]
Inductively,
\[
\frac{d^n}{dz^n}\frac1{\zeta-z}
=\frac{n!}{(\zeta-z)^{n+1}},
\]
which yields the displayed formula for every $n$.
:::

<1>4. The function $f$ is infinitely complex-differentiable on $D$.

::: {.proof}
The point $z_0\in D$ was arbitrary. Step <1>3 constructs derivatives of
every order on a neighborhood of every point of $D$. Hence all derivatives
$f^{(n)}$ exist throughout $D$ for every $n\ge0$.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is the required conclusion.
:::
:::
