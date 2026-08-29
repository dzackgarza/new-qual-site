---
schema: qual/card@1
id: E-AMD-FCSNELC6
kind: exercise
title: $\GF(p^d)\leq\GF(p^n)$ iff $d$ divides $n$
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
Show that $\mathbb{F}_{p^d} \le \mathbb{F}_{p^n} \iff d \mid n$.
:::

::: solution
**Goal:** Prove that for any prime $p$ and positive integers $d, n$, the finite field $\mathbb{F}_{p^d}$ is isomorphic to a subfield of $\mathbb{F}_{p^n}$ if and only if $d$ divides $n$.

<1>1. Forward implication ($\implies$):
    *Proof:*
    <2>1. Assume $\mathbb{F}_{p^d}$ is a subfield of $\mathbb{F}_{p^n}$.
    <2>2. Then $\mathbb{F}_{p^n}$ is a finite-dimensional vector space over $\mathbb{F}_{p^d}$ of dimension $k = [\mathbb{F}_{p^n} : \mathbb{F}_{p^d}]$.
    <2>3. By the Tower Law for field extensions over the prime subfield $\mathbb{F}_p$:
        $$[\mathbb{F}_{p^n} : \mathbb{F}_p] = [\mathbb{F}_{p^n} : \mathbb{F}_{p^d}] \cdot [\mathbb{F}_{p^d} : \mathbb{F}_p].$$
    <2>4. Substituting $[\mathbb{F}_{p^n} : \mathbb{F}_p] = n$ and $[\mathbb{F}_{p^d} : \mathbb{F}_p] = d$ gives $n = k \cdot d$.
    <2>5. Therefore $d \mid n$.

<1>2. Reverse implication ($\impliedby$):
    *Proof:*
    <2>1. Assume $d \mid n$, so $n = d k$ for some positive integer $k$.
    <2>2. For $a = p^d \ge 2$, the algebraic identity $a^k - 1 = (a - 1)(a^{k-1} + \dots + 1)$ implies:
        $$(p^d - 1) \mid (p^n - 1).$$
    <2>3. Let $p^n - 1 = m (p^d - 1)$. In $\mathbb{F}_p[x]$, the polynomial identity $y^m - 1 = (y - 1)(y^{m-1} + \dots + 1)$ with $y = x^{p^d - 1}$ implies:
        $$(x^{p^d - 1} - 1) \mid (x^{p^n - 1} - 1).$$
    <2>4. Multiplying both polynomials by $x$ yields:
        $$(x^{p^d} - x) \mid (x^{p^n} - x).$$
    <2>5. The field $\mathbb{F}_{p^n}$ consists of the $p^n$ distinct roots of $x^{p^n} - x = 0$ in the algebraic closure $\overline{\mathbb{F}}_p$.
    <2>6. Because $(x^{p^d} - x)$ divides $(x^{p^n} - x)$, every root of $x^{p^d} - x = 0$ is a root of $x^{p^n} - x = 0$.
    <2>7. Thus the set of roots $\mathbb{F}_{p^d}$ is a subfield of $\mathbb{F}_{p^n}$, i.e., $\mathbb{F}_{p^d} \le \mathbb{F}_{p^n}$.

<1>3. Conclusion:
    $\mathbb{F}_{p^d} \le \mathbb{F}_{p^n} \iff d \mid n$. Q.E.D.
:::
