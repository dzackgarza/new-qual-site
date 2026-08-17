---
schema: qual/card@1
id: P-HPTFQ
kind: problem
title: "- Prove Cauchy's theorem."
classification:
  areas:
  - algebra
  topics:
  - group-actions
  - cosets-and-lagrange
  - p-groups
relations: []
review: draft
solved: false
---

::: problem
- Prove Cauchy's theorem.

> Induce on $\size G$.
> Assume $\size G > p$ and pick $g\neq 1$.
> If $p\divides \size g$, use cyclic group theory, so assume otherwise.
> Use that $\size G = \size G/N \size N$ so $p$ divides $\size G/N$, apply IH to get an element of order $p$ in the quotient.
> Then $y\not\in N$ but $y^p\in N$, so $\gens{y}\neq \gens{y^p}$ since $y^p\in N \implies \gens{y^p} \subseteq N$.
> Get $p\divides \size \gens{y}$, apply IH.
:::
