---
schema: qual/card@1
id: P-AGH4312NODALCURVESEXIST
kind: problem
title: Existence of plane curves of degree $d$ with exactly $r$ nodes
classification:
  areas:
  - algebraic-geometry
  topics:
  - Genus
  - Embeddings
  - Curves
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Hartshorne IV.3.12 together with the generic-projection results of
    IV.3 and the plane-curve genus formula. The proof below uses the classical
    Severi deformation argument: start from a maximally nodal rational plane
    curve, prove by normalization and Riemann--Roch that its nodes impose
    independent degree-d conditions, and then smooth any prescribed subset of
    the nodes. This gives all requested pairs, including the quintic cases that
    do not arise by projecting a smooth degree-five space curve.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-18
---

::: {.problem}
For each value of $d=2,3,4,5$ and $r$ satisfying $0 \leq r \leq \frac{1}{2}(d-1)(d-2)$, show that there exists an irreducible plane curve of degree $d$ with $r$ nodes and no other singularities.
:::

::: {.solution}
Put
$$
\delta_d=\frac{(d-1)(d-2)}2.
$$

::: pf

::: {.pf-step #s1}

For every $d\geq3$ there is an integral plane curve $C_0$ of degree
$d$ having exactly $\delta_d$ nodes and no other singularities.

::: pf-proof

Let
$$
R_d\subseteq\PP^d
$$
be the degree-$d$ rational normal curve.  For $d>3$, repeatedly apply
[[P-AGH4311PROJECTIONCLOSEDIMMERSION|Exercise IV.3.11(a)]] to project from a
point outside the secant and tangent loci until $R_d$ is embedded in $\PP^3$.
Each projection is a closed immersion on the curve and pulls the hyperplane
bundle back to the preceding hyperplane bundle, so the resulting smooth
rational space curve still has degree $d$.  For $d=3$ we start directly with
the twisted cubic.

The [[T-CRVEMBP3|generic projection theorem for curves]] now gives a general
projection of this space curve to an integral plane curve
$$
C_0\subseteq\PP^2
$$
whose only singularities are nodes and whose normalization is $\PP^1$.
Projection preserves the hyperplane degree, so $\deg C_0=d$.  If $s$ is the
number of nodes, the genus-drop formula gives
$$
0
=
g(\PP^1)
=
\frac{(d-1)(d-2)}2-s.
$$
Hence
$$
s=\delta_d.
$$

:::

:::

::: {.pf-step #s2}

Let $C\subseteq\PP^2$ be any integral degree-$d$ curve having exactly
$\delta$ nodes and no other singularities, and let
$$
N=\{P_1,\ldots,P_\delta\}
$$
be its reduced node subscheme.  Then
$$
H^1\bigl(\PP^2,\mathcal I_N(d)\bigr)=0.
$$

::: pf-proof

Let
$$
\nu:\widetilde C\longrightarrow C
$$
be the normalization, and write
$$
\nu^{-1}(P_i)=\{P_i',P_i''\},
\qquad
\widetilde N=\sum_{i=1}^{\delta}(P_i'+P_i'').
$$
Put
$$
L
=
\nu^*\mco_C(d)(-\widetilde N).
$$

If $G$ is a degree-$d$ form vanishing at every node, then its restriction to
$C$, pulled back to $\widetilde C$, vanishes at both branches over every
node.  Thus restriction gives an injective map
$$
\frac{H^0(\PP^2,\mathcal I_N(d))}{kF}
\hookrightarrow
H^0(\widetilde C,L),
$$
where $F$ is an equation of $C$.  The kernel is precisely $kF$, since an
additional degree-$d$ form vanishing identically on the integral degree-$d$
curve $C$ is a scalar multiple of $F$.

The normalization has genus
$$
g
=
\frac{(d-1)(d-2)}2-\delta,
$$
while
$$
\deg L=d^2-2\delta.
$$
Consequently
$$
\deg L-(2g-2)=3d>0,
$$
so $L$ is nonspecial.  Riemann--Roch gives
$$
\begin{aligned}
h^0(\widetilde C,L)
&=d^2-2\delta+1-g\\
&=\frac{d(d+3)}2-\delta.
\end{aligned}
$$

Set
$$
\sigma=h^1(\PP^2,\mathcal I_N(d)).
$$
From
$$
0\longrightarrow\mathcal I_N(d)
\longrightarrow\mco_{\PP^2}(d)
\longrightarrow\mco_N
\longrightarrow0
$$
and $H^1(\PP^2,\mco(d))=0$, we obtain
$$
h^0(\PP^2,\mathcal I_N(d))
=
\binom{d+2}{2}-\delta+\sigma.
$$
The injection above therefore yields
$$
\frac{d(d+3)}2-\delta+\sigma
\le
\frac{d(d+3)}2-\delta.
$$
Hence $\sigma=0$, as claimed.

:::

:::

::: {.pf-step #s3}

The nodes of $C$ can be smoothed independently inside the complete
linear system of plane curves of degree $d$.

::: pf-proof

The vanishing in step [](#s2){.pf-ref} makes the evaluation map
$$
H^0(\PP^2,\mco(d))
\longrightarrow
H^0(N,\mco_N)
\cong
k^\delta
$$
surjective.

We identify this map with the differentials of the local node-smoothing
parameters.  If $F=0$ is the equation of $C$ and $G$ is a degree-$d$ form,
then the first-order deformation
$$
F+\varepsilon G=0
$$
has, at a node $P_i$, local deformation class equal to
$$
G(P_i)
\in
\frac{\mco_{\PP^2,P_i}}
     {(F,F_x,F_y)}
\cong k.
$$
Indeed an ordinary node is, after an étale change of local coordinates, the
germ $uv=0$, whose one-dimensional smoothing space has parameter in
$uv=\tau_i$.  Modulo the Jacobian ideal, a perturbing function contributes
exactly its constant value at the node.

Thus, étale-locally at $[C]$ in the projective space of degree-$d$ equations,
there is a map
$$
(\tau_1,\ldots,\tau_\delta)
:
\mathcal U\longrightarrow\AA^\delta
$$
whose $i$th coordinate is the smoothing parameter of $P_i$, and whose
differential is the displayed evaluation map.  That differential is
surjective, so the Jacobian criterion makes this map smooth at $[C]$.
After shrinking $\mathcal U$, every prescribed pattern
$$
\tau_i=0
\quad\text{or}\quad
\tau_i\ne0
$$
therefore occurs.

For $\tau_i=0$, the nearby singularity remains an ordinary node; for
$\tau_i\ne0$, it is smoothed.  Nodality is an open condition along the
zero-parameter locus.  Since $C$ has no singular points away from the
$P_i$, after shrinking once more the nearby curves acquire no new
singularities elsewhere.  Finally, geometric integrality is open in this
flat projective family, and $C$ itself is integral.  Hence the deformation
may be chosen integral while smoothing exactly any prescribed subset of the
nodes and retaining all the others as nodes.

:::

:::

::: {.pf-step #s4}

For every $d\geq3$ and every integer
$$
0\le r\le\delta_d,
$$
there is an integral plane curve of degree $d$ with exactly $r$ nodes and no
other singularities.

::: pf-proof

Start with the curve $C_0$ from step [](#s1){.pf-ref}, whose node set has cardinality
$\delta_d$.  Choose any subset of $r$ nodes to retain.  By step [](#s3){.pf-ref} there
is an integral degree-$d$ deformation in which precisely those $r$ local
smoothing parameters remain zero and every other one is nonzero.  The
resulting curve has exactly the chosen $r$ nodes and no other
singularities.

:::

:::

::: {.pf-step #s5}

The assertion also holds for $d=2$.

::: pf-proof

Here
$$
\delta_2=0.
$$
A nonsingular plane conic is irreducible and has no singularities, so it is
the required curve for the only possible value $r=0$.

:::

:::

::: pf-qed

For $d=3,4,5$, step [](#s4){.pf-ref} supplies the required curve for every
$$
0\le r\le\frac{(d-1)(d-2)}2.
$$
Step [](#s5){.pf-ref} handles $d=2$.

:::

:::

:::
