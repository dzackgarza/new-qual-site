---
schema: qual/card@1
id: E-AMD-GLBUESVX
kind: exercise
title: $x^{p^n}-x$ is the product of monic irreducibles in $\FF_p[x]$ of degree dividing
  $n$
classification:
  areas:
  - algebra
  topics:
  - Finite Fields
  - Irreducibility Criteria
  - Factorization
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}
Prove that $x^{p^n}-x$ is the product of all monic irreducible polynomials in $\mathbb{F}_p[x]$ with degree dividing $n$.
:::

::: solution
**Goal:** Prove the identity in $\mathbb{F}_p[x]$:
$$x^{p^n} - x = \prod_{d \mid n} \prod_{\substack{f \in \mathbb{F}_p[x] \text{ monic, irreducible} \\ \deg(f) = d}} f(x).$$

<1>1. $x^{p^n} - x$ is squarefree in $\mathbb{F}_p[x]$:
    *Proof:*
    <2>1. In $\mathbb{F}_p[x]$, the formal derivative of $P(x) = x^{p^n} - x$ is:
        $$P'(x) = p^n x^{p^n - 1} - 1 = 0 - 1 = -1.$$
    <2>2. Thus $\gcd(P(x), P'(x)) = \gcd(x^{p^n} - x, -1) = 1$.
    <2>3. Therefore, $P(x)$ has no multiple roots and decomposes as a product of distinct monic irreducible polynomials in $\mathbb{F}_p[x]$.

<1>2. Every monic irreducible $f(x)$ with $\deg(f) \mid n$ divides $x^{p^n} - x$:
    *Proof:*
    <2>1. Let $f(x) \in \mathbb{F}_p[x]$ be monic irreducible of degree $d$, where $d \mid n$.
    <2>2. Let $\alpha$ be a root of $f(x)$ in an algebraic closure $\overline{\mathbb{F}}_p$.
    <2>3. The extension $\mathbb{F}_p(\alpha)$ has degree $[\mathbb{F}_p(\alpha) : \mathbb{F}_p] = d$, so $\mathbb{F}_p(\alpha) \cong \mathbb{F}_{p^d}$.
    <2>4. Since $d \mid n$, $\mathbb{F}_{p^d}$ is a subfield of $\mathbb{F}_{p^n}$, so $\alpha \in \mathbb{F}_{p^n}$.
    <2>5. The field $\mathbb{F}_{p^n}$ consists precisely of the roots of $x^{p^n} - x = 0$, so $\alpha^{p^n} - \alpha = 0$.
    <2>6. Since $f(x)$ is the minimal polynomial of $\alpha$ over $\mathbb{F}_p$, $f(x)$ must divide $x^{p^n} - x$.

<1>3. Every monic irreducible factor $f(x)$ of $x^{p^n} - x$ has degree dividing $n$:
    *Proof:*
    <2>1. Let $f(x)$ be a monic irreducible factor of $x^{p^n} - x$ in $\mathbb{F}_p[x]$, and let $d = \deg(f)$.
    <2>2. Let $\alpha \in \overline{\mathbb{F}}_p$ be a root of $f(x)$.
    <2>3. Since $f(x) \mid (x^{p^n} - x)$, $\alpha$ satisfies $\alpha^{p^n} - \alpha = 0$, so $\alpha \in \mathbb{F}_{p^n}$.
    <2>4. Consequently, $\mathbb{F}_p \subseteq \mathbb{F}_p(\alpha) \subseteq \mathbb{F}_{p^n}$.
    <2>5. By the Tower Law:
        $$n = [\mathbb{F}_{p^n} : \mathbb{F}_p] = [\mathbb{F}_{p^n} : \mathbb{F}_p(\alpha)] \cdot [\mathbb{F}_p(\alpha) : \mathbb{F}_p] = [\mathbb{F}_{p^n} : \mathbb{F}_p(\alpha)] \cdot d.$$
    <2>6. Thus $d = \deg(f)$ divides $n$.

<1>4. Conclusion:
    Since $x^{p^n} - x$ is monic, squarefree, and its irreducible factors are exactly all monic irreducible polynomials in $\mathbb{F}_p[x]$ of degree $d \mid n$, the product identity holds. Q.E.D.
:::
