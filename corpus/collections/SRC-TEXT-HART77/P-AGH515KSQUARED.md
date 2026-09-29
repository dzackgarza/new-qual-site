---
schema: qual/card@1
id: P-AGH515KSQUARED
kind: problem
title: Self-intersection of the canonical divisor for hypersurfaces and products of curves
classification:
  areas:
  - algebraic-geometry
  topics:
  - Surfaces
  - Canonical Divisor
  - Intersection Theory
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Hartshorne V.1.5, the retained Egbert companion calculation, the
    hypersurface adjunction computation, and Hartshorne II.8.3 as represented
    by the product canonical-sheaf card. The proof below checks the product
    intersection numbers directly from fibres before expanding the canonical
    divisor square.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-18
---

::: {.problem}
a. If $X$ is a surface of degree $d$ in $\PP^3$, then
\[
K^2=d(d-4)^2
.\]

b. If $X$ is a product of two nonsingular curves $C, C^{\prime}$, of genus $g, g^{\prime}$ respectively, then
\[
K^2=8(g-1)\left(g^{\prime}-1\right)
.\]
Cf. (II, Ex. 8.3).
:::

::: {.solution}
In part (a), let $H$ denote the hyperplane class on $X$. In part (b), let
$p_1:C\times C'\to C$ and $p_2:C\times C'\to C'$ be the projections.

::: pf

::: {.pf-step #s1}

If $X\subseteq\PP^3$ is a nonsingular surface of degree $d$, then
$$
K_X=(d-4)H
\qquad\text{and}\qquad
H^2=d.
$$

::: pf-proof

Hypersurface adjunction gives
$$
K_X=(K_{\PP^3}+X)|_X=(-4H+dH)|_X=(d-4)H.
$$
The number $H^2$ is the intersection of $X$ with two general hyperplanes in
$\PP^3$, hence equals the degree of $X$, namely $d$.

:::

:::

::: {.pf-step #s2}

For the surface in part (a),
$$
\boxed{K_X^2=d(d-4)^2}.
$$

::: pf-proof

By bilinearity of the intersection pairing and step [](#s1){.pf-ref},
$$
K_X^2
=(d-4)^2H^2
=(d-4)^2d.
$$

:::

:::

::: {.pf-step #s3}

On $C\times C'$, one has
$$
K_{C\times C'}=p_1^*K_C+p_2^*K_{C'}.
$$

::: pf-proof

Hartshorne II.8.3, proved on [[P-AGH283PRODDIFF]], gives
$$
\omega_{C\times C'}
\cong
p_1^*\omega_C\tensor p_2^*\omega_{C'}.
$$
Passing to divisor classes gives the displayed equality of canonical classes.

:::

:::

::: {.pf-step #s4}

For divisors $D,E$ on $C$ and $D',E'$ on $C'$,
$$
(p_1^*D)\cdot(p_1^*E)=0,
\qquad
(p_2^*D')\cdot(p_2^*E')=0,
$$
and
$$
(p_1^*D)\cdot(p_2^*D')=(\deg D)(\deg D').
$$

::: pf-proof

Write divisors as integral linear combinations of closed points. For a point
$P\in C$, the divisor $p_1^*P=\{P\}\times C'$ is a fibre of $p_1$. Distinct
fibres of $p_1$ are disjoint, and the normal bundle of each fibre is the
constant one-dimensional vector space $T_PC$ tensored with its structure
sheaf, hence has degree zero. Therefore every pair of pullbacks from $C$ has
intersection number zero. The same argument applies to pullbacks from $C'$.

For points $P\in C$ and $Q\in C'$, the two fibres
$$
\{P\}\times C'
\qquad\text{and}\qquad
C\times\{Q\}
$$
meet transversely in the single point $(P,Q)$, so their intersection number is
one. Bilinearity of the intersection pairing then gives
$$
(p_1^*D)\cdot(p_2^*D')=(\deg D)(\deg D').
$$

:::

:::

::: {.pf-step #s5}

For $X=C\times C'$,
$$
\boxed{K_X^2=8(g-1)(g'-1)}.
$$

::: pf-proof

Set
$$
A=p_1^*K_C,
\qquad
B=p_2^*K_{C'}.
$$
By step [](#s3){.pf-ref}, $K_X=A+B$. Step [](#s4){.pf-ref} gives $A^2=B^2=0$ and
$$
A\cdot B
=(\deg K_C)(\deg K_{C'})
=(2g-2)(2g'-2).
$$
Therefore
$$
\begin{aligned}
K_X^2
&=(A+B)^2\\
&=2A\cdot B\\
&=2(2g-2)(2g'-2)\\
&=8(g-1)(g'-1).
\end{aligned}
$$

:::

:::

::: pf-qed

Step [](#s2){.pf-ref} proves part (a), and steps [](#s3){.pf-ref}, [](#s4){.pf-ref} and [](#s5){.pf-ref} prove part (b).

:::

:::

:::
