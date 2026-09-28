---
schema: qual/card@1
id: P-BERK86S-07
kind: problem
title: Solve two exponential-kernel integral equations
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-22
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-22
  note: >-
    Factored out e^x. The Volterra equation becomes
    u=1+lambda integral_0^x u and hence u'=lambda u; the Fredholm equation
    reduces to one scalar consistency equation (1-lambda)C=1.
---

::: {.problem}
For a real parameter $\lambda$, find all solutions on $0\le x\le1$ of
\[
\varphi(x)=e^x+\lambda\int_0^x e^{x-y}\varphi(y)\,dy
\]
and
\[
\psi(x)=e^x+\lambda\int_0^1 e^{x-y}\psi(y)\,dy.
\]
:::

::: {.solution}
<1>1. The first integral equation is equivalent, after setting
$$
u(x)\coloneqq e^{-x}\varphi(x),
$$
to
$$
u(x)=1+\lambda\int_0^x u(y)\,dy.
$$

::: {.proof}
Factor $e^x$ from the kernel:
$$
\begin{aligned}
\varphi(x)
&=
e^x+\lambda e^x\int_0^x e^{-y}\varphi(y)\,dy.
\end{aligned}
$$
Divide by $e^x$ and use the definition of $u$.
:::

<1>2. The first equation has exactly one solution, namely
$$
\boxed{\varphi(x)=e^{(1+\lambda)x}}.
$$

::: {.proof}
Any solution of step <1>1 is continuous, since its right-hand side is an
indefinite integral plus a constant. The fundamental theorem of calculus
therefore gives
$$
u'(x)=\lambda u(x),
\qquad
u(0)=1.
$$
The unique solution of this initial-value problem is
$$
u(x)=e^{\lambda x}.
$$
Thus
$$
\varphi(x)=e^xu(x)=e^{(1+\lambda)x}.
$$
Conversely, direct substitution verifies that this function satisfies the
original integral equation, so there are no additional solutions.
:::

<1>3. For a solution of the second equation, define
$$
C\coloneqq\int_0^1 e^{-y}\psi(y)\,dy.
$$
Then necessarily
$$
\psi(x)=e^x(1+\lambda C).
$$

::: {.proof}
The integral in the second equation is over the fixed interval $[0,1]$,
so
$$
\int_0^1e^{x-y}\psi(y)\,dy
=
e^x
\int_0^1e^{-y}\psi(y)\,dy
=
e^xC.
$$
Substitution gives the displayed formula.
:::

<1>4. The scalar $C$ from step <1>3 must satisfy
$$
(1-\lambda)C=1.
$$

::: {.proof}
Insert the formula from step <1>3 into the definition of $C$:
$$
\begin{aligned}
C
&=
\int_0^1
e^{-y}e^y(1+\lambda C)\,dy\\
&=
\int_0^1(1+\lambda C)\,dy\\
&=
1+\lambda C.
\end{aligned}
$$
Rearranging yields the claim.
:::

<1>5. If $\lambda\neq1$, the second equation has exactly one solution:
$$
\boxed{\psi(x)=\frac{e^x}{1-\lambda}}.
$$

::: {.proof}
Step <1>4 gives
$$
C=\frac1{1-\lambda}.
$$
Then step <1>3 gives
$$
\psi(x)
=
e^x
\left(
1+\frac{\lambda}{1-\lambda}
\right)
=
\frac{e^x}{1-\lambda}.
$$
The scalar equation determines $C$ uniquely, so no other solution is
possible. Direct substitution verifies the displayed function.
:::

<1>6. If $\lambda=1$, the second equation has no solution.

::: {.proof}
For $\lambda=1$, step <1>4 becomes
$$
0\cdot C=1,
$$
which is impossible.
:::

<1>7. Hence all solutions are
$$
\boxed{
\varphi(x)=e^{(1+\lambda)x}
\quad\text{for every }\lambda\in\RR,
}
$$
and
$$
\boxed{
\psi(x)=
\begin{cases}
\dfrac{e^x}{1-\lambda},&\lambda\neq1,\\
\text{no solution},&\lambda=1.
\end{cases}
}
$$

::: {.proof}
Combine steps <1>2, <1>5, and <1>6.
:::

<1>8. Q.E.D.

::: {.proof}
Step <1>7 is the complete solution set for both equations.
:::
:::
