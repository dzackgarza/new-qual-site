---
schema: qual/card@1
id: E-SS2.EX-5
kind: problem
title: Goursat's theorem for $C^1$ functions via Green's theorem
classification:
  areas:
  - complex-analysis
  topics:
  - Cauchy's Theorem
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Structured into Lamport steps from the card's own prose, which is the printed hint's route.
    Checked and kept: f continuously complex differentiable gives u = Re f and v = Im f of class
    C^1 with the Cauchy-Riemann equations (Chapter 1), and Green's theorem as quoted in the
    statement, applied to (u, -v) and to (v, u), produces the integrands -v_x - u_y = 0 and
    u_x - v_y = 0; the triangle is closed with piecewise C^1 boundary and its interior in Omega,
    so the theorem applies on it. Written out in the proof and absent from the prose: the
    derivative of a complex differentiable map is multiplication by a matrix of the form
    [[p, -q], [q, p]], which is what produces the four partials and the Cauchy-Riemann equations,
    and the compactness argument that a neighbourhood of T lies in Omega. The statement is
    unchanged. No retained solution set covers the exercises of Stein-Shakarchi, so the card's
    solution says the argument is its own; no published solution was searched for outside the
    checkout.
---

::: {.exercise}
Suppose $f$ is continuously complex differentiable on $\Omega$, and $T \subset \Omega$ is a triangle whose interior is also contained in $\Omega$. Apply Green's theorem to show that
$$
\int_T f(z)\, dz = 0.
$$
This provides a proof of Goursat's theorem under the additional assumption that $f'$ is continuous.

[Hint: Green's theorem says that if $(F, G)$ is a continuously differentiable vector field, then
$$
\int_T F\, dx + G\, dy = \int_{\text{Interior of } T} \left( \frac{\partial G}{\partial x} - \frac{\partial F}{\partial y} \right) dx\, dy.
$$
For appropriate $F$ and $G$, one can then use the Cauchy-Riemann equations.]
:::

::: {.solution}
Write $u=\Re f$ and $v=\Im f$, so that $f=u+iv$ and $\dd z=\dd x+i\,\dd y$. Because $f$ is continuously complex differentiable, $u$ and $v$ are continuously differentiable and satisfy the Cauchy--Riemann equations, so each integral that Green's theorem produces is the integral of a function vanishing identically. This is the printed hint's route, with each step checked against the book's Cauchy--Riemann equations (Chapter 1, §2) and the statement's form of Green's theorem; the argument is this card's own, since no retained solution set covers the exercises of Stein--Shakarchi.

::: pf

::: {.pf-step #components}
On a neighbourhood of the closed triangle $T$ the functions $u=\Re f$ and $v=\Im f$ are continuously differentiable and satisfy $u_x=v_y$ and $u_y=-v_x$.

::: pf-proof
At a point $z_0$ where $f$ is complex differentiable with derivative $a$, the real-linear approximation $f(z_0+h)=f(z_0)+ah+o(\abs h)$ says that the real differential of $(u,v)$ at $z_0$ is multiplication by the matrix $\begin{pmatrix}p&-q\\ q&p\end{pmatrix}$, where $a=p+iq$; hence all four partial derivatives exist there, with $u_x=v_y=p$ and $u_y=-v_x=q$, which are the Cauchy--Riemann equations. Continuous complex differentiability means $z\mapsto f'(z)$ is continuous, so $p=u_x$ and $q=v_x$ are continuous, and then $u_y=-v_x$ and $v_y=u_x$ are continuous as well: $u$ and $v$ are $C^1$. Since $T$ and its interior lie in $\Omega$ and $T$ is compact, a neighbourhood of $T$ lies in $\Omega$.
:::

:::


::: {.pf-step #real}
$\displaystyle\int_T u\,\dd x-v\,\dd y=0$.

::: pf-proof
Apply Green's theorem as quoted in the statement to the $C^1$ field $(F,G)=(u,-v)$ on the closed triangle $T$, whose boundary is a piecewise $C^1$ closed curve and whose interior lies in $\Omega$:
$$
\int_T u\,\dd x-v\,\dd y=\iint_{\operatorname{int}T}\Bigl(\frac{\partial G}{\partial x}-\frac{\partial F}{\partial y}\Bigr)\dd x\,\dd y=\iint_{\operatorname{int}T}(-v_x-u_y)\,\dd x\,\dd y=0,
$$
because $u_y=-v_x$ by step [](#components){.pf-ref}.
:::

:::


::: {.pf-step #imaginary}
$\displaystyle\int_T v\,\dd x+u\,\dd y=0$.

::: pf-proof
Green's theorem applied to the $C^1$ field $(F,G)=(v,u)$ on the same triangle gives
$$
\int_T v\,\dd x+u\,\dd y=\iint_{\operatorname{int}T}(u_x-v_y)\,\dd x\,\dd y=0,
$$
because $u_x=v_y$ by step [](#components){.pf-ref}.
:::

:::


::: {.pf-step #conclusion}
$\displaystyle\int_T f(z)\,\dd z=0$, so Goursat's theorem holds for every continuously complex differentiable $f$ on a neighbourhood of $T$.

::: pf-proof
Multiplying out, $f(z)\,\dd z=(u+iv)(\dd x+i\,\dd y)=(u\,\dd x-v\,\dd y)+i(v\,\dd x+u\,\dd y)$, since $i^2=-1$. A complex-valued integral is the pair of the integrals of its real and imaginary parts, so by steps [](#real){.pf-ref} and [](#imaginary){.pf-ref}
$$
\int_T f(z)\,\dd z=\int_T u\,\dd x-v\,\dd y+i\int_T v\,\dd x+u\,\dd y=0.
$$
:::

:::

:::
:::
