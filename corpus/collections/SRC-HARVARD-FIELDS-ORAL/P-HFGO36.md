---
schema: qual/card@1
id: P-HFGO36
kind: problem
title: Uniqueness of the field with 27 elements
classification:
  areas: [algebra]
  topics: [Finite Fields]
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Prove that any two fields with $27 = 3^3$ elements are **isomorphic**:
$$F_1 \cong F_2 \cong \mathbb{F}_{27}.$$
:::

::: solution
**Goal:** Prove that any finite field of order $27$ is a splitting field of the polynomial $x^{27} - x$ over its prime subfield $\mathbb{F}_3$, and use uniqueness of splitting fields to establish isomorphism.

<1>1. Prime Subfield and Vector Space Dimension:
    *Proof:*
    <2>1. Let $F$ be any field with $|F| = 27 = 3^3$ elements.
    <2>2. The characteristic of $F$ must be a prime dividing 27, so $\operatorname{char}(F) = 3$.
    <2>3. The prime subfield of $F$ is isomorphic to $\mathbb{F}_3 = \mathbb{Z}/3\mathbb{Z}$.
    <2>4. $F$ is a vector space over $\mathbb{F}_3$. Since $|F| = 3^{[F : \mathbb{F}_3]} = 27 = 3^3$, the extension degree is $[F : \mathbb{F}_3] = 3$.

<1>2. Root Characterization via the Multiplicative Group:
    *Proof:*
    <2>1. The multiplicative group $F^\times = F \setminus \{0\}$ has order $|F^\times| = 27 - 1 = 26$.
    <2>2. By **Lagrange's Theorem**, every non-zero element $\alpha \in F^\times$ satisfies:
        $$\alpha^{26} = 1 \implies \alpha^{27} = \alpha.$$
    <2>3. For the zero element $0 \in F$, $0^{27} = 0$, so $0^{27} - 0 = 0$ holds as well.
    <2>4. Thus, **every element of $F$ is a root** of the polynomial:
        $$P(x) = x^{27} - x \in \mathbb{F}_3[x].$$
    <2>5. Since $\deg(P) = 27$ and $F$ contains 27 distinct elements that are roots of $P(x)$, $P(x)$ factors completely into linear factors over $F$:
        $$x^{27} - x = \prod_{\alpha \in F} (x - \alpha).$$
    <2>6. The formal derivative is $P'(x) = 27 x^{26} - 1 = 0 - 1 = -1 \ne 0$, which is coprime to $P(x)$, confirming that $P(x)$ has 27 distinct roots in any splitting field.
    <2>7. Since $F$ is generated over $\mathbb{F}_3$ by these roots ($F = \mathbb{F}_3(F)$), $F$ is a **splitting field of $x^{27} - x$ over $\mathbb{F}_3$**.

<1>3. Uniqueness of Splitting Fields:
    *Proof:*
    <2>1. Let $F_1$ and $F_2$ be any two fields with 27 elements.
    <2>2. By Step 2, both $F_1$ and $F_2$ are splitting fields of the same polynomial $x^{27} - x \in \mathbb{F}_3[x]$ over the prime subfield $\mathbb{F}_3$.
    <2>3. By the **Uniqueness Theorem for Splitting Fields**, any two splitting fields of a given polynomial over a base field are isomorphic under an isomorphism that fixes the base field:
        $$F_1 \cong F_2 \cong \mathbb{F}_{27}.$$

<1>4. Conclusion:
    Every field of order 27 is the splitting field of $x^{27} - x$ over $\mathbb{F}_3$; by uniqueness of splitting fields, all fields of order 27 are isomorphic. Q.E.D.
:::
