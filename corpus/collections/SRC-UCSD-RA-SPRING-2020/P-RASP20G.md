---
schema: qual/card@1
id: P-RASP20G
kind: problem
title: "Weakly sequentially closed convex sets and intersection properties"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: problem
Let $H$ be a real Hilbert space.
Recall: If $K$ is a nonempty, closed, and convex subset of $H$, and $x \in H \setminus K$, then there exists a unique $y \in K$ such that $\|x - y\| = \min_{z \in K} \|x - z\|$.
Moreover, $\langle x - y, z - y \rangle \leq 0$ for all $z \in K$.

(1) Let $K$ be a nonempty, closed, and convex subset of $H$.
Prove that $K$ is weakly sequentially closed, i.e., if $u_n \in K$ ($n = 1, 2, \ldots$) and $u \in H$ satisfy that $u_n \to u$ weakly, then $u \in K$.

(2) Let $K_n$ ($n = 1, 2, \ldots$) be a decreasing sequence of nonempty, closed, and convex subsets of $H$ (i.e., $K_{n+1} \subseteq K_n$ for all $n$). Prove that $\bigcap_{n=1}^{\infty} K_n \neq \emptyset$.
:::

::: {.solution}
<1>1. $f$ measurable.
Proof: check.

<1>2. Q.E.D.
Proof: <1>1.
:::
