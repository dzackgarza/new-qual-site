---
schema: qual/card@1
id: P-YELFJ
kind: problem
title: An ideal maximal among annihilators of nonzero elements of an $R$-module is
  prime
classification:
  areas:
  - algebra
  topics:
  - Modules
  - Prime Ideals
  - Ideals
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: {.problem}
Let $R$ be a commutative ring and let $M$ be an $R$-module.
Recall that for $\mu \in M$, the *annihilator* of $\mu$ is the set:
$$\operatorname{Ann}(\mu) = \{ r \in R \mid r \mu = 0 \}.$$

Suppose that $I$ is an ideal in $R$ which is maximal among the set of annihilators of non-zero elements of $M$ (i.e. $I = \operatorname{Ann}(\mu)$ for some $\mu \in M \setminus \{0\}$, and if $\operatorname{Ann}(\nu) \supsetneq I$ for some $\nu \ne 0$, no such $\nu$ exists).

Prove that $I$ is a **prime** ideal in $R$.
:::

::: solution
**Goal:** Prove that an ideal $I = \operatorname{Ann}(\mu)$ maximal among annihilators of non-zero elements in $M$ is prime (such primes are called *associated primes* $\mathfrak{p} \in \operatorname{Ass}(M)$).

<1>1. Setting and Properness of $I$:
    *Proof:*
    <2>1. Let $I = \operatorname{Ann}(\mu)$ with $\mu \in M$ and $\mu \ne 0$.
    <2>2. Since $\mu \ne 0$, $1 \cdot \mu = \mu \ne 0$, so $1 \notin I$.
    <2>3. Thus $I \subsetneq R$ is a **proper ideal**.

<1>2. Prime Ideal Property ($ab \in I \implies a \in I \text{ or } b \in I$):
    *Proof:*
    <2>1. Let $a, b \in R$ such that $a b \in I = \operatorname{Ann}(\mu)$.
    <2>2. By definition of the annihilator, $a b \in \operatorname{Ann}(\mu) \implies (ab)\mu = 0$.
    <2>3. By module associativity, $a(b \mu) = 0$.
    <2>4. Suppose that $b \notin I$. We must prove that $a \in I$.
    <2>5. Since $b \notin I = \operatorname{Ann}(\mu)$, $b \mu \ne 0 \in M$.
    <2>6. Consider the element $\nu \coloneqq b \mu \in M \setminus \{0\}$.
    <2>7. We examine its annihilator $\operatorname{Ann}(\nu) = \operatorname{Ann}(b \mu)$:
        - If $r \in I = \operatorname{Ann}(\mu)$, then $r \mu = 0 \implies r(b \mu) = b(r \mu) = b(0) = 0$.
        - Thus $r \in \operatorname{Ann}(b \mu) = \operatorname{Ann}(\nu)$.
        - This proves the ideal containment:
            $$I \subseteq \operatorname{Ann}(b \mu) = \operatorname{Ann}(\nu).$$
    <2>8. By hypothesis, $I$ is **maximal** in the family $\{\operatorname{Ann}(m) \mid m \in M \setminus \{0\}\}$.
    <2>9. Since $\nu = b \mu \ne 0$, $\operatorname{Ann}(\nu)$ belongs to this family.
    <2>10. By maximality of $I$ in this family, the inclusion $I \subseteq \operatorname{Ann}(\nu)$ must be an **equality**:
        $$I = \operatorname{Ann}(\nu) = \operatorname{Ann}(b \mu).$$
    <2>11. Now, from Step <2>3, we know that $a (b \mu) = 0$, which means:
        $$a \in \operatorname{Ann}(b \mu).$$
    <2>12. Since $\operatorname{Ann}(b \mu) = I$, we conclude:
        $$a \in I.$$

<1>3. Conclusion:
    Whenever $ab \in I$ and $b \notin I$, we have $a \in I$. Therefore, $I$ is a prime ideal in $R$. Q.E.D.
:::
