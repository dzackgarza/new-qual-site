---
schema: qual/card@1
id: P-AGH410CUSPBLOWUP
kind: problem
title: Blowing up the cusp of $y^2 = x^3$ gives a bijective non-isomorphism
classification:
  areas:
  - algebraic-geometry
  topics:
  - Blowing Up
  - Plane Curves
  - Singularities
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: 'Compared the statement with the retained Hartshorne I.4.10 transcription. The proof computes both affine blowup charts, identifies the entire strict transform with the parameter t, and proves bicontinuity from finiteness while detecting failure of isomorphism on coordinate rings.'
- event: solution-written
  by: chatgpt
  date: 2026-09-17
---

::: {.problem}
Let $Y$ be the cuspidal cubic curve $y^2 = x^3$ in $\AA^2$.
Blow up the point $O = (0,0)$.
Let $E$ be the exceptional curve, and let $\tilde{Y}$ be the strict transform of $Y$.
Show that $E$ meets $\tilde{Y}$ in one point, and that $\tilde{Y} \cong \AA^1$.

In this case the morphism $\rho: \tilde{Y} \to Y$ is bijective and bicontinuous, but it is not an isomorphism.
:::

::: {.solution}
Let $B=\operatorname{Bl}_O\AA^2$.
Using homogeneous coordinates $[u:v]$ on the exceptional $\PP^1$, write
$$
B=\{((x,y),[u:v])\in\AA^2\times\PP^1:xv=yu\}.
$$
The blowup map is the projection to $(x,y)$.

<1>1. On the chart $u\ne0$, with $t=v/u$, the blowup is $\Spec k[x,t]$ with
$$
y=xt,
$$
and the strict transform of $Y$ is the curve $x=t^2$.

::: {.proof}
The equation $xv=yu$ becomes $xt=y$, so this chart is affine with coordinates $x,t$.
Substituting $y=xt$ into the cusp equation gives
$$
x^2t^2=x^3,
$$
or
$$
x^2(t^2-x)=0.
$$
Away from the exceptional divisor one has $x\ne0$, so the inverse image of $Y\setminus\{O\}$ is cut out by $t^2-x=0$.
Its closure in this chart is therefore exactly the irreducible curve $x=t^2$.
On it one also has $y=xt=t^3$.
:::

<1>2. The strict transform has no additional point in the chart $v\ne0$, and hence
$$
\boxed{\widetilde Y\cong\AA^1,\qquad
t\longmapsto((t^2,t^3),[1:t]).}
$$

::: {.proof}
On $v\ne0$, put $s=u/v$.
Then $x=ys$, and substitution into $y^2=x^3$ gives
$$
y^2=y^3s^3,
$$
so away from the exceptional divisor the strict transform satisfies
$$
1=ys^3.
$$
In particular $s\ne0$ there.
Thus every point of this chart on the strict transform lies in the overlap with $u\ne0$, where $t=1/s$.
Consequently step <1>1 already contains the entire strict transform.
The coordinate ring is
$$
k[x,t]/(x-t^2)\cong k[t],
$$
which proves the displayed isomorphism with $\AA^1$.
:::

<1>3. The exceptional curve meets $\widetilde Y$ in exactly one point.

::: {.proof}
The exceptional divisor is the inverse image of $O$, hence is given on the $u\ne0$ chart by $x=0$; then $y=xt=0$ automatically.
On the strict transform $x=t^2$, so the intersection condition is $t^2=0$, equivalently $t=0$ on the underlying variety.
Thus
$$
\boxed{E\cap\widetilde Y=\{((0,0),[1:0])\}.}
$$
Step <1>2 shows that no further intersection point occurs on the other chart.
:::

<1>4. Under the identification $\widetilde Y\cong\AA^1$, the morphism $\rho:\widetilde Y\to Y$ is
$$
t\longmapsto(t^2,t^3),
$$
and it is bijective.

::: {.proof}
The formula follows from step <1>2.
If $t\ne0$, then its image has $x=t^2\ne0$ and
$$
t=\frac yx,
$$
so distinct nonzero parameters have distinct images.
The only point mapping to the cusp $(0,0)$ is $t=0$.
Conversely, if $(x,y)\in Y$ and $x\ne0$, then $t=y/x$ satisfies
$$
t^2=\frac{y^2}{x^2}=x,
$$
and hence $t^3=tx=y$.
The cusp itself is the image of $0$.
Thus every point of $Y$ has exactly one preimage.
:::

<1>5. The bijection $\rho$ is bicontinuous but is not an isomorphism.

::: {.proof}
On coordinate rings, $\rho$ is induced by
$$
k[x,y]/(y^2-x^3)\longrightarrow k[t],
\qquad x\longmapsto t^2,\quad y\longmapsto t^3.
$$
The element $t$ is integral over the image because it satisfies the monic equation
$$
T^2-x=0.
$$
Hence $k[t]$ is finite over $k[t^2,t^3]$: it is generated as a module by $1,t$.
Therefore $\rho$ is a finite morphism and in particular a closed map.
By step <1>4 it is also bijective, so a continuous closed bijection is a homeomorphism; equivalently, $\rho$ is bicontinuous.

It is not an isomorphism because the displayed homomorphism of coordinate rings is not surjective.
Indeed $t\notin k[t^2,t^3]$: every nonconstant monomial in that subring has degree at least two as a polynomial in $t$, so no polynomial in $t^2,t^3$ equals $t$.
Thus the inverse homeomorphism is not a morphism of varieties.
:::

<1>6. Q.E.D.

::: {.proof}
Steps <1>1--<1>3 compute the strict transform and its exceptional intersection, while steps <1>4--<1>5 establish the asserted properties of $\rho$.
:::
:::
