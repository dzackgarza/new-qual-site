---
schema: qual/card@1
id: P-RASP23A
kind: problem
title: "True/false on linear functionals, weak convergence, and measurable sets"
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
  date: 2026-09-09
  note: Checked against Problem 1 of the official UCSD Spring 2023 real-analysis qualifying exam. The prior solution incorrectly treated “linear functional” in part (a) as automatically continuous.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
TRUE or FALSE: If true, prove it.
If false, disprove it.

(a) If $f$ is a linear functional of a normed vector space $X$, $f^{-1}(0)$ is closed.

(b) In a Hilbert space, if $\{x_n\}$ converges to $x$ weakly and $\|x_n\| \to \|x\|$, then $\{x_n\}$ converges to $x$ strongly, namely $\|x_n - x\| \to 0$.

(c) Let $E \subset \mathbb{R}$ be a Lebesgue measurable set and assume that there exists $0 < \alpha < 1$ such that $m(E \cap I) \leq \alpha \, m(I)$ for all open intervals $I$.
Then $m(E) = 0$.
:::

::: solution
<1>1. Part (a) is false.
::: proof
Let
\[
X=c_{00}
\]
be the vector space of finitely supported real sequences, equipped with the $\ell^2$ norm. Define
\[
F(x)=\sum_{k=1}^{\infty}k x_k,
\]
where the sum is finite because $x\in c_{00}$. Then $F$ is a linear functional on the normed space $X$.

For $n\ge2$, set
\[
x^{(n)}=e_1-\frac1n e_n.
\]
Then
\[
F(x^{(n)})=1-1=0,
\]
so $x^{(n)}\in\ker F$. But
\[
\|x^{(n)}-e_1\|_2=\frac1n\longrightarrow0,
\]
while
\[
F(e_1)=1\ne0.
\]
Thus $e_1$ lies in the closure of $\ker F$ but not in $\ker F$, so $F^{-1}(0)$ need not be closed.
:::

<1>2. Part (b) is true.
::: proof
Weak convergence gives
\[
\langle x_n,x\rangle\longrightarrow\langle x,x\rangle=\|x\|^2.
\]
Hence
\[
\begin{aligned}
\|x_n-x\|^2
&=\|x_n\|^2-2\operatorname{Re}\langle x_n,x\rangle+\|x\|^2\\
&\longrightarrow \|x\|^2-2\|x\|^2+\|x\|^2=0.
\end{aligned}
\]
Therefore $x_n\to x$ strongly.
:::

<1>3. Part (c) is true.
::: proof
Suppose $m(E)>0$. By the Lebesgue density theorem, almost every $x\in E$ is a density point of $E$. Choose such an $x$. Then
\[
\frac{m(E\cap(x-r,x+r))}{2r}\longrightarrow1
\qquad(r\downarrow0).
\]
Since $\alpha<1$, for sufficiently small $r>0$ we obtain
\[
m(E\cap(x-r,x+r))>\alpha\,2r,
\]
contradicting the assumed bound for every open interval. Hence
\[
\boxed{m(E)=0.}
\]
:::
:::
