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
Using the fundamental class in $\mathbb{Z}/2$-homology, there is an obvious definition of the mod $2$-degree for a continuous map between closed manifolds (not necessarily oriented).
Show that there is no map of nonzero mod $2$-degree between the Klein bottle and the torus, in either direction.
:::

::: {.solution}
<1>1. For a closed connected surface $S$, the mod-$2$ intersection pairing
$$
H^1(S;\mathbb F_2)\times H^1(S;\mathbb F_2)\to\mathbb F_2,
\qquad (x,y)\mapsto\langle x\smile y,[S]_2\rangle
$$
is nondegenerate.
::: {.proof}
This is Poincaré duality over $\mathbb F_2$, which does not require orientability.
:::

<1>2. If $f:M\to N$ has mod-$2$ degree $1$, then $f^*:H^1(N;\mathbb F_2)\to H^1(M;\mathbb F_2)$ preserves the intersection pairing and is injective.
::: {.proof}
For $x,y\in H^1(N;\mathbb F_2)$,
$$
\langle f^*x\smile f^*y,[M]_2\rangle
=\langle x\smile y,f_*[M]_2\rangle
=\langle x\smile y,[N]_2\rangle.
$$
Nondegeneracy then implies injectivity.
:::

<1>3. Since both the torus $T$ and Klein bottle $K$ have $\dim_{\mathbb F_2}H^1=2$, such an $f$ would induce an isometry between their mod-$2$ intersection forms.
::: {.proof}
An injective linear map between two $2$-dimensional vector spaces is an isomorphism, and <1>2 shows it preserves the pairing.
:::

<1>4. The mod-$2$ intersection form of $T$ is alternating: $x\smile x=0$ for every $x\in H^1(T;\mathbb F_2)$.
::: {.proof}
With the usual basis $a,b$, one has $a^2=b^2=0$ and $ab=ba$ over $\mathbb F_2$. Hence $(ra+sb)^2=0$ for all $r,s\in\mathbb F_2$.
:::

<1>5. The mod-$2$ intersection form of $K$ is not alternating: there is $x\in H^1(K;\mathbb F_2)$ with $x^2\ne0$.
::: {.proof}
A one-sided simple closed curve in the Klein bottle has mod-$2$ self-intersection $1$. Its Poincaré dual $x$ therefore satisfies
$$
\langle x^2,[K]_2\rangle=1.
$$
:::

<1>6. Hence no mod-$2$ degree-one map exists in either direction between $K$ and $T$.
::: {.proof}
Such a map would give an isometry by <1>3, impossible because alternation of a bilinear form is preserved by isometry and <1>4--<1>5 distinguish the two forms.
:::
:::
