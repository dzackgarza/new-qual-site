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
12. This exercise gives two simple observations about $1 / \Gamma$ (a) Show that $1 / | \Gamma ( s ) |$ is not $O ( e ^ { c | s | } )$ for any $c > 0$ . [Hint: If $s = - k - 1 / 2$ where k is a positive integer, then $| 1 / \Gamma ( s ) | \geq k ! / \pi . ]$

(b) Show that there is no entire function $F ( s )$ with $F ( s ) = O ( e ^ { c \left| { s } \right| } )$ that has simple zeros at $s = 0 , - 1 , - 2 , . . . , - n , . . . ,$ and that vanishes nowhere else.
:::

::: {.solution}
**(a).**

::: pf

::: {.pf-step #p1-s1}
For $s = -k - 1/2$ (with $k$ a positive integer), $|1/\Gamma(s)| \ge k!/\pi$.

::: pf-proof
the hint (using the reflection formula $\Gamma(s)\Gamma(1-s) = \pi/\sin(\pi s)$, which gives $|\Gamma(-k-1/2)| \le \pi/k!$).
:::

:::

::: {.pf-step #p1-s2}
If $1/|\Gamma(s)| = O(e^{c|s|})$, then there is $C$ with $1/|\Gamma(s)| \le C e^{c|s|}$ for all $s$.

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
Hence $1/|\Gamma(s)|$ is not $O(e^{c|s|})$ for any $c > 0$.

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
Then $F(s)/\Gamma(s)$ is entire with no zeros (the zeros of $F$ match the poles of $1/\Gamma$, and $1/\Gamma$ has simple zeros exactly at $0, -1, -2, \ldots$).

::: pf-proof
$1/\Gamma$ is entire with simple zeros at the non-positive integers, matching the zeros of $F$.
:::

:::

::: {.pf-step #p2-s3}
Hence $G(s) = F(s)/\Gamma(s)$ is an entire function with no zeros, so $1/G$ is entire.

::: pf-proof
step [](#p2-s2){.pf-ref}.
:::

:::

::: {.pf-step #p2-s4}
By (a), $1/|\Gamma(s)|$ is not $O(e^{c|s|})$, but $F(s) = O(e^{c|s|})$; this forces $G$ to grow in a way that contradicts the Hadamard factorization theorem (an entire function of order $\le 1$ with no zeros must be $e^{as+b}$, but then $F = e^{as+b}\Gamma$ would not be $O(e^{c|s|})$).

::: pf-proof
step [](#p2-s3){.pf-ref} and (a); more directly, if $F = O(e^{c|s|})$ then $F$ has order $\le 1$, so by Hadamard factorization $F(s) = e^{as+b}\prod_n (1 - s/z_n)$; but the product over the zeros $0, -1, -2, \ldots$ is $1/\Gamma(s)$ (up to a factor), and $1/\Gamma$ is not $O(e^{c|s|})$, contradiction.
:::

:::

::: {.pf-step #p2-s5}
Hence no such $F$ exists.

::: pf-proof
step [](#p2-s4){.pf-ref}.
:::

:::

::: pf-qed
Step [](#p1-s5){.pf-ref} (a) and step [](#p2-s5){.pf-ref} (b).
:::

:::
:::
