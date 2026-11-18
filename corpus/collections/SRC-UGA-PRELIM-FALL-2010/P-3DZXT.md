---
schema: qual/card@1
id: P-3DZXT
kind: problem
title: The binomial theorem, $(x+y)^5\equiv x^5+y^5\pmod{5}$, and $(x+y)^{5^n}\equiv
  x^{5^n}+y^{5^n}\pmod{5}$
classification:
  areas:
  - prelim
  topics:
  - Induction
  - Combinatorics
  - Number Theory
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured the prose solution into a Lamport proof and checked it: the binomial
    theorem, the four middle coefficients of (x+y)^5 with their values, the m = 5 congruence,
    the preservation of congruence under the fifth power (by the factorisation of a^5 - b^5),
    and the induction step with X = x^{5^n}, Y = y^{5^n}. The prose used "raising both sides
    to the fifth power preserves congruence" without proof; that is now a step. The statement
    is true as printed. The collection's provenance is the examination paper only, so no
    retained solution set covers the exercise and the argument is the card's own.
---

::: {.problem}
(a) State the binomial theorem.

(b) Prove that $(x+y)^5 \equiv x^5 + y^5 \pmod 5$.

(c) Prove by mathematical induction that $(x+y)^{5^n} \equiv x^{5^n} + y^{5^n} \pmod 5$ for every $n \in \NN$.
:::

::: {.solution}
The collection's provenance is the examination paper alone, so no retained solution set covers this exercise; the argument is the card's own.

::: pf

::: {.pf-step #binomial}
(a) For every positive integer $m$,
$$
(x+y)^m=\sum_{j=0}^{m}\binom mj x^{m-j}y^j .
$$

::: pf-proof
That is the binomial theorem, the coefficients being the binomial coefficients $\binom mj=\frac{m!}{j!(m-j)!}$.
:::

:::

::: {.pf-step #coefficients}
$5$ divides $\binom5j$ for $1\le j\le4$.

::: pf-proof
The four values are $\binom51=\binom54=5$ and $\binom52=\binom53=10$.
:::

:::

::: {.pf-step #case-five}
(b) $(x+y)^5\equiv x^5+y^5\pmod 5$.

::: pf-proof
By step [](#binomial){.pf-ref} with $m=5$, $(x+y)^5=x^5+\sum_{j=1}^{4}\binom5j x^{5-j}y^j+y^5$; step [](#coefficients){.pf-ref} makes every summand of the middle sum a multiple of $5$, so it is $0$ modulo $5$.
:::

:::

::: {.pf-step #fifth-power}
If $a\equiv b\pmod 5$ then $a^5\equiv b^5\pmod 5$.

::: pf-proof
$a\equiv b$ means $5\mid(a-b)$, and then $a^5-b^5=(a-b)(a^4+a^3b+a^2b^2+ab^3+b^4)$ is divisible by $5$.
:::

:::

::: {.pf-step}
(c) $(x+y)^{5^n}\equiv x^{5^n}+y^{5^n}\pmod 5$ for every $n\ge1$.

::: pf-proof
Induction on $n$. For $n=1$ the assertion is step [](#case-five){.pf-ref}. If it holds for $n$, then by step [](#fifth-power){.pf-ref}
$$
(x+y)^{5^{n+1}}=\left((x+y)^{5^n}\right)^5\equiv\left(x^{5^n}+y^{5^n}\right)^5\pmod 5,
$$
and step [](#case-five){.pf-ref} applied with $X=x^{5^n}$ and $Y=y^{5^n}$ gives $\left(X+Y\right)^5\equiv X^5+Y^5=x^{5^{n+1}}+y^{5^{n+1}}$. Hence the congruence holds for $n+1$, and by induction for every $n\ge1$.
:::

:::

:::
:::
