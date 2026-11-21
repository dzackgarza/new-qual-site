---
schema: qual/card@1
id: E-N6DX3
kind: problem
title: Cauchy–Riemann equations and elementary complex analysis
classification:
  areas:
  - complex-analysis
  topics:
  - Cauchy-Riemann
  - Holomorphic Functions
  - Meromorphic Functions
  - Harmonic Functions
relations: []
review: draft
audit:
- event: source-corrected
  by: Claude Opus 5.5
  date: 2026-10-29
  note: The source nests four guidance bullets under parts (j), (k), (l) and (m), one of which gives the example sum z^k/k^2; they are moved to the hint block. The parts are labelled (a) through (n).
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    Eight of the fourteen steps asserted their claim with no justification and each now carries one:
    parts (a) through (f), (h) and (i). Where a part asks for a definition the sentence says what makes
    the stated form the right one rather than repeating it: part (a) derives the pair by taking the
    difference quotient along real and along imaginary increments, part (c) says why a supremum tending
    to zero is the same as one $N$ serving every point, part (d) names the Laplacian, and part (e) says
    which conditions make the Dirichlet problem well posed. Part (f) now carries the reason the
    principal parts exhaust the poles and the remainder is entire and vanishes at infinity, hence zero.
    Part (h) says why the quotient is meromorphic and in what sense it is the derivative of a logarithm.
    Part (i) exhibits the example's failure: the function is $1$ on the closed upper half disc and $-1$
    below, so it is discontinuous at every point of $(-1,1)$ and hence differentiable nowhere, while its
    square is the constant $1$. Parts (g), (j), (k), (l), (m) and (n) were already justified and are
    unchanged. The statement is unchanged. The card stands alone, with no collection provenance and no
    retained published solution, so the argument is the card's own.
---

::: {.exercise}
(a) State the Cauchy-Riemann equations.

(b) Define what it means for a function to be

  - Holomorphic

  - Meromorphic

  - Analytic

  - Harmonic

  - Uniformly continuous

  - Uniformly bounded

  - Entire

(c) What does it mean for a sequence or series to uniformly converge?

(d) State the Laplace equation.

(e) What is the Dirichlet problem?

(f) Discuss how to carry out partial fraction decomposition

(g) Determine the radius of convergence of the power series for $\sqrt z$ expanded at $z_0= 4 + 3i$.

(h) What is the logarithmic derivative?

(i) Find a  function $f$ such that $f^2$ is analytic on the open unit disc but $f$ is not.

(j) Show that $f(z)=z^2$ is uniformly continuous on every disk $\abs{z}<R$,
  but is not uniformly continuous on $\CC$.

(k) Identify $\RR^2$ with $\CC$ and give a necessary and sufficient condition
  for a real-differentiable function at $(a,b)$ to be complex differentiable
  at $a+ib$.

(l) Let $f=u+iv$ be complex differentiable with continuous partial derivatives
  at $z=re^{i\theta}$, $r\ne0$. Derive the polar Cauchy--Riemann equations.

(m) Suppose $f(z)=\sum_{n\ge0}a_nz^n$ has radius of convergence exactly $1$.
  Give an example whose series converges at every point of $S^1$; give an
  example for which $f$ is analytic at $1$ but $\sum a_n$ diverges; and prove
  that $f$ cannot be analytic at every point of $S^1$.

(n) Find the Laurent expansions of
  $$
  {z+1\over z(z-1)^2}
  $$
  about $z=0$ and $z=1$.
:::

::: {.hint}
(j) Lipschitz implies uniformly continuous.

(k) Compute the difference quotient along real and along imaginary increments $h$.

(l) Use polar coordinates, the chain rule, and the Cauchy--Riemann equations.

(m) For convergence everywhere on $S^1$, consider $\sum z^k/k^2$.
:::

::: {.solution}
Write $f=u+iv$ throughout.

::: pf

::: {.pf-step #cr}
(a) The Cauchy--Riemann equations are $u_x=v_y$ and $u_y=-v_x$.

::: pf-proof
Complex differentiability at $z$ means that $\frac{f(z+h)-f(z)}{h}$ has a limit as $h \to 0$ through complex values. Taking $h$ real gives $u_x + iv_x$ and taking $h$ purely imaginary gives $v_y - iu_y$, so the two must be equal: $u_x = v_y$ and $v_x = -u_y$, which is the pair displayed.
:::

:::

::: pf-step
(b) A function on an open set is \dfn{holomorphic} if it is complex differentiable at every point; \dfn{meromorphic} if it is holomorphic except on a discrete set of poles; \dfn{analytic} if it is locally the sum of a convergent power series (in one complex variable, equivalent to holomorphic); \dfn{harmonic} if it is real-valued, $C^2$, and satisfies $u_{xx}+u_{yy}=0$; \dfn{entire} if it is holomorphic on all of $\CC$. A function $f$ on a set $E$ is \dfn{uniformly continuous} if for every $\varepsilon>0$ there is $\delta>0$ with $\abs{f(z)-f(w)}<\varepsilon$ for all $z,w\in E$ with $\abs{z-w}<\delta$; a family of functions on $E$ is \dfn{uniformly bounded} if one constant $M$ bounds $\abs f$ on $E$ for every member $f$.

::: pf-proof
Each clause is the standard definition in one complex variable; the only clause that is a theorem rather than a definition is the parenthetical one, that a function is holomorphic exactly when it is locally a convergent power series, which is the statement that holomorphic functions are analytic and that power series are holomorphic inside their disc of convergence. The uniform clauses quantify over pairs of points or over the family, which is what distinguishes them from plain continuity and plain boundedness.
:::

:::

::: pf-step
(c) $f_n\to f$ \dfn{uniformly} on $E$ if $\sup_{E}\abs{f_n-f}\to0$; a series converges uniformly if its partial sums do.

::: pf-proof
The supremum $\sup_E \abs{f_n - f}$ is the least number bounding $\abs{f_n - f}$ on $E$, so it tends to $0$ exactly when, for every $\varepsilon > 0$, some $N$ makes that bound less than $\varepsilon$; a single $N$ then serves every $z \in E$, which is uniform convergence, and the series case is applied to the partial sums.
:::

:::

::: pf-step
(d) The Laplace equation is $u_{xx}+u_{yy}=0$.

::: pf-proof
The Laplacian on $\RR^2$ is $\Delta = \partial_{xx} + \partial_{yy}$, and the Laplace equation is $\Delta u = 0$; for the $C^2$ real-valued $u$ of a harmonic function this is the displayed second-order equation.
:::

:::

::: pf-step
(e) Given a domain $\Omega$ and a continuous function $\varphi$ on $\partial\Omega$, the Dirichlet problem asks for $u$ harmonic on $\Omega$, continuous on $\overline\Omega$, with $u=\varphi$ on $\partial\Omega$.

::: pf-proof
The Dirichlet problem asks for a function harmonic in the interior of $\Omega$ and continuous on the closure with prescribed boundary values, so its data are the domain and a continuous $\varphi$ on $\partial\Omega$; the requirement is exactly $u = \varphi$ on the boundary and $\Delta u = 0$ inside, which is what the step states.
:::

:::

::: pf-step
(f) For a rational function $p/q$ with $\deg p<\deg q$, factor $q=c\prod_j(z-a_j)^{m_j}$ over $\CC$ and write $\frac pq=\sum_j\sum_{k=1}^{m_j}\frac{A_{j,k}}{(z-a_j)^k}$; multiplying through by $q$ and comparing coefficients, or expanding $(z-a_j)^{m_j}\frac pq$ at $a_j$, determines the $A_{j,k}$.

::: pf-proof
Over $\CC$ the polynomial $q$ factors into linear factors as displayed, with $c$ the leading coefficient. Subtracting from $p/q$ the sum of the principal parts kills the pole at each $a_j$, since each $\frac{A_{j,k}}{(z-a_j)^k}$ is the tail of the Laurent expansion there and matching the coefficients of $(z-a_j)^{-k}$ for $k = 1,\dots,m_j$ removes them all; what remains is entire, and because $\deg p < \deg q$ it tends to $0$ at infinity, so it is bounded and entire, hence constant, and constant with limit $0$, hence zero. Matching coefficients after multiplying by $q$ and expanding at $a_j$ therefore determines every $A_{j,k}$, and the expansion is unique because the principal parts are.
:::

:::

::: pf-step
(g) The radius of convergence is $\boxed{5}$.

::: pf-proof
The disk of radius $5=\abs{z_0}$ about $z_0$ is simply connected and omits $0$, so a branch of $\sqrt z$ is holomorphic on it and its Taylor series converges there. A larger disk contains $0$; a holomorphic $g$ there with $g^2=z$ would satisfy $g(0)=0$ and $2g(0)g'(0)=1$, which is impossible.
:::

:::

::: pf-step
(h) The logarithmic derivative of a holomorphic $f\not\equiv0$ is the meromorphic function $f'/f$.

::: pf-proof
Since $f$ is holomorphic and not identically zero on a domain, its zeros are isolated, so $f'/f$ is defined and holomorphic off them and has poles at them, which is what meromorphic means. Where a holomorphic branch of $\log f$ exists, differentiating $\exp(\log f) = f$ by the chain rule gives $\exp(\log f)\cdot(\log f)' = f'$, that is $(\log f)' = f'/f$, so the quotient deserves the name.
:::

:::

::: pf-step
(i) $f\coloneqq1$ on $\theset{\Im z\ge0}\cap\DD$ and $f\coloneqq-1$ on $\theset{\Im z<0}\cap\DD$ has $f^2\equiv1$ analytic, while $f$ is not continuous and so not analytic.

::: pf-proof
The square $f^2$ is the constant function $1$ on the disc, because $(\pm 1)^2 = 1$ at every point, and a constant function is analytic. The function $f$ itself is not continuous at any point of $(-1,1)$: along the real axis $f$ is $1$, while at points of the disc just below the axis it is $-1$, so a sequence approaching such a point from below has values tending to $-1 \ne 1 = f(x)$. A function that is not continuous at a point of an open set is not complex differentiable there, so $f$ is not analytic on $\DD$.
:::

:::

::: pf-step
(j) $z^2$ is uniformly continuous on $\abs z<R$ but not on $\CC$.

::: pf-proof
For $\abs z,\abs w<R$, $\abs{z^2-w^2}=\abs{z+w}\abs{z-w}\le2R\abs{z-w}$. On $\CC$, $z_n=n$ and $w_n=n+\frac1n$ satisfy $\abs{z_n-w_n}\to0$ and $\abs{w_n^2-z_n^2}=2+\frac1{n^2}\ge2$.
:::

:::

::: pf-step
(k) A real-differentiable $f$ is complex differentiable at $a+ib$ if and only if the Cauchy--Riemann equations hold at $(a,b)$.

::: pf-proof
$f$ is complex differentiable at $a+ib$ if and only if its real derivative there is multiplication by a complex number, that is, $\CC$-linear. Its matrix $\begin{pmatrix}u_x&u_y\\v_x&v_y\end{pmatrix}$ is $\CC$-linear if and only if it has the form $\begin{pmatrix}\alpha&-\beta\\\beta&\alpha\end{pmatrix}$, which is step [](#cr){.pf-ref}.
:::

:::

::: pf-step
(l) $u_r=\frac1rv_\theta$ and $v_r=-\frac1ru_\theta$.

::: pf-proof
By the chain rule with $x=r\cos\theta$, $y=r\sin\theta$,
$$
\begin{aligned}
u_r&=u_x\cos\theta+u_y\sin\theta, & u_\theta&=r(-u_x\sin\theta+u_y\cos\theta),\\
v_r&=v_x\cos\theta+v_y\sin\theta, & v_\theta&=r(-v_x\sin\theta+v_y\cos\theta).
\end{aligned}
$$
Substituting $v_x=-u_y$ and $v_y=u_x$ gives $v_\theta=r(u_y\sin\theta+u_x\cos\theta)=ru_r$ and $v_r=-u_y\cos\theta+u_x\sin\theta=-\frac1ru_\theta$.
:::

:::

::: pf-step
(m) $\sum_{n\ge1}z^n/n^2$ has radius $1$ and converges at every point of $S^1$; $\frac1{1+z}=\sum_{n\ge0}(-1)^nz^n$ has radius $1$ and is analytic at $1$, while $\sum(-1)^n$ diverges; and $f$ cannot be analytic at every point of $S^1$.

::: pf-proof
The first series converges absolutely on $S^1$ since $\sum1/n^2<\infty$, and its radius is $1$ by the root test. For the last claim, suppose $f$ extends holomorphically to a disk about each point of $S^1$. By compactness, finitely many such disks cover $S^1$; the extensions agree with $f$ on each disk's intersection with $\DD$, hence on overlaps by the identity theorem, so they glue with $f$ to a holomorphic function on $\abs z<1+\varepsilon$ for some $\varepsilon>0$. Its Taylor series at $0$ is $\sum a_nz^n$ and converges on that disk, contradicting radius $1$.
:::

:::

::: pf-step
(n) $\dfrac{z+1}{z(z-1)^2}=\dfrac1z-\dfrac1{z-1}+\dfrac2{(z-1)^2}$, with Laurent expansions
$$
\begin{aligned}
&\frac1z+\sum_{n\ge0}(2n+3)z^n &&(0<\abs z<1),\\
&\sum_{n\ge2}(2n-3)z^{-n} &&(\abs z>1),\\
&\frac2{w^2}-\frac1w+\sum_{n\ge0}(-1)^nw^n &&(0<\abs w<1,\ w=z-1),\\
&\frac1{w^2}+\sum_{n\ge3}(-1)^{n-1}w^{-n} &&(\abs w>1,\ w=z-1).
\end{aligned}
$$

::: pf-proof
The partial fractions follow by cover-up for the coefficients of $\frac1z$ and $\frac1{(z-1)^2}$ and by comparing $z^2$-coefficients for $\frac1{z-1}$. For $\abs z<1$, $-\frac1{z-1}=\sum z^n$ and $\frac2{(z-1)^2}=\sum2(n+1)z^n$. For $\abs z>1$, $-\frac1{z-1}=-\sum_{n\ge1}z^{-n}$ and $\frac2{(z-1)^2}=\sum_{n\ge2}2(n-1)z^{-n}$, and the $z^{-1}$ terms cancel. About $1$, $\frac1z=\frac1{1+w}$ equals $\sum(-1)^nw^n$ for $\abs w<1$ and $\sum_{n\ge1}(-1)^{n-1}w^{-n}$ for $\abs w>1$.
:::

:::

:::

:::
