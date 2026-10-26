---
schema: qual/card@1
id: P-MAXAT-1-12
kind: problem
title: Maxim algebraic topology 1.12
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against section 1, problem 12 of the retained Laurentiu Maxim Problems in Algebraic Topology PDF.
---

::: {.problem}
Show that $\mathbb { R } \mathbb { P } ^ { 2 n }$ cannot be embedded in $S ^ { 2 n + 1 }$
:::

Assume $n\geq1$ and suppose, for contradiction, that there is an embedding
\[
\mathbb{RP}^{2n}\hookrightarrow S^{2n+1}.
\]
Its image is a closed codimension-one submanifold.

::: pf

::: pf-step

Every closed embedded hypersurface in an orientable manifold is orientable if it is two-sided.


::: pf-proof

Let $M^m\subset N^{m+1}$ be a two-sided embedded hypersurface and choose a nowhere-zero normal vector field $\nu$. An orientation of $N$ determines an orientation of $M$ by declaring a basis $(v_1,\ldots,v_m)$ positive precisely when $(\nu,v_1,\ldots,v_m)$ is a positive basis of $TN$. Thus $M$ is orientable.

:::

:::

::: pf-step

The embedded copy of $\mathbb{RP}^{2n}$ in $S^{2n+1}$ is two-sided.


::: pf-proof

Alexander duality with $\mathbb Z/2$ coefficients gives
\[
\widetilde H_0(S^{2n+1}\setminus\mathbb{RP}^{2n};\mathbb Z/2)
\cong
\widetilde H^{2n}(\mathbb{RP}^{2n};\mathbb Z/2).
\]
The top mod-$2$ cohomology of the closed connected $2n$-manifold $\mathbb{RP}^{2n}$ is $\mathbb Z/2$, so the complement has exactly two connected components. A closed embedded hypersurface whose complement has two sides has trivial normal line bundle: choose the normal direction pointing into one fixed complementary component. Hence the embedding is two-sided.

:::

:::

::: pf-step

Therefore the assumed embedding would make $\mathbb{RP}^{2n}$ orientable.


::: pf-proof

The sphere $S^{2n+1}$ is orientable. Apply step <1>1 to the two-sided hypersurface from step <1>2.

:::

:::

::: pf-step

But $\mathbb{RP}^{2n}$ is nonorientable.


::: pf-proof

The antipodal map
\[
a:S^{2n}\to S^{2n},
\qquad a(x)=-x,
\]
is the deck transformation of the double covering $S^{2n}\to\mathbb{RP}^{2n}$. Its degree is
\[
\deg(a)=(-1)^{2n+1}=-1,
\]
so it reverses orientation. If the quotient were orientable, its orientation would pull back to an orientation of $S^{2n}$ preserved by every deck transformation, contradicting the fact that $a$ reverses orientation.

:::

:::

::: pf-step

This contradiction proves that
\[
\boxed{\mathbb{RP}^{2n}\text{ does not embed in }S^{2n+1}.}
\]


::: pf-proof

Step <1>3 says the hypothetical embedding forces orientability, while step <1>4 proves nonorientability.

:::

:::

::: pf-qed

Step <1>5 is the required nonembedding statement.

:::

:::
