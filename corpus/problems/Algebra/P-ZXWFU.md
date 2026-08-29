---
schema: qual/card@1
id: P-ZXWFU
kind: problem
title: Maximal real subfield of $\QQ(\zeta_n)$
classification:
  areas:
  - algebra
  topics:
  - Roots of Unity
  - Field Extensions
  - Galois Theory
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
What is the maximal real subfield in a cyclotomic extension $\mathbb{Q}(\zeta_n)/\mathbb{Q}$?
:::

::: solution
**Goal:** Determine the maximal real subfield $K^+ = \mathbb{Q}(\zeta_n) \cap \mathbb{R}$ of the cyclotomic field $K = \mathbb{Q}(\zeta_n)$, its degree over $\mathbb{Q}$, its Galois group, and explicit generators.

<1>1. Complex conjugation in the Galois group:
    *Proof:*
    <2>1. The cyclotomic extension $K = \mathbb{Q}(\zeta_n)$ is an abelian Galois extension of $\mathbb{Q}$ with Galois group $\operatorname{Gal}(K/\mathbb{Q}) \cong (\mathbb{Z}/n\mathbb{Z})^\times$.
    <2>2. The automorphism $\sigma_a \in \operatorname{Gal}(K/\mathbb{Q})$ acts by $\sigma_a(\zeta_n) = \zeta_n^a$ for $\gcd(a, n) = 1$.
    <2>3. Complex conjugation $c: z \mapsto \overline{z}$ restricts to an automorphism of $K$ because $\overline{\zeta_n} = \zeta_n^{-1} = \zeta_n^{n-1} \in K$.
    <2>4. Thus $c = \sigma_{-1} = \sigma_{n-1} \in \operatorname{Gal}(K/\mathbb{Q})$.

<1>2. Fixed field of complex conjugation:
    *Proof:*
    <2>1. An element $\alpha \in K$ is real ($\alpha \in \mathbb{R}$) if and only if $\overline{\alpha} = \alpha$, which means $c(\alpha) = \alpha$.
    <2>2. Thus, the maximal real subfield of $K$ is precisely the fixed field under complex conjugation:
        $$K^+ = K^{\langle c \rangle} = \mathbb{Q}(\zeta_n)^{\langle \sigma_{-1} \rangle} = \mathbb{Q}(\zeta_n) \cap \mathbb{R}.$$

<1>3. Degree and Galois group of $K^+$:
    *Proof:*
    <2>1. For $n \ge 3$, $\zeta_n \notin \mathbb{R}$, so $c \ne \operatorname{id}_K$ and the subgroup $H = \langle c \rangle = \{\operatorname{id}, c\}$ has order 2.
    <2>2. By the Fundamental Theorem of Galois Theory:
        $$[K : K^+] = |H| = 2, \qquad [K^+ : \mathbb{Q}] = \frac{[K : \mathbb{Q}]}{2} = \frac{\varphi(n)}{2}.$$
    <2>3. Since $\operatorname{Gal}(K/\mathbb{Q})$ is abelian, all subgroups are normal, so $K^+/\mathbb{Q}$ is Galois with group:
        $$\operatorname{Gal}(K^+/\mathbb{Q}) \cong (\mathbb{Z}/n\mathbb{Z})^\times / \{ \pm 1\}.$$

<1>4. Explicit generators:
    *Proof:*
    <2>1. The element $\zeta_n + \zeta_n^{-1} = \zeta_n + \overline{\zeta_n} = 2\cos\left(\frac{2\pi}{n}\right)$ is fixed by complex conjugation, hence lies in $K^+$.
    <2>2. The extension $K^+(\zeta_n) = K$ satisfies $[\mathbb{Q}(\zeta_n) : \mathbb{Q}(\zeta_n + \zeta_n^{-1})] \le 2$ because $\zeta_n$ satisfies the quadratic $x^2 - (\zeta_n + \zeta_n^{-1})x + 1 = 0$.
    <2>3. Since $[K : K^+] = 2$, this forces:
        $$K^+ = \mathbb{Q}\left(\zeta_n + \zeta_n^{-1}\right) = \mathbb{Q}\left(2\cos\frac{2\pi}{n}\right) = \mathbb{Q}\left(\cos\frac{2\pi}{n}\right).$$

<1>5. Conclusion:
    The maximal real subfield of $\mathbb{Q}(\zeta_n)$ is $\mathbb{Q}(\zeta_n + \zeta_n^{-1}) = \mathbb{Q}(\cos(2\pi/n))$, of degree $\varphi(n)/2$ over $\mathbb{Q}$ (for $n \ge 3$), with Galois group $(\mathbb{Z}/n\mathbb{Z})^\times / \{\pm 1\}$. Q.E.D.
:::
