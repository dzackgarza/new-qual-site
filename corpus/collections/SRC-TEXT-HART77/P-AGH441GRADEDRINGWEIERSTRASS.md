---
schema: qual/card@1
id: P-AGH441GRADEDRINGWEIERSTRASS
kind: problem
title: The section ring $\bigoplus_n H^0(\OO_X(nP))$ of an elliptic curve is a Weierstrass ring
classification:
  areas:
  - algebraic-geometry
  topics:
  - Elliptic Curves
  - Linear Systems
  - Embeddings
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Hartshorne IV.4.1 together with the genus-one Riemann--Roch setup.
    The proof below derives the weighted generators from their pole orders at
    P, proves generation and the unique degree-six relation degree by degree,
    and only then puts the resulting cubic into Legendre form. Hartshorne's
    standing convention that k is algebraically closed is used when splitting
    the cubic; characteristic two is excluded when completing the square.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-18
---

::: {.problem}
Let $X$ be an elliptic curve over $k$, with $\characteristic k \neq 2$, let $P \in X$ be a point, and let $R$ be the graded ring $R=\bigoplus_{n \geq 0} H^0(X, \OO_X(nP))$.
Show that for suitable choice of $t, x, y$
$$
R \cong k[t, x, y] /\left(y^2-x\left(x-t^2\right)\left(x-\lambda t^2\right)\right),
$$
as a graded ring, where $k[t, x, y]$ is graded by setting $\deg t=1$, $\deg x=2$, $\deg y=3$.
:::

::: {.solution}
We use Hartshorne's standing convention that $k$ is algebraically closed.
Write
$$
R_n=H^0(X,\mco_X(nP)).
$$

::: pf

::: {.pf-step #s1}

For every $n\ge1$,
$$
\dim_k R_n=n.
$$

::: pf-proof

Since $X$ has genus one, its canonical divisor is linearly equivalent to
zero.  Riemann--Roch gives
$$
\ell(nP)-\ell(-nP)=n.
$$
For $n>0$ the divisor $-nP$ has negative degree, so
$$
\ell(-nP)=0.
$$
Hence
$$
\ell(nP)=n.
$$

:::

:::

::: {.pf-step #s2}

There are homogeneous elements
$$
t\in R_1,
\qquad
x\in R_2,
\qquad
y\in R_3
$$
such that, after dehomogenizing by $t$,
$$
u=\frac{x}{t^2},
\qquad
v=\frac{y}{t^3}
$$
have poles at $P$ of exact orders $2$ and $3$, respectively.

::: pf-proof

Use the rational-function description
$$
H^0(X,\mco_X(nP))
=
\{f\in k(X):(f)+nP\ge0\}\cup\{0\}.
$$
Let $t$ denote the constant function $1$, regarded as a homogeneous element
of degree $1$.  Multiplication by $t$ realizes the natural inclusions
$$
R_{n-1}\hookrightarrow R_n.
$$

By step [](#s1){.pf-ref},
$$
\dim R_1=1,
\qquad
\dim R_2=2,
\qquad
\dim R_3=3.
$$
Choose
$$
x\in R_2\setminus kt^2.
$$
Its dehomogenization $u=x/t^2$ lies in $L(2P)$ but not in $L(P)$, so its
only pole is $P$ and that pole has exact order $2$.

Next choose
$$
y\in R_3\setminus tR_2.
$$
Then $v=y/t^3$ lies in $L(3P)$ but not in $L(2P)$, hence has exact pole
order $3$ at $P$ and no other poles.

:::

:::

::: {.pf-step #s3}

The elements $t,x,y$ generate the graded ring $R$.

::: pf-proof

For every $n\ge1$, consider the degree-$n$ elements
$$
t^n,
$$
together with
$$
x^a t^{n-2a}
\qquad
(1\le a,\ 2a\le n)
$$
and
$$
x^a y t^{n-(2a+3)}
\qquad
(0\le a,\ 2a+3\le n).
$$
After division by $t^n$, these become
$$
1,
\qquad
u^a,
\qquad
u^a v.
$$
Their pole orders at $P$ are, respectively,
$$
0,
\qquad
2a,
\qquad
2a+3.
$$
Thus their pole orders are exactly
$$
0,2,3,4,\ldots,n,
$$
with no repetition.  They are therefore linearly independent.  There are
exactly $n$ of them, and step [](#s1){.pf-ref} says $\dim_kR_n=n$.  Hence they form a
basis of $R_n$.

Every basis element is a monomial in $t,x,y$, so these three elements
generate all graded pieces of $R$.

:::

:::

::: {.pf-step #s4}

After replacing $y$ by another degree-$3$ generator, there are
coefficients $a_3,a_2,a_1,a_0\in k$, with $a_3\ne0$, such that
$$
y^2
=
a_3x^3+a_2x^2t^2+a_1xt^4+a_0t^6.
$$

::: pf-proof

Step [](#s3){.pf-ref} gives the following basis of $R_6$:
$$
t^6,
\quad
xt^4,
\quad
x^2t^2,
\quad
x^3,
\quad
yt^3,
\quad
xyt.
$$
Therefore $y^2\in R_6$ has a unique expression
$$
y^2
=
a_3x^3+a_2x^2t^2+a_1xt^4+a_0t^6
+b_1xyt+b_0yt^3.
$$
The coefficient $a_3$ is nonzero: after dehomogenizing, $v^2$ has pole
order $6$, while every displayed basis term except $u^3$ has pole order at
most $5$.

Since $\characteristic k\ne2$, set
$$
y_1
=
y-\frac12\left(b_1xt+b_0t^3\right).
$$
This differs from $y$ by an element of $tR_2$, so its dehomogenization still
has exact pole order $3$ and $t,x,y_1$ still generate $R$.  Completing the
square gives
$$
y_1^2
=
a_3x^3+a_2'x^2t^2+a_1'xt^4+a_0't^6
$$
for suitable $a_2',a_1',a_0'\in k$.  Rename $y_1$ as $y$ and the primed
coefficients as $a_2,a_1,a_0$.

:::

:::

::: {.pf-step #s5}

The relation in step [](#s4){.pf-ref} is the only relation among $t,x,y$.

::: pf-proof

Let
$$
A
=
\frac{k[t,x,y]}
{\left(y^2-a_3x^3-a_2x^2t^2-a_1xt^4-a_0t^6\right)},
$$
with weights
$$
\deg t=1,
\qquad
\deg x=2,
\qquad
\deg y=3.
$$
Step [](#s4){.pf-ref} gives a surjective graded homomorphism
$$
A\longrightarrow R.
$$

Because the defining relation is monic in $y^2$, every homogeneous class in
$A_n$ is a linear combination of the monomials
$$
t^n,
\qquad
x^a t^{n-2a},
\qquad
x^a y t^{n-(2a+3)}
$$
listed in step [](#s3){.pf-ref}.  Their images in $R_n$ are the basis constructed there,
so they are linearly independent already in $A_n$.  Thus
$$
A_n\xrightarrow{\sim}R_n
$$
for every $n$, and hence
$$
A\cong R.
$$

:::

:::

::: {.pf-step #s6}

The cubic
$$
q(u)=a_3u^3+a_2u^2+a_1u+a_0
$$
has three distinct roots in $k$.

::: pf-proof

Localizing the section ring at $t$ and taking degree zero gives
$$
R[t^{-1}]_0
=
\bigcup_{n\ge0}L(nP)
=
\Gamma(X\setminus\{P\},\mco_X).
$$
The nonconstant function $u$ has pole divisor $2P$, so it defines a finite
morphism
$$
u:X\longrightarrow\PP^1
$$
with $u^{-1}(\infty)=\{P\}$ set-theoretically.  Hence
$X\setminus\{P\}=u^{-1}(\AA^1)$ is affine, and the displayed ring is its
coordinate ring.

By step [](#s5){.pf-ref} this ring is
$$
k[u,v]/\left(v^2-q(u)\right).
$$
Thus $X\setminus\{P\}$ is the affine curve
$$
v^2=q(u).
$$

The coefficient $a_3$ is nonzero by step [](#s4){.pf-ref}, so $q$ has degree $3$.
Because $k$ is algebraically closed, it splits completely.  If $\alpha$ were
a repeated root, then the point
$$
(u,v)=(\alpha,0)
$$
would satisfy both partial derivative equations
$$
2v=0,
\qquad
q'(u)=0.
$$
It would therefore be a singular point of $X\setminus\{P\}$, contrary to
the nonsingularity of the elliptic curve $X$.  Hence
$$
q(u)=a_3(u-\alpha)(u-\beta)(u-\gamma)
$$
with $\alpha,\beta,\gamma$ pairwise distinct.

:::

:::

::: {.pf-step #s7}

After homogeneous changes of the degree-$2$ and degree-$3$
generators, the relation becomes
$$
y^2=x(x-t^2)(x-\lambda t^2)
$$
with $\lambda\in k\setminus\{0,1\}$.

::: pf-proof

Set
$$
\lambda
=
\frac{\gamma-\alpha}{\beta-\alpha}
$$
and replace $x$ by
$$
x'
=
\frac{x-\alpha t^2}{\beta-\alpha}.
$$
Then the relation in step [](#s6){.pf-ref} becomes
$$
y^2
=
c\,x'(x'-t^2)(x'-\lambda t^2),
\qquad
c=a_3(\beta-\alpha)^3\ne0.
$$
Since $k$ is algebraically closed, choose $\mu\in k^\times$ with
$$
\mu^2=c.
$$
Replacing $y$ by $y'=y/\mu$ gives
$$
y'^2
=
x'(x'-t^2)(x'-\lambda t^2).
$$
The roots are distinct, so $\lambda\ne0,1$.  Renaming $x',y'$ as $x,y$
proves the asserted presentation.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref} and [](#s3){.pf-ref} construct homogeneous generators of degrees $1,2,3$.
Steps [](#s4){.pf-ref} and [](#s5){.pf-ref} determine the unique degree-$6$ relation, and steps
[](#s6){.pf-ref} and [](#s7){.pf-ref} put its cubic factor into the required Legendre form.  Therefore
$$
\boxed{
R
\cong
k[t,x,y]/\left(y^2-x(x-t^2)(x-\lambda t^2)\right)
}
$$
as graded rings.

:::

:::

:::
