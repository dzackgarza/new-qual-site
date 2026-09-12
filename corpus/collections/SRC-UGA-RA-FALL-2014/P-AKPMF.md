---
schema: qual/card@1
id: P-AKPMF
kind: problem
title: $\|f\|_p=\sup_{\|g\|_q=1}|\int fg|$ for $f\in L^p(\RR^n)$ and conjugate exponents
classification:
  areas:
  - real-analysis
  topics:
  - Dual Spaces
  - Lp Spaces
  - Norms
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Problem 6 of the UGA Fall 2014 real-analysis qualifying exam recorded by the collection source.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-25
---

::: problem
Let $1 \leq p,q \leq \infty$ be conjugate exponents, and show that
\[
f \in L^p(\RR^n) \implies \|f\|_{p} = \sup _{\|g\|_{q}=1}\left|\int f(x) g(x) d x\right|
\]
:::
::: solution
<1>1. Hölder gives the upper bound.
::: proof
For every $g\in L^q(\mathbb R^n)$ with $\|g\|_q=1$, Hölder's inequality gives
\[
\left|\int_{\mathbb R^n}f(x)g(x)\,dx\right|
\le \|f\|_p\|g\|_q
=\|f\|_p.
\]
Hence
\[
\sup_{\|g\|_q=1}\left|\int fg\right|\le\|f\|_p.
\]
:::

<1>2. Prove equality when $1<p<\infty$.
::: proof
If $f=0$, the result is immediate. Otherwise define
\[
g(x)=\frac{\overline{f(x)}|f(x)|^{p-2}}{\|f\|_p^{p-1}},
\]
with $g=0$ where $f=0$. Since $q=p/(p-1)$,
\[
\|g\|_q^q
=\frac{\int |f|^{(p-1)q}}{\|f\|_p^{(p-1)q}}
=\frac{\int |f|^p}{\|f\|_p^p}=1.
\]
Moreover,
\[
\int fg
=\frac{\int |f|^p}{\|f\|_p^{p-1}}
=\|f\|_p.
\]
Thus the supremum is at least $\|f\|_p$, and Step 1 gives equality.
:::

<1>3. Prove equality when $p=1$ and $q=\infty$.
::: proof
If $f=0$, there is nothing to prove. Define the phase
\[
\theta(x)=
\begin{cases}
\overline{f(x)}/|f(x)|,&f(x)\ne0,\\
0,&f(x)=0.
\end{cases}
\]
Then $\|\theta\|_\infty=1$ and
\[
\int f\theta=\int |f|=\|f\|_1.
\]
Hence the supremum equals $\|f\|_1$.
:::

<1>4. Prove equality when $p=\infty$ and $q=1$.
::: proof
Let $M=\|f\|_\infty$. If $M=0$, the result is immediate. Fix $\varepsilon\in(0,M)$. By the definition of essential supremum,
\[
A_\varepsilon:=\{x:|f(x)|>M-\varepsilon\}
\]
has positive measure. Since Lebesgue measure on $\mathbb R^n$ is sigma-finite, there is a measurable set
\[
E\subseteq A_\varepsilon,
\qquad
0<m(E)<\infty.
\]
Define
\[
g(x)=\frac{\theta(x)\mathbf1_E(x)}{m(E)},
\qquad
\theta(x)=
\begin{cases}
\overline{f(x)}/|f(x)|,&f(x)\ne0,\\
0,&f(x)=0.
\end{cases}
\]
Then $\|g\|_1=1$ and
\[
\left|\int fg\right|
=\frac1{m(E)}\int_E|f(x)|\,dx
\ge M-\varepsilon.
\]
Letting $\varepsilon\downarrow0$ shows that the supremum is at least $M$. Step 1 gives the reverse inequality, hence equality.
:::

<1>5. Conclude.
::: proof
All conjugate pairs $1\le p,q\le\infty$ have been covered, so
\[
\boxed{
\|f\|_p
=\sup_{\|g\|_q=1}
\left|\int_{\mathbb R^n}f(x)g(x)\,dx\right|.}
\]
:::
:::
