---
schema: qual/card@1
id: E-MUN-4-11
kind: exercise
title: Even and odd integers and irrationality of $\sqrt{2}$
classification:
  areas:
  - topology
  topics:
  - Integers and Real Numbers
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.exercise}

Given $m \in \mathbb{Z}$, we say that $m$ is even if $m / 2 \in \mathbb{Z}$, and $m$ is odd otherwise.

(a) Show that if $m$ is odd, $m = 2n + 1$ for some $n \in \mathbb{Z}$ . [Hint: Choose $n$ so that $n < m / 2 < n + 1$ .]

(b) Show that if $p$ and $q$ are odd, so are $p \cdot q$ and $p^n$, for any $n \in \mathbb{Z}_+$ .

(c) Show that if $a > 0$ is rational, then $a = m / n$ for some $m, n \in \mathbb{Z}_+$ where not both $m$ and $n$ are even.
[Hint: Let $n$ be the smallest element of the set $\{x \mid x \in \mathbb{Z}_+ \text{ and } x \cdot a \in \mathbb{Z}_+\}$ .]

(d) Theorem.
$\sqrt{2}$ is irrational.
:::

::: {.solution}
**Goal.** Prove the parity facts and deduce that $\sqrt 2$ is irrational.

<1>1. (a) If $m$ is odd, then $m = 2n + 1$ for some $n \in \ZZ$.
<2>1. Choose $n \in \ZZ$ with $n < m/2 < n + 1$.
::: {.proof}
such an integer $n$ exists (the floor of $m/2$).
:::
<2>2. Then $2n < m < 2n + 2$, so $m = 2n + 1$.
::: {.proof}
$m$ is an integer strictly between the consecutive even integers $2n$ and $2n + 2$, so it equals the unique odd integer $2n + 1$ between them.
:::

<1>2. (b) If $p$ and $q$ are odd, then $pq$ and $p^n$ are odd.
<2>1. Write $p = 2a + 1$, $q = 2b + 1$.
::: {.proof}
by (a).
:::
<2>2. $pq = (2a+1)(2b+1) = 4ab + 2a + 2b + 1 = 2(2ab + a + b) + 1$, which is odd.
::: {.proof}
it has the form $2n + 1$.
:::
<2>3. $p^n$ is odd for all $n \in \ZZ_+$.
::: {.proof}
induction on $n$ using <1>2.2 (product of two odds is odd).
:::

<1>3. (c) If $a > 0$ is rational, then $a = m/n$ with $m, n \in \ZZ_+$ not both even.
<2>1. Let $n$ be the smallest positive integer with $n a \in \ZZ_+$, and set $m = n a$.
::: {.proof}
such an $n$ exists since $a$ is rational and positive.
:::
<2>2. $m$ and $n$ are not both even.
::: {.proof}
if both were even, then $m/2$ and $n/2$ are positive integers with $(n/2) a = m/2 \in \ZZ_+$, contradicting the minimality of $n$.
:::

<1>4. (d) $\sqrt 2$ is irrational.
<2>1. Suppose $\sqrt 2 = m/n$ with $m, n \in \ZZ_+$ not both even.
::: {.proof}
by (c), applied to $a = \sqrt 2 > 0$.
:::
<2>2. Then $m^2 = 2n^2$, so $m^2$ is even, hence $m$ is even.
::: {.proof}
the square of an odd number is odd (by (b)), so $m^2$ even forces $m$ even.
:::
<2>3. Write $m = 2k$; then $4k^2 = 2n^2$, so $n^2 = 2k^2$ is even, hence $n$ is even.
::: {.proof}
same parity argument.
:::
<2>4. Contradiction: $m$ and $n$ are both even, contradicting <1>4.1.
::: {.proof}
<1>4.2 and <1>4.3 force both even.
:::

<1>5. Q.E.D.
::: {.proof}
<1>4.4 shows $\sqrt 2$ is irrational.
:::
:::
