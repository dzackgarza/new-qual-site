---
schema: qual/card@1
id: P-TPZF3
kind: problem
title: Numbers in $[0,1]$ with no decimal digit $4$ form a compact nowhere dense set
  with no isolated points and Lebesgue measure zero
classification:
  areas:
  - real-analysis
  topics:
  - Cantor Set
  - Measure Theory
  - Compactness
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Problem 1 of the official UGA Real Analysis Qualifying Exam — January 2017 DOCX.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---


::: problem
Let $K$ be the set of numbers in $[0,1]$ whose decimal expansions do not use the digit $4$.

Use the convention that when a decimal number ends with $4$ but all other digits are different from $4$, replace that terminating expansion by the equivalent expansion ending in $3999\ldots$; for example,
\[
0.8754=0.8753999\ldots.
\]

Show that $K$ is compact, nowhere dense, has no isolated points, and determine $m(K)$.
:::

::: solution
<1>1. Construct finite-stage closed sets.
::: proof
For $n\ge1$, let $K_n$ be the set of numbers in $[0,1]$ whose first $n$ digits, using the stated convention at terminating endpoints, avoid the digit $4$.

Equivalently, at stage $n$ one deletes, for every admissible word $d_1\cdots d_{n-1}$ with each $d_j\ne4$, the open interval of numbers whose first $n-1$ digits are $d_1,\ldots,d_{n-1}$ and whose $n$th digit is $4$. Thus $K_n$ is a union of $9^n$ closed decimal cylinders, each of length $10^{-n}$. In particular, $K_n$ is compact and
\[
K_{n+1}\subseteq K_n.
\]
A number avoids the digit $4$ in every decimal place exactly when it lies in every $K_n$, so
\[
K=\bigcap_{n=1}^\infty K_n.
\]
Therefore $K$ is closed in the compact interval $[0,1]$, hence compact.
:::

<1>2. Compute the Lebesgue measure.
::: proof
Since the $9^n$ stage-$n$ cylinders have disjoint interiors and length $10^{-n}$,
\[
m(K_n)=9^n10^{-n}=\left(\frac9{10}\right)^n.
\]
The sets $K_n$ decrease and $m(K_1)<\infty$. Continuity of Lebesgue measure from above therefore gives
\[
m(K)
=\lim_{n\to\infty}m(K_n)
=\lim_{n\to\infty}\left(\frac9{10}\right)^n
=0.
\]
Hence
\[
\boxed{m(K)=0.}
\]
:::

<1>3. Prove that $K$ is nowhere dense.
::: proof
By Step 1, $K$ is closed. By Step 2, it has measure zero. A nonempty open interval has positive Lebesgue measure, so $K$ cannot contain any nonempty open interval. Thus
\[
\operatorname{int}(K)=\varnothing.
\]
Since $K$ is closed,
\[
\operatorname{int}(\overline K)=\operatorname{int}(K)=\varnothing,
\]
which is exactly that $K$ is nowhere dense.
:::

<1>4. Prove that $K$ has no isolated points.
::: proof
Fix $x\in K$ and $\varepsilon>0$. Choose $n$ so large that
\[
10^{-n}<\varepsilon.
\]
Because $x\in K_n$, it lies in one of the closed stage-$n$ cylinders $I_n=[a_n,b_n]$ of length $10^{-n}$. Both endpoints belong to $K$: the left endpoint has a terminating decimal expansion using only the admissible prefix followed by zeros, while the right endpoint either has such an admissible terminating expansion or, if its terminating expansion ends in the digit $4$, the convention replaces that final $4$ by $3999\ldots$, which contains no digit $4$.

Since $a_n\ne b_n$, at least one endpoint, call it $y_n$, is different from $x$. Moreover,
\[
|x-y_n|\le b_n-a_n=10^{-n}<\varepsilon.
\]
Thus every neighborhood of every $x\in K$ contains a point of $K$ distinct from $x$. Hence $K$ has no isolated points.
:::
:::
