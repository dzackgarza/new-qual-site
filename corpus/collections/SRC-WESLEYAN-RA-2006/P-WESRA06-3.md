---
schema: qual/card@1
id: P-WESRA06-3
kind: problem
title: Limsup sets, Borel--Cantelli, counting functions, and decimal digits
classification:
  areas: [real-analysis]
  topics: [Measure Theory]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Real Analysis Problem 3 in the deterministic MinerU Flash extraction assets/attachments/analysis_2003-2007_extracted.md. Flash reproduces the printed hypothesis sum_n mu(A_n)=55.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
Let $\Omega$ be a nonempty set, let $\mathcal A$ be a sigma-algebra on $\Omega$, and let $A_1,A_2,\ldots\in\mathcal A$.
Let
\[
\overline A=\{\omega\in\Omega:\omega\text{ belongs to infinitely many }A_n\}.
\]

1. Prove that $\overline A\in\mathcal A$.

2. If $\mu$ is a finite measure and
   \[
   \sum_{n=1}^\infty\mu(A_n)=55,
   \]
   determine $\mu(\overline A)$.

3. Let $f(\omega)$ be the number of sets $A_n$ containing $\omega$, with $f(\omega)=\infty$ when $\omega\in\overline A$.
   Prove that $f$ is measurable and, under the hypothesis in part 2, integrable.

4. For normalized Lebesgue measure on $[0,1]$, compute the measure of the set of numbers whose first even digit in their decimal expansion is either $4$ or $8$.
:::

::: {.solution}
<1>1. Express the infinitely-often set by countable unions and intersections.
::: {.proof}
A point belongs to infinitely many $A_n$ exactly when, for every $N$, it belongs to at least one $A_n$ with $n\ge N$.
Hence
\[
\overline A
=\bigcap_{N=1}^\infty\bigcup_{n=N}^\infty A_n.
\]
Since $\mathcal A$ is closed under countable unions and intersections,
\[
\boxed{\overline A\in\mathcal A.}
\]
:::

<1>2. Apply the first Borel--Cantelli lemma.
::: {.proof}
The hypothesis
\[
\sum_{n=1}^\infty\mu(A_n)=55<\infty
\]
implies, by the first Borel--Cantelli lemma,
\[
\mu(\limsup A_n)=0.
\]
Since $\overline A=\limsup A_n$,
\[
\boxed{\mu(\overline A)=0.}
\]
:::

<1>3. Identify the counting function as a monotone sum.
::: {.proof}
For each $N$, define
\[
f_N=\sum_{n=1}^N\mathbf1_{A_n}.
\]
Each $f_N$ is measurable and
\[
f_N(\omega)\uparrow f(\omega)
\]
for every $\omega$.
Therefore $f$ is measurable as the pointwise limit of measurable functions.

By the Monotone Convergence Theorem,
\[
\int_\Omega f\,d\mu
=\lim_{N\to\infty}\int_\Omega f_N\,d\mu
=\lim_{N\to\infty}\sum_{n=1}^N\mu(A_n)
=55.
\]
Hence
\[
\boxed{f\in L^1(\mu),\qquad \int f\,d\mu=55.}
\]
:::

<1>4. Compute the decimal-digit event.
::: {.proof}
Ignore the countable set of numbers having two decimal expansions; it has Lebesgue measure zero.
For the remaining numbers, the decimal digits are independent and each digit $0,1,\ldots,9$ has probability $1/10$ under normalized Lebesgue measure.

The first even digit is $4$ or $8$ exactly when there are some number $k-1\ge0$ of initial odd digits, followed by either $4$ or $8$.
The probability of an odd digit is
\[
\frac5{10}=\frac12,
\]
and the probability that the next digit is $4$ or $8$ is
\[
\frac2{10}=\frac15.
\]
Therefore the desired measure is
\[
\sum_{k=1}^\infty\left(\frac12\right)^{k-1}\frac15
=\frac15\frac1{1-1/2}
=\boxed{\frac25}.
\]
The exceptional event that every digit is odd has measure
\[
\lim_{N\to\infty}\left(\frac12\right)^N=0,
\]
so no further case contributes.
:::
:::
