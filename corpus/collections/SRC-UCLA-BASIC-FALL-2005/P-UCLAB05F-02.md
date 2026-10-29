---
schema: qual/card@1
id: P-UCLAB05F-02
kind: problem
title: Sufficient conditions for equality of mixed partial derivatives
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 2 of the official UCLA Basic Examination, September 2005 PDF. The first mixed-partial denominator in the scan is typographically written as `\partial x\,dy`; the intended equality of the two mixed second partials is otherwise explicit.
---

::: {.problem}
State some reasonable conditions on a real-valued function $f(x,y)$ on $\RR^2$ which guarantee that
$$
\frac{\partial^2f}{\partial x\,\partial y}
=
\frac{\partial^2f}{\partial y\,\partial x}
$$
at every point of $\RR^2$.
Then prove that your conditions do in fact guarantee this equality.
:::

::: {.solution}

Assume that $f\in C^2(\RR^2)$; equivalently, all second partial derivatives of $f$ exist and are continuous on $\RR^2$.

Fix $(a,b)\in\RR^2$. For nonzero $h,k$, define
$$
\Delta(h,k)
=
f(a+h,b+k)-f(a+h,b)-f(a,b+k)+f(a,b).
$$

::: pf

::: {.pf-step #s1-1}

For every nonzero $h,k$, there are points $\xi$ between $a$ and $a+h$ and $\eta$ between $b$ and $b+k$ such that
$$
\frac{\Delta(h,k)}{hk}
=
\frac{\partial}{\partial y}
\left(\frac{\partial f}{\partial x}\right)(\xi,\eta).
$$


::: pf-proof

Set
$$
G(x)=f(x,b+k)-f(x,b).
$$
By the one-variable mean value theorem, for some $\xi$ between $a$ and $a+h$,
$$
\Delta(h,k)
=
G(a+h)-G(a)
=
h\bigl(f_x(\xi,b+k)-f_x(\xi,b)\bigr).
$$
Applying the mean value theorem to the one-variable function $y\mapsto f_x(\xi,y)$ gives some $\eta$ between $b$ and $b+k$ such that
$$
f_x(\xi,b+k)-f_x(\xi,b)
=
k\frac{\partial}{\partial y}
\left(\frac{\partial f}{\partial x}\right)(\xi,\eta).
$$
Combining the two equalities and dividing by $hk$ proves the claim.

:::

:::

::: {.pf-step #s1-2}

For every nonzero $h,k$, there are points $\xi'$ between $a$ and $a+h$ and $\eta'$ between $b$ and $b+k$ such that
$$
\frac{\Delta(h,k)}{hk}
=
\frac{\partial}{\partial x}
\left(\frac{\partial f}{\partial y}\right)(\xi',\eta').
$$


::: pf-proof

Regroup the same increment as
$$
\Delta(h,k)
=
\bigl(f(a+h,b+k)-f(a,b+k)\bigr)
-
\bigl(f(a+h,b)-f(a,b)\bigr).
$$
Set
$$
H(y)=f(a+h,y)-f(a,y).
$$
The mean value theorem in the $y$-variable gives some $\eta'$ between $b$ and $b+k$ such that
$$
\Delta(h,k)
=
k\bigl(f_y(a+h,\eta')-f_y(a,\eta')\bigr).
$$
Applying the mean value theorem to $x\mapsto f_y(x,\eta')$ gives some $\xi'$ between $a$ and $a+h$ such that
$$
f_y(a+h,\eta')-f_y(a,\eta')
=
h\frac{\partial}{\partial x}
\left(\frac{\partial f}{\partial y}\right)(\xi',\eta').
$$
Dividing the resulting identity by $hk$ proves the claim.

:::

:::

::: {.pf-step #s1-3}

At the fixed point $(a,b)$,
$$
\frac{\partial}{\partial x}
\left(\frac{\partial f}{\partial y}\right)(a,b)
=
\frac{\partial}{\partial y}
\left(\frac{\partial f}{\partial x}\right)(a,b).
$$


::: pf-proof

Steps [](#s1-1){.pf-ref} and [](#s1-2){.pf-ref} show that, for each nonzero $h,k$,
$$
\frac{\partial}{\partial y}
\left(\frac{\partial f}{\partial x}\right)(\xi,\eta)
=
\frac{\Delta(h,k)}{hk}
=
\frac{\partial}{\partial x}
\left(\frac{\partial f}{\partial y}\right)(\xi',\eta').
$$
As $(h,k)\to(0,0)$, the points $(\xi,\eta)$ and $(\xi',\eta')$ both tend to $(a,b)$. The two mixed second partials are continuous because $f\in C^2(\RR^2)$. Taking limits in the displayed equality therefore gives the claimed equality at $(a,b)$.

:::

:::

::: {.pf-step #s1-4}

The mixed partial derivatives agree at every point of $\RR^2$.


::: pf-proof

The point $(a,b)$ was arbitrary, so step [](#s1-3){.pf-ref} applies throughout $\RR^2$.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} proves that the stated $C^2$ condition guarantees the required equality.

:::

:::

:::
