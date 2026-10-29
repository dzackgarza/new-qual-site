---
schema: qual/card@1
id: P-UCLAB07F-08
kind: problem
title: 'Divergence of $\sum a_n/(1+a_n)$ when $\sum a_n$ diverges'
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 8 of the retained UCLA Basic Examination, Fall 2007 PDF.
---

::: {.problem}
Suppose $a_n\ge0$ and $\sum_{n=1}^{\infty}a_n=\infty$.
Does it follow that $$\sum_{n=1}^{\infty}\frac{a_n}{1+a_n}=\infty?$$ Prove your answer.
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
\sum_{n=1}^{\infty}\frac{a_n}{1+a_n}=\infty.
$$


::: pf-proof

Whenever $a_n\ge1$,
$$
\frac{a_n}{1+a_n}
\ge
\frac12.
$$
Thus the transformed series has infinitely many terms at least $1/2$, so its partial sums are unbounded.

:::

:::

::: {.pf-step #s1-2}

If
$$
a_n<1
$$
for all sufficiently large $n$, then
$$
\frac{a_n}{1+a_n}\ge\frac{a_n}{2}
$$
for all sufficiently large $n$.


::: pf-proof

If $0\le a_n<1$, then
$$
1+a_n\le2.
$$
Since $a_n\ge0$,
$$
\frac{a_n}{1+a_n}\ge\frac{a_n}{2}.
$$

:::

:::

::: {.pf-step #s1-3}

In the case of step [](#s1-2){.pf-ref},
$$
\sum_{n=1}^{\infty}\frac{a_n}{1+a_n}=\infty.
$$


::: pf-proof

Choose $N$ such that $a_n<1$ for all $n\ge N$. By hypothesis,
$$
\sum_{n=N}^{\infty}a_n=\infty,
$$
because removing finitely many terms does not change divergence. By step [](#s1-2){.pf-ref},
$$
\sum_{n=N}^{M}\frac{a_n}{1+a_n}
\ge
\frac12\sum_{n=N}^{M}a_n.
$$
The right side tends to $+\infty$ as $M\to\infty$, so the transformed series diverges.

:::

:::

::: {.pf-step #s1-4}

Therefore
$$
\boxed{
\sum_{n=1}^{\infty}\frac{a_n}{1+a_n}=\infty
}.
$$


::: pf-proof

Either $a_n\ge1$ for infinitely many $n$, in which case step [](#s1-1){.pf-ref} applies, or $a_n<1$ eventually, in which case step [](#s1-3){.pf-ref} applies. These cases exhaust all possibilities.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} answers the question affirmatively.

:::

:::

:::
