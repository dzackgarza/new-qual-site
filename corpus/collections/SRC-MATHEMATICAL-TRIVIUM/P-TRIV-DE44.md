---
schema: qual/card@1
id: P-TRIV-DE44
kind: problem
title: Vibrating rectangular membrane with a single-mode initial profile
classification:
  areas: [prelim]
  topics:
  - Wave Equation
  - Separation of Variables
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Differential Equations, Problem 44, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
A two dimensional rectangular slab (with the two sides of length $a$ and $b$) has its edges fixed; at time $t = 0$ it has the profile
$$
u(x, y, 0) = \sin\frac{2x\pi}{a}\sin\frac{3y\pi}{b}; \tag{41}
$$
find $u(x, y, t)$ knowing that it satisfies the wave equation with a velocity $v$.
:::

::: {.solution}

The wave equation is
$$
u_{tt}=v^2(u_{xx}+u_{yy})
$$
on $0<x<a$, $0<y<b$, with $u=0$ on the boundary. To determine a unique evolution from the stated initial displacement, take the customary unstated initial condition $u_t(x,y,0)=0$.

::: pf

::: {.pf-step #s1-1}

The initial profile is already a single Dirichlet eigenmode of the spatial Laplacian:
$$
\phi(x,y)=\sin\frac{2\pi x}{a}\sin\frac{3\pi y}{b}.
$$


::: pf-proof

The sine factors vanish at $x=0,a$ and $y=0,b$. Moreover,
$$
\phi_{xx}+\phi_{yy}
=-\left[\left(\frac{2\pi}{a}\right)^2
+\left(\frac{3\pi}{b}\right)^2\right]\phi.
$$

:::

:::

::: {.pf-step #s1-2}

A solution retaining this spatial mode has the form
$$
u(x,y,t)=T(t)\phi(x,y),
$$
where
$$
T''+\omega^2T=0,
\qquad
\omega=v\pi\sqrt{\frac4{a^2}+\frac9{b^2}}.
$$


::: pf-proof

Substitute $T\phi$ into the wave equation and use step [](#s1-1){.pf-ref}. Division by the nonzero spatial mode gives
$$
T''=-v^2\pi^2\left(\frac4{a^2}+\frac9{b^2}\right)T.
$$

:::

:::

::: {.pf-step #s1-3}

The initial conditions give
$$
T(0)=1,
\qquad
T'(0)=0,
$$
so
$$
T(t)=\cos(\omega t).
$$


::: pf-proof

The general solution of step [](#s1-2){.pf-ref} is $T=A\cos(\omega t)+B\sin(\omega t)$. The prescribed initial displacement gives $A=1$, and zero initial velocity gives $B=0$.

:::

:::

::: {.pf-step #s1-4}

Therefore
$$
\boxed{
u(x,y,t)=
\sin\frac{2\pi x}{a}
\sin\frac{3\pi y}{b}
\cos\left(v\pi t\sqrt{\frac4{a^2}+\frac9{b^2}}\right)}.
$$


::: pf-proof

Combine steps [](#s1-1){.pf-ref} through [](#s1-3){.pf-ref}. The result satisfies the fixed-edge conditions, the wave equation, the stated initial profile, and zero initial velocity.

:::

:::

::: {.pf-step #s1-5}

Without an initial-velocity condition, the problem is underdetermined.


::: pf-proof

For any constant $B$, adding
$$
B\sin(\omega t)\phi(x,y)
$$
preserves the PDE, boundary conditions, and initial displacement while changing $u_t(x,y,0)$ by $B\omega\phi(x,y)$. Thus the displayed solution is the unique one only after imposing $u_t(x,y,0)=0$.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} gives the standard zero-initial-velocity solution, and step [](#s1-5){.pf-ref} records the missing datum in the source statement.

:::

:::

:::
