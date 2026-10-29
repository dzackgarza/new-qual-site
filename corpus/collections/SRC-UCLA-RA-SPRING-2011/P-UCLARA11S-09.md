---
schema: qual/card@1
id: P-UCLARA11S-09
kind: problem
title: A bounded holomorphic function off the middle-thirds Cantor set is constant
classification: {areas: [real-analysis], topics: []}
relations: []
review: draft
---

::: {.problem}
Let $E\subset[0,1]$ be the middle-thirds Cantor set,
$$
E=\left\{\sum_{i\ge1} b_i3^{-i}: b_i\in\{0,2\}\right\}.
$$
Regarding $[0,1]$ as a subset of $\CC$, suppose
$$
f:\CC\setminus E\to\CC
$$
is holomorphic and uniformly bounded.
Show that $f$ is constant.
:::

::: {.solution}

Choose $M<\infty$ such that
$$
|f(z)|\le M
\qquad
(z\in\CC\setminus E).
$$

::: pf

::: {.pf-step #s1-1}

The Cantor set $E$ has one-dimensional Lebesgue measure zero.


::: pf-proof

At the $n$-th stage of the middle-thirds construction, $E$ is contained in the union of $2^n$ closed intervals, each of length $3^{-n}$. Hence
$$
m(E)
\le
2^n3^{-n}
=
\left(\frac23\right)^n
$$
for every $n$. Letting $n\to\infty$ gives $m(E)=0$.

:::

:::

::: {.pf-step #s1-2}

For every $\varepsilon>0$, there are finitely many pairwise disjoint bounded open intervals
$$
I_j=(a_j,b_j),
\qquad
1\le j\le N,
$$
such that
$$
E\subset\bigcup_{j=1}^N I_j,
\qquad
a_j,b_j\notin E,
\qquad
\sum_{j=1}^N|I_j|<\varepsilon.
$$


::: pf-proof

By step [](#s1-1){.pf-ref} and outer regularity of Lebesgue measure, choose an open set
$$
U\supset E
$$
with
$$
m(U)<\varepsilon.
$$
Since $E$ is compact, finitely many bounded connected components of $U$ already cover $E$. Each component is an open interval whose endpoints lie outside $U$, hence outside $E$. Distinct components are disjoint, and the sum of their lengths is at most $m(U)<\varepsilon$.

If two selected intervals have touching closures, merge them into their convex hull. This does not increase the total length and does not introduce a point of $E$ at either new endpoint. After finitely many such mergers, the selected intervals have pairwise disjoint closures and therefore positive mutual distances.

:::

:::

::: {.pf-step #s1-3}

Each interval $I_j=(a_j,b_j)$ can be thickened to a closed rectangle
$$
Q_j
=
[a_j,b_j]\times[-\eta_j,\eta_j]
\subset\CC
$$
with
$$
0<\eta_j\le |I_j|,
$$
such that the rectangles are pairwise disjoint and
$$
\partial Q_j\cap E=\varnothing.
$$
Moreover,
$$
\sum_{j=1}^N\operatorname{per}(Q_j)
\le
6\sum_{j=1}^N|I_j|.
$$


::: pf-proof

By step [](#s1-2){.pf-ref}, the finitely many interval closures are pairwise disjoint, so their mutual distances are positive. Choose each $\eta_j>0$ small enough that the rectangles remain disjoint and also $\eta_j\le|I_j|$.

The horizontal sides have nonzero imaginary part and therefore miss $E\subset\RR$. The vertical sides meet the real axis only at $a_j$ and $b_j$, which lie outside $E$ by step [](#s1-2){.pf-ref}. Hence $\partial Q_j\cap E=\varnothing$.

Finally,
$$
\operatorname{per}(Q_j)
=
2|I_j|+4\eta_j
\le
6|I_j|.
$$
Summing gives the estimate.

:::

:::

::: {.pf-step #s1-4}

Fix $R>2$ and define, for $|z|<R$,
$$
F_R(z)
\coloneqq
\frac1{2\pi i}
\int_{|\zeta|=R}
\frac{f(\zeta)}{\zeta-z}\,d\zeta.
$$
Then $F_R$ is holomorphic on the disk $|z|<R$.


::: pf-proof

The circle $|\zeta|=R$ is disjoint from $E\subset[0,1]$, so $f$ is holomorphic in a neighborhood of that circle. For $|z|<R$, the Cauchy kernel is holomorphic in $z$ and uniformly bounded on compact subsets of the disk. Differentiation under the contour integral therefore shows that $F_R$ is holomorphic.

:::

:::

::: {.pf-step #s1-5}

Fix
$$
z\in B(0,R)\setminus E
$$
and set
$$
d
\coloneqq
\operatorname{dist}(z,E)>0.
$$
The intervals and rectangles in steps [](#s1-2){.pf-ref} through [](#s1-3){.pf-ref} may be chosen so that
$$
\bigcup_jQ_j
\subset
\{w:\operatorname{dist}(w,E)<d/2\}.
$$


::: pf-proof

Since $E$ is compact, its $d/2$-neighborhood is open. In step [](#s1-2){.pf-ref}, choose the finite interval cover inside the intersection of that neighborhood with the real axis, and then choose the thicknesses $\eta_j$ in step [](#s1-3){.pf-ref} sufficiently small. This keeps every rectangle inside the $d/2$-neighborhood.

:::

:::

::: {.pf-step #s1-6}

For the domain
$$
\Omega
\coloneqq
B(0,R)\setminus\bigcup_{j=1}^NQ_j,
$$
one has
$$
f(z)
=
F_R(z)
-
\frac1{2\pi i}
\sum_{j=1}^N
\int_{\partial Q_j}
\frac{f(\zeta)}{\zeta-z}\,d\zeta,
$$
where each $\partial Q_j$ is given the positive orientation as the boundary of the rectangle.


::: pf-proof

By step [](#s1-5){.pf-ref}, $z\in\Omega$. The function
$$
\zeta\longmapsto
\frac{f(\zeta)}{\zeta-z}
$$
is holomorphic on $\Omega\setminus\{z\}$ and on a neighborhood of every boundary component, because all boundaries avoid $E$.

Apply the Cauchy integral formula on the multiply connected domain $\Omega$. The positively oriented outer boundary is $|\zeta|=R$, while the boundary components of the holes occur with negative orientation relative to $\Omega$. Rewriting the latter with their own positive orientations gives exactly the displayed formula.

:::

:::

::: {.pf-step #s1-7}

The inner-boundary term in step [](#s1-6){.pf-ref} can be made arbitrarily small.


::: pf-proof

For $\zeta\in Q_j$, step [](#s1-5){.pf-ref} gives
$$
|\zeta-z|
\ge
d/2.
$$
Hence
$$
\begin{aligned}
\left|
\frac1{2\pi i}
\sum_{j=1}^N
\int_{\partial Q_j}
\frac{f(\zeta)}{\zeta-z}\,d\zeta
\right|
&\le
\frac1{2\pi}
\frac{2M}{d}
\sum_{j=1}^N
\operatorname{per}(Q_j)\\
&\le
\frac{6M}{\pi d}
\sum_{j=1}^N|I_j|.
\end{aligned}
$$
By step [](#s1-2){.pf-ref}, the final sum can be made smaller than any prescribed $\varepsilon>0$.

:::

:::

::: {.pf-step #s1-8}

For every
$$
z\in B(0,R)\setminus E,
$$
one has
$$
f(z)=F_R(z).
$$


::: pf-proof

In step [](#s1-6){.pf-ref}, choose interval covers with total length tending to zero. Step [](#s1-7){.pf-ref} shows that the inner-boundary term tends to zero, while the outer integral $F_R(z)$ is independent of the cover. Thus
$$
f(z)=F_R(z).
$$

:::

:::

::: pf-step

The function $F_R$ extends $f$ holomorphically across $E$ inside $B(0,R)$.


::: pf-proof

Step [](#s1-4){.pf-ref} says $F_R$ is holomorphic on all of $B(0,R)$, and step [](#s1-8){.pf-ref} says it agrees with $f$ on the punctured set
$$
B(0,R)\setminus E.
$$
Thus it is the desired extension.

:::

:::

::: {.pf-step #s1-10}

The function $f$ extends to a bounded entire function on $\CC$.


::: pf-proof

Fix one $R>2$. Define
$$
\widetilde f(z)
=
\begin{cases}
F_R(z),&|z|<R,\\
f(z),&|z|>1.
\end{cases}
$$
On the overlap
$$
1<|z|<R,
$$
the two definitions agree by step [](#s1-8){.pf-ref}, so they glue to an entire function on $\CC$.

Off $E$, this extension equals the original function and therefore has modulus at most $M$. Since $\CC\setminus E$ is dense and the extension is continuous, the same bound holds on $E$. Hence
$$
|\widetilde f(z)|\le M
$$
for every $z\in\CC$.

:::

:::

::: {.pf-step #s1-11}

Therefore
$$
\boxed{f\text{ is constant}.}
$$


::: pf-proof

By step [](#s1-10){.pf-ref}, $f$ has a bounded entire extension. Liouville's theorem makes that extension constant, hence the original function on $\CC\setminus E$ is constant.

:::

:::

::: pf-qed

Step [](#s1-11){.pf-ref} is the desired conclusion.

:::

:::

:::
