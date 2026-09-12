---
schema: qual/card@1
id: E-HAT-1.1-16
kind: problem
title: No retractions in six specific cases
classification:
  areas:
  - topology
  topics:
  - Retractions
  - Fundamental Group
  - Fixed Point Theorems
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: >-
    Checked against Hatcher, Algebraic Topology, Section 1.1, Exercise 16 and the
    accompanying figure. Hatcher's correction note clarifies that in (c), A is
    the dark circle in the interior of the solid torus; the figure shows it as a meridian.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: In each case used the necessary split-injectivity of the inclusion on pi_1 and exhibited the obstruction explicitly.
---

Show that there are no retractions $r: X \to A$ in the following cases:

(a) $X = \mathbb{R}^3$ with $A$ any subspace homeomorphic to $S^1$.

(b) $X = S^1 \times D^2$ with $A$ its boundary torus $S^1 \times S^1$.

(c) $X = S^1 \times D^2$ and $A$ the circle shown in the figure.

(d) $X = D^2 \lor D^2$ with $A$ its boundary $S^1 \lor S^1$.

(e) $X$ a disk with two points on its boundary identified and $A$ its boundary $S^1 \lor S^1$.

(f) $X$ the Möbius band and $A$ its boundary circle.

::: {.solution}
We use the same elementary obstruction in all six cases.

<1>1. If $r:X\to A$ is a retraction and $i:A\hookrightarrow X$ is the inclusion, then
\[
r_*\circ i_*=\operatorname{id}_{\pi_1(A)}.
\]
In particular, $i_*$ must be injective.
::: {.proof}
A retraction satisfies
\[
r\circ i=\operatorname{id}_A.
\]
Functoriality of the fundamental group gives
\[
(r\circ i)_*=r_*\circ i_*=(\operatorname{id}_A)_*.
\]
Any homomorphism possessing a left inverse is injective.
:::

<1>2. In case (a), no retraction $\mathbb R^3\to A\cong S^1$ exists.
::: {.proof}
The space $\mathbb R^3$ is contractible, so
\[
\pi_1(\mathbb R^3)=0,
\]
whereas
\[
\pi_1(A)\cong\mathbb Z.
\]
Thus the inclusion-induced map
\[
i_*:\mathbb Z\to0
\]
is not injective, contradicting <1>1 if a retraction existed.
:::

<1>3. In case (b), no retraction from the solid torus $S^1\times D^2$ to its boundary torus exists.
::: {.proof}
Let $m\subset S^1\times S^1$ be a meridian circle
\[
m=\{x_0\}\times S^1.
\]
It represents a nontrivial element of
\[
\pi_1(S^1\times S^1)\cong\mathbb Z^2,
\]
but in the solid torus it bounds the disk
\[
\{x_0\}\times D^2.
\]
Hence $i_*([m])=1$, so $i_*$ is not injective.
By <1>1 there can be no retraction.
:::

<1>4. In case (c), the indicated interior circle $A$ is a meridian and hence no retraction $S^1\times D^2\to A$ exists.
::: {.proof}
The dark circle in the source figure is an interior meridian of the solid torus.
It bounds a meridional disk lying in $S^1\times D^2$.
Thus its generator
\[
[A]\in\pi_1(A)\cong\mathbb Z
\]
maps to the identity in $\pi_1(S^1\times D^2)$.
The inclusion-induced map is therefore not injective, so <1>1 rules out a retraction.
:::

<1>5. In case (d), no retraction
\[
D^2\vee D^2\to S^1\vee S^1
\]
exists.
::: {.proof}
The wedge $D^2\vee D^2$ is contractible: contract each disk to the common wedge point.
Hence
\[
\pi_1(D^2\vee D^2)=0.
\]
On the other hand,
\[
\pi_1(S^1\vee S^1)\cong F(a,b)
\]
is the free group on two generators and is nontrivial.
Thus the inclusion-induced map is not injective, contradicting <1>1.
:::

<1>6. In case (e), no retraction from the quotient disk to its boundary $S^1\vee S^1$ exists.
::: {.proof}
Let the two identified boundary points divide the original boundary circle into arcs whose images become the two loops $a$ and $b$ of
\[
A=S^1\vee S^1.
\]
Then
\[
\pi_1(A)\cong F(a,b),
\]
and the element $ab$ is nontrivial in this free group.

But the loop $ab$ is exactly the image of the original boundary circle of $D^2$.
It bounds the image of the disk itself in the quotient space $X$, so
\[
i_*([ab])=1\in\pi_1(X).
\]
Hence $i_*$ has nontrivial kernel, and <1>1 excludes a retraction.
:::

<1>7. In case (f), no retraction from the Möbius band $M$ to its boundary circle exists.
::: {.proof}
The Möbius band deformation retracts onto its core circle, so
\[
\pi_1(M)\cong\mathbb Z.
\]
Its boundary circle traverses the core twice.
Thus, after choosing generators, the inclusion induces
\[
i_*:\mathbb Z\to\mathbb Z,
\qquad
i_*(n)=2n.
\]
If a retraction existed, <1>1 would give a homomorphism
\[
r_*:\mathbb Z\to\mathbb Z
\]
with
\[
r_*\circ i_*=\operatorname{id}_{\mathbb Z}.
\]
Every homomorphism $\mathbb Z\to\mathbb Z$ is multiplication by some integer $k$, so this would require
\[
2k=1,
\]
which is impossible.
:::

<1>8. Therefore none of the six indicated inclusions admits a retraction.
::: {.proof}
Cases (a)--(f) are established in <1>2--<1>7.
:::
:::
