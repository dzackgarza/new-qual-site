---
schema: qual/card@1
id: P-UCLAB08S-04
kind: problem
title: Dini theorem for decreasing nonnegative functions
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
  note: Checked against Problem 4 of the retained UCLA Basic Examination, Spring 2008.
---

::: {.problem}
Let $X\subset\mathbb R^N$ be compact, and let $(f_n)$ be continuous real-valued functions on $X$ satisfying
\[
0\le f_{n+1}(x)\le f_n(x)
\]
for all $x\in X$, with $f_n(x)\to0$ pointwise.
Prove Dini's theorem in this setting: $f_n\to0$ uniformly on $X$.
:::

Fix
\[
\varepsilon>0.
\]

::: pf

::: pf-step

For each $n$, define
\[
U_n
=
\{x\in X:f_n(x)<\varepsilon\}.
\]
Then $U_n$ is open in $X$.


::: pf-proof

The function
\[
f_n:X\to\mathbb R
\]
is continuous.
Therefore
\[
U_n
=
f_n^{-1}((-\infty,\varepsilon))
\]
is open in the subspace topology on $X$.

:::

:::

::: pf-step

The sets $U_n$ are increasing:
\[
U_n\subseteq U_{n+1}.
\]


::: pf-proof

If
\[
x\in U_n,
\]
then
\[
f_n(x)<\varepsilon.
\]
The monotonicity assumption gives
\[
0\le f_{n+1}(x)\le f_n(x)<\varepsilon.
\]
Hence
\[
x\in U_{n+1}.
\]

:::

:::

::: pf-step

The family
\[
\{U_n:n\ge1\}
\]
covers $X$.


::: pf-proof

Fix
\[
x\in X.
\]
Since
\[
f_n(x)\to0,
\]
there exists $N$ such that
\[
f_N(x)<\varepsilon.
\]
Thus
\[
x\in U_N.
\]
Since $x$ was arbitrary,
\[
X=\bigcup_{n=1}^\infty U_n.
\]

:::

:::

::: pf-step

There exists $N$ such that
\[
U_N=X.
\]


::: pf-proof

The sets $U_n$ form an open cover of the compact space $X$ by step <1>3.
Hence there is a finite subcover
\[
U_{n_1},\ldots,U_{n_r}.
\]
Let
\[
N=\max\{n_1,\ldots,n_r\}.
\]
By step <1>2,
\[
U_{n_j}\subseteq U_N
\]
for every $j$.
Therefore
\[
X
=
\bigcup_{j=1}^rU_{n_j}
\subseteq
U_N
\subseteq
X.
\]
Thus
\[
U_N=X.
\]

:::

:::

::: pf-step

For every $n\ge N$ and every $x\in X$,
\[
0\le f_n(x)<\varepsilon.
\]


::: pf-proof

Since
\[
U_N=X,
\]
one has
\[
f_N(x)<\varepsilon
\]
for every $x\in X$.
If
\[
n\ge N,
\]
then
\[
0\le f_n(x)\le f_N(x)<\varepsilon.
\]

:::

:::

::: pf-step

Therefore
\[
\boxed{f_n\to0\text{ uniformly on }X}.
\]


::: pf-proof

Step <1>5 shows that for every $\varepsilon>0$ there is $N$ such that
\[
|f_n(x)|<\varepsilon
\]
for every $n\ge N$ and every $x\in X$.
This is exactly uniform convergence to $0$.

:::

:::

::: pf-qed

Step <1>6 proves Dini's theorem in the stated setting.

:::

:::
