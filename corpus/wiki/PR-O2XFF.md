---
schema: qual/card@1
id: PR-O2XFF
kind: proposition
title: "The Weierstrass $M\\dash$Test"
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
---
:::{.proposition title="The Weierstrass $M\dash$Test"}
If $\sup_{x\in A} \abs{f_n(x)} \leq M_n$ for each $n$ where $\sum M_n < \infty$, then $\sum_{n=1}^\infty f_n(x)$ converges uniformly and absolutely on $A$.
[^m_test_suffices]
Conversely, if $\sum f_n$ converges uniformly on $A$ then $\sup_{x\in A} \abs{f_n(x)} \to 0$. 
It suffices to show $\abs{f_n(x)} \leq M_n$ for some $M_n$ not depending on $x$.

:::

[^m_test_suffices]:
