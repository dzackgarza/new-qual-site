---
schema: qual/card@1
id: P-UCLAB10F-10
kind: problem
title: Euler polygonal approximations for a Lipschitz ODE
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 10 of the retained UCLA Basic Examination, Fall 2010.
---

::: {.problem}
Suppose $f:\RR\to\RR$ is bounded and Lipschitz continuous.
For $k\in\NN$, define $x_k:[0,1]\to\RR$ by $x_k(0)=0$ and
$$
x_k(t)=x_k(n2^{-k})+(t-n2^{-k})f(x_k(n2^{-k}))
$$
whenever
$$
n2^{-k}<t\le(n+1)2^{-k},\qquad n\in\NN.
$$
Explain why $x_k$ converges uniformly, as $k\to\infty$, to a solution $x:[0,1]\to\RR$ of
$$
x'(t)=f(x(t)),\qquad x(0)=0.
$$
:::

::: {.solution}

Let
$$
h_k=2^{-k}.
$$
Assume
$$
\abs{f(x)}\le M
$$
for all $x\in\RR$, and let $L$ be a Lipschitz constant:
$$
\abs{f(x)-f(y)}\le L\abs{x-y}.
$$

::: pf

::: {.pf-step #s1-1}

Each Euler polygon $x_k$ is $M$-Lipschitz on $[0,1]$.


::: pf-proof

On every mesh interval
$$
[nh_k,(n+1)h_k],
$$
the function $x_k$ is affine with slope
$$
f(x_k(nh_k)).
$$
Its absolute value is at most $M$. Thus on each mesh interval,
$$
\abs{x_k(t)-x_k(s)}\le M\abs{t-s}.
$$
For arbitrary $s<t$, partition $[s,t]$ at the mesh points it crosses and add these estimates. The result is
$$
\abs{x_k(t)-x_k(s)}\le M\abs{t-s}.
$$

:::

:::

::: {.pf-step #s1-2}

The family $(x_k)$ is uniformly bounded on $[0,1]$:
$$
\abs{x_k(t)}\le M
$$
for every $k$ and $t\in[0,1]$.


::: pf-proof

Since
$$
x_k(0)=0,
$$
step [](#s1-1){.pf-ref} gives
$$
\abs{x_k(t)}
=
\abs{x_k(t)-x_k(0)}
\le
Mt
\le
M.
$$

:::

:::

::: {.pf-step #s1-3}

There is a subsequence $(x_{k_j})$ converging uniformly on $[0,1]$ to a continuous function $x$.


::: pf-proof

By step [](#s1-1){.pf-ref}, the family is equicontinuous, and by step [](#s1-2){.pf-ref} it is uniformly bounded. The Arzelà--Ascoli theorem on the compact interval $[0,1]$ therefore gives a uniformly convergent subsequence.

:::

:::

::: {.pf-step #s1-4}

For each $k$, define the left-mesh projection
$$
\tau_k(t)=h_k\left\lfloor\frac{t}{h_k}\right\rfloor
$$
for $0\le t<1$, and set $\tau_k(1)=1-h_k$.
Then
$$
0\le t-\tau_k(t)\le h_k.
$$


::: pf-proof

By construction, $\tau_k(t)$ is the left endpoint of the mesh interval containing $t$, except at $t=1$ where the chosen value is the left endpoint of the last interval. Hence the distance from $t$ to $\tau_k(t)$ is at most one mesh width.

:::

:::

::: {.pf-step #s1-5}

For every $k$ and $t\in[0,1]$,
$$
x_k(t)
=
\int_0^t f(x_k(\tau_k(s)))\,ds.
$$


::: pf-proof

On a mesh interval
$$
(nh_k,(n+1)h_k),
$$
the derivative of $x_k$ exists and equals
$$
x_k'(s)=f(x_k(nh_k))
=
f(x_k(\tau_k(s))).
$$
Thus the displayed equality follows by integrating the piecewise constant derivative from $0$ to $t$, using $x_k(0)=0$. The finitely many mesh points do not affect the integral.

:::

:::

::: {.pf-step #s1-6}

One has
$$
\sup_{0\le s\le1}
\abs{x_k(\tau_k(s))-x_k(s)}
\le
Mh_k.
$$


::: pf-proof

By step [](#s1-1){.pf-ref} and step [](#s1-4){.pf-ref},
$$
\abs{x_k(\tau_k(s))-x_k(s)}
\le
M\abs{\tau_k(s)-s}
\le
Mh_k.
$$
Taking the supremum gives the claim.

:::

:::

::: {.pf-step #s1-7}

Along the uniformly convergent subsequence from step [](#s1-3){.pf-ref},
$$
f(x_{k_j}(\tau_{k_j}(s)))
\longrightarrow
f(x(s))
$$
uniformly in $s\in[0,1]$.


::: pf-proof

By the Lipschitz property of $f$,
$$
\begin{aligned}
\abs{f(x_{k_j}(\tau_{k_j}(s)))-f(x(s))}
&\le
L\abs{x_{k_j}(\tau_{k_j}(s))-x(s)}\\
&\le
L\abs{x_{k_j}(\tau_{k_j}(s))-x_{k_j}(s)}
+
L\abs{x_{k_j}(s)-x(s)}.
\end{aligned}
$$
The first term is at most
$$
LMh_{k_j}\to0
$$
by step [](#s1-6){.pf-ref}, and the second tends uniformly to zero by step [](#s1-3){.pf-ref}. Hence the convergence is uniform.

:::

:::

::: {.pf-step #s1-8}

The subsequential limit satisfies
$$
x(t)=\int_0^t f(x(s))\,ds
$$
for every $t\in[0,1]$.


::: pf-proof

Take the identity in step [](#s1-5){.pf-ref} along the subsequence $k_j$. The left side converges uniformly to $x(t)$ by step [](#s1-3){.pf-ref}. By step [](#s1-7){.pf-ref}, the integrands converge uniformly, so
$$
\int_0^t f(x_{k_j}(\tau_{k_j}(s)))\,ds
\longrightarrow
\int_0^t f(x(s))\,ds.
$$
Passing to the limit gives the displayed integral equation.

:::

:::

::: {.pf-step #s1-9}

The function $x$ is continuously differentiable and solves
$$
x'(t)=f(x(t)),
\qquad
x(0)=0.
$$


::: pf-proof

The function $x$ is continuous by step [](#s1-3){.pf-ref}, and $f$ is continuous because it is Lipschitz. Therefore
$$
s\mapsto f(x(s))
$$
is continuous. By step [](#s1-8){.pf-ref} and the fundamental theorem of calculus,
$$
x'(t)=f(x(t)).
$$
Also step [](#s1-8){.pf-ref} at $t=0$ gives
$$
x(0)=0.
$$

:::

:::

::: {.pf-step #s1-10}

The initial-value problem
$$
y'(t)=f(y(t)),
\qquad
y(0)=0
$$
has at most one solution on $[0,1]$.


::: pf-proof

Let $x$ and $y$ be two solutions. Then
$$
x(t)-y(t)
=
\int_0^t
\bigl(f(x(s))-f(y(s))\bigr)\,ds.
$$
Hence
$$
\abs{x(t)-y(t)}
\le
L\int_0^t\abs{x(s)-y(s)}\,ds.
$$
By Grönwall's inequality,
$$
\abs{x(t)-y(t)}=0
$$
for all $t\in[0,1]$. Thus $x=y$.

:::

:::

::: {.pf-step #s1-11}

The full sequence $(x_k)$ converges uniformly to the solution $x$ from step [](#s1-9){.pf-ref}.


::: pf-proof

Suppose not. Then there would exist $\varepsilon>0$ and a subsequence $(x_{k_j})$ such that
$$
\norm{x_{k_j}-x}_\infty\ge\varepsilon
$$
for every $j$.

By steps [](#s1-1){.pf-ref} through [](#s1-2){.pf-ref}, this subsequence is still equicontinuous and uniformly bounded. Arzelà--Ascoli therefore gives a further subsequence converging uniformly to some function $y$. Repeating steps [](#s1-4){.pf-ref} through [](#s1-9){.pf-ref} for that further subsequence shows that $y$ solves the same initial-value problem. By uniqueness from step [](#s1-10){.pf-ref},
$$
y=x.
$$
But then the further subsequence converges uniformly to $x$, contradicting the lower bound $\varepsilon$. Therefore the full sequence converges uniformly to $x$.

:::

:::

::: {.pf-step #s1-12}

Hence
$$
\boxed{x_k\to x\text{ uniformly on }[0,1]}
$$
where $x$ solves
$$
\boxed{x'(t)=f(x(t)),\qquad x(0)=0}.
$$


::: pf-proof

Step [](#s1-11){.pf-ref} gives uniform convergence, and step [](#s1-9){.pf-ref} identifies the limit as a solution of the stated ODE and initial condition.

:::

:::

::: pf-qed

Step [](#s1-12){.pf-ref} is the required conclusion.

:::

:::

:::
