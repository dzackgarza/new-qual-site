---
schema: qual/card@1
id: P-RASP07C
kind: problem
title: "True/false on metric spaces, distributions, norms, and measure theory"
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
  note: Checked against Problem 3 of the official UCSD Spring 2007 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
True or false.
For each part, determine if it is always true or sometimes false.
If true give a brief proof.
If false give a counterexample or disprove it.

(a) If $X$ is a complete metric space and $\{x_n\}$ a bounded sequence in $X$, then $\{x_n\}$ has a convergent subsequence.

(b) If $f \in \mathcal{S}(\mathbb{R})$ (the space of Schwartz functions) and $\frac{d\hat{f}}{d\xi} = 0$, then $f = 0$.

(c) If $T \in \mathcal{S}'(\mathbb{R})$ (the space of tempered distributions) and $\frac{d\hat{T}}{d\xi} = 0$, then $T = 0$.

(d) Let $\|\cdot\|_1$ and $\|\cdot\|_2$ be two norms on a vector space $X$ such that $X$ is complete with respect to both norms.
If $\|\cdot\|_1 \leq \|\cdot\|_2$, then there exists $C > 0$ such that $\|\cdot\|_2 \leq C\|\cdot\|_1$.

(e) Let $\|\cdot\|_1$ and $\|\cdot\|_2$ be two norms on a vector space $X$ such that $X$ is complete with respect to one of the two norms.
If $\|\cdot\|_1 \leq \|\cdot\|_2$, then there exists $C > 0$ such that $\|\cdot\|_2 \leq C\|\cdot\|_1$.

(f) If $\mu(X) < \infty$, then $L^1(X, \mu) \subset L^2(X, \mu)$.

(g) $\ell^1(\mathbb{N}) \subset \ell^2(\mathbb{N})$.

(h) If $\mu_1$ and $\mu_2$ are two positive measures on a measurable space $(X, \mathcal{M})$ such that $\mu_1$ is absolutely continuous with respect to $\mu_2$, then there exists a measurable function $f$ on $X$ such that $d\mu_1 = f\,d\mu_2$.
:::

::: solution
<1>1. Part (a) is false.
::: proof
Take $X=\ell^2$ and let $x_n=e_n$, the standard unit vectors. Then $(e_n)$ is bounded, but
\[
\|e_n-e_m\|_2=\sqrt2
\qquad(n\ne m),
\]
so it has no Cauchy, hence no convergent, subsequence. Completeness does not imply sequential compactness of bounded sets.
:::

<1>2. Part (b) is true.
::: proof
If
\[
\frac d{d\xi}\widehat f=0,
\]
then the smooth function $\widehat f$ is constant. Since $f\in\mathcal S(\mathbb R)$, also $\widehat f\in\mathcal S(\mathbb R)$. The only constant Schwartz function is $0$, so
\[
\widehat f=0.
\]
Injectivity of the Fourier transform on $\mathcal S$ gives
\[
\boxed{f=0.}
\]
:::

<1>3. Part (c) is false.
::: proof
Let
\[
T=\delta_0.
\]
Its Fourier transform is a nonzero constant tempered distribution (the precise constant depends on the Fourier-transform convention). Therefore
\[
\frac d{d\xi}\widehat T=0,
\]
but $T\ne0$.
:::

<1>4. Part (d) is true.
::: proof
The identity map
\[
I:(X,\|\cdot\|_2)\longrightarrow(X,\|\cdot\|_1)
\]
is bounded because $\|x\|_1\le\|x\|_2$. It is also a bijection between Banach spaces. By the Bounded Inverse Theorem, its inverse is bounded. Hence there is $C>0$ such that
\[
\boxed{\|x\|_2\le C\|x\|_1\qquad\forall x\in X.}
\]
:::

<1>5. Part (e) is false.
::: proof
Take
\[
X=C^1([0,1]),
\]
with
\[
\|f\|_1:=\|f\|_\infty,
\qquad
\|f\|_2:=\|f\|_\infty+\|f'\|_\infty.
\]
Then $\|f\|_1\le\|f\|_2$, and $(X,\|\cdot\|_2)$ is Banach. But no constant $C$ satisfies
\[
\|f\|_2\le C\|f\|_1
\]
for all $f$. Indeed, for
\[
f_n(x)=\frac{\sin(nx)}n,
\]
we have
\[
\|f_n\|_1\le\frac1n,
\qquad
\|f_n\|_2\ge\|f_n'\|_\infty=1.
\]
Thus completeness of only one norm is insufficient.
:::

<1>6. Part (f) is false.
::: proof
On $X=(0,1)$ with Lebesgue measure, let
\[
f(x)=x^{-1/2}.
\]
Then
\[
\int_0^1|f(x)|\,dx<\infty,
\]
but
\[
\int_0^1|f(x)|^2\,dx
=\int_0^1\frac{dx}{x}=\infty.
\]
Thus $f\in L^1\setminus L^2$ even though $\mu(X)<\infty$.
:::

<1>7. Part (g) is true.
::: proof
If $a=(a_n)\in\ell^1$, then
\[
\sup_n|a_n|\le\sum_n|a_n|=\|a\|_1.
\]
Hence
\[
\sum_n|a_n|^2
\le \left(\sup_n|a_n|\right)\sum_n|a_n|
\le\|a\|_1^2.
\]
Therefore
\[
\boxed{\|a\|_2\le\|a\|_1,\qquad \ell^1\subseteq\ell^2.}
\]
:::

<1>8. Part (h) is false without additional hypotheses.
::: proof
Let
\[
X=\{x\},\qquad \mathcal M=\{\varnothing,X\},
\]
and define positive measures by
\[
\mu_1(X)=1,
\qquad
\mu_2(X)=\infty.
\]
The only $\mu_2$-null set is $\varnothing$, so
\[
\mu_1\ll\mu_2.
\]

If $d\mu_1=f\,d\mu_2$ for some measurable $f$, then $f$ is constant on the one-point space. If $f(x)=0$, then
\[
\int_X f\,d\mu_2=0,
\]
while if $f(x)>0$, then
\[
\int_X f\,d\mu_2=\infty.
\]
Neither value equals $\mu_1(X)=1$. Thus no such density exists.

The usual Radon--Nikodym theorem requires suitable sigma-finiteness (or a comparable semifiniteness/localizability hypothesis) on the measures.
:::
:::
