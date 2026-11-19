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
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    A retained solution read at this exercise. Read Yang Pi-Yeh, Hartshorne
    Solutions (9 June 2019), Solution 4.4.4, printed pp. 90--91,
    rendered as page images from
    tmp/sources/lfwin-hartshorne-solutions.pdf, whose PDF pages are the printed
    pages. Checked against the book: Hartshorne IV.4.4, whose printed page
    the card's earlier events record; this pass did not reopen it, and the
    comparison is against the statement the card carries. Recomputed the completed square, that $(a^2+b^2+c^2-ab-bc-ca)$ at $(a,b,c)=(\lambda,1,0)$ is $\lambda^2-\lambda+1$ and $(a-b)(b-c)(c-a)$ is $-\lambda(\lambda-1)$, hence the missing $2^8$; and the two candidate coefficients for case 7, $1728\frac{8k}{8k+27}$ against $1728\frac{k}{k+1}$ at $k=\frac{j}{1728-j}$.
    Not checked: Yang's Solutions outside printed pp. 90--91; the
    book's own page in this pass; and the printed book itself.
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    The card now carries a published-solution remark naming Yang Pi-Yeh's Solution 4.4.4 at printed pp. 90--91; it had none before. No step, statement or hypothesis of the card changes.
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

::: pf

::: {.pf-step #s1}

After completing the square, the equation becomes
$$
Y^2=x^3+Ax^2+Bx+C,
$$
where
$$
A=a_2+\frac{a_1^2}{4},\qquad
B=a_4+\frac{a_1a_3}{2},\qquad
C=a_6+\frac{a_3^2}{4}.
$$

::: pf-proof

Set
$$
Y=y+\frac{a_1x+a_3}{2}.
$$
Expanding $Y^2$ and substituting the original equation gives the displayed
cubic.  This coordinate change is defined because $\characteristic k\ne2$
and does not change the isomorphism class, hence not the $j$-invariant.

:::

:::

::: {.pf-step #s2}

Let $p(x)=x^3+Ax^2+Bx+C$ and let
$$
\Delta_p=A^2B^2-4B^3-4A^3C-27C^2+18ABC
$$
be its polynomial discriminant.  Then
$$
\boxed{j(X)=256\frac{(A^2-3B)^3}{\Delta_p}}.
$$

::: pf-proof

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

:::

::: {.pf-step #s3}

Hence $j$ is a rational function of the $a_i$ with coefficients in
$\QQ$, and if all $a_i$ lie in $k_0$, then $j\in k_0$.

::: pf-proof

Step [](#s1){.pf-ref} expresses $A,B,C$ polynomially in the $a_i$ with rational
coefficients, and step [](#s2){.pf-ref} expresses $j$ rationally in $A,B,C$ with integer
coefficients.  Since $X$ is nonsingular, $\Delta_p\ne0$.

If the $a_i$ lie in $k_0$, then $\characteristic k_0\ne2$, so $1/2$ and
$1/4$ belong to $k_0$.  Thus $A,B,C,\Delta_p$ and consequently $j$ all lie
in $k_0$.

:::

:::

::: {.pf-step #s4}

Suppose $\characteristic k_0\ne2,3$.  Then every
$\alpha\in k_0$ occurs as the $j$-invariant of an elliptic curve defined
over $k_0$.

::: pf-proof

For $\alpha=0$, take
$$
E_0:y^2=x^3+1.
$$
Its cubic discriminant is $-27\ne0$, and step [](#s2){.pf-ref} gives $j(E_0)=0$.

For $\alpha=1728$, take
$$
E_{1728}:y^2=x^3-x.
$$
Its cubic discriminant is $4\ne0$, and step [](#s2){.pf-ref} gives
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
For a cubic $x^3+ux+v$, step [](#s2){.pf-ref} becomes
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

:::

::: {.pf-step #s5}

Suppose $\characteristic k_0=3$.  Again every
$\alpha\in k_0$ occurs over $k_0$.

::: pf-proof

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

:::

::: pf-qed

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref} and [](#s3){.pf-ref} give the rational expression and descent of $j$ to the
coefficient field.  Steps [](#s4){.pf-ref} and [](#s5){.pf-ref} give an elliptic curve over $k_0$ with
every prescribed $j$-invariant $\alpha\in k_0$.

:::

:::

:::

::: {.remark title="Published solution"}
Yang Pi-Yeh, *Hartshorne Solutions* (9 June 2019), Solution 4.4.4, printed pp. 90--91, completes the square by $y\mapsto y-\frac{a_1x+a_3}{2}$, which carries the equation to $y^2=x^3+\bigl(a_2+\frac{a_1^2}{4}\bigr)x^2+\bigl(a_4+\frac{a_1a_3}{2}\bigr)x+\bigl(a_6+\frac{a_3^2}{4}\bigr)$, writes the cubic as $(x-a)(x-b)(x-c)$, and reaches $j$ in the two forms $j=2^8\frac{(\lambda^2-\lambda+1)^3}{\lambda^2(\lambda-1)^2}$ with $\lambda=\frac{a-c}{a-b}$ and $j=\frac{(a^2+b^2+c^2-ab-bc-ca)^3}{((a-b)(b-c)(c-a))^2}$; on printed p. 91 it then gives $j$ in the $a_i$, by Vieta's theorem, as one quotient of degree-six expressions, and settles existence in seven cases by characteristic and $j$, from $y^2+y=x^3$ in characteristic $2$ to $y^2=x^3+2kx+2k$ with $k=\frac{j}{1728-j}$ in characteristic $\ne2,3$. Two printed statements do not survive checking. The symmetric expression is missing the factor $2^8$: at $(a,b,c)=(\lambda,1,0)$, which is the Legendre curve itself, its numerator is $(\lambda^2-\lambda+1)^3$ and its denominator $\lambda^2(\lambda-1)^2$, so it is $\frac{1}{256}$ of the entry's own preceding expression, and the correct symmetric form is $2^8\frac{(a^2+b^2+c^2-ab-bc-ca)^3}{((a-b)(b-c)(c-a))^2}$. And case 7's curve does not carry the $j$ it is offered for: $y^2=x^3+2kx+2k$ has $j=1728\frac{8k}{8k+27}$, which under $k=\frac{j}{1728-j}$ equals $j$ only at $j=1728$; with $3kx$ in place of $2kx$ the same $k$ gives $1728\frac{k}{k+1}=j$, so the coefficient is the slip and the value of $k$ is right. Worth naming as well: the derivation of the $j$-formula divides by $2$, so cases 1 and 2, which are characteristic $2$, are separate constructions rather than instances of it.
:::
