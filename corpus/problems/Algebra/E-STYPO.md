---
schema: qual/card@1
id: E-STYPO
kind: problem
title: Finite fields are perfect; example of an imperfect field
classification:
  areas:
  - algebra
  topics:
  - Separability
  - Fields
  - Finite Fields
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
(1) State the definition of a **perfect field**.
(2) Give an example of an **imperfect field** and exhibit an inseparable polynomial over it.
(3) Prove that every **finite field** $\mathbb{F}_q$ is perfect.
:::

::: solution
**Goal:** Define perfect fields, prove that finite fields are perfect via the Frobenius automorphism, and construct the standard imperfect field $\mathbb{F}_p(t)$.

<1>1. Definition of a Perfect Field:
    *Proof:*
    <2>1. A field $K$ is called **perfect** if every irreducible polynomial $f(x) \in K[x]$ is **separable** (has distinct roots in an algebraic closure $\bar{K}$, or equivalently $f'(x) \ne 0$).
    <2>2. **Equivalent Characterization in Characteristic $p > 0$:**
        A field $K$ of characteristic $p > 0$ is perfect if and only if the **Frobenius endomorphism**:
        $$\Phi: K \longrightarrow K, \qquad x \longmapsto x^p$$
        is **surjective** (so every element in $K$ has a $p$-th root in $K$: $K^p = K$).
    <2>3. (Every field of characteristic 0 is automatically perfect because $\deg(f') = \deg(f) - 1$, so $f' \ne 0$ for non-constant $f$).

<1>2. Proof that Every Finite Field is Perfect:
    *Proof:*
    <2>1. Let $K = \mathbb{F}_{p^n}$ be a finite field of characteristic $p$.
    <2>2. The Frobenius map $\Phi: K \to K$ given by $\Phi(x) = x^p$ is a ring homomorphism:
        $$\Phi(x + y) = (x + y)^p = x^p + y^p = \Phi(x) + \Phi(y), \qquad \Phi(x y) = x^p y^p = \Phi(x)\Phi(y).$$
    <2>3. Since $K$ is a field, every non-zero ring homomorphism is **injective**:
        $$\ker\Phi = \{x \in K \mid x^p = 0\} = \{0\}.$$
    <2>4. For any map from a **finite set** to itself, **injectivity implies surjectivity** by the Pigeonhole Principle.
    <2>5. Since $K$ is finite, $\Phi$ is **surjective**:
        $$\Phi(K) = K^p = K.$$
    <2>6. Thus every element $a \in K$ has a $p$-th root $b \in K$ such that $b^p = a$.
    <2>7. Therefore, every finite field is **perfect**.

<1>3. Example of an Imperfect Field:
    *Proof:*
    <2>1. Let $K = \mathbb{F}_p(t)$ be the rational function field in one indeterminate $t$ over $\mathbb{F}_p$.
    <2>2. The image of the Frobenius map on $K$ is:
        $$K^p = \mathbb{F}_p(t^p) \subsetneq \mathbb{F}_p(t) = K.$$
    <2>3. In particular, the element $t \in K$ is **not a $p$-th power** in $K$ ($t \notin K^p$).
    <2>4. Consider the polynomial $f(x) = x^p - t \in K[x]$.
        - $f(x)$ is **irreducible** in $K[x]$ by Eisenstein's Criterion applied to the prime ideal $(t)$ in $\mathbb{F}_p[t]$.
        - Its formal derivative is $f'(x) = p x^{p-1} = 0$.
        - In an algebraic closure $\bar{K}$, let $\alpha = t^{1/p}$. Then $f(x) = x^p - \alpha^p = (x - \alpha)^p$.
        - Thus $f(x)$ has only $1$ root $\alpha$ with multiplicity $p \ge 2$, meaning $f(x)$ is **inseparable**.
    <2>5. Thus $K = \mathbb{F}_p(t)$ is **imperfect**.

<1>4. Conclusion:
    Finite fields are perfect because Frobenius is injective on a finite set, hence surjective ($K^p = K$); $\mathbb{F}_p(t)$ is imperfect with inseparable polynomial $x^p - t$. Q.E.D.
:::
