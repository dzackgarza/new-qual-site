---
schema: qual/card@1
id: P-AGH316QPPRODUCT
kind: problem
title: Products of quasi-projective varieties via the Segre embedding
classification:
  areas:
  - algebraic-geometry
  topics:
  - Products
  - Segre Embedding
  - Quasi-Projective Varieties
relations:
- kind: uses
  target: P-AGH214SEGRE
- kind: uses
  target: P-AGH315AFFPRODUCT
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: 'Compared all three parts with Hartshorne I.3.16. The proof first constructs the two ambient projections on Segre nonzero-entry charts, then uses them to identify X times Y as locally closed; affine product charts supply irreducibility and the categorical universal property.'
- event: solution-written
  by: chatgpt
  date: 2026-09-17
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-17
  note: 'Checked the Segre chart formulas, locally-closed/projective claims, and local-to-global universal morphism against the source and published discussions of I.3.16.'
---

::: {.problem}
Use the Segre embedding to identify $\PP^n \times \PP^m$ with its image, and hence give it the structure of a projective variety.
Now let $X \subseteq \PP^n$ and $Y \subseteq \PP^m$ be quasi-projective varieties, and consider $X \times Y \subseteq \PP^n \times \PP^m$.

(a) Show that $X \times Y$ is a quasi-projective variety.

(b) If $X$ and $Y$ are both projective, show that $X \times Y$ is projective.

(c) Show that $X \times Y$ is a product in the category of varieties.
:::

::: {.solution}
Let
$$
S\subseteq\PP^N,
\qquad
N=nm+n+m,
$$
be the Segre variety from [[P-AGH214SEGRE]], with homogeneous coordinates $z_{ij}=x_i y_j$.
We identify the set $\PP^n\times\PP^m$ with $S$.

<1>1. The two set-theoretic projections
$$
\pi_1:S\to\PP^n,
\qquad
\pi_2:S\to\PP^m
$$
are morphisms.

::: {.proof}
The opens
$$
D_+(z_{ij})\cap S
$$
cover $S$.
On such an open, the inverse construction in [[P-AGH214SEGRE]] recovers the first factor from the $j$th column and the second from the $i$th row:
$$
\pi_1([z_{ab}])=[z_{0j}:\cdots:z_{nj}],
$$
$$
\pi_2([z_{ab}])=[z_{i0}:\cdots:z_{im}].
$$
Because $z_{ij}\ne0$, neither displayed coordinate vector is zero.
Each formula is given by homogeneous linear forms and therefore defines a morphism on the chart.
The rank-one minor equations make these formulas agree on overlaps, so they glue to the stated morphisms.
:::

<1>2. The subset $X\times Y\subseteq S$ is a quasi-projective variety, proving (a).

::: {.proof}
Since $X\subseteq\PP^n$ and $Y\subseteq\PP^m$ are locally closed and the projections are continuous,
$$
X\times Y
=
\pi_1^{-1}(X)\cap\pi_2^{-1}(Y)
$$
is locally closed in the projective variety $S$.

It remains to check irreducibility.
Choose affine open covers $\{U_\alpha\}$ of $X$ and $\{V_\beta\}$ of $Y$, refined so that each $U_\alpha$ lies in a standard affine chart of $\PP^n$ and each $V_\beta$ lies in a standard affine chart of $\PP^m$.
Then
$$
U_\alpha\times V_\beta
=
\pi_1^{-1}(U_\alpha)\cap\pi_2^{-1}(V_\beta)
$$
is open in $X\times Y$.
On the corresponding Segre chart $D_+(z_{ij})$, the row-and-column formulas of step <1>1 identify this open with the affine product of $U_\alpha$ and $V_\beta$.
It is therefore irreducible by [[P-AGH315AFFPRODUCT]].

Any two nonempty members $U_\alpha\times V_\beta$ and $U_{\alpha'}\times V_{\beta'}$ intersect: irreducibility of $X$ gives
$$
U_\alpha\cap U_{\alpha'}\ne\varnothing,
$$
and irreducibility of $Y$ gives
$$
V_\beta\cap V_{\beta'}\ne\varnothing.
$$
Moreover, their intersection is open in each product chart.
Fix one nonempty chart $U_{\alpha_0}\times V_{\beta_0}$.
For every other nonempty chart $U_\alpha\times V_\beta$, the intersection with the fixed chart is a nonempty open subset of the irreducible variety $U_\alpha\times V_\beta$, hence is dense in that chart.
Therefore every product chart is contained in the closure of the fixed irreducible chart.
The fixed chart is consequently dense in $X\times Y$, and its closure is irreducible.
Hence $X\times Y$ is irreducible.
Being irreducible and locally closed in projective space, it is quasi-projective.
:::

<1>3. If $X$ and $Y$ are projective, then $X\times Y$ is projective.

::: {.proof}
In this case $X$ is closed in $\PP^n$ and $Y$ is closed in $\PP^m$.
Therefore
$$
X\times Y=\pi_1^{-1}(X)\cap\pi_2^{-1}(Y)
$$
is closed in $S$.
The Segre variety $S$ is projective by [[P-AGH214SEGRE]], and step <1>2 gives irreducibility.
Hence $X\times Y$ is a projective variety, proving (b).
:::

<1>4. The restricted projections make $X\times Y$ a categorical product of $X$ and $Y$.

::: {.proof}
The restrictions
$$
p_X:X\times Y\to X,
\qquad
p_Y:X\times Y\to Y
$$
of the morphisms in step <1>1 are morphisms by [[P-AGH310SUBVARIETY]].

Now let $Z$ be a variety with morphisms
$$
f:Z\to X,
\qquad
g:Z\to Y.
$$
There is only one possible set map compatible with the projections:
$$
h:Z\to X\times Y,
\qquad
h(z)=(f(z),g(z)).
$$
To show that $h$ is a morphism, fix $z\in Z$.
Choose affine open neighborhoods $U\subseteq X$ of $f(z)$ and $V\subseteq Y$ of $g(z)$, each lying in a standard projective chart.
Then
$$
W=f^{-1}(U)\cap g^{-1}(V)
$$
is an open neighborhood of $z$.
On $W$, the pair $(f,g)$ lands in the affine product $U\times V$ and is a morphism by the universal property proved in [[P-AGH315AFFPRODUCT]].
The identification of that affine product with the corresponding Segre open is an isomorphism by the row-and-column formulas of step <1>1.
Thus $h|_W$ is a morphism.
Since such neighborhoods cover $Z$, $h$ is a morphism globally.

By construction
$$
p_X\circ h=f,
\qquad
p_Y\circ h=g,
$$
and uniqueness follows because these two coordinates determine every point of the Cartesian set $X\times Y$.
This proves (c).
:::

<1>5. Q.E.D.

::: {.proof}
Steps <1>2--<1>4 prove (a)--(c), respectively.
:::
:::
