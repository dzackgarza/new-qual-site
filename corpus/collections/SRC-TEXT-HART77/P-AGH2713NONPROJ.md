---
schema: qual/card@1
id: P-AGH2713NONPROJ
kind: problem
title: A complete nonprojective variety
classification:
  areas:
  - algebraic-geometry
  topics:
  - Complete Varieties
  - Picard Groups
  - Nodal Cubic
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: Compared all four parts and the units hint with the retained Hartshorne II.7.13 transcription. Computed line bundles by matching the two branch fibres of the normalization, proved that matching produces an invertible sheaf, and fixed frames of O(n) to establish the sign of the d+n pullback formula.
- event: solution-written
  by: chatgpt
  date: 2026-09-17
---

::: {.problem}
Let $k$ be an algebraically closed field of characteristic $\neq 2$.
Let $C \subseteq \PP^2_k$ be the nodal cubic curve $y^2 z = x^3 + x^2 z$.
If $P_0 = (0, 0, 1)$ is the singular point, then $C - P_0$ is isomorphic to the multiplicative group $\GG_m = \Spec k[t, \inverseof{t}]$ (Ex.
6.7). For each $a \in k$, $a \neq 0$, consider the translation of $\GG_m$ given by $t \mapsto at$.
This induces an automorphism of $C$ which we denote $\varphi_a$.
Now consider $C \times (\PP^1 - \ts{0})$ and $C \times (\PP^1 - \ts{\infty})$.
We glue their open subsets $C \times (\PP^1 - \ts{0, \infty})$ by the isomorphism
$$
\varphi: \gens{P, u} \mapsto \gens{\varphi_u(P), u}, \qquad P \in C,\ u \in \GG_m = \PP^1 - \ts{0, \infty}
.
$$
Thus we obtain a scheme $X$, which is our example.
The projections to the second factor are compatible with $\varphi$, so there is a natural morphism $\pi: X \to \PP^1$.

(a) Show that $\pi$ is a proper morphism, and hence that $X$ is a complete variety over $k$.

(b) Use the method of (Ex.
    6.9) to show that $$ \Pic(C \times \AA^1) \cong \GG_m \times \ZZ \quad\text{and}\quad \Pic(C \times (\AA^1 - \ts{0})) \cong \GG_m \times \ZZ \times \ZZ
.
$$

(c) Now show that the restriction map $\Pic(C \times \AA^1) \to \Pic(C \times (\AA^1 - \ts{0}))$ is of the form $\gens{t, n} \mapsto \gens{t, 0, n}$, and that the automorphism $\varphi$ of $C \times (\AA^1 - \ts{0})$ induces a map of the form $\gens{t, d, n} \mapsto \gens{t, d + n, n}$ on its Picard group.

(d) Conclude that the image of the restriction map $\Pic X \to \Pic(C \times \ts{0})$ consists entirely of divisors of degree $0$ on $C$.
    Hence $X$ is not projective over $k$, and $\pi$ is not a projective morphism.
:::

::: {.hint}
For (b), if $A$ is a domain and $*$ denotes the group of units, then $(A[u])^*\cong A^*$ and $(A[u,u^{-1}])^*\cong A^*\times\ZZ$.
:::

::: {.solution}
The symbol $\GG_m$ in these Picard-group formulas denotes the group $k^\times$.
Let $V_0=\Spec k[u]$ and $V_\infty=\Spec k[u^{-1}]$ be the two standard opens of the base $\PP^1$.
Write $X_0=C\times V_0$ and $X_\infty=C\times V_\infty$.

::: pf

::: {.pf-step #s1}
The normalization of $C$ is $\PP_t^1$, with the two points $0,\infty$ identified at the node, and the action $t\mapsto ut$ descends to the asserted overlap automorphism.

::: pf-proof
The [[P-AGH267NODALCUBIC|normalization calculation]] uses $v=y/x$, with $x=v^2-1$ and $y=v(v^2-1)$ on $z=1$.
The two branches are $v=1,-1$.
The fractional linear coordinate
$$
t=\frac{v-1}{v+1}
$$
carries these branches to $0,\infty$, respectively, and identifies the smooth locus of $C$ with $\GG_m$.

For $R=k[u]$ or $k[u,u^{-1}]$, put $C_R=C\times\Spec R$ and let $\nu_R:\PP_R^1\to C_R$ be the base-changed normalization.
On the nodal affine chart the coordinate rings are
$$
A=R+(v^2-1)R[v]\subseteq B=R[v].
$$
Indeed, the polynomial identity proved in [[P-AGH267NODALCUBIC]], step 2, remains true with coefficients in $R$.
Writing $J=(v^2-1)B$, one obtains
$$
A/J=R,\qquad B/J=R\oplus R,
\qquad A=B\times_{R\oplus R}R,
$$
where the last map is the diagonal and the map from $B$ is evaluation at the two branches.
Away from the node the normalization is an isomorphism.
Thus the structure sheaf of $C_R$ consists of functions on its normalization whose values on the two branch sections agree.

The $R$-automorphism $t\mapsto ut$ for $R=k[u,u^{-1}]$ fixes the two branch sections and preserves this equality of values.
It therefore descends to $C_R$: the continuous map descends through the finite closed surjection identifying the branches, and its pullback on functions preserves the displayed subalgebra.
The same construction with $u^{-1}$ is its inverse.
This gives the regular overlap automorphism, not only separate automorphisms of its closed fibres.
:::

:::

::: {.pf-step #s2}
The morphism $\pi:X\to\PP^1$ is proper, and $X$ is a complete integral variety.

::: pf-proof
Over each of $V_0,V_\infty$, the morphism is the projection $C\times V_i\to V_i$.
It is a base change of the projective curve $C\to\Spec k$, so is proper.
Properness is local on the target, hence $\pi$ is proper [@Har10a, Chapter II, §4].
Since $\PP^1$ is proper over $k$, their composite is proper.

Each $X_i$ is integral: an affine coordinate ring of $C$ is a domain, and adjoining one polynomial variable preserves this property.
The two opens have a nonempty overlap, so their union is irreducible and reduced.
They are of finite type over $k$, and properness gives separatedness.
Thus $X$ is an integral variety proper over $k$, which is completeness.
:::

:::

::: {.pf-step #s3}
For $R=k[u]$ or $k[u,u^{-1}]$, an invertible sheaf on $C_R$ is equivalent to an invertible sheaf $L$ on $\PP_R^1$ together with an isomorphism
$$
\theta:L|_{0_R}\xrightarrow{\cong}L|_{\infty_R}.
$$

::: pf-proof
Pulling back an invertible sheaf $M$ from $C_R$ gives $L=\nu_R^*M$.
The two restrictions are canonically identified with the restriction of $M$ to the nodal section, giving $\theta$.
Conversely, from $(L,\theta)$ form the subsheaf of $\nu_{R*}L$ consisting of sections whose two branch values match under $\theta$.
It is coherent, being the kernel of the branch-difference map between coherent sheaves for the finite morphism $\nu_R$.
It agrees with $L$ away from the nodal section.

To verify invertibility at a point of that section, let $\mathfrak q$ be the corresponding prime of $A$ and localize the fibre-product ring description in step [](#s1){.pf-ref} at $\mathfrak q$.
The resulting normalization ring is finite and semilocal, with two maximal ideals, and its quotient by $J$ is $R_{\mathfrak p}\oplus R_{\mathfrak p}$ for the corresponding prime $\mathfrak p$ of $R$.
A rank-one projective module over a semilocal ring is free: choose a section nonzero modulo each maximal ideal by the Chinese remainder theorem and use Nakayama's lemma at each maximal ideal.
Thus $L$ has a frame over this semilocal ring, and in this frame the matching condition is
$$
f_\infty=\eta f_0\qquad\text{for some }\eta\in R_{\mathfrak p}^\times.
$$
Lift $(1,\eta)$ to an element $h$ of the normalization ring.
It avoids both maximal ideals and is therefore a unit.
The matching module is exactly $hA_{\mathfrak q}$: division by $h$ turns the condition into equality of the two residues, which characterizes $A_{\mathfrak q}$ by step [](#s1){.pf-ref}. It is consequently free of rank one, and its pullback is the original $L$.

Starting with $M$, the matching construction recovers $M$ by tensoring the equalizer description of $\OO_{C_R}$ with this locally free sheaf.
Starting with $(L,\theta)$, the local generator $h$ shows that both $L$ and the matching isomorphism are recovered.
The same equalizer description identifies the morphisms between these objects.
This proves the claimed equivalence, including isomorphism classes.
:::

:::

::: {.pf-step #s4}
There is a group isomorphism
$$
\Pic(C_R)\cong R^\times\times\ZZ.
$$
The integer is the degree on a normalized fibre.

::: pf-proof
Both rings $R$ are PIDs, so $\Pic(\Spec R)=0$.
The [[P-AGH279PICPE|projective-bundle Picard calculation]] gives $\Pic(\PP_R^1)=\ZZ$, generated by $\OO(1)$.
Thus the normalization sheaf in step [](#s3){.pf-ref} is uniquely $\OO(n)$ up to isomorphism.
In homogeneous coordinates $[T_0:T_1]$ with $t=T_1/T_0$, use the frames
$$
e_0=T_0^n\text{ at }0_R,\qquad e_\infty=T_1^n\text{ at }\infty_R.
$$
For negative $n$ these are the corresponding dual tensor-power frames.
The matching isomorphism is uniquely of the form $\theta(e_0)=\lambda e_\infty$ for $\lambda\in R^\times$.

An automorphism of $\OO(n)$ is multiplication by an element of $\Gamma(\PP_R^1,\OO)^\times=R^\times$.
It multiplies both branch frames by the same unit, and therefore does not change $\lambda$.
Consequently the pair $(\lambda,n)$ uniquely determines the isomorphism class on $C_R$, and every such pair occurs by step [](#s3){.pf-ref}. Tensor products multiply $\lambda$ and add $n$, giving the group isomorphism.

A unit of $k[u]$ is a nonzero constant, since degrees add under multiplication.
A unit of $k[u,u^{-1}]$ is uniquely $cu^d$ with $c\in k^\times$ and $d\in\ZZ$: the largest and smallest exponents both add under multiplication, so an invertible Laurent polynomial has only one term.
Hence (b) gives
$$
\boxed{\Pic(C\times\AA^1)\cong k^\times\times\ZZ,\qquad
\Pic(C\times\GG_m)\cong k^\times\times\ZZ\times\ZZ.}
$$
On the latter group use coordinates $(c,d,n)$ corresponding to $(cu^d,n)$.
:::

:::

::: {.pf-step #s5}
In these coordinates, restriction is $(c,n)\mapsto(c,0,n)$ and pullback by $\varphi$ is $(c,d,n)\mapsto(c,d+n,n)$.

::: pf-proof
Restriction from $k[u]$ to $k[u,u^{-1}]$ preserves $\OO(n)$ and its chosen branch frames and sends the constant matching unit $c$ to the same constant.
This proves the restriction formula; the chart at infinity, with coordinate $u^{-1}$, has the same image.

On the normalization, $\varphi$ is
$$
\tau:[T_0:T_1]\longmapsto[T_0:uT_1].
$$
The induced isomorphism $\tau^*\OO(n)\cong\OO(n)$ sends the pulled-back frame at zero to $e_0$, and the pulled-back frame at infinity to $u^n e_\infty$.
Thus pulling back the matching map $e_0\mapsto\lambda e_\infty$ and making this identification changes its coefficient to $u^n\lambda$.
For $\lambda=cu^d$, this is $cu^{d+n}$.
The degree remains $n$, proving the stated pullback formula and its sign.
:::

:::

::: {.pf-step #s6}
Every invertible sheaf on $X$ has degree zero on $C\times\{0\}$.

::: pf-proof
Let $M$ be invertible on $X$, and let $(c_0,n_0)$ and $(c_\infty,n_\infty)$ describe its restrictions to $X_0$ and $X_\infty$.
Use the specified gluing from the overlap in $X_\infty$ to the overlap in $X_0$.
Compatibility of the two restrictions requires
$$
(c_\infty,0,n_\infty)
=\varphi^*(c_0,0,n_0)
=(c_0,n_0,n_0)
$$
by step [](#s5){.pf-ref}. Equality of the middle coordinates gives $n_0=0$, and equality of the last coordinates also gives $n_\infty=0$.
The restriction to the fibre over zero therefore has normalization degree zero.
This is the degree on the nodal curve, as in [[P-AGH267NODALCUBIC]], step 3, and [[P-AGH269SINGCURVEPIC]], step 8.
:::

:::

::: {.pf-step #s7}
Neither $X$ nor the morphism $\pi$ is projective.

::: pf-proof
If $X$ had a projective embedding over $k$, pulling back $\OO(1)$ and restricting to the closed fibre over zero would give a very ample invertible sheaf on $C$.
A projective embedding of $\pi$ would give the same conclusion after base change to zero.
But step [](#s6){.pf-ref} says that either invertible sheaf would pull back to $\OO_{\PP^1}(0)$ on the normalization of $C$.
The coordinate sections of such an embedding would then become global sections of $\OO_{\PP^1}$, all of which are constants.
They would define a constant morphism from $\PP^1$, whereas the composite of the surjective normalization $\PP^1\to C$ with an embedding of the curve $C$ is nonconstant.
This contradiction proves both nonprojectivity assertions.
:::

:::

::: pf-qed
Step [](#s2){.pf-ref} proves (a), steps [](#s3){.pf-ref} and [](#s4){.pf-ref} prove (b), step [](#s5){.pf-ref} proves (c), and steps [](#s6){.pf-ref} and [](#s7){.pf-ref} prove (d).
:::

:::
:::
