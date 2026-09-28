---
schema: qual/card@1
id: P-AGH283PRODDIFF
kind: problem
title: Differentials and canonical sheaves of product schemes
classification:
  areas:
  - algebraic-geometry
  topics:
  - Sheaves of Differentials
  - Canonical Sheaves
  - Arithmetic Genus
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: Compared all three parts with the retained Hartshorne II.8.3 transcription and kept arbitrary base schemes in part (a). Made the classical algebraically closed field convention explicit for nonsingular varieties. The proof constructs inverse differential maps on affine tensor products and computes the arithmetic genus from the actual Segre homogeneous coordinate ring.
- event: solution-written
  by: chatgpt
  date: 2026-09-17
---

::: {.problem}
(a) Let $X$ and $Y$ be schemes over another scheme $S$, and let $p_1,p_2$ be the projections from $X\times_S Y$.
   Use (8.10) and (8.11) to show that
$$
\Omega_{(\fiberprod{X}{S}{Y})/S} \cong p_1^* \Omega_{X/S} \oplus p_2^* \Omega_{Y/S}
.
$$

(b) If $X$ and $Y$ are nonsingular varieties over an algebraically closed field $k$, show that
$$
\omega_{X \times Y} \cong p_1^* \omega_X \tensor p_2^* \omega_Y
.
$$

(c) Over an algebraically closed field $k$, let $Y$ be a nonsingular plane cubic curve, and let $X$ be the surface $Y \times Y$.
   Show that $p_g(X) = 1$ but $p_a(X) = -1$ (I, Ex. 7.2).
   This shows that the arithmetic genus and the geometric genus of a nonsingular projective variety may be different.
:::

::: {.solution}
In (a), put $Z=X\times_S Y$.
In (b), products are over $k$ and the canonical sheaf is the top exterior power of the sheaf of differentials.

<1>1. For $A$-algebras $B,C$, put $D=B\otimes_A C$.
There is a natural $D$-linear isomorphism
$$
\Omega_{D/A}\cong
(\Omega_{B/A}\otimes_A C)\oplus(B\otimes_A\Omega_{C/A}).
$$

::: {.proof}
Let $M$ be the displayed direct sum, with its $D$-module structure induced by the two factors.
Define
$$
\partial:D\longrightarrow M,\qquad
\partial(b\otimes c)=(db\otimes c,\ b\otimes dc).
$$
Additivity and $A$-balancing hold because both component derivations annihilate $A$.
Expanding $d(bb')$ and $d(cc')$ proves the Leibniz rule on elementary tensors, and bilinearity extends it to all of $D$.
Thus $\partial$ is an $A$-derivation and induces a $D$-linear map $u:\Omega_{D/A}\to M$.

The two algebra maps $B\to D$ and $C\to D$ induce a map $v:M\to\Omega_{D/A}$ with formulas
$$
v(db\otimes c,0)=(1\otimes c)d(b\otimes1),\qquad
v(0,b\otimes dc)=(b\otimes1)d(1\otimes c).
$$
The defining differential relations make these maps well-defined.
The composite $u\circ v$ fixes the displayed generators of both summands.
The other composite sends $d(b\otimes c)$ to
$$
(1\otimes c)d(b\otimes1)+(b\otimes1)d(1\otimes c)
=d(b\otimes c).
$$
Such differentials generate $\Omega_{D/A}$, so the composites are identities.
The formulas commute with homomorphisms of the algebras and with localization.
:::

<1>2. These affine isomorphisms give the natural sheaf isomorphism in (a).

::: {.proof}
Cover $S$ by affine opens $\Spec A$ and the corresponding inverse images in $X,Y$ by affine opens $\Spec B,\Spec C$.
The affine products $\Spec(B\otimes_A C)$ cover $Z$.
On such a product, the two summands of step <1>1 are exactly the modules defining $p_1^*\Omega_{X/S}$ and $p_2^*\Omega_{Y/S}$.
The natural maps to $\Omega_{Z/S}$ are induced by the projections, as in the transitivity sequence of [@Har10a, Proposition II.8.11]; base change identifies the relative term for either projection with the pullback of the other factor's differentials [@Har10a, Proposition II.8.10].
Step <1>1 proves that the sum of these natural maps is an isomorphism on each affine product.
Naturality and localization compatibility make the isomorphisms agree on overlaps, so they glue.
No flatness or finite-type hypothesis is needed in (a).
:::

<1>3. For smooth varieties $X,Y$ of dimensions $r,s$ over a field $k$, there is a natural isomorphism
$$
\omega_{X\times_kY}\cong p_1^*\omega_X\otimes p_2^*\omega_Y.
$$

::: {.proof}
The sheaves $\Omega_{X/k}$ and $\Omega_{Y/k}$ are locally free of ranks $r$ and $s$.
Their product is smooth, since smooth morphisms are preserved by base change and composition, and has dimension $r+s$ [@Har10a, Chapter III, §10].
Apply step <1>2 with $S=\Spec k$ and take the top exterior power.
For locally free sheaves of ranks $r$ and $s$, wedging the first summand before the second gives
$$
\bigwedge^{r+s}(F\oplus G)\cong\bigwedge^rF\otimes\bigwedge^sG.
$$
This is an isomorphism on local wedge bases, and the map is independent of those bases.
Exterior powers commute with pullback, as proved in [[P-AGH2516TENSOROPS]], part (e).
Consequently
$$
\begin{aligned}
\omega_{X\times_kY}
&\cong\bigwedge^{r+s}(p_1^*\Omega_{X/k}\oplus p_2^*\Omega_{Y/k})\\
&\cong p_1^*\bigwedge^r\Omega_{X/k}\otimes p_2^*\bigwedge^s\Omega_{Y/k}
\cong p_1^*\omega_X\otimes p_2^*\omega_Y.
\end{aligned}
$$
Over the algebraically closed field in (b), nonsingular varieties are smooth, so this proves (b).
The calculation also proves its smooth-variety formulation over an arbitrary field.
:::

<1>4. For the surface $X=Y\times_kY$ in (c), $\omega_X\cong\OO_X$ and $\boxed{p_g(X)=1}$.

::: {.proof}
The [[D-MODCONORM|adjunction formula]] for the smooth degree-three curve $Y\subseteq\PP_k^2$ gives
$$
\omega_Y\cong\OO_Y(3-3)\cong\OO_Y
$$
[@Har10a, Example II.8.20.3].
Step <1>3 therefore gives $\omega_X\cong\OO_X$.
The product of integral varieties over an algebraically closed field is integral [@Har10a, Exercises I.3.15--I.3.16 and II.3.23], and the Segre embedding makes $X$ projective.
Every global regular function on this projective integral variety is constant: its morphism to $\PP^1$ has closed irreducible image missing infinity, so has image a point, and reducedness makes the function equal to that constant.
Thus $\Gamma(X,\OO_X)=k$ and
$$
p_g(X)=\dim_k\Gamma(X,\omega_X)=1.
$$
:::

<1>5. The Segre Hilbert polynomial of $X$ is $P_X(q)=9q^2$, and $\boxed{p_a(X)=-1}$.

::: {.proof}
Write $Y=\operatorname{Proj}A$ with
$$
A=k[x_0,x_1,x_2]/(F),\qquad\deg F=3.
$$
Multiplication by $F$ is injective on the polynomial ring, so for $q\ge3$ the graded quotient sequence gives
$$
\dim_kA_q=\binom{q+2}{2}-\binom{q-1}{2}=3q.
$$
The homogeneous coordinate ring for the Segre embedding of $Y\times Y$ is
$$
R=\bigoplus_{q\ge0}A_q\otimes_k A_q,
$$
with multiplication induced by the two factors, as in [[P-AGH2511CARTPROD]].
Its degree-one generators are the products of a coordinate on the first factor with a coordinate on the second.
Thus, for $q\ge3$,
$$
\dim_kR_q=(\dim_kA_q)^2=9q^2.
$$
The Hilbert polynomial is consequently $P_X(q)=9q^2$.
For a projective variety of dimension two, the definition of arithmetic genus is $p_a(X)=(-1)^2(P_X(0)-1)$ [@Har10a, Chapter I, §7].
Since $P_X(0)=0$, this gives $p_a(X)=-1$.
The value $P_X(0)$ is the polynomial's value at zero, not the dimension of the degree-zero piece $R_0=k$.
:::

<1>6. Q.E.D.

::: {.proof}
Steps <1>1--<1>2 prove (a), step <1>3 proves (b), and steps <1>4--<1>5 give both genera required in (c).
:::
:::
