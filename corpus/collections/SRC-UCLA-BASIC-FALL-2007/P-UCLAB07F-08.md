---
schema: qual/card@1
id: P-UCLAB07F-08
kind: problem
title: Divergence after the transform a_n over 1 plus a_n
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
Does it follow that \[\sum_{n=1}^{\infty}\frac{a_n}{1+a_n}=\infty?\] Prove your answer.
:::

::: {.solution}
<1>1. If
\[
a_n\ge1
\]
for infinitely many $n$, then
\[
\sum_{n=1}^{\infty}\frac{a_n}{1+a_n}=\infty.
\]

::: {.proof}
Whenever $a_n\ge1$,
\[
\frac{a_n}{1+a_n}
\ge
\frac12.
\]
Thus the transformed series has infinitely many terms at least $1/2$, so its partial sums are unbounded.
:::

<1>2. If
\[
a_n<1
\]
for all sufficiently large $n$, then
\[
\frac{a_n}{1+a_n}\ge\frac{a_n}{2}
\]
for all sufficiently large $n$.

::: {.proof}
If $0\le a_n<1$, then
\[
1+a_n\le2.
\]
Since $a_n\ge0$,
\[
\frac{a_n}{1+a_n}\ge\frac{a_n}{2}.
\]
:::

<1>3. In the case of step <1>2,
\[
\sum_{n=1}^{\infty}\frac{a_n}{1+a_n}=\infty.
\]

::: {.proof}
Choose $N$ such that $a_n<1$ for all $n\ge N$. By hypothesis,
\[
\sum_{n=N}^{\infty}a_n=\infty,
\]
because removing finitely many terms does not change divergence. By step <1>2,
\[
\sum_{n=N}^{M}\frac{a_n}{1+a_n}
\ge
\frac12\sum_{n=N}^{M}a_n.
\]
The right side tends to $+\infty$ as $M\to\infty$, so the transformed series diverges.
:::

<1>4. Therefore
\[
\boxed{
\sum_{n=1}^{\infty}\frac{a_n}{1+a_n}=\infty
}.
\]

::: {.proof}
Either $a_n\ge1$ for infinitely many $n$, in which case step <1>1 applies, or $a_n<1$ eventually, in which case step <1>3 applies. These cases exhaust all possibilities.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 answers the question affirmatively.
:::
:::
