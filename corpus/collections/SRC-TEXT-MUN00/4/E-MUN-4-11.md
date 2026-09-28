---
schema: qual/card@1
id: E-MUN-4-11
kind: problem
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
<1>1. (a) If $m$ is odd, then $m = 2n + 1$ for some $n \in \ZZ$.

<2>1. There is $n \in \ZZ$ with $n < m/2 < n + 1$.

::: {.proof}
Let $n$ be the largest integer with $n \le m/2$. Since $m$ is odd, $m/2 \notin \ZZ$, so $n < m/2 < n + 1$.
:::

<2>2. Q.E.D.

::: {.proof}
By step <2>1, $2n < m < 2n + 2$. The only integer strictly between $2n$ and $2n + 2$ is $2n + 1$, so $m = 2n + 1$.
:::

<1>2. (b) If $p$ and $q$ are odd, then $pq$ and $p^n$ are odd for every $n \in \ZZ_+$.

<2>1. $pq$ is odd.

::: {.proof}
By step <1>1, $p = 2a + 1$ and $q = 2b + 1$ with $a, b \in \ZZ$. Then $pq = 2(2ab + a + b) + 1$, and $pq/2 = (2ab + a + b) + \tfrac12 \notin \ZZ$.
:::

<2>2. Q.E.D.

::: {.proof}
Step <2>1 gives the claim for $pq$. For $p^n$, induct on $n$: $p^1 = p$ is odd, and if $p^n$ is odd then $p^{n+1} = p^n \cdot p$ is odd by step <2>1.
:::

<1>3. (c) If $a > 0$ is rational, then $a = m/n$ with $m, n \in \ZZ_+$ not both even.

<2>1. Let $n$ be the smallest element of $\{x \in \ZZ_+ \mid xa \in \ZZ_+\}$ and put $m = na$. Then $a = m/n$ with $m, n \in \ZZ_+$.

::: {.proof}
Write $a = r/s$ with $r, s \in \ZZ_+$. Then $s \cdot a = r \in \ZZ_+$, so the set is nonempty, and by the well-ordering of $\ZZ_+$ it has a smallest element.
:::

<2>2. Q.E.D.

::: {.proof}
If $m$ and $n$ were both even, then $n/2 \in \ZZ_+$ and $(n/2)a = m/2 \in \ZZ_+$ with $n/2 < n$, which contradicts the minimality of $n$ in step <2>1.
:::

<1>4. (d) $\sqrt 2$ is irrational.

<2>1. Assume $\sqrt 2$ is rational. Then $\sqrt 2 = m/n$ with $m, n \in \ZZ_+$ not both even.

::: {.proof}
Apply step <1>3 to $a = \sqrt 2 > 0$.
:::

<2>2. $m$ is even.

::: {.proof}
From step <2>1, $m^2 = 2n^2$, so $m^2$ is even. If $m$ were odd, then $m^2$ would be odd by step <1>2.
:::

<2>3. $n$ is even.

::: {.proof}
By step <2>2, $m = 2k$ with $k \in \ZZ_+$, so $4k^2 = 2n^2$ and $n^2 = 2k^2$ is even. If $n$ were odd, then $n^2$ would be odd by step <1>2.
:::

<2>4. Q.E.D.

::: {.proof}
Steps <2>2 and <2>3 contradict the choice of $m$ and $n$ in step <2>1, so $\sqrt 2$ is irrational.
:::

<1>5. Q.E.D.

::: {.proof}
Steps <1>1 through <1>4 prove parts (a) through (d).
:::
:::
