---
schema: qual/card@1
id: P-AGHPLANECONIC
kind: problem
title: Coordinate rings of the parabola, the hyperbola, and any conic
classification:
  areas:
  - algebraic-geometry
  topics:
  - Coordinate Rings
  - Plane Curves
  - Conics
relations:
- kind: uses
  target: PR-7OT2Z
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against Hartshorne, Algebraic Geometry, §I.1 Exercise 1.1 (scan page 22
    of the retained PDF). What was checked: the printed text of (a), (b) and (c)
    against the card's statement, wording by wording. (a) and (b) agree as
    printed. (c) carries a star in the book, which the card did not record: a
    remark now says so, since a remark may note a starred question. The book's
    closing question reads "Which one is it when?", and the card read "Which one,
    and when?"; restored to the printed wording. What was not checked: the
    solution was read only for consistency with the repaired statement, not
    re-derived; no other part of §I.1 was read.
---

::: {.problem}
(a) Let $Y$ be the plane curve $y = x^2$, the zero set of $f = y - x^2$.
    Show that $A(Y)$ is isomorphic to a polynomial ring in one variable over $k$.

(b) Let $Z$ be the plane curve $xy = 1$.
    Show that $A(Z)$ is not isomorphic to a polynomial ring in one variable over $k$.

(c) Let $f$ be any irreducible quadratic polynomial in $k[x,y]$, and let $W$ be the conic it defines.
    Show that $A(W)$ is isomorphic to $A(Y)$ or to $A(Z)$.
    Which one is it when?
:::

::: {.solution}
**(a)** $A(Y) = k[x,y]/\generators{y-x^2} \cong k[t,t^2] \cong k[t]$.

**(b)** $A(Z) = k[x,y]/\generators{xy-1} \cong k[x^{\pm 1}]$.
This is not a polynomial ring: it contains the unit $\inverseof{x} \notin k$, while the units of $k[t]$ are exactly $k^*$.

**(c)** An affine change of coordinates of $\AA^2$ induces a $k$-algebra automorphism of $k[x,y]$, so it does not change $A(W)$ up to isomorphism.
Write $f = q + \ell + c$ with $q \neq 0$ a quadratic form, $\ell$ a linear form and $c \in k$.
Since $k$ is algebraically closed, $q$ is a product of two linear forms.

*Case 1: $q$ is a product of two non-proportional linear forms.* After a linear change of coordinates $q = xy$, so $f = xy + ax + by + c = (x+b)(y+a) + (c - ab)$.
Translating, $f = xy + c'$, and $c' \neq 0$ because $f$ is irreducible.
Rescaling $x$ gives $f = xy - 1$, so $A(W) \cong A(Z)$.

*Case 2: $q$ is the square of a linear form.* After a linear change of coordinates $q = x^2$, so $f = x^2 + ax + by + c$.
If $b = 0$, then $f \in k[x]$ factors into linear factors, so $b \neq 0$.
The substitution $y' = -(ax + by + c)$ is an affine change of coordinates, and it gives $f = x^2 - y'$, so $A(W) \cong A(Y)$.

So $A(W) \cong A(Y)$ exactly when the quadratic part of $f$ is a square, that is, when the projective closure of $W$ meets the line at infinity in one point, and $A(W) \cong A(Z)$ when it meets it in two points.
:::

::: {.remark}
Part (c) is starred in the source.
:::
