---
schema: qual/card@1
id: P-AGH374COHOMCLASS
kind: problem
title: The cohomology class of a subvariety
classification:
  areas:
  - algebraic-geometry
  topics:
  - Serre Duality
  - Sheaves of Differentials
  - Intersection Theory
  - Picard Group
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: "Read Exercise III.7.4, the definition and uniqueness of a dualizing sheaf with trace in III.7.1--7.2, the canonical-sheaf identification III.7.11--7.13, and Hartshorne's warning in III.7.14 that the preceding construction gives little explicit information about the trace. The source exercise suppresses a necessary normalization: scaling the trace on a smooth subvariety scales its class. The statement below makes the standard trace/Gysin normalization explicit before proving the four requested assertions."
- event: solution-written
  by: chatgpt
  date: 2026-09-18
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Step-by-step pass against the book. III.7.1(a) printed p. 240 (Fix one
    such isomorphism), III.7.2 p. 241 (the trace is part of the dualizing
    pair), III.7.1.1 pp. 240-241 (the Cech cocycle generator), III.7.12 p.
    246, III.7.13 p. 247 (the duality isomorphism the exercise uses),
    III.7.14 p. 247 (the trace is known only to exist), III.7.14.1(c) p. 247
    (res_P f^-1 df = v_P(f)), Appendix A C1 p. 430 (c_1(L(D)) = D), II.8.18
    p. 179 (Bertini, every characteristic), I.7.7 p. 53 (Bezout), Exercise
    7.3 p. 249. Corrected two steps: in (b) the scalar was transferred from
    H^p(L,Omega^p) to H^p(P^n,Omega^p) by asserting that restriction carries
    the normalized generator to the normalized generator, and is now
    transferred by the projection formula t_Pn(beta cup i_*1) = t_L(i^*beta
    cup 1) with i_*1 spanning H^{n-p}; in (d) the residue input is now
    stated as the Poincare residue with its constant checked against
    III.7.14.1(c) and cross-checked for a hypersurface in P^n, where (b) and
    c(O(d)) = d must agree. Not checked: whether the printed exercise has a
    canonical normalization in the literature; none was found.
---

::: {.problem}
Let $X$ be a nonsingular projective variety of dimension $n$ over an algebraically closed field $k$. Let $Y$ be a nonsingular subvariety of codimension $p$, hence of dimension $n-p$. From the natural map $\Omega_X \tensor \mco_Y \to \Omega_Y$ of (II, 8.12) we deduce a map $\Omega_X^{n-p} \to \Omega_Y^{n-p}$. This induces a map on cohomology
$$
H^{n-p}(X, \Omega_X^{n-p}) \to H^{n-p}(Y, \Omega_Y^{n-p})
.$$
Now $\Omega_Y^{n-p} = \omega_Y$ is a dualizing sheaf for $Y$, so we have the trace map
$$
t_Y: H^{n-p}(Y, \Omega_Y^{n-p}) \to k
.$$
Composing, we obtain a linear map $H^{n-p}(X, \Omega_X^{n-p}) \to k$. By (7.13) this corresponds to an element $\eta(Y) \in H^p(X, \Omega_X^p)$, which we call the \dfn{cohomology class of $Y$}.

For this exercise, use the standard compatible normalization of the trace maps on canonical sheaves: the trace on $\Spec k$ is the identity, the trace on a finite reduced $k$-scheme is the sum of the traces of its points, and traces are compatible with the Gysin maps for nonsingular closed immersions. Equivalently, use the trace normalization from Grothendieck--Serre duality rather than an arbitrary scalar multiple of the trace supplied merely by the existence statement of Serre duality.

(a) If $P \in X$ is a closed point, show that $t_X(\eta(P)) = 1$, where $\eta(P) \in H^n(X, \Omega^n)$ and $t_X$ is the trace map.

(b) If $X = \PP^n$, identify $H^p(X, \Omega^p)$ with $k$ by (Ex. 7.3), and show that $\eta(Y) = (\deg Y) \cdot 1$, where $\deg Y$ is the degree of $Y$ as a projective variety (I, §7).

   Hint: cut with a hyperplane $H \subseteq X$, and use Bertini's theorem (II, 8.18) to reduce to the case where $Y$ is a finite set of points.

(c) For any scheme $X$ of finite type over $k$, we define a homomorphism of sheaves of abelian groups $d\log: \mco_X^* \to \Omega_X$ by $d\log(f) = f^{-1} \, df$. Here $\mco_X^*$ is a group under multiplication, and $\Omega_X$ is a group under addition. This induces a map on cohomology
$$
\Pic X = H^1(X, \mco_X^*) \to H^1(X, \Omega_X)
,$$
which we denote by $c$. See (Ex. 4.5).

(d) Returning to the hypotheses above, suppose $p = 1$. Show that $\eta(Y) = c(\mcl(Y))$, where $\mcl(Y)$ is the invertible sheaf corresponding to the divisor $Y$.
:::

::: {.solution}
Write $j:Y\hookrightarrow X$ for the closed immersion. We use the normalized Serre pairing
$$
\langle\alpha,\beta\rangle_X
=t_X(\alpha\smile\beta),
$$
between $H^p(X,\Omega_X^p)$ and $H^{n-p}(X,\Omega_X^{n-p})$.
With the trace normalization stated in the problem, the Gysin morphism
$$
j_*:H^q(Y,\Omega_Y^q)\longrightarrow H^{q+p}(X,\Omega_X^{q+p})
$$
is characterized by the adjunction identity
$$
\langle j_*(a),b\rangle_X
=\langle a,j^*b\rangle_Y.
$$
In particular, the class defined in the problem is
$$
\eta(Y)=j_*(1).
$$

::: pf

::: {.pf-step #s1}

For a closed point $P\in X$,
$$
\boxed{t_X(\eta(P))=1}.
$$

::: pf-proof

Here $p=n$, so the functional defining $\eta(P)$ is the composite
$$
H^0(X,\OO_X)\xrightarrow{j^*}H^0(P,\OO_P)
\xrightarrow{t_P}k.
$$
Since $X$ is projective and integral over the algebraically closed field $k$,
$$
H^0(X,\OO_X)=k,
$$
and since $P\cong\Spec k$, the restriction map is the identity on $k$.
By the chosen normalization $t_P=\operatorname{id}_k$, so the functional sends $1$ to $1$.

Under Serre duality, evaluating that functional at $1\in H^0(X,\OO_X)$ is the same as pairing $\eta(P)$ with $1$:
$$
1
=\langle\eta(P),1\rangle_X
=t_X(\eta(P)).
$$
This proves part (a).

:::

:::

::: {.pf-step #s2}

Cohomology classes are compatible with transverse intersection by a nonsingular hyperplane: if $H\subseteq X$ is nonsingular and meets $Y$ transversely, then
$$
i^*\eta_X(Y)=\eta_H(Y\cap H),
$$
where $i:H\hookrightarrow X$.

::: pf-proof

Let $Z=Y\cap H$ and write the transverse Cartesian square
$$
\begin{array}{ccc}
Z&\xrightarrow{j_H}&H\\
\downarrow&&\downarrow i\\
Y&\xrightarrow{j}&X.
\end{array}
$$
For regular closed immersions meeting transversely, the normalized Gysin maps satisfy base change
$$
i^*j_*=(j_H)_*\,i_Y^*.
$$
Applying this to $1\in H^0(Y,\OO_Y)$ gives
$$
i^*\eta_X(Y)
=i^*j_*(1)
=(j_H)_*(1)
=\eta_H(Z).
$$
This is exactly the asserted compatibility.

:::

:::

::: {.pf-step #s3}

If $X=\PP^n$ and $Y$ has codimension $p$, then
$$
\boxed{\eta(Y)=(\deg Y)\cdot1\in H^p(\PP^n,\Omega_{\PP^n}^p)\cong k}.
$$

::: pf-proof

By Exercise III.7.3,
$$
H^p(\PP^n,\Omega^p)\cong k.
$$
Choose a general linear subspace
$$
L\cong\PP^p\subseteq\PP^n
$$
of complementary dimension to $Y$.
By Bertini's theorem (II, 8.18, printed p. 179), for a general $L$ the scheme $Y\cap L$ is regular of dimension $0$, hence a reduced set of distinct points; by Bézout's theorem (I.7.7, printed p. 53) applied to the $n-p$ successive general hyperplane sections, each meeting the previous one properly with intersection multiplicity $1$ everywhere, the degree of $Y\cap L$ is $\deg Y$. Thus
$$
Z=Y\cap L=\{P_1,\ldots,P_d\},
\qquad d=\deg Y.
$$
Repeated application of step [](#s2){.pf-ref} gives
$$
\eta_L(Z)=i^*\eta_{\PP^n}(Y).
$$

The Gysin map is additive on a disjoint union of points, so
$$
\eta_L(Z)=\sum_{a=1}^d\eta_L(P_a).
$$
By step [](#s1){.pf-ref} each point class has trace one. Since
$$
H^p(L,\Omega_L^p)\cong k
$$
and its trace identifies the standard generator with $1$, we obtain
$$
\eta_L(Z)=d\cdot1.
$$

What has been shown so far is the identity in $H^p(L,\Omega_L^p)$,
$$
i^*\eta_{\PP^n}(Y)=d\cdot 1_L ,
$$
where $1_L$ is the class with $\langle 1_L,\alpha_L\rangle_L=t_L(\alpha_L)$ for $\alpha_L=1\in H^0(L,\OO_L)$; the scalar $d$ still has to be read in $H^p(\PP^n,\Omega^p)$, and that is what the trace normalization of the statement supplies.

Let $\alpha_0=i_*1\in H^{n-p}(\PP^n,\Omega_{\PP^n}^{n-p})$ be the Gysin pushforward of the unit class of $L$; it is a nonzero element, and $H^{n-p}(\PP^n,\Omega^{n-p})\cong k$ by Exercise III.7.3, so $\alpha_0$ spans that space. Because the normalized traces are compatible with the Gysin maps of nonsingular closed immersions, the projection formula for $i:L\hookrightarrow\PP^n$ gives, for every $\beta\in H^p(\PP^n,\Omega^p)$,
$$
t_{\PP^n}\bigl(\beta\smile i_*1\bigr)
=t_L\bigl(i^*\beta\smile 1\bigr).
$$
By definition of $\eta$ and step [](#s2){.pf-ref},
$$
t_{\PP^n}\bigl(\eta(Y)\smile i_*1\bigr)
=t_L\bigl(i^*\eta(Y)\smile1\bigr)
=\langle i^*\eta(Y),1\rangle_L
=d ,
$$
while the same formula with $\beta=1_{\PP^n}$, the class with $\langle 1_{\PP^n},\alpha\rangle=t_{\PP^n}(\alpha)$, gives
$$
t_{\PP^n}\bigl(1_{\PP^n}\smile i_*1\bigr)=t_L\bigl(1\bigr)=1 .
$$
Both $\eta(Y)$ and $d\cdot1_{\PP^n}$ therefore pair equally with the spanning class $\alpha_0=i_*1$, and the Serre pairing is linear and nondegenerate, so
$$
\eta(Y)=(d)\cdot1_{\PP^n},
$$
which is part (b) with $d=\deg Y$.

:::

:::

::: {.pf-step #s4}

The rule
$$
d\log(f)=f^{-1}df
$$
is a morphism of sheaves of abelian groups
$$
d\log:\OO_X^*\longrightarrow\Omega_X.
$$

::: pf-proof

For local units $f,g$,
$$
\begin{aligned}
d\log(fg)
&=(fg)^{-1}d(fg)\\
&=f^{-1}g^{-1}(f\,dg+g\,df)\\
&=f^{-1}df+g^{-1}dg\\
&=d\log(f)+d\log(g).
\end{aligned}
$$
The construction commutes with restriction to smaller open sets because Kähler differentiation does.
Therefore it is a morphism from the multiplicative sheaf $\OO_X^*$ to the additive sheaf $\Omega_X$.
Passing to first cohomology and using
$$
\Pic X\cong H^1(X,\OO_X^*)
$$
gives the homomorphism
$$
c:\Pic X\longrightarrow H^1(X,\Omega_X)
$$
required in part (c).

:::

:::

::: {.pf-step #s5}

If $Y\subseteq X$ is a nonsingular divisor with local equations $f_i=0$ on an open cover $(U_i)$, then $c(\mcl(Y))$ is represented by the Čech cocycle
$$
\left\{\frac{df_i}{f_i}-\frac{df_j}{f_j}\right\}_{ij}.
$$

::: pf-proof

The invertible sheaf $\mcl(Y)=\OO_X(Y)$ has local generator $e_i=f_i^{-1}$ on $U_i$.
Use the Čech convention in which the transition function $g_{ij}$ is defined by
$$
e_j=g_{ij}e_i.
$$
Then
$$
g_{ij}=\frac{f_i}{f_j},
$$
and its image under $d\log$ is
$$
d\log\!\left(\frac{f_i}{f_j}\right)
=\frac{df_i}{f_i}-\frac{df_j}{f_j}.
$$
This is the displayed cocycle.

:::

:::

::: {.pf-step #s6}

For a nonsingular divisor $Y\subseteq X$,
$$
\boxed{\eta(Y)=c(\mcl(Y))\in H^1(X,\Omega_X)}.
$$

::: pf-proof

Let
$$
\alpha\in H^{n-1}(X,\Omega_X^{n-1}).
$$
By definition of $\eta(Y)$,
$$
\langle\eta(Y),\alpha\rangle_X
=t_Y(j^*\alpha).
$$

On a cover on which $Y$ is given by the equations $f_i$, the Gysin map of the divisor $Y$ is the Poincaré residue: for a form $\beta$ on $Y$, its image $j_*\beta\in H^n(X,\Omega_X^n)$ is represented by the Čech class
$$
\frac{df_i}{f_i}\wedge\widetilde\beta_i
-
\frac{df_j}{f_j}\wedge\widetilde\beta_j,
$$
where the $\widetilde\beta_i$ are local lifts to $X$, that is, $j_*\beta$ is the cup product of $\beta$ with the Čech cocycle
$$
\left\{\frac{df_i}{f_i}-\frac{df_j}{f_j}\right\}_{ij}
$$
of step [](#s5){.pf-ref}. The constant is $+1$: on a curve, with $f$ a local parameter at $P$ and $\beta=1$, this class is $df/f$, and Theorem III.7.14.1(c) (printed p. 247) gives $\operatorname{res}_P(f^{-1}df)=v_P(f)\cdot1=1$. Hartshorne states the residue only in dimension one --- Remark III.7.14 (printed p. 247) says that in general the trace is known only to exist --- so in dimension above one the displayed formula is taken as the definition of the Gysin map, which is one of the normalizations the problem statement fixes.
Compatibility of the normalized trace with this residue map gives
$$
t_X\bigl(c(\mcl(Y))\smile\alpha\bigr)
=t_Y(j^*\alpha).
$$
The constant can be checked independently in the case $X=\PP^n$, $Y$ a hypersurface: by step [](#s3){.pf-ref} $\eta(Y)$ is $(\deg Y)$ times the class of a point, and $c(\mcl(Y))=c(\OO(\deg Y))=\deg Y$ times the class of a hyperplane, so the two sides agree there.
Thus
$$
\langle c(\mcl(Y)),\alpha\rangle_X
=\langle\eta(Y),\alpha\rangle_X
$$
for every $\alpha$.
The Serre pairing is nondegenerate, so
$$
c(\mcl(Y))=\eta(Y).
$$
This proves part (d).

:::

:::

::: pf-qed

Step [](#s1){.pf-ref} proves part (a), steps [](#s2){.pf-ref} and [](#s3){.pf-ref} prove part (b), step [](#s4){.pf-ref} proves part (c), and steps [](#s5){.pf-ref} and [](#s6){.pf-ref} prove part (d).

:::

:::

:::

::: {.remark title="Trace normalization"}
As written in the source, the exercise suppresses a normalization needed to make its numerical assertions canonical, and the printed text supplies no canonical one. The passages are these.

III.7.1(a) is the assertion $H^n(X,\omega_X)\cong k$ for $X=\PP^n_k$, and it continues "Fix one such isomorphism"; the isomorphism is a choice, so the trace $t$ it determines is defined only up to a nonzero scalar. III.7.2 (printed p. 241) makes the trace part of the data: a dualizing sheaf is a *pair* $(\omega_X^\circ,t)$, uniqueness is uniqueness of the pair, and replacing $t$ by $ct$ gives a different pair representing the same functor. Corollary III.7.12 (printed p. 246) then says only that for $X$ projective and nonsingular $\omega_X^\circ$ is *isomorphic* to $\omega_X$; it does not normalize the isomorphism, and the isomorphism its proof produces comes from $\wedge^r(\mathcal I/\mathcal I^2)^\vee$ tensoring, not from a normalization of $t$. Remark III.7.14 (printed p. 247) states the position: "even for a nonsingular projective variety $X$, we don't have much information about the trace map $t:H^n(X,\omega)\to k$. We know only that it exists."

A natural choice does exist on $\PP^n$ and the book records it without using it: Remark III.7.1.1 (printed pp. 240--241) gives the Čech cocycle
$$\alpha=\frac{x_0^n}{x_1\cdots x_n}\,d\Bigl(\frac{x_1}{x_0}\Bigr)\wedge\cdots\wedge d\Bigl(\frac{x_n}{x_0}\Bigr),$$
which "determines a generator of $H^n(X,\omega)$, which is stable under change of variables". That fixes one isomorphism in III.7.1(a), but nothing in the text compares it with the trace on a point or on a divisor.

The other side, part (d), is canonical: Appendix A defines the Chern classes in the Chow ring $A(X)$, with the normalization C1 (printed p. 430), "If $\mathcal E\cong\mathcal L(D)$ for a divisor $D$, $c_t(\mathcal E)=1+Dt$", so $c_1$ of a line bundle is the class of its divisor with no scalar freedom. The exercise's numerical identities can therefore hold only if the trace is normalized to match that integer, which is what the statement on this card fixes: $t_{\Spec k}=\operatorname{id}$, additivity on finite reduced $k$-schemes, and compatibility with the Gysin maps. Part (a) is exactly the first of these, with $Y=P$ a closed point, and step [](#s3){.pf-ref} uses the third.
:::
