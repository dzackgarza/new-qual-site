---
schema: qual/card@1
id: E-0S3OA
kind: problem
title: Subgroups and closures of subgroups are topological groups
classification:
  areas:
  - topology
  topics:
  - Topological Groups
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §22 Supplementary Exercise 3, printed p. 146,
    with Exercise 17.9 and Theorem 18.1; the stored statement is the printed sentence.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second Edition
    by James Munkres: Solutions Manual" (30 November 2019), Exercise TG.3, printed p. 264.
    His argument: the closure of a subgroup is a subgroup, because f(H x H) lies in H for
    the continuous f(x,y) = x y^{-1} and f(closure H x closure H) lies in the closure of f(H
    x H); both H and its closure are subspaces of a T1 space and the operations are
    restrictions of continuous ones. (tmp/sources/munkres-solutions-whitman.pdf).
---

::: {.exercise}

Let $H$ be a subspace of the topological group $G$.
Show that if $H$ is also a subgroup of $G$, then both $H$ and $\overline{H}$ are topological groups.
:::

::: {.solution}

The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise TG.3, printed p. 264** (`tmp/sources/munkres-solutions-whitman.pdf`); the argument is his, and its four quoted inputs are named in step [](#inputs){.pf-ref}.

Let $G$ be a topological group, $H$ a subspace of $G$ that is also a subgroup, and $f:G\times G\to G$ the map $f(x,y)=x\cdot y^{-1}$.

::: pf

::: {.pf-step #inputs}
$f$ is continuous, $\overline{H\times H}=\overline H\times\overline H$ in $G\times G$, a continuous map sends closures into closures of images, and a subset of a closure lies in the closure of a subset: $A\subseteq B$ implies $\overline A\subseteq\overline B$.

::: pf-proof
$f=m\circ(\mathrm{id}\times\iota)$ is a composite of the continuous multiplication and inversion of $G$, hence continuous (Theorem 18.2(c)). The closure identity is Exercise 17.9. For a continuous $f$ and any $A$ one has $f(\overline A)\subseteq\overline{f(A)}$ (Theorem 18.1(2)), and $A\subseteq B$ implies $\overline A\subseteq\overline B$ (Exercise 17.6(a)).
:::

:::

::: {.pf-step #t1}
$H$ and $\overline H$ satisfy the $T_{1}$ axiom.

::: pf-proof
$G$ satisfies it, and a subspace of a $T_{1}$ space does: for distinct $x,y$ in the subspace there is a neighbourhood of $x$ in $G$ missing $y$, whose trace is a neighbourhood of $x$ in the subspace missing $y$, and symmetrically (Exercise 17.15).
:::

:::

::: {.pf-step #closure-subgroup}
$\overline H$ is a subgroup of $G$.

:::: {.pf-proof}

::: {.pf-step #closure-inside}
$f\big(\overline H\times\overline H\big)\subseteq\overline H$.

::: pf-proof
By step [](#inputs){.pf-ref}, $\overline{H\times H}=\overline H\times\overline H$ and $f\big(\overline H\times\overline H\big)\subseteq\overline{f(H\times H)}$. As $H$ is a subgroup, $f(H\times H)\subseteq H$, so $\overline{f(H\times H)}\subseteq\overline H$. Composing the inclusions gives $f\big(\overline H\times\overline H\big)\subseteq\overline H$.
:::

:::

::: {.pf-step #criterion}
A subset $K$ of a group $G$ containing $e$ is a subgroup exactly when $x\cdot y^{-1}\in K$ for all $x,y\in K$.

::: pf-proof
If $K$ is a subgroup this holds. Conversely, taking $y=x$ gives $x\cdot x^{-1}=e\in K$, then taking $x=e$ gives $y^{-1}\in K$, and then $x\cdot(y^{-1})^{-1}=x\cdot y\in K$; so $K$ is closed under inversion and multiplication and contains $e$. Here $\overline H\ne\varnothing$ because $e\in H\subseteq\overline H$.
:::

:::

::: {.pf-step #closure-closed}
Hence $\overline H$ is a subgroup.

::: pf-proof
By step [](#closure-inside){.pf-ref} the set $\overline H$ satisfies the criterion of step [](#criterion){.pf-ref}.
:::

:::

::::

:::

::: {.pf-step #operations}
The multiplication and inversion of $H$, and of $\overline H$, are continuous in the subspace topology.

::: pf-proof
The multiplication of $G$ is a continuous map $G\times G\to G$; on $H$ the multiplication is the composite of the continuous map $H\times H\to G\times G$, $(x,y)\mapsto(x,y)$, with it, so it is continuous (Theorem 18.2(c)), and it is the restriction to the subspace $H\times H$ of $G\times G$ (Theorem 18.2(d)). The same applies with $\overline H$ in place of $H$, and the inversion of $H$ and of $\overline H$ is the restriction of the continuous inversion of $G$ to that subspace.
:::

:::

::: {.pf-qed}
$H$ is a group by hypothesis with continuous operations by step [](#operations){.pf-ref}, and so is a topological group; $\overline H$ is a group by step [](#closure-subgroup){.pf-ref}, $T_{1}$ by step [](#t1){.pf-ref}, and has continuous operations by step [](#operations){.pf-ref}, and so is a topological group.
:::

:::

:::
