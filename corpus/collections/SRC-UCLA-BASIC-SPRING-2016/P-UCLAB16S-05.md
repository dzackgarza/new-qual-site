---
schema: qual/card@1
id: P-UCLAB16S-05
kind: problem
title: Lagrange multiplier condition for a constrained global minimum
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
  note: Checked against the vendored UCLA Basic Examination, Spring 2016, `assets/attachments/basic-16S.pdf`.
---

::: {.problem}
Let $f,g:\RR^2\to\RR$ be continuously differentiable.
Assume that $g$ attains the value $0$ at at least one point and that $\nabla g\ne0$ everywhere on $\RR^2$.
Suppose $(x_0,y_0)$ satisfies
\[
f(x_0,y_0)=\inf\{f(x,y):x,y\in\RR,\ g(x,y)=0\}.
\]
Show that there is $\lambda\in\RR$ such that
\[
\nabla f(x_0,y_0)=\lambda\nabla g(x_0,y_0).
\]
:::

::: {.solution}

Let
\[
p_0=(x_0,y_0).
\]

::: pf

::: {.pf-step #s1-1}

Since
\[
\nabla g(p_0)\ne0,
\]
at least one of
\[
g_x(p_0),
\qquad
g_y(p_0)
\]
is nonzero.


::: pf-proof

The gradient is
\[
\nabla g(p_0)
=
\bigl(g_x(p_0),g_y(p_0)\bigr).
\]
A vector in $\RR^2$ is nonzero exactly when at least one coordinate is nonzero.

:::

:::

::: {.pf-step #s1-2}

After interchanging the coordinate names if necessary, assume
\[
\boxed{g_y(p_0)\ne0}.
\]


::: pf-proof

Step [](#s1-1){.pf-ref} supplies a nonzero partial derivative.
If
\[
g_x(p_0)\ne0
\]
instead, the same argument below is obtained by exchanging $x$ and $y$.

:::

:::

::: {.pf-step #s1-3}

There exist an open interval
\[
I
\]
containing $x_0$ and a continuously differentiable function
\[
\phi:I\to\RR
\]
such that
\[
\phi(x_0)=y_0
\]
and
\[
\boxed{
g(x,\phi(x))=0
}
\]
for every $x\in I$.


::: pf-proof

Apply the implicit function theorem to
\[
g(x,y)=0
\]
at $(x_0,y_0)$.
The hypotheses hold because $g$ is $C^1$,
\[
g(x_0,y_0)=0,
\]
and
\[
g_y(x_0,y_0)\ne0
\]
by step [](#s1-2){.pf-ref}.

:::

:::

::: pf-step

The one-variable function
\[
h(x)
=
f(x,\phi(x))
\]
has a local minimum at
\[
x=x_0.
\]


::: pf-proof

By step [](#s1-3){.pf-ref},
\[
g(x,\phi(x))=0
\]
for every $x\in I$.
Thus every point
\[
(x,\phi(x))
\]
is feasible for the constrained minimization problem.
The hypothesis says
\[
f(x_0,y_0)
\le
f(x,\phi(x))
\]
for every $x\in I$.
Since
\[
\phi(x_0)=y_0,
\]
this means
\[
h(x_0)\le h(x)
\]
near $x_0$.

:::

:::

::: {.pf-step #s1-5}

Therefore
\[
h'(x_0)=0.
\]


::: pf-proof

The function $h$ is differentiable because both $f$ and $\phi$ are $C^1$.
A differentiable one-variable function has derivative zero at an interior local minimum.

:::

:::

::: {.pf-step #s1-6}

Differentiating the identity
\[
g(x,\phi(x))=0
\]
at $x_0$ gives
\[
\boxed{
\phi'(x_0)
=
-
\frac{g_x(p_0)}{g_y(p_0)}.
}
\]


::: pf-proof

The chain rule gives
\[
0
=
\frac d{dx}
g(x,\phi(x))
\Big|_{x=x_0}
=
g_x(p_0)
+
g_y(p_0)\phi'(x_0).
\]
Divide by
\[
g_y(p_0)\ne0.
\]

:::

:::

::: {.pf-step #s1-7}

Differentiating
\[
h(x)=f(x,\phi(x))
\]
at $x_0$ gives
\[
0
=
f_x(p_0)
+
f_y(p_0)\phi'(x_0).
\]


::: pf-proof

By the chain rule,
\[
h'(x_0)
=
f_x(p_0)
+
f_y(p_0)\phi'(x_0).
\]
Step [](#s1-5){.pf-ref} gives
\[
h'(x_0)=0.
\]

:::

:::

::: {.pf-step #s1-8}

Substituting step [](#s1-6){.pf-ref} into step [](#s1-7){.pf-ref} gives
\[
\boxed{
f_x(p_0)g_y(p_0)
-
f_y(p_0)g_x(p_0)
=
0.
}
\]


::: pf-proof

Step [](#s1-7){.pf-ref} becomes
\[
0
=
f_x(p_0)
-
f_y(p_0)
\frac{g_x(p_0)}{g_y(p_0)}.
\]
Multiply by
\[
g_y(p_0).
\]

:::

:::

::: {.pf-step #s1-9}

Define
\[
\lambda
=
\frac{f_y(p_0)}{g_y(p_0)}.
\]
Then
\[
f_y(p_0)=\lambda g_y(p_0)
\]
and
\[
f_x(p_0)=\lambda g_x(p_0).
\]


::: pf-proof

The first equality is the definition of $\lambda$.
From step [](#s1-8){.pf-ref},
\[
f_x(p_0)g_y(p_0)
=
f_y(p_0)g_x(p_0).
\]
Divide by
\[
g_y(p_0)\ne0
\]
and substitute
\[
f_y(p_0)=\lambda g_y(p_0)
\]
to obtain
\[
f_x(p_0)=\lambda g_x(p_0).
\]

:::

:::

::: {.pf-step #s1-10}

Therefore
\[
\boxed{
\nabla f(x_0,y_0)
=
\lambda\nabla g(x_0,y_0).
}
\]


::: pf-proof

Step [](#s1-9){.pf-ref} gives equality of the two coordinate components.

:::

:::

::: pf-qed

Step [](#s1-10){.pf-ref} is the required Lagrange-multiplier condition.

:::

:::

:::
