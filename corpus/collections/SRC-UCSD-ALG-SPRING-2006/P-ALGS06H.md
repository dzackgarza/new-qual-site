---
schema: qual/card@1
id: P-ALGS06H
kind: problem
title: "Cyclic multiplicative group and existence of irreducible polynomials over finite fields"
classification:
  areas:
  - algebra
  topics:
  - Field Theory
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: problem
(a) If $\mathbb{F}_q$ is a field with $q$ elements, show that $\mathbb{F}_q^\times$ is a cyclic group.

(b) Show that for each integer $n \geq 1$, there exists an irreducible polynomial over $\mathbb{F}_q$ of degree $n$.

(c) Consider the map $\phi: \mathbb{F}_{q^n} \to \mathbb{F}_{q^n}$ given by $\phi(x) = x^q$.
Note that $\phi$ is an $\mathbb{F}_q$-linear endomorphism of the $\mathbb{F}_q$-vector space $\mathbb{F}_{q^n}$.
Find the characteristic and minimal polynomials of $\phi$.
:::

::: {.solution}
<1>1. Part (a): $\mathbb{F}_q^\times$ is cyclic:
<2>1. Let $G = \mathbb{F}_q^\times$ be the multiplicative group of the finite field $\mathbb{F}_q$, which is an abelian group of order $|G| = q - 1$.
Let $m = \exp(G)$ denote the exponent of $G$, which is the least common multiple of the orders of all elements in $G$.
By Lagrange's Theorem, $m \le q - 1$.
<2>2. By definition of exponent, every element $x \in \mathbb{F}_q^\times$ satisfies $x^m - 1 = 0$.
The polynomial $x^m - 1 \in \mathbb{F}_q[x]$ has degree $m$ and can have at most $m$ roots in the field $\mathbb{F}_q$.
Because all $q - 1$ elements of $\mathbb{F}_q^\times$ are roots:
\[
q - 1 \le m.
\]
<2>3. Combining $m \le q - 1$ and $q - 1 \le m$ gives $m = q - 1$.
For any finite abelian group, there exists an element whose order equals the exponent $m$.
Thus there exists $\alpha \in \mathbb{F}_q^\times$ with $o(\alpha) = q - 1 = |\mathbb{F}_q^\times|$, so $\mathbb{F}_q^\times = \langle \alpha \rangle$ is cyclic.

<1>2. Part (b): Existence of an irreducible polynomial of degree $n$ over $\mathbb{F}_q$:
<2>1. Consider the finite field extension $\mathbb{F}_{q^n}$, which is an $n$-dimensional vector space over $\mathbb{F}_q$, so $[\mathbb{F}_{q^n} : \mathbb{F}_q] = n$.
<2>2. By Part (a), the multiplicative group $\mathbb{F}_{q^n}^\times$ is cyclic.
Let $\gamma$ be a generator of $\mathbb{F}_{q^n}^\times$.
Then $\mathbb{F}_{q^n} = \mathbb{F}_q(\gamma)$.
<2>3. Let $m_\gamma(x) \in \mathbb{F}_q[x]$ be the minimal polynomial of $\gamma$ over $\mathbb{F}_q$.
By field theory, $m_\gamma(x)$ is irreducible over $\mathbb{F}_q$, and its degree is:
\[
\deg(m_\gamma) = [\mathbb{F}_q(\gamma) : \mathbb{F}_q] = [\mathbb{F}_{q^n} : \mathbb{F}_q] = n.
\]
Thus $m_\gamma(x)$ is an irreducible polynomial of degree $n$ over $\mathbb{F}_q$.

<1>3. Part (c): Characteristic and minimal polynomials of the Frobenius endomorphism $\phi$:
<2>1. The map $\phi: \mathbb{F}_{q^n} \to \mathbb{F}_{q^n}$ given by $\phi(x) = x^q$ is the Frobenius $\mathbb{F}_q$-automorphism.
For any $x \in \mathbb{F}_{q^n}$, $\phi^n(x) = x^{q^n} = x$, so $\phi^n = \operatorname{id}_{\mathbb{F}_{q^n}}$.
Thus $\phi$ satisfies the polynomial $T^n - 1 \in \mathbb{F}_q[T]$.
<2>2. By Dedekind's Theorem on the linear independence of distinct group characters/automorphisms, the automorphisms $\{\operatorname{id}, \phi, \phi^2, \ldots, \phi^{n-1}\}$ are linearly independent over $\mathbb{F}_{q^n}$ (and hence over $\mathbb{F}_q$).
<2>3. Therefore, no non-zero polynomial in $\mathbb{F}_q[T]$ of degree strictly less than $n$ can annihilate $\phi$.
Since $T^n - 1$ is a monic polynomial of degree $n$ annihilating $\phi$, the minimal polynomial is:
\[
m_\phi(T) = T^n - 1.
\]
<2>4. The characteristic polynomial $\chi_\phi(T)$ is a monic polynomial of degree $\dim_{\mathbb{F}_q}(\mathbb{F}_{q^n}) = n$ which is divisible by $m_\phi(T)$.
Since $\deg(m_\phi) = n = \deg(\chi_\phi)$ and both are monic:
\[
\chi_\phi(T) = T^n - 1.
\]

<1>4. Conclusion:
$\mathbb{F}_q^\times$ is cyclic, an irreducible polynomial of degree $n$ exists for every $n \ge 1$, and both the minimal and characteristic polynomials of $\phi$ are $T^n - 1$. Q.E.D.
:::
