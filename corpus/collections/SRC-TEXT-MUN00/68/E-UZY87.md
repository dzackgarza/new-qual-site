---
schema: qual/card@1
id: E-UZY87
kind: problem
title: Conjugacy classes of finite order in a free product
classification:
  areas:
  - topology
  topics:
  - Free Products
relations: []
review: draft
---

::: {.exercise}

Let$G = G_1 * G_2$.
Given$c \in G$, let$cG_1c^{-1}$denote the set of all elements of the form$cxc^{-1}$, for$x \in G_1$.
It is a subgroup of$G$; show that its intersection with$G_2$consists of the identity alone.
:::

::: {.solution}
Let \(y\in cG_1c^{-1}\cap G_2\). We prove \(y=1\).
Write
\[
y=cxc^{-1}
\]
with \(x\in G_1\). If \(x=1\), then \(y=1\), so assume \(x\ne1\).

Choose a reduced word for \(c\). Cancel from its right end, if necessary, against \(x\), and rewrite the conjugate in cyclically reduced form. Concretely, there is a reduced word \(d\) and a nonidentity element \(x'\in G_1\) such that
\[
cxc^{-1}=d x' d^{-1},
\]
and either \(d\) is empty or the last letter of \(d\) lies in \(G_2\). In the latter case the displayed word is reduced: the last letter of \(d\) lies in \(G_2\), then \(x'\in G_1\setminus\{1\}\), then the first letter of \(d^{-1}\) lies in \(G_2\). Thus its reduced length is at least \(3\), so it cannot represent an element of the factor \(G_2\), whose nonidentity elements have reduced length \(1\).

If \(d\) is empty, then \(y=x'\in G_1\cap G_2\). By the reduced-word normal form for a free product, the two factors intersect only in the identity. Hence again \(y=1\).

Therefore
\[
cG_1c^{-1}\cap G_2=\{1\}.
\]
:::
