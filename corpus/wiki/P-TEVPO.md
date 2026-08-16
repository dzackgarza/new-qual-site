---
schema: qual/card@1
id: P-TEVPO
kind: problem
title: "Parts Suppose $\\exists M_g \\suchthat \\forall x,~ g(x) < M$."
classification:
  areas:
  - prelim
  topics:
  - limits
  - counterexamples
relations: []
review: draft
---

::: problem
1. Parts
   1. Suppose $\exists M_g \suchthat \forall x,~ g(x) < M$. Then let $\varepsilon > 0$ be arbitrarily chosen; we want to show that there exists a $\delta$ such that $\abs{x} \leq \delta \implies \abs{f(x)g(x)} \leq \varepsilon$. Since $\lim_{x\to 0} f(x) = 0$, choose a $\delta_f$ such that $\abs{x} \leq \delta_f \implies \abs{f(x)} \leq \frac{\varepsilon}{M_g}$. So letting $\delta = \delta_f$, we have
$$
\abs{x} \leq \delta \implies \abs{f(x)g(x)}  = \abs{f(x)} \abs{g(x)} \leq {\frac{\varepsilon}{M_g}}\abs{g(x)} \leq \frac{\varepsilon}{M_g}M_g = \varepsilon. \qed 
$$ 
     1. Let $f(x) = x$ and $g(x) = \frac{1}{x}$. Note that $g(x)$ is unbounded in any neighborhood of 0, and $f(x)g(x) = 1 \not\to 0$.
:::
