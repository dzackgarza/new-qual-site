---
schema: qual/card@1
id: P-AGH56BLOWUPSING
kind: problem
title: Resolving nodes, tacnodes, and the cusp $y^3 = x^5$ by blowing up
classification:
  areas:
  - algebraic-geometry
  topics:
  - Blowing Up
  - Singularities
  - Plane Curves
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: 'Compared all four parts with the retained Hartshorne I.5.6 transcription. The affine blowup-chart calculations prove the node, tacnode, and higher-cusp assertions directly. The solution also records the characteristic-7 and characteristic-13 exception inherited from I.5.1(c): blowing up only O cannot remove those additional singular points.'
- event: solution-written
  by: chatgpt
  date: 2026-09-17
---

::: {.problem}
1. Let $Y$ be the cusp or the node among the quartics $x^2 = x^4 + y^4$, $xy = x^6 + y^6$, $x^3 = y^2 + x^4 + y^4$, $x^2y + xy^2 = x^4 + y^4$.
   Show that the curve $\tilde{Y}$ obtained by blowing up $Y$ at $O = (0,0)$ is nonsingular (cf. (4.9.1) and (Ex. 4.10)).

2. Define a *node*, also called an ordinary double point, to be a double point, that is, a point of multiplicity $2$, of a plane curve with distinct tangent directions.
   If $P$ is a node on a plane curve $Y$, show that $\varphi^{-1}(P)$ consists of two distinct nonsingular points on the blown-up curve $\tilde{Y}$.
   One says that blowing up $P$ resolves the singularity at $P$.

3. Let $P \in Y$ be the tacnode among the quartics above.
   If $\varphi: \tilde{Y} \to Y$ is the blowing-up at $P$, show that $\varphi^{-1}(P)$ is a node.
   By part 2, the tacnode is resolved by two successive blowings-up.

4. Let $Y$ be the plane curve $y^3 = x^5$, which has a higher order cusp at $O$.
   Show that $O$ is a triple point, that blowing up $O$ gives rise to a double point, and identify which kind.
   Show that one further blowing up resolves the singularity.

Note: any singular point of a plane curve can be resolved by a finite sequence of successive blowings-up (V, 3.8).
:::

::: {.solution}
For the blowup of $\AA^2$ at the origin, use homogeneous coordinates $[u:v]$ on the exceptional $\PP^1$ and the equation
$$
xv=yu.
$$
On the chart $u\ne0$, put $t=v/u$, so $y=xt$.
On the chart $v\ne0$, put $s=u/v$, so $x=ys$.
For a curve of multiplicity $m$ at the origin, substituting in either chart produces a factor $x^m$ or $y^m$; removing that exceptional factor gives the strict-transform equation.

<1>1. Blowing up the node
$$
xy=x^6+y^6
$$
separates its two branches into two nonsingular points above the origin.

::: {.proof}
On the chart $y=xt$, the equation becomes
$$
x^2t=x^6+x^6t^6,
$$
so the strict transform is
$$
h(x,t)=t-x^4(1+t^6)=0.
$$
On the exceptional divisor $x=0$, this gives $t=0$.
At $(0,0)$ one has
$$
h_t=1,
$$
so this point of the strict transform is nonsingular.

On the other chart, $x=ys$, the same calculation gives
$$
s-y^4(1+s^6)=0,
$$
with the unique exceptional point $(y,s)=(0,0)$, again nonsingular because the derivative with respect to $s$ is $1$ there.
The two points are distinct points of the exceptional $\PP^1$: they are $[u:v]=[1:0]$ and $[0:1]$, corresponding to the two tangent directions $y=0$ and $x=0$.
Away from the exceptional divisor the blowup is an isomorphism, and [[P-AGH51PLANECURVESING]] shows that the original node curve has no other singular point.
Thus its strict transform is nonsingular.
:::

<1>2. Blowing up the cusp at the origin of
$$
x^3=y^2+x^4+y^4
$$
gives a nonsingular point above the cusp.

::: {.proof}
The tangent direction is $y=0$, so use $y=xt$.
Substitution gives
$$
x^3=x^2t^2+x^4+x^4t^4,
$$
and after removing the factor $x^2$ the strict transform is
$$
h(x,t)=x-t^2-x^2(1+t^4)=0.
$$
Its intersection with the exceptional divisor $x=0$ is the single point $t=0$.
At this point
$$
h_x=1,
$$
so the strict transform is nonsingular there.

Outside the exceptional divisor the blowup is an isomorphism.
Hence the whole strict transform is nonsingular whenever the original curve has no other singular points, in particular in characteristic zero and in every characteristic other than $2,7,13$ by [[P-AGH51PLANECURVESING]].
In characteristics $7$ and $13$, the two additional singular points found on that card lie away from the origin and remain singular after this blowup.
:::

<1>3. More generally, blowing up any node produces two distinct nonsingular points above it.

::: {.proof}
Translate the node to the origin.
Its multiplicity is two and its tangent cone is the product of two distinct linear forms.
After an invertible linear change of coordinates, write
$$
f(x,y)=xy+f_3(x,y)+f_4(x,y)+\cdots,
$$
where $f_j$ is homogeneous of degree $j$.

On the chart $y=xt$,
$$
f(x,xt)
=x^2\left(t+x f_3(1,t)+x^2f_4(1,t)+\cdots\right).
$$
Thus the strict transform has equation
$$
t+x f_3(1,t)+x^2f_4(1,t)+\cdots=0.
$$
On $x=0$ it meets the exceptional divisor only at $t=0$, and the derivative with respect to $t$ equals $1$ there.
Hence that point is nonsingular.

On the chart $x=ys$, the identical argument gives one nonsingular exceptional point $s=0$.
These are the two different points of $E\cong\PP^1$ determined by the two distinct tangent lines.
There are no other points over the original node.
Therefore
$$
\boxed{\varphi^{-1}(P)=\{P_1,P_2\}}
$$
with both $P_i$ nonsingular on the strict transform, proving part (2).
:::

<1>4. Blowing up the tacnode
$$
x^2=x^4+y^4
$$
once produces a node.

::: {.proof}
The tacnode has double tangent line $x=0$, so use the chart $x=ys$.
The equation becomes
$$
y^2s^2=y^4s^4+y^4.
$$
After removing the exceptional factor $y^2$, the strict transform is
$$
h(y,s)=s^2-y^2(s^4+1)=0.
$$
Its intersection with the exceptional divisor $y=0$ is the single point $s=0$.
The lowest-degree homogeneous part of $h$ at that point is
$$
s^2-y^2=(s-y)(s+y).
$$
Because the tacnode exercise assumes $\operatorname{char}k\ne2$, these are two distinct tangent directions.
The point therefore has multiplicity two and distinct tangents: it is a node.
Step <1>3 shows that one further blowup resolves it.
This proves part (3).
:::

<1>5. The origin of
$$
Y=V(y^3-x^5)
$$
has multiplicity three, and its first blowup produces an ordinary cusp.

::: {.proof}
The first nonzero homogeneous part of $y^3-x^5$ is $y^3$, so
$$
\boxed{\mu_O(Y)=3.}
$$
Its unique tangent direction is $y=0$.
Use the chart $y=xt$.
Then
$$
y^3-x^5=x^3t^3-x^5=x^3(t^3-x^2),
$$
so the strict transform is
$$
t^3=x^2.
$$
It meets the exceptional divisor $x=0$ only at $(x,t)=(0,0)$.
The lowest-degree term there is $-x^2$, so the new point has multiplicity two and a double tangent.
Its equation is the ordinary cusp form
$$
x^2=t^3.
$$
Thus the triple point becomes a cuspidal double point after one blowup.
:::

<1>6. A second blowup resolves the cusp from step <1>5.

::: {.proof}
For the cusp $t^3=x^2$, the tangent line is $x=0$.
On the blowup chart adapted to that tangent, put
$$
x=ts.
$$
Then
$$
t^3-x^2=t^3-t^2s^2=t^2(t-s^2).
$$
After removing the exceptional factor, the strict transform is
$$
t=s^2.
$$
This is nonsingular everywhere; at its unique exceptional point $(t,s)=(0,0)$ the derivative of $t-s^2$ with respect to $t$ is $1$.
Away from that point the blowup is an isomorphism and the preceding strict transform had no other singular point.
Hence the second blowup resolves the singularity, completing part (4).
:::

<1>7. Q.E.D.

::: {.proof}
Steps <1>1--<1>2 establish the requested explicit node and cusp calculations in part (1), with the necessary characteristic qualification for the cusp quartic.
Step <1>3 proves the general node statement in part (2), step <1>4 proves part (3), and steps <1>5--<1>6 prove part (4).
:::
:::

::: {.remark title="Characteristic exception inherited from Exercise I.5.1"}
Under only the source's assumption $\operatorname{char}k\ne2$, the cusp quartic in part (1) has two additional singular points in characteristics $7$ and $13$.
Blowing up the origin is an isomorphism near those points, so it cannot make the entire strict transform nonsingular in those characteristics.
The chart computation in step <1>2 proves that the singularity over the origin itself is resolved in every characteristic different from $2$; the global nonsingularity assertion requires excluding $7$ and $13$ as well.
:::
