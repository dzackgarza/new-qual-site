---
schema: qual/card@1
id: P-BKF90-4
kind: problem
title: Weighted mean-value theorem for an integral
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 4 in the deterministic MinerU Flash extraction assets/attachments/Fall90_extracted.md.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: >-
    Bounded the weighted integral between one third of the minimum and maximum
    of f, then used the intermediate value theorem.
---

::: {.problem}
Let $f$ be continuous and real-valued.
Show that
\[
\int_0^1 f(x)x^2\,dx=\frac13 f(\xi)
\]
for some $\xi\in[0,1]$.
:::

::: {.solution}

::: pf

::: pf-step

Let
$$
m\coloneqq\min_{x\in[0,1]}f(x),
\qquad
M\coloneqq\max_{x\in[0,1]}f(x).
$$
These numbers exist.

::: pf-proof

The function $f$ is continuous on the compact interval $[0,1]$, so the extreme value theorem applies.

:::

:::

::: {.pf-step #s2}

One has
$$
m
\le
3\int_0^1 f(x)x^2\,dx
\le
M.
$$

::: pf-proof

For every $x\in[0,1]$,
$$
m\le f(x)\le M.
$$
Since $x^2\ge0$,
$$
mx^2\le f(x)x^2\le Mx^2.
$$
Integrating and using
$$
\int_0^1x^2\,dx=\frac13
$$
gives
$$
\frac m3
\le
\int_0^1 f(x)x^2\,dx
\le
\frac M3,
$$
which is the claimed inequality after multiplication by $3$.

:::

:::

::: {.pf-step #s3}

There exists $\xi\in[0,1]$ such that
$$
f(\xi)=3\int_0^1 f(x)x^2\,dx.
$$

::: pf-proof

By step [](#s2){.pf-ref}, the right-hand side lies in the interval $[m,M]$. Since $f$ is continuous on the connected interval $[0,1]$ and attains both $m$ and $M$, the intermediate value theorem shows that $f$ attains every value in $[m,M]$.

:::

:::

::: {.pf-step #s4}

Therefore
$$
\boxed{\int_0^1 f(x)x^2\,dx=\frac13f(\xi)}
$$
for some $\xi\in[0,1]$.

::: pf-proof

This is step [](#s3){.pf-ref} divided by $3$.

:::

:::

::: pf-qed

Step [](#s4){.pf-ref} is the required identity.

:::

:::

:::
