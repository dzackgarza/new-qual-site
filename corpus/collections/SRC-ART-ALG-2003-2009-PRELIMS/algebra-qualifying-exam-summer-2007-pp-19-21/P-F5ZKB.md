---
schema: qual/card@1
id: P-F5ZKB
kind: problem
title: A finite field has $p^n$ elements; subfields of a field of size $3^{12}$; an
  infinite field of characteristic $3$
classification:
  areas:
  - algebra
  topics:
  - Finite Fields
  - Fields
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: problem
a. Show that a finite field must have exactly $p^n$ elements for some prime $p$ and some positive integer $n$.

b. List all the subfields of the field of size $3^{12}$.

c. Give an example of an infinite field of characteristic $3$.
:::

::: solution
**Goal:** Prove that finite fields have prime-power cardinality, determine all subfields of $\mathbb{F}_{3^{12}}$, and provide an explicit example of an infinite field of characteristic $3$.

<1>1. Part (a): Any finite field $F$ has cardinality $|F| = p^n$ for a prime $p$ and integer $n \ge 1$.
    *Proof:*
    <2>1. The characteristic $\operatorname{char}(F)$ of any field $F$ is either $0$ or a prime $p$. If $\operatorname{char}(F) = 0$, the prime subfield is isomorphic to $\mathbb{Q}$, which is infinite, contradicting the finiteness of $F$. Thus $\operatorname{char}(F) = p$ for some prime $p$.
    <2>2. The prime subfield of $F$ is $K_0 \cong \mathbb{F}_p = \mathbb{Z}/p\mathbb{Z}$.
    <2>3. $F$ is a vector space over its prime subfield $\mathbb{F}_p$ under field addition and scalar multiplication by elements of $\mathbb{F}_p$.
    <2>4. Since $F$ is finite, $F$ is finite-dimensional as an $\mathbb{F}_p$-vector space. Let $n = \dim_{\mathbb{F}_p}(F) \ge 1$.
    <2>5. Any $n$-dimensional vector space over $\mathbb{F}_p$ is isomorphic to $\mathbb{F}_p^n$ as an $\mathbb{F}_p$-vector space, hence has cardinality $|\mathbb{F}_p|^n = p^n$.

<1>2. Part (b): Subfields of $\mathbb{F}_{3^{12}}$.
    *Proof:*
    <2>1. For a finite field $\mathbb{F}_{p^m}$, every subfield is a finite field containing $\mathbb{F}_p$, so its degree $d$ over $\mathbb{F}_p$ must divide $m = [\mathbb{F}_{p^m} : \mathbb{F}_p]$ by the tower law.
    <2>2. Conversely, for each positive divisor $d \mid m$, the polynomial $x^{p^d} - x$ divides $x^{p^m} - x$ in $\mathbb{F}_p[x]$, and the roots of $x^{p^d} - x$ in $\mathbb{F}_{p^m}$ form the unique subfield of size $p^d$, isomorphic to $\mathbb{F}_{p^d}$.
    <2>3. Here $p = 3$ and $m = 12$. The positive divisors of $12$ are $d \in \{1, 2, 3, 4, 6, 12\}$.
    <2>4. Therefore, the subfields of $\mathbb{F}_{3^{12}}$ are precisely the six subfields isomorphic to:
        $$\mathbb{F}_3, \quad \mathbb{F}_{3^2} = \mathbb{F}_9, \quad \mathbb{F}_{3^3} = \mathbb{F}_{27}, \quad \mathbb{F}_{3^4} = \mathbb{F}_{81}, \quad \mathbb{F}_{3^6} = \mathbb{F}_{729}, \quad \mathbb{F}_{3^{12}} = \mathbb{F}_{531441}.$$

<1>3. Part (c): Example of an infinite field of characteristic $3$.
    *Proof:*
    <2>1. Consider the field of rational functions in one indeterminate $t$ over $\mathbb{F}_3$:
        $$K = \mathbb{F}_3(t) = \left\{ \frac{f(t)}{g(t)} : f(t), g(t) \in \mathbb{F}_3[t], \; g(t) \neq 0 \right\}.$$
    <2>2. $K$ is the field of fractions of the polynomial ring $\mathbb{F}_3[t]$, which is an integral domain, so $K$ is a field.
    <2>3. The characteristic of $K$ is $3$, since $1_K + 1_K + 1_K = 3 \cdot 1_{\mathbb{F}_3} = 0$.
    <2>4. $K$ contains the monomials $\{t^k : k \in \mathbb{N}\}$, which are pairwise distinct in $\mathbb{F}_3[t] \subset K$, so $K$ is infinite.
    *(Alternatively, the algebraic closure $\overline{\mathbb{F}}_3 = \bigcup_{n=1}^\infty \mathbb{F}_{3^n}$ is also an infinite field of characteristic $3$.)* Q.E.D.
:::
