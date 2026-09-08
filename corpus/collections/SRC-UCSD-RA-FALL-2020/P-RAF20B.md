---
schema: qual/card@1
id: P-RAF20B
kind: problem
title: "A bijective bounded operator with unbounded inverse on an incomplete space"
classification:
  areas:
  - real-analysis
  topics:
  - Bounded Operators
  - Normed Spaces
  - Bounded Inverse Theorem
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 2 of the official UCSD Fall 2020 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
Let $X$ denote the set of all sequences $a = (a_1, a_2, \ldots)$ with all $a_k$ ($k \geq 1$) real numbers but only finitely many of them nonzero.
$X$ is a real vector space with the usual component-wise addition and scalar multiplication.
It is a normed vector space with the norm $\|a\| = \sup_{k \geq 1} |a_k|$.
Define $T : X \to X$ by
$$
Ta = \left(a_1, \frac{a_2}{2}, \ldots, \frac{a_k}{k}, \ldots\right) \quad \text{if } a = (a_1, a_2, \ldots, a_k, \ldots) \in X.
$$

Prove that $T : X \to X$ is a bijective, linear, and bounded operator, but its inverse $T^{-1} : X \to X$ is unbounded.
:::

::: solution
<1>1. Prove linearity and boundedness.
::: proof
The map $T$ acts coordinatewise by multiplication by the scalars $1/k$, so it is linear. Moreover, for $a=(a_k)\in X$,
\[
\|Ta\|
=\sup_{k\ge1}\frac{|a_k|}{k}
\le \sup_{k\ge1}|a_k|
=\|a\|.
\]
Hence $T$ is bounded and
\[
\|T\|\le1.
\]
Since $Te_1=e_1$, in fact $\|T\|=1$.
:::

<1>2. Prove bijectivity.
::: proof
If $Ta=0$, then $a_k/k=0$ for every $k$, so $a=0$; hence $T$ is injective.

Given $b=(b_k)\in X$, define
\[
a_k:=kb_k.
\]
Because $b$ has finite support, so does $a$, hence $a\in X$. Then
\[
(Ta)_k=\frac{a_k}{k}=b_k,
\]
so $T$ is surjective.

Thus
\[
T^{-1}(b_1,b_2,\ldots)=(b_1,2b_2,3b_3,\ldots).
\]
:::

<1>3. Show that the inverse is unbounded.
::: proof
For the standard basis vector $e_n$,
\[
\|e_n\|=1,
\]
whereas
\[
T^{-1}e_n=ne_n
\]
and therefore
\[
\|T^{-1}e_n\|=n.
\]
If $T^{-1}$ were bounded, there would be a constant $C$ with
\[
n=\|T^{-1}e_n\|\le C\|e_n\|=C
\]
for every $n$, impossible. Hence
\[
\boxed{T^{-1}\text{ is unbounded}.}
\]
:::
:::
