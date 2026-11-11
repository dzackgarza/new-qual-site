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
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Read Bertram, Algebraic Geometry (Math 6130, Utah), Section 4,
    Proposition 4.3 with the paragraphs following, printed pp. 5-6, which
    proves the product of projective spaces is the product in the category
    of prevarieties via the Segre image and the local product-of-rational-
    functions formula, and derives Y x Z closed and U x V open. That closes
    part (c), which the retained sets omit. Checked the card's own steps
    against it: the two projections, local closedness, closedness, and the
    universal property on affine charts. Not checked: Bertram's graded-ring
    remark.
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

::: pf

::: {.pf-step #s1}

The two set-theoretic projections
$$
\pi_1:S\to\PP^n,
\qquad
\pi_2:S\to\PP^m
$$
are morphisms.

::: pf-proof

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

:::

::: {.pf-step #s2}

The subset $X\times Y\subseteq S$ is a quasi-projective variety, proving (a).

::: pf-proof

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
On the corresponding Segre chart $D_+(z_{ij})$, the row-and-column formulas of step [](#s1){.pf-ref} identify this open with the affine product of $U_\alpha$ and $V_\beta$.
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

:::

::: {.pf-step #s3}

If $X$ and $Y$ are projective, then $X\times Y$ is projective.

::: pf-proof

In this case $X$ is closed in $\PP^n$ and $Y$ is closed in $\PP^m$.
Therefore
$$
X\times Y=\pi_1^{-1}(X)\cap\pi_2^{-1}(Y)
$$
is closed in $S$.
The Segre variety $S$ is projective by [[P-AGH214SEGRE]], and step [](#s2){.pf-ref} gives irreducibility.
Hence $X\times Y$ is a projective variety, proving (b).

:::

:::

::: {.pf-step #s4}

The restricted projections make $X\times Y$ a categorical product of $X$ and $Y$.

::: pf-proof

The restrictions
$$
p_X:X\times Y\to X,
\qquad
p_Y:X\times Y\to Y
$$
of the morphisms in step [](#s1){.pf-ref} are morphisms by [[P-AGH310SUBVARIETY]].

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
The identification of that affine product with the corresponding Segre open is an isomorphism by the row-and-column formulas of step [](#s1){.pf-ref}.
Thus $h\restrict_W$ is a morphism.
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

:::

::: pf-qed

Steps [](#s2){.pf-ref}, [](#s3){.pf-ref} and [](#s4){.pf-ref} prove (a)--(c), respectively.

:::

:::

:::

::: {.remark title="Published solution"}
The complete published argument for (a)--(c) is Aaron Bertram, *Algebraic Geometry* (Math 6130, University of Utah), Section 4, Proposition 4.3 and the paragraphs following it, printed pp. 5--6: the Segre map "exhibits the product of projective spaces as a projective variety", the image is $V(\langle x_{ij}x_{kl}-x_{il}x_{jk}\rangle)$ with the two projections given by $\pi_1(\ldots:a_ib_j:\ldots)=(a_0b_0:\cdots:a_mb_0)$ and $\pi_2(\ldots:a_ib_j:\ldots)=(a_0b_0:\cdots:a_0b_n)$, and universality is proved by taking an open affine $U\subseteq W$ with $p_1(x)=(\varphi_0(x):\cdots:\varphi_m(x))$ and $p_2(x)=(\psi_0(x):\cdots:\psi_n(x))$ in $k(U)$, whereupon the unique set map is $f(x)=(\ldots:\varphi_i(x)\psi_j(x):\ldots)$, a morphism. For closed $Y=V(F_1,\ldots,F_a)$ and $Z=V(G_1,\ldots,G_b)$ it gives $Y\times Z=V(\langle F_i(x_{00},\ldots,x_{m0}),\ G_j(x_{00},\ldots,x_{0n})\rangle)$, and for open $U\subseteq Y$, $V\subseteq Z$ it gives $U\times V=Y\times Z-\pi_2^{-1}(Z-V)-\pi_1^{-1}(Y-U)$, which is parts (b) and (a). That is exactly the content of steps [](#s1){.pf-ref}--[](#s4){.pf-ref}: the two projections as morphisms, local closedness, closedness for projective factors, and the universal property read on affine charts.

Richard E. Borcherds, *Hartshorne, Chapter 1: Answers to exercises* (1994), gives no solution to 3.16.
William Troiani, *Hartshorne Exercise Solutions* (October 2020), Exercise 3.16, PDF p. 14: for (a) and (b) he writes $X=Z(\mathfrak a)$, $Y=Z(\mathfrak b)$ and forms, for $f_1\in\mathfrak a$ and $f_2\in\mathfrak b$, the polynomial $g(\{z_{ij}\})=\sum_{i,j}\alpha_{ij}z_{ij}$ from the expansion of $f_1(x)f_2(y)$, so that $f_1(P_1)f_2(P_2)=0$ exactly when $g(\psi(P_1,P_2))=0$; he does not treat (c).
Andrew Egbert, *Solutions to Hartshorne's Algebraic Geometry* (October 3, 2013), Exercise I.3.16, PDF p. 36: $X\times Y=(X\times\PP^m)\cap(\PP^n\times Y)=\pi_m^{-1}(X)\cap\pi_n^{-1}(Y)$, and (b) "similar", with no (c).
The proof above constructs the two ambient projections on the Segre charts first, then gets (a) as local closedness together with irreducibility chart by chart, (b) as closedness in the projective variety $S$, and (c) as the affine universal property transported along those charts; the published sets reach (a) and (b) only, and neither writes the projections as morphisms.
Bertram's Proposition 4.3 proves (c) as well, so (c) is no longer only supplied here.
:::

::: {.remark}
Part (c) is starred in the source.
:::
