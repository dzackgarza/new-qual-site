---
schema: qual/card@1
id: P-BKS04-4B
kind: problem
title: Unique maximum of $\log\prod x_i$ on the simplex $\sum a_ix_i=1$, $x_i>0$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against the retained UC Berkeley Spring 2004 preliminary exam and its companion solution packet.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Compared the authored solution with the retained `s04solution.pdf` solution packet.
---

::: {.problem}
Let $a_1,\ldots,a_n$ be positive real numbers.
Let $\Delta$ be the set of points $\mathbf x\in\RR^n$ satisfying the conditions

$$
\sum_{i=1}^na_ix_i=1,\quad x_i>0\text{ for all }i.
$$

Prove that the function $\log\left(\prod_{i=1}^nx_i\right)$ has a unique maximum on $\Delta$ and find the point where it occurs.
:::

::: {.solution}
The given function is continuous and approaches $-\infty$ at every point on the boundary of $\Delta$ (since each $x_i$ is bounded above, and at least one of them approaches zero at every point on the boundary).
Hence a maximum exists.
By Lagrange multipliers, at a maximum we must have $d\log\left(\prod_{i=1}^nx_i\right)=\lambda\,d\sum_{i=1}^na_ix_i$ for some $\lambda$, or $\sum_idx_i/x_i=\lambda\sum_ia_i\,dx_i$. Hence $(x_1,\ldots,x_n)=(1/\lambda)(1/a_1,\ldots,1/a_n)$. Combining this with the equation $\sum_ia_ix_i=1$ shows that $\lambda=n$ and $(x_1,\ldots,x_n)=(1/n)(1/a_1,\ldots,1/a_n)$. This locates the maximum and proves that it is unique.

Alternative solution: The arithmetic-mean--geometric-mean inequality gives

$$
\frac{\sum_{i=1}^na_ix_i}{n}\geq\left(\prod_{i=1}^n(a_ix_i)\right)^{1/n},
$$

with equality if and only if $a_1x_1=\cdots=a_nx_n$. On $\Delta$, the left hand side is constant, so we get an upper bound on $\prod_{i=1}^nx_i$, attained exactly when $a_1x_1=\cdots=a_nx_n$. It follows that there is a unique maximum where $a_ix_i=1/n$ for all $i$; that is, $x_i=1/(na_i)$ for all $i$.
:::
