---
schema: qual/card@1
id: P-APAS26J
kind: problem
title: Centralizer of $\mathcal{C}(H)$ in $\mathcal{C}(G)$ via branching multiplicities
classification:
  areas:
  - applied-algebra
  topics:
  - Representation Theory
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured as a Lamport proof of the argument already on the card, which is correct:
    Wedderburn decomposes both group algebras, the restriction decomposes into isotypic pieces,
    the image of C(H) is block-diagonal with each block generating End(W^mu), and the commutant
    is the other tensor factor. Added: the reduction of the centralizer in a direct sum to the
    direct sum of the commutants, which the card stated in one sentence; the argument that an
    operator commuting with the block-diagonal algebra preserves each isotypic block, via the
    projections being polynomial in the generators; the matrix-unit computation identifying the
    single-block commutant as I ⊗ End(C^m); and the closing remark that the terms with m = 0 may
    be kept because they contribute the zero algebra. No statement was changed. Not claimed: a
    retained solution set; the collection's provenance is the examination paper only.
---

::: {.problem}
Let $G$ be a finite group and let $H$ be a subgroup of $G$.
Let $\Lambda(G)$ be a set parameterizing irreducible unitary representations $V^\lambda$ of $G$, and let $\Lambda(H)$ be a set parameterizing irreducible unitary representations $W^\mu$ of $H$.
For $\lambda \in \Lambda(G)$ and $\mu \in \Lambda(H)$, let $m_{\lambda\mu}$ be the multiplicity of $W^\mu$ in the restriction of $V^\lambda$ to $H$.
Omitting terms with $m_{\lambda\mu} = 0$, show that the centralizer of $\mathcal{C}(H)$ in $\mathcal{C}(G)$ is isomorphic to
$$
\bigoplus_{\lambda \in \Lambda(G)} \bigoplus_{\mu \in \Lambda(H)} \operatorname{End}\bigl(\CC^{m_{\lambda\mu}}\bigr).
$$
:::

::: {.solution}
Throughout $G$ is finite, $H \le G$, and $\mathcal{C}(G) \coloneqq \CC[G]$ is the complex group algebra of $G$, with $\mathcal{C}(H) = \CC[H]$ embedded in it; $\theset{V^{\lambda}}$ and $\theset{W^{\mu}}$ are the irreducible unitary representations of $G$ and of $H$ up to isomorphism, and $m_{\lambda\mu}$ is the multiplicity of $W^{\mu}$ in $\restrictionof{V^{\lambda}}{H}$. The collection's `provenance` is the Spring 2026 preliminary examination, and no solutions sheet accompanies it, so the argument below is the card's own.

::: pf

::: {.pf-step #wedderburn}
$\mathcal{C}(G) \cong \bigoplus_{\lambda \in \Lambda(G)}\Endo(V^{\lambda})$ and $\mathcal{C}(H) \cong \bigoplus_{\mu\in\Lambda(H)}\Endo(W^{\mu})$.

::: pf-proof
For a finite group $\Gamma$ over $\CC$ Maschke's theorem makes $\CC[\Gamma]$ semisimple, and the Wedderburn decomposition of a semisimple algebra over an algebraically closed field as a product of matrix algebras gives $\CC[\Gamma] \cong \prod_{}\Endo(U)$ over the irreducible $\Gamma$-modules $U$; the product is written as a direct sum of algebras, one summand per isomorphism class. Applied to $G$ and to $H$ this is the displayed pair.

:::

:::

::: {.pf-step #reduce}
The centralizer of $\mathcal{C}(H)$ in $\mathcal{C}(G)$ is $\bigoplus_{\lambda}\bigl(\text{the commutant of the image of }\mathcal{C}(H)\text{ in }\Endo(V^{\lambda})\bigr)$.

::: pf-proof
Under the first decomposition an element of $\mathcal{C}(G)$ is a tuple $(x_{\lambda})_{\lambda}$, and the image of $\mathcal{C}(H)$ under the composite $\mathcal{C}(H) \hookrightarrow \mathcal{C}(G) \to \Endo(V^{\lambda})$ is a subalgebra $A_{\lambda} \subseteq \Endo(V^{\lambda})$, with the image of $\mathcal{C}(H)$ in $\mathcal{C}(G)$ being the tuple of the $A_{\lambda}$. A tuple $(x_{\lambda})$ centralizes every tuple $(a_{\lambda})$ lying in the image exactly when $x_{\lambda}a_{\lambda} = a_{\lambda}x_{\lambda}$ for every $\lambda$ and every $a_{\lambda} \in A_{\lambda}$, that is when each $x_{\lambda}$ lies in the commutant of $A_{\lambda}$ in $\Endo(V^{\lambda})$.

:::

:::

::: {.pf-step #restriction}
For fixed $\lambda$, $\restrictionof{V^{\lambda}}{H} \cong \bigoplus_{\mu}W^{\mu}\otimes\CC^{m_{\lambda\mu}}$ as $H$-modules, the sum over the $\mu$ with $m_{\lambda\mu} \ne 0$.

::: pf-proof
Over $\CC$ the restriction is completely reducible, so it is the direct sum of its isotypic components; the $\mu$-isotypic component is the direct sum of $m_{\lambda\mu}$ copies of $W^{\mu}$, which is $W^{\mu}\otimes\CC^{m_{\lambda\mu}}$ with $H$ acting on the first factor alone. Terms with $m_{\lambda\mu} = 0$ contribute $0$ and are omitted.

:::

:::

::: {.pf-step #image}
The image $A_{\lambda}$ of $\mathcal{C}(H)$ in $\Endo(V^{\lambda})$ is $\bigoplus_{\mu}\bigl(\Endo(W^{\mu})\otimes I_{m_{\lambda\mu}}\bigr)$.

::: pf-proof
By step [](#restriction){.pf-ref} the algebra $\Endo(V^{\lambda})$ is identified with $\Endo\bigl(\bigoplus_{\mu}W^{\mu}\otimes\CC^{m_{\lambda\mu}}\bigr)$, which is the algebra of block matrices with block $(\mu,\mu')$ equal to $\Hom(W^{\mu'}\otimes\CC^{m_{\lambda\mu'}}, W^{\mu}\otimes\CC^{m_{\lambda\mu}})$. The image of $\CC[H]$ is the subalgebra of block-diagonal elements with $h$ acting by $\rho_{\mu}(h)\otimes I$ on the $\mu$-block; as $h$ ranges over $H$ these generate $\Endo(W^{\mu})$ in the $\mu$-block, because $W^{\mu}$ is irreducible and hence $\CC[H] \to \Endo(W^{\mu})$ is surjective, and they generate nothing else. So $A_{\lambda}$ is the direct sum of the $\Endo(W^{\mu})\otimes I_{m_{\lambda\mu}}$ over $\mu$.

:::

:::

::: {.pf-step #commutant}
The commutant of $A_{\lambda}$ in $\Endo(V^{\lambda})$ is $\bigoplus_{\mu}\bigl(I_{W^{\mu}}\otimes\Endo(\CC^{m_{\lambda\mu}})\bigr)$, which is isomorphic to $\bigoplus_{\mu}\Endo(\CC^{m_{\lambda\mu}})$.

::: pf-proof
An endomorphism of $\bigoplus_{\mu}U_{\mu}$, with $U_{\mu} = W^{\mu}\otimes\CC^{m_{\lambda\mu}}$, commuting with the block-diagonal algebra $\bigoplus_{\mu}\Endo(W^{\mu})\otimes I$ must map each $U_{\mu}$ into itself: the projection onto $U_{\mu}$ is a polynomial in the block-diagonal generators, so it commutes with the endomorphism, and the off-diagonal blocks vanish. On the single block, an operator commuting with $\Endo(W)\otimes I_m$ on $W\otimes\CC^{m}$ is of the form $I_{W}\otimes T$ with $T \in \Endo(\CC^{m})$: for matrix units $E_{ij}\in\Endo(W)$ the identity $g(E_{ij}\otimes I) = (E_{ij}\otimes I)g$ forces $g$ to have scalar blocks, and the double commutant theorem (or a direct computation) identifies the set of those with $I\otimes\Endo(\CC^{m})$. Taking dimensions $\dim W^{\mu} = d_{\mu}$ gives $\dim\bigl(I\otimes\Endo(\CC^{m})\bigr) = m^{2}$, so this algebra is isomorphic to $\Endo(\CC^{m_{\lambda\mu}})$.

:::

:::

::: pf-step
The centralizer of $\mathcal{C}(H)$ in $\mathcal{C}(G)$ is isomorphic to $\bigoplus_{\lambda \in \Lambda(G)}\bigoplus_{\mu \in \Lambda(H)}\Endo(\CC^{m_{\lambda\mu}})$, omitting the terms with $m_{\lambda\mu} = 0$.

::: pf-proof
Steps [](#reduce){.pf-ref} and [](#commutant){.pf-ref} together identify the centralizer with $\bigoplus_{\lambda}\bigoplus_{\mu}\Endo(\CC^{m_{\lambda\mu}})$, the inner sum over the $\mu$ with $m_{\lambda\mu} \ne 0$; adding the zero summands for the other $\mu$ does not change the algebra, so the formula may be written over all $\mu \in \Lambda(H)$ as the exercise does.

:::

:::

:::
:::
