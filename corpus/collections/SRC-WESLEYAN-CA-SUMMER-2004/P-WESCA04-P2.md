---
schema: qual/card@1
id: P-WESCA04-P2
kind: problem
title: "Unions and intersections of two simply connected planar domains"
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Complex Analysis section 1.3, problem 2 (August 2, 2004) in the deterministic MinerU Flash extraction assets/attachments/analysis_2003-2007_extracted.md.
---

::: {.problem}
Let $D_1,D_2\subset\CC$ be simply connected domains whose intersection is nonempty and connected.
Prove that both
\[
D_1\cap D_2
\qquad\text{and}\qquad
D_1\cup D_2
\]
are simply connected.
:::

::: {.solution}

We use the standard planar-domain characterization:

> A domain
> \[
> \Omega\subseteq\CC
> \]
> is simply connected if and only if
> \[
> \widehat{\CC}\setminus\Omega
> \]
> is connected.

This is the classical complement criterion for plane domains; see, for
example, Conway, *Functions of One Complex Variable I*, the chapter on
simply connected regions.

::: pf

::: {.pf-step #s1-1}

The intersection
\[
D_1\cap D_2
\]
is a domain.


::: pf-proof

It is open because it is the intersection of two open sets.
It is nonempty and connected by hypothesis.
Thus it is a domain.

:::

:::

::: {.pf-step #s1-2}

For
\[
j=1,2,
\]
the set
\[
K_j
\coloneqq
\widehat{\CC}\setminus D_j
\]
is connected.


::: pf-proof

Each
\[
D_j
\]
is a simply connected plane domain.
Apply the planar-domain complement criterion.

:::

:::

::: {.pf-step #s1-3}

Both sets
\[
K_1
\quad\text{and}\quad
K_2
\]
contain the point at infinity
\[
\infty.
\]


::: pf-proof

Each
\[
D_j
\]
is contained in
\[
\CC
\subset
\widehat{\CC},
\]
so
\[
\infty\notin D_j.
\]
Hence
\[
\infty\in K_j.
\]

:::

:::

::: {.pf-step #s1-4}

The union
\[
K_1\cup K_2
\]
is connected.


::: pf-proof

By step [](#s1-2){.pf-ref}, both $K_1$ and $K_2$ are connected.
By step [](#s1-3){.pf-ref},
\[
K_1\cap K_2
\]
contains
\[
\infty,
\]
so the two connected sets meet.
The union of two connected subsets with nonempty intersection is connected.

:::

:::

::: {.pf-step #s1-5}

One has
\[
\widehat{\CC}
\setminus
(D_1\cap D_2)
=
K_1\cup K_2.
\]


::: pf-proof

This is De Morgan's law:
\[
\widehat{\CC}
\setminus
(D_1\cap D_2)
=
(\widehat{\CC}\setminus D_1)
\cup
(\widehat{\CC}\setminus D_2).
\]

:::

:::

::: {.pf-step #s1-6}

Therefore
\[
\boxed{
D_1\cap D_2
\text{ is simply connected}.
}
\]


::: pf-proof

By step [](#s1-1){.pf-ref},
\[
D_1\cap D_2
\]
is a domain.
By steps [](#s1-4){.pf-ref} through [](#s1-5){.pf-ref}, its complement in the Riemann sphere is connected.
Apply the planar-domain complement criterion.

:::

:::

::: {.pf-step #s1-7}

The intersection
\[
D_1\cap D_2
\]
is path-connected.


::: pf-proof

Every open connected subset of
\[
\RR^2\cong\CC
\]
is path-connected.
Indeed, fixing a point $z_0$ in an open connected set $U$, the set of points
that can be joined to $z_0$ by a polygonal path in $U$ is both open and
closed in $U$, hence equals $U$.
Apply this to
\[
U=D_1\cap D_2.
\]

:::

:::

::: {.pf-step #s1-8}

The union
\[
D_1\cup D_2
\]
is simply connected.


::: pf-proof

The sets
\[
D_1
\quad\text{and}\quad
D_2
\]
are open and simply connected.
Their intersection is nonempty and path-connected by step [](#s1-7){.pf-ref}.

Choose
\[
z_0\in D_1\cap D_2.
\]
The Seifert--van Kampen theorem gives
\[
\pi_1(D_1\cup D_2,z_0)
\cong
\pi_1(D_1,z_0)
*_{\pi_1(D_1\cap D_2,z_0)}
\pi_1(D_2,z_0).
\]
Since
\[
\pi_1(D_1)=\pi_1(D_2)=0,
\]
the pushout group is trivial.

The union is path-connected because it is the union of two path-connected
sets with nonempty intersection.
Hence
\[
D_1\cup D_2
\]
is simply connected.

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} proves the assertion for the intersection, and step [](#s1-8){.pf-ref} proves
the assertion for the union.

:::

:::

:::
