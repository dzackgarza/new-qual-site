---
schema: qual/card@1
id: P-HM21B18-FIN-11
kind: problem
title: Equilibria and stability for a nonlinear planar system
classification: {areas: [applied-algebra], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: The source's phase-portrait choices A--D are image-only in the retained extraction and are not reconstructed.
---

::: {.problem}
Consider
$$
x'=x+y-xy,
\qquad
y'=x-3y+xy.
$$

(a) Find the equilibrium points.

(b) Find the Jacobian matrix at each equilibrium point.

(c) Use the Jacobian to determine the stability of each equilibrium.

(d) Choose which source phase portrait A--D belongs to the system. In the
source, portrait A has a saddle at the origin and an attracting spiral in
the first quadrant; portrait C has the spiral in the third quadrant, while
B and D do not have that saddle/first-quadrant-attracting-spiral
configuration.
:::

::: {.solution}

Write
$$
F(x,y)=x+y-xy,
\qquad
G(x,y)=x-3y+xy.
$$

::: pf

::: {.pf-step #s1-1}

The equilibrium points are
$$
(0,0)\qquad\text{and}\qquad(2,2).
$$


::: pf-proof

At an equilibrium, $F=G=0$. Adding these two equations gives
$$
2x-2y=0,
$$
so $x=y$. Substituting into $F=0$ gives
$$
2x-x^2=x(2-x)=0.
$$
Hence $x=y=0$ or $x=y=2$.

:::

:::

::: pf-step

The Jacobian matrix is
$$
J(x,y)=
\begin{pmatrix}
1-y&1-x\\
1+y&-3+x
\end{pmatrix}.
$$
Thus
$$
J(0,0)=
\begin{pmatrix}
1&1\\
1&-3
\end{pmatrix},
\qquad
J(2,2)=
\begin{pmatrix}
-1&-1\\
3&-1
\end{pmatrix}.
$$


::: pf-proof

Differentiate $F$ and $G$:
$$
F_x=1-y,\quad F_y=1-x,\quad
G_x=1+y,\quad G_y=-3+x.
$$
Evaluation at the two equilibria from step [](#s1-1){.pf-ref} gives the displayed
matrices.

:::

:::

::: {.pf-step #s1-3}

The equilibrium $(0,0)$ is unstable and is a saddle.


::: pf-proof

The characteristic polynomial of $J(0,0)$ is
$$
\lambda^2-(\operatorname{tr}J)\lambda+\det J
=\lambda^2+2\lambda-4.
$$
Its roots are
$$
\lambda=-1\pm\sqrt5.
$$
One is positive and one is negative, so the linearization is a saddle.
Because the equilibrium is hyperbolic, the nonlinear equilibrium has the
same local saddle type and is unstable.

:::

:::

::: {.pf-step #s1-4}

The equilibrium $(2,2)$ is locally asymptotically stable and is an
attracting spiral.


::: pf-proof

For $J(2,2)$,
$$
\operatorname{tr}J=-2,\qquad \det J=4,
$$
so its characteristic polynomial is
$$
\lambda^2+2\lambda+4.
$$
The eigenvalues are
$$
\lambda=-1\pm i\sqrt3,
$$
whose real parts are negative. The equilibrium is hyperbolic, so the
linearization criterion implies that the nonlinear equilibrium is locally
asymptotically stable. The nonzero imaginary parts give the spiral type.

:::

:::

::: {.pf-step #s1-5}

The source phase portrait is candidate A.


::: pf-proof

Steps [](#s1-3){.pf-ref} and [](#s1-4){.pf-ref} require a saddle at $(0,0)$ and an attracting spiral
at $(2,2)$ in the first quadrant. Among the source candidates described in
the problem, exactly portrait A has this configuration.

:::

:::

::: {.pf-step #s1-6}

Therefore
$$
\boxed{
\begin{gathered}
\text{equilibria: }(0,0),(2,2),\\
J(0,0)=\begin{pmatrix}1&1\\1&-3\end{pmatrix}
\text{ is a saddle linearization},\\
J(2,2)=\begin{pmatrix}-1&-1\\3&-1\end{pmatrix}
\text{ is an attracting-spiral linearization},\\
\text{and the phase portrait is A.}
\end{gathered}}
$$


::: pf-proof

Steps [](#s1-1){.pf-ref} through [](#s1-5){.pf-ref} establish parts (a)--(d).

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} records every requested answer.

:::

:::

:::
