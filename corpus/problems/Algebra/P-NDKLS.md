---
schema: qual/card@1
id: P-NDKLS
kind: problem
title: What are the irreducible representations of finite abelian groups?
classification:
  areas:
  - algebra
  topics:
  - Representation Theory
  - Abelian Groups
  - Character Theory
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
What are the irreducible representations of finite abelian groups over $\mathbb{C}$?
Prove that every irreducible representation is 1-dimensional, and describe the dual group $\widehat{G} \cong G$.
:::

::: solution
**Goal:** Prove that all irreducible complex representations of a finite abelian group $G$ are 1-dimensional characters $\chi: G \to \mathbb{C}^\times$, and that $\widehat{G} \cong G$.

<1>1. Schur's Lemma and 1-Dimensionality:
    *Proof:*
    <2>1. Let $(\rho, V)$ be an irreducible complex representation of a finite group $G$.
    <2>2. For every element $g \in G$, the linear operator $\rho(g): V \to V$ commutes with all $\rho(h)$ ($h \in G$), because $G$ is **abelian**:
        $$\rho(g) \rho(h) = \rho(g h) = \rho(h g) = \rho(h) \rho(g).$$
    <2>3. By **Schur's Lemma**, any endomorphism of an irreducible complex representation that commutes with the $G$-action must be a scalar multiple of the identity:
        $$\rho(g) = \lambda(g) \operatorname{id}_V \quad \text{for some scalar } \lambda(g) \in \mathbb{C}^\times.$$
    <2>4. Therefore, every 1-dimensional subspace of $V$ is stable under $\rho(g)$ for all $g \in G$ (an invariant subspace).
    <2>5. Since $V$ is irreducible (has no non-trivial proper invariant subspaces), $V$ must itself be **1-dimensional**:
        $$\dim_\mathbb{C}(V) = 1.$$

<1>2. Character Group (Pontryagin Dual) $\widehat{G}$:
    *Proof:*
    <2>1. Since $\dim(V) = 1$, $\operatorname{GL}(V) \cong \mathbb{C}^\times$.
    <2>2. An irreducible representation is simply a group homomorphism (a **character**):
        $$\chi: G \longrightarrow \mathbb{C}^\times.$$
    <2>3. Since $G$ is finite of order $|G| = n$, every element $g \in G$ satisfies $g^n = e$.
    <2>4. Thus $\chi(g)^n = \chi(g^n) = \chi(e) = 1$, so the values of $\chi$ are roots of unity:
        $$\chi(g) \in S^1 \subset \mathbb{C}^\times.$$
    <2>5. The set of all characters $\widehat{G} = \operatorname{Hom}(G, \mathbb{C}^\times)$ forms an abelian group under pointwise multiplication:
        $$(\chi_1 \cdot \chi_2)(g) = \chi_1(g) \chi_2(g).$$

<1>3. Isomorphism $\widehat{G} \cong G$:
    *Proof:*
    <2>1. **For Cyclic Groups $\mathbb{Z}_n = \langle g \rangle$:**
        A homomorphism $\chi: \mathbb{Z}_n \to \mathbb{C}^\times$ is completely determined by $\chi(g) \in \{\zeta_n^k \mid 0 \le k < n\}$ where $\zeta_n = e^{2\pi i / n}$.
        There are $n$ distinct characters $\chi_k(g^m) = \zeta_n^{k m}$, and the mapping $k \mapsto \chi_k$ gives an isomorphism $\widehat{\mathbb{Z}_n} \cong \mathbb{Z}_n$.
    <2>2. **For General Finite Abelian Groups:**
        By the Fundamental Theorem of Finite Abelian Groups:
        $$G \cong \mathbb{Z}_{n_1} \times \mathbb{Z}_{n_2} \times \cdots \times \mathbb{Z}_{n_k}.$$
        Taking the dual distributes over direct products:
        $$\widehat{G} \cong \widehat{\mathbb{Z}_{n_1}} \times \cdots \times \widehat{\mathbb{Z}_{n_k}} \cong \mathbb{Z}_{n_1} \times \cdots \times \mathbb{Z}_{n_k} \cong G.$$
    <2>3. Thus $|\widehat{G}| = |G|$, and $G \cong \widehat{G}$ (non-canonically, though $G \cong \widehat{\widehat{G}}$ canonically).

<1>4. Conclusion:
    Every irreducible representation of a finite abelian group is 1-dimensional, given by characters $\chi \in \widehat{G} \cong G$. Q.E.D.
:::
