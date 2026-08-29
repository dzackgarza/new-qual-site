---
schema: qual/card@1
id: P-GKPVE
kind: problem
title: $K(u)/K$ is not Galois and $\Aut(K(u)/K)$ is trivial for a single root of an
  irreducible of degree $n$
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Field Extensions
  - Automorphisms
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Let $K$ be a field of characteristic 0 (or separable), and let $f(x) \in K[x]$ be an irreducible polynomial of degree $n \ge 3$ such that $f(x)$ has exactly one real root $u \in \mathbb{R}$ and $n - 1$ non-real complex roots.
(1) Prove that the extension degree $[K(u) : K] = n$.
(2) Prove that $K(u)/K$ is not a Galois extension.
(3) Prove that the automorphism group $\operatorname{Aut}(K(u)/K)$ is trivial ($\operatorname{Aut}(K(u)/K) = \{\operatorname{id}\}$).
:::

::: solution
**Goal:** Prove $[K(u) : K] = n$, that $K(u)/K$ is not Galois, and that $\operatorname{Aut}(K(u)/K) = \{\operatorname{id}\}$ when $K(u)$ contains only one root of the irreducible polynomial $f(x)$.

<1>1. Extension Degree $[K(u) : K] = n$:
    *Proof:*
    <2>1. Since $f(x) \in K[x]$ is monic (without loss of generality) and irreducible with $f(u) = 0$, $f(x)$ is the **minimal polynomial** of $u$ over $K$:
        $$m_{u, K}(x) = f(x).$$
    <2>2. By standard field theory:
        $$[K(u) : K] = \deg(m_{u, K}) = \deg(f) = n.$$

<1>2. Proof that $K(u)/K$ is Not Galois:
    *Proof:*
    <2>1. In characteristic 0, every algebraic extension is separable.
    <2>2. An algebraic extension is **Galois** if and only if it is normal (i.e. it is the splitting field of the minimal polynomial $f(x)$ of its generator).
    <2>3. Since $f(x)$ has $n \ge 3$ roots but only $u \in \mathbb{R}$ is real, the remaining $n - 1 \ge 2$ roots $\alpha_2, \dots, \alpha_n \in \mathbb{C} \setminus \mathbb{R}$ are non-real complex numbers.
    <2>4. Since $K \subseteq \mathbb{R}$ and $u \in \mathbb{R}$, the field $K(u) \subset \mathbb{R}$ is a **purely real field**.
    <2>5. Consequently, none of the non-real roots $\alpha_2, \dots, \alpha_n$ can belong to $K(u)$.
    <2>6. Thus $f(x)$ does not split into linear factors over $K(u)$.
    <2>7. Therefore, $K(u)/K$ is **not a normal extension**, so it is **not Galois**.

<1>3. Proof that $\operatorname{Aut}(K(u)/K) = \{\operatorname{id}\}$:
    *Proof:*
    <2>1. Let $\sigma \in \operatorname{Aut}(K(u)/K)$ be any $K$-automorphism of $K(u)$.
    <2>2. Since $f(u) = 0$ and $\sigma$ fixes $K$ pointwise:
        $$f(\sigma(u)) = \sigma(f(u)) = \sigma(0) = 0.$$
    <2>3. Therefore, $\sigma(u)$ must be a root of $f(x)$ that lies in $K(u)$.
    <2>4. By Step <1>2, $u$ is the **unique root** of $f(x)$ in $K(u)$ (since all other roots are non-real, whereas $K(u) \subset \mathbb{R}$).
    <2>5. This forces:
        $$\sigma(u) = u.$$
    <2>6. Since $K(u)$ is generated over $K$ by $u$, an automorphism that fixes both $K$ and $u$ fixes every element of $K(u)$:
        $$\sigma = \operatorname{id}_{K(u)}.$$
    <2>7. Thus $\operatorname{Aut}(K(u)/K) = \{\operatorname{id}\}$.

<1>4. Conclusion:
    $[K(u) : K] = n$, $K(u)/K$ is non-normal (hence not Galois), and its automorphism group is trivial because only one root lies in the real subfield. Q.E.D.
:::
