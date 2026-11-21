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
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    A retained solution read at this exercise. Read Yang Pi-Yeh, Hartshorne
    Solutions (9 June 2019), Solution 5.1.5, printed p. 100,
    rendered as a page image from
    tmp/sources/lfwin-hartshorne-solutions.pdf, whose PDF page is the printed
    page. Checked against the book: Hartshorne V.1.5, printed p. 367,
    which the card's earlier events record as read at a 110 dpi render of the
    text-layerless page; this pass did not reopen it, and the comparison is
    against the statement the card carries. Recomputed the two displays K^2 = d(d-4)^2 and K^2 = 8(g-1)(g'-1), the second
    through C^2 = C'^2 = 0 and C.C' = 1. Not
    checked: Yang's Solutions outside printed pp. 100-107; Hartshorne's printed
    p. 367 in this pass; and the printed book itself.
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    The remark now names Yang Pi-Yeh's Solution 5.1.5 at printed
    p. 100 beside Egbert's entry. No step, statement or hypothesis of
    the card changes.
---

::: {.problem}
(a) If $X$ is a surface of degree $d$ in $\PP^3$, then
$$
K^2=d(d-4)^2
.$$

(b) If $X$ is a product of two nonsingular curves $C, C^{\prime}$, of genus $g, g^{\prime}$ respectively, then
$$
K^2=8(g-1)\left(g^{\prime}-1\right)
.$$
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
K_X=(K_{\PP^3}+X)\restrict_X=(-4H+dH)\restrict_X=(d-4)H.
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

::: {.remark title="Published solution"}
The exercise is V.1.5 of Hartshorne, read in `tmp/sources/hartshorne-1977-algebraic-geometry.md`; the statement above is its text, both parts and the reference to (II, Ex. 8.3) included.

Andrew Egbert, *Solutions to Hartshorne's Algebraic Geometry* (October 3, 2013), text version `tmp/sources/hartshorne-solutions-egbert.md`, Exercise V.1.5: (a) $K_X=(d-4)H$ by adjunction since the canonical class of $\PP^3$ is $-4H$, and $H^2=d$ by the previous exercise, so $K_X^2=(d-4)^2d$; (b) $K_X=p_1^*K_C+p_2^*K_{C'}$ from II.8.3, so $K_X^2=(p_1^*K_C)^2+2p_1^*K_C\cdot p_2^*K_{C'}+(p_2^*K_{C'})^2$, "the middle term is $2(2g-2)(2g'-2)$ and the outer terms disappear". Steps [](#s3){.pf-ref} to [](#s5){.pf-ref} are this computation, with the vanishing of the outer terms proved in step [](#s4){.pf-ref} rather than asserted. Matches.

Yang Pi-Yeh, *Hartshorne Solutions* (9 June 2019), Solution 5.1.5, has both parts: (a) $K_X\sim(d-4)H$ with $H^2=d$ from the previous exercise, so $K_X^2=d(d-4)^2$; (b) $K_X=p_1^*K_C+p_2^*K_{C'}$ by (II, 8.3), and with $C^2=C'^2=0$ and $C\cdot C'=1$ the three terms are $0+2(2g-2)(2g'-2)+0=8(g-1)(g'-1)$.
:::
