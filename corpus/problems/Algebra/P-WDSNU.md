---
schema: qual/card@1
id: P-WDSNU
kind: problem
title: Regular representation
classification:
  areas:
  - algebra
  topics:
  - Representation Theory
  - Group Rings
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
What is the regular representation of a finite group $G$?
State its character, decomposition into irreducible representations, and connection to the group algebra $\mathbb{C}[G]$.
:::

::: solution
**Goal:** Define the (left) regular representation $L: G \to \operatorname{GL}(\mathbb{C}[G])$, compute its character, and prove its decomposition into irreducible representations.

<1>1. Definition of the Regular Representation:
    *Proof:*
    <2>1. Let $G$ be a finite group of order $|G| = n$.
    <2>2. Let $V = \mathbb{C}[G]$ be the group algebra of $G$ over $\mathbb{C}$, which is a complex vector space of dimension $|G|$ with formal basis $\{e_g\}_{g \in G}$ indexed by the elements of $G$.
    <2>3. The **left regular representation** $\rho_{\text{reg}}: G \to \operatorname{GL}(\mathbb{C}[G])$ is defined on the basis vectors by left translation:
        $$\rho_{\text{reg}}(g)(e_h) = e_{gh} \quad \text{for all } g, h \in G,$$
        extended linearly to all of $\mathbb{C}[G]$.
    <2>4. $\rho_{\text{reg}}$ is a faithful representation of dimension $\dim(V) = |G|$.

<1>2. Character of the Regular Representation $\chi_{\text{reg}}$:
    *Proof:*
    <2>1. The matrix of $\rho_{\text{reg}}(g)$ relative to the standard basis $\{e_h\}_{h \in G}$ is a permutation matrix.
    <2>2. The diagonal entries correspond to basis vectors $e_h$ fixed by left translation: $gh = h \iff g = e$.
    <2>3. Therefore:
        $$\chi_{\text{reg}}(g) = \operatorname{tr}(\rho_{\text{reg}}(g)) = \begin{cases} |G| & \text{if } g = e, \\ 0 & \text{if } g \ne e. \end{cases}$$

<1>3. Decomposition into Irreducible Representations:
    *Proof:*
    <2>1. Let $\{V_1, V_2, \dots, V_k\}$ be the complete set of non-isomorphic irreducible complex representations of $G$, with dimensions $d_i = \dim(V_i)$ and characters $\chi_i$.
    <2>2. Let the decomposition of the regular representation be $\rho_{\text{reg}} \cong \bigoplus_{i=1}^k m_i V_i$.
    <2>3. By character orthogonality, the multiplicity $m_i$ of $V_i$ in $\rho_{\text{reg}}$ is:
        $$m_i = \langle \chi_{\text{reg}}, \chi_i \rangle = \frac{1}{|G|} \sum_{g \in G} \chi_{\text{reg}}(g) \overline{\chi_i(g)} = \frac{1}{|G|} \chi_{\text{reg}}(e) \overline{\chi_i(e)} = \frac{1}{|G|} |G| d_i = d_i.$$
    <2>4. Thus, **every irreducible representation $V_i$ appears in the regular representation with multiplicity equal to its degree $d_i = \dim(V_i)$**:
        $$\mathbb{C}[G] \cong \bigoplus_{i=1}^k d_i V_i = \bigoplus_{i=1}^k V_i^{\oplus \dim(V_i)}.$$
    <2>5. Taking dimensions of both sides gives the classical identity:
        $$|G| = \sum_{i=1}^k d_i^2.$$

<1>4. Wedderburn's Theorem / Artin-Wedderburn Isomorphism:
    *Proof:*
    <2>1. As an associative $\mathbb{C}$-algebra, the group ring decomposes into a direct sum of matrix algebras:
        $$\mathbb{C}[G] \cong \prod_{i=1}^k \operatorname{End}_\mathbb{C}(V_i) \cong \bigoplus_{i=1}^k M_{d_i}(\mathbb{C}).$$

<1>5. Conclusion:
    The regular representation on $\mathbb{C}[G]$ has character $\chi_{\text{reg}}(e) = |G|$ and $\chi_{\text{reg}}(g\ne e) = 0$, containing every irreducible representation $V_i$ with multiplicity $\dim(V_i)$. Q.E.D.
:::
