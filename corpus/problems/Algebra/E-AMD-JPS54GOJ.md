---
schema: qual/card@1
id: E-AMD-JPS54GOJ
kind: exercise
title: Unique subfield of order $p^d$ in a field with $p^n$ elements
classification:
  areas:
  - algebra
  topics:
  - Finite Fields
  - Field Extensions
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}
Show that a field with $p^n$ elements has exactly one subfield of size $p^d$ for every $d$ dividing $n$.
:::

::: solution
**Goal:** Prove that $\mathbb{F}_{p^n}$ has a unique subfield of order $p^d$ for each $d \mid n$, and no others.

<1>1. Existence via fixed field of Frobenius power:
    *Proof:*
    <2>1. The Frobenius endomorphism $\varphi: x \mapsto x^p$ generates $\operatorname{Gal}(\mathbb{F}_{p^n}/\mathbb{F}_p) \cong \mathbb{Z}/n\mathbb{Z}$.
    <2>2. For $d \mid n$, the subgroup $\langle \varphi^d \rangle$ has order $n/d$ and index $d$.
    <2>3. By the Galois correspondence, the fixed field $\mathbb{F}_{p^n}^{\langle \varphi^d \rangle} = \{x \in \mathbb{F}_{p^n} \mid x^{p^d} = x\}$ is a subfield of degree $d$ over $\mathbb{F}_p$.
    <2>4. This fixed field has order $p^d$ and is the splitting field of $x^{p^d} - x$ inside $\mathbb{F}_{p^n}$.

<1>2. Uniqueness:
    *Proof:*
    <2>1. Any subfield $K \le \mathbb{F}_{p^n}$ of order $p^d$ is a copy of $\mathbb{F}_{p^d}$, and its elements are exactly the roots of $x^{p^d} - x$ in $\mathbb{F}_{p^n}$.
    <2>2. The polynomial $x^{p^d} - x$ has at most $p^d$ roots in any field, and the $p^d$ elements of $K$ are all roots.
    <2>3. Thus $K = \{x \in \mathbb{F}_{p^n} \mid x^{p^d} = x\}$ is uniquely determined.

<1>3. Necessity of $d \mid n$:
    *Proof:*
    <2>1. If $K \le \mathbb{F}_{p^n}$ is a subfield of order $p^d$, then $\mathbb{F}_{p^n}$ is a vector space over $K$.
    <2>2. Thus $p^n = (p^d)^{[\mathbb{F}_{p^n} : K]}$, which forces $d \mid n$.
    <2>3. Conversely, for $d \mid n$, $x^{p^d} - x$ divides $x^{p^n} - x$ (since $d \mid n \implies (p^d - 1) \mid (p^n - 1)$), so all roots of $x^{p^d} - x$ lie in $\mathbb{F}_{p^n}$.

<1>4. Conclusion:
    The subfields of $\mathbb{F}_{p^n}$ are exactly $\{\mathbb{F}_{p^d} \mid d \divides n\}$, one for each divisor of $n$. Q.E.D.
:::
