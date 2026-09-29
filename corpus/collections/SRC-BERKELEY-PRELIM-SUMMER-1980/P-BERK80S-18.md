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
3z^9+8z^6+z^5+2z^3+1
$$

have in the annulus $1<\abs{z}<2$?
:::

::: {.solution}
Let
$$
p(z)=3z^9+8z^6+z^5+2z^3+1.
$$
All zero counts below are with multiplicity.

::: pf

::: {.pf-step #s1}

$p$ has six zeros in $\abs{z}<1$ and no zero on $\abs{z}=1$.

::: pf-proof

On $\abs{z}=1$,
$$
\abs{8z^6}=8,
$$
while
$$
\abs{3z^9+z^5+2z^3+1}
\le3+1+2+1=7<8.
$$
By Rouché's theorem, $p$ and $8z^6$ have the same number of zeros in
$\abs{z}<1$, namely six. The strict inequality also gives
$\abs{p(z)}\ge8-7>0$ on $\abs{z}=1$.

:::

:::

::: {.pf-step #s2}

$p$ has nine zeros in $\abs{z}<2$.

::: pf-proof

On $\abs{z}=2$,
$$
\abs{3z^9}=3\cdot2^9=1536,
$$
while
$$
\begin{aligned}
\abs{8z^6+z^5+2z^3+1}
&\le 8\cdot2^6+2^5+2\cdot2^3+1\\
&=512+32+16+1\\
&=561<1536.
\end{aligned}
$$
By Rouché's theorem, $p$ and $3z^9$ have the same number of zeros in
$\abs{z}<2$, namely nine.

:::

:::

::: {.pf-step #s3}

$p$ has
$$
\boxed{3}
$$
zeros in the annulus $1<\abs{z}<2$.

::: pf-proof

By step [](#s1){.pf-ref}, every zero in $\abs{z}<2$ lies either in $\abs{z}<1$ or in
the annulus $1<\abs{z}<2$. Steps [](#s1){.pf-ref} and [](#s2){.pf-ref} give $9-6=3$ zeros in the
annulus.

:::

:::

::: pf-qed

Step [](#s3){.pf-ref} gives the requested number.

:::

:::

:::
