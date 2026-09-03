---
schema: qual/card@1
id: E-AMD-IDVVQWVQ
kind: problem
title: Every prime ideal is radical
classification:
  areas:
  - algebra
  topics:
  - Prime Ideals
  - Ideals
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}
Show that every prime ideal is radical.
:::

::: solution
**Goal:** Prove that for any prime ideal $\mathfrak{p}$ of a commutative ring $R$, the radical satisfies $\sqrt{\mathfrak{p}} = \mathfrak{p}$.

<1>1. Trivial inclusion $\mathfrak{p} \subseteq \sqrt{\mathfrak{p}}$:
    *Proof:*
    <2>1. By definition, $\sqrt{\mathfrak{p}} = \{x \in R \mid \exists n \ge 1, \, x^n \in \mathfrak{p}\}$.
    <2>2. For any $x \in \mathfrak{p}$, taking $n = 1$ gives $x^1 = x \in \mathfrak{p}$.
    <2>3. Thus $\mathfrak{p} \subseteq \sqrt{\mathfrak{p}}$.

<1>2. Reverse inclusion $\sqrt{\mathfrak{p}} \subseteq \mathfrak{p}$ via prime property:
    *Proof:*
    <2>1. Let $x \in \sqrt{\mathfrak{p}}$, so $x^n \in \mathfrak{p}$ for some integer $n \ge 1$.
    <2>2. We prove $x \in \mathfrak{p}$ by induction on $n$:
        - **Base case ($n = 1$):** $x^1 = x \in \mathfrak{p}$.
        - **Inductive step ($n > 1$):** Assume that for any $y \in R$, $y^k \in \mathfrak{p}$ with $1 \le k < n$ implies $y \in \mathfrak{p}$.
          Write $x^n = x \cdot x^{n-1} \in \mathfrak{p}$.
          Since $\mathfrak{p}$ is a prime ideal, $ab \in \mathfrak{p} \implies a \in \mathfrak{p} \text{ or } b \in \mathfrak{p}$.
          Applying this with $a = x$ and $b = x^{n-1}$:
          Either $x \in \mathfrak{p}$, or $x^{n-1} \in \mathfrak{p}$.
          If $x^{n-1} \in \mathfrak{p}$, the induction hypothesis gives $x \in \mathfrak{p}$.
    <2>3. In either case, $x \in \mathfrak{p}$.
    <2>4. Thus $\sqrt{\mathfrak{p}} \subseteq \mathfrak{p}$.

<1>3. Quotient characterization (alternative proof):
    *Proof:*
    <2>1. An ideal $I \subseteq R$ is radical if and only if the quotient ring $R/I$ is reduced (contains no non-zero nilpotent elements).
    <2>2. Because $\mathfrak{p}$ is prime, the quotient ring $R/\mathfrak{p}$ is an integral domain.
    <2>3. An integral domain contains no non-zero zero divisors, hence no non-zero nilpotents: if $\bar{x}^n = 0$, then $\bar{x} = 0$.
    <2>4. Thus $R/\mathfrak{p}$ is reduced, which implies $\mathfrak{p}$ is radical.

<1>4. Conclusion:
    $\sqrt{\mathfrak{p}} = \mathfrak{p}$, so every prime ideal is radical. Q.E.D.
:::
