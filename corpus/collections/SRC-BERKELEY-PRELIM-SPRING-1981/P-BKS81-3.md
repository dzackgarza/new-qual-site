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
<1>1. If $a\le0$, then
$$
a^2-a+1>0.
$$

::: {.proof}
In an ordered integral domain, squares are nonnegative, so $a^2\ge0$. The
assumption $a\le0$ gives $-a\ge0$, while $1>0$. Hence
$$
a^2-a+1=a^2+(-a)+1>0.
$$
:::

<1>2. If $0<a<1$, then
$$
a^2-a+1>0.
$$

::: {.proof}
One has $a^2\ge0$ and $1-a>0$. Therefore
$$
a^2-a+1=a^2+(1-a)>0.
$$
:::

<1>3. If $a\ge1$, then
$$
a^2-a+1>0.
$$

::: {.proof}
Now $a>0$ and $a-1\ge0$, so
$$
a(a-1)\ge0.
$$
Consequently
$$
a^2-a+1=a(a-1)+1>0.
$$
:::

<1>4. Therefore
$$
\boxed{a^2-a+1>0}
$$
for every $a\in D$.

::: {.proof}
By trichotomy, every $a$ lies in exactly one of the ranges treated in steps
<1>1--<1>3.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is the required inequality.
:::
:::
