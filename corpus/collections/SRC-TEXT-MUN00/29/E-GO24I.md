---
schema: qual/card@1
id: E-GO24I
kind: problem
title: The rationals are not locally compact
classification:
  areas:
  - topology
  topics:
  - Compactness
relations: []
review: draft
---

::: {.exercise}

Show that the rationals $\mathbb{Q}$ are not locally compact.
:::

::: {.solution}
Suppose \(\mathbb Q\) were locally compact at \(q\). Then some neighborhood \(V\) of \(q\) in \(\mathbb Q\) would have compact closure in \(\mathbb Q\). Choose real numbers \(a<b\) with
\[
q\in(a,b)\cap\mathbb Q\subset V.
\]
Pick an irrational \(r\in(a,b)\). Choose a sequence of rationals \(q_n\in(a,b)\) converging in \(\mathbb R\) to \(r\). The sequence lies in \(\overline V^{\mathbb Q}\). If that closure were compact, some subsequence would converge in \(\mathbb Q\) to a point \(s\in\mathbb Q\). But convergence in the subspace \(\mathbb Q\subset\mathbb R\) implies convergence in \(\mathbb R\), and uniqueness of real limits gives \(s=r\), contradiction. Hence \(\mathbb Q\) is not locally compact.
:::
