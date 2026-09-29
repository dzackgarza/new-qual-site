---
schema: qual/card@1
id: P-CASP26C
kind: problem
title: "The polynomial 1 + z + az^n has a root in |z| <= 2 for all a and n >= 2"
classification:
  areas:
  - complex-analysis
  topics:
  - Polynomial Roots
  - Rouché
  - Argument Principle
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
Prove that, for any $a \in \mathbb{C}$ and any integer $n \geq 2$, the polynomial $1 + z + az^n$ has at least one root in the disk $\{|z| \leq 2\}$.

Hint: The constant term in a monic polynomial is the product of its zeros (up to sign).
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Suppose for contradiction that all roots of $1 + z + az^n$ have modulus $> 2$.

::: pf-proof

assume the contrary.

:::

:::

::: {.pf-step #s2}

Write $1 + z + az^n = a\prod_{i=1}^n (z - r_i)$, where $r_1, \ldots, r_n$ are the roots.

::: pf-proof

factor the polynomial (assuming $a \neq 0$; if $a = 0$, the polynomial is $1 + z$ with root $-1$, which has modulus $1 \le 2$, done).

:::

:::

::: {.pf-step #s3}

The constant term is $1 = a(-1)^n \prod_i r_i$, so $\prod_i |r_i| = 1/|a|$.

::: pf-proof

the constant term is $a(-1)^n \prod_i r_i = 1$.

:::

:::

::: {.pf-step #s4}

If all $|r_i| > 2$, then $\prod_i |r_i| > 2^n$, so by step [](#s3){.pf-ref}, $1/|a| > 2^n$, i.e. $|a| < 2^{-n}$.

::: pf-proof

Step [](#s3){.pf-ref} and the assumption $|r_i| > 2$.

:::

:::

::: {.pf-step #s5}

On $|z| = 2$, $|az^n| = |a| \cdot 2^n < 1$, and $|1 + z| \ge |z| - 1 = 1$.

::: pf-proof

Step [](#s4){.pf-ref} and the reverse triangle inequality.

:::

:::

::: {.pf-step #s6}

Hence on $|z| = 2$, $|az^n| < 1 \le |1 + z|$, so by Rouché's theorem, $1 + z + az^n$ and $1 + z$ have the same number of zeros in $|z| < 2$.

::: pf-proof

Rouché's theorem.

:::

:::

::: {.pf-step #s7}

$1 + z$ has exactly one zero in $|z| < 2$ (at $z = -1$).

::: pf-proof

$1 + z = 0$ iff $z = -1$, which has modulus $1 < 2$.

:::

:::

::: {.pf-step #s8}

Hence $1 + z + az^n$ has a root in $|z| < 2$, contradicting the assumption that all roots have modulus $> 2$.

::: pf-proof

Steps [](#s6){.pf-ref} and [](#s7){.pf-ref}.

:::

:::

::: {.pf-step #s9}

Therefore $1 + z + az^n$ has at least one root in $|z| \le 2$.

::: pf-proof

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref}, [](#s3){.pf-ref}, [](#s4){.pf-ref}, [](#s5){.pf-ref}, [](#s6){.pf-ref}, [](#s7){.pf-ref} and [](#s8){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s9){.pf-ref}.

:::

:::

:::
