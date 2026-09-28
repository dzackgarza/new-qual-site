---
schema: qual/card@1
id: P-BKF18-8A
kind: problem
title: GCD distributes over LCM
classification:
  areas:
  - prelim
  topics:
  - Abstract Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: {.problem}
For nonzero integers $a,b,c$, show that
\[
\gcd(a,\operatorname{lcm}(b,c))
=\operatorname{lcm}(\gcd(a,b),\gcd(a,c)).
\]
:::

::: {.solution}
Given a prime $p ,$ let $\alpha , \beta ,$ and $\gamma$ be the exponents of $p$ in the prime factorization of $a , b ,$ and ${ \mathit { c } } ,$ respectively.
Then it will suffice to show that

$$
\operatorname* { m i n } \{ \alpha , \operatorname* { m a x } \{ \beta , \gamma \} \} = \operatorname* { m a x } \{ \operatorname* { m i n } \{ \alpha , \beta \} , \operatorname* { m i n } \{ \alpha , \gamma \} \} \ .
$$

Without loss of generality, we may assume that $\beta \leq \gamma ;$ in that case max $\{ \beta , \gamma \} = \gamma$ and min $\{ \alpha , \beta \} \le \operatorname* { m i n } \{ \alpha , \gamma \}$ Therefore the above equation is true because both sides are equal to min $\{ \alpha , \gamma \}$
:::
