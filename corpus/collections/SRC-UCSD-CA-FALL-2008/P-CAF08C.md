---
schema: qual/card@1
id: P-CAF08C
kind: problem
title: "Pointwise limit of analytic functions with uniformly bounded derivatives is analytic"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: problem
Let $G \subset \mathbb{C}$ be open and connected, and let $h \in H(G)$.
Suppose that $\{f_n(z)\} \subset H(G)$ is a sequence of analytic functions for which $\lim_{n \to \infty} f_n(z)$ exists (and is finite) for every $z \in G$.
Put $f(z) := \lim_{n \to \infty} f_n(z)$.
Suppose that $|f_n'(z)| \leq |h(z)|$ for all $z \in G$.
Prove that $f \in H(G)$.
:::

::: solution
Fix $z_0\in G$. Choose $r>0$ with
\[
\overline{B(z_0,r)}\subset G.
\]
Since $h$ is continuous, there is an $M<\infty$ such that
\[
|h(z)|\le M
\qquad(z\in\overline{B(z_0,r)}).
\]
Thus
\[
|f_n'(z)|\le M
\]
throughout this disk. Because line segments in the disk stay in the disk,
\[
|f_n(z)-f_n(w)|\le M|z-w|
\qquad(z,w\in\overline{B(z_0,r)}).
\]
So the family $(f_n)$ is equicontinuous there.

Moreover $(f_n(z_0))$ converges, hence is bounded. Therefore
\[
|f_n(z)|
\le |f_n(z_0)|+Mr
\]
shows that $(f_n)$ is uniformly bounded on the closed disk. By Montel's
theorem, every subsequence has a further subsequence converging uniformly on
compact subsets of $B(z_0,r)$ to a holomorphic function.

But the original sequence converges pointwise to $f$. Hence every such
subsequential holomorphic limit must equal $f$ pointwise. It follows that $f$
is holomorphic on $B(z_0,r)$. Since $z_0$ was arbitrary, $f\in H(G)$.
:::
