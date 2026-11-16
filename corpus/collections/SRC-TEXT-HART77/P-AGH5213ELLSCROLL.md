---
schema: qual/card@1
id: P-AGH5213ELLSCROLL
kind: problem
title: Existence of elliptic scrolls of given degree
classification:
  areas:
  - algebraic-geometry
  topics:
  - Surfaces
  - Ruled Surfaces
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-19
  note: >-
    Read Hartshorne V.2.13, the retained Egbert companion calculation, and
    the preceding invariant and elliptic ruled-surface very-ampleness cards.
    The companion has the intended route: choose a ruled surface of invariant
    e and embed by C_0+n f. Its final dimension line conflates h^0 with the
    projective-space dimension; the proof below keeps h^0=2n-e=d and hence
    embeds by the complete system in P^{d-1}. The e=-1 case is supplied by
    V.2.5(c), e=0 by V.2.5(a), and e>0 by the explicit normalized split bundle
    O_C direct-sum L with deg L=-e.
- event: solution-written
  by: chatgpt
  date: 2026-09-19
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-19
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Read the printed exercise at Hartshorne, Algebraic Geometry (1977), V.2,
    exercise 2.13, printed page 385. Rechecked the dimension count that Egbert
    gets wrong: on an elliptic curve Riemann-Roch gives h^0(O_C(k)) = k for
    k > 0, so h^0(X, O(C_0+bf)) = h^0(b) + h^0(b+e) = n + (n-e) = 2n-e = d,
    and the scroll lies in P^{d-1}, not in P^{d+1} as the rational scroll of
    Corollary 2.19 does. Checked the applications: V.2.12(b) for very ampleness
    at n >= e+3, V.2.5(a) and (c) for the existence of the surface at e = 0 and
    e = -1, and the split normalized bundle O_C + O_C(-e) for e > 0, whose
    negative twists have no sections. Searched outside the twelve retained sets:
    Yang Pi-Yeh, Hartshorne Solutions, exercise 5.2.13, printed p. 105
    (tmp/sources/lfwin-hartshorne-solutions.pdf), gives the argument from
    V.2.12(b) and the same 2n-e count; Algebraic Geometry II, National Taiwan
    University, 2020 Spring, has no entry for Exercise 13 of section 2. Not
    checked: whether an elliptic scroll so defined is required to be minimal or
    normalised; the exercise does not ask and the card does not claim.
- event: source-corrected
  by: claude
  date: 2026-11-15
  note: >-
    The input this card's very-ampleness step imports, Yang's 5.2.12, recorded
    with its two wrong values, on a reader's report of issue #121. Read in
    tmp/sources/lfwin-hartshorne-solutions.md (block "PDF pages 101-119") at
    Solution 5.2.12 and against the folios of the PDF: on printed p. 104 he
    writes h^0(L_X(C_0+Bf)) = h^0(L_C(fraktur-e+B)) = 2 at e = -1, and on p. 105
    h^0(C_0+(A+B)f) = h^0(C_0+Bf) + 2 = 4 and h^0(C_0+(A+B-P-Q)f) = 0. The true
    values are 3, 5 and 1. With e = -1 the surface is P(E) for the unique
    nontrivial extension 0 -> O_C -> E -> L(P) -> 0 of (2.11.6), so
    deg E = deg fraktur-e = -e = 1 by Notation 2.8.1; pi_*O(C_0+bf) = E tensor O(b) is
    indecomposable of degree 1 + 2 deg b, and Riemann-Roch with h^1 = 0 above
    degree 2g-1 gives h^0 = 2 deg b + 1, i.e. 3, 5, 1 at deg b = 1, 2, 0. His own
    5.2.13 count 2n-e gives the same 3 at n = 1, so his two entries disagree.
    Both tests he then applies are drops, h^0(D-Pf) = h^0(D)-2 and
    h^0(D-Pf-Qf) = h^0(D)-4, and they hold with the true values too, so his
    conclusions survive while the absolute values do not. The cause is his p. 104
    display, which keeps only the h^0(b+fraktur-e) summand of the decomposable
    splitting of 5.2.11 and then subtracts an unrelated h^1; the two-term split
    value coincides with the truth for deg b >= 1 and for every nontrivial b of
    degree 0, the terms being h^0(b) = 0 and h^0(b+fraktur-e) = 1 there, and it
    differs only at b ~ 0, where it gives 2 against the true 1 -- the one class
    at which the split formula and the indecomposable bundle part company, so the
    splitting's validity at e = -1 is not what the numbers turn on. The card's own
    steps use none of his numbers and are unchanged.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Read Fuentes and Pedreira (arXiv:math/0006204v3) on 2026-11-16, in
    tmp/sources/projective-theory-ruled-surfaces.md. Its introduction cites the
    classification of elliptic scrolls of Corrado Segre, its reference [17], and
    says that that classification does not follow directly from the
    very-ampleness criterion; [17] is Segre, Ricerche sulle rigate ellittiche di
    qualunque ordine, Atti Acc. Torino 21 (1885), 868--891, which is not in
    tmp/sources and was not read. The paper's own reference [4], the authors'
    "The classification of elliptic scrolls", preprint math.AG/0009050, appears
    only in its bibliography and is never cited in its text, so nothing here rests
    on it. What the paper does settle is the case e >= 0: its Theorem 3.2(1),
    printed p. 15, has a decomposable normalized bundle of invariant e >= 0 and
    every e >= 0 occurring; its Theorem 3.9(3), printed p. 18, makes the system of
    C_0 + bf very ample exactly when b and b+e are; and its Theorem 3.10(1),
    printed p. 19, gives N = h^0(b) + h^0(b+e) - 1 and degree 2 deg b - e. Those
    three are a published argument for every e >= 0 with n >= e+3. The case e = -1
    is outside the paper, whose Section 3 treats decomposable surfaces only, and
    the Atiyah surface there is indecomposable; step s1 constructs it and steps s3
    to s7 carry it through, and Yang Pi-Yeh's count, recorded above, agrees.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Corrected the remark's use of Fuentes--Pedreira's Theorem 3.10(1) on
    2026-11-16. That theorem gives N = h^0(O_X(b)) + h^0(O_X(b+e)) - 1, where N
    is the dimension of the projective space in which the scroll lies, together
    with deg S = 2 deg b - e; the remark read the first formula as the number of
    sections, which is the confusion it records against Egbert elsewhere, and it
    now says that on an elliptic base the section counts are n and n-e, so that
    h^0 = d = 2n-e and N = d-1, the scroll lying in P^{d-1}, which is what step
    s6 computes directly and what the event above states correctly. Also
    recorded here, since dated events are not rewritten: the event of 2026-11-11
    cites Yang Pi-Yeh by PDF, whose text version is
    tmp/sources/lfwin-hartshorne-solutions.md, and the National Taiwan University
    set, whose text version is tmp/sources/ntu-ag2-chapter5.md beside its PDF;
    the remark's citation of Yang names his.
---

::: {.problem}
For every $e \geqslant-1$ and $n \geqslant e+3$, there is an elliptic scroll of degree $d=2 n-e$ in $\PP^{d-1}$.
In particular, there is an elliptic scroll of degree 5 in $\PP^4$.
:::

::: {.solution}
Fix an elliptic curve $C$.

::: pf

::: {.pf-step #s1}

For every integer
$$
e\ge-1
$$
there is a ruled surface
$$
\pi:X=\PP(\mathcal E)\longrightarrow C
$$
with invariant $e$.

::: pf-proof

For $e=-1$, Hartshorne V.2.5(c), proved on [[P-AGH525INVARIANTE]], gives a
ruled surface over the genus-one curve $C$ with invariant $-1$.

For $e=0$, V.2.5(a) gives an indecomposable normalized rank-two bundle with
invariant zero.

Now let $e>0$. Choose a line bundle $M$ of degree $-e$ on $C$ and put
$$
\mathcal E=\OO_C\oplus M.
$$
The summand $\OO_C$ gives a nonzero global section. If $N$ has negative
degree, then both
$$
N
\qquad\text{and}\qquad
M\tensor N
$$
have negative degree and hence no sections. Thus
$$
H^0(C,\mathcal E\tensor N)=0,
$$
so $\mathcal E$ is normalized. Since
$$
\deg\det\mathcal E=-e,
$$
the invariant of $\PP(\mathcal E)$ is $e$.

:::

:::

::: {.pf-step #s2}

Let $C_0$ be the normalized section and $f$ a ruling fibre. Then
$$
C_0^2=-e,
\qquad
C_0\cdot f=1,
\qquad
f^2=0.
$$

::: pf-proof

These are the standard intersection formulas for a normalized geometrically
ruled surface: the invariant is
$$
e=-C_0^2,
$$
while a section meets every fibre once and distinct fibres are disjoint.

:::

:::

::: {.pf-step #s3}

Choose a divisor $\mfb$ on $C$ with
$$
\deg\mfb=n,
$$
and put
$$
D=C_0+\mfb f.
$$
If
$$
n\ge e+3,
$$
then $D$ is very ample.

::: pf-proof

This is exactly Hartshorne V.2.12(b), proved on
[[P-AGH5212ELLRULEDAMPLE]]: on a ruled surface over an elliptic curve,
$$
\linearsystem{C_0+\mfb f}
$$
is very ample if and only if
$$
\deg\mfb\ge e+3.
$$

:::

:::

::: {.pf-step #s4}

The embedding defined by $\linearsystem{D}$ makes every ruling fibre a line.

::: pf-proof

By step [](#s2){.pf-ref},
$$
D\cdot f
=
(C_0+\mfb f)\cdot f
=
1.
$$
Hence
$$
\OO_X(D)\restrict_f\cong\OO_{\PP^1}(1).
$$
Because the complete system $\linearsystem{D}$ is very ample by step [](#s3){.pf-ref}, its
restriction embeds each fibre as a projective line. Thus the image is a
scroll over the elliptic curve $C$.

:::

:::

::: {.pf-step #s5}

The degree of this embedded scroll is
$$
\boxed{d=2n-e}.
$$

::: pf-proof

For a surface embedded by the very ample divisor $D$, its degree is $D^2$.
Using step [](#s2){.pf-ref},
$$
\begin{aligned}
D^2
&=(C_0+\mfb f)^2\\
&=C_0^2+2n(C_0\cdot f)+n^2f^2\\
&=-e+2n\\
&=2n-e.
\end{aligned}
$$

:::

:::

::: {.pf-step #s6}

The complete linear system $\linearsystem{D}$ has
$$
\boxed{h^0(X,\OO_X(D))=2n-e=d}.
$$

::: pf-proof

Let $\mfe$ be the divisor on $C$ with
$$
\OO_C(\mfe)\cong\det\mathcal E.
$$
Then
$$
\deg\mfe=-e.
$$

The section restriction calculation from Hartshorne V.2.11, proved in
[[P-AGH5211VERYAMPLESECT]], gives, because $\mfb$ is nonspecial,
$$
h^0(X,\OO_X(C_0+\mfb f))
=
h^0(C,\OO_C(\mfb))
+
h^0(C,\OO_C(\mfb+\mfe)).
$$
Here
$$
\deg\mfb=n>0,
\qquad
\deg(\mfb+\mfe)=n-e\ge3>0.
$$
On the elliptic curve, Riemann--Roch and Serre duality give
$$
h^0(C,L)=\deg L
$$
for every positive-degree line bundle $L$. Therefore
$$
h^0(X,\OO_X(D))
=
n+(n-e)
=
2n-e
=
d.
$$

:::

:::

::: {.pf-step #s7}

The complete linear system $\linearsystem{D}$ embeds $X$ as an elliptic scroll of
degree $d$ in
$$
\boxed{\PP^{d-1}}.
$$

::: pf-proof

Step [](#s3){.pf-ref} gives very ampleness, so the complete system defines a closed
immersion
$$
X\hookrightarrow\PP\bigl(H^0(X,\OO_X(D))^\vee\bigr).
$$
By step [](#s6){.pf-ref} the target is $\PP^{d-1}$. Step [](#s4){.pf-ref} identifies the image as a
scroll over the elliptic curve, and step [](#s5){.pf-ref} gives degree $d$.

:::

:::

::: {.pf-step #s8}

There is an elliptic scroll of degree $5$ in $\PP^4$.

::: pf-proof

Take
$$
e=-1,
\qquad
n=2.
$$
Then
$$
n=e+3,
$$
so the construction applies, and
$$
d=2n-e=4+1=5.
$$
Step [](#s7){.pf-ref} therefore gives an elliptic scroll of degree $5$ in
$$
\PP^{5-1}=\PP^4.
$$

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref}, [](#s3){.pf-ref}, [](#s4){.pf-ref}, [](#s5){.pf-ref}, [](#s6){.pf-ref} and [](#s7){.pf-ref} prove the asserted existence for every $e\ge-1$ and
$n\ge e+3$, and step [](#s8){.pf-ref} gives the stated degree-five example.

:::

:::

:::

::: {.remark title="Published solution"}
Yang Pi-Yeh, *Hartshorne Solutions*, text version `tmp/sources/lfwin-hartshorne-solutions.md`, exercise 5.2.13, printed p. 105, argues exactly as steps [](#s3){.pf-ref} to [](#s7){.pf-ref}: by V.2.12(b), if $n\ge e+3$ then any $D\sim C_0+nf$ is very ample, and since $D\cdot f=1$ and $D^2=2n-e$ the embedding is an elliptic scroll of degree $d=2n-e$; then "$h^0(\mathcal L_X(D))=h^0(\pi_*\mathcal L_X(D))=h^0(\OO_C(n)+\OO_C(n-e))=2n-e$, so the embedding is in $\PP^{d-1}$", and it takes $e=-1$, $n=2$ for the degree-five example in $\PP^4$. Its $h^0$ uses $h^0(\OO_C(k))=k$ on an elliptic curve, which is the computation of step [](#s6){.pf-ref}. It does not construct the ruled surface of invariant $e$ for each $e\ge-1$, which is step [](#s1){.pf-ref}.

Luis Fuentes and Manuel Pedreira, *The Projective Theory of Ruled Surfaces* (arXiv:math/0006204v3), text version `tmp/sources/projective-theory-ruled-surfaces.md`, settle the case $e\ge0$: Theorem 3.2(1), printed p. 15, has every $e\ge0$ occurring for a decomposable surface; Theorem 3.9(3), printed p. 18, makes $\linearsystem{X_0+\mfb f}$ very ample exactly when $\mfb$ and $\mfb+\mfe$ are; and Theorem 3.10(1), printed p. 19, gives $N=h^0(\mfb)+h^0(\mfb+\mfe)-1$ and degree $2\deg\mfb-e$, where $N$ is the dimension of the projective space containing the scroll and not the number of sections; on an elliptic base the two section counts are $n$ and $n-e$, so $h^0=d=2n-e$ and $N=d-1$, and the scroll lies in $\PP^{d-1}$, which is what step [](#s6){.pf-ref} computes directly. That is steps [](#s3){.pf-ref}, [](#s5){.pf-ref}, [](#s6){.pf-ref} and [](#s7){.pf-ref} for $e\ge0$ on a decomposable surface. Their §3 covers decomposable surfaces only, so the Atiyah surface $e=-1$ is outside it, and step [](#s1){.pf-ref} is what supplies that case.

The very-ampleness step it imports is its own 5.2.12(b), and the two absolute values there are wrong by the
same amount, so the step survives while its arithmetic does not. On printed p. 104 it writes
$h^0(\mathcal L_X(C_0+Bf))=h^0(\mathcal L_C(\mathfrak e+B))=2$ at $e=-1$, $B$ of degree $1$; the true value is
$3$, because the surface is $\mathbf P(\mathcal E)$ for the unique nontrivial extension
$0\to\OO_C\to\mathcal E\to\mathcal L(P)\to0$ of (2.11.6), hence $\deg\mathcal E=\deg\mathfrak e=-e=1$ (Notation 2.8.1),
$\pi_*\OO(C_0+Bf)=\mathcal E\otimes\OO(B)$ is indecomposable of degree $3$, and Riemann--Roch with
$h^1=0$ at degree $\ge1$ gives $h^0=3$ --- the value its own 5.2.13 formula $2n-e$ gives at $n=1$. On p. 105 it
then writes $h^0(C_0+(A+B)f)=h^0(C_0+Bf)+2=4$, true $5$, and $h^0(C_0+(A+B-P-Q)f)=0$, true $1$. Both tests it
applies are drops, $h^0(D-Pf)=h^0(D)-2$ and $h^0(D-Pf-Qf)=h^0(D)-4$, and those hold with the correct values
too, so the conclusions are right. The cause is the shape of his display, which sits inside the splitting of
5.2.11, $h^i(C_0+\mathfrak bf)=h^i(\mathfrak b)+h^i(\mathfrak b+\mathfrak e)$: that identity is derived in the
decomposable case $\mathcal E\cong\OO\oplus\mathcal L$ with $e\ge0$ (Theorem 2.12(a)), while 5.2.12 is the
case $e=-1$, where $\mathcal E$ is indecomposable, yet there the two-term value is right for
$\deg\mathfrak b\ge1$ (both equal $2\deg\mathfrak b-e$). His p. 104 display keeps only the
$h^0(\mathfrak b+\mathfrak e)$ summand and then subtracts $h^1(\mathcal L_X(Bf-Pf))$ to reach the $0$; at
$\deg\mathfrak b=0$ the two-term value is $2$ only for $\mathfrak b\sim0$, against the true $1$, and for a
nontrivial $\mathfrak b$ of degree $0$, $A+B-P-Q$ say, it is $1$, which is the true value. So the class
$\mathfrak b\sim0$ is the one at which the split formula and the indecomposable bundle part company. None of
these numbers is used by the steps above.

Andrew Egbert, *Solutions to Hartshorne's Algebraic Geometry* (October 3, 2013), text version `tmp/sources/hartshorne-solutions-egbert.md`, Exercise V.2.13, PDF p. 269: he takes $D=C_0+nf$, cites (2.20b) and (2.21b) for ampleness, computes $D\cdot f=1$ and $D^2=2n-e$, and then needs $h^0$. His count is
$$
h^0(\OO_X(\mathcal L(D)))=h^0(\OO_C(n)\oplus\OO_C(n-e))=2n-1=d-1,
$$
which drops $e$: on an elliptic curve $h^0(\OO_C(n))=n$ and $h^0(\OO_C(n-e))=n-e$, so the sum is $2n-e=d$ and the scroll lies in $\PP^{d-1}$, as the exercise states. Step [](#s6){.pf-ref} gives $2n-e$ and step [](#s7){.pf-ref} the resulting $\PP^{d-1}$. Otherwise his plan is the one followed here: existence of the surface for each $e\ge-1$ in step [](#s1){.pf-ref}, very ampleness from V.2.12(b) in step [](#s3){.pf-ref}, degree $D^2$ in step [](#s5){.pf-ref}.
:::
