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

Show that the rationals $\QQ$ are not locally compact.
:::

::: {.solution}
Suppose \(\QQ\) were locally compact at \(q\). Then some neighborhood \(V\) of \(q\) in \(\QQ\) would have compact closure in \(\QQ\). Choose real numbers \(a<b\) with
\[
q\in(a,b)\cap\QQ\subset V.
\]
Pick an irrational \(r\in(a,b)\). Choose a sequence of rationals \(q_n\in(a,b)\) converging in \(\RR\) to \(r\). The sequence lies in \(\overline V^{\QQ}\). If that closure were compact, some subsequence would converge in \(\QQ\) to a point \(s\in\QQ\). But convergence in the subspace \(\QQ\subset\RR\) implies convergence in \(\RR\), and uniqueness of real limits gives \(s=r\), contradiction. Hence \(\QQ\) is not locally compact.
:::
