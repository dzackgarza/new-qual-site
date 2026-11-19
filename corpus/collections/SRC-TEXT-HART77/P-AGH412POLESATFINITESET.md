---
schema: qual/card@1
id: P-AGH412POLESATFINITESET
kind: problem
title: A rational function with poles at a prescribed finite set of points
classification:
  areas:
  - algebraic-geometry
  topics:
  - Riemann-Roch
  - Linear Systems
  - Divisors
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against Hartshorne, Algebraic Geometry (1977), Chapter IV, section 1,
    exercise 1.2, printed page 297 (PDF page 312 of
    tmp/sources/hartshorne-1977-algebraic-geometry.md, the checked-in
    extraction). The printed exercise reads: "Again let X be a curve, and let
    P_1, ..., P_r be points. Then there is a rational function f in K(X) having
    poles (of some order) at each of the P_i, and regular elsewhere." The card
    states exactly this. The proof was read and checked: with D the sum of the
    points and n-1 > 2g-2, Riemann-Roch gives l(nD) - l(nD - P_i) = 1 for each
    i, so L(nD - P_i) is a proper subspace of L(nD); a vector space over an
    infinite field is not a union of finitely many proper subspaces, so some f
    lies outside all of them, and then v_{P_i}(f) = -n at each P_i with no pole
    elsewhere.
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    A retained solution read at this exercise. Read Yang Pi-Yeh, Hartshorne
    Solutions (9 June 2019), Solution 4.1.2, printed p. 84,
    rendered as a page image from
    tmp/sources/lfwin-hartshorne-solutions.pdf, whose PDF page is the printed
    page. Checked against the book: Hartshorne IV.1.2, whose printed page
    the card's earlier events record; this pass did not reopen it, and the
    comparison is against the statement the card carries. Recomputed
    the degree 2r - (2r-1) = 1, the Riemann-Roch value, and the divisor of
    f with its multiplicities at the P_i. Not checked: Yang's Solutions outside printed pp. 84-85; the
    book's own page in this pass; and the printed book itself.
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    The remark now names Yang Pi-Yeh's Solution 4.1.2 at printed
    p. 84 beside the entry already there. No step, statement or
    hypothesis of the card changes.
---


::: {.problem}
Again let $X$ be a curve, and let $P_1, \ldots, P_r \in X$ be points. Then there is a rational function $f \in K(X)$ having poles (of some order) at each of the $P_i$, and regular elsewhere.
:::

::: {.solution}
Let $g$ be the genus of $X$, let $D=P_1+\cdots+P_r$, and let $L(E)=\{f\in K(X) \st f=0 \text{ or } (f)+E\ge0\}$, so that $\ell(E)=\dim_k L(E)$.

::: pf

::: {.pf-step #s1}

Fix $n$ with $n-1>2g-2$. For each $i$, there is $f_i\in L(nD)$ with a pole of order exactly $n$ at $P_i$.

::: pf-proof

The divisors $nD$ and $nD-P_i$ both have degree greater than $2g-2$, so by Riemann-Roch and the vanishing of $\ell(K-E)$ for $\deg E>2g-2$,
$$
\ell(nD)-\ell(nD-P_i)=(rn+1-g)-(rn-1+1-g)=1.
$$
An element $f_i\in L(nD)\setminus L(nD-P_i)$ has $v_{P_i}(f_i)\ge -n$ but not $v_{P_i}(f_i)\ge -n+1$, so $v_{P_i}(f_i)=-n$.

:::

:::

::: {.pf-step #s2}

Some $f\in L(nD)$ has a pole of order exactly $n$ at every $P_i$.

::: pf-proof

For each $i$, the set $H_i=L(nD-P_i)$ is a subspace of $L(nD)$, and it is proper by step [](#s1){.pf-ref}. A vector space over the infinite field $k$ is not a union of finitely many proper subspaces, so there is $f\in L(nD)$ outside $H_1\cup\cdots\cup H_r$. As in step [](#s1){.pf-ref}, $v_{P_i}(f)=-n$ for every $i$.

:::

:::

::: pf-qed

The function $f$ of step [](#s2){.pf-ref} satisfies $(f)+nD\ge0$, so it is regular at every point outside $\{P_1,\ldots,P_r\}$, and it has a pole at each $P_i$.

:::

:::

:::

::: {.remark title="Published solution"}
The exercise stands on printed p. 297 of Hartshorne, read in `tmp/sources/hartshorne-1977-algebraic-geometry.pdf`, where printed p. $N$ is PDF p. $N+15$; the statement above is that page's text, which names the points $P_1,\ldots,P_n$ where the card writes $P_1,\ldots,P_r$.

Jinhyun Park, *Solutions to Hartshorne's Algebraic Geometry*, Chapter IV §1, Exercise 2, PDF p. 30, text version `tmp/sources/hartshorne-solutions-park.md`, and Lomont, *Solutions to Hartshorne's Algebraic Geometry*, Chapter IV §1, Exercise 1.2, PDF p. 4, text version `tmp/sources/hartshorne-solutions-lomont.md`, both handle the cancellation obstruction explicitly: for $Q\notin F$ and $n>\max\{2g-2,g\}$ one has $D\in\linearsystem{n(P_1+\cdots+P_r-(r-1)Q)}$ of degree $n$, and in the sole bad case $D=nP_i$ one replaces $f$ by $f^\alpha g$ with $g$ from Exercise 1 having a pole only at $P_i$ and $\alpha>\max\{n_j,1\}$.

Yang Pi-Yeh, *Hartshorne Solutions* (9 June 2019), Solution 4.1.2, printed p. 84, generalizes the previous entry: with $Q$ distinct from the $P_i$ and $D=2P_1+\cdots+2P_r-(2r-1)Q$ of degree $1$, the same choice of $n$ gives $\ell(nD)=n+1-g\ge1$ and an $f$ with $(f)=D_0-2n(P_1+\cdots+P_r)+n(2r-1)Q$, so the poles are exactly at the $P_i$ and the order at each is $\ge 2n$.
:::
