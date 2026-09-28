---
schema: qual/card@1
id: P-AGH356QUADRICCURVES
kind: problem
title: Curves on a nonsingular quadric surface
classification:
  areas:
  - algebraic-geometry
  topics:
  - Quadric Surface
  - Divisors
  - Arithmetic Genus
  - Projective Normality
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: Compared all three parts and both ruling-line hints with the retained Hartshorne Chapter III section 5 transcription. Checked the product cohomology formula against Stacks Project section 33.29. The proof retains arbitrary fields, treats the ruling-line model after field extension when necessary, and uses the full restriction-map criterion for projective normality.
- event: solution-written
  by: chatgpt
  date: 2026-09-17
---

::: {.problem}
Let $Q$ be the nonsingular split quadric surface $xy=zw$ in $X=\PP_k^3$ over a field $k$.
We consider nonempty effective Cartier divisors $Y$ on $Q$, equivalently nonempty locally principal closed subschemes of codimension one.
Since $\Pic Q\cong\ZZ\oplus\ZZ$, we can speak of the type $(a,b)$ of $Y$ (II, 6.16 and II, 6.6.1).

Let us denote the invertible sheaf $\mcl(Y)$ by $\mco_Q(a, b)$. Thus for any $n \in \ZZ$, $\mco_Q(n)=\mco_Q(n, n)$.

(a) Use the special cases $(q,0)$ and $(0,q)$, with $q>0$, represented by disjoint unions of $q$ ruling lines after extending the field if necessary, to show:

(i) If $\abs{a-b}\le1$, then $H^1(Q,\mco_Q(a,b))=0$.

(ii) If $a,b<0$, then $H^1(Q,\mco_Q(a,b))=0$.

(iii) If $a\le-2$, then $H^1(Q,\mco_Q(a,0))\ne0$.

(b) Use these results to prove the following assertions.

(i) If $Y$ has type $(a,b)$ with $a,b>0$, then $Y$ is connected.

(ii) If $k$ is algebraically closed, then for any $a,b>0$ there is an irreducible nonsingular curve of type $(a,b)$.
Use (II, 7.6.2) and (II, 8.18).

(iii) An irreducible nonsingular curve of type $(a,b)$, with $a,b>0$, is projectively normal in $\PP_k^3$ if and only if $\abs{a-b}\le1$.
In particular, over an algebraically closed field this gives nonsingular curves that are not projectively normal, including the rational quartic of type $(1,3)$ (I, Ex. 3.18).

(c) For any nonempty effective Cartier divisor $Y$ of type $(a,b)$ on $Q$, show that
$$
p_a(Y)=ab-a-b+1.
$$
:::

::: {.hint}
For (c), calculate the Hilbert polynomials of the relevant sheaves and compare with the special case $(q,0)$ represented by $q$ disjoint ruling lines.
See (V, 1.5.2) for another method.
:::

::: {.solution}
Use the Segre identification $Q\cong\PP_k^1\times_k\PP_k^1$, whose coordinates can be taken as $x=s_0t_0$, $y=s_1t_1$, $z=s_0t_1$, $w=s_1t_0$.
Then
$$
\OO_Q(a,b)=p_1^*\OO_{\PP^1}(a)\otimes p_2^*\OO_{\PP^1}(b),
\qquad\OO_Q(1)=\OO_Q(1,1)
$$
by the Segre twisting formula [@Har10a, Exercise II.5.11].
Let $v(t)=\max(t+1,0)$ and $w(t)=\max(-t-1,0)$ for integers $t$.

<1>1. For all integers $a,b$, the cohomology dimensions and Euler characteristic are
$$
\begin{aligned}
h^0(Q,\OO_Q(a,b))&=v(a)v(b),\\
h^1(Q,\OO_Q(a,b))&=w(a)v(b)+v(a)w(b),\\
h^2(Q,\OO_Q(a,b))&=w(a)w(b),\\
\chi(\OO_Q(a,b))&=(a+1)(b+1).
\end{aligned}
$$

::: {.proof}
On $\PP_k^1$, the cohomology of $\OO(t)$ has dimensions $v(t)$ in degree zero and $w(t)$ in degree one, and vanishes in higher degrees [@Har10a, Theorem III.5.1].
Apply the [Künneth formula over a field](https://stacks.math.columbia.edu/tag/0BEC) to the two projective lines and these invertible sheaves.
It gives
$$
H^j(Q,\OO_Q(a,b))\cong
\bigoplus_{p+q=j}H^p(\PP^1,\OO(a))\otimes_k H^q(\PP^1,\OO(b)).
$$
Taking dimensions yields the first three formulas.
The alternating sum is $(v(a)-w(a))(v(b)-w(b))$, and $v(t)-w(t)=t+1$ for every integer $t$, giving the fourth formula.

The ruling-line calculation in the hint is explicit in these terms.
Choose $q$ distinct rational points of the first factor and let $D$ be their inverse image, a divisor of type $(q,0)$ consisting of $q$ disjoint projective lines.
The sequence
$$
0\to\OO_Q(-q,0)\to\OO_Q\to\OO_D\to0
$$
and $H^1(Q,\OO_Q)=0$ give
$$
H^1(Q,\OO_Q(-q,0))\cong k^q/k(1,\ldots,1),
\qquad h^1=q-1,
$$
since $H^0(Q,\OO_Q(-q,0))=0$.
Also $\chi(\OO_D)=q$ and $\chi(\OO_Q(-q,0))=1-q$.
The other ruling gives the symmetric calculation.
When $k$ has too few rational points for this choice, make it over an infinite extension field.
The cohomology base-extension comparison proved in [[P-AGH352HILBPOLY]], step <1>1, preserves these dimensions, so the numerical formulas remain valid over the original field.
:::

<1>2. All three assertions in (a) hold.

::: {.proof}
The expression for $h^1$ in step <1>1 is nonzero exactly when one index is at most $-2$ and the other is at least zero.
This follows because $w(t)>0$ exactly for $t\le-2$ and $v(t)>0$ exactly for $t\ge0$.
Such indices differ by at least two, proving (a)(i).
When both indices are negative, both $v$ terms vanish, proving (a)(ii).
For $a\le-2$ and $b=0$, the formula is $h^1=-a-1>0$, proving (a)(iii).
:::

<1>3. If $a,b>0$, every divisor $Y$ in (b)(i) is connected.

::: {.proof}
The defining effective Cartier divisor gives
$$
0\longrightarrow\OO_Q(-a,-b)\longrightarrow\OO_Q\longrightarrow\OO_Y\longrightarrow0.
$$
Step <1>1 gives $H^0(Q,\OO_Q(-a,-b))=0$, and (a)(ii) gives $H^1(Q,\OO_Q(-a,-b))=0$.
The long exact sequence therefore identifies $H^0(Y,\OO_Y)$ with $H^0(Q,\OO_Q)=k$.
A disconnected scheme has a nontrivial idempotent global function, obtained by taking values zero and one on two nonempty open-and-closed pieces.
No such idempotent exists in $k$, so $Y$ is connected, even if it is nonreduced.
:::

<1>4. Over an algebraically closed field, nonsingular irreducible divisors of every type $(a,b)$ with $a,b>0$ exist.

::: {.proof}
The product of the degree-$a$ and degree-$b$ Veronese embeddings of the two projective lines, followed by a Segre embedding, is a closed immersion whose pullback of $\OO(1)$ is $\OO_Q(a,b)$.
Thus this sheaf is very ample, as in [@Har10a, Example II.7.6.2].
Bertini's hyperplane theorem for this embedding gives a nonempty nonsingular divisor $Y$ of the required type [@Har10a, Theorem II.8.18].
Step <1>3 makes it connected.
Its regular local rings are domains, so distinct irreducible components cannot meet; the finitely many components would consequently be open and closed.
Connectedness forces only one component, and nonsingularity gives reducedness.
Hence $Y$ is irreducible and nonsingular, proving (b)(ii).
:::

<1>5. For the curve in (b)(iii), projective normality holds exactly when $\abs{a-b}\le1$.

::: {.proof}
The quadric is a positive-dimensional complete intersection, so [[P-AGH355COMPINT]] makes $H^0(\PP^3,\OO(n))\to H^0(Q,\OO_Q(n,n))$ surjective for all $n$.
For each $n\ge0$, twisting the divisor sequence gives
$$
0\to\OO_Q(n-a,n-b)\to\OO_Q(n,n)\to\OO_Y(n)\to0.
$$
Part (a)(i) makes $H^1(Q,\OO_Q(n,n))=0$.
Its long exact sequence thus identifies the cokernel of restriction from $Q$ to $Y$ with $H^1(Q,\OO_Q(n-a,n-b))$.
The first restriction, from projective space to $Q$, is already surjective.
Hence restriction from projective space to $Y$ is surjective in every degree $n\ge0$ exactly when all these $H^1$ groups vanish.
The curve is integral and normal by the irreducible nonsingular hypothesis, so this is precisely projective normality by [[P-AGH2514PROJNORM]], part (d).

If $\abs{a-b}\le1$, part (a)(i) gives all the required vanishings.
If, for example, $a\ge b+2$, take $n=b>0$.
Then $(n-a,n-b)=(b-a,0)$ with $b-a\le-2$, and part (a)(iii) makes the group nonzero.
Interchanging the factors treats $b\ge a+2$.
This proves both implications in (b)(iii).
:::

<1>6. For every divisor in (c),
$$
\boxed{P_Y(n)=(a+b)(n+1)-ab,\qquad p_a(Y)=ab-a-b+1.}
$$

::: {.proof}
Twist the effective Cartier divisor sequence by $\OO_Q(n,n)$ and use Euler additivity.
Step <1>1 gives, for every integer $n$,
$$
\chi(\OO_Y(n))=(n+1)^2-(n-a+1)(n-b+1)
=(a+b)(n+1)-ab.
$$
By [[P-AGH352HILBPOLY]], this is the Hilbert polynomial for the induced embedding of the curve in $\PP^3$.
The curve has dimension one, so $p_a(Y)=1-\chi(\OO_Y)=ab-a-b+1$.
The same computation gives $\deg Y=a+b$ from the leading coefficient.
For $q$ disjoint ruling lines it gives $P_Y(n)=q(n+1)$ and $p_a(Y)=1-q$, agreeing with the hint's Euler calculation.
This proof does not require $Y$ to be integral or nonsingular.
:::

<1>7. A nonsingular irreducible curve of type $(1,3)$ over an algebraically closed field is a rational quartic and is not projectively normal.

::: {.proof}
Step <1>6 gives degree four.
Consider its projection to the second projective line.
A fibre of this projection on $Q$ is a line on which $\OO_Q(1,3)$ has degree one.
No such line is a component of this integral curve of positive type in both coordinates, so its equation restricts to a nonzero linear form on the fibre.
Thus each fibre of the restricted projection is a zero-dimensional scheme of length one.
The projection is proper and quasi-finite and hence finite [@Har10a, Exercise III.11.2]; it is nonconstant and has degree one.
A finite birational morphism onto the normal curve $\PP^1$ is an isomorphism, by integral closedness on its affine charts.
Hence the curve is isomorphic to $\PP^1$ and is rational.
Step <1>5 excludes projective normality because the two type indices differ by two.
:::

<1>8. Q.E.D.

::: {.proof}
Steps <1>1--<1>2 prove (a), steps <1>3--<1>5 prove (b), step <1>6 proves (c), and step <1>7 verifies the stated rational-quartic example.
:::
:::

::: {.remark title="The field in the ruling-line model"}
Over a finite field with $s$ elements, each ruling has only $s+1$ $k$-rational fibres, so arbitrarily many distinct lines isomorphic over $k$ to $\PP_k^1$ cannot be chosen in that ruling.
The split-quadric cohomology formulas hold over every field; the field-extension comparison in step <1>1 makes the disjoint-line model a valid computation of their numerical values in all cases.
:::
