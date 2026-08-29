---
schema: qual/card@1
id: P-5AMY7
kind: problem
title: Irreducible polynomials of degrees 7 and 14 over $\FF_p$
classification:
  areas:
  - algebra
  topics:
  - Finite Fields
  - Irreducibility Criteria
  - Polynomials
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Can you have a degree 7 irreducible polynomial over $\mathbb{F}_p$? How about a degree 14 irreducible polynomial?
:::

::: solution
**Goal:** Prove that for any prime $p$ and any positive integer $n \ge 1$ (specifically $n = 7$ and $n = 14$), there exist irreducible polynomials of degree $n$ over $\mathbb{F}_p$, and compute their exact counts.

<1>1. General existence of degree $n$ irreducible polynomials over $\mathbb{F}_p$:
    *Proof:*
    <2>1. For any prime $p$ and positive integer $n \ge 1$, there exists a unique (up to isomorphism) finite field $\mathbb{F}_{p^n}$ with $p^n$ elements.
    <2>2. The extension $\mathbb{F}_{p^n}/\mathbb{F}_p$ is finite, normal, and separable (Galois) of degree $[\mathbb{F}_{p^n} : \mathbb{F}_p] = n$.
    <2>3. The multiplicative group $\mathbb{F}_{p^n}^\times$ is cyclic of order $p^n - 1$.
    <2>4. Let $\gamma \in \mathbb{F}_{p^n}^\times$ be a generator (a primitive element of $\mathbb{F}_{p^n}$).
    <2>5. Then $\mathbb{F}_p(\gamma) = \mathbb{F}_{p^n}$, which means the minimal polynomial $m_\gamma(x) \in \mathbb{F}_p[x]$ of $\gamma$ over $\mathbb{F}_p$ has degree:
        $$\deg(m_\gamma) = [\mathbb{F}_p(\gamma) : \mathbb{F}_p] = [\mathbb{F}_{p^n} : \mathbb{F}_p] = n.$$
    <2>6. By definition, $m_\gamma(x)$ is monic and irreducible in $\mathbb{F}_p[x]$ of degree $n$.
    <2>7. Thus irreducible polynomials of degree $n$ exist for **every** $n \ge 1$, including $n = 7$ and $n = 14$.

<1>2. Exact count of monic irreducibles of degree $n$ (Gauss formula):
    *Proof:*
    <2>1. The polynomial $x^{p^n} - x$ is the product of all monic irreducible polynomials in $\mathbb{F}_p[x]$ whose degrees divide $n$:
        $$x^{p^n} - x = \prod_{d \mid n} \prod_{f \in \mathcal{I}_d} f(x),$$
        where $\mathcal{I}_d$ is the set of monic irreducible polynomials of degree $d$.
    <2>2. Taking degrees:
        $$p^n = \sum_{d \mid n} d N_p(d)$$
        where $N_p(d) = |\mathcal{I}_d|$ is the number of monic irreducible polynomials of degree $d$.
    <2>3. By Möbius inversion:
        $$N_p(n) = \frac{1}{n} \sum_{d \mid n} \mu\left(\frac{n}{d}\right) p^d.$$

<1>3. Case $n = 7$:
    *Proof:*
    <2>1. Divisors of 7 are 1 and 7.
    <2>2. Using the formula:
        $$N_p(7) = \frac{1}{7} \left( \mu(1) p^7 + \mu(7) p^1 \right) = \frac{p^7 - p}{7}.$$
    <2>3. Since $p \ge 2$, $N_p(7) \ge \frac{2^7 - 2}{7} = \frac{126}{7} = 18 > 0$.
    <2>4. Thus there exist $\frac{p^7-p}{7}$ monic irreducible polynomials of degree 7 over $\mathbb{F}_p$.

<1>4. Case $n = 14$:
    *Proof:*
    <2>1. Divisors of 14 are 1, 2, 7, 14 with Möbius values $\mu(1)=1, \mu(2)=-1, \mu(7)=-1, \mu(14)=1$.
    <2>2. Using the formula:
        $$N_p(14) = \frac{1}{14} \left( p^{14} - p^7 - p^2 + p \right).$$
    <2>3. Since $p^{14} > p^7 + p^2$, $N_p(14) \ge \frac{2^{14} - 2^7 - 2^2 + 2}{14} = \frac{16384 - 128 - 4 + 2}{14} = \frac{16254}{14} = 1161 > 0$.
    <2>4. Thus there exist $\frac{p^{14} - p^7 - p^2 + p}{14}$ monic irreducible polynomials of degree 14 over $\mathbb{F}_p$.

<1>5. Conclusion:
    Yes, irreducible polynomials of degree 7 and degree 14 exist over $\mathbb{F}_p$ for every prime $p$. Q.E.D.
:::
