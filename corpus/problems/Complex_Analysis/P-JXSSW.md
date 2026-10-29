---
schema: qual/card@1
id: P-JXSSW
kind: problem
title: Laurent series and singularities at $0$ of $\sin^2(z)/z$, $z\exp(1/z^2)$, and
  $1/(z(4-z))$
classification:
  areas:
  - complex-analysis
  topics:
  - Laurent Series
  - Singularities
  - Essential Singularities
  - Removable Singularities
  - Poles
relations: []
review: draft
---

::: {.problem}
For the following functions, find the Laurent series about $0$ and classify their singularities there:
$$
{\sin^2(z) \over z}, \qquad
z \exp{1\over z^2}, \qquad
{1 \over z(4-z)}
.$$
:::

::: {.solution}
::: pf

::: pf-step
$$
\frac{\sin^2z}{z} =\sum_{n=1}^\infty (-1)^{n+1}\frac{2^{2n-1}}{(2n)!}z^{2n-1} =z-\frac{z^3}{3}+\frac{2z^5}{45}-\cdots,
$$
and $0$ is a $\boxed{\text{removable singularity}}$, with extended value $0$.

::: pf-proof
Expand $\sin^2z=(1-\cos 2z)/2 = \sum_{n \geq 1}(-1)^{n+1}\frac{(2z)^{2n}}{2\,(2n)!}$ and divide by $z$.
The series has no negative powers.
:::

:::

::: pf-step
For $z \neq 0$,
$$
z e^{1/z^2} =\sum_{n=0}^\infty\frac{z^{1-2n}}{n!} =z+\frac1z+\frac{1}{2!\,z^3}+\frac{1}{3!\,z^5}+\cdots,
$$
and $0$ is an $\boxed{\text{essential singularity}}$.

::: pf-proof
Substitute $1/z^2$ into the exponential series and multiply by $z$.
The principal part has infinitely many nonzero terms.
:::

:::

::: pf-step
For $0<\abs{z}<4$,
$$
\frac1{z(4-z)} =\sum_{n=0}^\infty\frac{z^{n-1}}{4^{n+1}} =\frac1{4z}+\frac1{16}+\frac z{64}+\cdots,
$$
and $0$ is a $\boxed{\text{simple pole}}$ with residue $1/4$.

::: pf-proof
Write $\frac1{z(4-z)} =\frac1{4z}\cdot\frac1{1-z/4}$ and expand the geometric series, valid for $\abs{z} < 4$.
The only negative power is $z^{-1}$.
:::

:::

:::
:::
