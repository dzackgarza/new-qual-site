---
schema: qual/card@1
id: P-73LXN
kind: problem
title: Galois group of $x^p-2$ over $\QQ$ for odd primes $p$
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
  by: gemini-3.7-flash
  date: 2026-08-16
---

::: problem
- Identify all of the elements of the Galois group of $x^p-2$ for $p$ an odd prime (note: this has a complicated presentation).
:::

::: {.solution}
**Goal:** Let $p$ be an odd prime.
Determine the Galois group $G = \operatorname{Gal}(K/\mathbb{Q})$ of the polynomial $f(x) = x^p - 2 \in \mathbb{Q}[x]$ over $\mathbb{Q}$, explicit actions of its elements, and its group structure / presentation.

<1>1. Determination of the roots and the splitting field $K$: <2>1. The roots of $f(x) = x^p - 2$ in $\mathbb{C}$ are $\alpha_k = \sqrt[p]{2} \zeta_p^k$ for $k \in \{0, 1, \dots, p-1\}$, where $\sqrt[p]{2}$ is the real positive $p$-th root of $2$ and $\zeta_p = e^{2\pi i / p}$ is a primitive $p$-th root of unity.
Proof: $(\sqrt[p]{2}\zeta_p^k)^p = (\sqrt[p]{2})^p (\zeta_p^p)^k = 2 \cdot 1 = 2$.
Since these $p$ numbers are distinct, they form all roots of $f(x)$.
<2>2. The splitting field of $f(x)$ over $\mathbb{Q}$ is $K = \mathbb{Q}(\sqrt[p]{2}, \zeta_p)$.
Proof: Any field containing all roots $\alpha_k$ must contain $\alpha_0 = \sqrt[p]{2}$ and $\alpha_1/\alpha_0 = \zeta_p$.
Conversely, $\mathbb{Q}(\sqrt[p]{2}, \zeta_p)$ contains each $\alpha_k = \sqrt[p]{2}\zeta_p^k$.

<1>2. Degree of the extension $[K : \mathbb{Q}]$: <2>1. $f(x) = x^p - 2$ is irreducible over $\mathbb{Q}$ by Eisenstein's Criterion at the prime 2. Proof: $2$ divides the constant term $-2$, $2$ does not divide the leading coefficient $1$, and $2^2 = 4$ does not divide $-2$.
<2>2. $[\mathbb{Q}(\sqrt[p]{2}) : \mathbb{Q}] = p$.
Proof: Since $f(x)$ is monic and irreducible over $\mathbb{Q}$ with root $\sqrt[p]{2}$, $[\mathbb{Q}(\sqrt[p]{2}) : \mathbb{Q}] = \deg(f) = p$.
<2>3. The minimal polynomial of $\zeta_p$ over $\mathbb{Q}$ is the cyclotomic polynomial $\Phi_p(x) = x^{p-1} + x^{p-2} + \dots + 1$, which is irreducible over $\mathbb{Q}$, so $[\mathbb{Q}(\zeta_p) : \mathbb{Q}] = p - 1$.
Proof: Standard property of the $p$-th cyclotomic polynomial for prime $p$.
<2>4. The extension degrees $[\mathbb{Q}(\sqrt[p]{2}) : \mathbb{Q}] = p$ and $[\mathbb{Q}(\zeta_p) : \mathbb{Q}] = p - 1$ are coprime, so $[K : \mathbb{Q}] = p(p-1)$.
Proof: $\gcd(p, p-1) = 1$.
The degree of the compositum of two extensions of coprime degrees with intersection $\mathbb{Q}$ is the product of their degrees: $[K : \mathbb{Q}] = [\mathbb{Q}(\sqrt[p]{2}, \zeta_p) : \mathbb{Q}] = p(p-1)$.
<2>5. $|G| = |\operatorname{Gal}(K/\mathbb{Q})| = [K : \mathbb{Q}] = p(p-1)$.
Proof: $K/\mathbb{Q}$ is Galois as it is the splitting field of the separable polynomial $x^p - 2$ in characteristic 0.

<1>3. Identification of the elements of $G$: <2>1. Any $\sigma \in G$ is uniquely determined by its action on the generators $\sqrt[p]{2}$ and $\zeta_p$.
Proof: $K = \mathbb{Q}(\sqrt[p]{2}, \zeta_p)$, so an automorphism is determined by where it sends the field generators.
<2>2. For any $\sigma \in G$, $\sigma(\sqrt[p]{2}) \in \{\sqrt[p]{2}\zeta_p^a \mid a \in \mathbb{Z}/p\mathbb{Z}\}$ and $\sigma(\zeta_p) \in \{\zeta_p^b \mid b \in (\mathbb{Z}/p\mathbb{Z})^\times\}$.
Proof: $\sigma$ must map a root of $x^p - 2$ to another root of $x^p - 2$, so $\sigma(\sqrt[p]{2}) = \sqrt[p]{2}\zeta_p^a$ for some $a \in \{0, 1, \dots, p-1\}$.
Similarly, $\sigma$ must map the primitive root $\zeta_p$ to another primitive $p$-th root of unity $\zeta_p^b$ for some $b \in \{1, 2, \dots, p-1\}$.
<2>3. There are exactly $p(p-1)$ distinct pairs $(a, b) \in \mathbb{Z}/p\mathbb{Z} \times (\mathbb{Z}/p\mathbb{Z})^\times$.
Proof: $|\mathbb{Z}/p\mathbb{Z}| = p$ and $|(\mathbb{Z}/p\mathbb{Z})^\times| = p-1$.
<2>4. Every such pair corresponds to a valid automorphism $\sigma_{a, b} \in G$.
Proof: Since $|G| = p(p-1)$ by <1>2.<2>5 and no two distinct pairs can define the same automorphism on the generators, each of the $p(p-1)$ pairs $(a, b)$ defines a unique element $\sigma_{a,b} \in G$ defined by: $$\sigma_{a, b}(\sqrt[p]{2}) = \sqrt[p]{2}\zeta_p^a, \quad \sigma_{a, b}(\zeta_p) = \zeta_p^b.$$

<1>4. Group composition law and algebraic structure: <2>1. For $\sigma_{a_1, b_1}, \sigma_{a_2, b_2} \in G$, the composition satisfies $\sigma_{a_1, b_1} \circ \sigma_{a_2, b_2} = \sigma_{a_1 + b_1 a_2, b_1 b_2}$.
<3>1. Action on $\zeta_p$: $$(\sigma_{a_1, b_1} \circ \sigma_{a_2, b_2})(\zeta_p) = \sigma_{a_1, b_1}(\zeta_p^{b_2}) = (\sigma_{a_1, b_1}(\zeta_p))^{b_2} = (\zeta_p^{b_1})^{b_2} = \zeta_p^{b_1 b_2}.$$ Proof: Direct computation using field homomorphism properties.
<3>2. Action on $\sqrt[p]{2}$: $$(\sigma_{a_1, b_1} \circ \sigma_{a_2, b_2})(\sqrt[p]{2}) = \sigma_{a_1, b_1}(\sqrt[p]{2}\zeta_p^{a_2}) = \sigma_{a_1, b_1}(\sqrt[p]{2}) \cdot \sigma_{a_1, b_1}(\zeta_p)^{a_2} = (\sqrt[p]{2}\zeta_p^{a_1}) \cdot (\zeta_p^{b_1})^{a_2} = \sqrt[p]{2} \zeta_p^{a_1 + b_1 a_2}.$$ Proof: Direct computation using field homomorphism properties.
<3>3. Q.E.D. Proof: Matches the definition of $\sigma_{a_1 + b_1 a_2, b_1 b_2}$.
<2>2. $G$ is isomorphic to the affine group $\operatorname{Aff}(\mathbb{F}_p) \cong \mathbb{Z}/p\mathbb{Z} \rtimes (\mathbb{Z}/p\mathbb{Z})^\times$, or equivalently the subgroup of upper triangular matrices $\left\{\begin{pmatrix} b & a \\ 0 & 1 \end{pmatrix} \;\middle|\; a \in \mathbb{F}_p, b \in \mathbb{F}_p^\times\right\} \le \operatorname{GL}_2(\mathbb{F}_p)$.
Proof: The map $\sigma_{a, b} \mapsto \begin{pmatrix} b & a \\ 0 & 1 \end{pmatrix}$ is an isomorphism because $\begin{pmatrix} b_1 & a_1 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} b_2 & a_2 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} b_1 b_2 & a_1 + b_1 a_2 \\ 0 & 1 \end{pmatrix}$, precisely matching <2>1. <2>3. Generators and Presentation: Let $\tau = \sigma_{1, 1}$ (translation $\tau(\sqrt[p]{2}) = \sqrt[p]{2}\zeta_p, \tau(\zeta_p) = \zeta_p$) and let $\omega = \sigma_{0, g}$ where $g$ is a primitive root modulo $p$ (scaling $\omega(\sqrt[p]{2}) = \sqrt[p]{2}, \omega(\zeta_p) = \zeta_p^g$). Then $\tau$ has order $p$, $\omega$ has order $p-1$, and $\omega \tau \omega^{-1} = \tau^g$.
Thus, $G$ has presentation: $$G = \langle \tau, \omega \mid \tau^p = 1, \; \omega^{p-1} = 1, \; \omega \tau \omega^{-1} = \tau^g \rangle.$$ Proof: $\tau^k = \sigma_{k, 1}$ gives the normal cyclic subgroup of order $p$, $\omega^j = \sigma_{0, g^j}$ gives a cyclic complement of order $p-1$, and conjugation is $\omega \tau \omega^{-1} = \sigma_{0, g} \sigma_{1, 1} \sigma_{0, g^{-1}} = \sigma_{g, g} \sigma_{0, g^{-1}} = \sigma_{g, 1} = \tau^g$.
:::
