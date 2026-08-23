---
schema: qual/card@1
id: P-RASP08B
kind: problem
title: "Convergence of level sets under monotone a.e. convergence"
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
Let $(X, \mu)$ be a measure space and $f, f_n : X \to \mathbb{R}$ measurable functions such that $f_1 \leq f_2 \leq \cdots \leq f_n \leq \cdots$ a.e. and $\lim_{n \to \infty} f_n = f$ a.e.

(a) For every $a \in \mathbb{R}$, show that $\lim_{n \to \infty} \mu(\{x : f_n(x) > a\})$ exists and
$$
\lim_{n \to \infty} \mu(\{x : f_n(x) > a\}) = \mu(\{x : f(x) > a\}).
$$

(b) Assume that $\mu(X) < \infty$.
Show that $\lim_{n \to \infty} \mu(\{x : f_n(x) < a\})$ exists for every $a \in \mathbb{R}$ and
$$
\mu(\{x : f(x) < a\}) \leq \lim_{n \to \infty} \mu(\{x : f_n(x) < a\}) \leq \mu(\{x : f(x) < a\}) + \mu(\{x : f(x) = a\}).
$$
Give an example where
$$
\mu(\{x : f(x) < a\}) < \lim_{n \to \infty} \mu(\{x : f_n(x) < a\})
$$
for some $a \in \mathbb{R}$.
:::
