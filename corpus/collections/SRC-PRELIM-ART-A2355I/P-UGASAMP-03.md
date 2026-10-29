---
schema: qual/card@1
id: P-UGASAMP-03
kind: problem
title: Convergence of $\frac{n^2+2}{n^2+3n}$ to $1$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
---

::: {.problem}
Give the definition for convergence of a sequence of real numbers $(a_n)_{n=1}^\infty$ to a real number $a$. Prove that
\[
a_n=\frac{n^2+2}{n^2+3n}
\]
converges to $1$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

A sequence \((a_n)_{n=1}^\infty\) of real numbers converges to \(a\in\RR\) if for every \(\varepsilon>0\) there is \(N\in\NN\) such that
\[
n\ge N
\quad\Longrightarrow\quad
|a_n-a|<\varepsilon.
\]


::: pf-proof

This is the \(\varepsilon\)--\(N\) definition of convergence of a real sequence.

:::

:::

::: {.pf-step #s1-2}

For every \(n\ge1\),
\[
\left|\frac{n^2+2}{n^2+3n}-1\right|
=
\frac{3n-2}{n^2+3n}
<
\frac{3}{n}.
\]


::: pf-proof

Direct subtraction gives
\[
\frac{n^2+2}{n^2+3n}-1
=
\frac{2-3n}{n^2+3n}.
\]
For \(n\ge1\), one has \(3n-2>0\), so
\[
\left|\frac{2-3n}{n^2+3n}\right|
=
\frac{3n-2}{n^2+3n}.
\]
Since \(3n-2<3n\) and \(n^2+3n>n^2\),
\[
\frac{3n-2}{n^2+3n}
<
\frac{3n}{n^2}
=
\frac3n.
\]

:::

:::

::: {.pf-step #s1-3}

Given \(\varepsilon>0\), choose an integer
\[
N>\frac3\varepsilon.
\]
Then \(n\ge N\) implies
\[
\left|a_n-1\right|<\varepsilon.
\]


::: pf-proof

If \(n\ge N\), then
\[
\frac3n\le\frac3N<\varepsilon.
\]
Combining this with step [](#s1-2){.pf-ref} gives
\[
|a_n-1|<\frac3n\le\frac3N<\varepsilon.
\]

:::

:::

::: {.pf-step #s1-4}

Therefore
\[
\boxed{\displaystyle \lim_{n\to\infty}\frac{n^2+2}{n^2+3n}=1.}
\]


::: pf-proof

Step [](#s1-3){.pf-ref} verifies the definition in step [](#s1-1){.pf-ref} with \(a=1\).

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} gives the requested definition, and step [](#s1-4){.pf-ref} proves the requested convergence.

:::

:::

:::
