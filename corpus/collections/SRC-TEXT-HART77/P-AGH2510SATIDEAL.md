---
schema: qual/card@1
id: P-AGH2510SATIDEAL
kind: problem
title: Saturated ideals and closed subschemes of projective space
classification:
  areas:
  - algebraic-geometry
  topics:
  - Graded Rings
  - Closed Subschemes
  - Saturation
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: Compared all four parts with the retained MinerU transcription Hartshorne_Solutions_extracted.md, section 2.5, solution 5.10. Checked the arbitrary-base-ring localization argument and corrected part (c) in projective dimension zero to use the nonnegative section ideal; the all-degree convention agrees with it when r is positive.
- event: solution-written
  by: chatgpt
  date: 2026-09-17
---

::: {.problem}
Let $A$ be a ring, let $S = A[x_0, \ldots, x_r]$, and let $X = \Proj S$.
We have seen that a homogeneous ideal $I$ in $S$ defines a closed subscheme of $X$ (Ex. 3.12), and that conversely every closed subscheme of $X$ arises in this way (5.16).

(a) For any homogeneous ideal $I \subseteq S$, define the \dfn{saturation} $\bar I$ of $I$ to be the set of $s \in S$ such that for each $i = 0, \ldots, r$ there is an $n$ with $x_i^n s \in I$.
We say $I$ is \dfn{saturated} if $I = \bar I$.
Show that $\bar I$ is a homogeneous ideal of $S$.

(b) Two homogeneous ideals $I_1$ and $I_2$ of $S$ define the same closed subscheme of $X$ if and only if they have the same saturation.

(c) If $Y$ is any closed subscheme of $X$, then the homogeneous ideal
$$
J_Y\coloneqq\bigoplus_{d\ge0}\Gamma(X,\mci_Y(d))\subseteq S
$$
is saturated.
Hence it is the largest homogeneous ideal defining the subscheme $Y$.
For $r\ge1$, this ideal is $\Gamma_*(\mci_Y)$; the nonnegative truncation also covers $r=0$.

(d) There is a bijection between saturated ideals of $S$ and closed subschemes of $X$.
:::

::: {.solution}
For $0\le i\le r$, put $T_i=S_{x_i}$, $R_i=(T_i)_0$, and $U_i=D_+(x_i)=\Spec R_i$.
The degree-one element $x_i$ is a unit in $T_i$ and trivializes $\OO_X(1)$ on $U_i$.

::: pf

::: {.pf-step #s1}

Saturation is a homogeneous ideal, and it satisfies
$$
\bar I=\bigcap_{i=0}^r(IT_i\cap S),\qquad
\bar I T_i=IT_i,\qquad\overline{\bar I}=\bar I.
$$

::: pf-proof

For $s\in S$, membership of $s/1$ in $IT_i$ is equivalent to $x_i^n s\in I$ for some $n\ge0$, by the criterion for membership in a localized ideal.
This proves the intersection formula and shows that $\bar I$ is an ideal containing $I$.
If $s=\sum_d s_d$ is its homogeneous decomposition and $x_i^n s\in I$, homogeneity of $I$ gives $x_i^n s_d\in I$ for every $d$.
Applying this for every $i$ shows that each $s_d$ lies in $\bar I$.
Hence $\bar I$ is homogeneous, proving part (a).

For fixed $i$, the inclusions $I\subseteq\bar I\subseteq IT_i\cap S$ give $\bar I T_i=IT_i$ after localization.
The intersection formula applied to $\bar I$ then gives $\overline{\bar I}=\bar I$.

:::

:::

::: {.pf-step #s2}

The closed subscheme defined by $I$ is determined on $U_i$ by the ideal $(IT_i)_0\subseteq R_i$.
Equality of these degree-zero ideals for two homogeneous ideals is equivalent to equality of their full localized ideals in $T_i$.

::: pf-proof

The restriction of $\Proj(S/I)$ to $U_i$ has coordinate ring
$$
((S/I)_{x_i})_0\cong R_i/(IT_i)_0.
$$
Here localization and taking a fixed graded component are exact.
Thus $(IT_i)_0$ is its defining ideal on this affine chart.

For every integer $d$, multiplication by the unit $x_i^d$ gives
$$
(IT_i)_d=x_i^d(IT_i)_0.
$$
Since the localized ideals are graded, their degree-zero components therefore determine all their components.

:::

:::

::: {.pf-step #s3}

The equivalence in part (b) holds.

::: pf-proof

Two homogeneous ideals define the same closed subscheme of $X$ exactly when their defining ideal sheaves agree on the affine cover $(U_i)$.
By step [](#s2){.pf-ref}, this is equivalent to $I_1T_i=I_2T_i$ for every $i$.
The intersection formula in step [](#s1){.pf-ref} then gives $\bar I_1=\bar I_2$.
Conversely, equality of the saturations gives
$$
I_1T_i=\bar I_1T_i=\bar I_2T_i=I_2T_i
$$
by step [](#s1){.pf-ref}, so the closed subschemes agree on every chart and hence on $X$.

:::

:::

::: {.pf-step #s4}

For part (c), $J_Y$ is the saturation of every homogeneous ideal defining $Y$.

::: pf-proof

::: {.pf-step #s4-1}

The canonical map $S_d\to\Gamma(X,\OO_X(d))$ is an isomorphism for $d\ge0$.
For $r\ge1$, it is an isomorphism for all integers $d$, with both sides zero when $d<0$.

::: pf-proof

On $U_i$, the sections of $\OO_X(d)$ are $(T_i)_d$.
Every variable is a non-zero-divisor in the polynomial ring over $A$, so these modules inject into the degree-$d$ component of the Laurent polynomial ring
$$
B=A[x_0^{\pm1},\ldots,x_r^{\pm1}].
$$
The sheaf gluing condition identifies global sections with $\bigcap_i(T_i)_d$ inside $B_d$.
If $r\ge1$, membership in every $T_i$ forbids a negative exponent of any variable: for a fixed variable $x_j$, choose $i\ne j$, so $T_i$ allows no negative powers of $x_j$.
Uniqueness of Laurent polynomial coefficients then gives $\bigcap_i T_i=S$.
Taking degree $d$ proves the assertion for $r\ge1$.

If $r=0$, the single chart is all of $X$, and $(T_0)_d=Ax_0^d$ for every integer $d$.
It agrees with $S_d$ exactly in the nonnegative degrees, except when $A=0$, in which case every module is zero.

:::

:::

::: {.pf-step #s4-2}

If $I$ defines $Y$, then $J_Y=\bar I$.

::: pf-proof

The existence of such an $I$ is the homogeneous-ideal description of closed subschemes recalled in the problem [@Har10a, Proposition II.5.16].
The inclusion $\mci_Y(d)\to\OO_X(d)$ is injective because twisting by an invertible sheaf is exact.
Step [](#s4-1){.pf-ref} therefore identifies $\Gamma(X,\mci_Y(d))$ with a submodule of $S_d$ for $d\ge0$.
Multiplication by $S_e$ carries this submodule into $\Gamma(X,\mci_Y(d+e))$, so their direct sum is a homogeneous ideal.

For $s\in S_d$ with $d\ge0$, the section belongs to $\Gamma(X,\mci_Y(d))$ exactly when its restriction belongs to this ideal sheaf on every $U_i$.
Trivializing the twist by $x_i^d$ makes this condition
$$
s/x_i^d\in(IT_i)_0\quad\text{for every }i.
$$
Since $x_i$ is invertible, it is equivalent to $s/1\in IT_i$ for every $i$, hence to $s\in\bar I$ by step [](#s1){.pf-ref}.
This identifies every nonnegative graded component of $J_Y$ with that of $\bar I$, proving equality.

:::

:::

::: pf-qed

Step [](#s4-2){.pf-ref} and idempotence of saturation prove that $J_Y$ is saturated.
Step [](#s3){.pf-ref} shows that it defines $Y$.
Every homogeneous ideal defining $Y$ is contained in its saturation $J_Y$, giving maximality.
For $r\ge1$, step [](#s4-1){.pf-ref} and the inclusions $\mci_Y(d)\subseteq\OO_X(d)$ show that all negative-degree sections vanish, so $J_Y=\Gamma_*(\mci_Y)$.

:::

:::

:::

::: {.pf-step #s5}

For part (d), the inverse bijections are
$$
\boxed{I\longmapsto\Proj(S/I),\qquad Y\longmapsto J_Y}.
$$

::: pf-proof

If $I$ is saturated, step [](#s4){.pf-ref} gives $J_{\Proj(S/I)}=\bar I=I$.
Conversely, for every closed subscheme $Y$, step [](#s4){.pf-ref} gives a saturated ideal $J_Y$ defining $Y$.
Thus the displayed maps are inverse.

:::

:::

::: pf-qed

Step [](#s1){.pf-ref} proves part (a), step [](#s3){.pf-ref} proves part (b), step [](#s4){.pf-ref} proves part (c) with the nonnegative-degree clarification, and step [](#s5){.pf-ref} proves part (d).

:::

:::

:::

::: {.remark title="Projective dimension zero"}
With the [[D-MODGRMOD|all-integer-degree convention for $\Gamma_*$]], its use as an ideal of $S$ in part (c) needs $r\ge1$.
For a field $k$, take $S=k[x_0]$, $X=\PP_k^0$, and $Y=\varnothing$.
Then $\mci_Y=\OO_X$ and
$$
\Gamma_*(\OO_X)\cong k[x_0,x_0^{-1}],
$$
which has nonzero negative-degree components and is not an ideal of $k[x_0]$ as a graded submodule.
The nonnegative section ideal is $J_Y=S$, the saturated ideal defining the empty subscheme.
:::
