---
schema: qual/card@1
id: E-HAT-3.C-15
kind: problem
title: "Pontryagin ring from polynomial cohomology"
classification:
  areas:
  - topology
  topics:
  - Cohomology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.C, Exercise 15; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.problem}
Suppose that $X$ is a path-connected H-space such that $H^*(X; \mathbb{Z})$ is free and finitely generated in each dimension, and $H^*(X; \mathbb{Q})$ is a polynomial ring $\mathbb{Q}[\alpha]$.
Show that the Pontryagin ring $H_*(X; \mathbb{Z})$ is commutative and associative, with a structure uniquely determined by the ring $H^*(X; \mathbb{Z})$.
:::

::: {.solution}
Put
\[
A=H^*(X;\mathbb Z).
\]
By hypothesis each graded piece of $A$ is free of finite rank, and
\[
A\otimes\mathbb Q\cong\mathbb Q[\alpha].
\]
Since the rational cohomology ring is graded-commutative and $\alpha^2\ne0$, the degree $d=|\alpha|$ is even. Moreover, $A^{nd}$ has rank one for every $n\ge0$, and all other positive-degree groups vanish.

Choose a generator $a_n$ of each $A^{nd}$, with $a_0=1$. After tensoring with $\mathbb Q$, write
\[
a_n=q_n\alpha^n,
\qquad q_n\in\mathbb Q^\times.
\]
The integral ring structure determines the nonzero integers $m_{ij}$ by
\[
a_i a_j=m_{ij}a_{i+j}.
\]
Equivalently,
\[
m_{ij}=\frac{q_iq_j}{q_{i+j}}.
\]
Thus the rational numbers $q_n$, up to the harmless rescaling $\alpha\mapsto c\alpha$, are determined by the integral ring $A$.

Now consider the coproduct
\[
\Delta:A\to A\otimes A
\]
induced by the H-space multiplication. In the lowest positive degree there are no decomposable terms, so rationally
\[
\Delta(\alpha)=\alpha\otimes1+1\otimes\alpha.
\]
Since $\Delta$ is an algebra homomorphism,
\[
\Delta(\alpha^n)=\sum_{i=0}^n\binom ni\alpha^i\otimes\alpha^{n-i}.
\]
Therefore
\[
\Delta(a_n)
=\sum_{i=0}^n
\binom ni\frac{q_n}{q_iq_{n-i}}
\,a_i\otimes a_{n-i}.
\]
Every coefficient is uniquely determined by the $q_i$, hence by the integral ring structure of $A$. Because $A\otimes A$ is torsionfree, equality after tensoring with $\mathbb Q$ already determines the integral coproduct. Thus the coproduct on $A$ is uniquely determined by the ring $A$.

The Pontryagin product on $H_*(X;\mathbb Z)$ is dual to this coproduct, since the homology and cohomology groups are degreewise finite free. Hence its structure constants are uniquely determined by the integral cohomology ring.

Finally, the rational coproduct above is cocommutative and coassociative. The two integral maps $\tau\Delta$ and $\Delta$, and likewise $(\Delta\otimes1)\Delta$ and $(1\otimes\Delta)\Delta$, become equal after tensoring with $\mathbb Q$. Their targets are torsionfree, so they were already equal integrally. Dualizing shows that the Pontryagin product is respectively commutative and associative.

Hence $H_*(X;\mathbb Z)$ is a commutative associative ring whose multiplication is uniquely determined by $H^*(X;\mathbb Z)$.
:::
