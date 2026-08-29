---
schema: qual/card@1
id: P-A4HRU
kind: problem
title: Image $pA$ and kernel $A[p]$ of multiplication by $p$
classification:
  areas:
  - algebra
  topics:
  - Modules
  - Homomorphisms
  - Torsion
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Let $A$ be an $R$-module (or abelian group), and let $p \in R$ be a ring element (e.g. a prime integer $p \in \mathbb{Z}$).
Define the multiplication-by-$p$ map:
$$\phi_p: A \longrightarrow A, \qquad x \longmapsto p x.$$
(1) Prove that $\phi_p$ is an $R$-module homomorphism when $p \in Z(R)$.
(2) Define the image submodule $p A \coloneqq \operatorname{im}(\phi_p)$ and the kernel submodule $A[p] \coloneqq \ker(\phi_p)$ ($p$-torsion submodule).
(3) Compute $p A$, $A/pA$, and $A[p]$ for $A = \mathbb{Z}$, $A = \mathbb{Z}/n\mathbb{Z}$, and $A = \mathbb{Q}/\mathbb{Z}$.
:::

::: solution
**Goal:** Define and analyze the multiplication-by-$p$ endomorphism $\phi_p$, its image $pA$, kernel $A[p]$, and quotient $A/pA$.

<1>1. Homomorphism Verification:
    *Proof:*
    <2>1. Let $p \in Z(R)$ (or $R$ commutative). For all $x, y \in A$ and $r \in R$:
        $$\phi_p(x + y) = p(x + y) = p x + p y = \phi_p(x) + \phi_p(y),$$
        $$\phi_p(r x) = p(r x) = (p r) x = (r p) x = r(p x) = r \phi_p(x).$$
    <2>2. Thus $\phi_p \in \operatorname{End}_R(A)$ is an $R$-module endomorphism.

<1>2. Submodule Definitions:
    *Proof:*
    <2>1. The **image** of $\phi_p$ is the $p$-multiple submodule:
        $$p A \coloneqq \operatorname{im}(\phi_p) = \{p x \mid x \in A\}.$$
    <2>2. The **kernel** of $\phi_p$ is the $p$-torsion (or $p$-annihilator) submodule:
        $$A[p] \coloneqq \ker(\phi_p) = \{a \in A \mid p a = 0\} = \operatorname{Ann}_A(p).$$
    <2>3. By the First Isomorphism Theorem for modules:
        $$A / A[p] \cong p A.$$

<1>3. Concrete Computations for Abelian Groups ($R = \mathbb{Z}$, $p$ a prime):
    *Proof:*
    <2>1. **Case 1: $A = \mathbb{Z}$ (Free Abelian Group):**
        - $\phi_p(x) = p x$ is injective since $\mathbb{Z}$ has no torsion.
        - $A[p] = \ker(\phi_p) = \{0\}$.
        - $p A = p \mathbb{Z}$.
        - Quotient $A / p A = \mathbb{Z} / p \mathbb{Z} \cong \mathbb{F}_p$ (a 1-dimensional $\mathbb{F}_p$-vector space).
    <2>2. **Case 2: $A = \mathbb{Z}/n\mathbb{Z}$ (Finite Cyclic Group):**
        - Let $d = \gcd(p, n)$.
        - $p A = p(\mathbb{Z}/n\mathbb{Z}) \cong \mathbb{Z}/\frac{n}{d}\mathbb{Z}$ of order $n/d$.
        - $A / p A \cong \mathbb{Z}/d\mathbb{Z}$.
        - $A[p] = \{x \in \mathbb{Z}/n\mathbb{Z} \mid p x \equiv 0 \pmod n\} = \langle n/d \rangle \cong \mathbb{Z}/d\mathbb{Z}$.
        - In particular, if $p \mid n$, then $A[p] \cong \mathbb{Z}_p$ and $A/pA \cong \mathbb{Z}_p$; if $p \nmid n$, then $A[p] = 0$ and $p A = A$.
    <2>3. **Case 3: $A = \mathbb{Q}/\mathbb{Z}$ (Divisible Torsion Group):**
        - Since $\mathbb{Q}$ is divisible, for every $x \in \mathbb{Q}/\mathbb{Z}$, $x = p(x/p)$, so $\phi_p$ is **surjective**:
          $$p(\mathbb{Q}/\mathbb{Z}) = \mathbb{Q}/\mathbb{Z} \implies A / p A = 0.$$
        - The $p$-torsion is:
          $$A[p] = \left\{ \frac{a}{b} + \mathbb{Z} \;\middle|\; p \frac{a}{b} \in \mathbb{Z} \right\} = \left\{ 0, \frac{1}{p}, \frac{2}{p}, \dots, \frac{p-1}{p} \right\} + \mathbb{Z} \cong \mathbb{Z}_p.$$

<1>4. Exact Sequence Structure:
    *Proof:*
    <2>1. For every module $A$, there is a canonical 4-term exact sequence:
        $$0 \longrightarrow A[p] \longrightarrow A \xrightarrow{\cdot p} A \longrightarrow A/pA \longrightarrow 0.$$

<1>5. Conclusion:
    Multiplication by $p$ yields the $p$-torsion submodule $A[p]$ as kernel and $pA$ as image, relating $A/pA \cong pA$ when $A$ is torsion-free. Q.E.D.
:::
