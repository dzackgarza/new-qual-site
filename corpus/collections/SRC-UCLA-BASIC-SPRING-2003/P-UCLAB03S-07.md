---
schema: qual/card@1
id: P-UCLAB03S-07
kind: problem
title: The annihilator of a sum of two subspaces
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 7 of the official UCLA Basic Examination, May 2003 PDF. The source writes functionals $f:V\to F$ although $V$ is specified to be real and no field $F$ is defined; the intended real dual is used here.
---

::: {.problem}
Let $V$ be a finite-dimensional real vector space.
For a subspace $W\subset V$, define its annihilator by
\[
W^0=\{f:V\to\RR\text{ linear}: f|_W=0\}.
\]
If $W_1,W_2\subset V$ are subspaces, prove that
\[
W_1^0\cap W_2^0=(W_1+W_2)^0.
\]
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

One has
\[
W_1^0\cap W_2^0\subseteq (W_1+W_2)^0.
\]


::: pf-proof

Let \(f\in W_1^0\cap W_2^0\). Then
\[
f(w_1)=0
\qquad\text{and}\qquad
f(w_2)=0
\]
for every \(w_1\in W_1\) and \(w_2\in W_2\). Every vector in \(W_1+W_2\) has the form \(w_1+w_2\), and linearity gives
\[
f(w_1+w_2)
=
f(w_1)+f(w_2)
=0.
\]
Thus \(f\) vanishes on \(W_1+W_2\), so
\[
f\in(W_1+W_2)^0.
\]

:::

:::

::: {.pf-step #s1-2}

One has
\[
(W_1+W_2)^0\subseteq W_1^0\cap W_2^0.
\]


::: pf-proof

Let \(f\in(W_1+W_2)^0\). Since
\[
W_1\subseteq W_1+W_2
\qquad\text{and}\qquad
W_2\subseteq W_1+W_2,
\]
the functional \(f\) vanishes on both \(W_1\) and \(W_2\). Hence
\[
f\in W_1^0
\qquad\text{and}\qquad
f\in W_2^0,
\]
so \(f\in W_1^0\cap W_2^0\).

:::

:::

::: {.pf-step #s1-3}

Therefore
\[
\boxed{W_1^0\cap W_2^0=(W_1+W_2)^0.}
\]


::: pf-proof

Steps [](#s1-1){.pf-ref} and [](#s1-2){.pf-ref} prove the two inclusions.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} is the required equality.

:::

:::

:::
