---
schema: qual/card@1
id: P-RAF16G
kind: problem
title: "Absolutely convergent series from bounded linear functional on c_0"
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
  note: Checked against Problem 7 of the official UCSD Fall 2016 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
Recall that $c_0 = \{(a_1, a_2, \ldots) : \text{all } a_k \in \mathbb{R} \text{ and } \lim_{k \to \infty} a_k = 0\}$ is a Banach space with respect to the usual component-wise addition and scalar multiplication, and the norm $\|(a_1, a_2, \ldots)\| = \sup_{k \geq 1} |a_k|$.
Let $\xi_k \in \mathbb{R}$ ($k = 1, 2, \ldots$). Assume that $\sum_{k=1}^{\infty} a_k \xi_k$ converges for any $(a_1, a_2, \ldots) \in c_0$.
Use the Principle of Uniform Boundedness to prove that $\sum_{k=1}^{\infty} |\xi_k| < \infty$.
:::

::: solution
<1>1. Define the partial-sum functionals.
::: proof
For each $n\ge1$, define
\[
T_n:c_0\to\mathbb R,
\qquad
T_n(a)=\sum_{k=1}^n a_k\xi_k.
\]
Then $T_n$ is a bounded linear functional and
\[
|T_n(a)|
\le \|a\|_\infty\sum_{k=1}^n|\xi_k|.
\]
Hence
\[
\|T_n\|\le\sum_{k=1}^n|\xi_k|.
\]
:::

<1>2. Compute the norm exactly.
::: proof
For fixed $n$, define $a^{(n)}\in c_0$ by
\[
a_k^{(n)}=
\begin{cases}
\operatorname{sgn}(\xi_k),&1\le k\le n,\\
0,&k>n,
\end{cases}
\]
with $\operatorname{sgn}(0)=0$. Then
\[
\|a^{(n)}\|_\infty\le1
\]
and
\[
T_n(a^{(n)})=\sum_{k=1}^n|\xi_k|.
\]
Therefore
\[
\boxed{\|T_n\|=\sum_{k=1}^n|\xi_k|.}
\]
:::

<1>3. Apply the Principle of Uniform Boundedness.
::: proof
By hypothesis, for every fixed $a\in c_0$, the scalar sequence
\[
T_n(a)=\sum_{k=1}^n a_k\xi_k
\]
converges. Hence
\[
\sup_n|T_n(a)|<\infty
\]
for every $a\in c_0$.

Since $c_0$ is Banach, the Principle of Uniform Boundedness gives
\[
\sup_n\|T_n\|<\infty.
\]
Using Step 2,
\[
\sup_n\sum_{k=1}^n|\xi_k|<\infty.
\]
The partial sums are increasing, so they converge to a finite limit. Thus
\[
\boxed{\sum_{k=1}^\infty|\xi_k|<\infty.}
\]
:::
:::
