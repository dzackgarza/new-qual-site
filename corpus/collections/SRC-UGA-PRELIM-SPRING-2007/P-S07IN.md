---
schema: qual/card@1
id: P-S07IN
kind: problem
title: Alternating sum of squares $1^2-2^2+\cdots+(-1)^{n-1}n^2$
classification:
  areas:
  - prelim
  topics:
  - Induction
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
---

::: problem
Using mathematical induction, show that for each positive integer $n$, $$1^2 - 2^2 + 3^2 - \dots + (-1)^{n-1}n^2 = (-1)^{n-1}n(n+1)/2.$$ (Hint: in the induction step, consider separately the cases where $n$ is even or odd.)
:::


::: solution
<1>1. Let
\[
S_n=1^2-2^2+3^2-\cdots+(-1)^{n-1}n^2.
\]
We prove by induction that
\[
S_n=(-1)^{n-1}\frac{n(n+1)}2
\]
for every $n\ge1$.
:::

<1>2. The formula holds for $n=1$.
::: {.proof}
We have
\[
S_1=1=(-1)^0\frac{1\cdot2}{2}.
\]
:::

<1>3. Assume the formula holds for some $n\ge1$.
Then it also holds for $n+1$.
::: {.proof}
By the induction hypothesis,
\[
\begin{aligned}
S_{n+1}
&=S_n+(-1)^n(n+1)^2\\
&=(-1)^{n-1}\frac{n(n+1)}2+(-1)^n(n+1)^2\\
&=(-1)^n(n+1)\left(-\frac n2+n+1\right)\\
&=(-1)^n\frac{(n+1)(n+2)}2.
\end{aligned}
\]
This is exactly the required formula with $n$ replaced by $n+1$.
:::

<1>4. Therefore
\[
1^2-2^2+\cdots+(-1)^{n-1}n^2
=(-1)^{n-1}\frac{n(n+1)}2
\]
for every positive integer $n$.
::: {.proof}
This follows from <1>2 and <1>3 by mathematical induction.
:::
