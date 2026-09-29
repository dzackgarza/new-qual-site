---
schema: qual/card@1
id: P-AGH266CUBICGRP
kind: problem
title: The group law on a nonsingular plane cubic
classification:
  areas:
  - algebraic-geometry
  topics:
  - Elliptic Curves
  - Group Law
  - Inflection Points
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: Read Exercise II.6.6 and Example II.6.10.2 in the Hartshorne transcription. Retained characteristic different from two, made intersection multiplicities explicit, and corrected the exact-order assertions at the identity. The rational-point computation includes a complete integer descent excluding a right triangle of square area.
- event: solution-written
  by: chatgpt
  date: 2026-09-17
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-17
---

::: {.problem}
Let $k$ be an algebraically closed field of characteristic different from two, and let
$$
X=V(y^2z-x^3+xz^2)\subseteq\PP_k^2,\qquad O=[0:1:0].
$$
Give this nonsingular cubic the group law of Example II.6.10.2, with identity $O$.

(a) Show that three points $P,Q,R$, counted with intersection multiplicities, are cut out by a line if and only if $P+Q+R=O$ in the group law.
Thus for three distinct points this is the usual collinearity criterion; a repeated point requires the corresponding tangency.

(b) Show that $2P=O$ if and only if the tangent line at $P$ contains $O$.
Consequently a point $P\ne O$ has exact order two if and only if its tangent contains $O$.

(c) Show that $3P=O$ if and only if $P$ is an inflection point.
Here an \dfn{inflection point} is a nonsingular point whose tangent line has intersection multiplicity at least three with the curve.
Consequently a point $P\ne O$ has exact order three if and only if it is an inflection point.

(d) For $k=\CC$, show that the points admitting homogeneous coordinates in $\QQ$ form a subgroup $X(\QQ)\subseteq X(\CC)$, and determine that subgroup explicitly.
:::

::: {.solution}
For divisor sums, write $[P]$ for the point divisor; write $+$ and integer multiples without brackets for the group law on points.
The group law is transported along the following bijection [@Har10a, Example II.6.10.2]:
$$
X(k)\longrightarrow\Cl^0(X),\qquad P\longmapsto\operatorname{cl}([P]-[O]).
$$
Here $\Cl^0(X)$ is the kernel of the [[P-AGH262DEGDIV|degree map]] on the [[D-5PQ5W|divisor class group]].

::: pf

::: {.pf-step #s1}

The tangent at $O$ cuts out $3[O]$, and every line section is linearly equivalent to $3[O]$.

::: pf-proof

For $F=y^2z-x^3+xz^2$, the partial derivatives at $O$ satisfy $F_x(O)=F_y(O)=0$ and $F_z(O)=1$.
Thus the tangent line is $z=0$.
Restricting the equation to this line gives $x^3=0$, so its intersection divisor is $3[O]$.

If $L$ has linear equation $\ell=0$, the ratio $\ell/z$ is a rational function on $X$ whose divisor is $L.X-3[O]$.
The equality follows by taking valuations of these local equations, as in [[P-AGH262DEGDIV|hyperplane restriction]].
Hence $L.X\sim3[O]$.
Every line has an effective intersection divisor of degree three, since it is not a component of the integral cubic [@Har10a, Theorem I.7.7].

:::

:::

::: {.pf-step #s2}

A line cuts out $[P]+[Q]+[R]$ if and only if $P+Q+R=O$.

::: pf-proof

If $L.X=[P]+[Q]+[R]$, step [](#s1){.pf-ref} gives
$$
\operatorname{cl}([P]-[O])+\operatorname{cl}([Q]-[O])+\operatorname{cl}([R]-[O])=0,
$$
which is precisely the stated group equation.

Conversely, suppose $P+Q+R=O$.
For $P\ne Q$, take their joining line; for $P=Q$, take the tangent at $P$.
Its intersection divisor has the form $[P]+[Q]+[T]$ for a point $T$, because its total degree is three and the chosen incidences have multiplicity at least two in total.
The forward implication gives $P+Q+T=O$.
Cancellation in the group yields $T=R$, so the line cuts out exactly the required divisor, including repeated points.
This proves part (a).

:::

:::

::: {.pf-step #s3}

Tangency through $O$ detects $2P=O$, and inflection detects $3P=O$.

::: pf-proof

Let $T_P$ be the tangent at $P$ and write
$$
T_P.X=2[P]+[R].
$$
Step [](#s2){.pf-ref} says $2P+R=O$.
For $P\ne O$, the tangent contains $O$ exactly when its remaining intersection point $R$ is $O$; this is equivalent to $2P=O$.
For $P=O$, both conditions hold by step [](#s1){.pf-ref}.

The tangent has intersection multiplicity at least three at $P$ exactly when $R=P$.
By the same group equation, this is equivalent to $3P=O$.
For $P\ne O$, the equations $2P=O$ and $3P=O$ mean exact orders two and three, respectively, since these integers are prime.
This proves parts (b)--(c).

:::

:::

::: {.pf-step #s4}

The inverse of an affine point $(a,b)$ is $(a,-b)$, and $X(\QQ)$ is a subgroup of $X(\CC)$.

::: pf-proof

The vertical line $x=az$ cuts out $[(a,b)]+[(a,-b)]+[O]$, with multiplicity two at $(a,0)$ when $b=0$.
Thus step [](#s2){.pf-ref} identifies these affine points as inverses.
The point $O$ is its own inverse.

For two rational points, their joining line, or the tangent when they coincide, has rational coefficients.
The tangent has rational coefficients because it is given by the partial derivatives of the defining polynomial at a rational point.
On this line, choose projective coordinates over $\QQ$.
The restricted cubic has two rational linear factors, counting the prescribed intersection multiplicities, so the remaining linear factor is rational too.
Its third intersection point is therefore rational.
By step [](#s2){.pf-ref}, the sum of the original points is the inverse of this third point, which is rational by the inversion formula.
Since $O$ is rational as well, this proves subgroup closure and inverses.

:::

:::

::: {.pf-step #s5}

No right triangle with positive integer side lengths has square area.

::: pf-proof

Suppose there is such a triangle, and choose one with least hypotenuse $c$, writing
$$
a^2+b^2=c^2,\qquad ab/2=d^2>0.
$$
It is primitive: otherwise dividing all three sides by their common divisor gives a smaller integer triangle whose area is a rational square and an integer, hence an integer square.
The area is an integer because an integer right triangle has an even leg, as reduction modulo four shows.
A rational square that is an integer is an integer square, by unique factorization applied to a reduced fraction.

Exactly one leg is even; exchange the legs so that $b$ is even.
Then $a,c$ are odd and relatively prime.
The integers $(c+a)/2$ and $(c-a)/2$ are relatively prime, and their product is $(b/2)^2$.
Each is therefore a square, say $m^2$ and $n^2$, with $m>n>0$.
This gives
$$
a=m^2-n^2,\qquad b=2mn,\qquad c=m^2+n^2,
$$
where $m,n$ are relatively prime and of opposite parity.
The area equation becomes
$$
mn(m-n)(m+n)=d^2.
$$
The four positive integers on the left are pairwise relatively prime.
For the last pair, their greatest common divisor divides $2$ and both are odd; all other pairs are relatively prime because $m,n$ are.
Thus each factor is a square:
$$
m=e^2,\qquad n=f^2,\qquad m+n=g^2,\qquad m-n=h^2.
$$
Both $g$ and $h$ are odd, and $g>h>0$.
Set $u=(g+h)/2$ and $v=(g-h)/2$.
These are positive integers with
$$
u^2+v^2=\frac{g^2+h^2}{2}=m=e^2,\qquad
2uv=\frac{g^2-h^2}{2}=n=f^2.
$$
The last equality implies that $f$ is even.
Hence $(u,v,e)$ is another integer right triangle, with square area
$$
uv/2=(f/2)^2>0.
$$
Its hypotenuse satisfies $e\le m<m^2+n^2=c$, contradicting the choice of $c$.

:::

:::

::: {.pf-step #s6}

The rational-point subgroup is
$$
\boxed{X(\QQ)=\{O,(-1,0),(0,0),(1,0)\}\cong(\ZZ/2\ZZ)^2}.
$$

::: pf-proof

The only point at infinity is $O$, since setting $z=0$ forces $x=0$.
For an affine rational point $(x,y)$ with $y\ne0$, define positive rational numbers
$$
A=\left|\frac{x^2-1}{y}\right|,\qquad
B=\left|\frac{2x}{y}\right|,\qquad
C=\left|\frac{x^2+1}{y}\right|.
$$
The equation $y^2=x(x^2-1)$ makes $x$ and $x^2-1$ nonzero.
Direct calculation gives $A^2+B^2=C^2$ and
$$
\frac{AB}{2}=\left|\frac{x(x^2-1)}{y^2}\right|=1.
$$
Multiplying by a common positive denominator $N$ gives an integer right triangle of area $N^2$, contradicting step [](#s5){.pf-ref}.
Thus every affine rational point has $y=0$, and then $x(x-1)(x+1)=0$.
This gives exactly the three displayed affine points, each of which lies on $X$.

By step [](#s4){.pf-ref} these three points are their own inverses, and none is $O$.
The subgroup therefore has four elements, all three nonidentity elements having order two.
Choosing any two distinct nonidentity elements gives an isomorphism from $(\ZZ/2\ZZ)^2$: their four sums are distinct and exhaust the subgroup.
This proves part (d).

:::

:::

::: pf-qed

Step [](#s2){.pf-ref} proves the collinearity criterion, step [](#s3){.pf-ref} proves the tangent and inflection criteria with the exact-order qualifications, and steps [](#s4){.pf-ref}, [](#s5){.pf-ref} and [](#s6){.pf-ref} prove subgroup closure and determine every rational point.

:::

:::

:::

::: {.remark title="The identity and repeated intersections"}
The source's exact-order assertions in parts (b)--(c) require excluding $O$ [@Har10a, Exercise II.6.6].
Indeed, the tangent at $O$ contains $O$ and has intersection divisor $3[O]$, so $O$ satisfies both geometric conditions but has order one.
The equations $2P=O$ and $3P=O$ retain the valid equivalences at every point.
In part (a), collinearity includes intersection multiplicities, as in Example II.6.10.2; merely repeating an arbitrary point on a secant does not impose tangency.
:::
