---
schema: qual/card@1
id: P-UCLAB02W-05
kind: problem
title: Differentiability and the multivariable chain rule
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 5 of the official UCLA Basic Examination, Winter 2002 PDF.
---

::: {.problem}
(a) Let $U\subset\RR^n$ be open and $f:U\to\RR^k$.
Define what it means for $f$ to be differentiable at a point $x\in U$.

(b) State carefully the Chain Rule for a composition of differentiable functions of several variables.

(c) Prove the Chain Rule you stated in part (b).
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

A function $f:U\to\RR^k$ is differentiable at $x\in U$ if there exists a linear map
$$
A:\RR^n\to\RR^k
$$
such that
$$
\lim_{h\to0}
\frac{\norm{f(x+h)-f(x)-Ah}}{\norm{h}}=0,
$$
where $h$ is restricted so that $x+h\in U$. The map $A$, when it exists, is denoted $Df(x)$.


::: pf-proof

This is the definition of differentiability in finite-dimensional Euclidean spaces. Equivalently, there is a remainder $r_f(h)$ satisfying
$$
f(x+h)=f(x)+Df(x)h+r_f(h),
\qquad
\frac{\norm{r_f(h)}}{\norm{h}}\longrightarrow0.
$$

:::

:::

::: {.pf-step #s1-2}

The multivariable Chain Rule is the following statement. Let $U\subset\RR^n$ and $V\subset\RR^k$ be open, let
$$
f:U\to V,
\qquad
g:V\to\RR^m,
$$
and let $x\in U$. If $f$ is differentiable at $x$ and $g$ is differentiable at $f(x)$, then $g\circ f$ is differentiable at $x$ and
$$
\boxed{D(g\circ f)(x)=Dg(f(x))\circ Df(x)}.
$$


::: pf-proof

This is the precise chain-rule statement to be proved in the remaining steps.

:::

:::

::: {.pf-step #s1-3}

Put
$$
A=Df(x),
\qquad
B=Dg(f(x)).
$$
Then there are remainders $r_f$ and $r_g$ such that
$$
f(x+h)-f(x)=Ah+r_f(h),
\qquad
\frac{\norm{r_f(h)}}{\norm{h}}\to0,
$$
and
$$
g(f(x)+u)-g(f(x))=Bu+r_g(u),
\qquad
\frac{\norm{r_g(u)}}{\norm u}\to0.
$$


::: pf-proof

These are exactly the differentiability expansions from step [](#s1-1){.pf-ref}, first for $f$ at $x$ and then for $g$ at $f(x)$.

:::

:::

::: {.pf-step #s1-4}

There are constants $C>0$ and $\delta>0$ such that, whenever $0<\norm{h}<\delta$,
$$
\norm{f(x+h)-f(x)}\le C\norm{h}.
$$


::: pf-proof

By step [](#s1-3){.pf-ref},
$$
\frac{\norm{r_f(h)}}{\norm{h}}\to0.
$$
Hence, for sufficiently small nonzero $h$,
$$
\norm{r_f(h)}\le\norm{h}.
$$
Therefore
$$
\norm{f(x+h)-f(x)}
\le
\norm{Ah}+\norm{r_f(h)}
\le
(\norm{A}+1)\norm{h}.
$$
Take $C=\norm{A}+1$.

:::

:::

::: {.pf-step #s1-5}

For sufficiently small $h$, if
$$
u_h=f(x+h)-f(x),
$$
then
$$
(g\circ f)(x+h)-(g\circ f)(x)-BAh
=Br_f(h)+r_g(u_h).
$$


::: pf-proof

By step [](#s1-3){.pf-ref},
$$
u_h=Ah+r_f(h).
$$
Using the differentiability expansion for $g$ at $f(x)$,
$$
\begin{aligned}
(g\circ f)(x+h)-(g\circ f)(x)
&=g(f(x)+u_h)-g(f(x))\\
&=Bu_h+r_g(u_h)\\
&=BAh+Br_f(h)+r_g(u_h).
\end{aligned}
$$
Rearranging gives the identity.

:::

:::

::: {.pf-step #s1-6}

The remainder in step [](#s1-5){.pf-ref} is $o(\norm{h})$:
$$
\frac{\norm{Br_f(h)+r_g(u_h)}}{\norm{h}}\longrightarrow0.
$$


::: pf-proof

For the first term,
$$
\frac{\norm{Br_f(h)}}{\norm{h}}
\le
\norm{B}\frac{\norm{r_f(h)}}{\norm{h}}
\longrightarrow0
$$
by step [](#s1-3){.pf-ref}.

For the second term, if $u_h\ne0$, then step [](#s1-4){.pf-ref} gives
$$
\frac{\norm{r_g(u_h)}}{\norm{h}}
=
\frac{\norm{r_g(u_h)}}{\norm{u_h}}
\frac{\norm{u_h}}{\norm{h}}
\le
C\frac{\norm{r_g(u_h)}}{\norm{u_h}}.
$$
As $h\to0$, step [](#s1-4){.pf-ref} implies $u_h\to0$, so the last factor tends to $0$ by step [](#s1-3){.pf-ref}. If $u_h=0$, then $r_g(u_h)=r_g(0)=0$. Hence the second term also tends to $0$ after division by $\norm{h}$.

:::

:::

::: {.pf-step #s1-7}

The composition $g\circ f$ is differentiable at $x$ with derivative $B\circ A$.


::: pf-proof

By steps [](#s1-5){.pf-ref} through [](#s1-6){.pf-ref},
$$
(g\circ f)(x+h)
=(g\circ f)(x)+BAh+o(\norm{h}).
$$
Since $BA:\RR^n\to\RR^m$ is linear, step [](#s1-1){.pf-ref} identifies it as the derivative of $g\circ f$ at $x$.

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} answers part (a), step [](#s1-2){.pf-ref} answers part (b), and step [](#s1-7){.pf-ref} proves the Chain Rule required in part (c).

:::

:::

:::
