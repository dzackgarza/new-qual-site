---
schema: qual/card@1
id: P-HCAO32
kind: problem
title: Ideal and Hilbert polynomial of the twisted cubic
classification:
  areas:
  - algebra
  topics:
  - Gröbner Bases
  - Polynomial Ideals
  - Hilbert Polynomials
  - Algebraic Geometry
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
Let $X$ be the twisted cubic in $\mathbb A^3$.

a. Find $I(X)$ and show that two generators suffice.

b. Find a term order for which these two generators are not a Gröbner basis for $I(X)$, but the corresponding set of three generators is a Gröbner basis.

c. Show that
\[
\langle x^2-yw,\ xz-y^2,\ xy-zw\rangle
\]
generates the ideal of the closure $\overline X$ in $\mathbb P^3$.

d. Compute the Hilbert polynomial of $X$.
:::

::: {.solution}
Let $k$ be an algebraically closed field and
$X=\{(t,t^2,t^3):t\in k\}\subseteq\AA^3$, with coordinates $x,y,z$ on $\AA^3$
and $x,y,z,w$ on $\PP^3$.

<1>1. (a) $I(X)=\langle y-x^2,\ z-x^3\rangle$.

::: {.proof}
Both generators vanish on $X$. Conversely, let $f\in I(X)$. Substituting
$y=x^2+(y-x^2)$ and $z=x^3+(z-x^3)$ gives
$f\equiv g(x)\pmod{\langle y-x^2,z-x^3\rangle}$ with $g\in k[x]$. Then
$g(t)=f(t,t^2,t^3)=0$ for every $t\in k$, and $k$ is infinite, so $g=0$.
:::

<1>2. (b) Under graded reverse lexicographic order with $x\succ y\succ z$,
$\{y-x^2,\ z-x^3\}$ is not a Gröbner basis of $I(X)$.

::: {.proof}
The initial monomials are $x^2$ and $x^3$, which generate $(x^2)$. The element
$$
x(y-x^2)-(z-x^3)=xy-z
$$
lies in $I(X)$, and its initial monomial $xy$ is not in $(x^2)$.
:::

<1>3. (b) Under the same order, the three generators
$$
x^2-y,\qquad xy-z,\qquad xz-y^2,
$$
obtained by setting $w=1$ in the generators of part (c), form a Gröbner basis
of $I(X)$.

::: {.proof}
Each vanishes at $(t,t^2,t^3)$, so each lies in $I(X)$. Their initial
monomials are $x^2$, $xy$, and $y^2$: in degree $2$, graded reverse
lexicographic order puts $y^2\succ xz$. Hence
$\langle x^2,xy,y^2\rangle\subseteq\operatorname{in}(I(X))$.

The monomials of degree at most $d$ outside $\langle x^2,xy,y^2\rangle$ are
$z^c$, $xz^c$, and $yz^c$; there are $(d+1)+d+d=3d+1$ of them.

On the other hand, the map $f\mapsto f(t,t^2,t^3)$ sends the polynomials of
degree at most $d$ onto the polynomials in $t$ of degree at most $3d$: an
exponent $e=3c+r$ with $r\in\{0,1,2\}$ is reached by $z^c$, $xz^c$, or $yz^c$.
Its kernel is $I(X)$ in degree at most $d$, so the quotient has dimension
$3d+1$. Because the order is degree-compatible, this dimension equals the
number of monomials of degree at most $d$ outside $\operatorname{in}(I(X))$.
The two monomial ideals $\langle x^2,xy,y^2\rangle\subseteq
\operatorname{in}(I(X))$ therefore have the same number of standard monomials
in each degree range, so they are equal.
:::

<1>4. (c) The closure $\overline X\subseteq\PP^3$ is
$\{[\lambda:\lambda^2:\lambda^3:1]:\lambda\in k\}\cup\{[0:0:1:0]\}$.

::: {.proof}
The morphism $\PP^1\to\PP^3$, $[s:t]\mapsto[s^2t:st^2:t^3:s^3]$, has closed
irreducible image because $\PP^1$ is proper. At $s=1$ it gives
$[t:t^2:t^3:1]$, which is $X$ in the chart $w\ne0$; at $s=0$ it gives
$[0:0:1:0]$. Since $X$ is a nonempty open subset of this irreducible image,
its closure is the whole image.
:::

<1>5. (c) The three quadrics $x^2-yw$, $xz-y^2$, $xy-zw$ are, up to sign, the
$2\times2$ minors of
$$
A=\begin{pmatrix} x & y & z \\ w & x & y \end{pmatrix},
$$
and their common zero set is $\overline X$.

::: {.proof}
The minors on columns $\{1,2\}$, $\{2,3\}$, and $\{1,3\}$ are
$\det\begin{pmatrix} x & y \\ w & x \end{pmatrix}=x^2-yw$,
$\det\begin{pmatrix} y & z \\ x & y \end{pmatrix}=y^2-xz$, and
$\det\begin{pmatrix} x & z \\ w & y \end{pmatrix}=xy-zw$.

The minors vanish exactly where $A$ has rank at most $1$. If $w\ne0$, rank $1$
means $(x,y,z)=\lambda(w,x,y)$ for some $\lambda$, so
$[x:y:z:w]=[\lambda:\lambda^2:\lambda^3:1]$. If $w=0$, the minors give
$x^2=0$ and $y^2=0$, so the point is $[0:0:1:0]$. Conversely each point of
$\overline X$ from step <1>4 makes the rows of $A$ proportional.
:::

<1>6. (c) $I(\overline X)=\langle x^2-yw,\ xz-y^2,\ xy-zw\rangle$.

::: {.proof}
The $2\times2$ minors of $A$ generate a prime ideal: this is the ideal of the
rational normal curve of degree $3$, the $2\times2$ minors of a $1$-generic
$2\times3$ matrix of linear forms. A prime ideal is radical, and by step <1>5
its zero set is $\overline X$, so by the Nullstellensatz it equals
$I(\overline X)$.
:::

<1>7. (d) The Hilbert polynomial of $X$ is $3d+1$.

::: {.proof}
The proof of step <1>3 shows that the polynomials of degree at most $d$ modulo
$I(X)$ have dimension $3d+1$ for every $d\ge0$. Equivalently, $\overline X$
is a rational curve of degree $3$, whose Hilbert polynomial is
$3d+1-0=3d+1$.
:::
:::
