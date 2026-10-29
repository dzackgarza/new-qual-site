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

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Modulo $10$,
$$
2019\equiv9.
$$


::: pf-proof

The difference $2019-9=2010$ is divisible by $10$.

:::

:::

::: {.pf-step #s1-2}

One has
$$
9^2\equiv1\pmod{10}.
$$


::: pf-proof

Indeed,
$$
9^2=81\equiv1\pmod{10}.
$$

:::

:::

::: {.pf-step #s1-3}

Therefore
$$
2019^{2019}\equiv9\pmod{10}.
$$


::: pf-proof

Since
$$
2019=2\cdot1009+1,
$$
steps [](#s1-1){.pf-ref} and [](#s1-2){.pf-ref} give
$$
2019^{2019}
\equiv
9^{2019}
=(9^2)^{1009}9
\equiv
1^{1009}9
\equiv9
\pmod{10}.
$$

:::

:::

::: {.pf-step #s1-4}

The units digit is
$$
\boxed{9}.
$$


::: pf-proof

The units digit of an integer is its residue modulo $10$ in
$\{0,1,\dots,9\}$, and step [](#s1-3){.pf-ref} gives residue $9$.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} gives the requested digit.

:::

:::

:::
