---
schema: qual/card@1
id: E-HAT-1.1-6
kind: problem
title: Natural map from $\pi_1$ to unbased homotopy classes of maps $S^1 \to X$
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - Conjugacy Classes
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 1.1, Exercise 6; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Proved both directions of the free-homotopy/conjugacy correspondence and used basepoint change for surjectivity.
---

We can regard $\pi_1(X, x_0)$ as the set of basepoint-preserving homotopy classes of maps $(S^1, s_0) \to (X, x_0)$.
Let $[S^1, X]$ be the set of homotopy classes of maps $S^1 \to X$, with no conditions on basepoints.
Thus there is a natural map $\Phi: \pi_1(X, x_0) \longrightarrow [S^1, X]$ obtained by ignoring basepoints.
Show that $\Phi$ is onto if $X$ is path-connected, and that $\Phi([f]) = \Phi([g])$ iff $[f]$ and $[g]$ are conjugate in $\pi_1(X, x_0)$.
Hence $\Phi$ induces a one-to-one correspondence between $[S^1, X]$ and the set of conjugacy classes in $\pi_1(X)$, when $X$ is path-connected.

::: {.solution}
<1>1. Sliding the basepoint of a loop along a path changes its based class by conjugation and does not change its free homotopy class.
::: {.proof}
Let $p:I\to X$ be a path from $x$ to $y$, and let $f$ be a loop based at $y$.
The loop
\[
p\cdot f\cdot\bar p
\]
is based at $x$.
There is a free homotopy from this loop to $f$ obtained by moving the basepoint from $x$ to $y$ along $p$ while shortening the initial and terminal copies of $p$ by the same amount.

More explicitly, for $t\in I$ let
\[
p_t(s)=p\bigl(t+(1-t)s\bigr),
\qquad 0\le s\le1,
\]
the terminal segment of $p$ from $p(t)$ to $y$.
Then the loop
\[
L_t=p_t\cdot f\cdot\bar p_t
\]
is based at $p(t)$.
Using the standard three-piece parametrization of this concatenation gives a continuous map
\[
S^1\times I\to X.
\]
At $t=0$ it is $p\cdot f\cdot\bar p$, while at $t=1$ the two path pieces are constant and the loop is homotopic to $f$ by reparametrization.
Thus the two loops are freely homotopic.
:::

<1>2. If $X$ is path connected, then $\Phi$ is surjective.
::: {.proof}
Let $f:S^1\to X$ be arbitrary and put
\[
y=f(s_0).
\]
Choose a path $p$ from $x_0$ to $y$.
Regard $f$ as a loop based at $y$ and define
\[
g=p\cdot f\cdot\bar p,
\]
a loop based at $x_0$.
By <1>1, $g$ and $f$ are freely homotopic.
Hence
\[
\Phi([g])=[f]\in[S^1,X].
\]
Since $[f]$ was arbitrary, $\Phi$ is onto.
:::

<1>3. If $[f]$ and $[g]$ are conjugate in $\pi_1(X,x_0)$, then
\[
\Phi([f])=\Phi([g]).
\]
::: {.proof}
Suppose
\[
[g]=[h]\,[f]\,[h]^{-1}
\]
for a loop $h$ based at $x_0$.
Then $g$ is based-homotopic to
\[
h\cdot f\cdot\bar h.
\]
By <1>1, the latter loop is freely homotopic to $f$.
Therefore $g$ and $f$ define the same unbased homotopy class, so
\[
\Phi([g])=\Phi([f]).
\]
:::

<1>4. If
\[
\Phi([f])=\Phi([g]),
\]
then $[f]$ and $[g]$ are conjugate in $\pi_1(X,x_0)$.
::: {.proof}
The equality of their images means that there is a free homotopy
\[
H:S^1\times I\to X
\]
from $f$ to $g$.
Track the chosen point $s_0\in S^1$ through the homotopy:
\[
h(t)=H(s_0,t).
\]
Since both $f$ and $g$ are based at $x_0$, the path $h$ is a loop at $x_0$.

Cutting the homotopy cylinder along $\{s_0\}\times I$ produces a square whose boundary maps to
\[
f\cdot h\cdot\bar g\cdot\bar h.
\]
This boundary loop is null-homotopic because it bounds the mapped square.
Consequently
\[
[f]=[h]\,[g]\,[h]^{-1}.
\]
Thus $[f]$ and $[g]$ are conjugate.
:::

<1>5. The fibers of $\Phi$ are exactly the conjugacy classes in $\pi_1(X,x_0)$.
::: {.proof}
The forward and reverse implications are <1>3 and <1>4.
:::

<1>6. If $X$ is path connected, $\Phi$ induces a bijection
\[
\{\text{conjugacy classes in }\pi_1(X,x_0)\}
\longrightarrow
[S^1,X].
\]
::: {.proof}
By <1>5 the map is constant exactly on conjugacy classes, so it factors through the set of conjugacy classes and the induced map is injective.
By <1>2 it is surjective.
:::
:::
