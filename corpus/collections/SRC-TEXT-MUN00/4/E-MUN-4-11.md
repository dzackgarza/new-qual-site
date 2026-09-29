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

::: pf

::: {.pf-step #s1}

(a) If $m$ is odd, then $m = 2n + 1$ for some $n \in \ZZ$.

::: pf-proof

::: {.pf-step #s1-1}

There is $n \in \ZZ$ with $n < m/2 < n + 1$.

::: pf-proof

Let $n$ be the largest integer with $n \le m/2$. Since $m$ is odd, $m/2 \notin \ZZ$, so $n < m/2 < n + 1$.

:::

:::

::: pf-qed

By step [](#s1-1){.pf-ref}, $2n < m < 2n + 2$. The only integer strictly between $2n$ and $2n + 2$ is $2n + 1$, so $m = 2n + 1$.

:::

:::

:::

::: {.pf-step #s2}

(b) If $p$ and $q$ are odd, then $pq$ and $p^n$ are odd for every $n \in \ZZ_+$.

::: pf-proof

::: {.pf-step #s2-1}

$pq$ is odd.

::: pf-proof

By step [](#s1){.pf-ref}, $p = 2a + 1$ and $q = 2b + 1$ with $a, b \in \ZZ$. Then $pq = 2(2ab + a + b) + 1$, and $pq/2 = (2ab + a + b) + \tfrac12 \notin \ZZ$.

:::

:::

::: pf-qed

Step [](#s2-1){.pf-ref} gives the claim for $pq$. For $p^n$, induct on $n$: $p^1 = p$ is odd, and if $p^n$ is odd then $p^{n+1} = p^n \cdot p$ is odd by step [](#s2-1){.pf-ref}.

:::

:::

:::

::: {.pf-step #s3}

(c) If $a > 0$ is rational, then $a = m/n$ with $m, n \in \ZZ_+$ not both even.

::: pf-proof

::: {.pf-step #s3-1}

Let $n$ be the smallest element of $\{x \in \ZZ_+ \mid xa \in \ZZ_+\}$ and put $m = na$. Then $a = m/n$ with $m, n \in \ZZ_+$.

::: pf-proof

Write $a = r/s$ with $r, s \in \ZZ_+$. Then $s \cdot a = r \in \ZZ_+$, so the set is nonempty, and by the well-ordering of $\ZZ_+$ it has a smallest element.

:::

:::

::: pf-qed

If $m$ and $n$ were both even, then $n/2 \in \ZZ_+$ and $(n/2)a = m/2 \in \ZZ_+$ with $n/2 < n$, which contradicts the minimality of $n$ in step [](#s3-1){.pf-ref}.

:::

:::

:::

::: {.pf-step #s4}

(d) $\sqrt 2$ is irrational.

::: pf-proof

::: {.pf-step #s4-1}

Assume $\sqrt 2$ is rational. Then $\sqrt 2 = m/n$ with $m, n \in \ZZ_+$ not both even.

::: pf-proof

Apply step [](#s3){.pf-ref} to $a = \sqrt 2 > 0$.

:::

:::

::: {.pf-step #s4-2}

$m$ is even.

::: pf-proof

From step [](#s4-1){.pf-ref}, $m^2 = 2n^2$, so $m^2$ is even. If $m$ were odd, then $m^2$ would be odd by step [](#s2){.pf-ref}.

:::

:::

::: {.pf-step #s4-3}

$n$ is even.

::: pf-proof

By step [](#s4-2){.pf-ref}, $m = 2k$ with $k \in \ZZ_+$, so $4k^2 = 2n^2$ and $n^2 = 2k^2$ is even. If $n$ were odd, then $n^2$ would be odd by step [](#s2){.pf-ref}.

:::

:::

::: pf-qed

Steps [](#s4-2){.pf-ref} and [](#s4-3){.pf-ref} contradict the choice of $m$ and $n$ in step [](#s4-1){.pf-ref}, so $\sqrt 2$ is irrational.

:::

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref}, [](#s3){.pf-ref} and [](#s4){.pf-ref} prove parts (a) through (d).

:::

:::

:::
