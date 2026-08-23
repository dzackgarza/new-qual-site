---
schema: qual/card@1
id: P-RASP06D
kind: problem
title: "Convergence of integrals via dominated convergence with variable dominator"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
solved: false
---

::: problem
Let $\{f_j\}$ be a sequence of real-valued functions in $L^1(X, \mu)$ such that $f_j \to f$ a.e. with $f \in L^1(X, \mu)$.
Suppose $\{g_j\}$ is a sequence of functions in $L^1(X, \mu)$ such that $|f_j| \leq g_j$, $g_j \to g$ a.e. for some $g \in L^1(X, \mu)$, and also $g_j \to g$ in $L^1$.
Prove that
$$
\int_X f\,d\mu = \lim_{j \to \infty} \int_X f_j\,d\mu.
$$
:::
