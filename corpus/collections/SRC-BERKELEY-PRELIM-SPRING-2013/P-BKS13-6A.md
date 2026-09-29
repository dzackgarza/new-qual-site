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
$$
W^\perp=((W^\perp)^\perp)^\perp.
$$
Give an example such that $W\ne (W^\perp)^\perp$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

For every linear subspace $X\subseteq V$,
$$
X\subseteq(X^\perp)^\perp.
$$

::: pf-proof

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

:::

::: {.pf-step #s2}

If
$$
X\subseteq Y,
$$
then
$$
Y^\perp\subseteq X^\perp.
$$

::: pf-proof

Any vector orthogonal to every element of $Y$ is, in particular,
orthogonal to every element of the smaller set $X$.

:::

:::

::: {.pf-step #s3}

One has
$$
W^\perp
\subseteq
((W^\perp)^\perp)^\perp.
$$

::: pf-proof

Apply step [](#s1){.pf-ref} to the subspace
$$
X=W^\perp.
$$

:::

:::

::: {.pf-step #s4}

One has
$$
((W^\perp)^\perp)^\perp
\subseteq
W^\perp.
$$

::: pf-proof

Step [](#s1){.pf-ref} applied to $W$ gives
$$
W\subseteq(W^\perp)^\perp.
$$
Apply the inclusion-reversing property in step [](#s2){.pf-ref} to this inclusion.

:::

:::

::: {.pf-step #s5}

Therefore
$$
\boxed{
W^\perp
=
((W^\perp)^\perp)^\perp
}.
$$

::: pf-proof

Combine steps [](#s3){.pf-ref} and [](#s4){.pf-ref}.

:::

:::

::: {.pf-step #s6}

Let
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

::: pf-proof

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

:::

::: {.pf-step #s7}

In the example of step [](#s6){.pf-ref},
$$
W\neq(W^\perp)^\perp.
$$

::: pf-proof

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

:::

::: pf-qed

Step [](#s5){.pf-ref} proves the triple-orthogonal-complement identity, and step
[](#s7){.pf-ref} gives the requested example where the double orthogonal complement
is strictly larger than the original subspace.

:::

:::

:::
