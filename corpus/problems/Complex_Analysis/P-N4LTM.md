---
schema: qual/card@1
id: P-N4LTM
kind: problem
title: 'Local mapping theorem: a zero of multiplicity $m$ splits into $m$ distinct
  nearby preimages'
classification:
  areas:
  - complex-analysis
  topics:
  - Open Mapping Theorem
  - Zeros
  - Argument Principle
relations: []
review: draft
---

::: {.problem}
Let $f$ be analytic in a domain $D$ and fix $z_0 \in D$ with $w_0 \definedas f(z_0)$.
Suppose $z_0$ is a zero of $f(z) - w_0$ with finite multiplicity $m$.
Show that there exists $\delta >0$ and $\eps > 0$ such that for each $w$ such that $0 < \abs{w-w_0} < \eps$, the equation $f(z) - w = 0$ has exactly $m$ *distinct* solutions inside the disc $\abs{z-z_0} < \delta$.
:::

::: {.solution}
Write
\[
f(z)-w_0=(z-z_0)^m g(z),
\qquad g(z_0)\ne0.
\]
Then
\[
f'(z)=(z-z_0)^{m-1}h(z)
\]
for a holomorphic function $h$ with $h(z_0)=m g(z_0)\ne0$. Choose
$\delta>0$ so small that the closed disk
$\overline{D(z_0,\delta)}$ lies in $D$, $z_0$ is the only zero of
$f-w_0$ there, and $h$ has no zero there. Thus $z_0$ is the only critical
point of $f$ in this closed disk.

Set
\[
M=\min_{|z-z_0|=\delta}|f(z)-w_0|>0
\]
and choose $0<\varepsilon<M$. If $0<|w-w_0|<\varepsilon$, then on the boundary
circle
\[
|(w-w_0)|<|f(z)-w_0|.
\]
Rouché's theorem therefore implies that
\[
f(z)-w=(f(z)-w_0)-(w-w_0)
\]
has exactly $m$ zeros in $D(z_0,\delta)$, counted with multiplicity.

None of these zeros is $z_0$, because $w\ne w_0$. At every zero $z$ in the
disk we also have $f'(z)\ne0$, since $z_0$ is the only critical point there.
Hence all $m$ zeros are simple. Therefore they are $m$ distinct solutions.
:::
