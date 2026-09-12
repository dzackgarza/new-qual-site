---
schema: qual/card@1
id: P-CAF05D
kind: problem
title: "Using Runge-type approximation to separate values outside a compact set"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: problem
Let $K \subset G \subset \mathbb{C}$ with $K$ compact and $G$ open.
Suppose that for any $f$ analytic in an open neighborhood of $K$ and any $\epsilon > 0$ there is $g \in H(G)$ so that $|f(z) - g(z)| < \epsilon$ for all $z \in K$.
Let $z_0 \in G \setminus K$ be arbitrary.
Show that there exists $h \in H(G)$ such that $$|h(z_0)| > \sup_{w \in K} |h(w)|.$$
:::

::: solution
Since $z_0\notin K$ and $K$ is compact, the function
\[
f(z)=\frac1{z-z_0}
\]
is holomorphic on an open neighborhood of $K$. Put
\[
M=\max_{w\in K}|w-z_0|<\infty.
\]
Choose $\epsilon>0$ so small that $M\epsilon<1$, and use the assumed
approximation property to find $g\in H(G)$ satisfying
\[
\left|g(w)-\frac1{w-z_0}\right|<\epsilon
\qquad(w\in K).
\]
Define
\[
h(z)=(z-z_0)g(z)-1.
\]
Then $h\in H(G)$ and
\[
h(z_0)=-1,
\qquad |h(z_0)|=1.
\]
For $w\in K$,
\[
|h(w)|
=|w-z_0|\left|g(w)-\frac1{w-z_0}\right|
\le M\epsilon<1.
\]
Therefore
\[
|h(z_0)|=1>\sup_{w\in K}|h(w)|,
\]
as required.
:::
