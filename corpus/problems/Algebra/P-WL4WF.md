---
schema: qual/card@1
id: P-WL4WF
kind: problem
title: The cyclotomic extension $\QQ(\zeta_{43})/\QQ$ has Galois group $\ZZ_{42}$
classification:
  areas:
  - algebra
  topics:
  - Roots of Unity
  - Galois Theory
  - Cyclic Groups
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
Prove that the cyclotomic extension $\QQ(\zeta_{43})/\QQ$ has degree 42 and that its Galois group is cyclic of order 42:
$$\Gal(\QQ(\zeta_{43})/\QQ) \cong (\ZZ/43\ZZ)^\times \cong \ZZ/42\ZZ.$$
:::

::: {.solution}
For the prime $43$,
$$
\Phi_{43}(x)=1+x+\cdots+x^{42}.
$$
The shifted polynomial $\Phi_{43}(x+1)$ is Eisenstein at $43$, so $\Phi_{43}$ is irreducible over $\QQ$. Hence
$$
[\QQ(\zeta_{43}):\QQ]=\deg\Phi_{43}=42.
$$

The field $\QQ(\zeta_{43})$ is the splitting field of $\Phi_{43}$, hence is Galois. Every automorphism is determined by
$$
\zeta_{43}\longmapsto \zeta_{43}^a,
\qquad a\in(\ZZ/43\ZZ)^\times,
$$
and every such $a$ occurs. Therefore
$$
\Gal(\QQ(\zeta_{43})/\QQ)
\cong(\ZZ/43\ZZ)^\times.
$$
Since the multiplicative group of a finite field is cyclic,
$$
(\ZZ/43\ZZ)^\times\cong C_{42}.
$$
Thus the extension has degree $42$ and cyclic Galois group of order $42$.
:::
