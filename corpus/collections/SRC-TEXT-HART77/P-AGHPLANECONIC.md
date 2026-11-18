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
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Lamport structure. Every part checked: (a) the substitution x -> t, y -> t^2 with the kernel computed by reducing modulo y - x^2; (b) the identification A(Z) = k[x,x^{-1}] and the unit-group argument (the units of k[t] are k^*, while A(Z) has the non-scalar unit x^{-1}); (c) that an affine change of coordinates induces an isomorphism of coordinate rings (invertibility by the inverse substitution), that an irreducible quadratic form in two variables over an algebraically closed field factors into two linear forms and one of the two cases holds, and that in each case the normalisation reaches xy - 1 or y - x^2 while checking the ideal rather than only the polynomial. Gaps filled: the case analysis did not say why q factors, nor why a proportional factor pair can be written as a square (the square root of the scalar, which needs k algebraically closed), nor why b = 0 and c' = 0 are impossible (irreducibility of f); and the closing geometric criterion is now tied to the zeros of the top-degree part on the line at infinity. The card has retained solutions and they are cited with their pages, Borcherds (PDF p. 1), Park (pp. 1-2) and Troiani (pp. 1-2), all on Exercise I.1.1. What was re-read this turn is their text versions, not the PDFs: Borcherds 1.1a identifies the coordinate ring with its subring k[x], 1.1b with k[x, 1/x] and 1.1c reports that the ring is A(Y) exactly when b^2 = 4ac; Park states D(f) as minus the determinant of the matrix of the quadratic part and lists xy - 1 for D(f) nonzero; Troiani's 1.1 factors the quadratic part into linear forms. The pagination is that recorded in the card's earlier source-checked note and was not re-measured here. The card's split on whether the quadratic part is a square is Park's discriminant criterion and the dependent-factor case of Troiani.
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
The argument is the card's own, checked against the three retained solutions cited below: **Richard E. Borcherds, *Hartshorne, Chapter 1: Answers to exercises* (1994), Exercise 1.1, PDF p. 1**; **Jinhyun Park, *Algebraic Geometry by Robin Hartshorne: Exercises solutions*, Exercise 1.1, PDF pp. 1--2**; **William Troiani, *Hartshorne Exercise Solutions* (October 2020), Exercise 1.1, PDF pp. 1--2**. The exercise is Hartshorne, *Algebraic Geometry*, §I.1 Exercise 1.1 (scan p. 22 of the retained PDF), where $k$ is algebraically closed.

Write $A(X)=k[x,y]/I(X)$ for the coordinate ring of a plane curve $X$, and $A(Y)=k[x,y]/\generators{y-x^2}$, $A(Z)=k[x,y]/\generators{xy-1}$.

::: pf

::: {.pf-step #parabola}
$A(Y)\cong k[t]$.

::: pf-proof
The $k$-algebra map $\phi:k[x,y]\to k[t]$ with $\phi(x)=t$, $\phi(y)=t^2$ kills $y-x^2$, so it factors through $A(Y)$. It is surjective because $t=\phi(x)$, and its kernel is exactly $\generators{y-x^2}$: given $h\in k[x,y]$, write $h$ as a polynomial in $y$ with coefficients in $k[x]$, $h=\sum_ia_i(x)y^i$, and replace $y$ by $x^2$ modulo $y-x^2$ to get $h\equiv\sum_ia_i(x)x^{2i}=h(x,x^2)$, which is $\phi(h)$ read in $k[t]$; so $h\in\ker\phi$ exactly when $h\in\generators{y-x^2}$. Hence $A(Y)\cong k[t]$, a polynomial ring in one variable.
:::

:::

::: {.pf-step #hyperbola}
$A(Z)\cong k[x,x^{-1}]$, and $A(Z)$ is not isomorphic to a polynomial ring in one variable.

::: pf-proof
In $k[x,x^{-1}]$ the element $x$ is a unit with inverse $x^{-1}$, so there is a $k$-algebra map $k[x,y]\to k[x,x^{-1}]$ with $x\mapsto x$, $y\mapsto x^{-1}$, and it kills $xy-1$, hence factors through $A(Z)$; it is surjective, and it is injective because $k[x,x^{-1}]=k[x]_x$ and the kernel of $k[x,y]\to k[x]_x$, $y\mapsto x^{-1}$, is generated by $xy-1$ (substituting $y=x^{-1}$ turns any relation into an identity in $k[x]_x$, and conversely $xy-1\mapsto0$). So $A(Z)\cong k[x,x^{-1}]$, in which $x^{-1}\notin k$ is a unit.
Now let $R$ be a polynomial ring $k[t]$ in one variable; its units are exactly $k^*$, since $\deg(st)=0$ forces $\deg s=\deg t=0$. The group of units of $A(Z)$ contains $x^{-1}$, which is not a scalar, so the unit groups have different cardinalities: $A(Z)^\times\supseteq\{cx^m:c\in k^*,m\in\ZZ\}$, which is infinite, while $(k[t])^\times=k^*$. An isomorphism of rings induces an isomorphism of unit groups, so $A(Z)\not\cong k[t]$.
:::

:::

::: {.pf-step #affine}
An affine change of coordinates of $\AA^2$ carries the coordinate ring of a plane curve isomorphically onto that of its image.

::: pf-proof
An affine change of coordinates is an automorphism $\psi$ of $k[x,y]$ of the form $\psi(x)=a_{11}x+a_{12}y+b_1$, $\psi(y)=a_{21}x+a_{22}y+b_2$ with $\det(a_{ij})\ne0$; such a $\psi$ is an automorphism because the inverse substitution has the same shape with the inverse matrix. If $W$ is defined by $f$ and $W'=\psi^{-1}(W)$ by $f'=\psi^{-1}(f)$, then $\psi$ maps the ideal $(f')$ onto $(f)$, so it induces an isomorphism $k[x,y]/(f')\to k[x,y]/(f)$.
:::

:::

::: {.pf-step #factor}
For an irreducible quadratic $f=q+\ell+c$, the quadratic part $q\ne0$ is a product of two linear forms, and exactly one of the following holds: $q$ is the square of a linear form, or $q$ is a product of two non-proportional linear forms.

::: pf-proof
A quadratic form in two variables over an algebraically closed field is a product of two linear forms: homogenizing, $q$ defines a homogeneous quadratic in two variables, which factors over $k$ into linear factors by the fundamental theorem of algebra applied to the dehomogenization. Write $q=L_1L_2$. If $L_1$ and $L_2$ are proportional, then $q=cL^2$ for some $L$ and $c\in k^*$, and since $k$ is algebraically closed $c$ has a square root $\sqrt c$, so $q=(\sqrt c\,L)^2$ is a square; otherwise $L_1,L_2$ are independent.
:::

:::

::: {.pf-step #caseone}
If $q$ is a product of two non-proportional linear forms, then $A(W)\cong A(Z)$.

::: pf-proof
Taking $L_1,L_2$ as coordinates, $q=xy$, so $f=xy+ax+by+c=(x+b)(y+a)+(c-ab)$. Translating $x\mapsto x-b$, $y\mapsto y-a$, an affine change of coordinates by step [](#affine){.pf-ref}, gives the polynomial $xy+c'$ with $c'=c-ab$. If $c'=0$ then $f$ would be $xy$, a product of two non-units, contradicting irreducibility; so $c'\ne0$. Since $k$ is algebraically closed there is $\lambda\in k^*$ with $\lambda^2=-c'$, and the substitution $x\mapsto\lambda x$, $y\mapsto\lambda y$ turns $xy+c'$ into $\lambda^2xy+c'=c'(1-xy)$, which generates the same ideal as $1-xy$ and hence as $xy-1$, because $c'$ is a unit. So $A(W)\cong k[x,y]/\generators{xy-1}=A(Z)$.
:::

:::

::: {.pf-step #casetwo}
If $q$ is the square of a linear form, then $A(W)\cong A(Y)$.

::: pf-proof
Taking that linear form as a coordinate, $q=x^2$, so $f=x^2+ax+by+c$. If $b=0$ then $f\in k[x]$ is a quadratic in one variable, hence a product of two linear factors over the algebraically closed $k$, contradicting irreducibility; so $b\ne0$. The assignment $x\mapsto x$, $y\mapsto-(ax+by+c)$ has linear part $\begin{pmatrix}1&0\\-a&-b\end{pmatrix}$ of determinant $-b\ne0$, hence is an affine change of coordinates by step [](#affine){.pf-ref}, and in the new coordinate $y'=-(ax+by+c)$ the polynomial reads $f=x^2-y'$. So $A(W)\cong k[x,y]/\generators{x^2-y}\cong k[x,y]/\generators{y-x^2}=A(Y)$, the last by the sign change $y\mapsto-y$.
:::

:::

::: {.pf-step #criterion}
$A(W)\cong A(Y)$ exactly when the quadratic part of $f$ is a square, that is, exactly when the projective closure of $W$ meets the line at infinity in a single point; otherwise $A(W)\cong A(Z)$ and the closure meets it in two points.

::: pf-proof
The two cases of step [](#factor){.pf-ref} are exhaustive and exclusive, and they give steps [](#casetwo){.pf-ref} and [](#caseone){.pf-ref} respectively. Geometrically, the points at infinity of the projective closure $\overline W\subseteq\PP^2$ are the zeros of the top-degree part $q$ of $f$ on the line at infinity $\{z=0\}$: in coordinates where $q=L_1L_2$, the point at infinity of the line $L_i=0$ is a zero of $q$, so $q$ a square means a single point at infinity, counted with multiplicity, and two non-proportional factors mean two distinct ones. For $f=y-x^2$ this is the single point at infinity of the parabola, and for $f=xy-1$ the two points of the hyperbola.
:::

:::

:::
:::

::: {.remark}
Part (c) is starred in the source.
:::

::: {.remark title="Published solution"}
Richard E. Borcherds, *Hartshorne, Chapter 1: Answers to exercises* (1994), Exercise 1.1, PDF p. 1, text version `tmp/sources/hartshorne-solutions-borcherds.md`: he sends any nonsingular conic to $xy+yz+zx=0$ by choosing three of its points and normalizing coordinates, reads regular functions on the conic as regular functions on $\PP^1$ minus one or two points, and reports the criterion $b^2=4ac$ for $A(W)\cong A(Y)$.
Jinhyun Park, *Algebraic Geometry by Robin Hartshorne: Exercises solutions*, Exercise 1.1, PDF pp. 1--2, text version `tmp/sources/hartshorne-solutions-park.md`: he takes the discriminant $D(f)=b^2-ac$ of the quadratic part, shows $D$ vanishes or not independently of multiplying $f$ by a unit, translating and applying a linear change of coordinates, and carries $D=0$ to $y-x^2$ and $D\neq 0$ to $xy-1$ while checking the coordinate ring only changes up to isomorphism.
William Troiani, *Hartshorne Exercise Solutions* (October 2020), Exercise 1.1, PDF pp. 1--2, text version `tmp/sources/hartshorne-solutions-troiani.md`: he factors the quadratic part into two linear forms over $\overline k=k$ and takes the cases of dependent factors, giving $y-x^2$, and independent factors, giving $xy-1$.
The proof above splits on whether the quadratic part is a square, which is Park's $D(f)=0$ and the dependent-factor case of Troiani, and normalizes both cases by an affine change of coordinates as Borcherds does projectively.
Agree.
:::
