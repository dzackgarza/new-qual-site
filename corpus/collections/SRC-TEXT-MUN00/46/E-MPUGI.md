---
schema: qual/card@1
id: E-MPUGI
kind: problem
title: Products with a locally compact Hausdorff factor preserve quotient maps
classification:
  areas:
  - topology
  topics:
  - Quotient Topology
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-11
  note: >-
    No complete published solution of Munkres §46 Exercise 9 (printed p. 289) was located; the sets searched are listed in the
    COMPLAINTS.md entry for §43--§50 of SRC-TEXT-MUN00. Checked against Theorem 46.11 (the adjunction between
    maps X x Z -> Y and maps Z -> C(X,Y) for the compact-open topology), which the exercise says the proof
    uses, and against the defining property of a quotient map (§22: a map out of the quotient is continuous iff
    its composite with the quotient map is). Part (a): i_X x p is constant on the fibres of q, so it factors
    through the quotient Y as a bijection f with f o q = i_X x p, and f is continuous by the quotient property.
    Part (b): with G(b)(x) = g(x,b) and Q(a)(x) = q(x,a), the identity q = g o (i_X x p) gives Q = G o p
    pointwise. Part (c): q is continuous, so its adjoint Q is continuous by Theorem 46.11; p is quotient and
    Q = G o p, so G is continuous; applying Theorem 46.11 to G gives that g is continuous; hence f is a
    continuous bijection with continuous inverse, so i_X x p = f o q is a quotient map. Nothing needed
    correction.
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Searched outside the checkout (issue #144). The AoPS blog post by cinnamon_e, "Topology by
    Munkres Chapter 7 | Day 17" (2025-09-10,
    https://artofproblemsolving.com/community/c3401823h3646977, text at
    tmp/sources/aops-shooting-star-munkres-ch7-day17.md), answers this exercise at its item 9 of
    §46, and the extraction dropped every inline formula, so the answer cannot be transcribed; the
    site answers an automated request with a Cloudflare human check, which is not worked around.
    Murayama's selection stops at Chapter 4, dbFin has no chapter-7 page, and the Math StackExchange,
    GitHub and web searches of this pass found no other treatment of the product of a quotient map
    with the identity on a locally compact space; they are recorded in the COMPLAINTS.md entry for
    §43--§50. The card keeps its own proof.
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    The card stood in queue D: its solution was prose with no numbered step. It is now a `pf` with
    eight steps covering (a), (b) and (c), each carrying a `pf-proof`. Cited by numbered statement
    only: Munkres, Topology, §46 Exercise 9, Theorem 46.11 (adjunction of a map on a product with a
    locally compact Hausdorff factor), §22 (quotient maps) and Theorem 22.2 (the quotient criterion
    for an induced map). The proof remains the card's own: the self-study notes for Chapter 7 that
    reach this exercise state it without answering it, and no retained set answers it, as the
    earlier event records. Checked: that $i_X\times p$ is surjective, that the induced $f$ is a
    bijection carrying saturated sets, that $f^{-1}(U)=q((i_X\times p)^{-1}(U))$ with the inner set
    saturated and open, that $q=g\circ(i_X\times p)$ gives $Q=G\circ p$ pointwise in the first
    variable, and that the adjunction applies twice, to $q$ and to $G$.
---

::: {.exercise}

Here is an application of Theorem 46.11 to quotient maps.
(Compare [[E-S57IX]].)

Theorem.
If $p: A \to B$ is a quotient map and $X$ is locally compact Hausdorff, then $i_X \times p: X \times A \to X \times B$ is a quotient map.

(a) Let $Y$ be the quotient space induced by $i_X \times p$; let $q: X \times A \to Y$ be the quotient map.
Show there is a bijective continuous map $f: Y \to X \times B$ such that $f \circ q = i_X \times p$.

(b) Let $g = f^{-1}$.
Let $G: B \to \mathcal{C}(X, Y)$ and $Q: A \to \mathcal{C}(X, Y)$ be the maps induced by $g$ and $q$, respectively.
Show that $Q = G \circ p$.

(c) Show that $Q$ is continuous; conclude that $G$ is continuous, so that $g$ is continuous.
:::

::: {.solution}

No retained published solution of Munkres, *Topology*, §46 Exercise 9 was located: the sets searched are listed in the `COMPLAINTS.md` entry for §43--§50 of `SRC-TEXT-MUN00`, and the self-study notes that do reach Chapter 7 state this exercise without answering it. The proof is the card's own, checked against the numbered statements of §22 and §46 it cites, and the adjunction it uses is Theorem 46.11.

::: pf

::: {.pf-step #quotient-adjunction}
Theorem 46.11 (used in (b) and (c)): for $X$ locally compact Hausdorff and any space $Z$, a map $F:X\times Z\to W$ is continuous if and only if its adjoint $\widehat F:Z\to\mathcal C(X,W)$, $\widehat F(z)(x)=F(x,z)$, is continuous, the function space carrying the compact-open topology.

::: pf-proof
This is the statement of Munkres, Theorem 46.11.
:::

:::

::: {.pf-step #bijection}
(a) $i_X\times p$ is surjective and $q$ identifies exactly its fibres, so there is a bijection $f:Y\to X\times B$ with $f\circ q=i_X\times p$.

::: pf-proof
$i_X$ is surjective and $p$ is surjective, so $i_X\times p$ is surjective. The quotient space $Y$ induced by a surjection $i_X\times p$ has its quotient map $q$ constant on each fibre and separating distinct fibres, so the induced map on the set of fibres is a bijection; $f$ is that bijection read on $X\times B$, and $f\circ q=i_X\times p$ holds by construction.
:::

:::

::: {.pf-step #continuity-of-f}
(a) $f$ is continuous.

::: pf-proof
Let $U\subseteq X\times B$ be open. Then $f^{-1}(U)=q((i_X\times p)^{-1}(U))$, and $(i_X\times p)^{-1}(U)$ is open and saturated for $q$ because $i_X\times p$ is constant on the fibres of $q$. A quotient map carries a saturated open set to an open set, so $f^{-1}(U)$ is open.
:::

:::

::: {.pf-step #Q-equals-Gp}
(b) $Q=G\circ p$.

::: pf-proof
$f\circ q=i_X\times p$ and $g=f^{-1}$ give $q=g\circ(i_X\times p)$. Evaluating at $(x,a)$, $Q(a)(x)=q(x,a)=g(x,p(a))=G(p(a))(x)$ for every $x$, that is, $Q(a)=G(p(a))$ for every $a\in A$.
:::

:::

::: {.pf-step #Q-continuous}
(c) $Q:A\to\mathcal C(X,Y)$ is continuous.

::: pf-proof
$q:X\times A\to Y$ is continuous and $X$ is locally compact Hausdorff, so its adjoint $Q$ is continuous by step [](#quotient-adjunction){.pf-ref}. Note that $\mathcal C(X,Y)$ here carries the compact-open topology of the function space on $X$, in which $Q$ is the adjoint of $q$.
:::

:::

::: {.pf-step #G-continuous}
(c) $G:B\to\mathcal C(X,Y)$ is continuous.

::: pf-proof
$Q=G\circ p$ by step [](#Q-equals-Gp){.pf-ref} with $Q$ continuous by step [](#Q-continuous){.pf-ref}, and $p$ is a quotient map. By the quotient criterion (Munkres, Theorem 22.2, applied with the target $\mathcal C(X,Y)$), $G$ is continuous.
:::

:::

::: {.pf-step #g-continuous}
(c) $g=f^{-1}$ is continuous, so $f$ is a homeomorphism.

::: pf-proof
$G$ is continuous and $X$ is locally compact Hausdorff, so by step [](#quotient-adjunction){.pf-ref} the adjoint $g:X\times B\to Y$ of $G$ is continuous. Steps [](#bijection){.pf-ref} and [](#continuity-of-f){.pf-ref} make $f$ a continuous bijection with continuous inverse, that is, a homeomorphism.
:::

:::

::: {.pf-step #quotient}
$i_X\times p:X\times A\to X\times B$ is a quotient map.

::: pf-proof
$i_X\times p$ equals $f\circ q$, the composite of the quotient map $q$ with a homeomorphism, and a homeomorphism composed with a quotient map on either side is a quotient map. So $i_X\times p$ is a quotient map, which is the theorem of the exercise.
:::

:::

:::

:::
