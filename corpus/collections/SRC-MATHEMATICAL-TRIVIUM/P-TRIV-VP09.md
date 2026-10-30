---
schema: qual/card@1
id: P-TRIV-VP09
kind: problem
title: Variational principle for the biharmonic equation
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Variational Principle, Problem 9, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Consider the biharmonic equation
$$
\frac{\partial^4 f}{\partial x^4} + 2\frac{\partial^4 f}{\partial x^2\partial y^2} + \frac{\partial^4 f}{\partial y^4} = 0. \tag{15}
$$
Find a functional $J[f]$ whose extrema in a class of $C^4(\bar{D})$ functions $f = f(x, y)$ with fixed boundary conditions, $f(x, y)\restrict_{\partial D} = f_0(x, y)$, satisfy this equation.
:::

::: {.solution}

Define
$$
\boxed{
J[f]
=
\frac12
\iint_D
(\Delta f)^2
\,dx\,dy,
}
$$
where
$$
\Delta f=f_{xx}+f_{yy}.
$$

::: pf

::: pf-step

Let
$$
f_\varepsilon=f+\varepsilon\eta,
$$
where
$$
\eta\in C_c^\infty(D).
$$


::: pf-proof

A compactly supported variation vanishes in a neighborhood of the boundary,
so it preserves the prescribed boundary values of $f$.

:::

:::

::: {.pf-step #s1-2}

The first variation is
$$
\evaluated{
\frac d{d\varepsilon}
J[f_\varepsilon]
}_{\varepsilon=0}
=
\iint_D
(\Delta f)(\Delta\eta)
\,dx\,dy.
$$


::: pf-proof

Since
$$
\Delta f_\varepsilon
=
\Delta f
+
\varepsilon\Delta\eta,
$$
differentiate
$$
\frac12
(\Delta f_\varepsilon)^2
$$
with respect to $\varepsilon$ at $0$.

:::

:::

::: {.pf-step #s1-3}

Two integrations by parts give
$$
\iint_D
(\Delta f)(\Delta\eta)
\,dx\,dy
=
\iint_D
(\Delta^2 f)\eta
\,dx\,dy.
$$


::: pf-proof

Because $\eta$ is compactly supported in $D$, all boundary terms vanish. First,
$$
\iint_D
(\Delta f)(\Delta\eta)
\,dA
=
-
\iint_D
\nabla(\Delta f)\cdot\nabla\eta
\,dA.
$$
Integrating by parts once more gives
$$
-
\iint_D
\nabla(\Delta f)\cdot\nabla\eta
\,dA
=
\iint_D
\Delta(\Delta f)\eta
\,dA.
$$

:::

:::

::: {.pf-step #s1-4}

At an extremum,
$$
\iint_D
(\Delta^2 f)\eta
\,dx\,dy
=0
$$
for every
$$
\eta\in C_c^\infty(D).
$$


::: pf-proof

The first variation from step [](#s1-2){.pf-ref} must vanish for every admissible variation.
Use step [](#s1-3){.pf-ref}.

:::

:::

::: {.pf-step #s1-5}

Therefore every extremum satisfies
$$
\boxed{\Delta^2f=0}
$$
in $D$.


::: pf-proof

Apply the fundamental lemma of the calculus of variations to step [](#s1-4){.pf-ref}.

:::

:::

::: {.pf-step #s1-6}

In Cartesian coordinates,
$$
\Delta^2f
=
f_{xxxx}
+
2f_{xxyy}
+
f_{yyyy}.
$$


::: pf-proof

Expand
$$
\Delta^2f
=
(\partial_x^2+\partial_y^2)^2f.
$$
Mixed derivatives commute because $f\in C^4(\bar D)$.

:::

:::

::: {.pf-step #s1-7}

Hence the functional in the boxed formula above has the required
biharmonic Euler--Lagrange equation.


::: pf-proof

Steps [](#s1-5){.pf-ref} through [](#s1-6){.pf-ref} reproduce exactly the differential equation stated in the
problem.

:::

:::

::: pf-qed

Step [](#s1-7){.pf-ref} verifies the requested variational principle.

:::

:::

:::
