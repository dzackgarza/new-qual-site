---
schema: qual/card@1
id: P-MMAQ-FJ4DDF5GZK
kind: problem
title: The Galois module $K$ is the regular representation, and cyclic Kummer generators
classification:
  areas:
  - algebra
  topics:
  - Representation Theory
  - Galois Theory
  - Fields
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: problem
Let $K/F$ be a finite Galois extension and let $n=[K:F]$. There is a theorem
(often referred to as the "normal basis theorem") which states that there
exists an irreducible polynomial $f(x)\in F[x]$ whose
roots form a basis for $K$ as a vector space over $F$. You may assume
that theorem in this problem.

-   Let $G=\Gal(K/F)$. The action of $G$ on $K$ makes $K$ into
    a finite-dimensional representation space for $G$ over $F$.
    Prove that $K$ is isomorphic to the regular representation
    for $G$ over $F$.

    > The regular representation is defined by letting $G$ act
    > on the group algebra $F[G]$ by multiplication on
    > the left.

-   Suppose that the Galois group $G$ is cyclic and that $F$
    contains a primitive $n^{\text{th}}$ root of unity. Show that
    there exists an injective homomorphism $\chi:G\rightarrow
    F^{\times}$.

-   Show that $K$ contains a non-zero element $a$ with the
    following property:
    `\begin{align*}
    g(a)=\chi(g)\cdot a
    .\end{align*}`{=tex}

    for all $g\in G$.

-   If $a$ has the property stated in (c), show that $K=F(a)$ and
    that $a^n\in F^{\times}$.
:::

::: {.solution}
<1>1. Part (a): $K \cong F[G]$ as $F[G]$-modules (regular representation):
<2>1. By the Normal Basis Theorem, there exists an element $\alpha \in K$ such that $\{g(\alpha) : g \in G\}$ is an $F$-basis for $K$.
Proof: Normal Basis Theorem for finite Galois extensions.
<2>2. Define the $F$-linear map $\Phi: F[G] \to K$ by $\Phi\left(\sum_{g \in G} c_g g\right) = \sum_{g \in G} c_g g(\alpha)$.
Proof: definition of $\Phi$.
<2>3. For any $h \in G$:
\[
\Phi\left(h \cdot \sum_{g \in G} c_g g\right) = \Phi\left(\sum_{g \in G} c_g (hg)\right) = \sum_{g \in G} c_g (hg)(\alpha) = h\left(\sum_{g \in G} c_g g(\alpha)\right) = h \cdot \Phi\left(\sum_{g \in G} c_g g\right).
\]
Thus $\Phi$ is a homomorphism of $F[G]$-modules.
Proof: $G$-action on $K$ is by field automorphisms.
<2>4. Since $\Phi$ sends the standard basis $\{g : g \in G\}$ of $F[G]$ to the basis $\{g(\alpha) : g \in G\}$ of $K$, $\Phi$ is an isomorphism of $F[G]$-modules.
Proof: a linear map sending a basis to a basis is an isomorphism.

<1>2. Part (b): Injective homomorphism $\chi: G \to F^\times$:
<2>1. Let $G = \langle \sigma \rangle \cong \mathbb{Z}_n$, and let $\zeta_n \in F$ be a primitive $n$-th root of unity.
Proof: setup.
<2>2. Define $\chi: G \to F^\times$ by $\chi(\sigma^k) = \zeta_n^k$ for all $k \in \mathbb{Z}$.
Proof: definition of $\chi$.
<2>3. Since $\chi(\sigma^n) = \zeta_n^n = 1$, $\chi$ is a well-defined group homomorphism.
Proof: universal property of cyclic groups.
<2>4. $\ker(\chi) = \{\sigma^k : \zeta_n^k = 1\} = \{\sigma^k : n \mid k\} = \{1\}$.
Thus $\chi$ is injective.
Proof: $\zeta_n$ has multiplicative order $n$.

<1>3. Part (c): Existence of an eigenvector $a \in K^\times$ for the $G$-action:
<2>1. Consider the Lagrange resolvent map $L: K \to K$ defined by:
\[
L(x) = \sum_{j=0}^{n-1} \chi(\sigma^j)^{-1} \sigma^j(x) = \sum_{j=0}^{n-1} \zeta_n^{-j} \sigma^j(x).
\]
Proof: definition of Lagrange resolvent.
<2>2. By Dedekind’s Theorem on the linear independence of distinct field automorphisms, the linear combination $\sum_{j=0}^{n-1} \zeta_n^{-j} \sigma^j$ is not identically zero on $K$.
Proof: Dedekind's Theorem.
<2>3. Thus there exists some $x \in K$ such that $a = L(x) \neq 0$.
Proof: <2>2.
<2>4. Compute $\sigma(a)$:
\[
\sigma(a) = \sum_{j=0}^{n-1} \zeta_n^{-j} \sigma^{j+1}(x) = \zeta_n \sum_{j=0}^{n-1} \zeta_n^{-(j+1)} \sigma^{j+1}(x) = \zeta_n L(x) = \zeta_n a = \chi(\sigma) a.
\]
Proof: re-indexing the sum modulo $n$ using $\zeta_n^{-n} = 1$ and $\sigma^n = \operatorname{id}$.
<2>5. By induction, $\sigma^k(a) = \chi(\sigma^k) a$ for all $k$, so $g(a) = \chi(g) a$ for all $g \in G$.
Proof: $g = \sigma^k$.

<1>4. Part (d): Show $K = F(a)$ and $a^n \in F^\times$:
<2>1. Compute $\sigma(a^n) = (\sigma(a))^n = (\zeta_n a)^n = \zeta_n^n a^n = a^n$.
Proof: field automorphism property $\sigma(a^n) = (\sigma(a))^n$.
<2>2. Since $\sigma$ generates $G$, $g(a^n) = a^n$ for all $g \in G$.
By Galois theory, $a^n \in K^G = F$. Since $a \neq 0$, $a^n \in F^\times$.
Proof: Fundamental Theorem of Galois Theory ($K^G = F$).
<2>3. Compute the stabilizer $\operatorname{Stab}_G(a) = \{g \in G : g(a) = a\}$:
If $g \in \operatorname{Stab}_G(a)$, then $\chi(g) a = a \implies (\chi(g) - 1)a = 0 \implies \chi(g) = 1$ since $a \neq 0$.
By injectivity of $\chi$ from Part (b), $g = 1$.
Proof: <1>2 and <1>3.
<2>4. By the Galois correspondence, $[K : F(a)] = |\operatorname{Stab}_G(a)| = 1$, so $K = F(a)$.
Proof: Galois correspondence.

<1>5. Conclusion:
$K \cong F[G]$ as regular representation, $\chi$ is an injective character, $a$ exists via Lagrange resolvents, and $K = F(a)$ with $a^n \in F^\times$. Q.E.D.
Proof: <1>1 through <1>4.
:::
