---
schema: qual/card@1
id: P-4XNZ6
kind: problem
title: Hardy-Littlewood maximal function bound via Vitali covering
classification:
  areas:
  - real-analysis
  topics:
  - Maximal Functions
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Problem 2 of the Spring 2016 JHU analysis qualifying exam in the preserved packet.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

Prove that the Hardy-Littlewood maximal function $f^*$ for an integrable function $f$ satisfies

$$m(\{x \in \mathbb{R}^d : f^*(x) > \alpha\}) \leq \frac{3^d}{\alpha} \|f\|_{L^1(\mathbb{R}^d)}$$

where $\alpha > 0$.
Recall that

$$f^*(x) = \sup_{x \in B} \frac{1}{m(B)} \int_B |f(y)| \, dy, \quad x \in \mathbb{R}^d$$

where the supremum is taken over all balls containing the point $x$.
You may assume the Vitali 3-times Covering Lemma.
State it clearly if you use it.

::: solution
<1>1. State the covering lemma and choose a witnessing ball at each superlevel point.
::: proof
We use the following Vitali $3$-times covering lemma: from any family of balls in $\mathbb R^d$ whose radii are uniformly bounded, one can choose a finite or countable pairwise disjoint subfamily $(B_j)$ such that
\[
\bigcup_{B\text{ in the original family}}B
\subseteq\bigcup_j 3B_j,
\]
where $3B_j$ is the concentric ball with three times the radius.

Fix $\alpha>0$ and set
\[
E_\alpha:=\{x\in\mathbb R^d:f^*(x)>\alpha\}.
\]
For each $x\in E_\alpha$, choose a ball $B_x\ni x$ such that
\[
\frac1{m(B_x)}\int_{B_x}|f(y)|\,dy>\alpha.
\]
Then
\[
\alpha m(B_x)<\int_{B_x}|f|\le\|f\|_1,
\]
so the radii of all the selected balls are uniformly bounded.
:::

<1>2. Apply the covering lemma.
::: proof
Choose a pairwise disjoint subfamily $(B_j)$ as in the $3$-times covering lemma. Since every $x\in E_\alpha$ lies in one of the original balls,
\[
E_\alpha\subseteq\bigcup_j3B_j.
\]
Therefore
\[
m(E_\alpha)
\le\sum_jm(3B_j)
=3^d\sum_jm(B_j).
\]
:::

<1>3. Use the large-average property and disjointness.
::: proof
For every selected ball,
\[
\alpha m(B_j)<\int_{B_j}|f|.
\]
Since the $B_j$ are pairwise disjoint,
\[
\alpha\sum_jm(B_j)
<\sum_j\int_{B_j}|f|
\le\|f\|_1.
\]
Hence
\[
\sum_jm(B_j)\le\frac{\|f\|_1}{\alpha}.
\]
Substituting into Step 2 gives
\[
\boxed{
m(\{x:f^*(x)>\alpha\})
\le\frac{3^d}{\alpha}\|f\|_{L^1(\mathbb R^d)}.}
\]
:::
:::
