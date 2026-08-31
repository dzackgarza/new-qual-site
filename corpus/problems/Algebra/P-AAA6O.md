---
schema: qual/card@1
id: P-AAA6O
kind: problem
title: Rational roots of polynomials in $\QQ[x]$ are integers
classification:
  areas:
  - algebra
  topics:
  - Polynomials
  - Factorization
  - Number Theory
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-16
---

::: problem
- Show that if $p\in \QQ[x]$ and $r\in \QQ$ is a rational root, then in fact $r\in \ZZ$.
:::

::: {.solution}
**Goal:** Let $p(x) = x^n + a_{n-1} x^{n-1} + \dots + a_1 x + a_0 \in \mathbb{Z}[x]$ be a monic polynomial with integer coefficients.
Prove that if $r \in \mathbb{Q}$ is a rational root of $p(x)$, then $r \in \mathbb{Z}$.

<1>1. Setting and representation of the rational root: <2>1. Let $r \in \mathbb{Q}$ satisfy $p(r) = 0$.
::: {.proof}
Hypothesis.
:::
<2>2. Write $r = \frac{a}{b}$ where $a, b \in \mathbb{Z}$, $b \ge 1$, and $\gcd(a, b) = 1$.
::: {.proof}
Every rational number can be expressed uniquely as a fraction in lowest terms with positive denominator.
:::
<2>3. Goal reduction: To show $r \in \mathbb{Z}$, it suffices to show that $b = 1$.
::: {.proof}
If $b = 1$, then $r = \frac{a}{1} = a \in \mathbb{Z}$.
:::

<1>2. Substitution into the polynomial equation: <2>1. Substituting $r = \frac{a}{b}$ into $p(r) = 0$ yields: $$\left(\frac{a}{b}\right)^n + a_{n-1} \left(\frac{a}{b}\right)^{n-1} + \dots + a_1 \left(\frac{a}{b}\right) + a_0 = 0.$$ Proof: Since $p(r) = 0$.
<2>2. Multiplying both sides of the equation by $b^n$ gives: $$a^n + a_{n-1} a^{n-1} b + a_{n-2} a^{n-2} b^2 + \dots + a_1 a b^{n-1} + a_0 b^n = 0.$$ Proof: Clearing denominators by multiplying by $b^n \neq 0$.

<1>3. Isolating the leading power $a^n$: <2>1. Rearranging the terms gives: $$a^n = -b \left(a_{n-1} a^{n-1} + a_{n-2} a^{n-2} b + \dots + a_1 a b^{n-2} + a_0 b^{n-1}\right).$$ Proof: Subtracting all terms other than $a^n$ to the right-hand side and factoring out $-b$.
<2>2. Since $a_i, a, b \in \mathbb{Z}$, the quantity $M = a_{n-1} a^{n-1} + a_{n-2} a^{n-2} b + \dots + a_0 b^{n-1}$ is an integer.
::: {.proof}
The ring $\mathbb{Z}$ is closed under addition and multiplication.
:::
<2>3. Therefore, $b \mid a^n$ in $\mathbb{Z}$.
::: {.proof}
$a^n = -b M$ with $M \in \mathbb{Z}$.
:::

<1>4. Deducing $b = 1$: <2>1. Suppose for contradiction that $b > 1$.
::: {.proof}
Assumption for contradiction.
:::
<2>2. Since $b > 1$, there exists a prime $q$ such that $q \mid b$.
::: {.proof}
Fundamental Theorem of Arithmetic (existence of prime factors for integers $> 1$). <2>3. Since $q \mid b$ and $b \mid a^n$, we have $q \mid a^n$.
:::
::: {.proof}
Transitivity of divisibility.
:::
<2>4. Since $q$ is prime and $q \mid a^n$, Euclid's Lemma implies $q \mid a$.
::: {.proof}
If a prime divides a product of integers, it divides at least one of the factors.
:::
<2>5. Thus $q \mid a$ and $q \mid b$, so $q \mid \gcd(a, b)$.
::: {.proof}
Definition of greatest common divisor.
:::
<2>6. Contradiction: $\gcd(a, b) = 1$, but $q \ge 2$.
::: {.proof}
Contradicts lowest terms representation in <1>1.<2>2. <2>7. Therefore, $b = 1$.
:::
::: {.proof}
By contradiction from <2>1 through <2>6.
:::

<1>5. Conclusion: $r = \frac{a}{1} = a \in \mathbb{Z}$.
::: {.proof}
By <1>1.<2>3 and <1>4.<2>7.
:::
:::
