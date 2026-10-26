---
schema: qual/card@1
id: P-UCLARA12F-06
kind: problem
title: A maximal-function route to differentiation
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against the Fall 2012 section of the vendored UCLA Analysis Qualifying Exam Solutions compilation.
---

::: {.problem}
Let $f\in L^1(\mathbb R)$ and let $Mf$ denote its maximal function,
\[
(Mf)(x)=\sup_{0<r<\infty}\frac1{2r}\int_{-r}^{r}|f(x-y)|\,dy.
\]
By the Hardy--Littlewood maximal function theorem,
\[
|\{x\in\mathbb R:(Mf)(x)>\lambda\}|\le 3\lambda^{-1}\|f\|_{L^1}
\qquad(\lambda>0).
\]
Using this, show that
\[
\limsup_{r\to0}\frac1{2r}\int_{-r}^{r}|f(y)-f(x)|\,dy=0
\]
for almost every $x\in\mathbb R$.
:::

Define
$$
D f(x)
\coloneqq
\limsup_{r\to0}
\frac1{2r}
\int_{-r}^r|f(x-y)-f(x)|\,dy.
$$

::: pf

::: pf-step

If $g\in C_c(\RR)$, then
$$
Dg(x)=0
$$
for every $x\in\RR$.


::: pf-proof

Fix $x$. By continuity of $g$ at $x$, for every $\varepsilon>0$ there is $\delta>0$ such that
$$
|g(x-y)-g(x)|<\varepsilon
$$
whenever $|y|<\delta$. Hence for $0<r<\delta$,
$$
\frac1{2r}\int_{-r}^r|g(x-y)-g(x)|\,dy<\varepsilon.
$$
Thus the limsup is $0$.

:::

:::

::: pf-step

For every $g\in C_c(\RR)$ and almost every $x$,
$$
Df(x)
\le
M(f-g)(x)+|f(x)-g(x)|.
$$


::: pf-proof

Write $h=f-g$. Then
$$
|f(x-y)-f(x)|
\le
|g(x-y)-g(x)|+|h(x-y)|+|h(x)|.
$$
Averaging over $[-r,r]$ gives
$$
\begin{aligned}
\frac1{2r}\int_{-r}^r|f(x-y)-f(x)|\,dy
&\le
\frac1{2r}\int_{-r}^r|g(x-y)-g(x)|\,dy\\
&\quad+
\frac1{2r}\int_{-r}^r|h(x-y)|\,dy
+|h(x)|.
\end{aligned}
$$
Taking the limsup as $r\to0$, using step <1>1 and the definition of the maximal function, yields the inequality.

:::

:::

::: pf-step

For every $\lambda>0$ and every $g\in C_c(\RR)$,
$$
\bigl|\{x:Df(x)>2\lambda\}\bigr|
\le
\frac4\lambda\|f-g\|_{L^1}.
$$


::: pf-proof

Set $h=f-g$. By step <1>2,
$$
\{Df>2\lambda\}
\subseteq
\{Mh>\lambda\}\cup\{|h|>\lambda\}.
$$
The given Hardy--Littlewood maximal inequality gives
$$
|\{Mh>\lambda\}|
\le\frac3\lambda\|h\|_1.
$$
Chebyshev's inequality gives
$$
|\{|h|>\lambda\}|
\le\frac1\lambda\|h\|_1.
$$
Adding the bounds proves the claim.

:::

:::

::: pf-step

For every $\lambda>0$,
$$
\bigl|\{x:Df(x)>2\lambda\}\bigr|=0.
$$


::: pf-proof

The space $C_c(\RR)$ is dense in $L^1(\RR)$. Given $\varepsilon>0$, choose $g\in C_c(\RR)$ such that
$$
\|f-g\|_1<\frac{\varepsilon\lambda}{4}.
$$
Step <1>3 then gives
$$
|\{Df>2\lambda\}|<\varepsilon.
$$
Since $\varepsilon>0$ is arbitrary, the set has measure zero.

:::

:::

::: pf-step

One has
$$
\boxed{
Df(x)=0
\quad\text{for almost every }x\in\RR.}
$$


::: pf-proof

For each positive rational $q$, step <1>4 shows that the set
$$
\{x:Df(x)>q\}
$$
has measure zero. Their countable union is the set where $Df(x)>0$. Hence $Df=0$ almost everywhere.

:::

:::

::: pf-qed

Step <1>5 is exactly the required differentiation statement.

:::

:::
