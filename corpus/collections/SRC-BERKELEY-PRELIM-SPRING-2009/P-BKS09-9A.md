---
schema: qual/card@1
id: P-BKS09-9A
kind: problem
title: Lower bound $\operatorname{lcm}(1,\dots,2m+1)\ge 2^{2m}$ via $\int_0^1 x^m(1-x)^m\,dx$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-25
  note: >-
    Compared the card with the retained Spring 2009 solution PDF and extraction.
    The source proof changes d_{2m+1} to d_m in its final inequality; the authored
    proof retains the correct index.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked the binomial expansion, denominator divisibility, and sharp elementary bound x(1-x)≤1/4.
---

::: {.problem}
Let $d _ { k } : = \operatorname { L C M } \{ 1 , 2 , \dots , k \}$ (the least common multiple) and $I _ { m } = \int _ { 0 } ^ { 1 } x ^ { m } ( 1 - x ) ^ { m } \mathrm { d } x$ . Show $d _ { 2 m + 1 } I _ { m }$ is an integer, and use this to show that $d _ { 2 m + 1 } \geq 2 ^ { 2 m }$
:::

::: {.solution}

::: pf

::: {.pf-step #binomial-expansion}
The integral $I_m$ can be written as
$$
I_m
=
\sum_{j=0}^m
(-1)^j\binom mj\frac{1}{m+j+1}.
$$

::: pf-proof
By the binomial theorem,
$$
x^m(1-x)^m
=
\sum_{j=0}^m(-1)^j\binom mj x^{m+j}.
$$
Integrating term by term on $[0,1]$ gives
$$
I_m
=
\sum_{j=0}^m
(-1)^j\binom mj
\int_0^1x^{m+j}\,dx
=
\sum_{j=0}^m
(-1)^j\binom mj\frac{1}{m+j+1}.
$$
:::

:::

::: {.pf-step #integer-product}
The number $d_{2m+1}I_m$ is an integer.

::: pf-proof
For $0\leq j\leq m$, the denominator $m+j+1$ is an integer between
$1$ and $2m+1$, so it divides
$$
d_{2m+1}=\operatorname{lcm}(1,2,\ldots,2m+1).
$$
Every summand in step [](#binomial-expansion){.pf-ref} therefore becomes an integer after multiplication
by $d_{2m+1}$. Hence
$$
d_{2m+1}I_m\in\ZZ.
$$
:::

:::

::: {.pf-step #integral-bound}
One has
$$
0<I_m\leq4^{-m}.
$$

::: pf-proof
For $0\leq x\leq1$,
$$
0\leq x(1-x)
=
\frac14-\left(x-\frac12\right)^2
\leq
\frac14.
$$
Thus
$$
0\leq x^m(1-x)^m\leq4^{-m}.
$$
The integrand is positive on $(0,1)$, so its integral is positive, and
integration over an interval of length $1$ gives
$$
0<I_m\leq4^{-m}.
$$
:::

:::

::: {.pf-step #product-at-least-one}
One has
$$
d_{2m+1}I_m\geq1.
$$

::: pf-proof
By step [](#integer-product){.pf-ref}, $d_{2m+1}I_m$ is an integer. By step [](#integral-bound){.pf-ref} and
$d_{2m+1}>0$, it is positive. Every positive integer is at least $1$.
:::

:::

::: {.pf-step #lower-bound}
The required lower bound is
$$
\boxed{d_{2m+1}\geq2^{2m}}.
$$

::: pf-proof
Steps [](#integral-bound){.pf-ref} and [](#product-at-least-one){.pf-ref} give
$$
1
\leq
d_{2m+1}I_m
\leq
d_{2m+1}4^{-m}.
$$
Multiplying by $4^m$ yields
$$
d_{2m+1}\geq4^m=2^{2m}.
$$
:::

:::

::: pf-qed
Step [](#integer-product){.pf-ref} proves the integrality assertion, and step [](#lower-bound){.pf-ref} proves the required
lower bound.
:::

:::

:::
