---
schema: qual/card@1
id: P-AGH2511CARTPROD
kind: problem
title: The Cartesian product of graded rings and the Segre embedding
classification:
  areas:
  - algebraic-geometry
  topics:
  - Graded Rings
  - Proj
  - Segre Embedding
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: Compared the construction with the retained MinerU transcription Hartshorne_Solutions_extracted.md, section 2.5, solution 5.11, and the Segre embedding with Stacks Project Tag 01WD. The proof treats arbitrary nonnegative gradings by common-degree localization, proves overlap compatibility, and identifies the twisting sheaf without assuming flatness over A.
- event: solution-written
  by: chatgpt
  date: 2026-09-17
---

::: {.problem}
Let $S$ and $T$ be two graded rings with $S_0 = T_0 = A$.
Define the \dfn{Cartesian product} $\fiberprod{S}{A}{T}$ to be the graded ring $\bigoplus_{d \geq 0} S_d \tensor_A T_d$.
If $X = \Proj S$ and $Y = \Proj T$, show that $\Proj(\fiberprod{S}{A}{T}) \cong \fiberprod{X}{A}{Y}$, and show that the sheaf $\OO(1)$ on $\Proj(\fiberprod{S}{A}{T})$ is isomorphic to $p_1^*(\OO_X(1)) \tensor p_2^*(\OO_Y(1))$ on $X \times Y$.

The Cartesian product of rings is related to the Segre embedding of projective spaces (I, Ex. 2.14) as follows.
If $x_0, \ldots, x_r$ generate $S_1$ over $A$, corresponding to a projective embedding $X \injects \PP^r_A$, and if $y_0, \ldots, y_s$ generate $T_1$, corresponding to $Y \injects \PP^s_A$, then $\ts{x_i \tensor y_j}$ generates $(\fiberprod{S}{A}{T})_1$, and hence defines a projective embedding $\Proj(\fiberprod{S}{A}{T}) \injects \PP^N_A$ with $N = rs + r + s$.
This is just the image of $X \times Y \subseteq \PP^r \times \PP^s$ in its Segre embedding.
:::

::: {.solution}
Put $R=\bigoplus_{d\ge0}S_d\otimes_A T_d$, $Z=\Proj R$, and $P=X\times_A Y$.
The multiplication of $R$ is induced by $(s\otimes t)(s'\otimes t')=ss'\otimes tt'$.
Write $p_1:P\to X$ and $p_2:P\to Y$ for the projections.
For a positive-degree homogeneous element $u\in S$, write $S_{(u)}=(S_u)_0$; use the same notation for $T$ and $R$.

::: pf

::: {.pf-step #s1}

For $\ell>0$, $u\in S_\ell$, and $v\in T_\ell$, putting $z=u\otimes v$ gives an isomorphism of $A$-algebras
$$
\theta_{u,v}:R_{(z)}\longrightarrow S_{(u)}\otimes_A T_{(v)},
\qquad
\frac{s\otimes t}{z^n}\longmapsto\frac{s}{u^n}\otimes\frac{t}{v^n},
$$
where $s\in S_{n\ell}$ and $t\in T_{n\ell}$.

::: pf-proof

As $A$-modules,
$$
S_{(u)}\cong\varinjlim_n S_{n\ell},\qquad
T_{(v)}\cong\varinjlim_n T_{n\ell},\qquad
R_{(z)}\cong\varinjlim_n(S_{n\ell}\otimes_A T_{n\ell}),
$$
with transition maps multiplication by $u$, $v$, and $u\otimes v$, respectively.
Tensor products commute with these direct limits.
In the product indexing set $\NN\times\NN$, every pair $(m,n)$ is bounded by $(q,q)$ for $q\ge\max(m,n)$.
Thus taking the diagonal indices gives the same direct limit, proving that the displayed map is a well-defined bijection.
Its formula preserves products and $1$, so it is an $A$-algebra isomorphism.

Explicitly, its inverse sends an elementary tensor with $s\in S_{m\ell}$ and $t\in T_{n\ell}$ to
$$
\frac{s}{u^m}\otimes\frac{t}{v^n}
\longmapsto
\frac{s u^{q-m}\otimes t v^{q-n}}{(u\otimes v)^q},
\qquad q\ge\max(m,n).
$$
Increasing $q$ multiplies numerator and denominator by the same element, so does not change the fraction.
The direct-limit construction verifies the formula even when the localization maps are not injective.

:::

:::

::: {.pf-step #s2}

The chart isomorphisms of step [](#s1){.pf-ref} glue to an isomorphism
$$
\Phi:P\xrightarrow{\ \cong\ }Z.
$$

::: pf-proof

The affine opens $D_+(u)\times_A D_+(v)$ with $u$ and $v$ of the same positive degree cover $P$.
Indeed, starting with arbitrary $f\in S_a$ and $g\in T_b$ of positive degrees, replace them by $u=f^b$ and $v=g^a$.
Their degrees both equal $ab$, and taking powers leaves the distinguished opens unchanged.

The opens $D_+(u\otimes v)$ also cover $Z$.
A point of $Z$ is a homogeneous prime not containing $R_+$.
Some positive-degree homogeneous element therefore lies outside it.
Write that element as a finite sum of elementary tensors in $S_d\otimes_A T_d$; at least one of those elementary tensors also lies outside the prime.
Step [](#s1){.pf-ref} gives an affine isomorphism between the corresponding members of these covers.

To check overlaps, take another pair $u'\in S_{\ell'}$, $v'\in T_{\ell'}$ and put $z'=u'\otimes v'$.
Inside $D_+(z)$, its intersection with $D_+(z')$ is the principal open defined by $(z')^\ell/z^{\ell'}$.
Under $\theta_{u,v}$ this element maps to
$$
\frac{(u')^\ell}{u^{\ell'}}\otimes
\frac{(v')^\ell}{v^{\ell'}}.
$$
Its invertible locus is exactly
$$
\bigl(D_+(u)\cap D_+(u')\bigr)
\times_A
\bigl(D_+(v)\cap D_+(v')\bigr):
$$
in a commutative ring a product is a unit exactly when both factors are units.
All the ring maps on this overlap send each homogeneous fraction to the same tensor of localized fractions, so they commute with restriction.
The affine isomorphisms therefore glue, as do their inverses.

:::

:::

::: {.pf-step #s3}

Under $\Phi$, the twisting sheaf satisfies
$$
\Phi^*\OO_Z(1)\cong p_1^*\OO_X(1)\otimes_{\OO_P}p_2^*\OO_Y(1).
$$

::: pf-proof

On the affine chart in step [](#s1){.pf-ref}, put $C=S_{(u)}$, $D=T_{(v)}$, $E=(S_u)_1$, and $F=(T_v)_1$.
The [[D-MODGRMOD|associated-sheaf construction]] identifies the restrictions of $\OO_X(1)$ and $\OO_Y(1)$ with the sheaves associated to $E$ over $C$ and $F$ over $D$.
Their pullbacks and tensor product on $\Spec(C\otimes_A D)$ correspond to the module
$$
\bigl(E\otimes_C(C\otimes_A D)\bigr)
\otimes_{C\otimes_A D}
\bigl((C\otimes_A D)\otimes_D F\bigr)
\cong E\otimes_A F.
$$
For the sheaf $\OO_Z(1)$, the corresponding module is $(R_z)_1$.
The same diagonal direct-limit argument as in step [](#s1){.pf-ref} gives
$$
\begin{aligned}
E\otimes_A F
&\cong\left(\varinjlim_n S_{n\ell+1}\right)
\otimes_A\left(\varinjlim_n T_{n\ell+1}\right)\\
&\cong\varinjlim_n(S_{n\ell+1}\otimes_A T_{n\ell+1})
\cong(R_z)_1.
\end{aligned}
$$
In the reverse direction, the map sends $(s\otimes t)/z^n$ to $(s/u^n)\otimes(t/v^n)$, now with both numerators of degree $n\ell+1$.
These maps are linear over the algebra isomorphism of step [](#s1){.pf-ref} and commute with the overlap localizations of step [](#s2){.pf-ref}.
They therefore glue to the asserted sheaf isomorphism.

:::

:::

::: {.pf-step #s4}

For the projective embeddings in the statement, the morphism defined by the sections $x_i\otimes y_j$ is their product followed by the Segre embedding.

::: pf-proof

The elementary tensors $x_i\otimes y_j$ generate $S_1\otimes_A T_1=R_1$ because the $x_i$ and $y_j$ generate the two factors.
By step [](#s3){.pf-ref}, their associated sections pull back under $\Phi$ to
$$
p_1^*x_i\otimes p_2^*y_j
\in\Gamma\bigl(P,p_1^*\OO_X(1)\otimes p_2^*\OO_Y(1)\bigr).
$$
The given projective embeddings make $\OO_X(1)$ and $\OO_Y(1)$ invertible and generated by these respective coordinate sections.
The products therefore generate their tensor product and define a morphism to $\PP_A^{(r+1)(s+1)-1}$.

On the chart where $x_i\otimes y_j$ is nonzero, step [](#s1){.pf-ref} gives the coordinate formula
$$
\frac{x_a\otimes y_b}{x_i\otimes y_j}
\longmapsto\frac{x_a}{x_i}\otimes\frac{y_b}{y_j}.
$$
This is exactly the coordinate formula for the product of the given embeddings followed by the [Segre embedding](https://stacks.math.columbia.edu/tag/01WD).
The product of closed immersions is a closed immersion, by base change and composition, and the Segre morphism is a closed immersion as well.
Hence the resulting morphism is the claimed projective embedding, with $N=(r+1)(s+1)-1=rs+r+s$.

When $S$ and $T$ are generated in degree one, every elementary tensor in $S_d\otimes_A T_d$ is a sum of products of $d$ of the $x_i\otimes y_j$.
Thus these elements also generate $R$ as an $A$-algebra, giving its stated degree-one projective presentation.

:::

:::

::: pf-qed

Step [](#s2){.pf-ref} identifies the schemes, step [](#s3){.pf-ref} identifies the twisting sheaves, and step [](#s4){.pf-ref} identifies the projective embedding with the Segre embedding.

:::

:::

:::
