---
schema: qual/card@1
id: E-SS6.EX-12
kind: exercise
title: "SS 6.12: Growth observations about the reciprocal Gamma function"
classification:
  areas:
  - complex-analysis
  topics: ['Gamma Function', 'Zeta Function', 'Mellin Transform']
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: exercise
12. This exercise gives two simple observations about $1 / \Gamma$ (a) Show that $1 / | \Gamma ( s ) |$ is not $O ( e ^ { c | s | } )$ for any $c > 0$ . [Hint: If $s = - k - 1 / 2$ where k is a positive integer, then $| 1 / \Gamma ( s ) | \geq k ! / \pi . ]$

(b) Show that there is no entire function $F ( s )$ with $F ( s ) = O ( e ^ { c \left| { s } \right| } )$ that has simple zeros at $s = 0 , - 1 , - 2 , . . . , - n , . . . ,$ and that vanishes nowhere else.
:::

::: {.solution}
**(a).**

<1>1. For $s = -k - 1/2$ (with $k$ a positive integer), $|1/\Gamma(s)| \ge k!/\pi$.
Proof: the hint (using the reflection formula $\Gamma(s)\Gamma(1-s) = \pi/\sin(\pi s)$, which gives $|\Gamma(-k-1/2)| \le \pi/k!$).

<1>2. If $1/|\Gamma(s)| = O(e^{c|s|})$, then there is $C$ with $1/|\Gamma(s)| \le C e^{c|s|}$ for all $s$.
Proof: definition of big-O.

<1>3. At $s = -k - 1/2$, this gives $k!/\pi \le C e^{c(k + 1/2)}$ for all $k$.
Proof: <1>1 and <1>2.

<1>4. But $k!$ grows faster than any exponential $e^{ck}$, so this is impossible for large $k$.
Proof: $k!/e^{ck} \to \infty$ as $k \to \infty$.

<1>5. Hence $1/|\Gamma(s)|$ is not $O(e^{c|s|})$ for any $c > 0$.
Proof: <1>3 and <1>4.

**(b).**

<1>1. Suppose such an $F$ exists, with simple zeros at $0, -1, -2, \ldots$ and nowhere else.
Proof: assume for contradiction.

<1>2. Then $F(s)/\Gamma(s)$ is entire with no zeros (the zeros of $F$ match the poles of $1/\Gamma$, and $1/\Gamma$ has simple zeros exactly at $0, -1, -2, \ldots$).
Proof: $1/\Gamma$ is entire with simple zeros at the non-positive integers, matching the zeros of $F$.

<1>3. Hence $G(s) = F(s)/\Gamma(s)$ is an entire function with no zeros, so $1/G$ is entire.
Proof: <1>2.

<1>4. By (a), $1/|\Gamma(s)|$ is not $O(e^{c|s|})$, but $F(s) = O(e^{c|s|})$; this forces $G$ to grow in a way that contradicts the Hadamard factorization theorem (an entire function of order $\le 1$ with no zeros must be $e^{as+b}$, but then $F = e^{as+b}\Gamma$ would not be $O(e^{c|s|})$).
Proof: <1>3 and (a); more directly, if $F = O(e^{c|s|})$ then $F$ has order $\le 1$, so by Hadamard factorization $F(s) = e^{as+b}\prod_n (1 - s/z_n)$; but the product over the zeros $0, -1, -2, \ldots$ is $1/\Gamma(s)$ (up to a factor), and $1/\Gamma$ is not $O(e^{c|s|})$, contradiction.

<1>5. Hence no such $F$ exists.
Proof: <1>4.

<1>6. Q.E.D.
Proof: <1>5 (a) and <1>5 (b).
:::
