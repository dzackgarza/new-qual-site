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
<1>1. The integral $I_m$ can be written as
$$
I_m
=
\sum_{j=0}^m
(-1)^j\binom mj\frac{1}{m+j+1}.
$$

::: {.proof}
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

<1>2. The number $d_{2m+1}I_m$ is an integer.

::: {.proof}
For $0\leq j\leq m$, the denominator $m+j+1$ is an integer between
$1$ and $2m+1$, so it divides
$$
d_{2m+1}=\operatorname{lcm}(1,2,\ldots,2m+1).
$$
Every summand in step <1>1 therefore becomes an integer after multiplication
by $d_{2m+1}$. Hence
$$
d_{2m+1}I_m\in\ZZ.
$$
:::

<1>3. One has
$$
0<I_m\leq4^{-m}.
$$

::: {.proof}
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

<1>4. One has
$$
d_{2m+1}I_m\geq1.
$$

::: {.proof}
By step <1>2, $d_{2m+1}I_m$ is an integer. By step <1>3 and
$d_{2m+1}>0$, it is positive. Every positive integer is at least $1$.
:::

<1>5. The required lower bound is
$$
\boxed{d_{2m+1}\geq2^{2m}}.
$$

::: {.proof}
Steps <1>3 and <1>4 give
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

<1>6. Q.E.D.

::: {.proof}
Step <1>2 proves the integrality assertion, and step <1>5 proves the required
lower bound.
:::
:::
