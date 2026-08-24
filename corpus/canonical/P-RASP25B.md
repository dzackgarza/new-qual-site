---
schema: qual/card@1
id: P-RASP25B
kind: problem
title: "Atomless probability measure is inner regular on diameter"
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
Let $\mathcal{B}_{\mathbb{R}^n}$ be the Borel $\sigma$-algebra on $\mathbb{R}^n$ and let $\mu : \mathcal{B}_{\mathbb{R}^n} \to [0, \infty]$ be a measure such that

(1) $\mu(\mathbb{R}^n) = 1$,

(2) $\mu(\{x\}) = 0$ for every $x \in \mathbb{R}^n$.

Prove that for every $\epsilon > 0$ there is $\delta > 0$ such that
$$
\operatorname{diam}(E) = \sup\{|x - y| : x, y \in E\} < \delta \implies \mu(E) < \epsilon.
$$

Hint: Start with $E \subset \overline{B_K(0)}$.
:::
