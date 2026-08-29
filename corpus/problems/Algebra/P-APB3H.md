---
schema: qual/card@1
id: P-APB3H
kind: problem
title: Frobenius of $\FF_{p^n}/\FF_p$ and its characteristic polynomial
classification:
  areas:
  - algebra
  topics:
  - Finite Fields
  - Minimal and Characteristic Polynomials
  - Galois Theory
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Let $K = \mathbb{F}_{p^n}$ be the finite field extension of degree $n$ over $F = \mathbb{F}_p$.
(1) What is the Frobenius endomorphism $\operatorname{Frob}_p: K \to K$, and how does it generate the Galois group $\operatorname{Gal}(K/F)$?
(2) Viewed as an $\mathbb{F}_p$-linear transformation $T: K \to K$ on the $n$-dimensional vector space $K \cong \mathbb{F}_p^n$, what are its minimal and characteristic polynomials?
:::

::: solution
**Goal:** Define the Frobenius automorphism on $\mathbb{F}_{p^n}/\mathbb{F}_p$ and compute its characteristic and minimal polynomials as an $\mathbb{F}_p$-linear operator.

<1>1. Definition and Galois Action of the Frobenius Endomorphism:
    *Proof:*
    <2>1. The **Frobenius map** $\sigma = \operatorname{Frob}_p: \mathbb{F}_{p^n} \to \mathbb{F}_{p^n}$ is defined by:
        $$\sigma(x) = x^p \quad \text{for } x \in \mathbb{F}_{p^n}.$$
    <2>2. **Field automorphism:**
        - By the Freshman's Dream (characteristic $p$), $(x + y)^p = x^p + y^p$.
        - $(xy)^p = x^p y^p$ and $1^p = 1$.
        - Because $\mathbb{F}_{p^n}$ is finite, the injective map $\sigma$ is a field automorphism.
    <2>3. **Fixed field:** By Fermat's Little Theorem, $\sigma(x) = x \iff x^p - x = 0 \iff x \in \mathbb{F}_p$.
    <2>4. **Galois generator:** $\sigma^k(x) = x^{p^k}$. The smallest positive integer $k$ such that $\sigma^k = \operatorname{id}$ is $k = n$ (since $x^{p^n} = x$ for all $x \in \mathbb{F}_{p^n}$).
    <2>5. Thus $\operatorname{Gal}(\mathbb{F}_{p^n}/\mathbb{F}_p) = \langle \sigma \rangle \cong \mathbb{Z}_n$ is cyclic of order $n$.

<1>2. Frobenius as an $\mathbb{F}_p$-Linear Transformation $T$:
    *Proof:*
    <2>1. Because $\sigma(c x + y) = c^p x^p + y^p = c x^p + y^p = c \sigma(x) + \sigma(y)$ for all $c \in \mathbb{F}_p$, $\sigma$ is an $\mathbb{F}_p$-linear operator $T \in \operatorname{End}_{\mathbb{F}_p}(\mathbb{F}_{p^n})$.
    <2>2. Since $\dim_{\mathbb{F}_p}(\mathbb{F}_{p^n}) = n$, the characteristic polynomial $\chi_T(x) = \det(x I - T) \in \mathbb{F}_p[x]$ has degree $n$.

<1>3. Minimal and Characteristic Polynomials:
    *Proof:*
    <2>1. **Minimal polynomial:**
        - The operator identity $\sigma^n = \operatorname{id}$ implies that the minimal polynomial $\mu_T(x)$ divides $x^n - 1$.
        - By the **Normal Basis Theorem**, there exists an element $\alpha \in \mathbb{F}_{p^n}$ such that $\{\alpha, \sigma(\alpha), \sigma^2(\alpha), \dots, \sigma^{n-1}(\alpha)\}$ forms a basis for $\mathbb{F}_{p^n}$ over $\mathbb{F}_p$.
        - Therefore, $\alpha$ is a cyclic vector for $T = \sigma$, meaning the $T$-annihilator of $\alpha$ is of degree $n$.
        - Thus the minimal polynomial must have degree $n$, which forces:
            $$\mu_T(x) = x^n - 1.$$
    <2>2. **Characteristic polynomial:**
        - Since $\deg(\mu_T) = n = \dim(\mathbb{F}_{p^n})$, the characteristic polynomial must coincide with the minimal polynomial:
            $$\chi_T(x) = x^n - 1.$$

<1>4. Conclusion:
    $\operatorname{Frob}_p(x) = x^p$ generates $\operatorname{Gal}(\mathbb{F}_{p^n}/\mathbb{F}_p) \cong \mathbb{Z}_n$, and its characteristic and minimal polynomials as an $\mathbb{F}_p$-linear operator are both $\chi_T(x) = \mu_T(x) = x^n - 1$. Q.E.D.
:::
