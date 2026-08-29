---
schema: qual/card@1
id: P-RMRPT
kind: problem
title: Characters of the multiplicative group of a finite field
classification:
  areas:
  - algebra
  topics:
  - Character Theory
  - Finite Fields
  - Cyclic Groups
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
What are the group characters of the multiplicative group of a finite field $\mathbb{F}_q^\times$?
:::

::: solution
**Goal:** Determine all group characters (multiplicative characters) of the multiplicative group $\mathbb{F}_q^\times$ for a finite field with $q = p^n$ elements.

<1>1. Structure of the multiplicative group $\mathbb{F}_q^\times$:
    *Proof:*
    <2>1. The multiplicative group $\mathbb{F}_q^\times = \mathbb{F}_q \setminus \{0\}$ is a cyclic group of order $q - 1$.
    <2>2. Let $g \in \mathbb{F}_q^\times$ be a generator (a primitive element of $\mathbb{F}_q$).
    <2>3. Then $\mathbb{F}_q^\times = \langle g \rangle = \{1, g, g^2, \dots, g^{q-2}\} \cong \mathbb{Z}/(q-1)\mathbb{Z}$.

<1>2. Definition of a group character:
    *Proof:*
    <2>1. A (complex) group character of $\mathbb{F}_q^\times$ is a group homomorphism:
        $$\chi: \mathbb{F}_q^\times \to \mathbb{C}^\times.$$
    <2>2. Since every element $x \in \mathbb{F}_q^\times$ satisfies $x^{q-1} = 1$, we have:
        $$(\chi(x))^{q-1} = \chi(x^{q-1}) = \chi(1) = 1.$$
    <2>3. Thus, the image of $\chi$ is contained in the group of $(q-1)$-th roots of unity $\mu_{q-1} = \{e^{2\pi i k / (q-1)} \mid 0 \le k < q-1\} \subset \mathbb{C}^\times$.

<1>3. Classification of all characters:
    *Proof:*
    <2>1. A homomorphism $\chi$ from the cyclic group $\langle g \rangle$ is completely determined by its value on the generator $g$.
    <2>2. The value $\chi(g)$ must be a $(q-1)$-th root of unity.
    <2>3. For each integer $k \in \{0, 1, \dots, q-2\}$, define the character $\chi_k: \mathbb{F}_q^\times \to \mathbb{C}^\times$ by:
        $$\chi_k(g^m) = e^{2\pi i k m / (q-1)} = \omega^{km}, \qquad \text{where } \omega = e^{2\pi i / (q-1)}.$$
    <2>4. Each $\chi_k$ is a well-defined group homomorphism: $\chi_k(g^a g^b) = \chi_k(g^{a+b}) = \omega^{k(a+b)} = \omega^{ka}\omega^{kb} = \chi_k(g^a)\chi_k(g^b)$.
    <2>5. Distinct values of $k \in \{0, 1, \dots, q-2\}$ give distinct characters because $\chi_k(g) = \omega^k$.

<1>4. Character group structure:
    *Proof:*
    <2>1. The set of all characters $\widehat{\mathbb{F}_q^\times} = \operatorname{Hom}(\mathbb{F}_q^\times, \mathbb{C}^\times)$ forms a group under pointwise multiplication $(\chi \psi)(x) = \chi(x)\psi(x)$.
    <2>2. Since $\chi_k \chi_j = \chi_{k+j \pmod{q-1}}$, the character group is cyclic of order $q-1$:
        $$\widehat{\mathbb{F}_q^\times} = \langle \chi_1 \rangle \cong \mathbb{Z}/(q-1)\mathbb{Z} \cong \mathbb{F}_q^\times.$$
    <2>3. The character $\chi_0$ is the **trivial (principal) character** $\chi_0(x) = 1$ for all $x$.
    <2>4. When extended to all of $\mathbb{F}_q$, these are the **Dirichlet characters** on $\mathbb{F}_q$ (setting $\chi(0) = 0$ for non-trivial characters and $\chi_0(0) = 1$).
    <2>5. For $q$ odd, the unique character of order 2 is the **quadratic character** (Legendre symbol on $\mathbb{F}_q$), $\chi_{(q-1)/2}(x) = +1$ if $x$ is a square and $-1$ if not.

<1>5. Conclusion:
    There are exactly $q-1$ characters, given by $\chi_k(g^m) = e^{2\pi i k m / (q-1)}$ for $k = 0, 1, \dots, q-2$, forming a cyclic group isomorphic to $\mathbb{F}_q^\times$. Q.E.D.
:::
