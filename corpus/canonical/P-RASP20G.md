---
schema: qual/card@1
id: P-RASP20G
kind: problem
title: "Weakly closed convex sets and nested bounded closed convex sets intersect"
classification:
  areas:
  - real-analysis
  topics:
  - Hilbert Spaces
  - Convexity
  - Weak Topology
  - Projection Theorem
relations: []
review: draft
solved: false
---

::: problem
Let $H$ be a real Hilbert space.
Recall: if $K$ is a nonempty, closed, convex subset of $H$ and $x \in H \setminus K$, then there exists a unique $y \in K$ such that $\|x - y\| = \min_{z \in K} \|x - z\|$; moreover $\langle x - y, z - y \rangle \leq 0$ for all $z \in K$.

(1) Let $K$ be a nonempty, closed, convex subset of $H$.
Prove that $K$ is weakly sequentially closed, i.e., if $u_n \in K$ ($n = 1, 2, \ldots$) and $u \in H$ satisfy $u_n \to u$ weakly, then $u \in K$.

(2) Let $K_n$ ($n = 1, 2, \ldots$) be a sequence of nonempty, bounded, closed, convex subsets of $H$ such that $K_{n+1} \subseteq K_n$ ($n = 1, 2, \ldots$). Prove that $\bigcap_{k=n}^\infty K_k \neq \emptyset$.
:::
