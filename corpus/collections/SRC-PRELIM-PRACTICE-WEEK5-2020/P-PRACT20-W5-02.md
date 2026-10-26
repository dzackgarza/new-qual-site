---
schema: qual/card@1
id: P-PRACT20-W5-02
kind: problem
title: Units digit of $2019^{2019}$
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Rewrote the statement in clean LaTeX with spacing around inline math, checked against Week5_solns.pdf (Problem 2).
---

::: {.problem}
What is the units digit of $2019^{2019}$?
:::

::: pf

::: pf-step

Modulo $10$,
\[
2019\equiv9.
\]


::: pf-proof

The difference $2019-9=2010$ is divisible by $10$.

:::

:::

::: pf-step

One has
\[
9^2\equiv1\pmod{10}.
\]


::: pf-proof

Indeed,
\[
9^2=81\equiv1\pmod{10}.
\]

:::

:::

::: pf-step

Therefore
\[
2019^{2019}\equiv9\pmod{10}.
\]


::: pf-proof

Since
\[
2019=2\cdot1009+1,
\]
steps <1>1 and <1>2 give
\[
2019^{2019}
\equiv
9^{2019}
=(9^2)^{1009}9
\equiv
1^{1009}9
\equiv9
\pmod{10}.
\]

:::

:::

::: pf-step

The units digit is
\[
\boxed{9}.
\]


::: pf-proof

The units digit of an integer is its residue modulo $10$ in
$\{0,1,\dots,9\}$, and step <1>3 gives residue $9$.

:::

:::

::: pf-qed

Step <1>4 gives the requested digit.

:::

:::
