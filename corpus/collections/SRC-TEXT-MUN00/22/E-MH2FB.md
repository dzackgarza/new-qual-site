---
schema: qual/card@1
id: E-MH2FB
kind: problem
title: Continuity of $xy^{-1}$ characterizes topological groups
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
    Read against Munkres, Topology (2000), §22 Supplementary Exercise 1, printed p. 145,
    with the definition of topological group printed there; the stored statement is the
    printed equivalence.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second Edition
    by James Munkres: Solutions Manual" (30 November 2019), Exercise TG.1, printed p. 259.
    Both directions are his: from the group axioms the map x y -> x y^{-1} is a composite of
    multiplication with the continuous map (x,y) -> (x, y^{-1}), and conversely separate
    continuity of that map gives inversion (fixing the first variable at the identity) and
    then multiplication. (tmp/sources/munkres-solutions-whitman.pdf).
---

::: {.exercise}

Let $H$ denote a group that is also a topological space satisfying the $T_1$ axiom.
Show that $H$ is a topological group if and only if the map of $H \times H$ into $H$ sending $x \times y$ into $x \cdot y^{-1}$ is continuous.
:::

::: {.solution}

Both directions are due to **Dan Whitman**, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise TG.1 (`tmp/sources/munkres-solutions-whitman.pdf`); "positron0802", *Solutions to Topology, Chapter 2* (1 January 2021), Supplementary Exercise 1, has the same. The statement was checked against Munkres, *Topology* (2000), §22 Supplementary Exercise 1, with the definition of a topological group there, Exercise 18.4, Exercise 18.10 and Exercise 18.11.

Throughout, $H$ is a group and a $T_{1}$ space, $e$ is its identity, and
$$
h\colon H\times H\longrightarrow H,\qquad h(x,y)\coloneqq x\cdot y^{-1}.
$$

::: pf

::: {.pf-step #forward}
If $H$ is a topological group, then $h$ is continuous.

::: pf-proof
Multiplication $m\colon H\times H\to H$, $m(x,y)=x\cdot y$, and inversion $\iota\colon H\to H$, $\iota(y)=y^{-1}$, are continuous by the definition of a topological group (printed p. 145), so $\mathrm{id}_{H}\times\iota$ is continuous by Exercise 18.10; and $h=m\circ(\mathrm{id}_{H}\times\iota)$ since $m(x,\iota(y))=x\cdot y^{-1}$. A composite of continuous maps is continuous.
:::

:::

::: {.pf-step #inversion}
If $h$ is continuous, then inversion $\iota$ is continuous.

::: pf-proof
A continuous map is continuous in each variable separately (Exercise 18.11), so for the fixed point $e$ the map $x\mapsto h(e,x)$ is continuous. The map $x\mapsto e\times x$ is continuous because it is an imbedding (Exercise 18.4), and $h(e,x)=e\cdot x^{-1}=x^{-1}$; so $x\mapsto x^{-1}$, which is $\iota$, is a composite of continuous maps.
:::

:::

::: {.pf-step #multiplication}
If $h$ and $\iota$ are continuous, then multiplication $m$ is continuous.

::: pf-proof
By step [](#inversion){.pf-ref} and Exercise 18.10 the map $(x,y)\mapsto(x,\iota(y))=(x,y^{-1})$ is continuous, and
$$
m(x,y)=x\cdot y=x\cdot(y^{-1})^{-1}=h\big(x,y^{-1}\big),
$$
the middle equality because inversion is an involution. So $m$ is the composite $h\circ(\mathrm{id}_{H}\times\iota)$ of continuous maps.
:::

:::

::: pf-step
Therefore $H$ is a topological group if and only if $h$ is continuous.

::: pf-proof
If $H$ is a topological group then $h$ is continuous by step [](#forward){.pf-ref}. Conversely, if $h$ is continuous then inversion is continuous by step [](#inversion){.pf-ref} and multiplication is continuous by step [](#multiplication){.pf-ref}, which with the $T_{1}$ hypothesis is exactly the definition of a topological group (printed p. 145).
:::

:::

:::

:::
