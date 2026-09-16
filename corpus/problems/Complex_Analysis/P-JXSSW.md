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
\[
{\sin^2(z) \over z} \\
z \exp{1\over z^2} \\
{1 \over z(4-z)}
.\]
:::

::: {.solution}
For the first function, use $\sin^2z=(1-\cos 2z)/2$:
\[
\frac{\sin^2z}{z}
=\sum_{n=1}^\infty
(-1)^{n+1}\frac{2^{2n-1}}{(2n)!}z^{2n-1}
=z-\frac{z^3}{3}+\frac{2z^5}{45}-\cdots.
\]
There are no negative powers, so the singularity at $0$ is removable; the
holomorphic extension has value $0$ there.

For the second function,
\[
z e^{1/z^2}
=z\sum_{n=0}^\infty\frac{1}{n!z^{2n}}
=\sum_{n=0}^\infty\frac{z^{1-2n}}{n!}
=z+\frac1z+\frac{1}{2!z^3}+\frac{1}{3!z^5}+\cdots.
\]
Its principal part has infinitely many nonzero terms, so $0$ is an essential
singularity.

Finally, for $0<|z|<4$,
\[
\frac1{z(4-z)}
=\frac1{4z}\frac1{1-z/4}
=\sum_{n=0}^\infty\frac{z^{n-1}}{4^{n+1}}
=\frac1{4z}+\frac1{16}+\frac z{64}+\frac{z^2}{256}+\cdots.
\]
Thus $0$ is a simple pole, with residue $1/4$.
:::
