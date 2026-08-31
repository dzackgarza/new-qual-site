---
schema: qual/card@1
id: P-JES3E
kind: problem
title: $\frac{e^{ny}-e^{-ny}}{2n^2}\sin nx$ solves the Laplace Cauchy problem on the
  disk with data $\sin(nx)/n$, and $\limsup_n|u|=\infty$ at some points
classification:
  areas:
  - complex-analysis
  topics:
  - Harmonic Functions
  - PDEs
  - Counterexamples
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-19
---

::: problem
Show that the function $u=u(x,y)$ given by
$$
u(x,y)=\frac{e^{ny}-e^{-ny}}{2n^2}\sin nx\quad \text{for}\ n\in {\mathbf N}
$$
is the solution on $D=\{(x,y)\ | x^2+y^2<1\}$ of the Cauchy problem for the Laplace equation
$$\frac{\partial ^2u}{\partial x^2}+\frac{\partial ^2u}{\partial y^2}=0,\quad
u(x,0)=0,\quad \frac{\partial u}{\partial y}(x,0)=\frac{\sin nx}{n}.$$

Show that there exist points $(x,y)\in D$ such that $\displaystyle{\limsup_{n\to\infty} |u(x,y)|=\infty}$.
:::

::: {.solution}
**Goal:** (1) Verify that $u_n(x,y) = \frac{e^{ny} - e^{-ny}}{2n^2}\sin(nx)$ solves, on $D = \{x^2 + y^2 < 1\}$, the Cauchy problem $\Delta u = 0$, $u(x,0) = 0$, $u_y(x,0) = \frac{\sin(nx)}{n}$; (2) show there exist points $(x,y) \in D$ with $\limsup_{n \to \infty} \abs{u_n(x,y)} = \infty$.

<1>1. Verify the boundary conditions at $y = 0$.
    ::: {.proof}
    $u_n(x,0) = \frac{e^0 - e^0}{2n^2}\sin(nx) = 0$. And $\dd{u_n}{y} = \frac{n e^{ny} + n e^{-ny}}{2n^2}\sin(nx) = \frac{e^{ny} + e^{-ny}}{2n}\sin(nx)$, so $\dd{u_n}{y}(x,0) = \frac{2}{2n}\sin(nx) = \frac{\sin(nx)}{n}$.
    :::

<1>2. Verify $\Delta u_n = 0$ on $D$.
    ::: {.proof}
    ${\partial^2 u_n \over \partial x^2} = -n^2 u_n$ (since ${d^2 \over dx^2}\sin(nx) = -n^2\sin(nx)$), and ${\partial^2 u_n \over \partial y^2} = \frac{n^2 e^{ny} - n^2 e^{-ny}}{2n^2}\sin(nx) = \frac{e^{ny} - e^{-ny}}{2}\sin(nx) = n^2 u_n$. Hence $u_{xx} + u_{yy} = -n^2 u_n + n^2 u_n = 0$.
    :::

<1>3. For (2), choose $x \in (0,1)$ with $x/\pi$ irrational.
    ::: {.proof}
    Any such $x$ has $\abs{x} < 1$, so $(x,y) \in D$ whenever $y$ is small enough that $x^2 + y^2 < 1$; e.g. $x = 1/\pi$ and $y = 1/2$ works since $1/\pi^2 + 1/4 < 1$.
    :::

<1>4. Along a subsequence of $n$'s, $\abs{\sin(nx)} \ge 1/2$.
    ::: {.proof}
    The sequence $nx \bmod 2\pi$ is equidistributed (Weyl's criterion), because $x/2\pi = (x/\pi)/2$ is irrational; hence $\abs{\sin(nx)} \ge 1/2$ for infinitely many $n$.
    :::

<1>5. For fixed $y > 0$, $\abs{u_n(x,y)} \to \infty$ along that subsequence.
    ::: {.proof}
    Along the subsequence of <1>4, $\abs{u_n(x,y)} \ge \frac{1}{2}\frac{e^{ny} - e^{-ny}}{2n^2} \ge \frac{e^{ny}}{4n^2}\qty(1 - e^{-2ny})$, and for fixed $y > 0$, $e^{ny}/n^2 \to \infty$ and $1 - e^{-2ny} \to 1$. (For $y < 0$ the same argument applies with $e^{-ny}$ in place of $e^{ny}$.)
    :::

<1>6. Q.E.D.
    ::: {.proof}
    <1>1–<1>2 verify (1); <1>3–<1>5 verify (2) at any point $(x,y) \in D$ with $y \neq 0$ and $x/\pi$ irrational, e.g. $(1/\pi, 1/2)$.
    :::

:::
