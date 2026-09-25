---
schema: qual/card@1
id: P-BKS13-6A
kind: problem
title: Triple orthogonal complements in inner product spaces
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-25
  note: Compared the authored statement with page 3 of the retained Spring 2013 solution PDF and independently reviewed both orthogonal-complement inclusions and the l^2 example.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked the triple-perp equality and the c_00 subset of l^2(N) counterexample to W=W^{perp perp}.
---

::: {.problem}
Show that if $V$ is a real vector space with a positive definite symmetric bilinear form $\langle\cdot,\cdot\rangle$ and $W\subset V$ is a linear subspace, then
\[
W^\perp=((W^\perp)^\perp)^\perp.
\]
Give an example such that $W\ne (W^\perp)^\perp$.
:::

::: {.solution}
<1>1. For every linear subspace $X\subseteq V$,
$$
X\subseteq(X^\perp)^\perp.
$$

::: {.proof}
Let
$$
x\in X.
$$
For every
$$
y\in X^\perp,
$$
one has
$$
\langle x,y\rangle=0
$$
by the definition of $X^\perp$. Thus $x$ is orthogonal to every vector in
$X^\perp$, so
$$
x\in(X^\perp)^\perp.
$$
:::

<1>2. If
$$
X\subseteq Y,
$$
then
$$
Y^\perp\subseteq X^\perp.
$$

::: {.proof}
Any vector orthogonal to every element of $Y$ is, in particular,
orthogonal to every element of the smaller set $X$.
:::

<1>3. One has
$$
W^\perp
\subseteq
((W^\perp)^\perp)^\perp.
$$

::: {.proof}
Apply step <1>1 to the subspace
$$
X=W^\perp.
$$
:::

<1>4. One has
$$
((W^\perp)^\perp)^\perp
\subseteq
W^\perp.
$$

::: {.proof}
Step <1>1 applied to $W$ gives
$$
W\subseteq(W^\perp)^\perp.
$$
Apply the inclusion-reversing property in step <1>2 to this inclusion.
:::

<1>5. Therefore
$$
\boxed{
W^\perp
=
((W^\perp)^\perp)^\perp
}.
$$

::: {.proof}
Combine steps <1>3 and <1>4.
:::

<1>6. Let
$$
V=\ell^2(\NN)
$$
with its usual real inner product, and let
$$
W=c_{00}
$$
be the subspace of finitely supported real sequences. Then
$$
W^\perp=\{0\}.
$$

::: {.proof}
For each $j\geq1$, the standard basis vector $e_j$ lies in $W$. If
$$
v=(v_1,v_2,\ldots)\in W^\perp,
$$
then
$$
0
=
\langle v,e_j\rangle
=
v_j
$$
for every $j$. Hence $v=0$.
:::

<1>7. In the example of step <1>6,
$$
W\neq(W^\perp)^\perp.
$$

::: {.proof}
Since
$$
W^\perp=\{0\},
$$
one has
$$
(W^\perp)^\perp
=
\{0\}^\perp
=
V.
$$
But $W$ is a proper subspace of $V$. For example,
$$
\left(1,\frac12,\frac13,\ldots\right)
\in
\ell^2(\NN)
$$
because
$$
\sum_{n=1}^{\infty}\frac1{n^2}<\infty,
$$
while this sequence is not finitely supported and hence does not belong
to $W$.
:::

<1>8. Q.E.D.

::: {.proof}
Step <1>5 proves the triple-orthogonal-complement identity, and step
<1>7 gives the requested example where the double orthogonal complement
is strictly larger than the original subspace.
:::
:::
