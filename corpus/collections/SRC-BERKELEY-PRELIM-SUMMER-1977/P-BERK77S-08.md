---
schema: qual/card@1
id: P-BERK77S-08
kind: problem
title: Global existence for $x'=3x+85\cos x$ with $x(0)=77$
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
  note: The unusual constants 85 and 77 were checked directly on the retained PDF page.
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    The vector field F(x)=3x+85 cos x is globally Lipschitz, so a unique
    maximal solution exists. Gronwall gives an explicit bound on |x(t)| on
    every finite time interval; then x' is bounded there, so a finite
    maximal endpoint would have a finite limiting state and local existence
    would extend the solution past that endpoint, a contradiction.
---

::: {.problem}
Prove that the initial-value problem
\[
\frac{dx}{dt}=3x+85\cos x,
\qquad x(0)=77,
\]
has a solution $x(t)$ defined for every $t\in\mathbb R$.
:::

::: {.solution}
Set
$$
F(x)=3x+85\cos x.
$$

<1>1. The vector field $F:\RR\to\RR$ is globally Lipschitz.

::: {.proof}
One has
$$
F'(x)=3-85\sin x,
$$
so
$$
\abs{F'(x)}
\leq
88
$$
for every $x\in\RR$. By the mean value theorem,
$$
\abs{F(x)-F(y)}
\leq
88\abs{x-y}
$$
for all $x,y\in\RR$.
:::

<1>2. There is a unique maximal solution
$$
x:(\alpha,\beta)\longrightarrow\RR
$$
of
$$
x'=F(x),
\qquad
x(0)=77,
$$
where
$$
-\infty\leq\alpha<0<\beta\leq\infty.
$$

::: {.proof}
The function $F$ is continuously differentiable, hence locally Lipschitz.
The Picard--Lindelöf theorem therefore gives a unique local solution through
$(0,77)$, and the standard continuation construction gives a unique maximal
solution on an open interval $(\alpha,\beta)$.
:::

<1>3. For every $t\in(\alpha,\beta)$,
$$
\abs{x(t)}
\leq
\left(77+\frac{85}{3}\right)e^{3\abs{t}}
-\frac{85}{3}.
$$

::: {.proof}
For $t\geq0$, the integral equation gives
$$
x(t)
=
77+\int_0^t\bigl(3x(s)+85\cos x(s)\bigr)\,ds,
$$
hence
$$
\abs{x(t)}
\leq
77+\int_0^t\bigl(3\abs{x(s)}+85\bigr)\,ds.
$$
Set
$$
u(t)=\abs{x(t)}+\frac{85}{3}.
$$
Then
$$
u(t)
\leq
77+\frac{85}{3}
+
3\int_0^t u(s)\,ds.
$$
Gronwall's inequality gives
$$
u(t)
\leq
\left(77+\frac{85}{3}\right)e^{3t}.
$$

For $t\leq0$, define
$$
y(s)=x(-s).
$$
Then
$$
y'(s)=-3y(s)-85\cos y(s),
\qquad
y(0)=77.
$$
The same estimate applies to $y$, because
$$
\abs{-3y-85\cos y}
\leq
3\abs y+85.
$$
Replacing $s$ by $-t$ gives the stated bound for negative $t$ as well.
:::

<1>4. The right endpoint of the maximal interval is
$$
\beta=\infty.
$$

::: {.proof}
Suppose instead that $\beta<\infty$. Step <1>3 bounds $x(t)$ on
$[0,\beta)$. Thus there is an $M<\infty$ such that
$$
\abs{x(t)}\leq M
$$
there. Consequently
$$
\abs{x'(t)}
=
\abs{3x(t)+85\cos x(t)}
\leq
3M+85.
$$
Hence $x$ is Lipschitz on $[0,\beta)$ and therefore has a finite limit
$$
L=\lim_{t\uparrow\beta}x(t).
$$

Local existence for the initial condition
$$
x(\beta)=L
$$
produces a solution on an interval containing $\beta$. By uniqueness, this
solution agrees with the original one just to the left of $\beta$, so it
extends the maximal solution past $\beta$. This contradicts maximality.
Thus $\beta=\infty$.
:::

<1>5. The left endpoint of the maximal interval is
$$
\alpha=-\infty.
$$

::: {.proof}
If $\alpha>-\infty$, step <1>3 bounds $x(t)$ on $(\alpha,0]$. The same
argument as in step <1>4 bounds $x'$ there, gives a finite limit
$$
\lim_{t\downarrow\alpha}x(t),
$$
and local existence at that limiting state extends the solution to times
less than $\alpha$. This contradicts maximality. Hence
$\alpha=-\infty$.
:::

<1>6. The initial-value problem has a solution defined for every
$t\in\RR$.

::: {.proof}
By steps <1>4 and <1>5, the maximal interval is
$$
(\alpha,\beta)=\RR.
$$
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>6 is the required global-existence conclusion.
:::
:::
