---
schema: qual/card@1
id: P-BERK84S-10
kind: problem
title: Completeness of a one-third Holder space
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 10 of the vendored Berkeley Preliminary Exam, Summer 1984.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Verified the norm axioms, uniform control from the anchor f(0)=0, and passage of the Holder quotient bound to the uniform limit.
---

::: {.problem}
Let $C ^ { 1 / 3 }$ be the set of real valued functions f on the closed interval [0, 1] such that

1. $f ( 0 ) = 0 ;$

2. $\| f \|$ is finite, where $b y$ definition

$$
\| f \| = \operatorname* { s u p } \left\{ { \frac { | f ( x ) - f ( y ) | } { | x - y | ^ { 1 / 3 } } } | x \neq y \right\} .
$$

Verify that $\| \cdot \|$ is a norm for the space $C ^ { 1 / 3 }$ , and prove that $C ^ { 1 / 3 }$ is complete with respect to this norm.
:::


::: {.solution}
For $f\in C^{1/3}$, write
\[
\|f\|_{1/3}
:=\sup_{x\ne y}
\frac{|f(x)-f(y)|}{|x-y|^{1/3}}.
\]

<1>1. The functional $\|\cdot\|_{1/3}$ is a norm on $C^{1/3}$.
::: {.proof}
Nonnegativity is immediate. If $\|f\|_{1/3}=0$, then
\[
|f(x)-f(y)|=0
\]
for all $x,y$, so $f$ is constant. Since $f(0)=0$, this constant is $0$, hence $f=0$.
Conversely $\|0\|_{1/3}=0$.

For $a\in\mathbb R$,
\[
\|af\|_{1/3}
=|a|\,\|f\|_{1/3}.
\]
Finally, for $x\ne y$,
\[
\frac{|(f+g)(x)-(f+g)(y)|}{|x-y|^{1/3}}
\le
\frac{|f(x)-f(y)|}{|x-y|^{1/3}}
+
\frac{|g(x)-g(y)|}{|x-y|^{1/3}}.
\]
Taking the supremum gives
\[
\|f+g\|_{1/3}\le \|f\|_{1/3}+\|g\|_{1/3}.
\]
Thus all norm axioms hold.
:::

<1>2. The Hölder norm controls the uniform norm.
::: {.proof}
Since $f(0)=0$, for every $x\in[0,1]$,
\[
|f(x)|=|f(x)-f(0)|
\le \|f\|_{1/3}|x|^{1/3}
\le \|f\|_{1/3}.
\]
Hence
\[
\|f\|_\infty\le \|f\|_{1/3}.
\]
:::

<1>3. Every Cauchy sequence in $\|\cdot\|_{1/3}$ converges uniformly to a function $f$ with $f(0)=0$.
::: {.proof}
Let $(f_n)$ be Cauchy in $\|\cdot\|_{1/3}$. By <1>2,
\[
\|f_n-f_m\|_\infty
\le \|f_n-f_m\|_{1/3},
\]
so $(f_n)$ is uniformly Cauchy. Since $\mathbb R$ is complete, there is a function $f:[0,1]\to\mathbb R$ such that $f_n\to f$ uniformly. Because each $f_n(0)=0$,
\[
f(0)=\lim_{n\to\infty}f_n(0)=0.
\]
:::

<1>4. In fact $f_n\to f$ in the Hölder norm.
::: {.proof}
Fix $\varepsilon>0$. Since $(f_n)$ is Cauchy, choose $N$ so that
\[
\|f_n-f_m\|_{1/3}<\varepsilon
\qquad(m,n\ge N).
\]
Fix $n\ge N$ and $x\ne y$. Then for every $m\ge N$,
\[
|(f_n-f_m)(x)-(f_n-f_m)(y)|
\le \varepsilon |x-y|^{1/3}.
\]
Letting $m\to\infty$ and using pointwise convergence $f_m\to f$ gives
\[
|(f_n-f)(x)-(f_n-f)(y)|
\le \varepsilon |x-y|^{1/3}.
\]
Therefore
\[
\|f_n-f\|_{1/3}\le\varepsilon
\qquad(n\ge N).
\]
Thus $f_n\to f$ in the given norm. In particular,
\[
\|f\|_{1/3}
\le \|f-f_N\|_{1/3}+\|f_N\|_{1/3}<\infty,
\]
so $f\in C^{1/3}$.

Hence $C^{1/3}$ is complete.
:::
:::
