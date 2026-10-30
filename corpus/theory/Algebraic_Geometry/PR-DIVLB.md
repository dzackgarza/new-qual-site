---
schema: qual/card@1
id: PR-DIVLB
kind: proposition
title: Cartier divisors, invertible sheaves, and the Picard group
slogan: 'Cartier divisors are line bundles with rational sections; on locally factorial schemes, Cartier, Weil, and Picard classes coincide.'
classification:
  areas:
  - algebraic-geometry
  topics:
  - Cartier Divisors
  - Picard Group
  - Invertible Sheaves
relations:
- kind: uses
  target: D-DIVOD
- kind: uses
  target: D-5PQ5W
review: draft
prompts:
- What is the correspondence between Cartier divisors and invertible sheaves?
- Why is $\Pic(X) = H^1(X, \units{\OO_X})$?
- Which line bundles come from divisors?
- Why does $\Pic(X) \cong H^1(X, \OO_X^\times)$ need the comparison of Čech and derived-functor $H^1$?
- Describe the maps between Cartier divisors, Weil divisors and line bundles with rational sections.
---

::: {.proposition}
Let $X$ be an integral scheme with function field $K$ and rational-function sheaf $\mck$.
The assignment
$$
D\longmapsto\OO_X(D)\subseteq\mck
$$
is a bijection from Cartier divisors to invertible $\OO_X$-submodules of $\mck$ [@Har10a, Proposition II.6.13]. Passing to Cartier divisors modulo principal divisors gives
$$
\CaCl(X)\longrightarrow\Pic(X),\qquad [D]\longmapsto[\OO_X(D)].
$$
Every invertible sheaf on an integral scheme has a nonzero rational section and hence embeds as an invertible $\OO_X$-submodule of $\mck$. Therefore this map is an isomorphism [@Har10a, Proposition II.6.15].
:::

::: {.proposition}
For every scheme $X$,
$$
\Pic(X)\cong H^1(X,\OO_X^\times)
$$
([[P-AGH345PICH1]]).
If $X$ is integral with rational-function sheaf $\mck$, then the sequence
$$
0 \to \OO_X^\times \to \mck^\times \to \mck^\times/\OO_X^\times \to 0
$$
has cohomology sequence
$$
K^\times\longrightarrow\Div_{\mathrm{Ca}}(X)\longrightarrow\Pic(X)\longrightarrow H^1(X,\mck^\times).
$$
For integral $X$, the sheaf $\mck^\times$ is flasque, so $H^1(X,\mck^\times)=0$; this recovers $\CaCl(X)\cong\Pic(X)$.
:::

::: {.proposition title="Divisors, line bundles with sections, and class groups"}
Let $X$ be an integral separated Noetherian scheme with function field $K$, and write $\mathcal{P}(X)$ for the group of isomorphism classes of pairs $(\mathcal{L}, s)$ with $\mathcal{L}$ invertible and $s$ a nonzero rational section of $\mathcal{L}$, under tensor product.

1. $\Div_{\mathrm{Ca}}(X) \to \mathcal{P}(X)$, $D = \{(U_i, f_i)\} \mapsto (\OO_X(D), 1)$, is an isomorphism, with inverse $(\mathcal{L}, s) \mapsto \{(U_i, \phi_i(s))\}$ for local trivializations $\phi_i\colon\mathcal L\restrict_{U_i}\iso\OO_{U_i}$.
   For an effective $D$ with invertible ideal sheaf $\mci_D$, $\OO_X(D) = \mci_D^{\vee}$ and $1$ is the canonical section vanishing on $D$.

2. If $X$ is regular in codimension one, $\Div_{\mathrm{Ca}}(X) \to \Div(X)$, $\{(U_i, f_i)\} \mapsto \sum_Y v_Y(f_i) Y$ with $U_i \cap Y \neq \emptyset$, is a homomorphism, and $(\mathcal{L}, s) \mapsto \div s$ is the composite with the inverse of part 1.

3. Under these maps, $t \in \units{K}$ goes to the principal Cartier divisor $\{(X, t)\}$, the pair $(\OO_X, t)$, and the principal Weil divisor $\div t$, so they descend to $\CaCl(X) \to \Cl(X)$ and $\CaCl(X) \cong \Pic(X)$.

4. If every local ring $\OO_{X,x}$ is a unique factorization domain, then $\CaCl(X) \cong \Cl(X) \cong \Pic(X)$, with inverse $D \mapsto (\OO_X(D), 1)$ [@Har10a, Proposition II.6.11].
:::

::: {.remark}
If local frames of an invertible sheaf satisfy $e_i=g_{ij}e_j$ on $U_i\cap U_j$, then $\theset{g_{ij}}$ is a Čech $1$-cocycle with values in $\OO_X^\times$. Conversely, such a cocycle glues the trivial line bundles on the $U_i$. The canonical degree-one comparison identifies these Čech classes with $H^1(X,\OO_X^\times)$, yielding the Picard-group isomorphism above.

For an integral locally factorial Noetherian scheme,
$$
\Pic(X) \cong \CaCl(X) \cong \Cl(X).
$$
:::
