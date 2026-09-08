---
schema: qual/card@1
id: P-RAF21C
kind: problem
title: "The averaging operator on L^p: norm bound and non-surjectivity of I - T"
classification:
  areas:
  - real-analysis
  topics:
  - Integral Operators
  - Lp Spaces
  - Minkowski Inequality
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 3 of the official UCSD Fall 2021 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
Let $p \in (1, \infty)$, and for $f \in L^p(\mathbb{R})$ define $Tf(x) := \int_0^1 f(x + y) \, dy$.

(a) Show that $\|Tf\|_p \leq \|f\|_p$, and equality holds if and only if $f = 0$ almost everywhere.

(b) Prove that $(I - T)(L^p(\mathbb{R})) \neq L^p(\mathbb{R})$, where $I$ is the identity map on $L^p(\mathbb{R})$.
:::

::: solution
<1>1. Prove the contraction estimate.
::: proof
For almost every $x$, Jensen's inequality for the probability measure on $[0,1]$ gives
\[
|Tf(x)|^p
=\left|\int_0^1 f(x+y)\,dy\right|^p
\le \int_0^1 |f(x+y)|^p\,dy.
\]
Integrating in $x$ and using Tonelli together with translation invariance of Lebesgue measure,
\[
\begin{aligned}
\|Tf\|_p^p
&\le \int_{\mathbb R}\int_0^1|f(x+y)|^p\,dy\,dx\\
&=\int_0^1\int_{\mathbb R}|f(x+y)|^p\,dx\,dy\\
&=\|f\|_p^p.
\end{aligned}
\]
Hence
\[
\boxed{\|Tf\|_p\le\|f\|_p.}
\]
:::

<1>2. Analyze equality in the contraction estimate.
::: proof
Suppose $\|Tf\|_p=\|f\|_p$. Then equality holds in the pointwise Jensen inequality for almost every $x$. Since $1<p<\infty$, the function $z\mapsto |z|^p$ is strictly convex. Therefore, for almost every $x$, the function
\[
y\longmapsto f(x+y)
\]
is constant for almost every $y\in[0,1]$.

Thus for almost every $x$ there exists $c_x$ such that
\[
f(t)=c_x
\]
for almost every $t\in(x,x+1)$. If two such intervals overlap in a set of positive measure, their constants must agree. Chaining overlapping unit intervals shows that $f$ is almost everywhere equal to one constant on $\mathbb R$. Since $f\in L^p(\mathbb R)$, that constant must be $0$. Hence equality occurs only for $f=0$ almost everywhere.
:::

<1>3. Show that $I-T$ is injective.
::: proof
If $(I-T)f=0$, then $Tf=f$. Hence
\[
\|Tf\|_p=\|f\|_p,
\]
and Step 2 implies $f=0$ almost everywhere. Therefore $I-T$ is injective.
:::

<1>4. Construct approximate fixed points of $T$.
::: proof
Let
\[
f_N=\mathbf1_{[0,N]}.
\]
Then
\[
\|f_N\|_p=N^{1/p}.
\]
For $x\in[0,N-1]$ we have $Tf_N(x)=1=f_N(x)$, while outside a fixed-width neighborhood of the two endpoints the same equality holds with both sides zero. Thus $(I-T)f_N$ is supported in
\[
[-1,0]\cup[N-1,N],
\]
and $|(I-T)f_N|\le1$. Hence
\[
\|(I-T)f_N\|_p\le 2^{1/p}.
\]
Therefore
\[
\frac{\|(I-T)f_N\|_p}{\|f_N\|_p}
\le \left(\frac2N\right)^{1/p}\longrightarrow0.
\]
:::

<1>5. Rule out surjectivity.
::: proof
Suppose $(I-T)(L^p)=L^p$. By Step 3, $I-T$ would then be a bounded bijective operator from the Banach space $L^p(\mathbb R)$ onto itself. The bounded inverse theorem would give a constant $C>0$ such that
\[
\|(I-T)f\|_p\ge C\|f\|_p
\]
for every $f\in L^p$.

Step 4 contradicts such a lower bound. Therefore
\[
\boxed{(I-T)(L^p(\mathbb R))\ne L^p(\mathbb R).}
\]
:::
:::
