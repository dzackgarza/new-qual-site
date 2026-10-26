---
schema: qual/card@1
id: P-PRECALC2-14
kind: problem
title: Convergence of $\sum\frac{n!}{2^{n^2}}$ and $\sum\frac{n^{\sqrt n}}{2^n}$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
Do the series $\sum _ { n = 1 } ^ { \infty } { \frac { n ! } { 2 ^ { n ^ { 2 } } } }$ and $\sum _ { n = 1 } ^ { \infty } { \frac { n ^ { \sqrt { n } } } { 2 ^ { n } } }$ converge or diverge?
:::

Consider first
\[
\sum_{n=1}^{\infty}
\frac{n!}{2^{n^2}}.
\]
Set
\[
a_n=\frac{n!}{2^{n^2}}.
\]

::: pf

::: pf-step

The ratio of successive terms is
\[
\boxed{
\frac{a_{n+1}}{a_n}
=
\frac{n+1}{2^{2n+1}}}.
\]


::: pf-proof

\[
\begin{aligned}
\frac{a_{n+1}}{a_n}
&=
\frac{(n+1)!}{2^{(n+1)^2}}
\frac{2^{n^2}}{n!}\\
&=
(n+1)
2^{n^2-(n+1)^2}\\
&=
\frac{n+1}{2^{2n+1}}.
\end{aligned}
\]

:::

:::

::: pf-step

One has
\[
\boxed{
\lim_{n\to\infty}
\frac{n+1}{2^{2n+1}}
=
0}.
\]


::: pf-proof

The denominator grows exponentially while the numerator grows linearly.
More explicitly,
\[
\frac{n+1}{2^{2n+1}}
=
\frac{n+1}{2\cdot4^n},
\]
and
\[
\frac{n+1}{4^n}\to0.
\]

:::

:::

::: pf-step

Therefore
\[
\boxed{
\sum_{n=1}^{\infty}
\frac{n!}{2^{n^2}}
\text{ converges}}.
\]


::: pf-proof

By steps <1>1--<1>2, the ratio-test limit is
\[
0<1.
\]
Hence the series converges absolutely.

:::

:::

::: pf-step

The \(n\)th root is
\[
\boxed{
b_n^{1/n}
=
\frac{n^{1/\sqrt n}}2}.
\]


::: pf-proof

\[
\left(n^{\sqrt n}\right)^{1/n}
=
n^{\sqrt n/n}
=
n^{1/\sqrt n},
\]
and
\[
(2^n)^{1/n}=2.
\]

:::

:::

::: pf-step

One has
\[
\boxed{
n^{1/\sqrt n}
=
\exp\left(\frac{\log n}{\sqrt n}\right)}.
\]


::: pf-proof

Use
\[
x^a=e^{a\log x}.
\]

:::

:::

::: pf-step

The exponent satisfies
\[
\boxed{
\frac{\log n}{\sqrt n}
\longrightarrow0}.
\]


::: pf-proof

For example, by l'Hôpital's rule on the continuous variable,
\[
\lim_{x\to\infty}
\frac{\log x}{\sqrt x}
=
\lim_{x\to\infty}
\frac{1/x}{1/(2\sqrt x)}
=
\lim_{x\to\infty}
\frac2{\sqrt x}
=
0.
\]
Hence the same holds along integers.

:::

:::

::: pf-step

Therefore
\[
\boxed{
n^{1/\sqrt n}\to1}.
\]


::: pf-proof

Apply the exponential function to step <1>6 and use continuity:
\[
\exp\left(\frac{\log n}{\sqrt n}\right)
\to
e^0
=
1.
\]

:::

:::

::: pf-step

Hence
\[
\boxed{
\lim_{n\to\infty}b_n^{1/n}
=
\frac12}.
\]


::: pf-proof

Combine steps <1>4 and <1>7.

:::

:::

::: pf-step

Therefore
\[
\boxed{
\sum_{n=1}^{\infty}
\frac{n^{\sqrt n}}{2^n}
\text{ converges}}.
\]


::: pf-proof

By step <1>8, the root-test limit is
\[
\frac12<1.
\]
Hence the series converges absolutely.

:::

:::

::: pf-qed

Steps <1>3 and <1>9 show that both requested series converge.

:::

:::
