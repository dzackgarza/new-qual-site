---
schema: qual/card@1
id: P-JHUMAY10ANF
kind: problem
title: 'Convolution with a compactly supported kernel maps $L^p$ to $L^q$ exactly when $p\le q$'
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

::: pf

::: {.pf-step #s1}

Endpoint bounds.

::: pf-proof

For $1\le p<\infty$, Minkowski's integral inequality gives
$$
\begin{aligned}
\|f*\varphi\|_p
&=\left\|\int_{\mathbb R}\varphi(y)f(\cdot-y)\,dy\right\|_p\\
&\le\int_{\mathbb R}|\varphi(y)|\,\|f(\cdot-y)\|_p\,dy\\
&=\|\varphi\|_1\|f\|_p.
\end{aligned}
$$
Also, by [[PR-7BGSE|Hölder's inequality]], if $p'$ is conjugate to $p$,
$$
|(f*\varphi)(x)|\le\|f\|_p\,\|\varphi(x-\cdot)\|_{p'}=\|f\|_p\|\varphi\|_{p'},
$$
so
$$
\|f*\varphi\|_\infty\le\|\varphi\|_{p'}\|f\|_p.
$$
For $p=\infty$, necessarily $q=\infty$, and directly
$$
\|f*\varphi\|_\infty\le\|\varphi\|_1\|f\|_\infty.
$$

:::

:::

::: {.pf-step #s2}

Interpolate the output norm for $p\le q\le\infty$.

::: pf-proof

Assume $1\le p<\infty$ and let $h=f*\varphi$. If $p\le q<\infty$, then
$$
\|h\|_q^q
=\int |h|^{q-p}|h|^p
\le\|h\|_\infty^{q-p}\|h\|_p^p.
$$
Hence
$$
\|h\|_q\le\|h\|_\infty^{1-p/q}\|h\|_p^{p/q}.
$$
Using step [](#s1){.pf-ref},
$$
\|f*\varphi\|_q
\le\|\varphi\|_{p'}^{1-p/q}\|\varphi\|_1^{p/q}\|f\|_p.
$$
The case $q=\infty$ is already contained in step [](#s1){.pf-ref}. This proves part (a).

:::

:::

::: {.pf-step #s3}

Failure when $p>q$.

::: pf-proof

Choose a nonzero compactly supported continuous kernel $\varphi$. Let
$$
\psi(x)=\overline{\varphi(-x)},
$$
so $\psi\in C_c$ and
$$
(\psi*\varphi)(0)=\int_{\mathbb R}|\varphi(y)|^2\,dy>0.
$$
Thus $h:=\psi*\varphi$ is not identically zero.

Choose $L>0$ so large that the translates $\psi(\cdot-kL)$ have pairwise disjoint supports, and likewise the translates $h(\cdot-kL)$ have pairwise disjoint supports. Define
$$
f_N=\sum_{k=1}^N\psi(\cdot-kL).
$$
Then
$$
\|f_N\|_p=N^{1/p}\|\psi\|_p,
$$
while
$$
f_N*\varphi=\sum_{k=1}^N h(\cdot-kL)
$$
and therefore
$$
\|f_N*\varphi\|_q=N^{1/q}\|h\|_q.
$$
If an estimate $\|f*\varphi\|_q\le A\|f\|_p$ held with $p>q$, then
$$
N^{1/q-1/p}\le A\frac{\|\psi\|_p}{\|h\|_q}
$$
for every $N$, impossible because $1/q-1/p>0$. Hence no such general estimate can hold for $p>q$.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref} and [](#s2){.pf-ref} prove part (a), and step [](#s3){.pf-ref} proves part (b).

:::

:::

:::
