---
schema: qual/card@1
id: P-UCLAB18F-01
kind: problem
title: Divergence preserved by a nonlinear summand transform
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
  note: Checked against the vendored UCLA Basic Examination, Fall 2018, `assets/attachments/basic-18F.pdf`.
---

::: {.problem}
Let $(a_n)_{n\ge1}$ be nonnegative and suppose $\sum_{n\ge1}a_n$ diverges.
Show that
$$
\sum_{n\ge1}\frac{a_n}{2a_n+1}
$$
also diverges.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

If
$$
a_n\ge1
$$
for infinitely many $n$, then
$$
\sum_{n=1}^{\infty}\frac{a_n}{2a_n+1}
$$
diverges.


::: pf-proof

Whenever
$$
a_n\ge1,
$$
one has
$$
2a_n+1
\le
3a_n,
$$
and therefore
$$
\frac{a_n}{2a_n+1}
\ge
\frac13.
$$
Thus the transformed series has infinitely many terms at least $1/3$.
Since all terms are nonnegative, its partial sums are unbounded.

:::

:::

::: {.pf-step #s1-2}

Suppose instead that
$$
a_n<1
$$
for all sufficiently large $n$.
Then for all sufficiently large $n$,
$$
\frac{a_n}{2a_n+1}
\ge
\frac{a_n}{3}.
$$


::: pf-proof

If
$$
0\le a_n<1,
$$
then
$$
2a_n+1<3.
$$
Hence
$$
\frac{a_n}{2a_n+1}
\ge
\frac{a_n}{3}.
$$

:::

:::

::: {.pf-step #s1-3}

In the case of step [](#s1-2){.pf-ref}, the transformed series diverges.


::: pf-proof

Choose $N$ such that
$$
a_n<1
$$
for all $n\ge N$.
Because
$$
\sum_{n=1}^{\infty}a_n
$$
diverges and the terms are nonnegative,
$$
\sum_{n=N}^{\infty}a_n
=
\infty.
$$
By step [](#s1-2){.pf-ref},
$$
\sum_{n=N}^{M}
\frac{a_n}{2a_n+1}
\ge
\frac13
\sum_{n=N}^{M}a_n.
$$
The right side tends to $+\infty$ as $M\to\infty$.
Thus the transformed series diverges.

:::

:::

::: {.pf-step #s1-4}

Therefore
$$
\boxed{
\sum_{n=1}^{\infty}\frac{a_n}{2a_n+1}
\text{ diverges}.
}
$$


::: pf-proof

Either $a_n\ge1$ infinitely often, in which case step [](#s1-1){.pf-ref} applies, or $a_n<1$ eventually, in which case step [](#s1-3){.pf-ref} applies.
These cases exhaust all possibilities.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} is the required conclusion.

:::

:::

:::
