---
schema: qual/card@1
id: FD-D7HOH
kind: definition
title: Convergence in measure
prompts:
- What does it mean for $f_k$ to converge to $f$ in measure?
classification:
  areas:
  - real-analysis
  topics:
  - Convergence of Functions
  - Measure Theory
relations: []
review: draft
---

::: {.definition}
Let $m$ be Lebesgue measure on $\RR^n$, let $E\subseteq\RR^n$ be [[D-MDJII|Lebesgue measurable]], and let $f_k\colon E\to\RR$ for $k\geq 1$ and $f\colon E\to\RR$ be [[D-DHFN4|measurable]].
The sequence $(f_k)$ \dfn{converges in measure} to $f$ on $E$ if for every $\alpha>0$,
$$
\lim_{k \to \infty} m\qty{\theset{x \in E \suchthat \abs{f_{k}(x)-f(x)}>\alpha}}=0.
$$
:::
