---
schema: qual/card@1
id: P-BKF08-9B
kind: problem
title: Primes of the form $2^n+n^2$ force $n\equiv3\pmod6$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against Problem 9B of the retained Berkeley Fall 2008 preliminary-exam solution packet f08solutions.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked the parity obstruction and the reduction modulo 3, including
    the use of n>=2 to exclude the prime value 3.
---

::: {.problem}
Let $n\ge2$ be an integer such that $2^n+n^2$ is prime.
Show that
$$
n\equiv3\pmod6.
$$
:::

::: {.solution}
Put
$$
p\coloneqq2^n+n^2,
$$
which is prime by hypothesis.

<1>1. The integer $n$ is odd.

::: {.proof}
If $n$ were even, then both $2^n$ and $n^2$ would be even, so $p$ would
be even. Since $n\ge2$,
$$
p=2^n+n^2\ge2^2+2^2=8>2,
$$
so an even value of $p$ could not be prime. Therefore $n$ is odd.
:::

<1>2. The integer $n$ is divisible by $3$.

::: {.proof}
Suppose instead that $3\nmid n$. Then
$$
n^2\equiv1\pmod3.
$$
Since $2\equiv-1\pmod3$ and $n$ is odd by step <1>1,
$$
2^n\equiv(-1)^n\equiv-1\pmod3.
$$
Consequently
$$
p=2^n+n^2\equiv-1+1\equiv0\pmod3.
$$
But $p\ge8>3$, so a positive integer divisible by $3$ cannot be prime.
This contradiction proves $3\mid n$.
:::

<1>3. Therefore
$$
\boxed{n\equiv3\pmod6}.
$$

::: {.proof}
By step <1>2, $n$ is congruent to either $0$ or $3$ modulo $6$.
Step <1>1 excludes the even congruence class $0$, leaving only
$n\equiv3\pmod6$.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 is the required congruence.
:::
:::
