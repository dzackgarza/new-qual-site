---
schema: qual/card@1
id: E-AZ6JL
kind: problem
title: Three topologies on the unit square
classification:
  areas:
  - topology
  topics:
  - Order Topology
  - Product Topology
  - Subspace Topology
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §16 Exercise 10, printed p. 92; the stored
    statement is the printed one, I = [0,1] being a subspace of R.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 2" (1 January 2021), Exercise 16.10, PDF pp. 5-6. The answer and the two
    witnesses for incomparability are his: I x (1/2,1] is product-open but no dictionary
    basis element at (1/2,1) stays inside it, and {1/2} x (0,1) is a dictionary interval but
    no product basis element at (1/2,1/2) stays inside it. The two inclusions into the
    subspace topology are proved on the card: the product lies in it by Exercise 16.9 and
    Theorem 16.3, and every dictionary basis element is the trace of a dictionary-open set
    of R x R, the half-open ones at the corners included. (tmp/sources/munkres-solutions-
    positron-ch2.pdf).
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Restructured into a structured proof under #2, the two incomparability witnesses and the two
    inclusions as top-level steps and the comparison as the QED step. Re-checked every claim: the
    strip $I\times(\tfrac12,1]$ is product-open and no dictionary basis element through
    $(\tfrac12,1)$ stays inside it, since such an element contains a point $(r,s)\succ(\tfrac12,1)$
    with $r>\tfrac12$ and then $(r,0)$; the slice $\{\tfrac12\}\times(0,1)$ is a dictionary interval
    but no product basis element through its centre stays inside it, since $A$ open in $I$ and
    $\tfrac12\in A$ forces some other $x\in A$; the product lies in the subspace topology by
    Exercise 16.9 and Theorem 16.3 with basis elements $\{x\}\times B$; and the three shapes of
    dictionary basis element of the square are traces of dictionary-open sets of $\RR^2$, the
    half-open corner intervals included. Added: that no interval about $\tfrac12$ in $I$ is a single
    point, and that the square's least and greatest elements are why only three shapes occur. No
    defect found in the statement, §16 Exercise 10. Not claimed: a printed publication, and
    Whitman's pp. 156--158 were not re-read in this batch.
---

::: {.exercise}

Let $I = [0, 1]$.
Compare the product topology on $I \times I$, the dictionary order topology on $I \times I$, and the topology $I \times I$ inherits as a subspace of $\RR \times \RR$ in the dictionary order topology.
:::

::: {.solution}
The answer, and the two witnesses for the incomparability of the product and dictionary order topologies, are those of the retained published solution **positron0802, *Solutions to Topology, Chapter 2* (1 January 2021), Exercise 16.10, PDF pp. 5--6** (`tmp/sources/munkres-solutions-positron-ch2.pdf`); the two inclusions into the subspace topology are proved below from Exercise 16.9 and Theorem 16.3, which that set quotes from the preceding exercise. Whitman, printed pp. 156--158, gives the same answer. On $I\times I$ with $I=[0,1]$, let $\mathcal{T}_1$ be the product topology, $\mathcal{T}_2$ the dictionary order topology and $\mathcal{T}_3$ the topology inherited from $\RR\times\RR$ in the dictionary order topology; write $\prec$ for the dictionary order, in which $(0,0)$ is least and $(1,1)$ greatest in $I\times I$.

::: pf

::: {.pf-step #dictionary-not-product}
$\mathcal{T}_2\not\subseteq\mathcal{T}_1$.

:::: pf-proof

::: {.pf-step #upper-strip}
$U=I\times(\tfrac12,1]$ lies in $\mathcal{T}_1$ and contains $(\tfrac12,1)$, but no $\mathcal{T}_2$-basis element containing $(\tfrac12,1)$ lies inside $U$.

::: pf-proof
$U$ is a basis element of the product topology, $(\tfrac12,1]$ being open in $I$ and $I$ itself open in $I$. Let $B$ be a $\mathcal{T}_2$-basis element with $(\tfrac12,1)\in B$. Since $(\tfrac12,1)\ne(1,1)$, the set $B$ contains a point $(r,s)\ne(\tfrac12,1)$ with $(\tfrac12,1)\prec(r,s)$: a basis element containing an interior point of an interval contains points on both sides of it, and a basis element of the form $[(0,0),(r,s))$ contains $(r,s)$ itself. Then $r>\tfrac12$ or $r=\tfrac12$ and $s>1$; the second is impossible in $I\times I$, so $r>\tfrac12$. Hence $(\tfrac12,1)\prec(r,0)\prec(r,s)$, so $(r,0)\in B$, while $(r,0)\notin U$ because $0\notin(\tfrac12,1]$. Thus $B\not\subseteq U$.
:::

:::

::: {.pf-step}
$U\notin\mathcal{T}_2$, so $\mathcal{T}_2\not\subseteq\mathcal{T}_1$.

::: pf-proof
If $U$ lay in $\mathcal{T}_2$, it would be a union of $\mathcal{T}_2$-basis elements and so would contain one through each of its points; step [](#upper-strip){.pf-ref} exhibits a point of $U$ through which no such element lies inside $U$.
:::

:::

:::

:::

::: {.pf-step #product-not-dictionary}
$\mathcal{T}_1\not\subseteq\mathcal{T}_2$.

:::: pf-proof

::: {.pf-step #vertical-slice}
$V=\{\tfrac12\}\times(0,1)$ lies in $\mathcal{T}_2$ and contains $(\tfrac12,\tfrac12)$, but no $\mathcal{T}_1$-basis element containing $(\tfrac12,\tfrac12)$ lies inside $V$.

::: pf-proof
$V=\big((\tfrac12,0),(\tfrac12,1)\big)$, an open interval in the dictionary order, so $V\in\mathcal{T}_2$. Let $A\times B$ be a $\mathcal{T}_1$-basis element with $(\tfrac12,\tfrac12)\in A\times B$, so $A$ is open in $I$ and $\tfrac12\in A$; then $A$ contains some $x\ne\tfrac12$, because no ball about $\tfrac12$ in $I$ is the single point $\tfrac12$. Hence $(x,\tfrac12)\in A\times B$ while $(x,\tfrac12)\notin V$, so $A\times B\not\subseteq V$.
:::

:::

::: {.pf-step}
$V\notin\mathcal{T}_1$, so $\mathcal{T}_1\not\subseteq\mathcal{T}_2$.

::: pf-proof
As in step [](#upper-strip){.pf-ref}'s application, a $\mathcal{T}_1$-open set contains a $\mathcal{T}_1$-basis element about each of its points; step [](#vertical-slice){.pf-ref} shows $V$ fails this at $(\tfrac12,\tfrac12)$.
:::

:::

:::

:::

::: {.pf-step #product-inside-subspace}
$\mathcal{T}_1\subseteq\mathcal{T}_3$.

::: pf-proof
By Exercise 16.9 the dictionary order topology on $\RR\times\RR$ is the product topology $\RR_d\times\RR$, with $\RR_d$ discrete; by Theorem 16.3 (printed p. 90) a subspace of a product has the product of the subspace topologies, so $\mathcal{T}_3$ is the topology of $\RR_d\restrictionof_I\times\RR\restrictionof_I$, where $\RR_d\restrictionof_I$ is discrete and $\RR\restrictionof_I$ is the usual topology of $I$. A $\mathcal{T}_1$-basis element is $A\times B$ with $A,B$ open in $I$, and
$$
A\times B=\bigcup_{x\in A}\{x\}\times B
$$
is a union of basis elements $\{x\}\times B$ of $\mathcal{T}_3$, since $\{x\}$ is open in the discrete space $\RR_d\restrictionof_I$ and $B$ is open in $I$. So every basis element of $\mathcal{T}_1$ lies in $\mathcal{T}_3$.
:::

:::

::: {.pf-step #dictionary-inside-subspace}
$\mathcal{T}_2\subseteq\mathcal{T}_3$.

:::: pf-proof

::: {.pf-step #traces}
Every basis element of $\mathcal{T}_2$ is the trace on $I\times I$ of a basis element of the dictionary order topology of $\RR\times\RR$.

::: pf-proof
An open interval $\big((a,b),(c,d)\big)$ of the square is the trace of the open interval with the same endpoints in $\RR\times\RR$; the half-open interval $[(0,0),(c,d))$ is the trace of $\big((0,-1),(c,d)\big)$, since $(0,-1)\prec(0,0)$ and no point of the square lies below $(0,0)$; and the half-open interval $\big((a,b),(1,1)\big]$ is the trace of $\big((a,b),(1,2)\big)$, since $(1,1)\prec(1,2)$ and no point of the square lies above $(1,1)$. These are the three shapes of basis element of the dictionary order topology on the square, the square having a least and a greatest element.
:::

:::

::: {.pf-step}
$\mathcal{T}_2\subseteq\mathcal{T}_3$.

::: pf-proof
A trace on $I\times I$ of an open set of $\RR\times\RR$ in the dictionary order topology is open in the subspace topology $\mathcal{T}_3$, so step [](#traces){.pf-ref} expresses every basis element of $\mathcal{T}_2$ as an open set of $\mathcal{T}_3$.
:::

:::

:::

:::

::: {.pf-step}
$\mathcal{T}_1$ and $\mathcal{T}_2$ are incomparable, and $\mathcal{T}_3$ is strictly finer than each of them.

::: pf-proof
Steps [](#dictionary-not-product){.pf-ref} and [](#product-not-dictionary){.pf-ref} give the incomparability. Steps [](#product-inside-subspace){.pf-ref} and [](#dictionary-inside-subspace){.pf-ref} give the two inclusions into $\mathcal{T}_3$, and both are strict: $\mathcal{T}_3=\mathcal{T}_1$ would give $\mathcal{T}_2\subseteq\mathcal{T}_1$, and $\mathcal{T}_3=\mathcal{T}_2$ would give $\mathcal{T}_1\subseteq\mathcal{T}_2$, neither of which holds. Hence the subspace topology from $\RR\times\RR$ is strictly finer than both.
:::

:::

:::
:::
