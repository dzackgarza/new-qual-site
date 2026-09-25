---
schema: qual/card@1
id: P-BKS10-6B
kind: problem
title: Last decimal digit of a power tower of sevens
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored UC Berkeley Spring 2010 preliminary-exam solution packet, which reproduces the problem statement before its solution.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked the exponent modulo 4 and the resulting power of 7 modulo 10.
---

::: {.problem}
Find the last decimal digit of
\[
7^{\,7^{\,7^7}}.
\]
:::

::: {.solution}
Let
$$
E\coloneqq7^{7^7}.
$$

<1>1. One has
$$
E\equiv3\pmod4.
$$

::: {.proof}
Since
$$
7\equiv3\pmod4
$$
and $7^7$ is odd,
$$
E
=
7^{7^7}
\equiv
3^{7^7}
\equiv
3
\pmod4.
$$
:::

<1>2. Powers of $7$ modulo $10$ have period $4$.

::: {.proof}
Directly,
$$
7^1\equiv7,
\qquad
7^2\equiv9,
\qquad
7^3\equiv3,
\qquad
7^4\equiv1
\pmod{10}.
$$
Multiplication by $7^4\equiv1$ repeats the cycle.
:::

<1>3. The last decimal digit of the given power tower is
$$
\boxed{3}.
$$

::: {.proof}
By step <1>1,
$$
E\equiv3\pmod4.
$$
By the period in step <1>2,
$$
7^E
\equiv
7^3
\equiv
3
\pmod{10}.
$$
Thus the last decimal digit is $3$.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 gives the requested digit.
:::
:::
