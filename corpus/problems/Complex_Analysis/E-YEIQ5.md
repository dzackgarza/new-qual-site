---
schema: qual/card@1
id: E-YEIQ5
kind: problem
title: An analytic function sending a simple closed curve into $\RR$ is constant
classification:
  areas:
  - complex-analysis
  topics:
  - Open Mapping Theorem
  - Maximum Modulus Principle
relations: []
review: draft
---

::: problem
Let $f$ be an analytic function on a region $\Omega$.
Show that $f$ is a constant if there is a simple closed curve $\gamma$ in $\Omega$ such that its image $f(\gamma)$ is contained in the real axis.
:::

::: solution
The statement is false for a general region $\Omega$.
Take
\[
\Omega=\{z:1/2<|z|<2\},
\qquad
f(z)=z+{1\over z},
\]
and let $\gamma$ be the unit circle. Then $f$ is nonconstant and holomorphic on
$\Omega$, while for $z=e^{it}$,
\[
f(z)=e^{it}+e^{-it}=2\cos t\in\RR.
\]
Thus $f(\gamma)\subset\RR$ although $f$ is not constant.

The natural corrected statement is true if the bounded component $U$ of
$\CC\setminus\gamma$ is contained in $\Omega$. Indeed, then
$v=\Im f$ is harmonic on $U$, continuous on $\overline U$, and satisfies
$v=0$ on $\partial U=\gamma$. The maximum and minimum principles for harmonic
functions give $v\equiv0$ on $U$. Hence $f(U)\subset\RR$.

If $f$ were nonconstant on $U$, the open mapping theorem would make $f(U)$
open in $\CC$, which is impossible for a subset of $\RR$. Thus $f$ is constant
on the nonempty open set $U$, and the identity theorem then makes $f$ constant
on the connected region $\Omega$.
:::
