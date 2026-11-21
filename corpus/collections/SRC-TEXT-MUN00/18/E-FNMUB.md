---
schema: qual/card@1
id: E-FNMUB
kind: problem
title: Uniqueness of continuous extensions into Hausdorff spaces
classification:
  areas:
  - topology
  topics:
  - Continuous Functions
  - Hausdorff Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §18 Exercise 13, printed p. 112; the stored
    statement is the printed one, an extension to the closure of A being meant.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 2" (1 January 2021), Exercise 18.13, PDF p. 13. Two presumed extensions
    differing at a point of the closure are separated by disjoint open sets in Y, and the
    intersection of their preimages is a neighbourhood of that point meeting A, where the
    two must agree. (tmp/sources/munkres-solutions-positron-ch2.pdf).
---

::: {.exercise}

Let $A \subset X$; let $f: A \to Y$ be continuous; let $Y$ be Hausdorff.
Show that if $f$ may be extended to a continuous function $g: \overline{A} \to Y$, then $g$ is uniquely determined by $f$.
:::

::: {.solution}

The argument is **"positron0802"**, *Solutions to Topology, Chapter 2* (1 January 2021), Exercise 18.13 (`tmp/sources/munkres-solutions-positron-ch2.pdf`); Whitman, *Solutions Manual* (30 November 2019), Exercise 18.13, manual p. 189, has the same proof. The statement was checked against Munkres, *Topology* (2000), §18 Exercise 13.

::: pf

::: {.pf-step #setup}
Let $g_{1},g_{2}\colon\overline{A}\to Y$ be continuous and suppose that $\restrictionof{g_1}{A}=\restrictionof{g_2}{A}=f$. Then $g_{1}$ and $g_{2}$ agree on $A$.

::: pf-proof
By hypothesis each $g_{i}$ extends $f$, so for $x\in A$ one has $g_{1}(x)=f(x)=g_{2}(x)$.
:::

:::

::: {.pf-step #point-separation}
If $g_{1}(x_{0})\neq g_{2}(x_{0})$ for some $x_{0}\in\overline{A}$, then there are disjoint open sets $U,V\subset Y$ with $g_{1}(x_{0})\in U$ and $g_{2}(x_{0})\in V$.

::: pf-proof
The two points $g_{1}(x_{0})$ and $g_{2}(x_{0})$ of the Hausdorff space $Y$ are distinct, so Hausdorffness supplies disjoint open neighbourhoods of them.
:::

:::

::: {.pf-step #neighbourhood}
With $U,V$ as in step [](#point-separation){.pf-ref} and
$$
W\coloneqq g_{1}^{-1}(U)\cap g_{2}^{-1}(V),
$$
the set $W$ is open in $\overline{A}$ and contains $x_{0}$, and there is a point $y\in W\cap A$.

:::: pf-proof

::: {.pf-step #open-set}
$W$ is an open neighbourhood of $x_{0}$ in $\overline{A}$.

::: pf-proof
Both $g_{1}$ and $g_{2}$ are continuous, so $g_{1}^{-1}(U)$ and $g_{2}^{-1}(V)$ are open in $\overline{A}$, and so is their intersection. Since $g_{1}(x_{0})\in U$ and $g_{2}(x_{0})\in V$, the point $x_{0}$ lies in both preimages.
:::

:::

::: {.pf-step #meets-A}
$W\cap A\neq\emptyset$.

::: pf-proof
Write $W=\overline{A}\cap O$ with $O$ open in $X$, possible because $W$ is open in the subspace $\overline{A}$. Then $x_{0}\in W\subset O$, and $x_{0}\in\overline{A}$; by Theorem 17.5(a) the open set $O$ containing $x_{0}$ meets $A$, so there is $y\in O\cap A$. Since $A\subset\overline{A}$, that $y$ also lies in $\overline{A}\cap O=W$.
:::

:::

::::

:::

::: {.pf-step #contradiction}
The hypotheses of step [](#point-separation){.pf-ref} lead to a contradiction.

::: pf-proof
Let $y\in W\cap A$, which exists by step [](#neighbourhood){.pf-ref}. Since $y\in A$, step [](#setup){.pf-ref} gives $g_{1}(y)=g_{2}(y)=f(y)$. Since $y\in g_{1}^{-1}(U)$ we get $f(y)\in U$, and since $y\in g_{2}^{-1}(V)$ we get $f(y)\in V$; thus $f(y)\in U\cap V=\varnothing$, which is impossible.
:::

:::

::: pf-step
Therefore the continuous extension of $f$ to $\overline{A}$ is unique when it exists.

::: pf-proof
Step [](#contradiction){.pf-ref} shows that no point $x_{0}\in\overline{A}$ can have $g_{1}(x_{0})\neq g_{2}(x_{0})$, so $g_{1}=g_{2}$ for any two continuous extensions of $f$ to $\overline{A}$.
:::

:::

:::

:::
