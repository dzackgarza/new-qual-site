---
schema: qual/card@1
id: P-JH5RI
kind: problem
title: Homotopy classes of self-maps of $S^1\vee S^1$ with and without fixed points
classification:
  areas:
  - topology
  topics:
  - Fixed Points
  - Homotopy
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-05
  note: Checked the statement against problem 4 of the official UGA Spring 2008 topology exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-05
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-05
  note: >-
    Used the identity homotopy class for the forced-fixed-point example: every
    representative has Lefschetz number chi(S^1 vee S^1)=-1. For the
    fixed-point-free example, collapse one circle to the wedge point and follow
    by a half-turn of the other circle. Compare Hatcher, Algebraic Topology,
    Theorem 2C.3.
---

::: problem
Give an example of a homotopy class of maps of $S^1 \lor  S^1$ each member of which must have a fixed point, and also an example of a map of $S^1 \lor S^1$ which doesn't have a fixed point.
:::

::: {.solution}
Let
\[
X=S^1_a\vee S^1_b
\]
with wedge point $v$.

<1>1. Every self-map of $X$ homotopic to the identity has a fixed point.
::: {.proof}
The graph $X$ has one $0$-cell and two $1$-cells, so
\[
H_0(X;\QQ)\cong\QQ,
\qquad
H_1(X;\QQ)\cong\QQ^2,
\]
and all higher homology groups vanish.

Let
\[
g:X\longrightarrow X
\]
be homotopic to $\operatorname{id}_X$.
Homotopic maps induce the same maps on homology, hence
\[
g_*=\operatorname{id}
\]
on both nonzero homology groups.
Its Lefschetz number is therefore
\[
L(g)
=\operatorname{tr}(g_*|H_0)-\operatorname{tr}(g_*|H_1)
=1-2
=-1.
\]
In particular,
\[
L(g)\ne0.
\]
By the Lefschetz fixed-point theorem, $g$ has a fixed point.
Thus the homotopy class of the identity is an example in which every representative has a fixed point.
:::

<1>2. There is a fixed-point-free self-map of $X$.
::: {.proof}
Identify the first circle $S^1_a$ with the unit circle in $\CC$ so that its wedge point is
\[
v=1.
\]
Let
\[
r:X\longrightarrow S^1_a
\]
be the retraction that is the identity on $S^1_a$ and collapses the entire second circle $S^1_b$ to $v$.
Let
\[
R:S^1_a\longrightarrow S^1_a,
\qquad
R(z)=-z,
\]
be rotation by $\pi$, and define
\[
f=R\circ r:X\longrightarrow S^1_a\subseteq X.
\]

If $x\in S^1_a$, then
\[
f(x)=-x\ne x.
\]
If $x\in S^1_b$, then
\[
f(x)=R(v)=-1.
\]
The point $-1$ lies in $S^1_a\setminus\{v\}$, while
\[
S^1_a\cap S^1_b=\{v\}.
\]
Hence $f(x)\ne x$ for every $x\in S^1_b$, including $x=v$.

Thus $f$ has no fixed points.
:::

Therefore the identity homotopy class supplies the first requested example, while the explicit map
\[
\boxed{f=R\circ r}
\]
supplies the second.
:::
