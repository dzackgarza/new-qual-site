---
schema: qual/card@1
id: P-RASP08A
kind: problem
title: "True/false on FTC, Urysohn, Baire category, and absolute continuity"
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
  note: Checked against Problem 1 of the official UCSD Spring 2008 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: problem
Determine if the statements below are True or False.

(a) Suppose $f : [0,1] \to \mathbb{C}$ is a continuous function that is differentiable a.e. with respect to Lebesgue measure.
If $f' \in L^1([0,1])$, then
$$
f(1) - f(0) = \int_0^1 f'(x)\,dx.
$$

(b) Given any two points $a \neq b$ in a locally compact Hausdorff space, there is a real-valued continuous function $f$ such that $f(a) \neq f(b)$.

(c) Let $X$ be a Banach space and $\{f_n\}_{n=1}^{\infty}$ a sequence in the dual $X^*$ such that $f_n \neq 0$ for all $n$.
Then the set $\{x \in X : f_n(x) \neq 0, \forall n = 1, 2, \ldots\}$ is dense in $X$.

(d) Let $X$ be a measurable space.
Let $\nu$ be a complex measure on $X$ and $\mu$ a $\sigma$-finite positive measure on $X$.
Suppose that there is a constant $C$ such that for every $f \in L^1(X, d\mu)$,
$$
\left|\int_X f\,d\nu\right| \leq C \left|\int_X f\,d\mu\right|.
$$
Then $d\nu = h\,d\mu$ for some $h \in L^1(X, d\mu)$.
:::


::: solution
<1>1. Part (a) is false.
::: proof
Let $F:[0,1]\to[0,1]$ be the Cantor--Lebesgue function. Then $F$ is continuous, differentiable almost everywhere, and
\[
F'(x)=0
\]
for almost every $x$. Hence $F'\in L^1([0,1])$ and
\[
\int_0^1F'(x)\,dx=0.
\]
But
\[
F(1)-F(0)=1.
\]
Thus the asserted Fundamental Theorem of Calculus identity need not hold without absolute continuity.
:::

<1>2. Part (b) is true.
::: proof
Let $a\ne b$. Since a locally compact Hausdorff space is completely regular, there is a continuous function
\[
f:X\to[0,1]
\]
such that
\[
f(a)=1,
\qquad
f(b)=0.
\]
For completeness, one may choose an open neighborhood $U$ of $a$ with compact closure and $b\notin\overline U$, then use the standard compactly supported Urysohn lemma for locally compact Hausdorff spaces to obtain $f\in C_c(X)$ with $f(a)=1$ and $\operatorname{supp}f\subset U$.
Hence $f(a)\ne f(b)$.
:::

<1>3. Part (c) is true.
::: proof
For each $n$, the kernel
\[
K_n:=\ker f_n
\]
is a proper closed subspace of $X$. A proper linear subspace of a normed space has empty interior, so each complement
\[
U_n:=X\setminus K_n
\]
is open and dense.

Since $X$ is Banach, the Baire Category Theorem gives
\[
\bigcap_{n=1}^\infty U_n
\]
dense in $X$. But this intersection is exactly
\[
\{x\in X:f_n(x)\ne0\text{ for every }n\}.
\]
:::

<1>4. Part (d) is true.
::: proof
First suppose $E,F$ are measurable with
\[
0<\mu(E),\mu(F)<\infty.
\]
The function
\[
g:=\frac{\mathbf1_E}{\mu(E)}-\frac{\mathbf1_F}{\mu(F)}
\]
belongs to $L^1(\mu)$ and satisfies $\int g\,d\mu=0$. The assumed inequality therefore forces
\[
\int g\,d\nu=0,
\]
so
\[
\frac{\nu(E)}{\mu(E)}
=
\frac{\nu(F)}{\mu(F)}.
\]
Thus there is a constant $c\in\mathbb C$ such that
\[
\nu(E)=c\mu(E)
\]
for every measurable $E$ of finite positive $\mu$-measure. Sets of zero $\mu$-measure also have zero $\nu$-measure by applying the hypothesis to their indicators together with a finite-measure set, so the same identity holds for every finite-measure $E$.

Because $\mu$ is sigma-finite, choose $X_k\uparrow X$ with $\mu(X_k)<\infty$. Then
\[
\nu(A\cap X_k)=c\mu(A\cap X_k)
\]
for every measurable $A$. Passing to the limit yields
\[
\nu(A)=c\mu(A)
\]
whenever $\mu(A)<\infty$; if $\mu(X)<\infty$, this already proves $\nu=c\mu$ and $h\equiv c\in L^1(\mu)$.

If $\mu(X)=\infty$, then $c$ must be $0$. Indeed, otherwise along finite-measure sets $X_k$ with $\mu(X_k)\to\infty$ we would have
\[
|\nu(X_k)|=|c|\mu(X_k)\to\infty,
\]
contradicting continuity from below for the finite complex measure $\nu$. Hence $\nu=0$, and we may take $h=0$.

Therefore in all cases
\[
\boxed{d\nu=h\,d\mu\text{ for some }h\in L^1(\mu).}
\]
:::
:::
