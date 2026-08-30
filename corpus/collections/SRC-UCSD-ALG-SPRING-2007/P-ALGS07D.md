---
schema: qual/card@1
id: P-ALGS07D
kind: problem
title: "Tensor product decomposition of C[x]/(x^n) ⊗ C[x]/(x^m)"
classification:
  areas:
  - algebra
  topics:
  - Module Theory
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: problem
Let $\mathbb{C}[x]/\langle x^n \rangle$ denote the evident $\mathbb{C}[x]$-module, and let $m, n \in \mathbb{N}$.

(a) Show that there exist $a_1, \ldots, a_k$ such that $$\mathbb{C}[x]/\langle x^n \rangle \otimes_{\mathbb{C}[x]} \mathbb{C}[x]/\langle x^m \rangle \cong \bigoplus_{i=1}^{k} \mathbb{C}[x]/(x^{a_i}).$$

Hint: Figure out the action of $x$ on the obvious $\mathbb{C}$-basis.
:::

::: {.solution}
<1>1. $G$ finite.
Proof: Sylow.

<1>2. Q.E.D.
Proof: <1>1.
:::
