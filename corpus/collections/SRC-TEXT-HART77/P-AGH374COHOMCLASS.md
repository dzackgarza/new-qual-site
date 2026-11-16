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
  note: "Read Exercise III.7.4, the definition and uniqueness of a dualizing sheaf with trace in III.7.1--7.2, the canonical-sheaf identification III.7.11--7.13, and Hartshorne's warning in III.7.14 that the preceding construction gives little explicit information about the trace. The source exercise suppresses a necessary normalization: scaling the trace on a smooth subvariety scales its class. The first version of this card put the normalization into the statement; it is now stated at the head of the solution instead, the statement being the printed one."
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
    III.7.14.1(c). The cross-check this note records there, that (b) and
    c(O(d)) = d agree for a hypersurface in P^n, is withdrawn in the event
    of 2026-11-16: it compares a class in H^1(Omega^1) with the class of a
    point and uses part (d) for a hyperplane, so it is not independent.
    Not checked: whether the printed exercise has a
    canonical normalization in the literature; none was found.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Second published-solution search for III.7.4(b) and (d) (issue #121);
    nothing complete was located, and the card keeps its own derivation.
    Read this pass: Yang Pi-Yeh, Hartshorne Solutions (9 June 2019),
    Solution 3.7.4, printed p. 75 of tmp/sources/lfwin-hartshorne-solutions.pdf,
    text version tmp/sources/lfwin-hartshorne-solutions.md -- (a) as in
    step s1 here; (b) cuts Y down to its deg Y points by a general linear
    subspace, computes the factor deg Y there, and then asserts that
    k = H^p(H, Omega^p_H) = H^p(X, Omega^p_X) = k "is just identity from
    the proof in 3.7.3"; so he does move the count back to P^n, by citing
    his own 3.7.3, but the identification he cites is a different one
    (the boundary isomorphism of H^0(O) -> H^1(Omega) there), and the
    transfer by the projection formula that the assertion needs is step
    s3 here; (d) writes c(L_Y) as a Cech cocycle and sends it by the map
    H^1(X, Omega_X) -> H^0(X, O_X) of 3.7.3, whose inverse is a defined
    boundary map, and evaluates it as a sum of coordinate times partial
    derivatives, using homogeneous coordinates and Euler's formula; that
    is a computation for X = P^n only, so his (d) has no treatment of a
    general X. Dongryul Kim, text version
    tmp/sources/hartshorne-solutions-kim.md, has Exercise 3.7.4 on release
    PDF p. 170 with (a) and (c) proved and (b) a fragment ("we can always
    take"), and no (d); the list of problems he has not solved, at the
    head of the text on PDF p. 1, restates the exercise as "Compute this
    for X = P^n and for p = 1". Stacks Project tags read: 0FWC, Section 50.22 (de Rham cohomology as
    a Weil cohomology theory, with the trace map Theta on H^{2d} and the
    statement that the cycle class followed by lambda_X is the degree
    map) and 0FLE, Section 50.9 (the dlog first Chern class into
    H^1(X, Omega^1)). 0FWC is a statement about H^{2p}_{dR}; the
    exercise's eta(Y) is the (p,p) Hodge component in H^p(X, Omega^p),
    and no tag read makes that identification. 0FLE supplies only the map
    c of part (c). Math StackExchange 1794757, text version
    tmp/sources/mse-1794757-cohomology-class-of-a-subvariety.md, has one
    answer, by the account S.M. (2016-05-22), proving (a) only; the text
    version records no acceptance, so "accepted" is not claimed. The two
    Stacks files are tmp/sources/stacks-tags/0FWC.md and 0FLE.md. Checked
    against the book: the printed exercise, printed pp. 249--250; the
    trace and duality inputs III.7.1, III.7.2, III.7.12--7.14, printed
    pp. 240--247; Appendix A's C1, printed p. 430. Not checked: whether
    the printed exercise admits a normalizing convention in the
    literature; none was found in any of the sources read across both
    passes.
- event: solution-reviewed
  by: claude
  date: 2026-11-16
  note: >-
    Repairs on the reader's report of this batch, three of substance. (1) The
    statement is the printed exercise again: the normalization paragraph is
    removed from the problem block and stated at the head of the solution,
    which is where a convention the book does not print belongs. (2) Step s3
    no longer applies the trace to the wrong degree: it names 1_V in
    H^{dim V} by t_V(1_V) = 1, observes that every point class on L equals
    1_L by step s1, and defines 1_{P^n} by t_{P^n}(1_{P^n} sm i_*1) = 1, that
    is, as the class pairing to 1 with the class of a linear P^p. The
    previous version defined 1_L by a trace applied to H^0 and 1_{P^n} by a
    trace applied to H^{n-p}, both ill-typed, and never stated the
    identification the transfer uses. (3) Step s6 is no longer circular. It
    states the divisor case (R) as an input, notes that part (d) is its case
    beta = 1, proves (R) in dimension one from the residue theorem and
    III.7.14.1(c) of the book, and says that for n >= 2 Hartshorne supplies no
    such statement (Remark III.7.14 says the trace is known only to exist).
    The withdrawn sentences are those that took the residue formula as the
    definition of the Gysin map by appeal to the problem statement, and the
    "independent check" for a hypersurface in P^n, which compared a class in
    H^1(Omega^1) with a point class. Also corrected: the audit description of
    Yang's (b) and (d) and of Kim's coverage, and the text versions named for
    Kim, MSE 1794757 and the two Stacks tags. Checked against the book in this
    pass: the printed exercise on pp. 249-250, III.7.1(a) p. 240, III.7.2
    p. 241, III.7.12-7.14 pp. 246-247, II.8.18 p. 179, I.7.7 p. 53, Exercise
    III.7.3 p. 249, Appendix A C1 p. 430. Not checked: no source proving (R)
    for n >= 2 was located, and the card does not claim one.
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
The printed exercise fixes no normalization of the trace. Serre duality supplies
the trace of a dualizing sheaf only up to a nonzero scalar (III.7.2, printed
p. 241; III.7.14, printed p. 247, says of it that "we know only that it
exists"), and parts (b) and (d) assert numerical identities in the cohomology
of $X$, so they hold only for the trace that matches the integers. The
convention adopted here, and used in steps [](#s3){.pf-ref} and
[](#s6){.pf-ref}, is the standard one for canonical sheaves: the trace on
$\Spec k$ is the identity, the trace on a finite reduced $k$-scheme is the sum
of the traces of its points, and the traces are compatible with the Gysin maps
for nonsingular closed immersions. Equivalently, one takes the trace of
Grothendieck--Serre duality rather than an arbitrary scalar multiple of the one
whose existence Serre duality asserts. The remark below records what the book
does and does not determine; part (a) needs no convention at all, because
$\eta(P)$ is defined by duality against the very trace that computes it.

Write $j:Y\hookrightarrow X$ for the closed immersion. We use the normalized Serre pairing
$$
\langle\alpha,\beta\rangle_X
=t_X(\alpha\smile\beta),
$$
between $H^p(X,\Omega_X^p)$ and $H^{n-p}(X,\Omega_X^{n-p})$.
With the compatibility clause of that convention the Gysin morphism
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

Two generators have to be named, and both are fixed by the convention at the
head of the solution. For a nonsingular projective variety $V$ of dimension
$m$, let $1_V\in H^m(V,\Omega_V^m)\cong k$ be the class with $t_V(1_V)=1$.
On $L$, which has dimension $p$, step [](#s1){.pf-ref} says that
$t_L(\eta_L(P))=1$ for every point $P$, so
$$
\eta_L(P)=1_L
$$
for every $P\in Z$: both classes have trace $1$ and $H^p(L,\Omega_L^p)$ is
one-dimensional. Hence
$$
i^*\eta_{\PP^n}(Y)=\eta_L(Z)=d\cdot 1_L
$$
in $H^p(L,\Omega_L^p)$.

The scalar is now read in $H^p(\PP^n,\Omega^p)$. Let
$\alpha_0=i_*1\in H^{n-p}(\PP^n,\Omega_{\PP^n}^{n-p})$ be the Gysin
pushforward of the unit class of $L$. By the compatibility clause of the
convention, the projection formula for $i:L\hookrightarrow\PP^n$ identifies
the two traces, for every $\beta\in H^p(\PP^n,\Omega^p)$:
$$
t_{\PP^n}\bigl(\beta\smile i_*1\bigr)
=t_L\bigl(i^*\beta\smile 1\bigr).
$$
With $\beta=1$ this reads $t_{\PP^n}(1\smile i_*1)=t_L(1_L)=1$, so
$\alpha_0\ne0$; and $H^{n-p}(\PP^n,\Omega^{n-p})\cong k$ by Exercise III.7.3,
so $\alpha_0$ spans that space. Define $1_{\PP^n}\in H^p(\PP^n,\Omega^p)$ to
be the class with
$$
t_{\PP^n}\bigl(1_{\PP^n}\smile \alpha_0\bigr)=1 ,
$$
which exists and is unique because the pairing is nondegenerate: it is the
class pairing to $1$ with the class of the linear $\PP^p$. This is a
normalization and not a consequence of the book. Exercise III.7.3 identifies
$H^p(\PP^n,\Omega^p)$ with $k$, but does not say which generator of the dual
space the trace of Serre duality is, and (b) is false by a scalar for another
choice.

With $\beta=\eta(Y)$, step [](#s2){.pf-ref} and the last display give
$$
t_{\PP^n}\bigl(\eta(Y)\smile \alpha_0\bigr)
=t_L\bigl(i^*\eta(Y)\smile1\bigr)
=d\,\langle 1_L,1\rangle_L
=d\,t_L(1_L)=d ,
$$
and with $\beta=1_{\PP^n}$ the definition of $1_{\PP^n}$ gives
$t_{\PP^n}(1_{\PP^n}\smile\alpha_0)=1$. Both $\eta(Y)$ and
$d\cdot1_{\PP^n}$ therefore pair equally with the spanning class
$\alpha_0$, and the Serre pairing is nondegenerate, so
$$
\eta(Y)=d\cdot1_{\PP^n},
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
The two sides are elements of $H^1(X,\Omega_X)$, and they are seen to be equal
by pairing both with every class of $H^{n-1}(X,\Omega_X^{n-1})$; the one input
this uses is the divisor case (R) below, which the book proves for curves and
which for $n\ge2$ is part of the trace convention.

::: pf-proof

Let
$$
\alpha\in H^{n-1}(X,\Omega_X^{n-1}).
$$
By the definition of $\eta(Y)$ and the adjunction identity of the head of the
solution,
$$
\langle\eta(Y),\alpha\rangle_X
=t_X(j_*(1)\smile\alpha)
=t_Y(j^*\alpha).
$$
By step [](#s5){.pf-ref}, $c(\mcl(Y))$ is the Čech class
$$
\left\{\frac{df_i}{f_i}-\frac{df_j}{f_j}\right\}_{ij}
$$
of the cover $(U_i)$ on which $Y$ has local equations $f_i=0$.

**The input (R).** For a nonsingular divisor $Y\subset X$ of a nonsingular
projective $X$ of dimension $n$, and every $\beta\in
H^{n-1}(Y,\Omega_Y^{n-1})$,
$$
j_*(\beta)=c(\mcl(Y))\smile\beta,
$$
with the right-hand side read through the lifts $\widetilde\beta_i$; in other
words the Gysin map of a divisor is cup product with the $d\log$ class of
$\mcl(Y)$, and in particular $j_*(1)=c(\mcl(Y))$ is the Poincaré residue of
the unit class. Part (d) is the case $\beta=1$ of (R).

(R) is not a consequence of Chapter III for $n\ge2$. Remark III.7.14 (printed
p. 247) says of the trace of a nonsingular projective variety that "we don't
have much information ... We know only that it exists", and it states the
residue description for curves only; the identification of the two is exactly
the extra structure the exercise's numerical assertion needs, which is why the
convention at the head of the solution includes it. In dimension one (R) is
proved in the book: let $X$ be a curve, $Y=\{P\}$, $f$ a local parameter at
$P$, and $\alpha\in H^0(X,\Omega_X^0)=H^0(X,\OO_X)$; the trace on a curve is
the sum of residues (Remark III.7.14), and Theorem III.7.14.1(c) (printed
p. 247) gives
$$
t_X\bigl(c(\OO(P))\smile\alpha\bigr)
=\operatorname{res}_P\bigl(\alpha\,f^{-1}df\bigr)
=\alpha(P)\,v_P(f)=\alpha(P)
=t_P(j^*\alpha),
$$
with the constant $+1$ because $\operatorname{res}_P(f^{-1}df)=v_P(f)\cdot1$
and $v_P(f)=1$ for a local parameter. So (R), and with it part (d), is a
theorem in dimension one and a convention in higher dimension.

Granting (R), the two classes pair equally with every $\alpha$:
$$
\langle c(\mcl(Y)),\alpha\rangle_X
=t_X\bigl(c(\mcl(Y))\smile\alpha\bigr)
=t_X\bigl(j_*(1)\smile\alpha\bigr)
=t_Y(j^*\alpha)
=\langle\eta(Y),\alpha\rangle_X .
$$
The Serre pairing is nondegenerate, so
$$
c(\mcl(Y))=\eta(Y).
$$
This proves part (d).

:::

:::

::: pf-qed

Step [](#s1){.pf-ref} proves part (a) with no convention, steps [](#s2){.pf-ref} and [](#s3){.pf-ref} prove part (b) under the trace convention stated at the head of the solution, step [](#s4){.pf-ref} proves part (c), and steps [](#s5){.pf-ref} and [](#s6){.pf-ref} prove part (d) from input (R): in dimension one (R) is Theorem III.7.14.1, and for $n\ge2$ it is the divisor case of the same convention, not a theorem in the book.

:::

:::

:::

::: {.remark title="Trace normalization"}
As written in the source, the exercise suppresses a normalization needed to make its numerical assertions canonical, and the printed text supplies no canonical one. The passages are these.

III.7.1(a) is the assertion $H^n(X,\omega_X)\cong k$ for $X=\PP^n_k$, and it continues "Fix one such isomorphism"; the isomorphism is a choice, so the trace $t$ it determines is defined only up to a nonzero scalar. III.7.2 (printed p. 241) makes the trace part of the data: a dualizing sheaf is a *pair* $(\omega_X^\circ,t)$, uniqueness is uniqueness of the pair, and replacing $t$ by $ct$ gives a different pair representing the same functor. Corollary III.7.12 (printed p. 246) then says only that for $X$ projective and nonsingular $\omega_X^\circ$ is *isomorphic* to $\omega_X$; it does not normalize the isomorphism, and the isomorphism its proof produces comes from $\wedge^r(\mathcal I/\mathcal I^2)^\vee$ tensoring, not from a normalization of $t$. Remark III.7.14 (printed p. 247) states the position: "even for a nonsingular projective variety $X$, we don't have much information about the trace map $t:H^n(X,\omega)\to k$. We know only that it exists."

A natural choice does exist on $\PP^n$ and the book records it without using it: Remark III.7.1.1 (printed pp. 240--241) gives the Čech cocycle
$$\alpha=\frac{x_0^n}{x_1\cdots x_n}\,d\Bigl(\frac{x_1}{x_0}\Bigr)\wedge\cdots\wedge d\Bigl(\frac{x_n}{x_0}\Bigr),$$
which "determines a generator of $H^n(X,\omega)$, which is stable under change of variables". That fixes one isomorphism in III.7.1(a), but nothing in the text compares it with the trace on a point or on a divisor.

The other side, part (d), is canonical: Appendix A defines the Chern classes in the Chow ring $A(X)$, with the normalization C1 (printed p. 430), "If $\mathcal E\cong\mathcal L(D)$ for a divisor $D$, $c_t(\mathcal E)=1+Dt$", so $c_1$ of a line bundle is the class of its divisor with no scalar freedom. The exercise's numerical identities can therefore hold only if the trace is normalized to match that integer, which is what the convention at the head of the solution fixes: $t_{\Spec k}=\operatorname{id}$, additivity on finite reduced $k$-schemes, and compatibility with the Gysin maps of nonsingular closed immersions. It is stated in the solution and not in the problem, because it is not in the printed exercise; the printed text says only "Fix one such isomorphism". Part (a) is the first clause, with $Y=P$ a closed point, and needs no convention beyond it: $\eta(P)$ is defined by duality against $t_X$ itself. Part (b) uses the compatibility clause in step [](#s3){.pf-ref} to fix which generator of $H^p(\PP^n,\Omega^p)$ the number $\deg Y$ is measured against. Part (d) uses the same clause in its divisor form, which is input (R) of step [](#s6){.pf-ref}: for $n\ge2$ that is the one statement of the exercise the book does not supply, and it is recorded there as a convention rather than proved.
:::
