---
schema: qual/card@1
id: P-AZOFF-E04
kind: problem
title: Which values $f(1/n)$ an analytic function on the disk can take
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Liouville, FTA, and power series, Problem 4, in the deterministic MinerU Flash extraction assets/attachments/Azoff Problems by Topic_extracted.md.
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Ruled out (a) by continuity at the accumulation point zero, (b) by the
    identity theorem applied to the odd subsequence, and (c) by the derivative
    quotient at zero. For (d), the rational function (1-2z)/(1-z) is analytic
    on the unit disk and has the prescribed values.
---

::: {.problem}
Suppose $f$ is analytic on the open unit disk.
Determine, with proof, which of the following are possible.

a) $\textstyle f ( { \frac { 1 } { n } } ) = ( - 1 ) ^ { n }$ for each integer $n > 1$

b) $\begin{array} { r } { f ( \frac { 1 } { n } ) = \exp ( - n ) } \end{array}$ for each even integer $n > 1$ while $\begin{array} { r } { f ( \frac { 1 } { n } ) = 0 } \end{array}$ for each odd integer $n > 1$

c) $\begin{array} { r } { f ( \frac { 1 } { n ^ { 2 } } ) = \frac { 1 } { n } } \end{array}$ for each integer $n > 1$

d) $\begin{array} { r } { f ( \frac { 1 } { n } ) = \frac { n - 2 } { n - 1 } } \end{array}$ for each integer $n > 1$
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Part (a) is impossible.

::: pf-proof

The points $1/n$ converge to $0$, which lies in the open unit disk. Since an
analytic function is continuous,
$$
f(1/n)\longrightarrow f(0).
$$
But the prescribed values
$$
f(1/n)=(-1)^n
$$
do not converge. Hence no analytic function on the disk can satisfy (a).

:::

:::

::: {.pf-step #s2}

Part (b) is impossible.

::: pf-proof

For every odd integer $n>1$, the prescription gives
$$
f(1/n)=0.
$$
These are distinct zeros accumulating at $0$, an interior point of the unit
disk. By the identity theorem,
$$
f\equiv0
$$
on the disk. This contradicts the values prescribed for even $n$, since
$$
f(1/n)=e^{-n}\neq0.
$$

:::

:::

::: {.pf-step #s3}

Part (c) is impossible.

::: pf-proof

Since
$$
\frac1{n^2}\longrightarrow0
$$
and
$$
f(1/n^2)=\frac1n\longrightarrow0,
$$
continuity gives $f(0)=0$. Analyticity at $0$ would then require
$$
f'(0)
=
\lim_{z\to0}\frac{f(z)}z.
$$
Along the sequence $z=1/n^2$, however,
$$
\frac{f(1/n^2)}{1/n^2}
=
n\longrightarrow\infty.
$$
Thus the derivative at $0$ cannot exist, a contradiction.

:::

:::

::: {.pf-step #s4}

Part (d) is possible; one such function is
$$
\boxed{
f(z)=\frac{1-2z}{1-z}.
}
$$

::: pf-proof

For $\abs{z}<1$, the denominator $1-z$ is nonzero, so this rational function
is analytic on the open unit disk. For every integer $n>1$,
$$
\begin{aligned}
f(1/n)
&=
\frac{1-2/n}{1-1/n}\\
&=
\frac{n-2}{n-1}.
\end{aligned}
$$
Hence it realizes exactly the values in (d).

:::

:::

::: {.pf-step #s5}

Exactly part (d) is possible.

::: pf-proof

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref} and [](#s3){.pf-ref} rule out (a)--(c), while step [](#s4){.pf-ref} constructs an analytic
function satisfying (d).

:::

:::

::: pf-qed

Step [](#s5){.pf-ref} is the requested classification.

:::

:::

:::
