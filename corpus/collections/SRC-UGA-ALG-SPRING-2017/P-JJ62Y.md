---
schema: qual/card@1
id: P-JJ62Y
kind: problem
title: Galois group of $x^5-2$ over $\QQ$ isomorphic to $\begin{pmatrix}a&b\\0&1\end{pmatrix}$
  with $a\in\FF_5^\times$ and $b\in\FF_5$, and the Galois intermediate fields
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Splitting Fields
  - Matrix Groups
relations: []
review: draft
---

::: problem
(a) Let $K$ denote the splitting field of $x^5 - 2$ over $\mathbb{Q}$. Show that the Galois group $\operatorname{Gal}(K/\mathbb{Q})$ is isomorphic to the matrix group
$$
\operatorname{Aff}(\mathbb{F}_5) = \left\{ \begin{pmatrix} a & b \\ 0 & 1 \end{pmatrix} \;\middle|\; a \in \mathbb{F}_5^\times, \, b \in \mathbb{F}_5 \right\}.
$$

(b) Determine all intermediate fields between $K$ and $\mathbb{Q}$ that are Galois over $\mathbb{Q}$.
:::

::: solution
**Goal:** Compute the Galois group of the splitting field of $x^5 - 2$ as an affine matrix group over $\mathbb{F}_5$, and classify all normal subgroups to determine the Galois intermediate extensions.

<1>1. Part (a): Splitting field and extension degree.
::: {.proof}
    <2>1. The roots of $x^5 - 2$ in $\mathbb{C}$ are $\alpha_k = \sqrt[5]{2} \zeta_5^k$ for $k \in \{0, 1, 2, 3, 4\}$, where $\sqrt[5]{2} \in \mathbb{R}$ is the real 5-th root and $\zeta_5 = e^{2\pi i / 5}$ is a primitive 5-th root of unity.
    <2>2. The splitting field is $K = \mathbb{Q}(\sqrt[5]{2}, \zeta_5)$.
    <2>3. By Eisenstein's criterion with $p = 2$, $x^5 - 2$ is irreducible over $\mathbb{Q}$, so $[\mathbb{Q}(\sqrt[5]{2}) : \mathbb{Q}] = 5$.
    <2>4. The cyclotomic polynomial $\Phi_5(x) = x^4 + x^3 + x^2 + x + 1$ is irreducible over $\mathbb{Q}$, so $[\mathbb{Q}(\zeta_5) : \mathbb{Q}] = 4$.
    <2>5. Since $\gcd(5, 4) = 1$, the extension degree is
    $$[K : \mathbb{Q}] = [\mathbb{Q}(\sqrt[5]{2}) : \mathbb{Q}] \cdot [\mathbb{Q}(\zeta_5) : \mathbb{Q}] = 5 \cdot 4 = 20.$$
    <2>6. Thus $|G| = |\operatorname{Gal}(K/\mathbb{Q})| = 20$.

:::

<1>2. Part (a): Group isomorphism with $\operatorname{Aff}(\mathbb{F}_5)$.
::: {.proof}
    <2>1. Any automorphism $\sigma \in G = \operatorname{Gal}(K/\mathbb{Q})$ is uniquely determined by its action on the generators $\zeta_5$ and $\sqrt[5]{2}$.
    <2>2. Since $\sigma(\zeta_5)$ must be a primitive 5-th root of unity and $\sigma(\sqrt[5]{2})$ must be a root of $x^5 - 2$:
    $$\sigma(\zeta_5) = \zeta_5^a \quad \text{for some } a \in \mathbb{F}_5^\times = \{1, 2, 3, 4\},$$
    $$\sigma(\sqrt[5]{2}) = \sqrt[5]{2} \zeta_5^b \quad \text{for some } b \in \mathbb{F}_5 = \{0, 1, 2, 3, 4\}.$$
    <2>3. For each pair $(a, b) \in \mathbb{F}_5^\times \times \mathbb{F}_5$, denote this unique automorphism by $\sigma_{a, b}$. Since there are $4 \times 5 = 20$ such pairs and $|G| = 20$, every pair $(a, b)$ occurs.
    <2>4. Compute the composition $\sigma_{a, b} \circ \sigma_{c, d}$:
    $$(\sigma_{a, b} \circ \sigma_{c, d})(\zeta_5) = \sigma_{a, b}(\zeta_5^c) = (\zeta_5^a)^c = \zeta_5^{a c},$$
    $$(\sigma_{a, b} \circ \sigma_{c, d})(\sqrt[5]{2}) = \sigma_{a, b}(\sqrt[5]{2} \zeta_5^d) = (\sqrt[5]{2} \zeta_5^b)(\zeta_5^a)^d = \sqrt[5]{2} \zeta_5^{a d + b}.$$
    <2>5. Thus $\sigma_{a, b} \circ \sigma_{c, d} = \sigma_{a c, \, a d + b}$.
    <2>6. Define the map $\Psi: G \to \operatorname{GL}_2(\mathbb{F}_5)$ by
    $$\Psi(\sigma_{a, b}) = \begin{pmatrix} a & b \\ 0 & 1 \end{pmatrix}.$$
    <2>7. Multiply the corresponding matrices:
    $$\begin{pmatrix} a & b \\ 0 & 1 \end{pmatrix} \begin{pmatrix} c & d \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} a c & a d + b \\ 0 & 1 \end{pmatrix} = \Psi(\sigma_{a c, \, a d + b}).$$
    <2>8. Thus $\Psi$ is a group homomorphism. Since $\Psi(\sigma_{a, b}) = I \iff a = 1, b = 0 \iff \sigma_{a, b} = \operatorname{id}$, $\Psi$ is injective.
    <2>9. Since both groups have order 20, $\Psi$ is an isomorphism.

:::

<1>3. Part (b): Classification of Galois intermediate fields.
::: {.proof}
    <2>1. By the Fundamental Theorem of Galois Theory, intermediate fields $E$ that are Galois over $\mathbb{Q}$ correspond bijectively to normal subgroups $N \trianglelefteq G$.
    <2>2. Structure of normal subgroups of $G \cong \operatorname{Aff}(\mathbb{F}_5) \cong \mathbb{Z}/5\mathbb{Z} \rtimes \mathbb{Z}/4\mathbb{Z}$:
        - Sylow 5-subgroup: $N_5 = \left\{ \begin{pmatrix} 1 & b \\ 0 & 1 \end{pmatrix} \;\middle|\; b \in \mathbb{F}_5 \right\} \cong \mathbb{Z}/5\mathbb{Z}$.
        - $N_5$ is normal in $G$ because $n_5 \equiv 1 \pmod 5$ and $n_5 \mid 4 \implies n_5 = 1$.
        - The quotient $G/N_5 \cong \mathbb{F}_5^\times \cong \mathbb{Z}/4\mathbb{Z}$ is cyclic of order 4.
    <2>3. Normal subgroups containing $N_5$:
        - Every subgroup of the cyclic quotient $G/N_5 \cong \mathbb{Z}/4\mathbb{Z}$ is normal, yielding 3 normal subgroups containing $N_5$:
          1. $N = N_5$ of order 5 (index 4 in $G$): The fixed field is $K^{N_5} = \mathbb{Q}(\zeta_5)$, which is Galois over $\mathbb{Q}$ with Galois group $\mathbb{Z}/4\mathbb{Z}$.
          2. $N = \left\{ \begin{pmatrix} a & b \\ 0 & 1 \end{pmatrix} \;\middle|\; a \in \{\pm 1\}, \, b \in \mathbb{F}_5 \right\}$ of order 10 (index 2 in $G$): The fixed field is the unique quadratic subfield of $\mathbb{Q}(\zeta_5)$, which is $\mathbb{Q}(\sqrt{5})$ (since $\zeta_5 + \zeta_5^{-1} = \frac{-1 + \sqrt{5}}{2}$).
          3. $N = G$ of order 20 (index 1 in $G$): The fixed field is $K^G = \mathbb{Q}$.
    <2>4. Non-existence of other normal subgroups:
        - If $N \trianglelefteq G$ does not contain $N_5$, then $N \cap N_5 = \{I\}$, so $|N|$ is coprime to 5, meaning $|N| \in \{1, 2, 4\}$.
        - If $|N| = 1$, $N = \{I\}$, corresponding to the fixed field $K$.
        - If $|N| = 2$, then $N = \left\{ I, \begin{pmatrix} -1 & b \\ 0 & 1 \end{pmatrix} \right\}$. Conjugating by $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ yields
        $$\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} -1 & b \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} -1 & b - 2 \\ 0 & 1 \end{pmatrix} \notin N \quad (\text{since } -2 \not\equiv 0 \pmod 5).$$
        Thus no subgroup of order 2 is normal.
        - If $|N| = 4$, $N$ would be a normal Sylow 2-subgroup, but $n_2 = 5$ (the 5 conjugates of $\mathbb{Z}/4\mathbb{Z}$), so no Sylow 2-subgroup is normal.
    <2>5. The complete list of normal subgroups is $\{I\}$, $N_5$, $N_{10}$, and $G$.
    <2>6. The corresponding intermediate fields Galois over $\mathbb{Q}$ are:
    $$\mathbb{Q}, \quad \mathbb{Q}(\sqrt{5}), \quad \mathbb{Q}(\zeta_5), \quad \mathbb{Q}(\sqrt[5]{2}, \zeta_5).$$

:::

<1>4. Conclusion:
::: {.proof}
    $\operatorname{Gal}(K/\mathbb{Q}) \cong \operatorname{Aff}(\mathbb{F}_5)$, and the intermediate fields Galois over $\mathbb{Q}$ are $\mathbb{Q}$, $\mathbb{Q}(\sqrt{5})$, $\mathbb{Q}(\zeta_5)$, and $K$.
:::
:::
