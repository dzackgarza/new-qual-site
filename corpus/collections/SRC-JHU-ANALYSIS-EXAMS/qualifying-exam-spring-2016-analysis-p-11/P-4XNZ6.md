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

::: {.problem}
Prove that the Hardy-Littlewood maximal function $f^*$ for an integrable function $f$ satisfies

$$m(\{x \in \mathbb{R}^d : f^*(x) > \alpha\}) \leq \frac{3^d}{\alpha} \|f\|_{L^1(\mathbb{R}^d)}$$

where $\alpha > 0$.
Recall that

$$f^*(x) = \sup_{x \in B} \frac{1}{m(B)} \int_B |f(y)| \, dy, \quad x \in \mathbb{R}^d$$

where the supremum is taken over all balls containing the point $x$.
You may assume the Vitali 3-times Covering Lemma.
State it clearly if you use it.
:::

::: {.solution}
<1>1. State the covering lemma.
::: {.proof}
Vitali $3$-times covering lemma: every finite collection of
balls in $\mathbb R^d$ has a pairwise disjoint subcollection
$B_1,\dots,B_N$ such that the union of the whole collection
is contained in $\bigcup_{j=1}^N3B_j$, where $3B_j$ is the
concentric ball with three times the radius.
:::

<1>2. The superlevel set is open and is a union of balls with large averages.
::: {.proof}
Take the balls in the definition of $f^*$ to be open.
A closed ball containing $x$ lies in a slightly larger
concentric open ball, whose average of $|f|$ is arbitrarily
close, so this does not change $f^*$.

Fix $\alpha>0$ and set
\[
E_\alpha:=\{x\in\mathbb R^d:f^*(x)>\alpha\}.
\]
For each $x\in E_\alpha$, choose an open ball $B_x\ni x$ such that
\[
\frac1{m(B_x)}\int_{B_x}|f(y)|\,dy>\alpha.
\]
Every point of $B_x$ then lies in $E_\alpha$, so
$E_\alpha=\bigcup_{x\in E_\alpha}B_x$ is open, hence measurable.
:::

<1>3. Every compact subset of $E_\alpha$ satisfies the bound.
::: {.proof}
Let $K\subset E_\alpha$ be compact. Finitely many of the
balls $B_x$ cover $K$. Step <1>1 gives pairwise disjoint
balls $B_1,\dots,B_N$ among them with
\[
K\subseteq\bigcup_{j=1}^N3B_j.
\]
Each $B_j$ satisfies $\alpha m(B_j)<\int_{B_j}|f|$, and the
$B_j$ are pairwise disjoint. Therefore
\[
m(K)
\le\sum_{j=1}^N m(3B_j)
=3^d\sum_{j=1}^N m(B_j)
<\frac{3^d}{\alpha}\sum_{j=1}^N\int_{B_j}|f|
\le\frac{3^d}{\alpha}\|f\|_1.
\]
:::

<1>4. Inner regularity gives the bound for $E_\alpha$.
::: {.proof}
Lebesgue measure is inner regular on measurable sets, so
$m(E_\alpha)=\sup\{m(K):K\subset E_\alpha\text{ compact}\}$
[@Fol13]. Step <1>3 then gives
\[
\boxed{
m(\{x:f^*(x)>\alpha\})
\le\frac{3^d}{\alpha}\|f\|_{L^1(\mathbb R^d)}.}
\]
:::
:::
