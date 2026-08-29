---
schema: qual/card@1
id: E-AMD-J3YZ5TXF
kind: exercise
title: The Galois group of $x^n - 2$ over $\QQ$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Splitting Fields
  - Roots of Unity
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}
The splitting field of $x^n-2$ over $\mathbb{Q}$ is $\mathbb{Q}(2^{1/n}, \zeta_n)$.
Show that the Galois group embeds into the affine group $\mathbb{Z}/n\mathbb{Z} \rtimes (\mathbb{Z}/n\mathbb{Z})^\times$ by $\sigma \mapsto (a,b)$, where $\sigma(2^{1/n}) = \zeta_n^a 2^{1/n}$ and $\sigma(\zeta_n) = \zeta_n^b$.

Deduce that it is dihedral of order $2n$ exactly when $\varphi(n) = 2$, that is for $n = 3, 4, 6$, and not for general $n$.
:::

::: solution
**Goal:** Prove that $\operatorname{Gal}(\mathbb{Q}(2^{1/n}, \zeta_n)/\mathbb{Q})$ embeds into the affine group $\operatorname{Aff}(\mathbb{Z}/n\mathbb{Z}) = \mathbb{Z}/n\mathbb{Z} \rtimes (\mathbb{Z}/n\mathbb{Z})^\times$, and determine all $n$ for which the Galois group is dihedral of order $2n$.

<1>1. Embedding into the affine group:
    *Proof:*
    <2>1. The roots of $x^n - 2$ are $\zeta_n^k 2^{1/n}$ for $k \in \mathbb{Z}/n\mathbb{Z}$.
    <2>2. Any $\mathbb{Q}$-automorphism $\sigma \in G = \operatorname{Gal}(K/\mathbb{Q})$ must send $2^{1/n}$ to a root of $x^n - 2$ and $\zeta_n$ to a primitive $n$-th root of unity:
        $$\sigma(2^{1/n}) = \zeta_n^a 2^{1/n} \quad (a \in \mathbb{Z}/n\mathbb{Z}), \qquad \sigma(\zeta_n) = \zeta_n^b \quad (b \in (\mathbb{Z}/n\mathbb{Z})^\times).$$
    <2>3. For two automorphisms $\sigma_1 \leftrightarrow (a_1, b_1)$ and $\sigma_2 \leftrightarrow (a_2, b_2)$, their composition evaluates as:
        $$\sigma_1(\sigma_2(2^{1/n})) = \sigma_1(\zeta_n^{a_2} 2^{1/n}) = (\zeta_n^{b_1})^{a_2} (\zeta_n^{a_1} 2^{1/n}) = \zeta_n^{a_1 + b_1 a_2} 2^{1/n},$$
        $$\sigma_1(\sigma_2(\zeta_n)) = \sigma_1(\zeta_n^{b_2}) = \zeta_n^{b_1 b_2}.$$
    <2>4. The map $\sigma \mapsto (a, b)$ preserves the semidirect product group law $(a_1, b_1) \cdot (a_2, b_2) = (a_1 + b_1 a_2, b_1 b_2)$ of $\mathbb{Z}/n\mathbb{Z} \rtimes (\mathbb{Z}/n\mathbb{Z})^\times$.
    <2>5. Since $2^{1/n}$ and $\zeta_n$ generate $K$ over $\mathbb{Q}$, $\sigma$ is uniquely determined by $(a, b)$, so this is an injective homomorphism.

<1>2. Order of the Galois group:
    *Proof:*
    <2>1. $x^n - 2$ is irreducible over $\mathbb{Q}$ by Eisenstein's criterion at $p = 2$, so $[\mathbb{Q}(2^{1/n}) : \mathbb{Q}] = n$.
    <2>2. The cyclotomic extension has degree $[\mathbb{Q}(\zeta_n) : \mathbb{Q}] = \varphi(n)$.
    <2>3. The full splitting field degree is $[K : \mathbb{Q}] = n \varphi(n)$.
    <2>4. Thus the Galois group has order $2n$ if and only if $\varphi(n) = 2$.

<1>3. Characterization of dihedral structure:
    *Proof:*
    <2>1. The dihedral group $D_n$ of order $2n$ has the presentation $\mathbb{Z}/n\mathbb{Z} \rtimes \{1, -1\}$, where the non-trivial element acts by inversion $a \mapsto -a$.
    <2>2. When $\varphi(n) = 2$, the unit group $(\mathbb{Z}/n\mathbb{Z})^\times$ has order $2$, so $(\mathbb{Z}/n\mathbb{Z})^\times = \{1, -1\}$.
    <2>3. In this case, the affine group itself is $\mathbb{Z}/n\mathbb{Z} \rtimes \{1, -1\} \cong D_n$, and since $|G| = n \varphi(n) = 2n$, the embedding is an isomorphism $G \cong D_n$.
    <2>4. Solving Euler's totient equation $\varphi(n) = 2$:
        - For prime powers $p^k$: $\varphi(p^k) = p^{k-1}(p-1) = 2 \implies p = 3, k = 1$ ($n = 3$) or $p = 2, k = 2$ ($n = 4$).
        - For composite $n = 2 \cdot 3 = 6$: $\varphi(6) = \varphi(2)\varphi(3) = 1 \cdot 2 = 2$.
        - No other integer satisfies $\varphi(n) = 2$.
    <2>5. Hence $\varphi(n) = 2 \iff n \in \{3, 4, 6\}$.

<1>4. Conclusion:
    The Galois group embeds into $\mathbb{Z}/n\mathbb{Z} \rtimes (\mathbb{Z}/n\mathbb{Z})^\times$ and is isomorphic to the dihedral group $D_n$ if and only if $n \in \{3, 4, 6\}$. Q.E.D.
:::
