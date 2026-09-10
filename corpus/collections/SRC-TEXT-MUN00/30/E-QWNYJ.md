---
schema: qual/card@1
id: E-QWNYJ
kind: problem
title: Countable products of separable spaces are separable
classification:
  areas:
  - topology
  topics:
  - Countability
  - Product Topology
relations: []
review: draft
---

::: {.exercise}

Show that if $X$ is a countable product of spaces having countable dense subsets, then $X$ has a countable dense subset.
:::

::: {.solution}
Let
\[
X=\prod_{n=1}^\infty X_n,
\]
and for each \(n\) choose a countable dense set \(D_n\subset X_n\). Choose a basepoint \(a_n\in D_n\). Let \(D\subset X\) consist of all sequences \(x=(x_n)\) such that \(x_n\in D_n\) for every \(n\) and \(x_n=a_n\) for all but finitely many \(n\).

The set \(D\) is countable: it is a countable union, over finite subsets \(F\subset\mathbb Z_+\), of the countable products \(\prod_{n\in F}D_n\).

It is dense. A basic nonempty open set in the product topology restricts only finitely many coordinates, say \(n\in F\), with \(x_n\in U_n\). Since \(D_n\) is dense, choose \(d_n\in D_n\cap U_n\) for \(n\in F\), and set all other coordinates equal to \(a_n\). The resulting point lies in \(D\) and in the basic open set. Hence \(D\) is countable dense.
:::
