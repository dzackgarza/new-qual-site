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

::: {.problem}
(a) If $\FF_q$ is a field with $q$ elements, show that $\FF_q^\times$ is a cyclic group.

(b) Show that for each integer $n \geq 1$, there exists an irreducible polynomial over $\FF_q$ of degree $n$.

(c) Consider the map $\phi: \FF_{q^n} \to \FF_{q^n}$ given by $\phi(x) = x^q$.
Note that $\phi$ is an $\FF_q$-linear endomorphism of the $\FF_q$-vector space $\FF_{q^n}$.
Find the characteristic and minimal polynomials of $\phi$.
:::

::: {.solution}

::: pf

::: pf-step
Part (a): $\FF_q^\times$ is cyclic:

::: pf-proof

::: pf-step
Let $G = \FF_q^\times$ be the multiplicative group of the finite field $\FF_q$, which is an abelian group of order $|G| = q - 1$.
Let $m = \exp(G)$ denote the exponent of $G$, which is the least common multiple of the orders of all elements in $G$.
By Lagrange's Theorem, $m \le q - 1$.
:::

::: pf-step
By definition of exponent, every element $x \in \FF_q^\times$ satisfies $x^m - 1 = 0$.
The polynomial $x^m - 1 \in \FF_q[x]$ has degree $m$ and can have at most $m$ roots in the field $\FF_q$.
Because all $q - 1$ elements of $\FF_q^\times$ are roots:
\[
q - 1 \le m.
\]
:::

::: pf-step
Combining $m \le q - 1$ and $q - 1 \le m$ gives $m = q - 1$.
For any finite abelian group, there exists an element whose order equals the exponent $m$.
Thus there exists $\alpha \in \FF_q^\times$ with $o(\alpha) = q - 1 = |\FF_q^\times|$, so $\FF_q^\times = \langle \alpha \rangle$ is cyclic.
:::

:::

:::

::: pf-step
Part (b): Existence of an irreducible polynomial of degree $n$ over $\FF_q$:

::: pf-proof

::: pf-step
Consider the finite field extension $\FF_{q^n}$, which is an $n$-dimensional vector space over $\FF_q$, so $[\FF_{q^n} : \FF_q] = n$.
:::

::: pf-step
By Part (a), the multiplicative group $\FF_{q^n}^\times$ is cyclic.
Let $\gamma$ be a generator of $\FF_{q^n}^\times$.
Then $\FF_{q^n} = \FF_q(\gamma)$.
:::

::: pf-step
Let $m_\gamma(x) \in \FF_q[x]$ be the minimal polynomial of $\gamma$ over $\FF_q$.
By field theory, $m_\gamma(x)$ is irreducible over $\FF_q$, and its degree is:
\[
\deg(m_\gamma) = [\FF_q(\gamma) : \FF_q] = [\FF_{q^n} : \FF_q] = n.
\]
Thus $m_\gamma(x)$ is an irreducible polynomial of degree $n$ over $\FF_q$.
:::

:::

:::

::: pf-step
Part (c): Characteristic and minimal polynomials of the Frobenius endomorphism $\phi$:

::: pf-proof

::: pf-step
The map $\phi: \FF_{q^n} \to \FF_{q^n}$ given by $\phi(x) = x^q$ is the Frobenius $\FF_q$-automorphism.
For any $x \in \FF_{q^n}$, $\phi^n(x) = x^{q^n} = x$, so $\phi^n = \operatorname{id}_{\FF_{q^n}}$.
Thus $\phi$ satisfies the polynomial $T^n - 1 \in \FF_q[T]$.
:::

::: pf-step
By Dedekind's Theorem on the linear independence of distinct group characters/automorphisms, the automorphisms $\{\operatorname{id}, \phi, \phi^2, \ldots, \phi^{n-1}\}$ are linearly independent over $\FF_{q^n}$ (and hence over $\FF_q$).
:::

::: pf-step
Therefore, no non-zero polynomial in $\FF_q[T]$ of degree strictly less than $n$ can annihilate $\phi$.
Since $T^n - 1$ is a monic polynomial of degree $n$ annihilating $\phi$, the minimal polynomial is:
\[
m_\phi(T) = T^n - 1.
\]
:::

::: pf-step
The characteristic polynomial $\chi_\phi(T)$ is a monic polynomial of degree $\dim_{\FF_q}(\FF_{q^n}) = n$ which is divisible by $m_\phi(T)$.
Since $\deg(m_\phi) = n = \deg(\chi_\phi)$ and both are monic:
\[
\chi_\phi(T) = T^n - 1.
\]
:::

:::

:::

::: pf-qed
Conclusion:
$\FF_q^\times$ is cyclic, an irreducible polynomial of degree $n$ exists for every $n \ge 1$, and both the minimal and characteristic polynomials of $\phi$ are $T^n - 1$.
:::

:::
:::
