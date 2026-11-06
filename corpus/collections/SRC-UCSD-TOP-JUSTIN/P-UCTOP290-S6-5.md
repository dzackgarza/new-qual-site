---
schema: qual/card@1
id: P-UCTOP290-S6-5
kind: problem
title: Represent a singular homology class by a simplicial circuit
classification:
  areas:
  - topology
  topics:
  - Singular Homology
  - Simplicial Homology
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-10-31
  note: Read sheet 6, Problem 5 in its checked-in extraction and page image.
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against UCSD Math 290 Fall 2014 problem sheet 6, problem 5
    (assets/attachments/UCSD_290_F14_sheet6.pdf, printed page 258), from the
    checked-in extraction and a 300 dpi render. The printed problem asks, for a
    class c in H_n(X) represented by a singular n-cycle z, for a simplicial
    complex K, a class mu in H_n(K) and a map f: |K| -> X with f_*(mu) = c, and
    for the singular set of |K|, the points without a neighbourhood homeomorphic
    to R^n, to be a subcomplex of dimension at most n-2. The card states exactly
    these requirements, so no repair was needed.
---

::: {.problem}
Given $c\in H_n(X;\ZZ)$, construct a finite
simplicial complex $K$, a class
$\mu\in H_n(K;\ZZ)$, and a map $f:K\to X$
with $f_*\mu=c$. Arrange that the set of
points of $K$ without a neighborhood
homeomorphic to $\RR^n$ lies in a
subcomplex of dimension at most $n-2$.
:::

::: {.solution}

Let $c\in H_n(X;\ZZ)$ be represented by the finite singular cycle
$z=\sum_jm_j\sigma_j$ with $m_j\ne0$, and let $\Delta^n$ be the standard
$n$-simplex.

::: pf

::: {.pf-step #copies}

Taking $\abs{m_j}$ copies of $\Delta^n$ for each $j$, oriented positively when
$m_j>0$ and negatively when $m_j<0$, and labelling every face of each copy by
the restriction of $\sigma_j$ to that face, produces a finite set of oriented
$n$-simplices whose oriented boundary is zero as a formal sum of labelled
$(n-1)$-simplices.

::: pf-proof

This is just the chain $\partial z$ read formally: the coefficient of a
labelled $(n-1)$-simplex $\tau$ in that boundary is the sum of the
coefficients of the copies having $\tau$ as a face with a given orientation,
and $\partial z=0$ says every such coefficient vanishes.

:::

:::

::: {.pf-step #glue}

Each positively oriented occurrence of a labelled $(n-1)$-simplex in that
boundary is matched with a negatively oriented occurrence of the same labelled
simplex, and gluing the matched pairs of faces by the identity of their
parameter simplices gives a finite $\Delta$-complex $K$ and a continuous map
$f\colon|K|\to X$.

::: pf-proof

Since the formal boundary vanishes, the occurrences of each labelled
$(n-1)$-simplex split into those with sign $+$ and those with sign $-$, and
within each sign group the parameterizations are the same map of
$\Delta^{n-1}$, so faces are matched within each labelled simplex and the
gluing is by an affine identification of parameter simplices. The maps
$\sigma_j$ agree on the faces glued together, because two faces are glued only
when they carry the same labelled simplex; so they descend to a continuous map
$f$ on the quotient. The quotient of finitely many simplices by finitely many
identifications of faces is a finite $\Delta$-complex; subdividing it if an
identification is not simplicial gives a finite simplicial complex with the
same realization.

:::

:::

::: {.pf-step #fundamental}

The sum $\mu$ of all the top-dimensional simplices of $K$, with the
orientations they inherit, is a cycle, and $f_*\mu=c$.

::: pf-proof

In the quotient every codimension-one face is either an interior face, glued
to exactly one other face with which it cancels in the boundary, or a
remaining face; but the remaining faces are the unmatched occurrences, and
there are none because every occurrence was matched. So $\partial\mu=0$, and
$\mu\in H_n(K;\ZZ)$. Pushing $\mu$ forward along $f$ gives
$\sum_jm_j\sigma_j=z$, because $f$ restricted to the copy labelled $\sigma_j$
is $\sigma_j$ and the orientations were chosen with the signs $m_j$; hence
$f_*[\mu]=[z]=c$.

:::

:::

::: {.pf-step #circuit}

The set of points of $|K|$ without a neighbourhood homeomorphic to $\RR^n$ is
contained in the $(n-2)$-skeleton of $K$; for $n=1$ it is empty and $|K|$ is a
disjoint union of circles.

::: pf-proof

A point in the interior of a top simplex has a neighbourhood homeomorphic to
$\RR^n$. A point in the relative interior of a codimension-one face lies in
exactly two top simplices, glued along that face by an affine identification,
so its neighbourhood is the union of two half-balls along their flat boundary,
which is homeomorphic to $\RR^n$. Hence a singular point must lie in the
relative interior of a face of dimension at most $n-2$, which is the
$(n-2)$-skeleton. For $n=1$ the $(n-2)$-skeleton is empty, and a finite
$1$-dimensional $\Delta$-complex in which every edge is matched with another
edge and every vertex is a manifold point is a disjoint union of circles.

:::

:::

:::


:::
