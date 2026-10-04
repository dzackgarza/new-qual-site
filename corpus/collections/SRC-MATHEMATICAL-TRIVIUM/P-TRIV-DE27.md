---
schema: qual/card@1
id: P-TRIV-DE27
kind: problem
title: Self-adjoint forms of the Laguerre, Hermite and Chebyshev equations
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Differential Equations, Problem 27, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Given the eigenvalue problem ${ \mathcal { L } } ( x ) \psi ( x ) = \lambda \psi ( x )$ with ${ \mathcal L } ( x ) = p _ { 0 } ( x ) \frac { d ^ { 2 } } { d x ^ { 2 } } +$ $p _ { 1 } ( x ) \frac { d } { d x } + p _ { 2 } ( x )$ ,  is self-adjoint if $p _ { 0 } ^ { \prime } = p _ { 1 }$ . Find a function $f ( x )$ such that, by multiplying the following ODE, it makes them self adjoint:

(a) Laguerre’s ODE: $x y ^ { \prime \prime } + ( 1 - x ) y ^ { \prime } + a y = 0$

(b) Hermite’s ODE: $y ^ { \prime \prime } - 2 x y ^ { \prime } + 2 \alpha y = 0$

(c) Chabyshev’s ODE: $( 1 - x ^ { 2 } ) y ^ { \prime \prime } - x y ^ { \prime } + n ^ { 2 } y = 0$
:::

::: {.solution}
For an equation
\[
p_0y''+p_1y'+p_2y=0,
\]
seek a nonzero multiplier $f$ for which the multiplied equation satisfies $(fp_0)'=fp_1$.

<1>1. The multiplier must satisfy
\[
\frac{f'}f=\frac{p_1-p_0'}{p_0}.
\]

::: {.proof}
The self-adjointness condition for the multiplied equation is
\[
(fp_0)'=fp_1.
\]
Expanding the derivative gives $f'p_0+fp_0'=fp_1$. Dividing by $fp_0$ gives the displayed first-order equation for $f$.
:::

<1>2. For Laguerre's equation, one may take
\[
\boxed{f(x)=e^{-x}}.
\]

::: {.proof}
Here $p_0=x$ and $p_1=1-x$, so step <1>1 gives
\[
\frac{f'}f=\frac{(1-x)-1}{x}=-1.
\]
Thus $f=Ce^{-x}$, and the irrelevant nonzero constant may be chosen as $1$. Indeed, the multiplied differential terms are
\[
xe^{-x}y''+(1-x)e^{-x}y'=(xe^{-x}y')'.
\]
:::

<1>3. For Hermite's equation, one may take
\[
\boxed{f(x)=e^{-x^2}}.
\]

::: {.proof}
Here $p_0=1$ and $p_1=-2x$, so step <1>1 gives $f'/f=-2x$. Hence $f=Ce^{-x^2}$, and
\[
e^{-x^2}y''-2xe^{-x^2}y'=(e^{-x^2}y')'.
\]
:::

<1>4. For Chebyshev's equation, one may take
\[
\boxed{f(x)=\frac1{\sqrt{1-x^2}}}
\]
on $|x|<1$.

::: {.proof}
Here $p_0=1-x^2$ and $p_1=-x$, so
\[
\frac{f'}f=\frac{-x-(-2x)}{1-x^2}=\frac{x}{1-x^2}.
\]
Integration gives
\[
\log f=-\frac12\log(1-x^2)+C,
\]
hence the displayed multiplier. Then
\[
fp_0=\sqrt{1-x^2},
\qquad
(fp_0)'=-\frac{x}{\sqrt{1-x^2}}=fp_1.
\]
:::

<1>5. Q.E.D.

::: {.proof}
Steps <1>2--<1>4 give multipliers satisfying the self-adjointness condition in all three cases.
:::
:::
