---
schema: qual/card@1
id: P-RASP04A
kind: problem
title: "True/false on null sets, nowhere dense sets, and subspaces"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 1 of the official UCSD Spring 2004 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
In this problem $(X, \|\cdot\|)$ is an infinite dimensional normed space.
Determine which of the following statements are true.
For the true statements give a brief reason and for the false statements give a counterexample.

(a) If $A = \mathbb{R} \setminus E$ and $m(E) = 0$, then $\bar{A} = \mathbb{R}$.

(b) Every $m$-null set $E \in \mathcal{B}_{\mathbb{R}}$ is nowhere dense in $\mathbb{R}$.

(c) Every proper subspace $E \subset X$ is nowhere dense.

(d) If $E$ is a subspace of $X$ with non-empty interior, then $E = X$.
:::

::: solution
<1>1. Part (a) is true.
::: proof
Let $A=\mathbb R\setminus E$ with $m(E)=0$. Every nonempty open interval has positive Lebesgue measure, so no nonempty open interval can be contained in $E$. Equivalently, every nonempty open interval meets $A$. Thus $A$ is dense in $\mathbb R$, and
\[
\boxed{\overline A=\mathbb R.}
\]
:::

<1>2. Part (b) is false.
::: proof
Take
\[
E=\mathbb Q.
\]
Then $E$ is Borel and has Lebesgue measure zero, but
\[
\overline E=\mathbb R.
\]
Hence the interior of $\overline E$ is all of $\mathbb R$, so $E$ is not nowhere dense.
:::

<1>3. Part (c) is false.
::: proof
Take
\[
X=\ell^2
\]
and let
\[
E=c_{00}
\]
be the subspace of finitely supported sequences. Then $E$ is a proper linear subspace of $\ell^2$, but it is dense in $\ell^2$. Therefore
\[
\overline E=X,
\]
so $E$ is not nowhere dense.
:::

<1>4. Part (d) is true.
::: proof
Suppose the subspace $E\subset X$ has nonempty interior. Then for some $x_0\in E$ and $r>0$,
\[
B(x_0,r)\subset E.
\]
Since $x_0\in E$ and $E$ is a subspace, subtracting $x_0$ gives
\[
B(0,r)\subset E.
\]
Now fix any $x\in X$. Choose $t>0$ so small that
\[
\|tx\|<r.
\]
Then $tx\in E$, and since $E$ is a subspace,
\[
x=t^{-1}(tx)\in E.
\]
Thus
\[
\boxed{E=X.}
\]
:::
:::
