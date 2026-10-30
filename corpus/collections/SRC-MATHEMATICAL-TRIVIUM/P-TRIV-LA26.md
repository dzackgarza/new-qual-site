---
schema: qual/card@1
id: P-TRIV-LA26
kind: problem
title: Linear transformations preserving a sphere, a light cone and a hyperboloid
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Linear Algebra, Problem 26, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Describe the linear transformations whose invariant subspaces are

(a) 3-dimensional sphere $x_1^2 + x_2^2 + x_3^2 = R^2$ in $\RR^3$,

(b) 4-dimensional cone $x_1^2 - x_2^2 - x_3^2 - x_4^2 = 0$ in $\RR^4$,

(c) n-dimensional hyperboloid $x_1^2 + \cdots + x_p^2 - x_{p+1}^2 - \cdots - x_n^2 = R^2$ in $\RR^n$.
:::

::: {.remark}
The sets in the problem are quadratic surfaces rather than linear subspaces.
The solution interprets “invariant” as setwise preservation by an invertible
linear transformation. For the null cone, setwise preservation is slightly
larger than exact preservation of the quadratic form: positive scalar
dilations also preserve the cone.
:::

::: {.solution}

::: pf

::: pf-step

Let
$$
q_E(x)=x^Tx
$$
on $\RR^3$. An invertible linear map $A$ preserves the sphere
$$
q_E(x)=R^2,
\qquad R>0,
$$
if and only if
$$
A^TA=I.
$$


::: pf-proof

If $A^TA=I$, then
$$
q_E(Ax)
=
x^TA^TAx
=
x^Tx
=
q_E(x),
$$
so every sphere centered at the origin is preserved.

Conversely, suppose the radius-$R$ sphere is preserved setwise. For every
unit vector $u$, the point $Ru$ lies on the sphere, so
$$
\norm{ARu}=R.
$$
Thus
$$
u^TA^TAu=1
$$
for every unit vector $u$, and by homogeneity
$$
x^TA^TAx=x^Tx
$$
for every $x$. Hence the symmetric matrix $A^TA-I$ has zero quadratic form
on every vector, so
$$
A^TA=I.
$$

:::

:::

::: {.pf-step #s1-2}

Therefore the transformations in part (a) are exactly
$$
\boxed{O(3)}.
$$


::: pf-proof

This is the definition of the real orthogonal group.

:::

:::

::: pf-step

For the cone in part (b), put
$$
J=
\operatorname{diag}(1,-1,-1,-1)
$$
and
$$
q(x)=x^TJx.
$$


::: pf-proof

Then the cone equation is exactly
$$
q(x)=0.
$$

:::

:::

::: {.pf-step #s1-4}

Every matrix satisfying
$$
A^TJA=J
$$
preserves the cone.


::: pf-proof

For such $A$,
$$
q(Ax)
=
x^TA^TJAx
=
x^TJx
=
q(x).
$$
Hence $q(x)=0$ if and only if $q(Ax)=0$.

:::

:::

::: {.pf-step #s1-5}

More generally, every matrix satisfying
$$
A^TJA=cJ
$$
with $c>0$ preserves the cone setwise.


::: pf-proof

Then
$$
q(Ax)=c,q(x),
$$
so the zero set of $q$ is unchanged. Such a matrix can be written
$$
A=\sqrt c,L
$$
with
$$
L^TJL=J.
$$

:::

:::

::: {.pf-step #s1-6}

Conversely, if an invertible $A$ preserves the cone setwise, then
$$
A^TJA=cJ
$$
for some $c>0$.


::: pf-proof

Define the quadratic form
$$
r(x)=q(Ax)=x^TA^TJAx.
$$
Setwise cone preservation says
$$
r(x)=0
\iff
q(x)=0.
$$
For nondegenerate indefinite quadratic forms in dimension at least $3$, two
real quadratic forms with the same null cone are proportional. Hence
$$
r=cq,
$$
equivalently
$$
A^TJA=cJ.
$$
Because congruent real symmetric matrices have the same inertia,
$A^TJA$ has signature $(1,3)$. The form $cJ$ has that same signature only
when $c>0$.

:::

:::

::: {.pf-step #s1-7}

Thus the exact form-preserving transformations in part (b) are
$$
\boxed{O(1,3)},
$$
while all invertible setwise cone-preserving transformations form
$$
\boxed{\RR_{>0}\cdot O(1,3)}.
$$


::: pf-proof

Steps [](#s1-4){.pf-ref} through [](#s1-6){.pf-ref} give the two characterizations.

:::

:::

::: pf-step

For part (c), let
$$
J_{p,n-p}
=
\operatorname{diag}(
\underbrace{1,\ldots,1}_{p},
\underbrace{-1,\ldots,-1}_{n-p}
)
$$
and
$$
q(x)=x^TJ_{p,n-p}x.
$$


::: pf-proof

Then the hyperboloid in the problem is the level set
$$
q(x)=R^2.
$$

:::

:::

::: {.pf-step #s1-9}

Every matrix satisfying
$$
A^TJ_{p,n-p}A=J_{p,n-p}
$$
preserves the hyperboloid.


::: pf-proof

For every $x$,
$$
q(Ax)
=
x^TA^TJ_{p,n-p}Ax
=
x^TJ_{p,n-p}x
=
q(x).
$$
Hence the level set $q=R^2$ is preserved.

:::

:::

::: {.pf-step #s1-10}

Conversely, if an invertible $A$ preserves the hyperboloid
$$
q(x)=R^2
$$
setwise, then
$$
q(Ax)=q(x)
$$
for every $x$ with $q(x)>0$.


::: pf-proof

Let $x$ satisfy $q(x)>0$. Set
$$
t=\frac{R}{\sqrt{q(x)}}.
$$
Then
$$
q(tx)=t^2q(x)=R^2,
$$
so by preservation of the hyperboloid,
$$
q(A(tx))=R^2.
$$
By linearity of $A$ and homogeneity of $q$,
$$
t^2q(Ax)=R^2=t^2q(x).
$$
Since $t\neq0$,
$$
q(Ax)=q(x).
$$

:::

:::

::: {.pf-step #s1-11}

The equality
$$
q(Ax)=q(x)
$$
holds for every $x\in\RR^n$.


::: pf-proof

The difference
$$
p(x)=q(Ax)-q(x)
$$
is a polynomial in the coordinates of $x$. By step [](#s1-10){.pf-ref}, it vanishes on the
open set
$$
\{x:q(x)>0\}.
$$
A real polynomial that vanishes on a nonempty open set is identically zero.
Hence $p(x)=0$ for all $x$.

:::

:::

::: {.pf-step #s1-12}

Therefore the transformations in part (c) are exactly
$$
\boxed{O(p,n-p)}.
$$


::: pf-proof

By step [](#s1-11){.pf-ref},
$$
x^T(A^TJ_{p,n-p}A-J_{p,n-p})x=0
$$
for every $x$. The matrix in parentheses is symmetric, so it must be zero:
$$
A^TJ_{p,n-p}A=J_{p,n-p}.
$$
This is the defining relation for $O(p,n-p)$. Step [](#s1-9){.pf-ref} proves the converse.

:::

:::

::: pf-qed

Step [](#s1-2){.pf-ref} solves part (a), step [](#s1-7){.pf-ref} solves part (b), and step [](#s1-12){.pf-ref} solves
part (c).

:::

:::

:::
