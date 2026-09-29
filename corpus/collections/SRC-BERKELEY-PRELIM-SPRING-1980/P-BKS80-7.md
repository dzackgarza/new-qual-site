---
schema: qual/card@1
id: P-BKS80-7
kind: problem
title: If $2^n+n^2$ is prime then $n\equiv3\pmod6$
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-13}
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: Checked the parity obstruction and the modulo-three obstruction for odd n not divisible by three.
---

::: {.problem}
Let $n\ge2$ be an integer such that $2^n+n^2$ is prime.
Prove that
\[
n\equiv3\pmod6.
\]
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

The integer $n$ is odd.

::: pf-proof

If $n$ were even, then both $2^n$ and $n^2$ would be even. Hence
$$
2^n+n^2
$$
would be even. Since $n\ge2$, this number is greater than $2$, so it
would not be prime. Therefore $n$ is odd.

:::

:::

::: {.pf-step #s2}

The integer $n$ is divisible by $3$.

::: pf-proof

Suppose instead that $3\nmid n$. Then
$$
n^2\equiv1\pmod3.
$$
By step [](#s1){.pf-ref}, $n$ is odd, so
$$
2^n\equiv(-1)^n\equiv-1\pmod3.
$$
Therefore
$$
2^n+n^2\equiv0\pmod3.
$$
An odd integer $n\ge2$ not divisible by $3$ must satisfy $n\ge5$, so
$2^n+n^2>3$. Thus the displayed divisibility by $3$ contradicts the
assumed primality. Hence $3\mid n$.

:::

:::

::: {.pf-step #s3}

One has
$$
\boxed{n\equiv3\pmod6.}
$$

::: pf-proof

By step [](#s1){.pf-ref}, $n$ is odd, and by step [](#s2){.pf-ref}, $3\mid n$. The odd multiples
of $3$ are exactly the integers congruent to $3$ modulo $6$.

:::

:::

::: pf-qed

Step [](#s3){.pf-ref} is the required congruence.

:::

:::

:::
