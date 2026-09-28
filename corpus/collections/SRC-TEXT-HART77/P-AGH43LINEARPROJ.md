---
schema: qual/card@1
id: P-AGH43LINEARPROJ
kind: problem
title: Domain of $f = x_1/x_0$ on $\PP^2$ and of the induced map to $\PP^1$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Rational Maps
  - Projective Space
  - Regular Functions
relations:
- kind: uses
  target: P-AGH41RATFNDOM
- kind: uses
  target: P-AGH42RATMAPDOM
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: 'Compared both parts with Hartshorne I.4.3. The rational function has maximal domain D_+(x_0), while the induced projective map is [x_0:x_1] and extends to the complement of the single common zero [0:0:1].'
- event: solution-written
  by: chatgpt
  date: 2026-09-17
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-17
  note: 'Checked nonextendability of x_1/x_0 along x_0=0 and nonextendability of [x_0:x_1] at its base point using the two standard affine charts of P^1.'
---

::: {.problem}
(a) Let $f$ be the rational function on $\PP^2$ given by $f = x_1/x_0$.
Find the set of points where $f$ is defined, and describe the corresponding regular function.

(b) Now regard this function as a rational map from $\PP^2$ to $\AA^1$.
Embed $\AA^1$ in $\PP^1$, and let $\varphi: \PP^2 \dashrightarrow \PP^1$ be the resulting rational map.
Find the set of points where $\varphi$ is defined, and describe the corresponding morphism.
:::

::: {.solution}
<1>1. On the standard affine chart
$$
D_+(x_0)=\{[x_0:x_1:x_2]:x_0\ne0\},
$$
the rational function $f=x_1/x_0$ is regular.

::: {.proof}
The chart $D_+(x_0)$ is isomorphic to $\AA^2$ with affine coordinates
$$
u_1=\frac{x_1}{x_0},
\qquad
u_2=\frac{x_2}{x_0}.
$$
Under this identification, $f$ is exactly the coordinate function $u_1$.
:::

<1>2. The rational function $f$ is not regular at any point of the hyperplane $H_0=Z(x_0)$.

::: {.proof}
First let
$$
Q\in H_0\cap D_+(x_1).
$$
On the affine chart $D_+(x_1)$, the function
$$
u=\frac{x_0}{x_1}
$$
is regular and vanishes at $Q$.
If $f=x_1/x_0$ were regular near $Q$, then on the nonempty open set where both are defined we would have
$$
u f=1.
$$
Equality of regular functions would extend this identity to a neighborhood of $Q$, but evaluation at $Q$ would give $0=1$, a contradiction.

The only point of $H_0$ not covered by $D_+(x_1)$ is
$$
P=[0:0:1].
$$
On the affine chart $D_+(x_2)$ around $P$, put
$$
u=\frac{x_0}{x_2},
\qquad
v=\frac{x_1}{x_2}.
$$
Then
$$
\mco_{P,\PP^2}\cong k[u,v]_{(u,v)},
\qquad
f=\frac vu.
$$
If $v/u=a/s$ in this local ring with $s\notin(u,v)$, then
$$
v s=u a.
$$
Since $k[u,v]$ is a UFD and $u$ does not divide $v$, it must divide $s$, contradicting $s\notin(u,v)$.
Thus $f$ is not regular at $P$ either.
:::

<1>3. The maximal domain of definition of $f$ is
$$
\boxed{D(f)=D_+(x_0)\cong\AA^2},
$$
and the corresponding regular function is the affine coordinate $x_1/x_0$.

::: {.proof}
Step <1>1 gives regularity on $D_+(x_0)$, while step <1>2 excludes every point of its complement.
Maximality now follows from [[P-AGH41RATFNDOM]].
This proves (a).
:::

<1>4. After the standard embedding
$$
\AA^1\hookrightarrow\PP^1,
\qquad
t\longmapsto[1:t],
$$
the induced rational map is
$$
\varphi([x_0:x_1:x_2])=[x_0:x_1].
$$

::: {.proof}
On $D_+(x_0)$,
$$
[1:f]=\left[1:\frac{x_1}{x_0}\right]=[x_0:x_1].
$$
Thus the displayed homogeneous pair represents the same rational map.
The two linear forms $x_0,x_1$ have no common zero away from
$$
P=[0:0:1],
$$
so they define a morphism
$$
\PP^2\setminus\{P\}\longrightarrow\PP^1.
$$
:::

<1>5. The rational map $\varphi$ is not defined at $P=[0:0:1]$.

::: {.proof}
Suppose that $\varphi$ extended to a morphism on a neighborhood $W$ of $P$.
Write
$$
\varphi(P)=[a:b].
$$
At least one of $a,b$ is nonzero.

If $a\ne0$, then after shrinking $W$ we may assume the image lies in the target chart $D_+(y_0)$.
Its affine coordinate $y_1/y_0$ would pull back to a regular function near $P$.
On the dense open subset where $x_0\ne0$, that pullback is
$$
\frac{x_1}{x_0},
$$
contradicting step <1>2.

If $b\ne0$, use instead the target chart $D_+(y_1)$.
Then $y_0/y_1$ would pull back to the rational function
$$
\frac{x_0}{x_1},
$$
which is likewise not regular at $P$ by the same local-ring argument with $u$ and $v$ interchanged.
Both possibilities are impossible, so no extension exists at $P$.
:::

<1>6. Therefore
$$
\boxed{D(\varphi)=\PP^2\setminus\{[0:0:1]\}},
$$
and on this maximal domain
$$
\boxed{\varphi([x_0:x_1:x_2])=[x_0:x_1]}.
$$

::: {.proof}
Step <1>4 gives the morphism on the displayed open set, and step <1>5 proves that the only missing point cannot be added.
By [[P-AGH42RATMAPDOM]], this is the maximal domain of definition.
This proves (b).
:::

<1>7. Q.E.D.

::: {.proof}
Steps <1>1--<1>3 prove (a), and steps <1>4--<1>6 prove (b).
:::
:::
