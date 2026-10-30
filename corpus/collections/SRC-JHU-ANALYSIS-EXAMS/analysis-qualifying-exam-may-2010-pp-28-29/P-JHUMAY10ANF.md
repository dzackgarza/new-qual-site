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
Let $\varphi:\RR\to\RR$ be continuous with compact support.

(a) If $1\le p\le q\le\infty$, prove that there is a constant $A$ such that
$$
\norm{f*\varphi}_q\le A\norm{f}_p
\qquad(f\in L^p).
$$
If you use Young's convolution inequality, prove it.

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
\norm{f*\varphi}_p
&=\norm{\int_{\RR}\varphi(y)f(\cdot-y)\,dy}_p\\
&\le\int_{\RR}\abs{\varphi(y)}\,\norm{f(\cdot-y)}_p\,dy\\
&=\norm{\varphi}_1\norm{f}_p.
\end{aligned}
$$
Also, by [[PR-7BGSE|Hölder's inequality]], if $p'$ is conjugate to $p$,
$$
\abs{(f*\varphi)(x)}\le\norm{f}_p\,\norm{\varphi(x-\cdot)}_{p'}=\norm{f}_p\norm{\varphi}_{p'},
$$
so
$$
\norm{f*\varphi}_\infty\le\norm{\varphi}_{p'}\norm{f}_p.
$$
For $p=\infty$, necessarily $q=\infty$, and directly
$$
\norm{f*\varphi}_\infty\le\norm{\varphi}_1\norm{f}_\infty.
$$

:::

:::

::: {.pf-step #s2}

Interpolate the output norm for $p\le q\le\infty$.

::: pf-proof

Assume $1\le p<\infty$ and let $h=f*\varphi$. If $p\le q<\infty$, then
$$
\norm{h}_q^q
=\int \abs{h}^{q-p}\abs{h}^p
\le\norm{h}_\infty^{q-p}\norm{h}_p^p.
$$
Hence
$$
\norm{h}_q\le\norm{h}_\infty^{1-p/q}\norm{h}_p^{p/q}.
$$
Using step [](#s1){.pf-ref},
$$
\norm{f*\varphi}_q
\le\norm{\varphi}_{p'}^{1-p/q}\norm{\varphi}_1^{p/q}\norm{f}_p.
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
(\psi*\varphi)(0)=\int_{\RR}\abs{\varphi(y)}^2\,dy>0.
$$
Thus $h:=\psi*\varphi$ is not identically zero.

Choose $L>0$ so large that the translates $\psi(\cdot-kL)$ have pairwise disjoint supports, and likewise the translates $h(\cdot-kL)$ have pairwise disjoint supports. Define
$$
f_N=\sum_{k=1}^N\psi(\cdot-kL).
$$
Then
$$
\norm{f_N}_p=N^{1/p}\norm{\psi}_p,
$$
while
$$
f_N*\varphi=\sum_{k=1}^N h(\cdot-kL)
$$
and therefore
$$
\norm{f_N*\varphi}_q=N^{1/q}\norm{h}_q.
$$
If an estimate $\norm{f*\varphi}_q\le A\norm{f}_p$ held with $p>q$, then
$$
N^{1/q-1/p}\le A\frac{\norm{\psi}_p}{\norm{h}_q}
$$
for every $N$, impossible because $1/q-1/p>0$. Hence no such general estimate can hold for $p>q$.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref} and [](#s2){.pf-ref} prove part (a), and step [](#s3){.pf-ref} proves part (b).

:::

:::

:::
