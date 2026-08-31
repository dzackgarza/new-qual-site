---
schema: qual/card@1
id: P-ARTALG-JU03-3
kind: problem
title: No GCD in polynomial ring and subring of Euclidean domain
classification:
  areas:
  - algebra
  topics:
  - Commutative Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

(a) Let $R$ be the ring of all polynomials in $\mathbb{Q}[x]$ having no $x$-term.
Show that $x^5$ and $x^6$ have no GCD in $R$.

(b) If $S$ is a Euclidean domain and $T$ is a subring of $S$, is it true that $T$ is a Euclidean domain?
Justify your answer.

::: {.solution}
**(a).**

<1>1. $R$ is the subring of $\mathbb{Q}[x]$ consisting of polynomials with no $x$-term.
::: {.proof}
definition.
:::

<1>2. In $\mathbb{Q}[x]$, $\gcd(x^5, x^6) = x^5$.
::: {.proof}
standard GCD in the polynomial ring.
:::

<1>3. $x^5 \notin R$ (it has an $x$-term... actually $x^5$ has no $x$-term, so $x^5 \in R$; the issue is different).
::: {.proof}
$x^5$ has no $x$-term, so $x^5 \in R$.
:::

<1>4. The common divisors of $x^5$ and $x^6$ in $R$ are the polynomials in $R$ dividing both, i.e. $x^k$ for $k \le 5$ with no $x$-term, so $k \in \{0, 2, 3, 4, 5\}$ (excluding $k = 1$ since $x$ has an $x$-term).
::: {.proof}
the divisors of $x^5$ in $R$ are $x^k$ for $k \in \{0, 2, 3, 4, 5\}$ (and $k = 1$ is excluded).
:::

<1>5. The maximal common divisors are $x^5$ and $x^4$ (both divide $x^5$ and $x^6$, and neither divides the other in $R$... $x^5$ does not divide $x^4$).
::: {.proof}
<1>4 (both $x^4$ and $x^5$ are common divisors, and neither is a multiple of the other in $R$).
:::

<1>6. Hence there is no greatest common divisor (no common divisor that is a multiple of all others).
::: {.proof}
<1>5.
:::

**(b).**

<1>1. No, a subring of a Euclidean domain need not be a Euclidean domain.
::: {.proof}
answer.
:::

<1>2. Counterexample: $S = \mathbb{Q}[x]$ (a Euclidean domain) and $T = \mathbb{Q}[x^2, x^3]$ (a subring).
::: {.proof}
choose the example.
:::

<1>3. $T = \mathbb{Q}[x^2, x^3]$ is not a UFD: $x^6 = (x^2)^3 = (x^3)^2$ are two distinct factorizations into irreducibles.
::: {.proof}
$x^2$ and $x^3$ are irreducible in $T$, and $x^6$ has two factorizations.
:::

<1>4. A Euclidean domain is a UFD, so $T$ is not a Euclidean domain.
::: {.proof}
<1>3.
:::

<1>5. Hence a subring of a Euclidean domain need not be Euclidean.
::: {.proof}
<1>2 and <1>4.
:::

<1>6. Q.E.D.
::: {.proof}
<1>6 (a) and <1>5 (b).
:::
:::
