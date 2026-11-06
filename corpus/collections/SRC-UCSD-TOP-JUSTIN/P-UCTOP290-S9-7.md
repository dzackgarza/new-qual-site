---
schema: qual/card@1
id: P-UCTOP290-S9-7
kind: problem
title: Euler characteristics of projective spaces, products, surfaces, and complements
classification:
  areas:
  - topology
  topics:
  - Euler Characteristic
  - Homology
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-10-31
  note: Read sheet 9, Problem 7 in its checked-in extraction.
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against UCSD Math 290 Fall 2014 problem sheet 9, problem 7
    (assets/attachments/UCSD_290_F14_sheet9.pdf, printed pages 266 and 267),
    from the checked-in extraction and a 300 dpi render of both pages. The
    printed list is RP^2, RP^3, S^2 vee S^2, S^2 x S^2, S^2 x S^3, CP^3, the
    torus with two discs removed, the genus-four surface, R^3 minus the unit
    circle in the (x,y) plane, and R^2 minus five distinct points; the card
    lists the same ten in the same order, so no repair was needed.
---

::: {.problem}
Compute the Euler characteristic of each space:
$\RP^2$, $\RP^3$, $S^2\vee S^2$,
$S^2\times S^2$, $S^2\times S^3$, $\CP^3$,
a torus with two open disks removed,
$\Sigma_4$, $\RR^3$ minus the unit circle,
and $\RR^2$ minus five points.
:::

::: {.solution}

Write $\chi$ for the Euler characteristic, computed as the alternating sum of
the ranks of integral homology, which agrees with the alternating sum of the
numbers of cells of any finite CW structure.

::: pf

::: {.pf-step #projective}

$\boxed{\chi(\RP^2)=1}$, $\boxed{\chi(\RP^3)=0}$ and $\boxed{\chi(\CP^3)=4}$.

::: pf-proof

$\RP^n$ has a CW structure with exactly one cell in each dimension
$0,\dots,n$, so its Euler characteristic is $\sum_{k=0}^{n}(-1)^k$, which is
$1$ for $n=2$ and $0$ for $n=3$. $\CP^n$ has one cell in each even dimension
$0,2,\dots,2n$, so $\chi(\CP^3)=1+1+1+1=4$.

:::

:::

::: {.pf-step #products}

$\boxed{\chi(S^2\vee S^2)=3}$, $\boxed{\chi(S^2\times S^2)=4}$ and
$\boxed{\chi(S^2\times S^3)=0}$.

::: pf-proof

For a wedge at a point, $\widetilde H_*$ of the wedge is the direct sum of the
reduced homology of the factors, so $\chi(X\vee Y)=\chi(X)+\chi(Y)-1$; with
$\chi(S^2)=2$ this gives $2+2-1=3$. For a product of finite CW complexes the
product cell structure gives $\chi(X\times Y)=\chi(X)\chi(Y)$, so
$\chi(S^2\times S^2)=2\cdot2=4$ and $\chi(S^2\times S^3)=2\cdot0=0$.

:::

:::

::: {.pf-step #surfaces}

The torus with two open discs removed has $\boxed{\chi=-2}$, and
$\boxed{\chi(\Sigma_4)=-6}$.

::: pf-proof

$\chi(T^2)=0$, and removing the interior of a disc removes one $2$-cell from a
cell structure, decreasing $\chi$ by $1$; removing two decreases it by $2$,
giving $-2$. A closed orientable surface of genus $g$ has the cell structure
with one $0$-cell, $2g$ $1$-cells and one $2$-cell, so $\chi(\Sigma_g)=2-2g$
and $\chi(\Sigma_4)=2-8=-6$.

:::

:::

::: {.pf-step #circle}

If $C$ is the unit circle in the plane $z=0$, then $\boxed{\chi(\RR^3\setminus
C)=1}$.

::: pf-proof

One-point compactification identifies $\RR^3\setminus C$ with $S^3\setminus K$
for the compact subset $K=C\cup\{\infty\}$ of $S^3$, a circle together with a
point disjoint from it. Alexander duality gives $\widetilde H_i(S^3\setminus
K;\ZZ)\cong\widetilde H^{2-i}(K;\ZZ)$, and $\widetilde H^*(K;\ZZ)$ is $\ZZ$ in
degrees $0$ and $1$ and $0$ elsewhere, because $K$ has two components and its
only other cohomology is that of the circle in degree $1$. So $\widetilde H_1$
and $\widetilde H_2$ of $\RR^3\setminus C$ are each $\ZZ$ and all other
reduced groups vanish, giving $\chi=1-1+1=1$. The same answer comes from the
homotopy equivalence $\RR^3\setminus C\simeq S^1\vee S^2$.

:::

:::

::: {.pf-step #points}

$\boxed{\chi(\RR^2\setminus\{p_1,\dots,p_5\})=-4}$.

::: pf-proof

The plane with five points removed deformation retracts onto a wedge of five
circles, one around each puncture: the radial retraction of the complement of
a small disc around each puncture onto the boundary circle, composed with the
retraction of the punctured plane onto the union of those circles and a
connecting tree of arcs. A wedge of five circles has homology of rank $1$ in
degree $0$ and $5$ in degree $1$, so its Euler characteristic is $1-5=-4$. The
same count follows from additivity, each puncture decreasing $\chi$ by $1$
from $\chi(\RR^2)=1$.

:::

:::

:::


:::
