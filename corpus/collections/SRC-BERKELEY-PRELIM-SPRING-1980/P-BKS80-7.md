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
<1>1. The integer $n$ is odd.

::: {.proof}
If $n$ were even, then both $2^n$ and $n^2$ would be even. Hence
$$
2^n+n^2
$$
would be even. Since $n\ge2$, this number is greater than $2$, so it
would not be prime. Therefore $n$ is odd.
:::

<1>2. The integer $n$ is divisible by $3$.

::: {.proof}
Suppose instead that $3\nmid n$. Then
$$
n^2\equiv1\pmod3.
$$
By step <1>1, $n$ is odd, so
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

<1>3. One has
$$
\boxed{n\equiv3\pmod6.}
$$

::: {.proof}
By step <1>1, $n$ is odd, and by step <1>2, $3\mid n$. The odd multiples
of $3$ are exactly the integers congruent to $3$ modulo $6$.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 is the required congruence.
:::
:::
