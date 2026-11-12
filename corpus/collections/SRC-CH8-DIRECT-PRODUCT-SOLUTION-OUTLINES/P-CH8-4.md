---
schema: qual/card@1
id: P-CH8-4
kind: problem
title: $G\oplus H$ is abelian if and only if $G$ and $H$ are
classification:
  areas:
    - algebra
  topics:
    - Direct Products
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against Gallian, Contemporary Abstract Algebra, seventh edition (2010),
    Chapter 8, External Direct Products, Exercises, exercise 4, printed page
    167 (PDF page 182 of
    tmp/sources/Gallian-Contemporary-Abstract-Algebra-7e.pdf, which is not
    tracked in the repository). The printed exercise reads: Show that G x H is Abelian if and only if G and H are Abelian. State the general case.. The card asks the same two questions, the equivalence and the general case, so no repair was needed.
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    The retained outline's pairwise comparison of coordinates is kept, split into the two directions, and the general case is stated as the coordinatewise argument over n factors.
---

::: {.problem}
Show that $G \oplus H$ is Abelian if and only if $G$ and $H$ are Abelian.
State the general case.
:::

::: {.solution}

Let $G,H$ be groups and $G\oplus H$ their external direct product with the
componentwise operation.

::: pf

::: {.pf-step #forward}

If $G\oplus H$ is abelian then $G$ and $H$ are abelian.

::: pf-proof

Let $g_1,g_2\in G$ and $h_1,h_2\in H$, and put $x=(g_1,h_1)$, $y=(g_2,h_2)$.
Since $G\oplus H$ is abelian, $xy=yx$, that is
$(g_1g_2,h_1h_2)=(g_2g_1,h_2h_1)$; equality of pairs gives $g_1g_2=g_2g_1$ and
$h_1h_2=h_2h_1$. As $g_1,g_2$ and $h_1,h_2$ were arbitrary, both $G$ and $H$
are abelian.

:::

:::

::: {.pf-step #backward}

If $G$ and $H$ are abelian then $G\oplus H$ is abelian.

::: pf-proof

Let $x=(g_1,h_1)$ and $y=(g_2,h_2)$ in $G\oplus H$. Then
$xy=(g_1g_2,h_1h_2)=(g_2g_1,h_2h_1)=yx$, the middle equality holding in each
coordinate by commutativity in $G$ and in $H$. So every two elements of
$G\oplus H$ commute.

:::

:::

::: {.pf-step #general}

The external direct product of finitely many groups is abelian if and only if
every factor is abelian.

::: pf-proof

Both directions are the coordinatewise computation above, with the index set
$\{1,\dots,n\}$ in place of $\{1,2\}$: if the product is abelian then
comparing the $i$-th coordinates of $xy$ and $yx$ for arbitrary $x,y$ shows
$G_i$ is abelian, and if every factor is abelian then the products agree
coordinate by coordinate. This is the general case the printed exercise asks
to state, and it uses no hypothesis beyond finiteness of the product.

:::

:::

:::


:::

::: {.remark}
Certificate. <https://github.com/dzackgarza/new-qual-site/blob/16c09abaa4/proofs/cards/CH8DirectProduct.lean> (`prod_comm_iff`) proves that a
direct product is abelian exactly when both factors are: one direction projects
the product commutator to each factor, the other assembles the two commutators
coordinatewise.
:::
