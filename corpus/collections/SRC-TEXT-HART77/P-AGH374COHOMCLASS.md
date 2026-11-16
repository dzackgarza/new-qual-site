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
    subspace and then asserts that k = H^p(H, Omega^p_H) = H^p(X,
    Omega^p_X) = k is the identity, which is the normalization step s3
    now supplies by the projection formula, and he never moves the count
    from the subspace back to P^n; (d) writes c(L_Y) as a Cech cocycle
    and then sends it by a map H^1(X, Omega_X) -> H^0(X, O_X) whose value
    is written as a sum of coordinate times partial derivatives, which is
    neither a defined map nor the duality pairing. Dongryul Kim, release
    PDF p. 170, lists Exercise 3.7.4 in his "problems I haven't solved".
    Stacks Project tags read: 0FWC, Section 50.22 (de Rham cohomology as
    a Weil cohomology theory, with the trace map Theta on H^{2d} and the
    statement that the cycle class followed by lambda_X is the degree
    map) and 0FLE, Section 50.9 (the dlog first Chern class into
    H^1(X, Omega^1)). 0FWC is a statement about H^{2p}_{dR}; the
    exercise's eta(Y) is the (p,p) Hodge component in H^p(X, Omega^p),
    and no tag read makes that identification. 0FLE supplies only the map
    c of part (c). Math StackExchange 1794757 and its accepted answer by
    the account S.M. (2016-05-22) prove (a) only. Checked against the
    book: the printed exercise, printed pp. 249--250; the trace and
    duality inputs III.7.1, III.7.2, III.7.12--7.14, printed pp. 240--247;
    Appendix A's C1, printed p. 430. Not checked: whether the printed
    exercise admits a normalizing convention in the literature; none was
    found in any of the sources read across both passes.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Second pass on the reader's report of this batch, checked against the
    book and its text version. Restored the three events the report names as
    rewritten in place: the note of 2026-09-18 by chatgpt again ends where it
    ended, without the sentence about the 2026-11-16 move of the
    normalization; the note of 2026-11-11 again records the cross-check for a
    hypersurface in P^n as it was written on that date; and the note of
    2026-11-16 again carries the descriptions of Yang, of Kim and of Math
    StackExchange 1794757 written then. What those descriptions got wrong is
    corrected here and not in them: Yang's (b) does move the count back to
    P^n, by citing his own 3.7.3, though that citation is to a different
    identification; his (d) is a computation in homogeneous coordinates
    using Euler's formula, defined for X = P^n only; Kim's source has
    Exercise 3.7.4 on release PDF p. 170 with (a) and (c) proved, (b) a
    fragment and no (d), and his doubt stands in his list of problems he has
    not solved on PDF p. 1, not in a list of corrections; and the MSE answer
    is not recorded as accepted. The cross-check named in the note of
    2026-11-11 is not independent, as the note of 2026-11-16 says: it
    compares a class in H^1(Omega^1) with a class of a point.

    The mathematics of the card is repaired in four places. (1) The head of
    the solution now states four inputs and says which the book proves:
    (N) the trace at points, (G) the adjunction definition of Gysin maps,
    which is forced by the exercise's own definition of eta(Y), (R) the
    divisor case, and (B) base change for a transverse hyperplane section.
    The earlier text claimed the traces are "compatible with the Gysin
    maps", which with (G) is automatic and constrains nothing, and it called
    (R) part of the convention while stating only (N). (2) Step s3's use of
    "1" in H^p(P^n, Omega^p) before 1_{P^n} is defined, and of i^*1 = 1_L,
    is gone: alpha_0 = i_*(1) is the class of the linear subspace and is
    proved nonzero by restricting along the hyperplanes that cut L out, and
    the pairing then goes through (G) alone. (3) Step s5's transition
    convention is flipped to s_i = g_ij s_j, the one Hartshorne's Cech
    differential carries, so that the cocycle is df_j/f_j - df_i/f_i; with
    the earlier convention the constant in (R) is -1, as the reader
    computed. (4) Step s6 now compares the Cech class with the residue trace
    of Remark III.7.14 through the Cech complex of the flasque resolution,
    which is where the sign is decided, and states that (d) for n >= 2 is
    proved relative to (R) and that (R) itself is not proved there; "This
    proves part (d)" is no longer said without that qualification. Step s2's
    base change is named as input (B) instead of being asserted as a fact
    about "the normalized Gysin maps", and the card says that (B) is the
    step the printed hint uses and that no source proving it for n >= 2 was
    located. Checked against the book in this pass, in
    tmp/sources/hartshorne-1977-algebraic-geometry.md: the printed exercise
    on pp. 249-250, the Cech complex of III.4 on p. 218, III.7.1(a) p. 240,
    III.7.1.1 pp. 240-241, III.7.2 p. 241, III.7.12-7.13 pp. 246-247,
    Remark III.7.14 and Theorems III.7.14.1, 7.14.2 on pp. 247-248,
    Exercise III.7.3 p. 249, Appendix A C1 p. 430. Not checked: no source
    proving (R) or (B) for n >= 2 was located.
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
exists"), and parts (b) and (d) assert numerical identities, so they hold only
for the trace that matches the integers. What this solution uses is the
following, and nothing else.

(N) The trace on $\Spec k$ is the identity, and the trace on a finite reduced
$k$-scheme is the sum of the traces of its points.

(G) For a nonsingular closed immersion $j:Y\hookrightarrow X$ of codimension $p$
the Gysin map
$$
j_*:H^q(Y,\Omega_Y^q)\longrightarrow H^{q+p}(X,\Omega_X^{q+p})
$$
is defined by adjunction with $j^*$ under the Serre pairing
$$
\langle\alpha,\beta\rangle_V=t_V(\alpha\smile\beta),
\qquad
\langle j_*(a),b\rangle_X=\langle a,j^*b\rangle_Y .
$$
This is forced and not a choice: the exercise defines $\eta(Y)$ as the class
whose functional is $b\mapsto t_Y(j^*b)$, so $\eta(Y)=j_*(1)$ with $j_*$ as in
(G). In particular no separate clause "the traces are compatible with Gysin
maps" is a constraint on the trace, because with (G) the identity
$t_X(j_*(a)\smile b)=t_Y(a\smile j^*b)$ holds by definition.

(R) For a nonsingular divisor $\iota:Y\hookrightarrow X$ of a nonsingular
projective $X$ of dimension $n$, and every $\nu\in H^{n-1}(X,\Omega_X^{n-1})$,
$$
t_X\bigl(c(\mcl(Y))\smile\nu\bigr)=t_Y(\restrictionof{\nu}{Y}),
$$
where $c$ is the $d\log$ map of part (c). Equivalently, by (G), the Gysin map
of a divisor is cup product with the $d\log$ class: $\iota_*(\beta)$ pairs with
every $\nu$ as $c(\mcl(Y))\smile\beta$ does, for every lift of $\beta$.

(B) Base change for a transverse hyperplane section: if $H\subseteq X$ is a
nonsingular divisor meeting the nonsingular $Y$ transversely, and $Z=Y\cap H$,
then
$$
i^*j_*=(j_H)_*\,i_Y^*
$$
for the four inclusions of the square of step [](#s2){.pf-ref}; in this
solution $H$ is always a hyperplane of $\PP^n$. This is the compatibility the
printed hint uses when it says to "cut with a hyperplane $H\subseteq X$"; it is
the projection formula for the trace, read for the transverse pair $(Y,H)$.

(N) is a normalization, and part (a) uses only (N). (R) is the substantive
input, and part (d) is its case $\beta=1$. (B) is the second one, and part (b)
is its consequence.

Of these, the book proves (R) for curves, and step [](#s6){.pf-ref} derives it
there from the residue description of the trace in Remark III.7.14 (printed
pp. 247--248), sign included. It proves nothing of the kind for $\dim X\ge2$:
Remark III.7.14 says of the trace that "we know only that it exists", and its
residue construction is stated for curves. Neither (R) nor (B) for higher
dimension is proved in this card, and no source proving them was located in the
two search passes recorded above; both are the standard compatibility of the
trace of Grothendieck--Serre duality with cycle classes, which Hartshorne's
Chapter III does not contain. Parts (b) and (d) are therefore theorems relative
to (R) and (B), and open with respect to the book alone. The remark below
records what the book does and does not determine.

Write $j:Y\hookrightarrow X$ for the closed immersion. We use the normalized Serre pairing
$$
\langle\alpha,\beta\rangle_X
=t_X(\alpha\smile\beta),
$$
between $H^p(X,\Omega_X^p)$ and $H^{n-p}(X,\Omega_X^{n-p})$.
With (G) the Gysin morphism
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

That the four inputs are consistent --- that there is a trace satisfying (N),
(R) and (B) at once, and it is unique up to the normalization (N) --- is a
theorem of Grothendieck--Serre duality, and it is neither proved nor cited
here. What is proved below is that the exercise's four assertions follow from
those inputs, and that (R) itself is a theorem of the book in dimension one.

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
\downarrow i_Y&&\downarrow i\\
Y&\xrightarrow{j}&X.
\end{array}
$$
The assertion is (B) of the head of the solution, the base-change identity
$i^*j_*=(j_H)_*i_Y^*$. Both sides are maps
$H^q(Y,\Omega_Y^q)\to H^{q+p}(H,\Omega_H^{q+p})$, and applying it to
$1\in H^0(Y,\OO_Y)$ gives
$$
i^*\eta_X(Y)
=i^*j_*(1)
=(j_H)_*(1)
=\eta_H(Z),
$$
which is the asserted compatibility. This is the one step of part (b) that the
book does not supply: the identity is the projection formula for the trace of
the transverse pair $(Y,H)$, and the proof of the printed hint's instruction to
cut with a hyperplane is exactly this statement. It is not derived here from
(N) or (R), and no source proving it for $\dim X\ge2$ was located in the two
search passes recorded above.

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
$\alpha_0=i_*(1)\in H^{n-p}(\PP^n,\Omega_{\PP^n}^{n-p})$ be the Gysin
pushforward of the unit class $1\in H^0(L,\OO_L)$; by (G) and the exercise's
definition it is the class $\eta_{\PP^n}(L)$ of the linear subspace. It is
nonzero. Indeed, restricting along the $n-p$ hyperplanes that cut $L$ out, as
in step [](#s2){.pf-ref}, gives
$$
\restrictionof{\alpha_0}{L}=\eta_L(L)=1_L\ne0,
$$
since $\langle\eta_L(L),\beta\rangle_L=t_L(1\smile\beta)=t_L(\beta)$ for every
$\beta\in H^0(L,\Omega_L^0)$, so $\eta_L(L)$ is the class of trace $1$; a class
whose restriction to $L$ is nonzero is nonzero. By Exercise III.7.3 the space
$H^{n-p}(\PP^n,\Omega^{n-p})$ is one-dimensional, so $\alpha_0$ spans it.

Define $1_{\PP^n}\in H^p(\PP^n,\Omega^p)$ to be the class with
$$
t_{\PP^n}\bigl(1_{\PP^n}\smile \alpha_0\bigr)=1 ,
$$
which exists and is unique because $\alpha_0\ne0$ and the Serre pairing is
nondegenerate: it is the class pairing to $1$ with the class of the linear
$\PP^p$. This is a normalization and not a consequence of the book. Exercise
III.7.3 identifies $H^p(\PP^n,\Omega^p)$ with $k$, but does not say which
generator of the dual space the trace of Serre duality is, and (b) is false by
a scalar for another choice.

By (G) applied to $i:L\hookrightarrow\PP^n$ and to $1\in H^0(L,\OO_L)$, for
every $\beta\in H^p(\PP^n,\Omega^p)$ one has
$$
t_{\PP^n}\bigl(\beta\smile\alpha_0\bigr)
=t_{\PP^n}\bigl(\beta\smile i_*(1)\bigr)
=t_L\bigl(i^*\beta\smile1\bigr)
=t_L(i^*\beta).
$$
With $\beta=\eta(Y)$ this and step [](#s2){.pf-ref} give
$$
t_{\PP^n}\bigl(\eta(Y)\smile \alpha_0\bigr)
=t_L\bigl(i^*\eta(Y)\bigr)
=t_L\bigl(d\cdot1_L\bigr)=d ,
$$
while the definition of $1_{\PP^n}$ gives
$t_{\PP^n}(1_{\PP^n}\smile\alpha_0)=1$. So $\eta(Y)$ and $d\cdot1_{\PP^n}$ pair
equally with $\alpha_0$; since $\alpha_0\ne0$ and the Serre pairing is
nondegenerate, $\beta\mapsto t_{\PP^n}(\beta\smile\alpha_0)$ is injective, and
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
Use the convention $s_i=g_{ij}s_j$ for the transition functions of a line
bundle, which is the one Hartshorne's Čech complex carries (printed p. 218):
its differential is $(d\alpha)_{i_0i_1}=\alpha_{i_1}-\alpha_{i_0}$, and
$g_{ij}g_{jk}=g_{ik}$ is the multiplicative form of
$(d\alpha)_{ijk}=0$. With $s_i=e_i$ this gives
$f_i^{-1}=g_{ij}f_j^{-1}$, that is
$$
g_{ij}=\frac{f_j}{f_i},
$$
and its image under $d\log$ is
$$
d\log\!\left(\frac{f_j}{f_i}\right)
=\frac{df_j}{f_j}-\frac{df_i}{f_i}.
$$
This is the displayed cocycle. The opposite convention $e_j=g_{ij}e_i$ gives
$g_{ij}=f_i/f_j$ and the cocycle with both signs reversed, which is the class of
the inverse line bundle; the sign matters, and step [](#s6){.pf-ref} checks that
the one used here is the one whose trace is $+1$.

:::

:::

::: {.pf-step #s6}

For a nonsingular divisor $Y\subseteq X$,
$$
\boxed{\eta(Y)=c(\mcl(Y))\in H^1(X,\Omega_X)}.
$$
The two sides are elements of $H^1(X,\Omega_X)$, and they are seen to be equal
by pairing both with every class of $H^{n-1}(X,\Omega_X^{n-1})$; the one input
this uses is the divisor case (R) of the head of the solution, which the book
proves for curves and which for $n\ge2$ is named there as an input and not
proved.

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
\left\{\frac{df_j}{f_j}-\frac{df_i}{f_i}\right\}_{ij}
$$
of the cover $(U_i)$ on which $Y$ has local equations $f_i=0$.

**The input (R).** It is the statement (R) of the head of the solution: for
every $\nu\in H^{n-1}(X,\Omega_X^{n-1})$,
$$
t_X\bigl(c(\mcl(Y))\smile\nu\bigr)=t_Y(\restrictionof{\nu}{Y}).
$$
By (G) this is the same as $j_*(\beta)$ pairing with every $\nu$ as
$c(\mcl(Y))\smile\beta$ does, for every $\beta=j^*\nu$; in the classical
language the Gysin map of a divisor is cup product with the $d\log$ class of
$\mcl(Y)$, and $j_*(1)=c(\mcl(Y))$ is the Poincaré residue of the unit class.
Part (d) is the case $\beta=1$ of (R).

(R) is not a consequence of Chapter III for $n\ge2$: Remark III.7.14 (printed
p. 247) says of the trace of a nonsingular projective variety that "we don't
have much information ... We know only that it exists", and its residue
description is stated for curves only. In dimension one (R) is proved in the
book, and the proof has to compare the Čech class with the residue, which is
where the sign lives.

Let $X$ be a curve, $Y=\{P\}$, and take the cover $U_1=X\setminus P$ with
$f_1=1$ and $U_2$ a neighbourhood of $P$ on which $f_2=f$ is a local
parameter. By step [](#s5){.pf-ref} the class $c(\OO(P))$ is
$$
c_{12}=\frac{df_2}{f_2}-\frac{df_1}{f_1}=\frac{df}{f}
\quad\text{on }U_1\cap U_2 .
$$
The trace of Remark III.7.14 is defined on $H^1(X,\Omega_X)$ by the flasque
resolution
$$
0\to\Omega_X\to\Omega_X\tensor\mathcal{K}_X
\to\bigoplus_{P\in X}i_*\bigl(\Omega_K/\Omega_P\bigr)\to0
$$
as the sum of the residues. To read a Čech class in it, take the Čech complex
of that resolution for the cover $\{U_1,U_2\}$: the middle sheaf is constant,
so its Čech complex is acyclic, and the connecting map sends the class of a
family $(\theta_i)$ of rational differentials with
$c_{ij}=\theta_j-\theta_i$ to the principal parts of the $\theta_i$. Hence
$$
t_X(c)=\sum_{P\in X}\operatorname{res}_P(\theta_i),
$$
the index $i$ being any one with $P\in U_i$; the sum is independent of the
choice because two choices differ by a global rational differential, whose
residues sum to $0$ by the residue theorem (III.7.14.2, printed p. 248).

Here $c_{12}=df/f=\theta_2-\theta_1$ with $\theta_1=0$ and $\theta_2=df/f$.
The principal part of $\theta_2$ at $P$ is $df/f$, and Theorem III.7.14.1(c)
(printed p. 247) gives
$$
\operatorname{res}_P\left(\frac{df}{f}\right)=v_P(f)\cdot1=1 .
$$
So $t_X(c(\OO(P)))=+1$, while $t_P(j^*\alpha)=\alpha(P)$ for every
$\alpha\in H^0(X,\OO_X)$; that is (R) in the case at hand, and with it part (d)
in dimension one. With the opposite transition convention of step
[](#s5){.pf-ref} this cocycle would be $-df/f$ and the constant would be
$-1$, so the convention there is what makes the sign come out right.

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
For $n=1$ this is a theorem of the book. For $n\ge2$ it is part (d) proved
relative to (R), and relative to (R) alone: (R) itself is not proved here.

:::

:::

::: pf-qed

Step [](#s1){.pf-ref} proves part (a) with no input beyond the normalization (N). Steps [](#s2){.pf-ref} and [](#s3){.pf-ref} prove part (b) relative to (B), which is where the count $\deg Y$ is carried from $L$ back to $\PP^n$, and to the normalization $1_{\PP^n}$ of step [](#s3){.pf-ref}. Step [](#s4){.pf-ref} proves part (c). Steps [](#s5){.pf-ref} and [](#s6){.pf-ref} prove part (d) relative to (R): in dimension one (R) is proved there from Theorem III.7.14.1, sign included, and for $n\ge2$ (R) is an input the book does not supply.

:::

:::

:::

::: {.remark title="Trace normalization"}
As written in the source, the exercise suppresses a normalization needed to make its numerical assertions canonical, and the printed text supplies no canonical one. The passages are these.

III.7.1(a) is the assertion $H^n(X,\omega_X)\cong k$ for $X=\PP^n_k$, and it continues "Fix one such isomorphism"; the isomorphism is a choice, so the trace $t$ it determines is defined only up to a nonzero scalar. III.7.2 (printed p. 241) makes the trace part of the data: a dualizing sheaf is a *pair* $(\omega_X^\circ,t)$, uniqueness is uniqueness of the pair, and replacing $t$ by $ct$ gives a different pair representing the same functor. Corollary III.7.12 (printed p. 246) then says only that for $X$ projective and nonsingular $\omega_X^\circ$ is *isomorphic* to $\omega_X$; it does not normalize the isomorphism, and the isomorphism its proof produces comes from $\wedge^r(\mathcal I/\mathcal I^2)^\vee$ tensoring, not from a normalization of $t$. Remark III.7.14 (printed p. 247) states the position: "even for a nonsingular projective variety $X$, we don't have much information about the trace map $t:H^n(X,\omega)\to k$. We know only that it exists."

A natural choice does exist on $\PP^n$ and the book records it without using it: Remark III.7.1.1 (printed pp. 240--241) gives the Čech cocycle
$$\alpha=\frac{x_0^n}{x_1\cdots x_n}\,d\Bigl(\frac{x_1}{x_0}\Bigr)\wedge\cdots\wedge d\Bigl(\frac{x_n}{x_0}\Bigr),$$
which "determines a generator of $H^n(X,\omega)$, which is stable under change of variables". That fixes one isomorphism in III.7.1(a), but nothing in the text compares it with the trace on a point or on a divisor.

The other side, part (d), is canonical: Appendix A defines the Chern classes in the Chow ring $A(X)$, with the normalization C1 (printed p. 430), "If $\mathcal E\cong\mathcal L(D)$ for a divisor $D$, $c_t(\mathcal E)=1+Dt$", so $c_1$ of a line bundle is the class of its divisor with no scalar freedom. The exercise's numerical identities can therefore hold only if the trace is normalized to match that integer, which is what the head of the solution states as (N), (G), (R) and (B). None of the four is in the printed exercise, whose text says only "Fix one such isomorphism". Part (a) uses (N) alone, with $Y=P$ a closed point: $\eta(P)$ is defined by duality against $t_X$ itself. Part (b) uses (B) in step [](#s2){.pf-ref} to carry the count from the linear $L$ to $\PP^n$, and the normalization $1_{\PP^n}$ of step [](#s3){.pf-ref} to say which generator of $H^p(\PP^n,\Omega^p)$ the number $\deg Y$ is measured against. Part (d) uses (R) in step [](#s6){.pf-ref}: the book proves it for curves and for $n\ge2$ it is an input, which the card names and does not prove.
:::
