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
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §4 Exercise 11, printed p. 34; parts (a)-(d)
    and both hints are stored as printed.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second
    Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 4.11,
    printed pp. 65-66 (tmp/sources/munkres-solutions-whitman.pdf). (a) is the book's
    hint: take the integer n with n < m/2 < n+1, so 2n < m < 2n+2 and the only integer
    between is 2n+1. Two steps the card had asserted are now derived: the existence of
    the largest integer below m/2 comes from E-MUN-4-9(a), and the discreteness of Z -
    that 2n < m < 2n+2 forces m = 2n+1 - now follows from [1, infinity) being inductive,
    which makes every positive integer at least 1, applied to m-2n and to 2-(m-2n).
    Whitman reaches the same discreteness through a lemma that no integer lies strictly
    between 0 and 1, proved by well-ordering.
    (b) is his product computation and induction, (c) his minimal-denominator argument
    with the well-ordering of Z_+, and (d) his parity contradiction.
---

::: {.exercise}

Given $m \in \ZZ$, we say that $m$ is even if $m / 2 \in \ZZ$, and $m$ is odd otherwise.

(a) Show that if $m$ is odd, $m = 2n + 1$ for some $n \in \ZZ$ . [Hint: Choose $n$ so that $n < m / 2 < n + 1$ .]

(b) Show that if $p$ and $q$ are odd, so are $p \cdot q$ and $p^n$, for any $n \in \ZZ_+$ .

(c) Show that if $a > 0$ is rational, then $a = m / n$ for some $m, n \in \ZZ_+$ where not both $m$ and $n$ are even.
[Hint: Let $n$ be the smallest element of the set $\{x \mid x \in \ZZ_+ \text{ and } x \cdot a \in \ZZ_+\}$ .]

(d) Theorem.
$\sqrt{2}$ is irrational.
:::

::: {.solution}
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 4.11, printed pp. 65--66** (`tmp/sources/munkres-solutions-whitman.pdf`); the four parts below are his, (a) following the book's hint to take the integer between $m/2$ and $m/2+1$, and (c) the hint to take the least $n$ with $na$ a positive integer.

::: pf

::: {.pf-step #s1}

(a) If $m$ is odd, then $m = 2n + 1$ for some $n \in \ZZ$.

::: pf-proof

::: {.pf-step #s1-1}

There is $n \in \ZZ$ with $n < m/2 < n + 1$.

::: pf-proof

Let $n$ be the largest integer with $n \le m/2$, which exists by [[E-MUN-4-9]](a). Since $m$ is odd, $m/2 \notin \ZZ$, so $n < m/2 < n + 1$.

:::

:::

::: pf-qed

By step [](#s1-1){.pf-ref}, $2n < m < 2n + 2$. Then $k=m-2n$ is an integer with $0<k<2$. Every positive integer is at least $1$, because $[1,\infty)$ is an inductive subset of $\RR$ and $\ZZ_{+}$ is contained in every inductive subset; applied to $k>0$ this gives $k\ge1$, and applied to $2-k>0$ it gives $2-k\ge1$, that is $k\le1$. Hence $k=1$ and $m = 2n + 1$.

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
