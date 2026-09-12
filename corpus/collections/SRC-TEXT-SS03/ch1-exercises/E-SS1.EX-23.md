---
schema: qual/card@1
id: E-SS1.EX-23
kind: problem
title: "SS 1.23: A smooth function whose Taylor series vanishes identically"
classification:
  areas:
  - complex-analysis
  topics: ['Complex Numbers', 'Power Series', 'Cauchy-Riemann']
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: exercise
23. Consider the function $f$ defined on R by

$$
f (x) = \left\{ \begin{array}{c l} 0 & \text {if} x \leq 0, \\ e ^ {- 1 / x ^ {2}} & \text {if} x > 0. \end{array} \right.
$$

Prove that $f$ is indefinitely diferentiable on $\mathbb { R } ,$ and that $f ^ { ( n ) } ( 0 ) = 0$ for all $n \geq 1$ Conclude that $f$ does not have a converging power series expansion $\scriptstyle \sum _ { n = 0 } ^ { \infty } a _ { n } x ^ { n }$ for x near the origin.
:::

::: solution
For $x>0$, set $t=1/x$. We claim that for every $n\ge0$ there is a polynomial $P_n$ such that
\[
f^{(n)}(x)=P_n(1/x)e^{-1/x^2}.
\]
This is clear for $n=0$, with $P_0=1$. If it holds for $n$, differentiation gives
\[
f^{(n+1)}(x)=\left[-x^{-2}P_n'(1/x)+2x^{-3}P_n(1/x)\right]e^{-1/x^2},
\]
which has the same form.

For every integer $m\ge0$,
\[
\lim_{x\downarrow0}x^{-m}e^{-1/x^2}=0.
\]
Indeed, with $t=1/x$, this is $t^m e^{-t^2}\to0$ as $t\to\infty$. Hence for every $n$,
\[
\lim_{x\downarrow0}f^{(n)}(x)=0.
\tag{1}
\]

We now prove inductively that $f$ is $C^\infty$ at $0$ and $f^{(n)}(0)=0$ for every $n\ge0$. For $n=0$, continuity follows from (1). Suppose $f^{(n)}$ has been extended continuously to $0$ with value $0$. Since it vanishes identically on $(-\infty,0]$, its derivative from the left at $0$ is $0$; from the right,
\[
\frac{f^{(n)}(h)-f^{(n)}(0)}{h}
=\frac{P_n(1/h)e^{-1/h^2}}{h}\longrightarrow0
\]
by the same exponential-decay estimate. Thus $f^{(n+1)}(0)=0$, and (1) shows continuity of the next derivative at $0$. Therefore $f\in C^\infty(\mathbb R)$ and all derivatives at $0$ vanish.

If $f$ were represented near $0$ by a convergent power series $\sum_{n\ge0}a_nx^n$, then necessarily
\[
a_n=\frac{f^{(n)}(0)}{n!}=0
\]
for all $n$. The series would therefore be identically zero near $0$, contradicting $f(x)=e^{-1/x^2}>0$ for $x>0$. Hence no convergent power-series expansion about $0$ represents $f$ on any neighborhood of $0$.
:::
