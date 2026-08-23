---
schema: qual/card@1
id: P-RAF09F
kind: problem
title: "Maximal function bound for approximate identity supremum"
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
Suppose that on $\mathbb{R}^n$, $\phi(x) \leq C(1 + \|x\|)^{-n-\epsilon}$ for some positive $C$ and $\epsilon > 0$.
Also assume that $\phi(x)$ is measurable.
If $f \in L^p(\mathbb{R}^n)$ with $1 \leq p \leq \infty$, define
$$
\mathcal{U}_\phi(f)(x) := \sup_{t > 0} \{f * \phi_t(x)\}
$$
where $f * \phi_t(x) = \int f(x-y)\phi_t(y)\,dy$, $\phi_t(y) = \frac{1}{t^n}\phi\!\left(\frac{y}{t}\right)$.

Show that there exists $C'$ independent of $f$ such that $\|\mathcal{U}_\phi(f)\|_p \leq C' \|f\|_p$ where $H(f)$ is the Hardy-Littlewood maximal function defined as
$$
H(f)(x) := \sup_{r > 0} \frac{1}{m(B(x,r))} \int_{B(x,r)} |f(y)|\,dy.
$$
:::
