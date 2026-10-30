---
schema: qual/card@1
id: P-UCLARA13S-03
kind: problem
title: Circular differentiation from Bourgain's maximal estimate
classification:
  areas:
  - real-analysis
  topics:
  - Maximal Functions
  - Differentiation
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Transcribed from the UCLA Analysis Qualifying Exam Solutions compendium, Spring 2013 section.
---

::: {.problem}
For continuous $f:\RR^2\to\RR$, define
$$
A_r f(x,y)=\frac1{2\pi}\int_{-\pi}^{\pi} f(x+r\cos\theta,y+r\sin\theta)\,d\theta,
\qquad
Mf(x,y)=\sup_{0<r<1} A_r f(x,y).
$$
By a theorem of Bourgain, there is an absolute constant $C$ such that
$$
\norm{Mf}_{L^3(\RR^2)}\le C\norm{f}_{L^3(\RR^2)}
$$
for all $f\in C_c(\RR^2)$.
Use this to show that if $K\subset\RR^2$ is compact, then
$$
A_r\chi_K(x,y)\longrightarrow 1\qquad(r\to0)
$$
for almost every $(x,y)\in K$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Let $S\subset\RR^2$ be bounded and open. Then for every $t>0$,
$$
m^*\bigl(\{x\in\RR^2:M\chi_S(x)>t\}\bigr)
\le
C_0 t^{-3}m(S),
$$
where $C_0$ depends only on the constant in Bourgain's estimate.


::: pf-proof

::: pf-step

There exists an increasing sequence
$$
0\le f_k\in C_c(\RR^2),
\qquad
f_k\uparrow\chi_S
$$
pointwise.


::: pf-proof

Since $S$ is bounded and open, define for example
$$
f_k(x)
\coloneqq
\min\{1,k\,\operatorname{dist}(x,S^c)\}.
$$
Then $f_k$ is continuous, vanishes outside $S$, has compact support contained in the compact set $\overline S$, and increases pointwise to $\chi_S$.

:::

:::

::: {.pf-step #s1-2}

For every $k$ and $t>0$,
$$
m\bigl(\{Mf_k>t\}\bigr)
\le
C_0t^{-3}m(S).
$$


::: pf-proof

Chebyshev's inequality and Bourgain's estimate give
$$
\begin{aligned}
m(\{Mf_k>t\})
&\le
t^{-3}\norm{Mf_k}_3^3\\
&\le
C^3t^{-3}\norm{f_k}_3^3.
\end{aligned}
$$
Because $0\le f_k\le\chi_S$,
$$
\norm{f_k}_3^3
=
\int_{\RR^2}\abs{f_k}^3
\le
m(S).
$$
Take $C_0=C^3$.

:::

:::

::: {.pf-step #s1-3}

One has
$$
Mf_k(x)\uparrow M\chi_S(x)
\qquad
(x\in\RR^2).
$$


::: pf-proof

For every fixed $r\in(0,1)$, monotone convergence on the circle gives
$$
A_rf_k(x)\uparrow A_r\chi_S(x).
$$
Hence
$$
\sup_k Mf_k(x)
\le
M\chi_S(x).
$$
Conversely, if
$$
M\chi_S(x)>s,
$$
choose $r$ with
$$
A_r\chi_S(x)>s.
$$
Then $A_rf_k(x)>s$ for all sufficiently large $k$, so
$$
\sup_k Mf_k(x)\ge s.
$$
Letting $s\uparrow M\chi_S(x)$ proves the equality.

:::

:::

::: pf-qed

By step [](#s1-3){.pf-ref},
$$
\{M\chi_S>t\}
=
\bigcup_{k=1}^{\infty}\{Mf_k>t\}.
$$
The sets on the right increase with $k$, so continuity from below and step [](#s1-2){.pf-ref} give
$$
m(\{M\chi_S>t\})
=
\lim_{k\to\infty}m(\{Mf_k>t\})
\le
C_0t^{-3}m(S).
$$
This proves step [](#s1){.pf-ref}.

:::

:::

:::

::: {.pf-step #s2}

Fix $n\ge1$ and define
$$
E_n
\coloneqq
\left\{
x\in K:
\limsup_{r\downarrow0}
\abs{A_r\chi_K(x)-1}
>
\frac1n
\right\}.
$$
Then
$$
m^*(E_n)=0.
$$


::: pf-proof

::: {.pf-step #s2-1}

For every $\varepsilon>0$, there is a bounded open set $U\supset K$ such that
$$
m(U\setminus K)<\varepsilon.
$$


::: pf-proof

Lebesgue measure is outer regular, so choose an open set $U\supset K$ with
$$
m(U)<m(K)+\varepsilon.
$$
Because $K$ is compact, intersect $U$ with a sufficiently large ball containing $K$ to make it bounded without changing the inclusion. Then
$$
m(U\setminus K)
=
m(U)-m(K)
<
\varepsilon.
$$

:::

:::

::: {.pf-step #s2-2}

For every $x\in K$,
$$
\limsup_{r\downarrow0}
\abs{A_r\chi_K(x)-1}
\le
M\chi_{U\setminus K}(x).
$$


::: pf-proof

Fix $x\in K$. Since $U$ is open and contains $x$, there is $r_x>0$ such that
$$
B(x,r_x)\subset U.
$$
Thus for $0<r<r_x$,
$$
A_r\chi_U(x)=1.
$$
Since
$$
\chi_U-\chi_K
=
\chi_{U\setminus K},
$$
one obtains
$$
\begin{aligned}
\abs{A_r\chi_K(x)-1}
&=
\abs{A_r\chi_K(x)-A_r\chi_U(x)}\\
&=
A_r\chi_{U\setminus K}(x)\\
&\le
M\chi_{U\setminus K}(x).
\end{aligned}
$$
Taking the limsup proves the claim.

:::

:::

::: {.pf-step #s2-3}

For every $\varepsilon>0$,
$$
m^*(E_n)
\le
C_0n^3\varepsilon.
$$


::: pf-proof

By step [](#s2-2){.pf-ref},
$$
E_n
\subset
\left\{
x:
M\chi_{U\setminus K}(x)>\frac1n
\right\}.
$$
The set $U\setminus K$ is open, bounded, and has measure less than $\varepsilon$ by step [](#s2-1){.pf-ref}. Applying step [](#s1){.pf-ref} with $t=1/n$ gives
$$
m^*(E_n)
\le
C_0n^3m(U\setminus K)
<
C_0n^3\varepsilon.
$$

:::

:::

::: pf-qed

The estimate in step [](#s2-3){.pf-ref} holds for every $\varepsilon>0$. Letting $\varepsilon\downarrow0$ gives
$$
m^*(E_n)=0.
$$

:::

:::

:::

::: {.pf-step #s3}

For almost every $x\in K$,
$$
\lim_{r\downarrow0}
A_r\chi_K(x)
=
1.
$$


::: pf-proof

By step [](#s2){.pf-ref}, every $E_n$ has outer measure zero. Hence
$$
E
\coloneqq
\bigcup_{n=1}^{\infty}E_n
$$
has outer measure zero.

If $x\in K\setminus E$, then
$$
\limsup_{r\downarrow0}
\abs{A_r\chi_K(x)-1}
\le
\frac1n
$$
for every $n$. Therefore
$$
\limsup_{r\downarrow0}
\abs{A_r\chi_K(x)-1}
=0,
$$
which is equivalent to
$$
A_r\chi_K(x)\to1.
$$

:::

:::

::: pf-qed

Step [](#s3){.pf-ref} is exactly the desired almost-everywhere circular differentiation statement on $K$.

:::

:::

:::
