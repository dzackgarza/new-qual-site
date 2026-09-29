---
schema: qual/card@1
id: P-BKS81-3
kind: problem
title: Positivity of $a^2-a+1$ in an ordered integral domain
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: Checked the three order ranges directly, without using division or completion of the square.
---

::: {.problem}
Let $D$ be an ordered integral domain and $a\in D$.
Prove that
\[
a^2-a+1>0.
\]
:::

::: {.solution}
::: pf

::: {.pf-step #nonpositive-case}
If $a\le0$, then
$$
a^2-a+1>0.
$$

::: pf-proof
In an ordered integral domain, squares are nonnegative, so $a^2\ge0$. The
assumption $a\le0$ gives $-a\ge0$, while $1>0$. Hence
$$
a^2-a+1=a^2+(-a)+1>0.
$$
:::

:::

::: {.pf-step #unit-interval-case}
If $0<a<1$, then
$$
a^2-a+1>0.
$$

::: pf-proof
One has $a^2\ge0$ and $1-a>0$. Therefore
$$
a^2-a+1=a^2+(1-a)>0.
$$
:::

:::

::: {.pf-step #at-least-one-case}
If $a\ge1$, then
$$
a^2-a+1>0.
$$

::: pf-proof
Now $a>0$ and $a-1\ge0$, so
$$
a(a-1)\ge0.
$$
Consequently
$$
a^2-a+1=a(a-1)+1>0.
$$
:::

:::

::: {.pf-step #positivity-boxed}
Therefore
$$
\boxed{a^2-a+1>0}
$$
for every $a\in D$.

::: pf-proof
By trichotomy, every $a$ lies in exactly one of the ranges treated in steps
[](#nonpositive-case){.pf-ref}, [](#unit-interval-case){.pf-ref}, and [](#at-least-one-case){.pf-ref}.
:::

:::

::: pf-qed
Step [](#positivity-boxed){.pf-ref} is the required inequality.
:::

:::
:::
