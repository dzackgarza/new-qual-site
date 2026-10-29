---
schema: qual/card@1
id: P-TOPS04E
kind: problem
title: "No nonzero mod 2 degree map between the Klein bottle and the torus"
classification:
  areas:
  - topology
  topics:
  - Degree
  - Surfaces
  - Mod 2
relations: []
review: draft
---

::: {.problem}
Using the fundamental class in $\ZZ/2$-homology, there is an obvious definition of the mod $2$-degree for a continuous map between closed manifolds (not necessarily oriented).
Show that there is no map of nonzero mod $2$-degree between the Klein bottle and the torus, in either direction.
:::

::: {.solution}

::: pf

::: pf-step

For a closed connected surface $S$, the mod-$2$ intersection pairing
$$
H^1(S;\FF_2)\times H^1(S;\FF_2)\to\FF_2,
\qquad (x,y)\mapsto\langle x\smile y,[S]_2\rangle
$$
is nondegenerate.

::: pf-proof

This is Poincaré duality over $\FF_2$, which does not require orientability.

:::

:::

::: {.pf-step #s2}

If $f:M\to N$ has mod-$2$ degree $1$, then $f^*:H^1(N;\FF_2)\to H^1(M;\FF_2)$ preserves the intersection pairing and is injective.

::: pf-proof

For $x,y\in H^1(N;\FF_2)$,
$$
\langle f^*x\smile f^*y,[M]_2\rangle
=\langle x\smile y,f_*[M]_2\rangle
=\langle x\smile y,[N]_2\rangle.
$$
Nondegeneracy then implies injectivity.

:::

:::

::: {.pf-step #s3}

Since both the torus $T$ and Klein bottle $K$ have $\dim_{\FF_2}H^1=2$, such an $f$ would induce an isometry between their mod-$2$ intersection forms.

::: pf-proof

An injective linear map between two $2$-dimensional vector spaces is an isomorphism, and step [](#s2){.pf-ref} shows it preserves the pairing.

:::

:::

::: {.pf-step #s4}

The mod-$2$ intersection form of $T$ is alternating: $x\smile x=0$ for every $x\in H^1(T;\FF_2)$.

::: pf-proof

With the usual basis $a,b$, one has $a^2=b^2=0$ and $ab=ba$ over $\FF_2$. Hence $(ra+sb)^2=0$ for all $r,s\in\FF_2$.

:::

:::

::: {.pf-step #s5}

The mod-$2$ intersection form of $K$ is not alternating: there is $x\in H^1(K;\FF_2)$ with $x^2\ne0$.

::: pf-proof

A one-sided simple closed curve in the Klein bottle has mod-$2$ self-intersection $1$. Its Poincaré dual $x$ therefore satisfies
$$
\langle x^2,[K]_2\rangle=1.
$$

:::

:::

::: pf-step

Hence no mod-$2$ degree-one map exists in either direction between $K$ and $T$.

::: pf-proof

Such a map would give an isometry by step [](#s3){.pf-ref}, impossible because alternation of a bilinear form is preserved by isometry and steps [](#s4){.pf-ref} and [](#s5){.pf-ref} distinguish the two forms.

:::

:::

:::

:::
