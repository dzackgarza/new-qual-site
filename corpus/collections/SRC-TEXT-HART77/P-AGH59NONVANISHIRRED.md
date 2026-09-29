---
schema: qual/card@1
id: P-AGH59NONVANISHIRRED
kind: problem
title: Nonvanishing partials force $f$ to be irreducible
classification:
  areas:
  - algebraic-geometry
  topics:
  - Plane Curves
  - Nonsingular Varieties
  - Irreducibility
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: 'Compared the statement and Ex. I.3.7 hint with the retained Hartshorne I.5.9 transcription. The source omits the necessary positive-degree/nonempty condition: a nonzero constant polynomial has empty zero set and satisfies the derivative hypothesis vacuously. The card states the intended positive-degree form and records this exception.'
- event: solution-written
  by: chatgpt
  date: 2026-09-17
---

::: {.problem}
Let $f \in k[x,y,z]$ be a homogeneous polynomial of positive degree, let $Y = Z(f) \subseteq \PP^2$ be the algebraic set defined by $f$, and suppose that for every $P \in Y$ at least one of
$$
\frac{\partial f}{\partial x}(P), \qquad \frac{\partial f}{\partial y}(P), \qquad \frac{\partial f}{\partial z}(P)
$$
is nonzero.
Show that $f$ is irreducible, and hence that $Y$ is a nonsingular variety.

*Hint:* Use (Ex. 3.7).
:::

::: {.solution}
The ground field $k$ is algebraically closed, as throughout the chapter.

::: pf

::: {.pf-step #factorization-gives-common-zero}
If $f$ has a factorization
$$
f=gh
$$
with $g,h$ homogeneous of positive degree, then there is a point
$$
P\in Z(g)\cap Z(h).
$$

::: pf-proof
Each of $Z(g)$ and $Z(h)$ is a nonempty projective plane curve.
Indeed, a nonconstant homogeneous polynomial in three variables defines a positive-dimensional projective hypersurface.
Exercise I.3.7, proved on [[P-AGH37HYPMEETS]], says that any two projective plane curves meet.
Hence their intersection contains a point $P$.
:::

:::

::: {.pf-step #common-zero-kills-partials}
At every point $P\in Z(g)\cap Z(h)$, all three first partial derivatives of $f=gh$ vanish.

::: pf-proof
For each coordinate $x_i\in\{x,y,z\}$, the product rule gives
$$
\frac{\partial f}{\partial x_i}
=
g\frac{\partial h}{\partial x_i}
+h\frac{\partial g}{\partial x_i}.
$$
At a point where $g(P)=h(P)=0$, both summands vanish.
Thus
$$
f_x(P)=f_y(P)=f_z(P)=0.
$$
Since $f(P)=0$ as well, such a point is singular on the hypersurface.
:::

:::

::: {.pf-step #f-irreducible}
The polynomial $f$ is irreducible.

::: pf-proof
Suppose instead that $f$ is reducible.
Because $f$ is homogeneous, it admits a factorization
$$
f=gh
$$
with $g,h$ homogeneous of positive degree.
To see that the factors may be taken homogeneous, factor $f$ into irreducibles in the graded UFD $k[x,y,z]$; the least- and greatest-degree terms of a product show that every irreducible factor of a homogeneous element is homogeneous.

By step [](#factorization-gives-common-zero){.pf-ref}, choose
$$
P\in Z(g)\cap Z(h).
$$
Step [](#common-zero-kills-partials){.pf-ref} makes all three first partial derivatives of $f$ vanish at $P$.
This contradicts the hypothesis of the problem.
Therefore no such factorization exists and $f$ is irreducible.
:::

:::

::: {.pf-step #y-nonsingular-variety}
The algebraic set $Y=Z(f)$ is a nonsingular projective variety.

::: pf-proof
Step [](#f-irreducible){.pf-ref} makes the principal homogeneous ideal $(f)$ prime.
Thus $Y$ is irreducible by the [[P-AGH24CORRESPONDENCE|projective ideal correspondence]], and it is nonempty because $f$ has positive degree.
Hence $Y$ is a projective variety.

For a hypersurface in $\PP^2$, the projective Jacobian criterion [[P-AGH58JACOBIANRANK]] says that a point is nonsingular exactly when the gradient has rank one, i.e. when not all of
$$
f_x,\quad f_y,\quad f_z
$$
vanish there.
This is the assumed condition at every $P\in Y$.
Thus $Y$ is nonsingular.
:::

:::

::: pf-qed
Steps [](#factorization-gives-common-zero){.pf-ref}, [](#common-zero-kills-partials){.pf-ref} and [](#f-irreducible){.pf-ref} prove irreducibility, and step [](#y-nonsingular-variety){.pf-ref} gives the asserted nonsingular-variety conclusion.
:::

:::
:::

::: {.remark title="The positive-degree hypothesis"}
The source states the exercise for an arbitrary homogeneous polynomial.
If $f\in k^\times$ is a nonzero constant, then $Z(f)=\varnothing$, so the derivative hypothesis holds vacuously, while a unit is not an irreducible polynomial.
Thus positive degree, equivalently nonemptiness in the intended hypersurface situation, is necessary for the stated conclusion.
:::
