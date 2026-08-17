---
schema: qual/card@1
id: E-AMD-2QM6SJIQ
kind: exercise
title: Compute the Galois group of $x^n - 1 \in \QQ[x]$ as a function of $n$.
classification:
  areas:
  - algebra
  topics:
  - galois-theory
  - roots-of-unity
  - abelian-groups
relations: []
review: draft
solved: true
---

::: {.exercise}
Compute the Galois group of $x^n - 1 \in \QQ[x]$ as a function of $n$.
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

Let $K$ be the splitting field of $f(x) = x^n - 1$ over $\QQ$.

1. **Roots and Splitting Field:** The roots of $x^n - 1$ in $\CC$ are the $n$-th roots of unity:
   $$
   \mu_n = \left\{ \zeta_n^k \;\middle|\; k = 0, 1, \ldots, n-1 \right\}, \qquad \text{where } \zeta_n = e^{2\pi i / n}.
   $$
   Since every root is a power of the primitive $n$-th root of unity $\zeta_n$, the splitting field is the **cyclotomic field**:
   $$
   K = \QQ(\zeta_n).
   $$

2. **Action of Automorphisms on Primitive Roots:** Let $\sigma \in \Gal(\QQ(\zeta_n)/\QQ)$.
   Since $\sigma$ fixes $\QQ$, $\sigma(\zeta_n)$ must also be a root of $x^n - 1$ of order $n$, i.e. another primitive $n$-th root of unity:
   $$
   \sigma(\zeta_n) = \zeta_n^a \quad \text{for some } a \in (\ZZ/n\ZZ)^\times = \{a \in \{1, \ldots, n\} : \gcd(a, n) = 1\}.
   $$
   An automorphism $\sigma \in \Gal(\QQ(\zeta_n)/\QQ)$ is completely determined by the integer $a \bmod n$, because $\sigma(\zeta_n^k) = (\sigma(\zeta_n))^k = \zeta_n^{ak}$.

3. **Isomorphism with the Group of Units $(\ZZ/n\ZZ)^\times$:** Define the map:
   $$
   \Phi: \Gal(\QQ(\zeta_n)/\QQ) \longrightarrow (\ZZ/n\ZZ)^\times, \qquad \sigma \longmapsto a \bmod n \quad \text{where } \sigma(\zeta_n) = \zeta_n^a.
   $$

   - **Homomorphism:** If $\tau(\zeta_n) = \zeta_n^b$, then $(\sigma \circ \tau)(\zeta_n) = \sigma(\zeta_n^b) = (\zeta_n^a)^b = \zeta_n^{ab}$, so $\Phi(\sigma \circ \tau) = ab \bmod n = \Phi(\sigma)\Phi(\tau)$.

   - **Injectivity:** If $\Phi(\sigma) = 1$, then $\sigma(\zeta_n) = \zeta_n$, which implies $\sigma = \operatorname{id}$.

   - **Surjectivity (Irreducibility of Cyclotomic Polynomials):** The minimal polynomial of $\zeta_n$ over $\QQ$ is the $n$-th cyclotomic polynomial $\Phi_n(x)$, which is irreducible over $\QQ$ and has degree $\deg \Phi_n = \phi(n)$ (Euler's totient function).
     Therefore:
     $$
     [\QQ(\zeta_n) : \QQ] = \phi(n) = |(\ZZ/n\ZZ)^\times|.
     $$
     Since $|\Gal(\QQ(\zeta_n)/\QQ)| = [\QQ(\zeta_n) : \QQ] = \phi(n) = |(\ZZ/n\ZZ)^\times|$, the injective homomorphism $\Phi$ is an isomorphism.

4. **Conclusion:** For any integer $n \geq 1$:
   $$
   \Gal(\QQ(\zeta_n)/\QQ) \cong (\ZZ/n\ZZ)^\times.
   $$
   This is an abelian group of order $\phi(n)$.
:::
