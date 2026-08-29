---
schema: qual/card@1
id: P-LJURM
kind: problem
title: A polynomial with Galois group $S_3$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Polynomials
  - Permutations
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Give a polynomial with $S_3$ as its Galois group over $\mathbb{Q}$, and prove it.
:::

::: solution
**Goal:** Prove that $f(x) = x^3 - 2 \in \mathbb{Q}[x]$ has Galois group $\operatorname{Gal}(f/\mathbb{Q}) \cong S_3$.

<1>1. Choice of polynomial:
    *Proof:*
    <2>1. Let $f(x) = x^3 - 2 \in \mathbb{Q}[x]$.

<1>2. Irreducibility over $\mathbb{Q}$:
    *Proof:*
    <2>1. By Eisenstein's Criterion with prime $p = 2$: $2 \mid (-2)$, $2 \nmid 1$, and $2^2 \nmid (-2)$.
    <2>2. Thus $f(x)$ is irreducible over $\mathbb{Q}$.
    <2>3. Since $f$ is an irreducible cubic, its degree divides $|\operatorname{Gal}(f/\mathbb{Q})|$, so $3 \mid |\operatorname{Gal}(f/\mathbb{Q})|$.

<1>3. Splitting field and its degree:
    *Proof:*
    <2>1. The roots of $f(x)$ in $\mathbb{C}$ are $\alpha_1 = \sqrt[3]{2} \in \mathbb{R}$, $\alpha_2 = \sqrt[3]{2}\omega$, and $\alpha_3 = \sqrt[3]{2}\omega^2$, where $\omega = e^{2\pi i/3} = \frac{-1 + i\sqrt{3}}{2}$.
    <2>2. The splitting field is $K = \mathbb{Q}(\sqrt[3]{2}, \omega)$.
    <2>3. $[\mathbb{Q}(\sqrt[3]{2}) : \mathbb{Q}] = 3$ since $f$ is irreducible of degree 3.
    <2>4. Since $\mathbb{Q}(\sqrt[3]{2}) \subset \mathbb{R}$ and $\omega \notin \mathbb{R}$, $\omega$ has degree 2 over $\mathbb{Q}(\sqrt[3]{2})$ with minimal polynomial $x^2 + x + 1$.
    <2>5. By the tower law, $[K : \mathbb{Q}] = [K : \mathbb{Q}(\sqrt[3]{2})] \cdot [\mathbb{Q}(\sqrt[3]{2}) : \mathbb{Q}] = 2 \cdot 3 = 6$.

<1>4. Identification of the Galois group:
    *Proof:*
    <2>1. $\operatorname{Gal}(f/\mathbb{Q})$ embeds as a transitive subgroup of the symmetric group on 3 letters, $S_3$.
    <2>2. The order of the Galois group is $|\operatorname{Gal}(f/\mathbb{Q})| = [K : \mathbb{Q}] = 6$.
    <2>3. Since $|S_3| = 3! = 6$, the embedding $\operatorname{Gal}(f/\mathbb{Q}) \hookrightarrow S_3$ must be an isomorphism:
        $$\operatorname{Gal}(f/\mathbb{Q}) \cong S_3.$$

<1>5. Alternative criterion via discriminant:
    *Proof:*
    <2>1. The discriminant of $x^3 + px + q$ is $\Delta = -4p^3 - 27q^2$.
    <2>2. For $f(x) = x^3 - 2$, $p = 0$ and $q = -2$, so $\Delta = -27(-2)^2 = -108 < 0$.
    <2>3. Since $\Delta = -108$ is negative, it is not a square in $\mathbb{Q}$.
    <2>4. An irreducible cubic over $\mathbb{Q}$ has Galois group $A_3 \cong \mathbb{Z}_3$ if $\Delta$ is a square in $\mathbb{Q}$, and $S_3$ if $\Delta$ is not a square.
    <2>5. Since $-108 \notin (\mathbb{Q}^\times)^2$, $\operatorname{Gal}(f/\mathbb{Q}) \cong S_3$.

<1>6. Conclusion:
    The polynomial $f(x) = x^3 - 2$ has Galois group $S_3$ over $\mathbb{Q}$. Q.E.D.
:::
