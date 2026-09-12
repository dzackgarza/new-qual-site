---
schema: qual/card@1
id: P-WESRA05-3
kind: problem
title: Norm-induced metrics, Banach spaces, and uniform boundedness
classification:
  areas: [real-analysis]
  topics: [Functional Analysis, Banach Spaces]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
  note: Checked directly against Problem 3 of the scanned Wesleyan Real Analysis Preliminary Examination, 2005, in analysis_2003-2007.pdf.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: problem
Let $B$ be a real vector space.

1. Define a norm on $B$.
2. Give the metric induced by a norm and prove that it is a metric.
3. Define a Banach space.
4. State the Uniform Boundedness Theorem for a family of bounded linear maps from the Banach space $B$ to a normed space $N$, and explain the main idea of its proof.
:::

::: solution
<1>1. Define a norm.
::: proof
A norm is a map $\|\cdot\|:B\to[0,\infty)$ such that for all $x,y\in B$ and $a\in\mathbb R$,
\[
\|x\|=0\iff x=0,
\qquad
\|ax\|=|a|\,\|x\|,
\qquad
\|x+y\|\le\|x\|+\|y\|.
\]
:::

<1>2. Construct the induced metric.
::: proof
Define
\[
d(x,y)=\|x-y\|.
\]
Then $d(x,y)\ge0$, and
\[
d(x,y)=0\iff x-y=0\iff x=y.
\]
Also
\[
d(x,y)=\|x-y\|=\|-(y-x)\|=d(y,x),
\]
and the norm triangle inequality gives
\[
d(x,z)=\|x-z\|
\le\|x-y\|+\|y-z\|
=d(x,y)+d(y,z).
\]
Thus $d$ is a metric.
:::

<1>3. Define a Banach space.
::: proof
A normed vector space is a Banach space if it is complete for the metric induced by its norm; equivalently, every norm-Cauchy sequence converges in norm to an element of the space.
:::

<1>4. State Uniform Boundedness.
::: proof
Let $B$ be Banach, let $N$ be normed, and let $\mathcal T$ be a family of bounded linear operators $T:B\to N$. If for every $x\in B$,
\[
\sup_{T\in\mathcal T}\|Tx\|<\infty,
\]
then
\[
\boxed{\sup_{T\in\mathcal T}\|T\|<\infty.}
\]
This is the Uniform Boundedness Principle, or Banach--Steinhaus theorem.
:::

<1>5. Explain the Baire-category argument.
::: proof
For $m\in\mathbb N$, set
\[
E_m=\left\{x\in B:\sup_{T\in\mathcal T}\|Tx\|\le m\right\}.
\]
Each $E_m$ is closed, because it is the intersection over $T\in\mathcal T$ of the closed sets $\{x:\|Tx\|\le m\}$. Pointwise boundedness says
\[
B=\bigcup_{m=1}^\infty E_m.
\]
Since $B$ is complete, Baire's theorem implies that some $E_m$ contains a ball
\[
B(x_0,r)\subseteq E_m.
\]
If $\|h\|<r$, then $x_0$ and $x_0+h$ lie in $E_m$, so for every $T\in\mathcal T$,
\[
\|Th\|
\le\|T(x_0+h)\|+\|Tx_0\|
\le2m.
\]
By scaling, for arbitrary $x\ne0$,
\[
\|Tx\|\le \frac{2m}{r}\|x\|.
\]
Hence
\[
\sup_{T\in\mathcal T}\|T\|\le\frac{2m}{r}<\infty.
\]
:::
:::
