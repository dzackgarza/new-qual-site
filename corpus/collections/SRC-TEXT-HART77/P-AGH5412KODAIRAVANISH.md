---
schema: qual/card@1
id: P-AGH5412KODAIRAVANISH
kind: problem
title: Kodaira vanishing for the cubic surface
classification:
  areas:
  - algebraic-geometry
  topics:
  - Cubic Surfaces
  - Intersection Theory
  - Canonical Divisor
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-19
  note: >-
    Read Hartshorne V.4.12, the retained Egbert long-exact-sequence sketch,
    the cubic-surface blowup description, and V.4.8. The retained sketch
    writes X isomorphic to P^2, which is not literal: a smooth cubic surface
    is Bl_6 P^2. What is needed is H^1(X,O_X)=0, which follows because q is
    unchanged under point blowups. By (4.11), an ample D has positive
    intersection with every line and D^2>0; V.4.8 therefore supplies a
    nonsingular irreducible curve C in |D|. Then the exact sequence
    0 -> O_X(-D) -> O_X -> O_C -> 0 closes the argument because
    H^0(O_X)=H^0(O_C)=k and -D is not effective.
- event: solution-written
  by: chatgpt
  date: 2026-09-19
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-19
  note: >-
    Re-read the complete proof against the retained V.4.12 sketch, the cubic
    blowup cohomology, (4.11), and V.4.8. Checked that the smooth effective
    representative exists, that H^0(O_X(-D)) vanishes including the
    nowhere-vanishing-section edge case, and that the restriction k -> k in
    the divisor sequence is an isomorphism.
---

::: {.problem}
Use (4.11) to show that if $D$ is any ample divisor on the cubic surface $X$, then $H^1\left(X, \mathcal{O}_X(-D)\right)=0$.
This is Kodaira's vanishing theorem for the cubic surface (III, 7.15).
:::

::: {.solution}
Let
$$
X\subseteq\PP^3
$$
be the nonsingular cubic surface and let $D$ be ample.

<1>1. One has
$$
\boxed{
H^0(X,\OO_X)=k,
\qquad
H^1(X,\OO_X)=0.}
$$

::: {.proof}
The cubic surface is
$$
X\cong\operatorname{Bl}_{P_1,\ldots,P_6}\PP^2
$$
for six points in general position [[FE-SRFCUBIC]]. Point blowups of a
nonsingular surface preserve
$$
q=h^1(\OO)
$$
[[FE-SRFBLOW]]. Since
$$
H^1(\PP^2,\OO_{\PP^2})=0,
$$
it follows that
$$
H^1(X,\OO_X)=0.
$$
Also $X$ is integral and projective over the algebraically closed ground
field, so every global regular function is constant:
$$
H^0(X,\OO_X)=k.
$$
:::

<1>2. The divisor class $D$ contains a nonsingular irreducible curve
$$
\boxed{C\in|D|.}
$$

::: {.proof}
The ampleness criterion (4.11) gives
$$
D\cdot L>0
$$
for every one of the $27$ lines on $X$, and
$$
D^2>0.
$$
Thus $D$ satisfies alternative (c) of V.4.8. By
[[P-AGH548IRREDCLASSES]], every such class contains an irreducible
nonsingular curve. Choose one and call it $C$. Then
$$
C\sim D.
$$
:::

<1>3. The line bundle
$$
\OO_X(-D)
$$
has no nonzero global section:
$$
\boxed{H^0(X,\OO_X(-D))=0.}
$$

::: {.proof}
Suppose a nonzero section existed. If it vanished nowhere, it would
trivialize $\OO_X(-D)$, forcing $D\sim0$ and hence $D^2=0$, contrary to
step <1>2. Thus its zero divisor is a nonzero effective divisor
$$
E\sim-D.
$$
Because $D$ is ample, it has positive intersection with every nonzero
effective curve, hence
$$
D\cdot E>0.
$$
But numerical equivalence gives
$$
D\cdot E
=
-D^2
<0,
$$
since $D^2>0$ by step <1>2. This contradiction proves the vanishing.
:::

<1>4. The curve $C$ gives an exact sequence
$$
0
\longrightarrow
\OO_X(-D)
\longrightarrow
\OO_X
\longrightarrow
\OO_C
\longrightarrow
0.
$$

::: {.proof}
Since $C$ is an effective Cartier divisor linearly equivalent to $D$, its
ideal sheaf is
$$
\mathcal I_C\cong\OO_X(-C)\cong\OO_X(-D).
$$
The standard ideal-sheaf sequence of $C$ is therefore exactly the displayed
sequence.
:::

<1>5. One has
$$
\boxed{H^0(C,\OO_C)=k,}
$$
and the restriction map
$$
H^0(X,\OO_X)\longrightarrow H^0(C,\OO_C)
$$
is an isomorphism.

::: {.proof}
The curve $C$ is nonsingular and irreducible by step <1>2, hence integral
and projective. Thus every global regular function on $C$ is constant:
$$
H^0(C,\OO_C)=k.
$$
The restriction map sends the constant function $1$ on $X$ to the constant
function $1$ on $C$. Under the identifications
$$
H^0(X,\OO_X)=k=H^0(C,\OO_C),
$$
it is therefore the identity map on $k$.
:::

<1>6. Consequently
$$
\boxed{H^1(X,\OO_X(-D))=0.}
$$

::: {.proof}
The long exact cohomology sequence of step <1>4 begins
$$
0
\longrightarrow
H^0(X,\OO_X(-D))
\longrightarrow
H^0(X,\OO_X)
\longrightarrow
H^0(C,\OO_C)
\longrightarrow
H^1(X,\OO_X(-D))
\longrightarrow
H^1(X,\OO_X).
$$
By steps <1>1, <1>3, and <1>5 this becomes
$$
0
\longrightarrow
0
\longrightarrow
k
\xrightarrow{\sim}
k
\longrightarrow
H^1(X,\OO_X(-D))
\longrightarrow
0.
$$
Exactness forces
$$
H^1(X,\OO_X(-D))=0.
$$
:::

<1>7. Q.E.D.

::: {.proof}
Steps <1>1--<1>5 establish the cohomological inputs for the divisor sequence,
and step <1>6 gives the required vanishing.
:::
:::
