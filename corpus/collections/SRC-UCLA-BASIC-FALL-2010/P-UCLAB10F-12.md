---
schema: qual/card@1
id: P-UCLAB10F-12
kind: problem
title: Differentiate an integral over a moving disk
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
  note: Checked against Problem 12 of the retained UCLA Basic Examination, Fall 2010.
---

::: {.problem}
Let
$$
D(t)=\{(x,y)\in\RR^2:x^2+y^2\le r(t)^2\},
$$
where $r:\RR\to\RR$ is continuously differentiable.
For a given smooth nonnegative function $u:\RR^2\times\RR\to\RR$, express
$$
\frac{d}{dt}\left(\int_{D(t)}u(x,t)\,dx\right)
-
\int_{D(t)}u_t(x,t)\,dx
$$
in terms of a surface integral.
You may use standard calculus theorems without proof.
:::

::: {.solution}

Fix a time $t$ with $r(t)\ne0$, and write
$$
R(t)=\abs{r(t)}.
$$
Then
$$
D(t)=\{x\in\RR^2:\norm{x}\le R(t)\}.
$$

::: pf

::: {.pf-step #s1-1}

In polar coordinates,
$$
\int_{D(t)}u(x,t)\,dx
=
\int_0^{2\pi}\int_0^{R(t)}
u(\rho\cos\theta,\rho\sin\theta,t)\,
\rho\,d\rho\,d\theta.
$$


::: pf-proof

This is the standard change-of-variables formula
$$
x=(\rho\cos\theta,\rho\sin\theta),
$$
whose Jacobian is $\rho$, for the disk of radius $R(t)$.

:::

:::

::: {.pf-step #s1-2}

Differentiating the expression in step [](#s1-1){.pf-ref} gives
$$
\begin{aligned}
\frac d{dt}\int_{D(t)}u(x,t)\,dx
&=
\int_{D(t)}u_t(x,t)\,dx\\
&\quad+
R'(t)R(t)
\int_0^{2\pi}
u(R(t)\cos\theta,R(t)\sin\theta,t)\,d\theta.
\end{aligned}
$$


::: pf-proof

Apply the one-variable Leibniz rule to the inner integral in $\rho$, then integrate in $\theta$. The derivative of the integrand with respect to $t$ contributes
$$
\int_0^{2\pi}\int_0^{R(t)}
u_t(\rho\cos\theta,\rho\sin\theta,t)\rho\,d\rho\,d\theta,
$$
which is
$$
\int_{D(t)}u_t(x,t)\,dx.
$$
The moving upper endpoint contributes the second term displayed above.

:::

:::

::: {.pf-step #s1-3}

The boundary arclength element on $\partial D(t)$ is
$$
dS=R(t)\,d\theta.
$$
Hence
$$
R(t)
\int_0^{2\pi}
u(R(t)\cos\theta,R(t)\sin\theta,t)\,d\theta
=
\int_{\partial D(t)}u(x,t)\,dS.
$$


::: pf-proof

Parametrize the circle by
$$
\gamma(\theta)
=
\bigl(R(t)\cos\theta,R(t)\sin\theta\bigr).
$$
Then
$$
\norm{\gamma'(\theta)}=R(t),
$$
so the line element is $dS=R(t)\,d\theta$.

:::

:::

::: {.pf-step #s1-4}

Therefore, whenever $r(t)\ne0$,
$$
\boxed{
\frac d{dt}\left(\int_{D(t)}u(x,t)\,dx\right)
-
\int_{D(t)}u_t(x,t)\,dx
=
R'(t)\int_{\partial D(t)}u(x,t)\,dS
}.
$$


::: pf-proof

Substitute the identity from step [](#s1-3){.pf-ref} into step [](#s1-2){.pf-ref} and subtract the interior $u_t$ integral.

:::

:::

::: {.pf-step #s1-5}

In terms of the function $r$ appearing in the problem,
$$
R'(t)
=
\operatorname{sgn}(r(t))\,r'(t)
$$
when $r(t)\ne0$.
Thus the general signed formula is
$$
\boxed{
\frac d{dt}\left(\int_{D(t)}u\,dx\right)
-
\int_{D(t)}u_t\,dx
=
\operatorname{sgn}(r(t))\,r'(t)
\int_{\partial D(t)}u\,dS
}.
$$
If $r(t)>0$, as for an ordinary radius function, this reduces to
$$
\boxed{
r'(t)\int_{\partial D(t)}u(x,t)\,dS
}.
$$


::: pf-proof

For $r(t)\ne0$,
$$
\frac d{dt}\abs{r(t)}
=
\operatorname{sgn}(r(t))\,r'(t).
$$
Insert this into step [](#s1-4){.pf-ref}.

:::

:::

::: {.pf-step #s1-6}

If $r(t)=0$, the moving-boundary contribution is $0$.


::: pf-proof

Near such a time, smoothness of $u$ gives
$$
\int_{D(t)}u(x,t)\,dx
=
O(r(t)^2).
$$
Because
$$
\frac d{dt}r(t)^2=2r(t)r'(t)=0
$$
at a zero of $r$, the first-order contribution caused by the changing disk is zero. The boundary has zero arclength there, so the surface-integral expression also vanishes in the natural limiting sense.

:::

:::

::: pf-qed

Steps [](#s1-4){.pf-ref} through [](#s1-6){.pf-ref} give the requested surface-integral expression, including the sign convention forced by the fact that the disk depends on $r(t)^2$.

:::

:::

:::
