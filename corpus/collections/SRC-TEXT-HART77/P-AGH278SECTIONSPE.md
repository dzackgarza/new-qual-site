---
schema: qual/card@1
id: P-AGH278SECTIONSPE
kind: problem
title: Sections of a projective bundle and invertible quotients
classification:
  areas:
  - algebraic-geometry
  topics:
  - Projective Bundles
  - Locally Free Sheaves
  - Invertible Sheaves
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: Checked the projective-bundle and quotient conventions against Stacks Project section 27.21 (Tag 01OA). The proof constructs the tautological quotient and its inverse in local coordinates, retains the quotient map as part of the data, and verifies base-change naturality.
- event: solution-written
  by: chatgpt
  date: 2026-09-17
---

::: {.problem}
Let $X$ be a noetherian scheme, let $\mce$ be a coherent locally free sheaf on $X$, and let $\pi: \PP(\mce) \to X$ be the corresponding projective space bundle.
Show that there is a natural bijection between sections of $\pi$, i.e. morphisms $\sigma: X \to \PP(\mce)$ with $\pi \circ \sigma = \id_X$, and quotient invertible sheaves $\mce \to \mcl \to 0$ of $\mce$.
:::

::: {.solution}
Use the quotient convention
$$
P=\PP(\mce)\coloneqq\operatorname{Proj}_X\operatorname{Sym}^{\bullet}\mce.
$$
An invertible quotient is a pair $(\mcl,q)$ with $q:\mce\twoheadrightarrow\mcl$, considered up to isomorphism: $(\mcl,q)$ and $(\mcl',q')$ are equivalent when there is an isomorphism $\theta:\mcl\to\mcl'$ with $\theta\circ q=q'$.
Thus the quotient map, not only the class of $\mcl$ in the Picard group, is part of the data.
If $\mce$ has rank zero at a point, neither a section of $\pi$ nor an invertible quotient on all of $X$ exists, so both sets are empty.
For the empty scheme both sets have one element.
We may therefore prove the assertion using open sets on which $\mce$ is free of positive finite rank.

<1>1. The [[D-SCHRELSPECPROJ|relative Proj]] carries a canonical surjection
$$
q_{\mathrm{univ}}:\pi^*\mce\twoheadrightarrow\OO_P(1).
$$

::: {.proof}
On an affine open $V=\Spec A\subseteq X$ with a frame $e_0,\ldots,e_r$ for $\mce$, the symmetric algebra is $A[T_0,\ldots,T_r]$, with $T_i$ corresponding to $e_i$ in degree one.
Thus $P|_V\cong\PP_V^r$.
Define the map there by $e_i\mapsto T_i$, where $T_i$ is the coordinate section of $\OO(1)$.
On $D_+(T_i)$ this coordinate is a frame of $\OO(1)$, so the map is surjective.
The maps on different frames agree: a change of frame in $\mce$ makes the identical linear change of degree-one elements in its symmetric algebra.
They therefore glue to the stated canonical quotient.
:::

<1>2. A section $\sigma:X\to P$ gives the invertible quotient
$$
q_\sigma:\mce\cong\sigma^*\pi^*\mce
\xrightarrow{\sigma^*q_{\mathrm{univ}}}\sigma^*\OO_P(1).
$$

::: {.proof}
The first identification comes from $\pi\circ\sigma=\id_X$.
Pullback preserves invertible sheaves and surjective module morphisms, the latter by right exactness of tensor product in its definition.
Hence the target is invertible and the displayed map is surjective.
This construction gives a well-defined isomorphism class of quotient pairs.
:::

<1>3. Every invertible quotient $q:\mce\twoheadrightarrow\mcl$ defines a unique section $\sigma_q:X\to P$ whose pulled-back quotient is isomorphic to $(\mcl,q)$.

::: {.proof}
On a framed affine open $V$ as in step <1>1, put $s_i=q(e_i)\in\Gamma(V,\mcl)$.
These sections generate $\mcl|_V$.
Let $V_i\subseteq V$ be the open subset where $s_i$ is a frame.
On $V_i$, define the morphism to the chart $D_+(T_i)$ of $\PP_V^r$ by the coordinate ratios
$$
T_j/T_i\longmapsto s_j/s_i.
$$
These are regular functions because $s_i$ trivializes the invertible sheaf there.
On $V_i\cap V_h$, the identities $(s_j/s_i)/(s_h/s_i)=s_j/s_h$ are exactly the projective-chart transition formulas.
The maps consequently glue to a $V$-morphism $V\to\PP_V^r$, as in [@Har10a, Theorem II.7.1].

Changing the frame of $\mce$ replaces the $s_i$ by the corresponding linear combinations, the same coordinate change used to glue $P$.
On an overlap, writing both constructions in a common local frame gives the same ratios.
The local morphisms therefore glue to a section $\sigma_q:X\to P$.
Replacing $q$ by an isomorphic quotient makes no change to these ratios, so the section depends only on its quotient class.

The local isomorphism $\sigma_q^*\OO_P(1)\to\mcl$ sends the pullback of $T_i$ to $s_i$.
On each $V_i$ this is an isomorphism because it sends a frame to a frame, and it intertwines the pulled-back universal quotient with $q$.
Such an isomorphism is unique: the sections $q(e_i)$ generate the target.
The local isomorphisms therefore glue over all of $X$.
Finally, any section inducing this quotient must have the displayed coordinate-ring maps on every $V_i$, so must equal $\sigma_q$.
:::

<1>4. The two constructions are inverse and are natural under base change.

::: {.proof}
Starting with a quotient, step <1>3 proves that pulling back the universal quotient along its associated section recovers that quotient up to the specified isomorphism.
Starting with a section $\sigma$, its coordinates on each $D_+(T_i)$ pull back to the ratios of the images of $e_j$ under $q_\sigma$.
Step <1>3 reconstructs exactly those maps on coordinate rings, so it reconstructs $\sigma$.
Thus the two constructions are mutually inverse.

For any morphism $g:X'\to X$, the framed polynomial-algebra construction gives
$$
\PP(g^*\mce)\cong\PP(\mce)\times_X X',
$$
with the universal quotient and $\OO(1)$ identified with their pullbacks.
Pullback takes an invertible quotient of $\mce$ to an invertible quotient of $g^*\mce$, and a section to its base-changed section.
The coordinate ratios in step <1>3 commute with these pullbacks, proving naturality.
:::

<1>5. Q.E.D.

::: {.proof}
Steps <1>1--<1>3 construct both maps, and step <1>4 proves the required natural bijection.
:::
:::
