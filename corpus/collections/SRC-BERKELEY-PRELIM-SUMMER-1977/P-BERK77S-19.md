---
schema: qual/card@1
id: P-BERK77S-19
kind: problem
title: A square root of $-1$ modulo an odd prime forces $p\equiv1\pmod4$
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
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    A solution x has multiplicative order exactly four in F_p^×:
    x^4=1 while x^2=-1≠1 because p is odd. Lagrange's theorem then makes
    4 divide p-1.
---

::: {.problem}
Let $p$ be an odd prime. If
\[
x^2\equiv-1\pmod p
\]
has a solution, prove that
\[
p\equiv1\pmod4.
\]
:::

::: {.solution}

::: pf

::: pf-step

A solution $x$ of
$$
x^2\equiv-1\pmod p
$$
represents a nonzero element of $\FF_p$.

::: pf-proof

If $x\equiv0\pmod p$, then $x^2\equiv0\pmod p$, which cannot equal
$-1$ modulo the prime $p$. Hence
$$
x\in\FF_p^\times.
$$

:::

:::

::: {.pf-step #s2}

The multiplicative order of $x$ in $\FF_p^\times$ is exactly $4$.

::: pf-proof

Squaring the congruence gives
$$
x^4\equiv1\pmod p,
$$
so the order of $x$ divides $4$. It is not $1$, because then
$x^2\equiv1$. It is not $2$, because the hypothesis gives
$$
x^2\equiv-1\not\equiv1\pmod p,
$$
where the inequality uses that $p$ is odd. Therefore the order is $4$.

:::

:::

::: {.pf-step #s3}

One has
$$
4\mid(p-1).
$$

::: pf-proof

The group $\FF_p^\times$ has order $p-1$. By step [](#s2){.pf-ref}, it contains an
element of order $4$. Lagrange's theorem implies that the order of an
element divides the order of the finite group, so
$$
4\mid(p-1).
$$

:::

:::

::: {.pf-step #s4}

Therefore
$$
\boxed{
p\equiv1\pmod4.
}
$$

::: pf-proof

The divisibility statement in step [](#s3){.pf-ref} is equivalent to the displayed
congruence.

:::

:::

::: pf-qed

Step [](#s4){.pf-ref} is the required conclusion.

:::

:::

:::
