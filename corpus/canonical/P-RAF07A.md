---
schema: qual/card@1
id: P-RAF07A
kind: problem
title: "True/false on convergence, operators, and compactness"
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
True or false. For each part, determine if it is always true or sometimes false. If true give a brief proof. If false give a counterexample or disprove it. No credit if reason is missing or incorrect.

(a) If $f : \mathbb{R} \to \mathbb{R}$ is continuous with $f \in L^1(\mathbb{R}, m)$, then $\lim_{x \to \infty} f(x) = 0$.

(b) If $f : \mathbb{R} \to \mathbb{R}$ is a continuously differentiable function with $f, f' \in L^1(\mathbb{R}, m)$, then $\lim_{x \to \infty} f(x) = 0$.

(c) If $\{f_n\}$ is a sequence of Lebesgue integrable functions on $[0,1]$ such that $f_n$ converges to $0$ in $L^1([0,1], m)$, then there exists a Lebesgue measurable set $E \subset [0,1]$ with $m(E) > 0$ such that $\lim_{n \to \infty} f_n(x) = 0$ for all $x \in E$.

(d) If $X$ and $Y$ are Banach spaces and $T : X \to Y$ is a linear mapping for which $f \circ T \in X^*$ for all $f \in Y^*$, then $T$ is bounded.

(e) If $\alpha > 0$ and $\{f_n\}$ a sequence of functions on $[0,1]$ for which
$$
|f_n(x) - f_n(y)| \leq |x - y|^\alpha \quad \text{and} \quad f_n(0) = 0 \;\forall n,\; \forall x, y \in [0,1],
$$
then there exists a subsequence $\{f_{n_j}\}$ that converges uniformly on $[0,1]$.
:::
