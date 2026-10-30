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

::: {.problem}
Let $K \subset G \subset \CC$ with $K$ compact and $G$ open.
Suppose that for any $f$ analytic in an open neighborhood of $K$ and any $\epsilon > 0$ there is $g \in H(G)$ so that $\abs{f(z) - g(z)} < \epsilon$ for all $z \in K$.
Let $z_0 \in G \setminus K$ be arbitrary.
Show that there exists $h \in H(G)$ such that $$\abs{h(z_0)} > \sup_{w \in K} \abs{h(w)}.$$
:::

::: {.solution}
Since $z_0\notin K$ and $K$ is compact, the function
$$
f(z)=\frac1{z-z_0}
$$
is holomorphic on an open neighborhood of $K$. Put
$$
M=\max_{w\in K}\abs{w-z_0}<\infty.
$$
Choose $\epsilon>0$ so small that $M\epsilon<1$, and use the assumed
approximation property to find $g\in H(G)$ satisfying
$$
\abs{g(w)-\frac1{w-z_0}}<\epsilon
\qquad(w\in K).
$$
Define
$$
h(z)=(z-z_0)g(z)-1.
$$
Then $h\in H(G)$ and
$$
h(z_0)=-1,
\qquad \abs{h(z_0)}=1.
$$
For $w\in K$,
$$
\abs{h(w)}
=\abs{w-z_0}\abs{g(w)-\frac1{w-z_0}}
\le M\epsilon<1.
$$
Therefore
$$
\abs{h(z_0)}=1>\sup_{w\in K}\abs{h(w)},
$$
as required.
:::
