---
schema: qual/card@1
id: P-UCLAB18S-01
kind: problem
title: Linear independence of exponential functions
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored UCLA Basic Examination, Spring 2018, `assets/attachments/basic-18S.pdf`.
---

::: {.problem}
Prove that the functions
\[
e^t,e^{2t},\ldots,e^{nt}
\]
are linearly independent in the space of continuous functions on $[1,2]$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Suppose
\[
c_1e^t+c_2e^{2t}+\cdots+c_ne^{nt}=0
\]
for every
\[
t\in[1,2],
\]
where
\[
c_1,\ldots,c_n\in\RR.
\]


::: pf-proof

To prove linear independence, it suffices to show that every linear relation of this form has all coefficients equal to zero.

:::

:::

::: {.pf-step #s1-2}

Define the polynomial
\[
p(s)
=
c_1s+c_2s^2+\cdots+c_ns^n.
\]
Then
\[
p(e^t)=0
\]
for every
\[
t\in[1,2].
\]


::: pf-proof

Since
\[
e^{kt}=(e^t)^k,
\]
the relation in step [](#s1-1){.pf-ref} is exactly
\[
p(e^t)=0.
\]

:::

:::

::: {.pf-step #s1-3}

The polynomial $p$ vanishes at every point of the interval
\[
[e,e^2].
\]


::: pf-proof

The exponential map is continuous and strictly increasing, and maps
\[
[1,2]
\]
onto
\[
[e,e^2].
\]
Thus for every
\[
s\in[e,e^2],
\]
there exists
\[
t\in[1,2]
\]
with
\[
s=e^t.
\]
Step [](#s1-2){.pf-ref} then gives
\[
p(s)=0.
\]

:::

:::

::: pf-step

Therefore
\[
p
\]
is the zero polynomial.


::: pf-proof

A nonzero real polynomial of degree at most $n$ has at most $n$ real roots.
Step [](#s1-3){.pf-ref} gives infinitely many roots, indeed an entire interval.
Hence $p$ must be identically zero.

:::

:::

::: {.pf-step #s1-5}

Thus
\[
\boxed{
c_1=c_2=\cdots=c_n=0.
}
\]


::: pf-proof

The coefficients of the zero polynomial all vanish.

:::

:::

::: {.pf-step #s1-6}

Hence
\[
\boxed{
e^t,e^{2t},\ldots,e^{nt}
\text{ are linearly independent in }C([1,2]).
}
\]


::: pf-proof

Step [](#s1-5){.pf-ref} shows that the only linear relation among the functions is the trivial one.

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} is the required conclusion.

:::

:::

:::
