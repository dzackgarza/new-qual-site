---
schema: qual/card@1
id: P-TRIV-RA05
kind: problem
title: Estimating $\sin^{100} 0.1$ to within $10\%$
classification:
  areas: [real-analysis]
  topics:
  - Estimates
  - Exponential Function
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Real Analysis, Problem 5, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Restored the exponent in sin^100 0.1, lost as sin100.1, against Real Analysis Problem 5 on page 8 of the source PDF.
---

::: {.problem}
Find $\sin^{100} 0.1$ with $10\%$ accuracy.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The alternating Taylor series for sine gives
$$
0.1-\frac{0.1^3}{6}
<
\sin0.1
<
0.1-\frac{0.1^3}{6}+\frac{0.1^5}{120}.
$$


::: pf-proof

For $0<x<1$, the sine series
$$
\sin x
=
x-\frac{x^3}{3!}+\frac{x^5}{5!}-\cdots
$$
is alternating with decreasing term magnitudes. Truncating after a negative
term gives a lower bound and after the following positive term gives an upper
bound.

:::

:::

::: {.pf-step #s1-2}

Dividing by $0.1$ gives
$$
1-\frac1{600}
<
\frac{\sin0.1}{0.1}
<
1-\frac1{600}+\frac1{1,200,000}.
$$


::: pf-proof

Since
$$
\frac{0.1^2}{6}=\frac1{600}
$$
and
$$
\frac{0.1^4}{120}=\frac1{1,200,000},
$$
the bounds follow from step [](#s1-1){.pf-ref}.

:::

:::

::: {.pf-step #s1-3}

Let
$$
r=\frac{\sin0.1}{0.1}.
$$
Then
$$
e^{-0.167}
<
r^{100}
<
e^{-0.166}.
$$


::: pf-proof

For $0<u<1$,
$$
-\frac{u}{1-u}
\leq
\log(1-u)
\leq
-u.
$$

For the lower bound in step [](#s1-2){.pf-ref}, take $u=1/600$. Then
$$
100\log r
>
-\frac{100/600}{1-1/600}
=
-\frac{100}{599}
>
-0.167.
$$

For the upper bound, step [](#s1-2){.pf-ref} gives
$$
r
<
1-\frac{1999}{1,200,000}.
$$
Hence
$$
100\log r
<
-100\frac{1999}{1,200,000}
<
-0.166.
$$
Exponentiating gives the result.

:::

:::

::: {.pf-step #s1-4}

Numerically,
$$
0.8462
<
r^{100}
<
0.8471.
$$


::: pf-proof

The endpoint exponentials in step [](#s1-3){.pf-ref} satisfy
$$
e^{-0.167}>0.8462
$$
and
$$
e^{-0.166}<0.8471.
$$

:::

:::

::: {.pf-step #s1-5}

Therefore
$$
\sin^{100}0.1
=
10^{-100}r^{100},
$$
so
$$
8.462\times10^{-101}
<
\sin^{100}0.1
<
8.471\times10^{-101}.
$$


::: pf-proof

Since
$$
\sin0.1=0.1r,
$$
raising to the hundredth power gives
$$
\sin^{100}0.1
=
(0.1)^{100}r^{100}
=
10^{-100}r^{100}.
$$
Apply step [](#s1-4){.pf-ref}.

:::

:::

::: {.pf-step #s1-6}

Thus a convenient answer with much better than $10\%$ accuracy is
$$
\boxed{\sin^{100}0.1\approx8.47\times10^{-101}}.
$$


::: pf-proof

The interval in step [](#s1-5){.pf-ref} has relative width far below $10\%$, and the stated
approximation lies inside that interval.

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} gives the requested approximation.

:::

:::

:::
