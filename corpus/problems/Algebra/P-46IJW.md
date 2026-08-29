---
schema: qual/card@1
id: P-46IJW
kind: problem
title: Artin–Wedderburn theorem
classification:
  areas:
  - algebra
  topics:
  - Semisimplicity
  - Rings
  - Structure Theorem
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
State and explain the Artin–Wedderburn Structure Theorem for semisimple Artinian rings and finite-dimensional semisimple algebras.
:::

::: solution
**Goal:** State the Artin–Wedderburn Theorem, classify simple modules, and detail its formulation for rings and finite-dimensional algebras over a field.

<1>1. Statement of the Artin–Wedderburn Theorem (Rings):
    *Proof:*
    <2>1. A ring $R$ (with 1) is **semisimple** if it is semisimple as a left $R$-module (i.e. $R$ is a direct sum of minimal left ideals).
    <2>2. **Theorem (Artin–Wedderburn):** Let $R$ be a semisimple ring (or a left Artinian ring with Jacobson radical $J(R) = 0$).
        Then $R$ is isomorphic to a finite direct product (direct sum) of matrix rings over division rings:
        $$R \cong M_{n_1}(D_1) \times M_{n_2}(D_2) \times \cdots \times M_{n_r}(D_r) = \bigoplus_{i=1}^r M_{n_i}(D_i)$$
        where:
        - $r \ge 1$ is the number of isomorphism classes of simple left $R$-modules.
        - Each $D_i$ is a division ring.
        - Each $n_i \ge 1$ is a positive integer.
    <2>3. **Uniqueness:** The number of factors $r$, the sizes $n_i$, and the division rings $D_i$ (up to isomorphism) are uniquely determined by $R$ up to permutation of the factors.

<1>2. Simple Modules and Schur's Lemma:
    *Proof:*
    <2>1. There are exactly $r$ non-isomorphic simple (irreducible) left $R$-modules $S_1, S_2, \dots, S_r$.
    <2>2. The $i$-th simple module is isomorphic to the column vectors $S_i \cong D_i^{n_i}$, on which $M_{n_i}(D_i)$ acts by matrix multiplication and all other factors act as 0.
    <2>3. By **Schur's Lemma**, the endomorphism ring of each simple module is a division ring:
        $$\operatorname{End}_R(S_i) \cong D_i^{\text{op}}.$$
    <2>4. The ring $R$ itself decomposes as a left $R$-module as:
        $$R \cong \bigoplus_{i=1}^r S_i^{\oplus n_i} = S_1^{n_1} \oplus S_2^{n_2} \oplus \cdots \oplus S_r^{n_r}.$$

<1>3. Special Case: Finite-Dimensional Algebras over an Algebraically Closed Field $k$:
    *Proof:*
    <2>1. Let $A$ be a finite-dimensional semisimple algebra over an algebraically closed field $k$ (e.g. $k = \mathbb{C}$).
    <2>2. The only finite-dimensional division algebra over an algebraically closed field is $k$ itself ($D_i \cong k$).
    <2>3. Therefore, the Artin–Wedderburn theorem specializes to:
        $$A \cong M_{n_1}(k) \times M_{n_2}(k) \times \cdots \times M_{n_r}(k).$$
    <2>4. **Application to Group Rings (Maschke's Theorem):** For a finite group $G$ and $k = \mathbb{C}$, the group algebra $\mathbb{C}[G]$ is semisimple, giving:
        $$\mathbb{C}[G] \cong \bigoplus_{i=1}^r M_{d_i}(\mathbb{C})$$
        where $d_i = \dim(V_i)$ are the degrees of the irreducible representations of $G$, and $|G| = \sum d_i^2$.

<1>4. Conclusion:
    Every semisimple Artinian ring decomposes uniquely as $\prod_{i=1}^r M_{n_i}(D_i)$. Q.E.D.
:::
