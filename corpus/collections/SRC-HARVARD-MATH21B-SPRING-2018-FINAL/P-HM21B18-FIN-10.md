---
schema: qual/card@1
id: P-HM21B18-FIN-10
kind: problem
title: Six elementary ordinary differential equations
classification: {areas: [applied-algebra], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
---

::: {.problem}
Find the general solution to each differential equation:

1. $f'(t)=1/(t+1)$;
2. $f''(t)=e^t+t$;
3. $f''(t)+f(t)=t+2$;
4. $f''(t)-2f'(t)+f(t)=e^t$;
5. $f''(t)-f(t)=e^t+\sin t$;
6. $f''(t)-f(t)=e^{-3t}$.
:::

::: {.solution}
In the formulas below, the constants are arbitrary real numbers and may
differ from one equation to another.

<1>1. The general solution of $f'(t)=1/(t+1)$ is
\[
f(t)=\log|t+1|+C
\]
on any interval not containing $t=-1$.

::: {.proof}
On such an interval,
\[
\frac{d}{dt}\log|t+1|=\frac1{t+1}.
\]
All antiderivatives differ by an additive constant.
:::

<1>2. The general solution of $f''(t)=e^t+t$ is
\[
f(t)=e^t+\frac{t^3}{6}+C_1t+C_2.
\]

::: {.proof}
Integrating once gives
\[
f'(t)=e^t+\frac{t^2}{2}+C_1,
\]
and integrating again gives the displayed formula.
:::

<1>3. The general solution of $f''+f=t+2$ is
\[
f(t)=C_1\cos t+C_2\sin t+t+2.
\]

::: {.proof}
The homogeneous equation has characteristic polynomial $r^2+1$, so its
real solution space is spanned by $\cos t$ and $\sin t$. The function
$f_p=t+2$ satisfies $f_p''+f_p=t+2$. Adding the homogeneous and
particular solutions gives the formula.
:::

<1>4. The general solution of
$f''-2f'+f=e^t$ is
\[
f(t)=e^t\left(C_1+C_2t+\frac{t^2}{2}\right).
\]

::: {.proof}
The operator on the left is $(D-1)^2$. Write $f=e^tg$. Then
\[
(D-1)(e^tg)=e^tg',
\qquad
(D-1)^2(e^tg)=e^tg''.
\]
Thus the equation reduces to $g''=1$, whose general solution is
$g=C_1+C_2t+t^2/2$.
:::

<1>5. The general solution of
$f''-f=e^t+\sin t$ is
\[
f(t)=C_1e^t+C_2e^{-t}
+\frac12te^t-\frac12\sin t.
\]

::: {.proof}
The homogeneous equation has solutions $e^t,e^{-t}$. For
$f_{p,1}=\frac12te^t$,
\[
f_{p,1}''-f_{p,1}=e^t.
\]
For $f_{p,2}=-\frac12\sin t$,
\[
f_{p,2}''-f_{p,2}=\sin t.
\]
Their sum is therefore a particular solution, and adding the homogeneous
solution gives the formula.
:::

<1>6. The general solution of
$f''-f=e^{-3t}$ is
\[
f(t)=C_1e^t+C_2e^{-t}+\frac18e^{-3t}.
\]

::: {.proof}
The homogeneous solutions are again $e^t,e^{-t}$. For a particular
solution $f_p=Ae^{-3t}$,
\[
f_p''-f_p=(9A-A)e^{-3t}=8Ae^{-3t}.
\]
Hence $A=1/8$, proving the displayed formula.
:::

<1>7. Collecting the six answers,
\[
\boxed{
\begin{aligned}
1.\;&\log|t+1|+C,\\
2.\;&e^t+\frac{t^3}{6}+C_1t+C_2,\\
3.\;&C_1\cos t+C_2\sin t+t+2,\\
4.\;&e^t\left(C_1+C_2t+\frac{t^2}{2}\right),\\
5.\;&C_1e^t+C_2e^{-t}+\frac12te^t-\frac12\sin t,\\
6.\;&C_1e^t+C_2e^{-t}+\frac18e^{-3t}.
\end{aligned}}
\]

::: {.proof}
These are exactly the solutions established in steps <1>1 through <1>6.
:::

<1>8. Q.E.D.

::: {.proof}
Step <1>7 records the general solution of every requested equation.
:::
:::
