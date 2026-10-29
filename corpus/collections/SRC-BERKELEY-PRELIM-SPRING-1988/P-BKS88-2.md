---
schema: qual/card@1
id: P-BKS88-2
kind: problem
title: Last digit of $23^{23^{23^{23}}}$
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
  note: Checked against the vendored UC Berkeley Spring 1988 preliminary examination.
---

::: {.problem}
Determine the last digit of
$$
23^{23^{23^{23}}}
$$
in the decimal system.
:::

::: {.solution}
Let
$$
N:=23^{23^{23^{23}}}
\qquad\text{and}\qquad
E:=23^{23^{23}}.
$$

::: pf

::: {.pf-step #exponent-modulo-four}
$E\equiv 3\pmod 4$.

::: pf-proof
Since $23\equiv 3\pmod 4$ and $23^{23}$ is odd,
$$
E=23^{23^{23}}
\equiv 3^{23^{23}}
\equiv 3
\pmod 4,
$$
because $3^m\equiv 3\pmod 4$ for every odd integer $m$.
:::

:::

::: pf-step
$N\equiv \boxed{7}\pmod{10}$.

::: pf-proof
Modulo $10$, the powers of $3$ have period $4$:
$$
3,9,7,1,3,\ldots.
$$
Since $23\equiv 3\pmod{10}$, one has
$$
N=23^E\equiv 3^E\pmod{10}.
$$
By [](#exponent-modulo-four){.pf-ref}, $E\equiv 3\pmod 4$, so
$$
3^E\equiv 3^3\equiv 7\pmod{10}.
$$
Thus the last digit of $N$ is $7$.
:::

:::

:::

:::
