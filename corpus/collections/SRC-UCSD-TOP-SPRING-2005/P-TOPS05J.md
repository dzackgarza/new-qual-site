---
schema: qual/card@1
id: P-TOPS05J
kind: problem
title: "Split short exact sequence for homology of a product relative to its wedge"
classification:
  areas:
  - topology
  topics:
  - Cohomology
  - Exact Sequences
  - Wedge Product
relations: []
review: draft
---

::: {.problem}
Let $X \vee Y$ be the one point union of $X$ and $Y$.
Prove for each $\ell > 0$ there is a split short exact sequence
$$
0 \to H_\ell(X \vee Y) \to H_\ell(X \times Y) \to H_\ell(X \times Y, X \vee Y) \to 0.
$$
:::

::: {.solution}
<1>1. For $\ell>0$,
$$
H_\ell(X\vee Y)\cong H_\ell(X)\oplus H_\ell(Y).
$$
::: {.proof}
Reduced homology takes wedges to direct sums, and in positive degrees reduced and unreduced homology agree.
:::

<1>2. Let $i:X\vee Y\hookrightarrow X\times Y$ be the standard inclusion. The map
$$
r=(p_X{}_*,p_Y{}_*):H_\ell(X\times Y)\to H_\ell(X)\oplus H_\ell(Y)
$$
is a left inverse to $i_*$.
::: {.proof}
On the $X$ wedge summand, $p_X$ is the identity and $p_Y$ is constant; on the $Y$ summand the roles reverse. Constant maps induce zero on positive-dimensional homology. Thus under <1>1,
$$
r\circ i_*=\operatorname{id}.
$$
:::

<1>3. Hence $i_*$ is injective and its image is a direct summand of $H_\ell(X\times Y)$.
::: {.proof}
A homomorphism admitting a left inverse is a split injection.
:::

<1>4. In the long exact sequence of the pair $(X\times Y,X\vee Y)$, the connecting homomorphism
$$
H_\ell(X\times Y,X\vee Y)\to H_{\ell-1}(X\vee Y)
$$
vanishes.
::: {.proof}
Since $i_*:H_{\ell-1}(X\vee Y)\to H_{\ell-1}(X\times Y)$ is injective by the same argument when $\ell-1>0$, exactness forces the connecting map to vanish. For $\ell=1$, the connecting map lands in $H_0(X\vee Y)$; for path-connected based spaces the inclusion induces an isomorphism on $H_0$, so it vanishes as well.
:::

<1>5. Therefore
$$
0\to H_\ell(X\vee Y)\xrightarrow{i_*}H_\ell(X\times Y)
\to H_\ell(X\times Y,X\vee Y)\to0
$$
is exact and split.
::: {.proof}
Exactness follows from the pair sequence and <1>4. Splitting follows from <1>3: write
$$
H_\ell(X\times Y)=\operatorname{im}i_*\oplus\ker r;
$$
then the quotient by $\operatorname{im}i_*$ is naturally isomorphic to $\ker r$, providing a section of the quotient map.
:::
:::
