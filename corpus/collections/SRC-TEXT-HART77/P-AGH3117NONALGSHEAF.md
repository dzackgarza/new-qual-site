---
schema: qual/card@1
id: P-AGH3117NONALGSHEAF
kind: problem
title: A nonalgebraizable invertible sheaf on a formal completion of the plane
classification:
  areas:
  - algebraic-geometry
  topics:
  - Formal Functions
  - Formal Schemes
  - Picard Group
  - Plane Curves
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Exercise III.11.7 together with II.9.9.1 and the preceding Exercises
    III.11.5--11.6. The square-zero Picard sequence was cross-checked against
    Stacks Project Tag 0C6R. The source's assertion that the kernel is a
    k-vector space needs a characteristic-zero hypothesis: in characteristic
    p the multiplicative formal group need not be additive. The solution
    proves the correct arbitrary-characteristic filtration, proves the stated
    vector-space assertion in characteristic zero using the I-adic logarithm,
    and gives an explicit positive-characteristic counterexample on a line in
    P^2. Parts (b) and (c) are then proved in arbitrary characteristic.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
- event: source-checked
  by: claude
  date: 2026-11-09
  note: 'Read III.11.7 against Hartshorne p. 281 and Dongryul Kim, Solutions to Hartshorne, p. 213. Steps s1-s5, s7 and s8 check out. Repaired step s6: its positive-characteristic argument claimed that the first nonzero Cech term of the transition function of L^p must be a coboundary, which does not exclude the cross terms of the formal units. Step s6 now compares coefficients in the two formal charts Spf k[t][[s]] and Spf k[t^{-1}][[s/t]] and shows that no power u^m of u = 1 + z^2/(xy) is a coboundary, so the class of L has infinite order in the kernel. Against Kim: his 11.7(a) asserts without proof that the kernel is a k-vector space and computes only H^2 vanishing and surjectivity; his remark that the k-vector-space structure is the inverse limit of k-vector spaces is the assertion under discussion.'
- event: solution-reviewed
  by: claude
  date: 2026-11-11
  note: >-
    Second step-by-step pass. Checked s1 (H^0(X_r)=k), s2 (the square-zero
    Picard sequence and H^2(O_Y(-rd))=0), s3 (Pic Xhat = lim Pic X_r and
    K_r/K_{r+1} = V_r, the transition maps being surjective), s4 (dim V_r =
    r d^2 + d(d-3)/2 from the hypersurface sequence and h^2(P^2,O(-m)) =
    C(m-1,2)), s5 (char 0: log and exp identify 1+Ihat with Ihat, so K is a
    k-vector space with the infinite descending chain of subspaces K_r), and
    s7. Corrected s6: its coefficient comparison was written for 1 +
    s^{2m}/t^m, which equals u^m only for m a power of p; the step now
    reduces to m = p^a first (if u^M = A/B then u^{p^a M} = A^{p^a}/B^{p^a})
    and then runs the same comparison, and the sentence after it was
    adjusted to say so. The characteristic-p conclusion is unchanged and is
    the one recorded: the kernel is a filtered formal group with infinite-
    dimensional successive quotients, and it is not a k-vector space when
    char k = p.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Second published-solution search for III.11.7(a) (issue #121); no
    complete published argument for the printed claim was located, and none
    can exist, since the claim is false in characteristic p. Read this
    pass: Yang Pi-Yeh, Hartshorne Solutions (9 June 2019), Solution 3.11.7,
    printed p. 82 of tmp/sources/lfwin-hartshorne-solutions.pdf, text
    version tmp/sources/lfwin-hartshorne-solutions.md. He writes the kernel
    as the inverse limit of the completions of the graded pieces and calls
    it "hence infinite dimensional", which is the same step the card
    records as false in characteristic p, and he does not identify the
    successive kernels with H^1(Y, O_Y(-nd)) either. Stack Exchange API
    searches for the exercise on site=math and site=mathoverflow
    (/search/advanced with the exercise's own phrases) returned nothing;
    the only Stack Exchange item the earlier pass found, question 4667761
    on III.11.5, computes the successive kernels of the H^1 terms and says
    nothing about the vector-space structure. Checked against the book in
    this pass: the printed exercise on printed p. 281, and Exercise II.9.6
    which it invokes. Not checked: nothing new; the card's own
    characteristic-p counterexample was not re-derived in this pass.
- event: solution-reviewed
  by: claude
  date: 2026-11-16
  note: >-
    Repairs on the reader's report of this batch. Step s6's reduction is
    rewritten: a general exponent is written m = p^b m' with p not dividing
    m', the freshman's dream gives u^m = (1 + s^{2p^b}/t^{p^b})^{m'}, and
    the coefficient comparison is now made at s^{2p^b}, where the term
    m' t^{-p^b} has m' nonzero in k; the comparison at s^{2p^b} against
    t^{-2p^b}k[t^{-1}] is a contradiction. The earlier step excluded only
    the powers m = p^a and then asserted the general case, which its
    displayed identity does not give. Step s5 now says why the chain
    K = K_1 > K_2 > ... is a chain of k-subspaces: K_r is the image of
    H^1(Xhat, Ihat^r) under the logarithm. Corrected on the audit trail:
    the 2026-11-11 note's description of the reduction, the 2026-11-16
    note's description of Yang's argument, and the remark's citation of
    Kim, which now names its text version. Checked against the book:
    III.11.7 on printed p. 281, Exercise II.9.6. Not checked: nothing new
    in the characteristic-p example beyond the rewritten exponent, which
    was recalculated rather than machine-checked.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Second pass on the reader's report of this batch. The mathematics of
    steps s5 and s6 was re-derived and stands: with b_j = 0 for 0 < j < 2q
    the coefficient of s^{2q} in B u^m is b_{2q} t^{-2q} + m' t^{-q}, and
    m' is nonzero in k because p does not divide m', so the comparison is a
    contradiction. No change is made to the proof. Restored, as the report
    asks, the two event descriptions the previous pass had rewritten in
    place: the note of 2026-11-11 reads again as written, without a
    2026-11-16 judgement spliced into it and without its reference to "the
    event of 2026-11-16 below", and the note of 2026-11-16 again carries the
    description of Yang's argument that was written on that date. The
    corrections those passages now lack are made here: the reduction to the
    exponents m = p^a recorded in the earlier note excludes nothing, as the
    later note says, and Yang writes the successive kernels as
    k[x_0,x_1,x_2]/(f^{n-1}), takes their projective limit, identifies it
    with the completion of k[x_0,x_1,x_2] at (f) and calls that "hence
    infinite dimensional", which is the k-vector-space inference the card
    records as false in characteristic p. Checked against the book in this
    pass: III.11.7 on printed p. 281 and Exercise II.9.6. Not checked:
    nothing new beyond those two re-derivations.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Third pass on the reader's report of this batch, on the audit trail only.
    The solution-reviewed event of 2026-11-16 whose note begins "Repairs on
    the reader's report of this batch" is restored as it was written, and this
    event is appended after it rather than put in its place; the reference in
    the event above to the event "of 2026-11-16 above" whose note begins
    "Repairs on the reader's report" therefore has its referent again. The
    mathematics and the source descriptions stand as that event and the event
    above it record them, and the note of 2026-11-11 keeps the text it was
    written with. Checked in this pass: nothing new; no step was re-derived.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Third pass, on the audit trail and the rule that a dated event is never
    edited. The event above whose note begins "Second pass on the reader's
    report of this batch" was extended in place by commit 15a20526df, which
    added that the pages it cites were read in
    tmp/sources/hartshorne-1977-algebraic-geometry.md, where printed p. N is
    PDF p. N+15. It is restored as it was written in 1abd969bbb, and the
    addition is stated here. Checked in this pass: this card's audit trail in
    git, commit by commit. Not checked: no step was re-derived, and the pages
    named were not re-read.
---

::: {.problem}
Now let $Y$ be a curve in $X = \PP_k^2$, and let $\hat{X}$ be the formal completion of $X$ along $Y$.

(a) Use the method of (Ex.
11.5) to show that $\Pic \hat{X} \to \Pic Y$ is surjective, and that its kernel is an infinite-dimensional vector space over $k$.

(b) Conclude that there is an invertible sheaf $\mcl$ on $\hat{X}$ which is not algebraizable.

(c) Conclude also that there is a locally free sheaf $\mcf$ on $\hat{X}$ such that no twist $\mcf(n)$ is generated by global sections.
Cf.
(II, 9.9.1).
:::

::: {.solution}
Let
$$
d=\deg Y,
\qquad
\mci=\mci_Y\cong\mco_X(-d),
$$
and for $r\ge1$ put
$$
X_r=\bigl(Y,\mco_X/\mci^r\bigr).
$$
Thus $X_1=Y$ and $\hat X=\varprojlim_rX_r$.

There is one characteristic issue in part (a). The successive kernels below are always finite-dimensional $k$-vector spaces, and they make the kernel of $\Pic\hat X\to\Pic Y$ an infinite-dimensional filtered formal group.
If $\operatorname{char}k=0$, the $I$-adic logarithm identifies that formal group with an additive $k$-vector space, giving the assertion in the source literally.
In positive characteristic the assertion that the *group itself* is a $k$-vector space is false; step [](#s6){.pf-ref} gives an explicit counterexample.
The surjectivity in (a), and all of (b)--(c), hold in every characteristic.

::: pf

::: {.pf-step #s1}
For every $r\ge1$,
$$
H^0(X_r,\mco_{X_r})=k.
$$

::: pf-proof
Since $Y$ is an integral projective curve over the algebraically closed field $k$,
$$
H^0(Y,\mco_Y)=k.
$$
For $r\ge2$ there is an exact sequence
$$
0
\longrightarrow
\mci^{r-1}/\mci^r
\longrightarrow
\mco_{X_r}
\longrightarrow
\mco_{X_{r-1}}
\longrightarrow0.
$$
Because $Y$ is a hypersurface of degree $d$,
$$
\mci^{r-1}/\mci^r
\cong
\mco_Y(-(r-1)d).
$$
This line bundle has negative degree
$$
-(r-1)d^2<0,
$$
so it has no nonzero global section.
Hence
$$
H^0(X_r,\mco_{X_r})
\hookrightarrow
H^0(X_{r-1},\mco_{X_{r-1}}).
$$
The constants give a copy of $k$ in every term, so induction from $X_1=Y$ forces equality with $k$ at every stage.
:::

:::

::: {.pf-step #s2}
For every $r\ge1$ there is a short exact sequence of abelian groups
$$
0
\longrightarrow
V_r
\longrightarrow
\Pic X_{r+1}
\longrightarrow
\Pic X_r
\longrightarrow0,
\qquad
V_r\coloneqq H^1\bigl(Y,\mco_Y(-rd)\bigr).
$$

::: pf-proof
The immersion
$$
X_r\hookrightarrow X_{r+1}
$$
is a square-zero thickening whose ideal is
$$
\mci^r/\mci^{r+1}
\cong
\mco_Y(-rd).
$$
The Picard sequence for a square-zero thickening ([Stacks Project, Tag 0C6R](https://stacks.math.columbia.edu/tag/0C6R)) contains
$$
H^0(X_{r+1},\mco_{X_{r+1}}^\times)
\longrightarrow
H^0(X_r,\mco_{X_r}^\times)
\longrightarrow
H^1\bigl(Y,\mco_Y(-rd)\bigr)
$$
$$
\longrightarrow
\Pic X_{r+1}
\longrightarrow
\Pic X_r
\longrightarrow
H^2\bigl(Y,\mco_Y(-rd)\bigr).
$$
By step [](#s1){.pf-ref} the first two groups of units are both $k^\times$, and their map is the identity.
Since $Y$ has dimension $1$,
$$
H^2\bigl(Y,\mco_Y(-rd)\bigr)=0.
$$
Exactness therefore gives the displayed short exact sequence.
:::

:::

::: {.pf-step #s3}
The natural map
$$
\Pic\hat X\longrightarrow\Pic Y
$$
is surjective.
If
$$
K=\ker(\Pic\hat X\to\Pic Y)
$$
and
$$
K_r=\ker(\Pic\hat X\to\Pic X_r),
$$
then
$$
K=K_1\supseteq K_2\supseteq\cdots
$$
and
$$
K_r/K_{r+1}\cong V_r.
$$

::: pf-proof
As in [[P-AGH3115PICFORMAL|Exercise III.11.5]], Exercise II.9.6 gives
$$
\Pic\hat X\cong\varprojlim_r\Pic X_r.
$$
Every transition map in this inverse system is surjective by step [](#s2){.pf-ref}. Starting with any class in
$$
\Pic X_1=\Pic Y,
$$
choose successively a lift to $X_2$, then to $X_3$, and so on.
The resulting compatible sequence is a class in $\Pic\hat X$, proving surjectivity.

Now fix $r$.
An element of $K_r$ has trivial restriction to $X_r$, so its restriction to $X_{r+1}$ lies in
$$
\ker(\Pic X_{r+1}\to\Pic X_r)=V_r.
$$
This gives a homomorphism
$$
K_r\longrightarrow V_r.
$$
Its kernel is exactly $K_{r+1}$.
It is surjective because a class in $V_r$ can first be regarded as a class on $X_{r+1}$ trivial on $X_r$, and then lifted successively through all higher $X_s$ using the surjectivity from step [](#s2){.pf-ref}. Thus
$$
K_r/K_{r+1}\cong V_r.
$$
:::

:::

::: {.pf-step #s4}
The dimensions $\dim_kV_r$ are unbounded.
More precisely, for $r\gg0$,
$$
\dim_kV_r
=
rd^2+\frac{d(d-3)}2.
$$

::: pf-proof
Let $F$ be the homogeneous equation of $Y$.
Twisting the hypersurface sequence by $-rd$ gives
$$
0
\longrightarrow
\mco_{\PP^2}(-(r+1)d)
\xrightarrow{\cdot F}
\mco_{\PP^2}(-rd)
\longrightarrow
\mco_Y(-rd)
\longrightarrow0.
$$
By [[T-IJW1K|the cohomology calculation on projective space]],
$$
H^1(\PP^2,\mco(q))=0
$$
for every $q$, and
$$
\dim_kH^2(\PP^2,\mco(-m))
=
\binom{m-1}{2}
$$
for $m\ge3$.
Since a curve has no $H^2$ for a quasicoherent sheaf, the long exact sequence gives, for $r\gg0$,
$$
0
\longrightarrow
V_r
\longrightarrow
H^2\bigl(\PP^2,\mco(-(r+1)d)\bigr)
\longrightarrow
H^2\bigl(\PP^2,\mco(-rd)\bigr)
\longrightarrow0.
$$
Therefore
$$
\begin{aligned}
\dim_kV_r
&=
\binom{(r+1)d-1}{2}
-
\binom{rd-1}{2}\\
&=
rd^2+\frac{d(d-3)}2.
\end{aligned}
$$
This tends to infinity with $r$.
In particular $V_r\ne0$ for all sufficiently large $r$, so the filtration in step [](#s3){.pf-ref} has infinitely many strict inclusions.
:::

:::

::: {.pf-step #s5}
If $\operatorname{char}k=0$, then $K$ is an infinite-dimensional $k$-vector space.

::: pf-proof
Let
$$
\hat\mci=\ker(\mco_{\hat X}\to\mco_Y).
$$
The kernel of
$$
\mco_{\hat X}^\times\longrightarrow\mco_Y^\times
$$
is the sheaf of principal formal units
$$
1+\hat\mci.
$$
In characteristic zero the convergent $I$-adic series
$$
\log(1+a)
=
\sum_{m\ge1}(-1)^{m+1}\frac{a^m}{m}
$$
and
$$
\exp(a)
=
\sum_{m\ge0}\frac{a^m}{m!}
$$
are inverse isomorphisms of sheaves of abelian groups
$$
1+\hat\mci
\xrightarrow{\sim}
\hat\mci.
$$
Because the right-hand side is a sheaf of $k$-vector spaces, this transports a $k$-vector-space structure to $1+\hat\mci$ and hence to its cohomology.

Step [](#s1){.pf-ref} gives
$$
H^0(\hat X,\mco_{\hat X})=k,
$$
so
$$
H^0(\hat X,\mco_{\hat X}^\times)
\longrightarrow
H^0(Y,\mco_Y^\times)
$$
is the isomorphism $k^\times\to k^\times$.
The long exact sequence for
$$
1
\longrightarrow
1+\hat\mci
\longrightarrow
\mco_{\hat X}^\times
\longrightarrow
\mco_Y^\times
\longrightarrow1
$$
therefore identifies
$$
K
\cong
H^1(\hat X,1+\hat\mci)
\cong
H^1(\hat X,\hat\mci)
$$
as a $k$-vector space.

Under the identification just made, the two filtrations match: a class in $K_r$ is represented by a cocycle with values in $1+\hat\mci^r$, so its logarithm lies in $H^1(\hat X,\hat\mci^r)$ and $K_r$ is the image of $H^1(\hat X,\hat\mci^r)$ in $H^1(\hat X,\hat\mci)$. Each $K_r$ is therefore a $k$-subspace of $K$. A finite-dimensional $k$-vector space bounds the length of a strictly descending chain of subspaces, and steps [](#s3){.pf-ref} and [](#s4){.pf-ref} give the infinite chain
$$
K=K_1\supsetneq K_2\supsetneq\cdots
$$
of subspaces. Hence
$$
\boxed{\dim_kK=\infty}.
$$
This proves the vector-space assertion in part (a) when $\operatorname{char}k=0$.
:::

:::

::: {.pf-step #s6}
In characteristic $p>0$, the assertion that $K$ itself is a $k$-vector space is false in general.

::: pf-proof
Take
$$
Y=\{z=0\}\subseteq\PP_k^2,
$$
so that $Y\cong\PP_k^1$, and let
$$
U_x=\operatorname{Spf} k[t][[s]],\qquad t=y/x,\ s=z/x,
\qquad
U_y=\operatorname{Spf} k[t^{-1}][[s']],\qquad s'=z/y=s/t
$$
be the two formal opens over $x\ne0$ and $y\ne0$. On their intersection
$$
\frac{z^2}{xy}=\frac{s^2}{t}=\frac{s'^2}{t^{-1}},
$$
so
$$
u=1+\frac{z^2}{xy}
$$
is a unit of $\OO(U_x\cap U_y)$ congruent to $1$ modulo the ideal of $Y$.
The formal scheme $\hat X$ is covered by the two opens $U_x,U_y$, which have no
triple intersection; by the Čech description of invertible sheaves on a formal
scheme, $u$ is therefore the transition function of an invertible sheaf
$\mathfrak L$ on $\hat X$ with $\restrictionof{\mathfrak L}{Y}\cong\OO_Y$.

What has to be shown is that no positive power $u^m$ is a Čech coboundary, that
is, that $u^m=A/B$ has no solution with
$$
A=\sum_{i\ge0}a_i(t)s^i\in k[t][[s]],\qquad
B=\sum_{j\ge0}b_j(t^{-1})s'^j\in k[t^{-1}][[s/t]]
$$
units of the respective rings.

Write $m=p^b m'$ with $p\nmid m'$ and put $q=p^b$. In characteristic $p$ one
has $(1+x)^{p^b}=1+x^{p^b}$, so
$$
u^m=\Bigl(1+\frac{s^{2q}}{t^{q}}\Bigr)^{m'}
=1+m'\frac{s^{2q}}{t^{q}}+\text{terms in higher powers of }\frac{s^{2q}}{t^{q}},
$$
and $m'\ne0$ in $k$ because $p\nmid m'$. Suppose $u^m=A/B$, so that
$$
A=B\,u^m .
$$
For $B\in k[t^{-1}][[s/t]]$ the coefficient of $s^j$ in $B$ is
$b_j(t^{-1})\,t^{-j}$ with $b_j\in k[t^{-1}]$; write $a_j\in k[t]$ for the
coefficient of $s^j$ in $A$. At $j=0$ the comparison gives $a_0=b_0$, and
$b_0=a_0\in k[t]\cap k[t^{-1}]=k$, so after multiplying $A$ and $B$ by the same
constant we may take $a_0=b_0=1$. For $1\le j<2q$ the expansion of $u^m$ has no
term in $s^j$, so the comparison reads
$$
a_j(t)=b_j(t^{-1})\,t^{-j},
$$
an identity between a polynomial in $t$ and an element of $t^{-j}k[t^{-1}]$;
hence $a_j=b_j=0$. At $j=2q$ the comparison reads
$$
a_{2q}(t)=b_{2q}(t^{-1})\,t^{-2q}+m'\,t^{-q},
$$
that is
$$
a_{2q}(t)-m'\,t^{-q}\in t^{-2q}k[t^{-1}].
$$
The left-hand side is a polynomial in $t$ plus the single monomial $-m't^{-q}$,
with $m'\ne0$, while every element of $t^{-2q}k[t^{-1}]$ is a $k$-linear
combination of $t^{-k}$ with $k\ge2q>q$. This is impossible. Hence $u^m$ is not a
coboundary, for any positive exponent $m$. In particular $\mathfrak L$ is nontrivial and
has infinite order in $K$.

The additive group of a $k$-vector space is killed by its prime $p$, so a group
containing an element of infinite order is not a $k$-vector space. Since the
group law of $K=\ker(\Pic\hat X\to\Pic Y)$ is the multiplicative structure of
$\Pic$, the kernel in part (a) is not a $k$-vector space in characteristic $p$.
The correct characteristic-free statement is the filtered statement of steps
[](#s2){.pf-ref}, [](#s3){.pf-ref} and [](#s4){.pf-ref}.
:::

:::

::: {.pf-step #s7}
There is a nonalgebraizable invertible sheaf on $\hat X$.

::: pf-proof
By steps [](#s3){.pf-ref} and [](#s4){.pf-ref}, $K$ is nonzero in every characteristic.
Choose a nontrivial class
$$
[\mathfrak L]\in K.
$$
Thus
$$
\mathfrak L\restrict_Y\cong\mco_Y.
$$
Suppose that $\mathfrak L$ were algebraizable.
Then there would be a coherent sheaf $\mcg$ on $X$ with
$$
\hat\mcg\cong\mathfrak L.
$$

The local argument in [[P-AGH3116ALGEBRAIZABLE|Exercise III.11.6, steps 7--8]] applies to this single algebraization: faithfully flat completion shows that $\mcg$ is locally free of rank one on a neighbourhood of $Y$, and its reflexive hull
$$
\mcl=\mcg^{\vee\vee}
$$
is a rank-one reflexive sheaf on $X=\PP_k^2$.
Since projective space is regular and locally factorial, $\mcl$ is invertible; moreover $\mcl$ agrees with $\mcg$ near $Y$, so
$$
\hat\mcl\cong\mathfrak L.
$$

But
$$
\Pic\PP_k^2\cong\ZZ
$$
with generator $\mco_X(1)$, so
$$
\mcl\cong\mco_X(m)
$$
for some $m\in\ZZ$.
Restricting to $Y$ gives
$$
\mco_Y(m)
\cong
\mathfrak L\restrict_Y
\cong
\mco_Y.
$$
Now
$$
\deg\mco_Y(m)=md.
$$
Since $d>0$, triviality forces $m=0$.
Hence
$$
\mcl\cong\mco_X
$$
and therefore
$$
\mathfrak L\cong\mco_{\hat X},
$$
contrary to the choice of $[\mathfrak L]\ne0$.

Thus $\mathfrak L$ is not algebraizable, proving (b).
:::

:::

::: {.pf-step #s8}
There is a locally free sheaf $\mathfrak F$ on $\hat X$ such that no twist $\mathfrak F(n)$ is generated by global sections.

::: pf-proof
Condition (i) of [[P-AGH3116ALGEBRAIZABLE|Exercise III.11.6(b)]] says that *every* locally free sheaf on $\hat X$ is algebraizable.
Step [](#s7){.pf-ref} gives an invertible, hence locally free, counterexample.
Therefore condition (i) is false.

Exercise III.11.6(b) proves that condition (i) is equivalent to condition (ii).
Hence condition (ii) is false.
Consequently there is a locally free sheaf $\mathfrak F$ on $\hat X$ for which no integer $n_0$ has the property that
$$
\mathfrak F(n)
$$
is generated by global sections for every $n\ge n_0$.

Suppose some twist $\mathfrak F(n_1)$ were generated by global sections.
For every $r\ge0$, the sheaf
$$
\mco_{\hat X}(r)
$$
is generated by global sections because it is the restriction of the globally generated sheaf $\mco_{\PP^2}(r)$.
Tensor products of globally generated sheaves are globally generated, so
$$
\mathfrak F(n_1+r)
=
\mathfrak F(n_1)\otimes\mco_{\hat X}(r)
$$
would be globally generated for every $r\ge0$.
Taking $n_0=n_1$ would then satisfy condition (ii) for $\mathfrak F$, a contradiction.

Therefore
$$
\boxed{\mathfrak F(n)\text{ is not generated by global sections for every }
n\in\ZZ}.
$$
This is the phenomenon announced in Hartshorne II.9.9.1.
:::

:::

::: pf-qed
Steps [](#s2){.pf-ref}, [](#s3){.pf-ref}, and [](#s4){.pf-ref} prove the characteristic-free surjectivity and infinite filtered kernel in (a), step [](#s5){.pf-ref} gives the stated infinite-dimensional vector-space conclusion in characteristic zero, and step [](#s6){.pf-ref} records the necessary correction in positive characteristic.
Step [](#s7){.pf-ref} proves (b), and step [](#s8){.pf-ref} proves (c).
:::

:::
:::

::: {.remark title="Published solution"}
Dongryul Kim, *Solutions to Hartshorne's Algebraic Geometry* (Chapters II--III), text version `tmp/sources/hartshorne-solutions-kim.md`, Chapter III §11, Exercise 11.7, PDF p. 213, source revision `6c627eed7b0226249df79b8777f5ac450f17885a`: he writes $\Pic\hat X=\varprojlim\Pic Y_n$, uses the exact sequence of Exercise III.4.6 with $H^2=0$ and $H^1(\OO_Y(-dn))$ growing, concludes that $\Pic\hat X\to\Pic Y$ is surjective with an infinite-dimensional kernel, and remarks that the kernel of $\Pic Y_n\to\Pic Y_1$ is a $k$-vector space. That last remark is the point the proof above corrects: it holds in characteristic zero (step s5, by the $I$-adic logarithm) but fails in characteristic $p$, where step s6 exhibits a line bundle of infinite order in the kernel on the line $z=0$. Kim's parts (b) and (c) agree with steps s7 and s8.
:::
