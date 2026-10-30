---
schema: qual/card@1
id: P-AGH2512VERYAMPLE
kind: problem
title: Tensor products of very ample invertible sheaves
classification:
  areas:
  - algebraic-geometry
  topics:
  - Very Ample Sheaves
  - Invertible Sheaves
  - Segre Embedding
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: Read Exercise II.5.12 and the immersion definition preceding Remark II.5.16.1 in the original Hartshorne transcription. The unrestricted version of (b) is false for that open-in-closed convention. The erratum proves nonexistence of any finite projective embedding in an explicit example, not only failure of the proposed Segre composite. The locally noetherian formulation and the arbitrary-base closed-in-open formulation are proved separately.
- event: solution-written
  by: chatgpt
  date: 2026-09-17
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: Hartshorne II.5.12 prints both parts over arbitrary base schemes, where part (b) is false with the open-in-closed immersion convention. The statement requires Y in (a) and Z in (b) to be locally noetherian.
---

::: {.problem}
(a) Let $X$ be a scheme over a locally noetherian scheme $Y$, and let $\mcl, \mcm$ be two very ample invertible sheaves on $X$ relative to $Y$.
Show that $\mcl \tensor \mcm$ is also very ample.

(b) Let $f: X \to Y$ and $g: Y \to Z$ be two morphisms of schemes, with $Z$ locally noetherian.
Let $\mcl$ be a very ample invertible sheaf on $X$ relative to $Y$, and let $\mcm$ be a very ample invertible sheaf on $Y$ relative to $Z$.
Show that $\mcl \tensor f^* \mcm$ is a very ample invertible sheaf on $X$ relative to $Z$.
:::

::: {.hint}
Use a Segre embedding.
:::

::: {.solution}
Use [[D-MODAMPLE|very ampleness]] and the [[D-MORIMM|immersion]] convention in which the source is an open subscheme of a closed subscheme of the target.

::: pf

::: {.pf-step #s1}

For a scheme $B$ and nonnegative integers $r,s$, the Segre closed immersion
$$
\sigma:\PP_B^r\times_B\PP_B^s\longrightarrow\PP_B^{(r+1)(s+1)-1}
$$
satisfies
$$
\sigma^*\OO(1)\cong q_1^*\OO_{\PP_B^r}(1)\otimes q_2^*\OO_{\PP_B^s}(1),
$$
where $q_1,q_2$ are the projections.

::: pf-proof

The products $X_iY_j$ of the homogeneous coordinate sections generate the displayed tensor product of invertible sheaves and define $\sigma$.
On the target chart with $Z_{ij}\ne0$, its inverse image is $D_+(X_i)\times_B D_+(Y_j)$, and the coordinate map sends
$$
Z_{ab}/Z_{ij}\longmapsto (X_a/X_i)(Y_b/Y_j).
$$
The coordinates with $b=j$ and $a=i$ recover all affine coordinates of the two factors, so the map is surjective on coordinate rings.
Thus $\sigma$ is a closed immersion.
The construction by generating sections identifies its pullback of $\OO(1)$ with their invertible sheaf; equivalently, the chart frames are $X_iY_j$, with transition functions $(X_a/X_i)(Y_b/Y_j)$.
This construction commutes with base change, so the calculation over affine opens proves the assertion over every $B$; see the [Segre embedding](https://stacks.math.columbia.edu/tag/01WD) and [[P-AGH2511CARTPROD]].

:::

:::

::: {.pf-step #s2}

A [[D-MORIMM|locally closed immersion]] into a locally noetherian scheme is an [[D-MORIMM|immersion]] in the convention of the statement.

::: pf-proof

Let $h:V\to W$ be closed in an open subscheme $W'\subseteq W$.
For every affine open $T\subseteq W$, the open subset $T\cap W'$ of the noetherian space $T$ is quasi-compact.
Its closed subscheme $h^{-1}(T)$ is therefore quasi-compact.
Thus $h$ is quasi-compact.
The [factorization for quasi-compact immersions](https://stacks.math.columbia.edu/tag/01QV) writes $h$ as an open immersion followed by a closed immersion.
Concretely, its closed factor is defined by the quasi-coherent ideal $\ker(\OO_W\to h_*\OO_V)$; its restriction to $W'$ is the ideal defining $V$, so $V$ is open in that closed factor.

:::

:::

::: {.pf-step #s3}

The assertion of part (a) holds.

::: pf-proof

Choose $Y$-immersions
$$
i:X\longrightarrow\PP_Y^r,\qquad j:X\longrightarrow\PP_Y^s
$$
with $i^*\OO(1)\cong\mcl$ and $j^*\OO(1)\cong\mcm$.
The graph $\Gamma_j:X\to X\times_Y\PP_Y^s$ is a closed immersion because $\PP_Y^s\to Y$ is separated.
The map $i\times\operatorname{id}:X\times_Y\PP_Y^s\to\PP_Y^r\times_Y\PP_Y^s$ is a base change of $i$.
Their composite is $(i,j)$, which is a locally closed immersion since closed and open immersions are stable under base change and locally closed immersions are stable under composition.
Consequently
$$
h=\sigma\circ(i,j):X\longrightarrow\PP_Y^{(r+1)(s+1)-1}
$$
is a locally closed immersion.
The target is locally noetherian, so step [](#s2){.pf-ref} makes $h$ an immersion in the convention of the statement.
Step [](#s1){.pf-ref} gives
$$
h^*\OO(1)\cong i^*\OO(1)\otimes j^*\OO(1)\cong\mcl\otimes\mcm.
$$
This realizes the required very ample sheaf.

:::

:::

::: {.pf-step #s4}

The assertion of part (b) holds.

::: pf-proof

Choose immersions over the indicated bases
$$
i:X\longrightarrow\PP_Y^r,\qquad j:Y\longrightarrow\PP_Z^s
$$
with $i^*\OO_{\PP_Y^r}(1)\cong\mcl$ and $j^*\OO_{\PP_Z^s}(1)\cong\mcm$.
Write $\pi:\PP_Y^r\to Y$ for the projection and $a:\PP_Y^r\to\PP_Z^r$ for the base-change map, so $\pi\circ i=f$.
The identification $\PP_Y^r\cong\PP_Z^r\times_Z Y$ gives the base change
$$
k=(a,j\circ\pi):\PP_Y^r\longrightarrow\PP_Z^r\times_Z\PP_Z^s
$$
of $j$.
The composite
$$
h=\sigma\circ k\circ i:X\longrightarrow\PP_Z^{(r+1)(s+1)-1}
$$
is a locally closed immersion.
Its target is locally noetherian, so step [](#s2){.pf-ref} gives the required open-in-closed factorization.
The twisting sheaf on relative projective space commutes with base change, giving $a^*\OO_{\PP_Z^r}(1)\cong\OO_{\PP_Y^r}(1)$ [@Har77, Chapter II, §5].
Therefore step [](#s1){.pf-ref} gives
$$
\begin{aligned}
h^*\OO(1)
&\cong i^*a^*\OO_{\PP_Z^r}(1)\otimes (j\circ f)^*\OO_{\PP_Z^s}(1)\\
&\cong\mcl\otimes f^*\mcm.
\end{aligned}
$$
Thus this sheaf is very ample relative to $Z$.

:::

:::

::: pf-qed

Steps [](#s3){.pf-ref} and [](#s4){.pf-ref} prove parts (a) and (b).

:::

:::

:::
