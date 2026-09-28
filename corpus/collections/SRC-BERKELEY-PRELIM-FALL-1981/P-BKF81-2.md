---
schema: qual/card@1
id: P-BKF81-2
kind: problem
title: Contractive autonomous systems
classification:
  areas:
  - prelim
  topics:
  - Calculus
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
Consider $x_i'=F_i(x_1,\dots,x_n)$ with $F:\mathbb R^n\to\mathbb R^n$ of class $C^1$.

(a) If $\langle DF(x)z,z\rangle\le0$ for all $x,z$, show that $\|U(t)-V(t)\|^2$ is decreasing for any two solutions $U,V$.

(b) If $W(t)$ is a solution for $t>0$ and $\langle DF(x)z,z\rangle\le-\|z\|^2$, show that $W(t)$ converges to some $C\in\mathbb R^n$ as $t\to\infty$.
:::

::: {.solution}
<1>1. Express the difference $F(U)-F(V)$ by integrating the derivative of $F$ along a segment.
::: {.proof}
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

<1>2. Under the hypothesis of part (a), the squared distance between two solutions is nonincreasing.
::: {.proof}
Since
$$
Z'=U'-V'=F(U)-F(V),
$$
step <1>1 gives
$$
\begin{aligned}
\frac d{dt}\|Z\|^2
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
\frac d{dt}\|U(t)-V(t)\|^2\le0.
$$
Thus $\|U(t)-V(t)\|^2$ is nonincreasing, proving part (a).
:::

<1>3. Under the stronger hypothesis, the velocity of a solution decays exponentially.
::: {.proof}
Assume now
$$
\langle DF(x)z,z\rangle\le-\|z\|^2.
$$
Because $F$ is $C^1$ and $W'=F(W)$, the solution $W$ is $C^2$ and
$$
W''(t)=DF(W(t))W'(t).
$$
Therefore
$$
\begin{aligned}
\frac d{dt}\|W'(t)\|^2
&=2\langle W''(t),W'(t)\rangle\\
&=2\left\langle DF(W(t))W'(t),W'(t)\right\rangle\\
&\le-2\|W'(t)\|^2.
\end{aligned}
$$
Fix $t_0>0$. Multiplying by $e^{2t}$, or integrating this differential
inequality, gives
$$
\|W'(t)\|^2
\le e^{-2(t-t_0)}\|W'(t_0)\|^2
$$
for every $t\ge t_0$. Hence
$$
\|W'(t)\|
\le e^{-(t-t_0)}\|W'(t_0)\|.
$$
:::

<1>4. The trajectory is Cauchy and therefore converges.
::: {.proof}
If $s>t\ge t_0$, then step <1>3 yields
$$
\begin{aligned}
\|W(s)-W(t)\|
&\le\int_t^s\|W'(r)\|\,dr\\
&\le\|W'(t_0)\|\int_t^s e^{-(r-t_0)}\,dr\\
&\le\|W'(t_0)\|e^{-(t-t_0)}.
\end{aligned}
$$
The final expression tends to $0$ as $t\to\infty$, independently of
$s>t$. Thus $W(t)$ is a Cauchy trajectory at infinity. Since
$\mathbb R^n$ is complete, there is some
$$
C\in\mathbb R^n
$$
such that
$$
\boxed{W(t)\longrightarrow C\qquad(t\to\infty).}
$$
:::
:::
