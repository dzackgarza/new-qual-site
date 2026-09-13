---
schema: qual/card@1
id: P-BERK80S-18
kind: problem
title: Zeros of a polynomial in an annulus
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 18 of the vendored Berkeley Preliminary Exam, Summer 1980.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Verified both strict Rouché estimates and subtracted the resulting disk counts to obtain the annular zero count.
---

::: {.problem}
How many zeros does the complex polynomial

$$
3 z ^ { 9 } + 8 z ^ { 6 } + z ^ { 5 } + 2 z ^ { 3 } + 1
$$

have in the annulus $1 < | z | < 2 \ ?$
:::


::: {.solution}
Let
\[
p(z)=3z^9+8z^6+z^5+2z^3+1.
\]
The polynomial has
\[
\boxed{3}
\]
zeros in the annulus $1<|z|<2$, counted with multiplicity.

<1>1. $p$ has six zeros in $|z|<1$.
::: {.proof}
On $|z|=1$,
\[
|8z^6|=8,
\]
while
\[
|3z^9+z^5+2z^3+1|
\le3+1+2+1=7<8.
\]
By Rouché's theorem, $p(z)$ and $8z^6$ have the same number of zeros in $|z|<1$. Therefore $p$ has exactly six zeros there, counted with multiplicity.
The inequality is strict, so $p$ has no zero on $|z|=1$.
:::

<1>2. $p$ has nine zeros in $|z|<2$.
::: {.proof}
On $|z|=2$,
\[
|3z^9|=3\cdot2^9=1536.
\]
For the remaining terms,
\[
\begin{aligned}
|8z^6+z^5+2z^3+1|
&\le 8\cdot2^6+2^5+2\cdot2^3+1\\
&=512+32+16+1\\
&=561<1536.
\end{aligned}
\]
Thus Rouché's theorem gives the same number of zeros as $3z^9$, namely nine, inside $|z|<2$. Again the strict inequality shows there are no zeros on $|z|=2$.
:::

<1>3. Subtract the two disk counts.
::: {.proof}
Every zero in $|z|<2$ lies either in $|z|<1$ or in the annulus $1<|z|<2$, because there are no zeros on $|z|=1$. Hence the annulus contains
\[
9-6=3
\]
zeros, counted with multiplicity.
:::
:::
