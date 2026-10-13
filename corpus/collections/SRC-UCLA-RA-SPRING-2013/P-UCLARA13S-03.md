---
schema: qual/card@1
id: P-UCLARA13S-03
kind: problem
title: Circular differentiation from Bourgain's maximal estimate
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
  note: Transcribed from the UCLA Analysis Qualifying Exam Solutions compendium, Spring 2013 section.
---

::: {.problem}
For continuous $f:\mathbb R^2\to\mathbb R$, define
\[
A_r f(x,y)=\frac1{2\pi}\int_{-\pi}^{\pi} f(x+r\cos\theta,y+r\sin\theta)\,d\theta,
\qquad
Mf(x,y)=\sup_{0<r<1} A_r f(x,y).
\]
By a theorem of Bourgain, there is an absolute constant $C$ such that
\[
\|Mf\|_{L^3(\mathbb R^2)}\le C\|f\|_{L^3(\mathbb R^2)}
\]
for all $f\in C_c(\mathbb R^2)$.
Use this to show that if $K\subset\mathbb R^2$ is compact, then
\[
A_r\chi_K(x,y)\longrightarrow 1\qquad(r\to0)
\]
for almost every $(x,y)\in K$.
:::

::: {.solution}
<1>1. Let $S\subset\mathbb R^2$ be bounded and open. Then for every $t>0$,
\[
m^*\bigl(\{x\in\mathbb R^2:M\chi_S(x)>t\}\bigr)
\le
C_0 t^{-3}m(S),
\]
where $C_0$ depends only on the constant in Bourgain's estimate.

<2>1. There exists an increasing sequence
\[
0\le f_k\in C_c(\mathbb R^2),
\qquad
f_k\uparrow\chi_S
\]
pointwise.

::: {.proof}
Since $S$ is bounded and open, define for example
\[
f_k(x)
\coloneqq
\min\{1,k\,\operatorname{dist}(x,S^c)\}.
\]
Then $f_k$ is continuous, vanishes outside $S$, has compact support contained in the compact set $\overline S$, and increases pointwise to $\chi_S$.
:::

<2>2. For every $k$ and $t>0$,
\[
m\bigl(\{Mf_k>t\}\bigr)
\le
C_0t^{-3}m(S).
\]

::: {.proof}
Chebyshev's inequality and Bourgain's estimate give
\[
\begin{aligned}
m(\{Mf_k>t\})
&\le
t^{-3}\|Mf_k\|_3^3\\
&\le
C^3t^{-3}\|f_k\|_3^3.
\end{aligned}
\]
Because $0\le f_k\le\chi_S$,
\[
\|f_k\|_3^3
=
\int_{\mathbb R^2}|f_k|^3
\le
m(S).
\]
Take $C_0=C^3$.
:::

<2>3. One has
\[
Mf_k(x)\uparrow M\chi_S(x)
\qquad
(x\in\mathbb R^2).
\]

::: {.proof}
For every fixed $r\in(0,1)$, monotone convergence on the circle gives
\[
A_rf_k(x)\uparrow A_r\chi_S(x).
\]
Hence
\[
\sup_k Mf_k(x)
\le
M\chi_S(x).
\]
Conversely, if
\[
M\chi_S(x)>s,
\]
choose $r$ with
\[
A_r\chi_S(x)>s.
\]
Then $A_rf_k(x)>s$ for all sufficiently large $k$, so
\[
\sup_k Mf_k(x)\ge s.
\]
Letting $s\uparrow M\chi_S(x)$ proves the equality.
:::

<2>4. Q.E.D.

::: {.proof}
By step <2>3,
\[
\{M\chi_S>t\}
=
\bigcup_{k=1}^{\infty}\{Mf_k>t\}.
\]
The sets on the right increase with $k$, so continuity from below and step <2>2 give
\[
m(\{M\chi_S>t\})
=
\lim_{k\to\infty}m(\{Mf_k>t\})
\le
C_0t^{-3}m(S).
\]
This proves step <1>1.
:::

<1>2. Fix $n\ge1$ and define
\[
E_n
\coloneqq
\left\{
x\in K:
\limsup_{r\downarrow0}
|A_r\chi_K(x)-1|
>
\frac1n
\right\}.
\]
Then
\[
m^*(E_n)=0.
\]

<2>1. For every $\varepsilon>0$, there is a bounded open set $U\supset K$ such that
\[
m(U\setminus K)<\varepsilon.
\]

::: {.proof}
Lebesgue measure is outer regular, so choose an open set $U\supset K$ with
\[
m(U)<m(K)+\varepsilon.
\]
Because $K$ is compact, intersect $U$ with a sufficiently large ball containing $K$ to make it bounded without changing the inclusion. Then
\[
m(U\setminus K)
=
m(U)-m(K)
<
\varepsilon.
\]
:::

<2>2. For every $x\in K$,
\[
\limsup_{r\downarrow0}
|A_r\chi_K(x)-1|
\le
M\chi_{U\setminus K}(x).
\]

::: {.proof}
Fix $x\in K$. Since $U$ is open and contains $x$, there is $r_x>0$ such that
\[
B(x,r_x)\subset U.
\]
Thus for $0<r<r_x$,
\[
A_r\chi_U(x)=1.
\]
Since
\[
\chi_U-\chi_K
=
\chi_{U\setminus K},
\]
one obtains
\[
\begin{aligned}
|A_r\chi_K(x)-1|
&=
|A_r\chi_K(x)-A_r\chi_U(x)|\\
&=
A_r\chi_{U\setminus K}(x)\\
&\le
M\chi_{U\setminus K}(x).
\end{aligned}
\]
Taking the limsup proves the claim.
:::

<2>3. For every $\varepsilon>0$,
\[
m^*(E_n)
\le
C_0n^3\varepsilon.
\]

::: {.proof}
By step <2>2,
\[
E_n
\subset
\left\{
x:
M\chi_{U\setminus K}(x)>\frac1n
\right\}.
\]
The set $U\setminus K$ is open, bounded, and has measure less than $\varepsilon$ by step <2>1. Applying step <1>1 with $t=1/n$ gives
\[
m^*(E_n)
\le
C_0n^3m(U\setminus K)
<
C_0n^3\varepsilon.
\]
:::

<2>4. Q.E.D.

::: {.proof}
The estimate in step <2>3 holds for every $\varepsilon>0$. Letting $\varepsilon\downarrow0$ gives
\[
m^*(E_n)=0.
\]
:::

<1>3. For almost every $x\in K$,
\[
\lim_{r\downarrow0}
A_r\chi_K(x)
=
1.
\]

::: {.proof}
By step <1>2, every $E_n$ has outer measure zero. Hence
\[
E
\coloneqq
\bigcup_{n=1}^{\infty}E_n
\]
has outer measure zero.

If $x\in K\setminus E$, then
\[
\limsup_{r\downarrow0}
|A_r\chi_K(x)-1|
\le
\frac1n
\]
for every $n$. Therefore
\[
\limsup_{r\downarrow0}
|A_r\chi_K(x)-1|
=0,
\]
which is equivalent to
\[
A_r\chi_K(x)\to1.
\]
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 is exactly the desired almost-everywhere circular differentiation statement on $K$.
:::
:::
