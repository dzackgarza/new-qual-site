---
schema: qual/card@1
id: P-AMD-WEXTRZWM
kind: problem
title: "Let $\\mathcal B$ denote the set of all Borel subsets of $\\RR$ and $\\mu : \\mathcal B \\to [0, \\infty)$ denote a\u2026"
classification:
  areas:
  - real-analysis
  topics:
  - continuity-of-measure
  - measure-theory
  - absolute-continuity
relations: []
review: draft
---

::: {.problem}
Let $\mathcal B$ denote the set of all Borel subsets of $\RR$ and $\mu : \mathcal B \to [0, \infty)$ denote a finite Borel measure on $\RR$.
  
  a. Prove that if $\{F_k\}$ is a sequence of Borel sets for which $F_k \supseteq  F_{k+1}$ for all $k$, then
  $$
  \lim _{k \rightarrow \infty} \mu\left(F_{k}\right)=\mu\left(\bigcap_{k=1}^{\infty} F_{k}\right)
  $$
  b. Suppose $\mu$ has the property that $\mu(E) = 0$ for every $E \in \mathcal B$ with Lebesgue measure $m(E) = 0$.
    Prove that for every $\eps > 0$ there exists $\delta > 0$ so that if $E \in \mathcal B$ with $m(E) < \delta$, then $\mu(E) < \eps$.
:::
