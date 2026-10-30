---
schema: qual/card@1
id: P-BKF81-2
kind: problem
title: Contractive autonomous systems
classification:
  areas:
  - prelim
  topics:
  - Ordinary Differential Equations
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
- event: solution-written
  by: chatgpt
  date: 2026-09-11
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-11
  note: "Integrated DF along the segment between two solutions for contractivity, then differentiated W'=F(W) to obtain exponential velocity decay and convergence."
---

::: {.problem}
Consider $x_i'=F_i(x_1,\dots,x_n)$ with $F:\RR^n\to\RR^n$ of class $C^1$.

(a) If $\langle DF(x)z,z\rangle\le0$ for all $x,z$, show that $\norm{U(t)-V(t)}^2$ is decreasing for any two solutions $U,V$.

(b) If $W(t)$ is a solution for $t>0$ and $\langle DF(x)z,z\rangle\le-\norm{z}^2$, show that $W(t)$ converges to some $C\in\RR^n$ as $t\to\infty$.
:::

::: {.solution}

::: pf

::: {.pf-step #integral-representation}
Express the difference $F(U)-F(V)$ by integrating the derivative of $F$ along a segment.

::: pf-proof
Fix a time at which two solutions $U,V$ are defined, and put
$$
Z=U-V.
$$
For
$$
\Phi(s)=F(V+sZ),
\qquad 0\le s\le1,
$$
the fundamental theorem of calculus gives
$$
F(U)-F(V)
=\int_0^1 DF(V+sZ)Z\,ds.
$$
:::

:::

::: pf-step
Under the hypothesis of part (a), the squared distance between two solutions is nonincreasing.

::: pf-proof
Since
$$
Z'=U'-V'=F(U)-F(V),
$$
step [](#integral-representation){.pf-ref} gives
$$
\begin{aligned}
\frac d{dt}\norm{Z}^2
&=2\langle Z',Z\rangle\\
&=2\int_0^1
\left\langle DF(V+sZ)Z,Z\right\rangle ds.
\end{aligned}
$$
If
$$
\langle DF(x)z,z\rangle\le0
$$
for all $x,z$, every integrand is nonpositive. Hence
$$
\frac d{dt}\norm{U(t)-V(t)}^2\le0.
$$
Thus $\norm{U(t)-V(t)}^2$ is nonincreasing, proving part (a).
:::

:::

::: {.pf-step #velocity-decay}
Under the stronger hypothesis, the velocity of a solution decays exponentially.

::: pf-proof
Assume now
$$
\langle DF(x)z,z\rangle\le-\norm{z}^2.
$$
Because $F$ is $C^1$ and $W'=F(W)$, the solution $W$ is $C^2$ and
$$
W''(t)=DF(W(t))W'(t).
$$
Therefore
$$
\begin{aligned}
\frac d{dt}\norm{W'(t)}^2
&=2\langle W''(t),W'(t)\rangle\\
&=2\left\langle DF(W(t))W'(t),W'(t)\right\rangle\\
&\le-2\norm{W'(t)}^2.
\end{aligned}
$$
Fix $t_0>0$. Multiplying by $e^{2t}$, or integrating this differential
inequality, gives
$$
\norm{W'(t)}^2
\le e^{-2(t-t_0)}\norm{W'(t_0)}^2
$$
for every $t\ge t_0$. Hence
$$
\norm{W'(t)}
\le e^{-(t-t_0)}\norm{W'(t_0)}.
$$
:::

:::

::: pf-step
The trajectory is Cauchy and therefore converges.

::: pf-proof
If $s>t\ge t_0$, then step [](#velocity-decay){.pf-ref} yields
$$
\begin{aligned}
\norm{W(s)-W(t)}
&\le\int_t^s\norm{W'(r)}\,dr\\
&\le\norm{W'(t_0)}\int_t^s e^{-(r-t_0)}\,dr\\
&\le\norm{W'(t_0)}e^{-(t-t_0)}.
\end{aligned}
$$
The final expression tends to $0$ as $t\to\infty$, independently of
$s>t$. Thus $W(t)$ is a Cauchy trajectory at infinity. Since
$\RR^n$ is complete, there is some
$$
C\in\RR^n
$$
such that
$$
\boxed{W(t)\longrightarrow C\qquad(t\to\infty).}
$$
:::

:::

:::
:::
