---
schema: qual/card@1
id: P-CASP20G
kind: problem
title: "Positive harmonic functions with h(0)=1 form a normal family"
classification:
  areas:
  - complex-analysis
  topics:
  - Harmonic Functions
  - Normal Families
  - Harnack Theorem
relations: []
review: draft
---

::: problem
Let $\mathcal{H}$ be the family of harmonic functions $h : \mathbb{D} \to \mathbb{R}$ with $h(0) = 1$ and $h(z) > 0$ for all $z \in \mathbb{D}$.
Show that every sequence in $\mathcal{H}$ admits a subsequence that converges uniformly on compact subsets of $\mathbb{D}$ to a function in $\mathcal{H}$.
:::

::: solution
Harnack's inequality gives, for $h\in\mathcal H$ and $|z|\le r<1$,
\[
\frac{1-r}{1+r}
\le h(z)\le
\frac{1+r}{1-r},
\]
because $h(0)=1$. Thus the family is uniformly bounded above and below on
every compact subset of $\mathbb D$.

Interior derivative estimates for harmonic functions then give equicontinuity
on compact subsets. By Arzelà--Ascoli and a diagonal argument, every sequence
$(h_n)$ has a subsequence converging uniformly on compact subsets to a harmonic
function $h$.

The convergence at $0$ gives $h(0)=1$. The lower Harnack bound passes to the
limit, so $h(z)>0$ for every $z\in\mathbb D$. Hence $h\in\mathcal H$, proving
the required normality.
:::
