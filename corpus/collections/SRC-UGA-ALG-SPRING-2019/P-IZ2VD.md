---
schema: qual/card@1
id: P-IZ2VD
kind: problem
title: Irreducibles of degree $d$ over $\FF_p$ divide $x^{p^d}-x$, and divide $x^{p^n}-x$
  only if $d$ divides $n$
classification:
  areas:
  - algebra
  topics:
  - Finite Fields
  - Irreducibility Criteria
  - Field Extensions
relations: []
review: draft
---
::: {.problem}
Let $F = \FF_p$, where $p$ is a prime number.

(a) Show that if $\pi(x) \in \FF_p[x]$ is irreducible of degree $d$, then $\pi(x)$ divides $x^{p^d} - x$ in $\FF_p[x]$.

(b) Show that if $\pi(x) \in \FF_p[x]$ is an irreducible polynomial that divides $x^{p^n} - x$, then $\deg \pi(x)$ divides $n$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Every irreducible polynomial $\pi\in\FF_p[x]$ of degree $d$ divides $x^{p^d}-x$.

::: pf-proof

::: pf-step

Construct the field $K = \FF_p[x]/\langle \pi(x) \rangle$. Since $\pi(x)$ is irreducible over $\FF_p$, $\langle \pi(x) \rangle$ is a maximal ideal, so $K$ is a field.

:::

::: pf-step

The extension degree is $[K : \FF_p] = \deg \pi(x) = d$, so $|K| = p^d$.

:::

::: pf-step

The multiplicative group $K^\times = K \setminus \{0\}$ is a group of order $p^d - 1$.

:::

::: pf-step

By Lagrange's Theorem (or Euler's Theorem for finite groups), every element $\alpha \in K^\times$ satisfies $\alpha^{p^d - 1} = 1$, which implies $\alpha^{p^d} = \alpha$.

:::

::: pf-step

For $\alpha = 0$, $0^{p^d} - 0 = 0$. Thus $\alpha^{p^d} - \alpha = 0$ for all $\alpha \in K$.

:::

::: pf-step

Consider the residue class $\bar{x} = x + \langle \pi(x) \rangle \in K$.

:::

::: pf-step

Applying the polynomial identity to $\bar{x}$ gives
    $$\bar{x}^{p^d} - \bar{x} = 0 \quad \text{in } K = \FF_p[x]/\langle \pi(x) \rangle.$$

:::

::: pf-step

By definition of the quotient ring, this means $x^{p^d} - x \in \langle \pi(x) \rangle$.

:::

::: pf-step

Therefore $\pi(x)$ divides $x^{p^d} - x$ in $\FF_p[x]$.

:::

:::

:::

::: {.pf-step #s2}

If an irreducible $\pi\in\FF_p[x]$ divides $x^{p^n}-x$, then $\deg\pi\mid n$.

::: pf-proof

::: pf-step

Let $L = \FF_{p^n}$ be the splitting field of $x^{p^n} - x$ over $\FF_p$, which is a finite field of degree $[L : \FF_p] = n$.

:::

::: pf-step

The elements of $L$ are precisely the $p^n$ distinct roots of $x^{p^n} - x$.

:::

::: pf-step

Since $\pi(x) \mid (x^{p^n} - x)$ in $\FF_p[x]$, every root of $\pi(x)$ in an algebraic closure $\overline{\FF}_p$ is also a root of $x^{p^n} - x$, and therefore lies in $L$.

:::

::: pf-step

Let $\alpha \in L$ be a root of $\pi(x)$.

:::

::: pf-step

Since $\pi(x)$ is irreducible over $\FF_p$, it is a scalar multiple of the minimal polynomial $m_{\alpha, \FF_p}(x)$, so
    $$[\FF_p(\alpha) : \FF_p] = \deg \pi(x).$$

:::

::: pf-step

Since $\alpha \in L$, we have the tower of subfields $\FF_p \subseteq \FF_p(\alpha) \subseteq L$.

:::

::: pf-step

By the Tower Law for field extensions:
    $$n = [L : \FF_p] = [L : \FF_p(\alpha)] \cdot [\FF_p(\alpha) : \FF_p] = [L : \FF_p(\alpha)] \cdot \deg \pi(x).$$

:::

::: pf-step

Since $[L : \FF_p(\alpha)]$ is an integer, $\deg \pi(x)$ divides $n$.

:::

:::

:::

::: pf-qed

Step [](#s1){.pf-ref} proves part (a), and step [](#s2){.pf-ref} proves part (b).

:::

:::

:::
