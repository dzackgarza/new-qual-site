---
schema: qual/card@1
id: P-RAF10A
kind: problem
title: "True/false on Banach spaces, L^p spaces, and topologies"
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
For each of the following, determine if the statement is true (always) or false (not always true).
If true, give a brief proof, citing appropriate theorem(s); if false, give a counterexample or prove it is false in some other rigorous way.

(a) Any bounded sequence in a Banach space has a convergent subsequence.

(b) There exists a sequence of functions $f_n \in L^1([0,1])$ such that $f_n$ converges to $0$ in $L^1$, but there is no subsequence $f_{n_k}$ that converges pointwise to $0$ a.e.

(c) The space $C([0,1])$ is dense in $L^\infty([0,1])$.

(d) The sequence $e^{i2\pi n x}$ converges to $0$ weakly in $L^2([0,1])$.

(e) Let $a_j \in \mathbb{R}$, $j = 1, \ldots, n$, and $\frac{1}{p} + \frac{1}{q} = 1$, $1 < p < \infty$.
Then
$$
\sum_{j=1}^{n} a_j \leq n^{1/p} \left(\sum_{j=1}^{n} |a_j|^q\right)^{1/q}.
$$

(f) Let $Y = \{f : \mathbb{R} \to [-\pi, \pi]\}$.
Let $[-\pi, \pi]$ have its natural topology, and give $Y$ the weakest topology such that the mappings $p_r : Y \to [-\pi, \pi]$ defined by $p_r(f) := f(r)$ are continuous for all $r \in \mathbb{R}$.
Then $Y$ is compact.
:::
