---
schema: qual/card@1
id: P-RASP20B
kind: problem
title: "Three calculations: approximate identity at continuity point, Lebesgue-Stieltjes measure, oscillatory average"
classification:
  areas:
  - real-analysis
  topics:
  - Approximate Identity
  - Lebesgue-Stieltjes Measures
  - Riemann-Lebesgue Lemma
relations: []
review: draft
solved: false
---

::: problem
There are three sub-problems; all of them are calculation type.
Justify your calculations.

(1) Let $f \in L^\infty(\mathbb{R})$ and $g \in L^1(\mathbb{R})$.
Assume $f$ is continuous at $x = 1$ with $f(1) = \pi$, and $g \geq 0$ on $\mathbb{R}$ with $\|g\|_{L^1(\mathbb{R})} = 2$.
Calculate
$$
\lim_{k \to +\infty} \int_{[-k,k]} f\left(1 + \frac{x^2}{k}\right) g(x) \, dm(x).
$$

(2) Let $\mu$ be the Lebesgue–Stieltjes measure associated to the increasing right-continuous function
$$
F(x) = \begin{cases} 0 & \text{if } x < 0, \\ x + 2 & \text{if } 0 \leq x < 1, \\ 4x^2 & \text{if } 1 \leq x < \infty. \end{cases}
$$
Calculate $\mu((-\infty, 0])$, $\mu(\{1\})$, and $\mu([1, 2])$.

(3) Let $E$ be a Lebesgue-measurable subset of $[0, 1]$ with $m(E) = 1/2$.
Let $u_k \in \mathbb{R}$ ($k = 1, 2, \ldots$). Calculate
$$
\lim_{k \to \infty} \int_E \cos^2(k\pi x + u_k) \, dm(x).
$$
:::
