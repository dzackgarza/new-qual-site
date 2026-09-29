---
schema: qual/card@1
id: P-AGH359NONPROJ
kind: problem
title: A nonprojective infinitesimal extension of the projective plane
classification:
  areas:
  - algebraic-geometry
  topics:
  - Projectivity
  - Infinitesimal Extensions
  - Picard Group
  - Counterexamples
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: Compared the extension cocycle, Picard obstruction and both generalizations with the retained Hartshorne III.5.9 transcription. The proof computes the obstruction using the actual changes of split rings and exhibits its nonzero Laurent class. It also verifies properness of the thickening and states the Chern-class sign convention for the surface generalization.
- event: solution-written
  by: chatgpt
  date: 2026-09-17
---

::: {.problem}
We show that the result of (Ex. 5.8) is false in dimension two.
Let $k$ be an algebraically closed field of characteristic zero and let $X=\PP_k^2$.
Let $\omega$ be the sheaf of differential two-forms and let $\mct$ be the tangent sheaf.
Define an infinitesimal extension $X'$ of $X$ by $\omega$ using the element $\xi\in H^1(X,\omega\tensor\mct)$ described below (Ex. 4.10).

Let $x_0, x_1, x_2$ be the homogeneous coordinates of $X$, let $U_0, U_1, U_2$ be the standard open covering, and let $\xi_{ij}=(x_j/x_i)\, d(x_i/x_j)$.
This gives a Čech one-cocycle with values in $\Omega_X^1$, and since $\dim X=2$, we have $\omega\tensor\mct\cong\Omega_X^1$ (II, Ex. 5.16b).
Use the exact sequence
$$
\cdots \to H^1(X, \omega) \to \Pic X' \to \Pic X \mapsvia{\delta} H^2(X, \omega) \to \cdots
$$
of (Ex. 4.6) to show that $\delta$ is injective.
We have $\omega \cong \mco_X(-3)$ by (II, 8.20.1), so $H^2(X, \omega) \cong k$.
Since $\characteristic k=0$, you need only show that $\delta(\mco(1)) \neq 0$, which can be done by calculating in Čech cohomology.

Since $H^1(X, \omega)=0$, we see that $\Pic X'=0$.
In particular, $X'$ has no ample invertible sheaves, so it is not projective.
:::

::: {.solution}
Write $\Omega^1=\Omega_{X/k}$, $\omega=\bigwedge^2\Omega^1$, and $\mathcal T=(\Omega^1)^\vee$.
On $U_0$ use $u=x_1/x_0$, $v=x_2/x_0$, and the frame $\eta=du\wedge dv$ of $\omega$.
The extension and all its local splittings retain the specified quotient $X$ and the specified kernel $\omega$, as in [[P-AGH3410INFEXT]].

::: pf

::: {.pf-step #s1}
Contraction gives an isomorphism $\omega\otimes\mathcal T\cong\Omega^1$, under which a one-form $\alpha$ corresponds to the derivation $D_\alpha(f)=df\wedge\alpha$ with values in $\omega$.

::: pf-proof
The contraction map sends $\eta\otimes(A\partial_u+B\partial_v)$ to $A\,dv-B\,du$.
It is an isomorphism on this local basis and is defined intrinsically by contraction, so the local maps agree on overlaps.
The identity
$$
df\wedge\iota_w\eta=w(f)\eta
$$
in a rank-two differential module identifies the corresponding homomorphism $\Omega^1\to\omega$ with $df\mapsto df\wedge\alpha$.
The latter satisfies the Leibniz rule and annihilates $k$, so it is the associated derivation.
This fixes the sign of the identification used below.
:::

:::

::: {.pf-step #s2}
The forms $\xi_{ij}=d\log(x_i/x_j)$ form a cocycle, and they define the extension by gluing the split rings with transitions
$$
G_{ij}(a,z)=(a,z+D_{ij}(a)),\qquad D_{ij}(a)=da\wedge\xi_{ij}.
$$

::: pf-proof
The logarithmic identity $d\log(ab)=d\log a+d\log b$ gives $\xi_{ij}+\xi_{jh}=\xi_{ih}$ on every triple intersection.
Thus the corresponding derivations satisfy the same cocycle identity by step [](#s1){.pf-ref}.
On each $U_i$, take $\OO_{U_i}\oplus\omega|_{U_i}$ with multiplication $(a,z)(b,w)=(ab,aw+bz)$.
By [[P-AGH3410INFEXT]], the map $G_{ij}$ from chart $j$ to chart $i$ is an automorphism of identified square-zero extensions, its inverse is $G_{ji}$, and the cocycle identity makes these maps valid gluing data.
The glued scheme is the extension $X'$ associated to $\xi$.
In particular the kernel and the quotient glue by their identity maps.
:::

:::

::: {.pf-step #s3}
The extension $X'$ is a proper noetherian scheme of dimension two over $k$.

::: pf-proof
On each affine chart its ring is $A\oplus M$, where $A$ is a finite-type $k$-algebra and $M$ is the finite $A$-module corresponding to $\omega$.
This ring is finite over $A$ through its split inclusion, so is noetherian and of finite type over $k$.
The finitely many charts make $X'$ a noetherian finite-type scheme.
Its nilpotent ideal has quotient $X$, so their underlying spaces agree and $\dim X'=2$.

For a valuation ring $R$ over $k$ with fraction field $K$, a morphism $\Spec K\to X'$ factors through $X$ because every nilpotent section maps to zero in the field.
Properness of $X$ gives a unique extension to $\Spec R\to X$, hence to $X'$.
Every extension to $X'$ must itself factor through $X$, since $R$ is reduced, so uniqueness holds for $X'$ as well.
The valuative criterion, applied to the finite-type morphism $X'\to\Spec k$, proves properness [@Har10a, Theorem II.4.7].
:::

:::

::: {.pf-step #s4}
In the Čech complex for $\omega$, the obstruction to lifting $\OO_X(1)$ is represented on $U_0\cap U_1\cap U_2$ by
$$
\boxed{\delta([\OO_X(1)])=\left[\frac{du\wedge dv}{uv}\right].}
$$

::: pf-proof
Use the frame $e_i=x_i$ of $\OO_X(1)$ on $U_i$, with $e_j=g_{ij}e_i$ and $g_{ij}=x_j/x_i$.
Lift the transition unit $g_{ij}$ in the $i$th split ring to $(g_{ij},0)$.
On a triple overlap, the lift of $g_{jh}$ must first be expressed in the $i$th splitting using $G_{ij}$.
The multiplicative cocycle defect is therefore
$$
(g_{ij},0)G_{ij}(g_{jh},0)(g_{ih},0)^{-1}
=\left(1,\frac{D_{ij}(g_{jh})}{g_{jh}}\right),
$$
because $g_{ij}g_{jh}=g_{ih}$ and the ideal is square-zero.
By the construction of the connecting homomorphism for the unit sequence in [[P-AGH346SQUAREZEROPIC]], its second component is the Čech two-cocycle representing $\delta([\OO(1)])$.
Changing the chosen lifts adds a coboundary to this additive cocycle.

For $(i,j,h)=(0,1,2)$, one has $\xi_{01}=-du/u$ and $g_{12}=v/u$.
The derivation in step [](#s1){.pf-ref} gives
$$
D_{01}(u)=0,\qquad D_{01}(v)=\frac{\eta}{u},\qquad
D_{01}(v/u)=\frac{\eta}{u^2}.
$$
Dividing the last expression by $g_{12}=v/u$ gives $\eta/(uv)$, proving the claimed formula.
:::

:::

::: {.pf-step #s5}
The class in step [](#s4){.pf-ref} is nonzero and generates the one-dimensional $k$-space $H^2(X,\omega)$.

::: pf-proof
The canonical-sheaf computation gives $\omega\cong\OO_X(-3)$ [@Har10a, Example II.8.20.1].
Normalize this isomorphism so that the local frame $\eta$ on $U_0$ corresponds to $x_0^{-3}$.
Then $\eta/(uv)$ corresponds to the degree-$-3$ homogeneous fraction $1/(x_0x_1x_2)$.

The standard three-affine cover computes the cohomology by [@Har10a, Theorem III.4.5].
Its top cohomology for $\OO(-3)$ is the degree-$-3$ part of the Laurent polynomial ring $k[x_0^{\pm1},x_1^{\pm1},x_2^{\pm1}]$, modulo the sum of the three subrings in which only two variables are inverted.
The denominator is spanned by the monomials having at least one nonnegative exponent.
Among degree-$-3$ monomials, exactly one has all three exponents negative: $x_0^{-1}x_1^{-1}x_2^{-1}$.
Uniqueness of Laurent coefficients makes its class nonzero and a basis of this quotient.
The asserted nonvanishing and dimension follow.
:::

:::

::: {.pf-step #s6}
One has $\Pic X'=0$, and $X'$ has no ample invertible sheaf.

::: pf-proof
The group $\Pic X$ is $\ZZ$ with generator $[\OO(1)]$ [@Har10a, Proposition II.6.4 and Corollary II.6.16].
The map $\delta$ is a group homomorphism, so step [](#s5){.pf-ref} sends its integer $n$ to $n$ times a nonzero vector of the one-dimensional additive $k$-space.
Characteristic zero makes this map injective.
Furthermore, $H^1(X,\omega)=H^1(\PP^2,\OO(-3))=0$ by [@Har10a, Theorem III.5.1].
The exact Picard sequence in the statement now makes $\Pic X'$ inject into $\Pic X$ with image $\ker\delta=0$.
Hence every invertible sheaf on $X'$ is trivial.

The trivial sheaf on $X$ is not ample: the coherent sheaf $\OO_X(-1)$ has no nonzero global section and is unchanged by tensoring with any power of $\OO_X$.
If an invertible sheaf on $X'$ were ample, its restriction to the closed subscheme $X$ would be ample by [[P-AGH357AMPLENESS]], part (a), contradicting that restriction's triviality.
Thus $X'$ has no ample invertible sheaf and is not projective.
:::

:::

::: pf-qed
Steps [](#s1){.pf-ref}, [](#s2){.pf-ref}, and [](#s3){.pf-ref} construct the stated proper two-dimensional extension, steps [](#s4){.pf-ref} and [](#s5){.pf-ref} compute its nonzero obstruction, and step [](#s6){.pf-ref} proves injectivity of $\delta$, the trivial Picard group, and nonprojectivity.
:::

:::
:::

::: {.remark title="Extensions of an arbitrary nonsingular projective surface"}
Let $S$ be a nonsingular projective integral surface over an algebraically closed field of characteristic zero, and let $D$ be an ample divisor.
Use the logarithmic convention $c_1(D)=[d\log h_{ij}]$, where $h_{ij}$ are the transitions from frame $j$ to frame $i$ of $\OO_S(D)$.
The [logarithmic Chern-class construction](https://stacks.math.columbia.edu/tag/0FLE) places this class in $H^1(S,\Omega^1_S)$.
Under the contraction convention of step [](#s1){.pf-ref} it defines an extension by $\omega_S$.
For transitions $g_{ij}$ of $\OO_S(E)$, the calculation in step [](#s4){.pf-ref} gives obstruction cocycle
$$
d\log g_{jh}\wedge d\log h_{ij}
=-d\log h_{ij}\wedge d\log g_{jh}.
$$
This is the Hodge cup product $c_1(D)\cup c_1(E)$ with the total-complex sign convention in that Chern-class construction.
The top-degree Hodge--de Rham comparison and the [cycle-class degree formula](https://stacks.math.columbia.edu/tag/0FWC) identify its trace with the intersection number $(D.E)\in k$.
For the top-degree comparison, the Hodge--de Rham spectral sequence has only $H^2(S,\omega_S)$ in total degree four, since the surface has no differential forms or coherent cohomology above degree two.
Its edge map onto $H^4_{\mathrm{dR}}(S/k)$ is therefore surjective.
Both spaces are one-dimensional, by Serre duality [@Har10a, Theorem III.7.6] and the de Rham Weil-cohomology theorem cited in the degree formula, so this edge map is an isomorphism.
The trace is normalized to give degree on zero-cycle classes.
Thus, with this identification $H^2(S,\omega_S)\cong k$,
$$
\delta([\OO_S(E)])=(D.E).
$$
For ample $E$ this is a positive integer, hence is nonzero in characteristic zero [@Har10a, Chapter V, §1].
No ample sheaf on $S$ can therefore lift to the extension, and restriction of an ample sheaf would be ample.
The extension has no ample invertible sheaf and is not projective; it is proper by the valuation-ring argument in step [](#s3){.pf-ref}.
The specified cocycle for $\PP^2$ in the problem is the negative of this logarithmic $c_1(\OO(1))$ convention; it changes the sign of the obstruction, not its kernel or the nonprojectivity conclusion.
:::

::: {.remark title="Proper thickenings in positive characteristic"}
Let $Z$ be proper over a field of characteristic $p>0$.
Then $Z$ is projective if and only if $Z_{\mathrm{red}}$ is projective.
One direction follows by taking the closed subscheme $Z_{\mathrm{red}}$ of a projective scheme.
For the converse, let $N$ be the nilradical, choose $e$ with $N^e=0$, and write $Z_j=(|Z|,\OO_Z/N^j)$.
The ideals $N^j/N^{j+1}$ have square zero, and their cohomology groups are killed by $p$.
The Picard sequence in [[P-AGH346SQUAREZEROPIC]] consequently shows that the $p$th tensor power of every invertible sheaf on $Z_j$ lifts to $Z_{j+1}$: its obstruction is $p$ times a class in $H^2(N^j/N^{j+1})$ and is zero.
Starting with an ample invertible sheaf on $Z_1=Z_{\mathrm{red}}$ and iterating gives a lift to $Z_e=Z$ of its $p^{e-1}$st power.
This lift is ample by [[P-AGH357AMPLENESS]], part (b), since its restriction to the reduction is ample.
Properness and an ample sheaf imply projectivity [@Har10a, Theorem II.7.6 and Remark II.5.16.1].
This proves the positive-characteristic assertion without a smoothness hypothesis on the reduction.
:::
