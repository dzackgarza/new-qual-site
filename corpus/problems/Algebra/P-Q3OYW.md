---
schema: qual/card@1
id: P-Q3OYW
kind: problem
title: Are there separable polynomials of any degree over any field?
classification:
  areas:
  - algebra
  topics:
  - Separability
  - Polynomials
  - Fields
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Are there separable polynomials of any degree $n \ge 1$ over any field $F$?
What about irreducible separable polynomials?
:::

::: solution
**Goal:** Prove that separable polynomials of every degree $n \ge 1$ exist over every field $F$, and analyze the existence of irreducible separable polynomials.

<1>1. General Separable Polynomials of any Degree $n \ge 1$:
    *Proof:*
    <2>1. A polynomial $f(x) \in F[x]$ is **separable** if its roots in an algebraic closure $\overline{F}$ are all distinct (i.e. $\gcd(f, f') = 1$).
    <2>2. **Case A: $F$ is an infinite field:**
        - Choose $n$ distinct elements $c_1, c_2, \dots, c_n \in F$ (which exist because $|F| = \infty$).
        - Define $f(x) = (x - c_1)(x - c_2) \cdots (x - c_n) \in F[x]$.
        - The roots of $f$ in $\overline{F}$ are $\{c_1, \dots, c_n\}$, which are $n$ pairwise distinct elements in $F$.
        - Thus $f(x)$ is a separable polynomial of degree $n$.
    <2>3. **Case B: $F$ is a finite field $\mathbb{F}_q$ ($q = p^k$):**
        - **Option 1 (Factor into distinct linear factors over an extension):**
            Let $f(x) = x^{q^n} - x$. This has $q^n$ distinct roots (all elements of $\mathbb{F}_{q^n}$).
            More directly, for any $n \ge 1$, there exists a finite field extension $\mathbb{F}_{q^n}$ of degree $n$ over $\mathbb{F}_q$.
            The extension $\mathbb{F}_{q^n}/\mathbb{F}_q$ is simple and separable, so by the Primitive Element Theorem, there exists a primitive element $\alpha \in \mathbb{F}_{q^n}$ such that $\mathbb{F}_{q^n} = \mathbb{F}_q(\alpha)$.
            The minimal polynomial $m_\alpha(x) \in \mathbb{F}_q[x]$ is monic, irreducible, and separable of degree $n$.
        - **Option 2 (Square-free linear combinations):** For any $n \ge 1$, $x^n - c$ for suitable $c \in F^\times$ or products of distinct irreducible factors from $x^{q^n}-x$ give separable polynomials.
    <2>4. Thus, separable polynomials of every degree $n \ge 1$ exist over **every** field $F$.

<1>2. Existence of Irreducible Separable Polynomials:
    *Proof:*
    <2>1. **For finite fields:** As shown in Case B, for every $n \ge 1$, the field extension $\mathbb{F}_{p^n}/\mathbb{F}_p$ is cyclic and Galois, possessing an irreducible separable polynomial of degree $n$ (the minimal polynomial of a primitive generator).
    <2>2. **For characteristic 0 fields:** Every irreducible polynomial over a field of characteristic 0 is separable. Over $\mathbb{Q}$, Eisenstein polynomials $x^n - 2$ are irreducible and separable of degree $n$ for all $n \ge 1$.
    <2>3. **For algebraically closed fields:** If $F = \overline{F}$, the only irreducible polynomials are linear (degree 1). So irreducible polynomials of degree $n \ge 2$ do not exist. But separable (reducible) polynomials $(x - c_1)\cdots(x - c_n)$ exist for all $n$.
    <2>4. **For general fields:** Every field $F$ admits separable polynomials of every degree $n \ge 1$.

<1>3. Conclusion:
    Yes, for every field $F$ and every positive integer $n \ge 1$, there exist separable polynomials of degree $n$ in $F[x]$. Q.E.D.
:::
