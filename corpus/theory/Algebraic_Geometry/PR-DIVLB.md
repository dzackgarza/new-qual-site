---
schema: qual/card@1
id: PR-DIVLB
kind: proposition
title: Cartier divisors, invertible sheaves, and the Picard group
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
- Why is $\Pic(X) = H^1(X, \OO_X\units)$?
- Which line bundles come from divisors?
- Why does $\Pic(X) \cong H^1(X, \OO_X^\times)$ need the comparison of Čech and derived-functor $H^1$?
- Describe the maps between Cartier divisors, Weil divisors and line bundles with rational sections.
---

::: {.proposition}
$D \mapsto \OO_X(D)$ is an injection $\CaCl(X) \injects \Pic(X)$, and it is a bijection onto the invertible subsheaves of $\mck$ [@Har10a, Proposition II.6.13].
When $X$ is integral every invertible sheaf is such a subsheaf, so $\CaCl(X) \cong \Pic(X)$ [@Har10a, Proposition II.6.15].
:::

::: {.proposition}
$\Pic(X) \cong H^1(X, \OO_X\units)$ ([[P-AGH345PICH1]]), and the sequence
\[
0 \to \OO_X\units \to \mck\units \to \mck\units/\OO_X\units \to 0
\]
has cohomology sequence $\mck(X)\units \to \Div_{\mathrm{Ca}}(X) \to \Pic(X) \to H^1(X, \mck\units)$.
:::

::: {.proposition title="Divisors, line bundles with sections, and class groups"}
Let $X$ be an integral separated Noetherian scheme with function field $K$, and write $\mathcal{P}(X)$ for the group of isomorphism classes of pairs $(\mathcal{L}, s)$ with $\mathcal{L}$ invertible and $s$ a nonzero rational section of $\mathcal{L}$, under tensor product.

1. $\Div_{\mathrm{Ca}}(X) \to \mathcal{P}(X)$, $D = \{(U_i, f_i)\} \mapsto (\OO_X(D), 1)$, is an isomorphism, with inverse $(\mathcal{L}, s) \mapsto \{(U_i, \phi_i(s)^{-1})\}$ for local trivializations $\phi_i$. For an effective $D$ with invertible ideal sheaf $\mci_D$, $\OO_X(D) = \mci_D^{\vee}$ and $1$ is the canonical section vanishing on $D$.

2. If $X$ is regular in codimension one, $\Div_{\mathrm{Ca}}(X) \to \Div(X)$, $\{(U_i, f_i)\} \mapsto \sum_Y v_Y(f_i) Y$ with $U_i \cap Y \neq \emptyset$, is a homomorphism, and $(\mathcal{L}, s) \mapsto \div s$ is the composite with the inverse of part 1.

3. Under these maps, $t \in K\units$ goes to the principal Cartier divisor $\{(X, t)\}$, the pair $(\OO_X, t)$, and the principal Weil divisor $\div t$, so they descend to $\CaCl(X) \to \Cl(X)$ and $\CaCl(X) \cong \Pic(X)$.

4. If every local ring $\OO_{X,x}$ is a unique factorization domain, then $\CaCl(X) \cong \Cl(X) \cong \Pic(X)$, with inverse $D \mapsto (\OO_X(D), 1)$ [@Har10a, Proposition II.6.11].
:::

::: {.remark}
Both halves are the same observation: gluing data for a line bundle is a cocycle $g_{ij} \in \OO\units(U_{ij})$, and Cartier data $f_i$ produces the cocycle $g_{ij} = f_i/f_j$.
Saying "a Cartier divisor is a line bundle together with a choice of rational section" is the cleanest one-line answer, and it explains the failure of surjectivity for non-integral $X$: a line bundle with no rational section is not a divisor.

Combined with the injection $\CaCl \injects \Cl$, the chain to recite is
\[
\Pic(X) \cong \CaCl(X) \injects \Cl(X) ,
\]
an isomorphism throughout when $X$ is locally factorial.
The gap at the second arrow is measured by the singularities.
:::
