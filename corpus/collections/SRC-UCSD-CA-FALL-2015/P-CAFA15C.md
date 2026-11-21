---
schema: qual/card@1
id: P-CAFA15C
kind: problem
title: Polynomial with non-increasing real coefficients has no roots inside the unit disk
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
- event: source-corrected
  by: claude-opus-5.5
  date: 2026-10-31
  note: The exam states only that the coefficients are non-increasing reals; the statement
    adds a_n > 0, without which it fails (a_0 = 0, a_1 = -1 gives the root 0).
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps; checked the identity (1-z)P(z) = a_0 - W(z) with W(z) =
    sum of (a_{k-1}-a_k) z^k plus a_n z^{n+1}, the telescoping identity giving a_0 as the
    sum of the differences plus a_n, the nonnegativity of the difference coefficients, the
    bound |W| <= a_0 with strictness traced to the single term a_n |z|^{n+1} < a_n (which is
    what makes the argument work even when all a_k are equal), and hence P nonzero in the
    open disk. The argument is the card's own; no retained set is cited. No repair needed.
---

::: {.problem}
Let $a_0, a_1, \dots, a_n$ be a strictly positive, non-increasing sequence of real numbers:
$$a_0 \ge a_1 \ge a_2 \ge \cdots \ge a_n > 0.$$
Prove that the polynomial:
$$P(z) = a_0 + a_1 z + a_2 z^2 + \cdots + a_n z^n$$
has **no roots inside the open unit disk** $\abs{z} < 1$ (Eneström–Kakeya Theorem).
:::

::: {.solution}
The argument is the card's own; no retained solution set is cited on it. Write $P(z)=\sum_{k=0}^{n}a_{k}z^{k}$ with $a_{0}\ge a_{1}\ge\dots\ge a_{n}>0$.

::: pf

::: {.pf-step #identity}
$(1-z)P(z)=a_{0}-W(z)$, where $W(z)=\sum_{k=1}^{n}(a_{k-1}-a_{k})z^{k}+a_{n}z^{n+1}$, and $\sum_{k=1}^{n}(a_{k-1}-a_{k})+a_{n}=a_{0}$.

::: pf-proof
Multiplying out,
$$
(1-z)\sum_{k=0}^{n}a_{k}z^{k}=\sum_{k=0}^{n}a_{k}z^{k}-\sum_{k=0}^{n}a_{k}z^{k+1}=a_{0}+\sum_{k=1}^{n}(a_{k}-a_{k-1})z^{k}-a_{n}z^{n+1},
$$
which is $a_{0}-W(z)$. The telescoping identity $\sum_{k=1}^{n}(a_{k-1}-a_{k})=a_{0}-a_{n}$ gives the second display, and each coefficient $a_{k-1}-a_{k}\ge0$ because the sequence is non-increasing.
:::

:::

::: {.pf-step #bound}
For $\abs{z}<1$, $\ \abs{W(z)}<a_{0}$.

::: pf-proof
By the triangle inequality and the nonnegativity of the coefficients $d_{k}=a_{k-1}-a_{k}$,
$$
\abs{W(z)}\le\sum_{k=1}^{n}d_{k}\abs{z}^{k}+a_{n}\abs{z}^{n+1}\le\sum_{k=1}^{n}d_{k}+a_{n}=a_{0},
$$
using $\abs{z}^{k}\le1$ for $k\ge1$. The inequality is strict: the last term satisfies $a_{n}\abs{z}^{n+1}<a_{n}$ because $a_{n}>0$ and $\abs{z}^{n+1}<1$, and all other changes only decrease the bound further, so the total is less than $\sum_{k=1}^{n}d_{k}+a_{n}=a_{0}$.
:::

:::

::: {.pf-step #nonzero}
$P(z)\ne0$ for $\abs{z}<1$.

::: pf-proof
For such $z$ one has $1-z\ne0$, and by steps [](#identity){.pf-ref} and [](#bound){.pf-ref},
$$
\abs{(1-z)P(z)}=\abs{a_{0}-W(z)}\ge a_{0}-\abs{W(z)}>0,
$$
so $(1-z)P(z)\ne0$ and therefore $P(z)\ne0$.
:::

:::

::: {.pf-step}
$P$ has no root inside the open unit disk.

::: pf-proof
Step [](#nonzero){.pf-ref} is the assertion for every $z$ with $\abs{z}<1$.
:::

:::

:::
:::
