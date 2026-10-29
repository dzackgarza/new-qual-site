---
schema: qual/card@1
id: P-UCLAB01F-05
kind: problem
title: Equality of mixed partial derivatives under continuity hypotheses
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 5 of the retained UCLA Basic Exam, Fall 2001 PDF.
---

::: {.problem}
Suppose $f:\RR^2\to\RR$ is continuous, the first partial derivatives
$$
\frac{\partial f}{\partial x},\qquad \frac{\partial f}{\partial y}
$$
exist everywhere and are continuous everywhere, and the mixed partials
$$
\frac{\partial}{\partial x}\left(\frac{\partial f}{\partial y}\right),
\qquad
\frac{\partial}{\partial y}\left(\frac{\partial f}{\partial x}\right)
$$
also exist everywhere and are continuous everywhere.
Prove that
$$
\frac{\partial}{\partial x}\left(\frac{\partial f}{\partial y}\right)
=
\frac{\partial}{\partial y}\left(\frac{\partial f}{\partial x}\right)
$$
at every point of $\RR^2$.
:::

::: {.solution}

Fix $(a,b)\in\RR^2$. For nonzero $h,k$, set
$$
D(h,k)=f(a+h,b+k)-f(a+h,b)-f(a,b+k)+f(a,b).
$$

::: pf

::: {.pf-step #s1-1}

For every nonzero $h,k$, there are points $\xi$ between $a$ and $a+h$ and $\eta$ between $b$ and $b+k$ such that
$$
\frac{D(h,k)}{hk}
=
\frac{\partial}{\partial y}
\left(\frac{\partial f}{\partial x}\right)(\xi,\eta).
$$


::: pf-proof

Set $G(x)=f(x,b+k)-f(x,b)$. The one-variable mean value theorem gives some $\xi$ between $a$ and $a+h$ with
$$
D(h,k)=h\bigl(f_x(\xi,b+k)-f_x(\xi,b)\bigr).
$$
Applying the mean value theorem to $y\mapsto f_x(\xi,y)$ gives some $\eta$ between $b$ and $b+k$ such that
$$
f_x(\xi,b+k)-f_x(\xi,b)=k(f_x)_y(\xi,\eta).
$$
Combining these identities proves the claim.

:::

:::

::: {.pf-step #s1-2}

For every nonzero $h,k$, there are points $\xi'$ between $a$ and $a+h$ and $\eta'$ between $b$ and $b+k$ such that
$$
\frac{D(h,k)}{hk}
=
\frac{\partial}{\partial x}
\left(\frac{\partial f}{\partial y}\right)(\xi',\eta').
$$


::: pf-proof

Set $H(y)=f(a+h,y)-f(a,y)$. The mean value theorem gives some $\eta'$ between $b$ and $b+k$ with
$$
D(h,k)=k\bigl(f_y(a+h,\eta')-f_y(a,\eta')\bigr).
$$
Applying the mean value theorem to $x\mapsto f_y(x,\eta')$ gives some $\xi'$ between $a$ and $a+h$ such that
$$
f_y(a+h,\eta')-f_y(a,\eta')=h(f_y)_x(\xi',\eta').
$$
Combining these identities proves the claim.

:::

:::

::: {.pf-step #s1-3}

At $(a,b)$,
$$
\frac{\partial}{\partial x}
\left(\frac{\partial f}{\partial y}\right)(a,b)
=
\frac{\partial}{\partial y}
\left(\frac{\partial f}{\partial x}\right)(a,b).
$$


::: pf-proof

Steps [](#s1-1){.pf-ref} and [](#s1-2){.pf-ref} give
$$
(f_x)_y(\xi,\eta)
=
\frac{D(h,k)}{hk}
=
(f_y)_x(\xi',\eta').
$$
As $(h,k)\to(0,0)$, both intermediate points tend to $(a,b)$. Continuity of the two mixed partial derivatives therefore gives
$$
(f_x)_y(a,b)=(f_y)_x(a,b).
$$

:::

:::

::: {.pf-step #s1-4}

The mixed partial derivatives agree at every point of $\RR^2$.


::: pf-proof

The point $(a,b)$ was arbitrary, so step [](#s1-3){.pf-ref} holds throughout $\RR^2$.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} is the required conclusion.

:::

:::

:::
