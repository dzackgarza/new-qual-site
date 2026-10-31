---
schema: qual/card@1
id: E-SS6.EX-12
kind: problem
title: $1/\Gamma$ is not of exponential type
classification:
  areas:
  - complex-analysis
  topics:
  - Gamma Function
  - Entire Functions
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: {.exercise}
This exercise gives two simple observations about $1/\Gamma$.

(a) Show that $1/\abs{\Gamma(s)}$ is not $O(e^{c\abs{s}})$ for any $c > 0$. [Hint: If $s = -k - 1/2$ where $k$ is a positive integer, then $\abs{1/\Gamma(s)} \geq k!/\pi$.]

(b) Show that there is no entire function $F(s)$ with $F(s) = O(e^{c\abs{s}})$ that has simple zeros at $s = 0, -1, -2, \ldots, -n, \ldots$, and that vanishes nowhere else.
:::

::: {.solution}
**(a).**

::: pf

::: {.pf-step #p1-s1}
For $s = -k - 1/2$ (with $k$ a positive integer), $\abs{1/\Gamma(s)} \ge k!/\pi$.

::: pf-proof
the hint (using the reflection formula $\Gamma(s)\Gamma(1-s) = \pi/\sin(\pi s)$, which gives $\abs{\Gamma(-k-1/2)} \le \pi/k!$).
:::

:::

::: {.pf-step #p1-s2}
If $1/\abs{\Gamma(s)} = O(e^{c\abs{s}})$, then there is $C$ with $1/\abs{\Gamma(s)} \le C e^{c\abs{s}}$ for all $s$.

::: pf-proof
definition of big-O.
:::

:::

::: {.pf-step #p1-s3}
At $s = -k - 1/2$, this gives $k!/\pi \le C e^{c(k + 1/2)}$ for all $k$.

::: pf-proof
step [](#p1-s1){.pf-ref} and step [](#p1-s2){.pf-ref}.
:::

:::

::: {.pf-step #p1-s4}
But $k!$ grows faster than any exponential $e^{ck}$, so this is impossible for large $k$.

::: pf-proof
$k!/e^{ck} \to \infty$ as $k \to \infty$.
:::

:::

::: {.pf-step #p1-s5}
Hence $1/\abs{\Gamma(s)}$ is not $O(e^{c\abs{s}})$ for any $c > 0$.

::: pf-proof
step [](#p1-s3){.pf-ref} and step [](#p1-s4){.pf-ref}.
:::

:::

:::

**(b).**

::: pf

::: pf-step
Suppose such an $F$ exists, with simple zeros at $0, -1, -2, \ldots$ and nowhere else.

::: pf-proof
assume for contradiction.
:::

:::

::: {.pf-step #p2-s2}
$F$ has order at most $1$, and $F(s) = e^{as+b}\, s \prod_{n=1}^{\infty}\left(1 + \frac{s}{n}\right)e^{-s/n}$ for some constants $a, b \in \CC$.

::: pf-proof
$F = O(e^{c\abs{s}})$ gives order at most $1$. Hadamard's factorization theorem for order at most $1$ gives $F = e^{P} E$ with $P$ a polynomial of degree at most $1$ and $E$ the canonical product of genus $1$ over the zeros $0, -1, -2, \ldots$, which is the displayed product.
:::

:::

::: {.pf-step #p2-s3}
$1/\Gamma(s) = e^{-(a - \gamma)s - b}\, F(s)$.

::: pf-proof
Step [](#p2-s2){.pf-ref} and the product formula $1/\Gamma(s) = s e^{\gamma s}\prod_{n \ge 1}(1 + s/n)e^{-s/n}$.
:::

:::

::: {.pf-step #p2-s4}
$1/\abs{\Gamma(s)} = O(e^{c'\abs{s}})$ with $c' = c + \abs{a - \gamma}$.

::: pf-proof
Step [](#p2-s3){.pf-ref} and $F = O(e^{c\abs{s}})$.
:::

:::

::: {.pf-step #p2-s5}
Hence no such $F$ exists.

::: pf-proof
Step [](#p2-s4){.pf-ref} contradicts step [](#p1-s5){.pf-ref}.
:::

:::

::: pf-qed
Step [](#p1-s5){.pf-ref} (a) and step [](#p2-s5){.pf-ref} (b).
:::

:::
:::
