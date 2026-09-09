---
schema: qual/card@1
id: P-JHUMAY10ANF
kind: problem
title: 'Convolution with a compactly supported kernel maps $L^p$ to $L^q$ exactly in the expected direction'
classification:
  areas:
  - real-analysis
  topics:
  - Convolution
  - Lp Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 6 of the JHU Analysis Qualifying Exam, May 2010, in the preserved exam collection.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: {.problem}
Let $\varphi:\mathbb R\to\mathbb R$ be continuous with compact support.

(a) If $1\le p\le q\le\infty$, prove that there is a constant $A$ such that
\[
\|f*\varphi\|_q\le A\|f\|_p
\qquad(f\in L^p).
\]

(b) Show by example that no such general estimate can hold when $p>q$.
:::

::: {.solution}
<1>1. Endpoint bounds.
::: {.proof}
For $1\le p<\infty$, Minkowski's integral inequality gives
\[
\begin{aligned}
\|f*\varphi\|_p
&=\left\|\int_{\mathbb R}\varphi(y)f(\cdot-y)\,dy\right\|_p\\
&\le\int_{\mathbb R}|\varphi(y)|\,\|f(\cdot-y)\|_p\,dy\\
&=\|\varphi\|_1\|f\|_p.
\end{aligned}
\]
Also, by Hölder's inequality, if $p'$ is conjugate to $p$,
\[
|(f*\varphi)(x)|\le\|f\|_p\,\|\varphi(x-\cdot)\|_{p'}=\|f\|_p\|\varphi\|_{p'},
\]
so
\[
\|f*\varphi\|_\infty\le\|\varphi\|_{p'}\|f\|_p.
\]
For $p=\infty$, necessarily $q=\infty$, and directly
\[
\|f*\varphi\|_\infty\le\|\varphi\|_1\|f\|_\infty.
\]
:::

<1>2. Interpolate the output norm for $p\le q\le\infty$.
::: {.proof}
Assume $1\le p<\infty$ and let $h=f*\varphi$. If $p\le q<\infty$, then
\[
\|h\|_q^q
=\int |h|^{q-p}|h|^p
\le\|h\|_\infty^{q-p}\|h\|_p^p.
\]
Hence
\[
\|h\|_q\le\|h\|_\infty^{1-p/q}\|h\|_p^{p/q}.
\]
Using <1>1,
\[
\|f*\varphi\|_q
\le\|\varphi\|_{p'}^{1-p/q}\|\varphi\|_1^{p/q}\|f\|_p.
\]
The case $q=\infty$ is already contained in <1>1. This proves part (a).
:::

<1>3. Failure when $p>q$.
::: {.proof}
Choose a nonzero compactly supported continuous kernel $\varphi$. Let
\[
\psi(x)=\overline{\varphi(-x)},
\]
so $\psi\in C_c$ and
\[
(\psi*\varphi)(0)=\int_{\mathbb R}|\varphi(y)|^2\,dy>0.
\]
Thus $h:=\psi*\varphi$ is not identically zero.

Choose $L>0$ so large that the translates $\psi(\cdot-kL)$ have pairwise disjoint supports, and likewise the translates $h(\cdot-kL)$ have pairwise disjoint supports. Define
\[
f_N=\sum_{k=1}^N\psi(\cdot-kL).
\]
Then
\[
\|f_N\|_p=N^{1/p}\|\psi\|_p,
\]
while
\[
f_N*\varphi=\sum_{k=1}^N h(\cdot-kL)
\]
and therefore
\[
\|f_N*\varphi\|_q=N^{1/q}\|h\|_q.
\]
If an estimate $\|f*\varphi\|_q\le A\|f\|_p$ held with $p>q$, then
\[
N^{1/q-1/p}\le A\frac{\|\psi\|_p}{\|h\|_q}
\]
for every $N$, impossible because $1/q-1/p>0$. Hence no such general estimate can hold for $p>q$.
:::
:::
