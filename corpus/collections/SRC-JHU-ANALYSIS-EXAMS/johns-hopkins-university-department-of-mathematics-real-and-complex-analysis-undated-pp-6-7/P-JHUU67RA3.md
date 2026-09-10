---
schema: qual/card@1
id: P-JHUU67RA3
kind: problem
title: 'Holder inequality, Young inequality, and $L^p$ Banach spaces'
classification:
  areas:
  - real-analysis
  topics:
  - Lp Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against entry 3 of the undated JHU Real and Complex Analysis exam, pp. 6–7. Corrected the a.e.-quotient issue in the Lp completeness statement, made the convolution item well-defined on the line, and stated Hölder with absolute values.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-10
  note: Restored the source's unrestricted smooth-kernel convolution obstruction on [0,1]; the prior authored version had narrowed h to compact support and changed the ambient domain to the line.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-10
  note: Replaced part (3) by a proof for arbitrary smooth h using the explicit interval convolution formula and a discontinuous L1 target.
---

::: {.problem}
Let $I=[0,1]$ and write
\[
\|f\|_p=\left(\int_I|f|^p\right)^{1/p}
\quad(1\le p<\infty),
\qquad
\|f\|_\infty=\operatorname*{ess\,sup}_I|f|.
\]

1. Show that $C(I)$ with the norm $\|\cdot\|_p$, $1\le p<\infty$, is not Banach.

2. Prove that $L^p(I)$, meaning measurable finite-$p$-norm functions modulo equality almost everywhere, is Banach for $1\le p\le\infty$.

3. Prove that there is no smooth function $h\in C^\infty(\mathbb R)$ such that
\[
(f*h)(x):=\int_0^1 f(y)h(x-y)\,dy=f(x)
\qquad\text{for every }f\in L^1([0,1])\text{ and every }x\in[0,1].
\]

4. Prove Hölder's inequality: if $1/p+1/q=1$, then
\[
\int_I|fg|\le \|f\|_p\|g\|_q.
\]

5. Deduce Young's convolution inequality on $\mathbb R$: if
\[
1\le p,q,r\le\infty,
\qquad
\frac1p+\frac1q=1+\frac1r,
\]
then
\[
\|f*g\|_r\le\|f\|_p\|g\|_q.
\]
:::

::: {.solution}
<1>1. $C(I)$ is not complete in the $L^p$ norm for finite $p$.
::: {.proof}
Let
\[
f=\mathbf1_{[0,1/2]}.
\]
Choose continuous functions $f_n$ which equal $1$ on $[0,1/2-1/n]$, equal $0$ on $[1/2+1/n,1]$, and interpolate linearly in between. Then
\[
\|f_n-f\|_p^p\le \frac{2}{n}\longrightarrow0.
\]
Thus $(f_n)$ is Cauchy in $C(I)$ with the $L^p$ norm. If it converged in that norm to some $g\in C(I)$, uniqueness of $L^p$ limits would give $g=f$ almost everywhere. Continuity would then force $g=1$ on $[0,1/2)$ and $g=0$ on $(1/2,1]$, impossible at $1/2$. Hence $C(I)$ is not complete.
:::

<1>2. $L^p(I)$ is complete.
::: {.proof}
First let $1\le p<\infty$ and let $(f_n)$ be Cauchy in $L^p$. Choose a subsequence $(f_{n_k})$ such that
\[
\|f_{n_{k+1}}-f_{n_k}\|_p\le2^{-k}.
\]
Set
\[
g_m=|f_{n_1}|+\sum_{k=1}^{m}|f_{n_{k+1}}-f_{n_k}|.
\]
By Minkowski,
\[
\|g_m\|_p
\le \|f_{n_1}\|_p+\sum_{k=1}^{m}2^{-k},
\]
so by monotone convergence the pointwise limit $g=\lim_m g_m$ belongs to $L^p$. Therefore
\[
\sum_{k=1}^\infty |f_{n_{k+1}}(x)-f_{n_k}(x)|<\infty
\]
for almost every $x$. The subsequence consequently converges pointwise a.e. to some measurable $f$.

Moreover, for every $k$,
\[
|f-f_{n_k}|
\le \sum_{j=k}^\infty |f_{n_{j+1}}-f_{n_j}|,
\]
and Minkowski gives
\[
\|f-f_{n_k}\|_p\le\sum_{j=k}^\infty2^{-j}\longrightarrow0.
\]
Since the original sequence is Cauchy, it follows that $f_n\to f$ in $L^p$.

For $p=\infty$, if $(f_n)$ is Cauchy in essential-supremum norm, choose representatives after discarding the countable union of null exceptional sets in the Cauchy estimates. Off that null set, $(f_n(x))$ is uniformly Cauchy, hence converges uniformly to a bounded measurable $f$, and $\|f_n-f\|_\infty\to0$. Thus $L^\infty(I)$ is complete as well.
:::

<1>3. There is no smooth convolution identity on $L^1([0,1])$.
::: {.proof}
Suppose $h\in C^\infty(\mathbb R)$ satisfied the stated identity for every $f\in L^1([0,1])$. Fix such an $f$. For $x,x'\in[0,1]$,
\[
\begin{aligned}
|(f*h)(x')-(f*h)(x)|
&\le \int_0^1 |f(y)|\,|h(x'-y)-h(x-y)|\,dy\\
&\le \|f\|_1\sup_{t\in[-1,1]}|h(t+x'-x)-h(t)|.
\end{aligned}
\]
For $x,x'\in[0,1]$, all arguments of $h$ occurring above lie in the compact interval $[-1,1]$. Since $h$ is continuous, it is uniformly continuous there. Hence the right-hand side tends to $0$ as $x'\to x$, so $f*h$ is continuous on $[0,1]$.

Now take
\[
f=\mathbf1_{[0,1/2]}.
\]
This belongs to $L^1([0,1])$ but is discontinuous at $1/2$. The assumed identity would give
\[
f(x)=(f*h)(x)
\qquad(x\in[0,1]),
\]
while the right-hand side is continuous. This is impossible. Therefore no smooth $h$ can act as the identity convolution kernel on all of $L^1([0,1])$.
:::

<1>4. Hölder's inequality.
::: {.proof}
The endpoint cases $p=1,q=\infty$ and $p=\infty,q=1$ are immediate. Assume $1<p,q<\infty$ and $1/p+1/q=1$. If either norm vanishes there is nothing to prove, so normalize
\[
F=\frac{|f|}{\|f\|_p},
\qquad
G=\frac{|g|}{\|g\|_q}.
\]
Young's scalar inequality gives
\[
F(x)G(x)\le \frac{F(x)^p}{p}+\frac{G(x)^q}{q}.
\]
Integrating,
\[
\int_I FG
\le \frac1p\int_I F^p+\frac1q\int_I G^q
=\frac1p+\frac1q=1.
\]
Multiplying back by the norms yields
\[
\int_I|fg|\le\|f\|_p\|g\|_q.
\]
:::

<1>5. Young's convolution inequality.
::: {.proof}
If $r=\infty$, then $1/p+1/q=1$, so Hölder gives directly
\[
|(f*g)(x)|\le\|f\|_p\|g\|_q.
\]

Assume $r<\infty$. The relation implies $r\ge p,q$. For fixed $x$, write
\[
|f(y)g(x-y)|
=
\bigl(|f(y)|^p|g(x-y)|^q\bigr)^{1/r}
|f(y)|^{1-p/r}|g(x-y)|^{1-q/r}.
\]
Apply generalized Hölder in $y$ with reciprocal exponents
\[
\frac1r,
\qquad
\frac1p-\frac1r,
\qquad
\frac1q-\frac1r,
\]
whose sum is $1$. This gives
\[
|f*g(x)|
\le
\left(\int |f(y)|^p|g(x-y)|^q\,dy\right)^{1/r}
\|f\|_p^{1-p/r}\|g\|_q^{1-q/r}.
\]
Raise to the $r$th power and integrate in $x$. Tonelli and translation invariance give
\[
\begin{aligned}
\|f*g\|_r^r
&\le
\|f\|_p^{r-p}\|g\|_q^{r-q}
\iint |f(y)|^p|g(x-y)|^q\,dy\,dx\\
&=
\|f\|_p^{r-p}\|g\|_q^{r-q}
\|f\|_p^p\|g\|_q^q\\
&=\|f\|_p^r\|g\|_q^r.
\end{aligned}
\]
Taking $r$th roots proves
\[
\|f*g\|_r\le\|f\|_p\|g\|_q.
\]
:::
:::
