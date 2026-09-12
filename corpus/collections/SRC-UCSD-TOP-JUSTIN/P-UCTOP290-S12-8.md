---
schema: qual/card@1
id: P-UCTOP290-S12-8
kind: problem
title: "No retraction from CP^n onto CP^k for k < n, and the mod-2 analogue for RP^n"
classification:
  areas:
  - topology
  topics:
  - Cohomology Ring
  - Retractions
relations: []
review: draft
---

::: problem
Assume the fact that $H^*(\mathbb{C}P^n;\mathbb{Z}) = \mathbb{Z}[\alpha]/(\alpha^{n+1})$, where $\alpha$ has degree $2$, and $H^*(\mathbb{R}P^n;\mathbb{Z}_2) = \mathbb{Z}_2[\beta]/(\beta^{n+1})$, where $\beta$ has degree $1$.
(These are "truncated polynomial rings".) Show that if $k < n$ there is no retraction from $\mathbb{C}P^n$ to its standard submanifold $\mathbb{C}P^k$, and similarly for $\mathbb{R}P^n$.
:::

::: {.solution}
<1>1. Let
$$
i:\mathbb CP^k\hookrightarrow\mathbb CP^n
$$
be the standard inclusion and suppose a retraction $r:\mathbb CP^n\to\mathbb CP^k$ existed. Then
$$
i^*\circ r^*=\operatorname{id}_{H^*(\mathbb CP^k;\mathbb Z)}.
$$
::: {.proof}
A retraction satisfies $r\circ i=\operatorname{id}_{\mathbb CP^k}$. Cohomology is contravariant, so $(r\circ i)^*=i^*r^*$.
:::

<1>2. If $\alpha_k\in H^2(\mathbb CP^k)$ and $\alpha_n\in H^2(\mathbb CP^n)$ are the standard generators, then
$$
r^*(\alpha_k)=\alpha_n.
$$
::: {.proof}
The standard inclusion satisfies $i^*(\alpha_n)=\alpha_k$. Since $H^2(\mathbb CP^n)\cong\mathbb Z$, write $r^*(\alpha_k)=m\alpha_n$. Applying $i^*$ and using <1>1 gives $m\alpha_k=\alpha_k$, hence $m=1$.
:::

<1>3. This is impossible when $k<n$.
::: {.proof}
In $H^*(\mathbb CP^k)$ one has $\alpha_k^{k+1}=0$. Therefore
$$
0=r^*(\alpha_k^{k+1})=r^*(\alpha_k)^{k+1}=\alpha_n^{k+1}.
$$
But $k+1\le n$, so $\alpha_n^{k+1}\ne0$ in
$$
H^*(\mathbb CP^n;\mathbb Z)=\mathbb Z[\alpha_n]/(\alpha_n^{n+1}),
$$
a contradiction.
:::

<1>4. The identical argument over $\mathbb F_2$ rules out a retraction
$$
\mathbb RP^n\to\mathbb RP^k
$$
for $k<n$.
::: {.proof}
Let $\beta_k,\beta_n$ be the degree-one generators. A retraction would force $r^*(\beta_k)=\beta_n$, but then
$$
0=r^*(\beta_k^{k+1})=\beta_n^{k+1}\ne0
$$
because $k+1\le n$. Thus no such retraction exists.
:::
:::
