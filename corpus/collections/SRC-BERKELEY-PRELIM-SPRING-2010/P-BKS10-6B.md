---
schema: qual/card@1
id: P-BKS10-6B
kind: problem
title: Last decimal digit of $7^{7^{7^7}}$
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
$$
7^{\,7^{\,7^7}}.
$$
:::

::: {.solution}
Let
$$
E\coloneqq7^{7^7}.
$$

::: pf

::: {.pf-step #e-mod-four}
One has
$$
E\equiv3\pmod4.
$$

::: pf-proof
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

:::

::: {.pf-step #powers-of-seven-period}
Powers of $7$ modulo $10$ have period $4$.

::: pf-proof
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

:::

::: {.pf-step #last-digit}
The last decimal digit of the given power tower is
$$
\boxed{3}.
$$

::: pf-proof
By step [](#e-mod-four){.pf-ref},
$$
E\equiv3\pmod4.
$$
By the period in step [](#powers-of-seven-period){.pf-ref},
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

:::

::: pf-qed
Step [](#last-digit){.pf-ref} gives the requested digit.
:::

:::

:::
