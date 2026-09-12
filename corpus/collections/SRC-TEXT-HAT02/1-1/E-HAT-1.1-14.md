---
schema: qual/card@1
id: E-HAT-1.1-14
kind: problem
title: Isomorphism $\pi_1(X \times Y) \approx \pi_1(X) \times \pi_1(Y)$ given by projections
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - Product Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 1.1, Exercise 14; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Constructed the inverse on loop classes by pairing coordinate loops and checked both compositions explicitly.
---

Show that the isomorphism $\pi_1(X \times Y) \approx \pi_1(X) \times \pi_1(Y)$ in Proposition 1.12 is given by $[f] \mapsto (p_{1*}([f]), p_{2*}([f]))$ where $p_1$ and $p_2$ are the projections of $X \times Y$ onto its two factors.

::: {.solution}
Fix the basepoint $(x_0,y_0)\in X\times Y$ and define
\[
\Psi:\pi_1(X\times Y,(x_0,y_0))
\longrightarrow
\pi_1(X,x_0)\times\pi_1(Y,y_0)
\]
by
\[
\Psi([f])=([p_1\circ f],[p_2\circ f]).
\]

<1>1. The map $\Psi$ is a homomorphism.
::: {.proof}
For based loops $f,g$ in $X\times Y$,
\[
p_i\circ(f\cdot g)=(p_i\circ f)\cdot(p_i\circ g)
\]
up to the standard concatenation parametrization.
Hence
\[
\Psi([f][g])
=
\bigl([p_1f][p_1g],[p_2f][p_2g]\bigr)
=
\Psi([f])\Psi([g]).
\]
The definition depends only on the based homotopy class because composing a based homotopy with either projection gives a based homotopy in the corresponding factor.
:::

<1>2. Define
\[
\Theta:\pi_1(X,x_0)\times\pi_1(Y,y_0)
\longrightarrow
\pi_1(X\times Y,(x_0,y_0))
\]
by
\[
\Theta([a],[b])=[t\mapsto(a(t),b(t))].
\]
Then $\Theta$ is well defined.
::: {.proof}
If $a\simeq a'$ and $b\simeq b'$ relative to endpoints, let
\[
A:I\times I\to X,
\qquad
B:I\times I\to Y
\]
be the two based homotopies.
Then
\[
H(s,t)=(A(s,t),B(s,t))
\]
is a based homotopy in $X\times Y$ from $(a,b)$ to $(a',b')$.
Thus the class defining $\Theta$ depends only on $[a]$ and $[b]$.
:::

<1>3. One has
\[
\Psi\circ\Theta=\operatorname{id}.
\]
::: {.proof}
For $([a],[b])$,
\[
\Psi\Theta([a],[b])
=
\Psi([t\mapsto(a(t),b(t))])
=
([a],[b]),
\]
since the two projections recover $a$ and $b$ exactly.
:::

<1>4. One also has
\[
\Theta\circ\Psi=\operatorname{id}.
\]
::: {.proof}
If $f:I\to X\times Y$ is a based loop, then for every $t$
\[
f(t)=\bigl(p_1(f(t)),p_2(f(t))\bigr).
\]
Therefore the loop used to define
\[
\Theta\Psi([f])
\]
is literally $f$, so
\[
\Theta\Psi([f])=[f].
\]
:::

<1>5. Thus $\Psi$ is the product isomorphism, and it is exactly
\[
[f]\longmapsto\bigl(p_{1*}([f]),p_{2*}([f])\bigr).
\]
::: {.proof}
By <1>3--<1>4, $\Theta$ is a two-sided inverse of $\Psi$.
The displayed formula is the definition of the two induced projection maps.
:::
:::
