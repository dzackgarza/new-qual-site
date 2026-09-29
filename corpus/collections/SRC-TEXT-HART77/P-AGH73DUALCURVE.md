---
schema: qual/card@1
id: P-AGH73DUALCURVE
kind: problem
title: The dual curve $\dualof{Y} \subseteq \dualof{(\PP^2)}$ of a plane curve
classification:
  areas:
  - algebraic-geometry
  topics:
  - Plane Curves
  - Intersection Theory
  - Morphisms
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: Read Exercise I.7.3 together with Exercises I.5.3--I.5.4 in the Hartshorne source. Added the necessary degree-greater-than-one hypothesis for the literal I.5.4 intersection-multiplicity characterization, since self-intersection of a line with itself is not defined there. The proof characterizes tangency by the linear term of a local plane-curve equation and realizes the Gauss map by the three homogeneous partial derivatives of a defining equation.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
---

::: {.problem}
Let $Y \subseteq \PP^2$ be a curve of degree greater than one.
Regard the set of lines in $\PP^2$ as another projective space $\dualof{(\PP^2)}$, taking $(a_0, a_1, a_2)$ as homogeneous coordinates of the line
$$
L: a_0 x_0 + a_1 x_1 + a_2 x_2 = 0.
$$

For each nonsingular point $P \in Y$, show that there is a unique line $T_P(Y)$ whose intersection multiplicity with $Y$ at $P$ is $> 1$.
This is the *tangent line* to $Y$ at $P$.

Show that the map $P \mapsto T_P(Y)$ defines a morphism from $\Reg Y$, the set of nonsingular points of $Y$, into $\dualof{(\PP^2)}$.
The closure of the image of this morphism is called the *dual curve* $\dualof{Y} \subseteq \dualof{(\PP^2)}$ of $Y$.
:::

::: {.solution}
Let $F(x_0,x_1,x_2)$ be an irreducible homogeneous equation of degree $d$ for $Y$.
Write $F_i=\partial F/\partial x_i$.

::: pf

::: {.pf-step #unique-tangent-direction}
At a nonsingular point $P\in Y$, there is a unique tangent direction in the affine tangent plane.

::: pf-proof
Choose an affine chart containing $P$, translate $P$ to the origin, and let
$$
f(x,y)=f_1(x,y)+f_2(x,y)+\cdots
$$
be a local equation of the curve, decomposed into homogeneous terms.
Since $P$ is nonsingular, Exercise I.5.3 gives
$$
f_1\ne0.
$$
Thus the linear equation $f_1=0$ defines a unique line through the origin.
This is the unique tangent direction at $P$.
:::

:::

::: {.pf-step #line-multiplicity-tangent-iff}
A line $L$ through a nonsingular point $P$ has intersection multiplicity $(L.Y)_P>1$ if and only if its local linear equation is proportional to $f_1$.

::: pf-proof
Choose affine linear coordinates $(u,v)$ centered at $P$ with $L$ given by $v=0$.
Because $L$ is not a component of the irreducible curve $Y$ unless $Y=L$, the local intersection multiplicity is the order of vanishing of the restricted equation
$$
f(u,0)\in k[u]_{(u)}.
$$
Equivalently,
$$
(L.Y)_P=\operatorname{length}k[u]_{(u)}/(f(u,0)).
$$
This length is greater than one exactly when $f(u,0)$ has no nonzero linear term.

The linear term of $f(u,0)$ is the restriction of $f_1$ to $L$.
It vanishes identically exactly when $f_1$ is a scalar multiple of the equation $v$ of $L$.
Thus $(L.Y)_P>1$ exactly for the unique line $f_1=0$ from step [](#unique-tangent-direction){.pf-ref}.
:::

:::

::: {.pf-step #tangent-line-formula}
For $P=[p_0:p_1:p_2]\in\Reg Y$, the unique line of step [](#line-multiplicity-tangent-iff){.pf-ref} is
$$
\boxed{
T_P(Y):F_0(P)x_0+F_1(P)x_1+F_2(P)x_2=0}.
$$

::: pf-proof
At least one $F_i(P)$ is nonzero because $P$ is nonsingular, so the displayed equation defines a line.
Euler's identity for the homogeneous form $F$ gives
$$
\sum_{i=0}^2 p_iF_i(P)=dF(P)=0,
$$
so the line passes through $P$; this remains valid when $d=0$ in $k$ because $F(P)=0$.

On any affine chart, the linear part of the translated local equation of $Y$ at $P$ is obtained by evaluating the first derivatives of $F$ at $P$.
Hence the displayed line is precisely the line defined by that nonzero linear part.
Step [](#line-multiplicity-tangent-iff){.pf-ref} therefore shows that it is the unique line whose intersection multiplicity with $Y$ at $P$ is greater than one.
:::

:::

::: {.pf-step #gauss-map-morphism}
The assignment $P\mapsto T_P(Y)$ is a morphism
$$
\gamma:\Reg Y\dualof{\longrightarrow(\PP^2)}.
$$

::: pf-proof
In dual homogeneous coordinates, step [](#tangent-line-formula){.pf-ref} gives
$$
\gamma(P)=[F_0(P):F_1(P):F_2(P)].
$$
The three $F_i$ are homogeneous polynomials of the same degree $d-1$.
They have no common zero on $\Reg Y$, by the Jacobian criterion for nonsingularity.
Therefore these three homogeneous forms define a morphism from $\Reg Y$ to the dual projective plane.
Its value at each point is exactly the tangent line from step [](#tangent-line-formula){.pf-ref}.
:::

:::

::: {.pf-step #dual-curve-closure}
The closure of $\gamma(\Reg Y)$ is the dual algebraic set $\dualof{Y}$.

::: pf-proof
The image of the irreducible open subset $\Reg Y$ is irreducible, and its closure in the projective plane $\dualof{(\PP^2)}$ is therefore an irreducible closed subset.
By definition this closure is the dual curve $\dualof{Y}$.
:::

:::

::: pf-qed
Steps [](#unique-tangent-direction){.pf-ref}, [](#line-multiplicity-tangent-iff){.pf-ref} and [](#tangent-line-formula){.pf-ref} prove existence and uniqueness of the tangent line by intersection multiplicity, and step [](#gauss-map-morphism){.pf-ref} proves that the tangent-line assignment is a morphism.
Step [](#dual-curve-closure){.pf-ref} identifies its closure with the dual curve.
:::

:::
:::

::: {.remark title="The line case"}
Exercise I.7.3 is stated for an arbitrary plane curve, but its reference to the intersection multiplicity of Exercise I.5.4 requires the two curves to be distinct.
If $Y$ is a line, its tangent line at every point is $Y$ itself, so $(Y.Y)_P$ is not defined by I.5.4. The gradient formula in step [](#gauss-map-morphism){.pf-ref} still defines the constant tangent map, whose image is the single point of $\dualof{(\PP^2)}$ representing $Y$.
The degree-greater-than-one hypothesis above is therefore exactly what is needed for the exercise's literal intersection-multiplicity formulation.
:::
