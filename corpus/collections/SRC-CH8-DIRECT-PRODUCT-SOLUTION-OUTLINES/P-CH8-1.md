---
schema: qual/card@1
id: P-CH8-1
kind: problem
title: External direct products of finitely many groups are groups
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
    Chapter 8, External Direct Products, Exercises, exercise 1, printed page
    167 (PDF page 182 of
    tmp/sources/Gallian-Contemporary-Abstract-Algebra-7e.pdf, which is not
    tracked in the repository). The printed exercise reads: Prove that the external direct product of any finite number of groups is a group. (This exercise is referred to in this chapter.). The card asks exactly this, so no repair was needed.
- event: solution-written
  by: claude
  date: 2026-11-06
  note: >-
    The retained outline on the card is a run-on paragraph of extraction residue; its argument, the componentwise verification of closure, associativity, identity and inverse, is kept and written as four steps, with the coordinates indexed by the factors.
---

::: {.problem}
Prove that the external direct product of any finite number of groups is a group.
:::

::: {.solution}

Let $G_1,\dots,G_n$ be groups with identities $e_1,\dots,e_n$, and let
$G=G_1\oplus\cdots\oplus G_n$ be their external direct product: the set of
$n$-tuples $(g_1,\dots,g_n)$ with $g_i\in G_i$, with the operation
$$
(g_1,\dots,g_n)(h_1,\dots,h_n)=(g_1h_1,\dots,g_nh_n).
$$

::: pf

::: {.pf-step #closed}

The operation is well defined and $G$ is closed under it; it is associative.

::: pf-proof

Each $g_ih_i$ lies in $G_i$, because $G_i$ is closed under its operation, so
the product of two $n$-tuples is again an $n$-tuple of elements of the
factors. Associativity is componentwise: for triples $(a_i),(b_i),(c_i)$, both
$(a_ib_i)c_i$ and $a_i(b_ic_i)$ equal the same element of $G_i$ by
associativity in $G_i$, so the two $n$-tuples $(a_ib_i)c_i$ and $a_i(b_ic_i)$
agree in every coordinate and hence are equal.

:::

:::

::: {.pf-step #identity}

$e=(e_1,\dots,e_n)$ is a two-sided identity, and
$(g_1,\dots,g_n)^{-1}=(g_1^{-1},\dots,g_n^{-1})$.

::: pf-proof

$(g_1,\dots,g_n)(e_1,\dots,e_n)=(g_1e_1,\dots,g_ne_n)=(g_1,\dots,g_n)$ and
symmetrically on the other side, computed coordinate by coordinate. For the
inverse,
$(g_1,\dots,g_n)(g_1^{-1},\dots,g_n^{-1})=(g_1g_1^{-1},\dots,g_ng_n^{-1})=(e_1,\dots,e_n)$,
and the same product in the other order also gives $e$; each $g_i^{-1}$ exists
in $G_i$ because $G_i$ is a group.

:::

:::

::: {.pf-step #group}

$G$ is a group, so the external direct product of finitely many groups is a
group.

::: pf-proof

Steps [](#closed){.pf-ref} and [](#identity){.pf-ref} verify the three group
axioms: a well-defined associative binary operation, a two-sided identity, and
a two-sided inverse for each element. Nothing in the argument uses more than
finiteness of the tuple, so the same computation gives the external direct
product of any finite number of groups; the printed exercise refers to this
result later in the chapter, where the product of $n$ factors is written
$G_1\oplus\cdots\oplus G_n$ and its elements are added coordinatewise when the
factors are abelian.

:::

:::

:::


:::
