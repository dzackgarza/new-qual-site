---
schema: qual/card@1
id: P-AGH444JINVARIANTRATIONALINCOEFFICIENTS
kind: problem
title: The $j$-invariant is a rational function of the Weierstrass coefficients over $\QQ$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Elliptic Curves
  - Curves
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Hartshorne IV.4.4 together with the definition of j in IV.4.1 and the
    Legendre reduction in IV.4.6. The proof expresses j through the
    discriminant of the cubic obtained by completing the square, then gives
    explicit models over the coefficient field for every prescribed j,
    including the characteristic-three case.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-18
---

::: {.problem}
Let $X$ be an elliptic curve in $\PP^2$ given by an equation of the form
$$
y^2+a_1 x y+a_3 y=x^3+a_2 x^2+a_4 x+a_6 .
$$
Show that the $j$-invariant is a rational function of the $a_i$, with coefficients in $\QQ$.
In particular, if the $a_i$ are all in some field $k_0 \subseteq k$, then $j \in k_0$ also.
Furthermore, for every $\alpha \in k_0$, there exists an elliptic curve defined over $k_0$ with $j$-invariant equal to $\alpha$.
:::

::: {.solution}
Throughout this section Hartshorne assumes $\characteristic k\ne2$.

<1>1. After completing the square, the equation becomes
$$
Y^2=x^3+Ax^2+Bx+C,
$$
where
$$
A=a_2+\frac{a_1^2}{4},\qquad
B=a_4+\frac{a_1a_3}{2},\qquad
C=a_6+\frac{a_3^2}{4}.
$$

::: {.proof}
Set
$$
Y=y+\frac{a_1x+a_3}{2}.
$$
Expanding $Y^2$ and substituting the original equation gives the displayed
cubic.  This coordinate change is defined because $\characteristic k\ne2$
and does not change the isomorphism class, hence not the $j$-invariant.
:::

<1>2. Let $p(x)=x^3+Ax^2+Bx+C$ and let
$$
\Delta_p=A^2B^2-4B^3-4A^3C-27C^2+18ABC
$$
be its polynomial discriminant.  Then
$$
\boxed{j(X)=256\frac{(A^2-3B)^3}{\Delta_p}}.
$$

::: {.proof}
Write
$$
p(x)=(x-r_1)(x-r_2)(x-r_3).
$$
The roots are distinct: otherwise a repeated root $r$ would make
$(r,0)$ singular on $Y^2=p(x)$.

Set
$$
x=r_1+(r_2-r_1)X.
$$
Then the three roots become $0,1,\lambda$, where
$$
\lambda=\frac{r_3-r_1}{r_2-r_1}.
$$
The right-hand side acquires the nonzero factor $(r_2-r_1)^3$.
Since $k$ is algebraically closed, choose
$s\in k^\times$ with $s^2=(r_2-r_1)^3$ and set $Y=sY'$.
Thus the curve is isomorphic to the Legendre curve
$$
Y'^2=X(X-1)(X-\lambda).
$$
Hartshorne's Legendre formula is therefore
$$
j=256\frac{(\lambda^2-\lambda+1)^3}
{\lambda^2(\lambda-1)^2}.
$$
By Vieta,
$$
r_1+r_2+r_3=-A,
\qquad
r_1r_2+r_1r_3+r_2r_3=B,
$$
and direct simplification gives
$$
\lambda^2-\lambda+1
=\frac{A^2-3B}{(r_2-r_1)^2}.
$$
Also
$$
\Delta_p=(r_1-r_2)^2(r_1-r_3)^2(r_2-r_3)^2.
$$
Substitution in the Legendre formula cancels the powers of $r_2-r_1$ and
gives the claimed expression.  Expanding the symmetric product of squared
root differences gives the displayed polynomial formula for $\Delta_p$.
:::

<1>3. Hence $j$ is a rational function of the $a_i$ with coefficients in
$\QQ$, and if all $a_i$ lie in $k_0$, then $j\in k_0$.

::: {.proof}
Step <1>1 expresses $A,B,C$ polynomially in the $a_i$ with rational
coefficients, and step <1>2 expresses $j$ rationally in $A,B,C$ with integer
coefficients.  Since $X$ is nonsingular, $\Delta_p\ne0$.

If the $a_i$ lie in $k_0$, then $\characteristic k_0\ne2$, so $1/2$ and
$1/4$ belong to $k_0$.  Thus $A,B,C,\Delta_p$ and consequently $j$ all lie
in $k_0$.
:::

<1>4. Suppose $\characteristic k_0\ne2,3$.  Then every
$\alpha\in k_0$ occurs as the $j$-invariant of an elliptic curve defined
over $k_0$.

::: {.proof}
For $\alpha=0$, take
$$
E_0:y^2=x^3+1.
$$
Its cubic discriminant is $-27\ne0$, and step <1>2 gives $j(E_0)=0$.

For $\alpha=1728$, take
$$
E_{1728}:y^2=x^3-x.
$$
Its cubic discriminant is $4\ne0$, and step <1>2 gives
$j(E_{1728})=1728$.

Now assume $\alpha\ne0,1728$ and put
$$
u=-\frac{3\alpha}{\alpha-1728},
\qquad
v=-\frac{2\alpha}{\alpha-1728}.
$$
Take
$$
E_\alpha:y^2=x^3+ux+v.
$$
For a cubic $x^3+ux+v$, step <1>2 becomes
$$
j=1728\frac{4u^3}{4u^3+27v^2}.
$$
Here
$$
4u^3+27v^2
=-
\frac{108\cdot1728\,\alpha^2}{(\alpha-1728)^3}
\ne0,
$$
so the curve is nonsingular, and direct substitution gives
$$
j(E_\alpha)=\alpha.
$$
All coefficients belong to $k_0$.
:::

<1>5. Suppose $\characteristic k_0=3$.  Again every
$\alpha\in k_0$ occurs over $k_0$.

::: {.proof}
Here $1728=0$.  For $\alpha=0$, take
$$
E_0:y^2=x^3-x.
$$
Its cubic discriminant is $4=1$, while $A^2-3B=0$, so
$$
j(E_0)=0.
$$

If $\alpha\ne0$, take
$$
E_\alpha:y^2=x^3+x^2-\alpha^{-1}.
$$
For this cubic,
$$
A=1,\qquad B=0,\qquad C=-\alpha^{-1}.
$$
Hence in characteristic $3$,
$$
A^2-3B=1,
\qquad
\Delta_p=4\alpha^{-1}=\alpha^{-1}\ne0.
$$
Therefore $E_\alpha$ is nonsingular and
$$
j(E_\alpha)
=256\frac1{\alpha^{-1}}
=\alpha,
$$
because $256=1$ in characteristic $3$.
:::

<1>6. Q.E.D.

::: {.proof}
Steps <1>1--<1>3 give the rational expression and descent of $j$ to the
coefficient field.  Steps <1>4--<1>5 give an elliptic curve over $k_0$ with
every prescribed $j$-invariant $\alpha\in k_0$.
:::
:::
