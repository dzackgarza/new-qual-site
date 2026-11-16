---
schema: qual/card@1
id: P-AGH544CUBICGROUPLAW
kind: problem
title: Associativity of the group law on a plane cubic
classification:
  areas:
  - algebraic-geometry
  topics:
  - Cubic Surfaces
  - Birational Geometry
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-19
  note: >-
    Read Hartshorne V.4.4, the retained Egbert Cayley--Bacharach construction,
    and the earlier chord-and-tangent group-law material. For part (a), the
    cubic formed by PP', QQ', RR' meets C in the nine points P,P',P'',
    Q,Q',Q'',R,R',R''; the cubic L union L' union P''Q'' contains eight, so
    Cayley--Bacharach forces R'' onto P''Q'' in the reduced nine-point case.
    The hyperplane-divisor calculation supplies the tangent/coincident cases
    when the named intersections are regular. It does not cover singular
    intersections on an irreducible cubic; that part of the printed statement
    remains open in this card.
    For associativity, write A for the third point on PQ, B for the third
    point on QR, S=P+Q for the third point on P_0A, and T=Q+R for the third
    point on P_0B. Applying part (a) to the collinear triples (P,Q,A) and
    (T,B,P_0) shows that the third point on PT, the point R, and S are
    collinear; hence that third point equals the third point on SR. Applying
    the P_0-reflection gives associativity.
- event: solution-written
  by: chatgpt
  date: 2026-09-19
- event: source-checked
  by: claude
  date: 2026-11-11
  note: >-
    Read the printed exercise at Hartshorne, Algebraic Geometry (1977), V.4,
    exercise 4.4, printed page 407, with (4.5) as printed on page 407 and (4.6)
    on page 408. Checked part (a) against (4.5), which is the lemma on cubics
    applied through Cayley-Bacharach for a complete intersection of two cubics.
    Searched outside the twelve retained sets for part (b): Algebraic Geometry
    II, National Taiwan University, 2020 Spring, Chapter V homework, Exercise 4
    part (b), PDF p. 16 (tmp/sources/ntu-ag2-chapter5.pdf), gives the
    configuration P, Q, U, the lines PQ, P_0R, TU, P_0V, QU, PV and the
    collinearity of P_0, X, Y from part (a), concluding
    (P+Q)+U = T+U = W = P+Y = P+(Q+U); Yang Pi-Yeh, Hartshorne Solutions,
    exercise 5.4.4, printed p. 109
    (tmp/sources/lfwin-hartshorne-solutions.pdf), runs a different
    configuration with the same shape of argument. Both use part (a) for the
    collinearity and the chord-and-tangent definition for the sums, which is
    what the card's steps do. Not checked: whether the associativity of the
    partial group law requires the general position of the points on the
    cubic; the printed exercise leaves it to the construction, and neither
    published treatment separates the cases.
- event: source-checked
  by: claude
  date: 2026-11-16
  note: >-
    Part (b) transcribed for issue #121 from the published solution: Algebraic
    Geometry II, National Taiwan University, 2020 Spring, Chapter V homework,
    Exercise 4(b) (Tzu-Yang Chou), PDF p. 16 of
    tmp/sources/ntu-ag2-chapter5.pdf, read in the extraction
    tmp/sources/ntu-ag2-chapter5.md. Its configuration is now the one on the
    card: P, Q, U regular points, R = P*Q, T = P0*R, V = T*U, W = P0*V,
    X = Q*U, Y = P*V; part (a) applied to the lines PQR and TUV makes P0, X, Y
    collinear, and the chain (P+Q)+U = T+U = W = P+Y = P+(Q+U) is step
    associativity. Supplied on the card: the pairing part (a) is applied with
    (RT) -> P0, (QU) -> X, (PV) -> Y, which the source leaves to the reader,
    and the definition of each of the six points in terms of the third-point
    operation. The source assumes the six lines are defined and the points
    distinct; the tangent and coincident cases are covered by step
    collinear-with-multiplicity, as the card records. Checked against
    Hartshorne V.4.4(b), printed p. 407, and against the book's (II, 6.10.2)
    and (II, 6.11.4) conventions for the chord-and-tangent law: the group law
    is X+Y = iota(X*Y) with iota the third point on the line through the
    inflection point P0, which is how each identity above is read. Yang
    Pi-Yeh's exercise 5.4.4, printed p. 109, uses a different configuration
    with the same shape and is not needed. Andrew Egbert's entry for (b),
    PDF p. 287, is the citation of Silverman-Tate only.
---

::: {.problem}
(a) Use (4.5) to prove the following lemma on cubics: If $C$ is an irreducible plane cubic curve, if $L$ is a line meeting $C$ in points $P, Q, R$, and $L^{\prime}$ is a line meeting $C$ in points $P^{\prime}, Q^{\prime}, R^{\prime}$, let $P^{\prime \prime}$ be the third intersection of the line $P P^{\prime}$ with $C$, and define $Q^{\prime \prime}, R^{\prime \prime}$ similarly.
Then $P^{\prime \prime}, Q^{\prime \prime}, R^{\prime \prime}$ are collinear.

(b) Let $P_0$ be an inflection point of $C$, and define the group operation on the set of regular points of $C$ by the geometric recipe "let the line $P Q$ meet $C$ at $R$, and let $P_0 R$ meet $C$ at $T$, then $P+Q=T$" as in (II, 6.10.2) and (II, 6.11.4). Use (a) to show that this operation is associative.
:::

::: {.solution}
All intersections with the cubic are counted with multiplicity. Thus when
two named points coincide, the corresponding secant line is interpreted as
the tangent line at that regular point. This is exactly the usual
chord-and-tangent convention.

::: pf

::: {.pf-step #nine-point-divisor}
For part (a), let
$$
M_P=PP',
\qquad
M_Q=QQ',
\qquad
M_R=RR'.
$$
The reducible cubic
$$
D=M_P\cup M_Q\cup M_R
$$
meets $C$ in the degree-nine intersection cycle
$$
P+P'+P''+Q+Q'+Q''+R+R'+R''.
$$

::: pf-proof
Each line $M_P$ meets the irreducible plane cubic $C$ in a zero-dimensional scheme of length
$3$:
$$
M_P\restrict_C=P+P'+P''.
$$
The same statement holds for $M_Q$ and $M_R$. Since $C$ is irreducible of
degree $3$, no line is a component of $C$. Therefore the product cubic $D$
has no common component with $C$, and Bezout gives the displayed total
intersection cycle of degree $9$. This point sum records lengths; it does not
assert that a singular point is a Cartier divisor on $C$.
:::

:::

::: {.pf-step #eight-points-on-reducible-cubic}
Assume first that the nine intersections displayed in step [](#nine-point-divisor){.pf-ref} are
distinct reduced points. Let
$$
N=P''Q''
$$
and form the reducible cubic
$$
D'=L\cup L'\cup N.
$$
Then $D'$ contains eight of the nine intersection points of $C$ and $D$:
$$
P,Q,R,P',Q',R',P'',Q''.
$$

::: pf-proof
By hypothesis,
$$
P,Q,R\in L,
\qquad
P',Q',R'\in L'.
$$
By definition of $N$, one also has
$$
P'',Q''\in N.
$$
Thus all the listed points lie on $D'$.
:::

:::

::: {.pf-step #cayley-bacharach-collinear-reduced}
Under the reducedness hypothesis of step [](#eight-points-on-reducible-cubic){.pf-ref}, the ninth point $R''$
lies on $N$. Hence
$$
P'',Q'',R''
$$
are collinear.

::: pf-proof
Apply the Cayley--Bacharach theorem (4.5) to the two cubics $C$ and $D$.
They have no common component, and $D'$ contains eight of their nine distinct
intersection points. Therefore Cayley--Bacharach forces $D'$ to contain the
ninth point $R''$ as well.

Under the present distinctness hypothesis, $R''$ is different from
$$
P,Q,R,P',Q',R'.
$$
Since
$$
C\cap L=\{P,Q,R\},
\qquad
C\cap L'=\{P',Q',R'\},
$$
it follows that $R''$ lies on neither $L$ nor $L'$. Since it lies on
$D'=L\cup L'\cup N$, it must lie on
$$
N=P''Q''.
$$
Thus
$$
\boxed{P'',Q'',R''\text{ are collinear}.}
$$
This proves part (a).
:::

:::

::: {.pf-step #collinear-with-multiplicity}
The conclusion of part (a) remains valid with tangent and coincident-point
intersections when all named points are regular on $C$.

::: pf-proof
Write $H$ for the hyperplane Cartier divisor class on $C$. Each regular
closed point of an integral curve is a Cartier divisor on the whole curve,
so the assumption that the named points are regular permits the following
calculation on $C$.
Every line cuts a Cartier divisor linearly equivalent to $H$. Thus, with
intersection multiplicities understood,
$$
P+Q+R\sim H,
\qquad
P'+Q'+R'\sim H,
$$
and
$$
\begin{aligned}
P+P'+P''&\sim H,\\
Q+Q'+Q''&\sim H,\\
R+R'+R''&\sim H.
\end{aligned}
$$
Adding the last three relations and subtracting the first two gives
$$
\boxed{P''+Q''+R''\sim H.}
$$

It remains to check that every effective divisor in the class $H$ is cut by
an actual line in the given plane embedding. Since $C\subseteq\PP^2$ is a
plane cubic, twisting its ideal sequence by $\OO_{\PP^2}(1)$ gives
$$
0
\longrightarrow
\OO_{\PP^2}(-2)
\longrightarrow
\OO_{\PP^2}(1)
\longrightarrow
\OO_C(1)
\longrightarrow0.
$$
Now
$$
H^0(\PP^2,\OO(-2))=0,
\qquad
H^1(\PP^2,\OO(-2))=0,
$$
so restriction induces an isomorphism
$$
H^0(\PP^2,\OO(1))
\xrightarrow{\sim}
H^0(C,\OO_C(1)).
$$

The effective divisor
$$
Z=P''+Q''+R''\sim H
$$
therefore is the zero divisor of the restriction of a linear form on
$\PP^2$. Hence some line cuts $C$ in exactly $Z$, counted with
multiplicity. This says precisely that $P'',Q'',R''$ are collinear in the
chord-and-tangent sense.

Step [](#cayley-bacharach-collinear-reduced){.pf-ref} is the Cayley--Bacharach proof in the reduced case; the present
argument covers coalescing regular points and tangent lines.
:::

:::

::: {.pf-step #singular-intersections-by-specialization}
The collinearity conclusion holds when a named intersection is singular and
each joining line is defined either by distinct paired points or as the
tangent at a regular coincident pair.

::: pf-proof
Let $B$ be the dual plane of lines in $\PP^2$. A line section of the integral
cubic $C$ has length $3$. Let $T\to B$ record a line together with an ordering
of its three intersection points, repeated according to multiplicity. This
is a finite flat cover. Locally choose a point of the moving line outside
$C$ as the point at infinity and write the restricted cubic as a monic
polynomial $f(t)$ of degree $3$. Its ordered-root algebra is obtained by
adjoining a root of $f$, a root of the remaining monic quadratic, and then
the final root. These steps are free of ranks $3$, $2$, and $1$.

The two ordered sections in the statement give a point of the finite flat
cover $T\times T\to B\times B$. Every irreducible component of this cover
dominates $B\times B$: locally its coordinate algebra is torsion-free over
the base domain, so a minimal prime cannot contract to a nonzero prime of
the base. Hence configurations over a nonempty open subset of $B\times B$
are dense in every component.

Choose that open subset so that both lines meet $C$ in three distinct
regular points and none of the three joining lines passes through a
singular point of $C$. This open is nonempty. A general line is transverse
to $C$ and avoids its finite singular locus. After fixing one such first
line, choose the first two points of the second line section freely on the
regular locus. For a fixed point of the first line and a fixed singular
point of $C$, only finitely many second points lie on their joining line.
The third point of the second line section also varies as either chosen
point varies, so the same avoidance applies to the remaining pairing.
Thus all joining lines avoid
the singular locus for a general choice. Every named point is then regular,
and step [](#collinear-with-multiplicity){.pf-ref} gives the collinearity.

On the open part of $T\times T$ where each paired pair consists of distinct
points, the three joining lines vary algebraically. On each joining line,
divide its restricted cubic by the two linear factors belonging to the
paired points; the remaining monic linear factor gives its third
intersection algebraically. Thus $P''$, $Q''$, and $R''$ are morphisms to
$C$ on this open part. Collinearity is the vanishing of the determinant of
their three homogeneous coordinate rows, hence a closed condition. It
holds on this dense regular locus, so it holds at the given configuration,
including the singular intersections.

If a paired point coincides at a regular point, the same argument extends
across that diagonal. In a local parameter $t$ on $C$, write the embedded
point as a homogeneous coordinate vector $a(t)$. The coefficients of the
secant line through $a(t)$ and $a(u)$ are $a(t)\times a(u)$. Dividing by
$u-t$ and setting $u=t$ gives $a(t)\times a'(t)$, the nonzero coefficient
vector of the tangent line. Dividing the restricted cubic by the two
linear factors of these approaching points likewise gives a monic linear
factor whose root is the third tangent intersection. Hence the joining
line and its third intersection extend algebraically to a regular
coincident pair. The collinearity determinant remains zero at that limit.

:::

:::

::: {.pf-step #group-law-via-star-and-iota}
For regular points $X,Y\in C$, write
$$
X*Y
$$
for the third intersection of the chord or tangent through $X,Y$ with $C$.
Also put
$$
\iota(Z)=P_0*Z.
$$
Then the operation in part (b) is
$$
\boxed{X+Y=\iota(X*Y).}
$$

::: pf-proof
By definition, the line $XY$ meets $C$ a third time at $X*Y$. The line
$P_0(X*Y)$ then meets $C$ a third time at $\iota(X*Y)$. This is exactly the
two-line recipe defining $X+Y$.
:::

:::

::: {.pf-step #two-collinear-triples}
Let $P,Q,U$ be regular points of $C$ and define
$$
R=P*Q,\qquad
T=P_0*R,\qquad
V=T*U,\qquad
W=P_0*V,\qquad
X=Q*U,\qquad
Y=P*V.
$$
Then
$$
P+Q=T,
\qquad
T+U=W,
\qquad
\text{and}
\qquad
P*Y=V.
$$

::: pf-proof
Each of the six points is the third intersection of a named line with $C$,
which is the configuration of the published proof, PDF p. 16: $R$ on $PQ$,
$T$ on $P_0R$, $V$ on $TU$, $W$ on $P_0V$, $X$ on $QU$, $Y$ on $PV$.

Since $\iota$ is the third point on the line through $P_0$,
$$
P+Q=\iota(P*Q)=\iota(R)=P_0*R=T,
$$
and likewise $T+U=\iota(T*U)=\iota(V)=P_0*V=W$. The identity $P*Y=V$ restates
$Y=P*V$, the third point of the line $PV$ being symmetric in the first two
points.
:::

:::

::: {.pf-step #v-r-s-collinear}
With the notation of step [](#two-collinear-triples){.pf-ref},
$$
\boxed{P_0,\ X,\ Y\ \text{are collinear}.}
$$

::: pf-proof
Apply part (a) to the two lines
$$
L:\ P,Q,R
\qquad\text{and}\qquad
L':\ T,U,V,
$$
each of which meets $C$ in the three named points. Part (a) joins a point of
$L$ to a point of $L'$ and takes the third intersection with $C$: for the
pairs $(R,T)$, $(Q,U)$ and $(P,V)$ those third points are
$$
P_0,\qquad X,\qquad Y,
$$
by the definitions $T=P_0*R$, $X=Q*U$ and $Y=P*V$ of step [](#two-collinear-triples){.pf-ref}. Part (a)
states that the three third points are collinear, which is the claim.
:::

:::

::: {.pf-step #v-equals-s-star-r}
With the notation of step [](#two-collinear-triples){.pf-ref},
$$
\boxed{Q+U=Y}
\qquad\text{and}\qquad
\boxed{P+Y=W}.
$$

::: pf-proof
By step [](#v-r-s-collinear){.pf-ref}, $P_0$, $X$ and $Y$ are collinear, so $Y$ is the third
intersection of the line $P_0X$ with $C$, that is, $Y=\iota(X)$. Since
$X=Q*U$ by step [](#two-collinear-triples){.pf-ref},
$$
Q+U=\iota(Q*U)=\iota(X)=Y.
$$
For the second identity, $P*Y=V$ by step [](#two-collinear-triples){.pf-ref}, so
$$
P+Y=\iota(P*Y)=\iota(V)=P_0*V=W. 
$$
:::

:::

::: {.pf-step #associativity}
The operation is associative:
$$
\boxed{(P+Q)+U=P+(Q+U)}.
$$

::: pf-proof
Using step [](#two-collinear-triples){.pf-ref} and step [](#v-equals-s-star-r){.pf-ref},
$$
(P+Q)+U=T+U=W=P+Y=P+(Q+U).
$$
This is the chain of the published proof, PDF p. 16.

The tangent interpretation covers the cases in which some of the regular
points coincide or a joining line is tangent; step [](#collinear-with-multiplicity){.pf-ref} proves part (a) with precisely those
intersection multiplicities, so the same chain of identities remains valid.
This proves part (b).
:::

:::

::: pf-qed
Steps [](#nine-point-divisor){.pf-ref}, [](#eight-points-on-reducible-cubic){.pf-ref}, [](#cayley-bacharach-collinear-reduced){.pf-ref}, [](#collinear-with-multiplicity){.pf-ref} and [](#singular-intersections-by-specialization){.pf-ref} prove the cubic lemma whenever its joining lines are defined, and steps [](#group-law-via-star-and-iota){.pf-ref}, [](#two-collinear-triples){.pf-ref}, [](#v-r-s-collinear){.pf-ref}, [](#v-equals-s-star-r){.pf-ref} and [](#associativity){.pf-ref} use
that lemma, in the configuration of the published solution, to prove associativity of the chord-and-tangent law.
:::

:::
:::

::: {.remark title="Published solution"}
Andrew Egbert, *Solutions to Hartshorne's Algebraic Geometry* (October 3, 2013), text version `tmp/sources/hartshorne-solutions-egbert.md`, Exercise V.4.4, PDF pp. 286--287. For (a) he has the argument: the cubic $PP'\cup QQ'\cup RR'$ meets $C$ in the nine points, the cubic $L\cup L'\cup P''Q''$ contains eight of them, so "by Cayley--Bacharach, as in 4.4.a" the ninth $R''$ lies on $P''Q''$. Steps [](#nine-point-divisor){.pf-ref}, [](#eight-points-on-reducible-cubic){.pf-ref} and [](#cayley-bacharach-collinear-reduced){.pf-ref} are that argument, and steps [](#collinear-with-multiplicity){.pf-ref} and [](#singular-intersections-by-specialization){.pf-ref} add the cases of tangent lines and coincident points, which he does not treat. For (b), the associativity, his whole solution is "See Tate, Silverman: Rational Points. It's in the first chapter. They even give nice pictures": a citation, with no argument; steps [](#group-law-via-star-and-iota){.pf-ref} to [](#associativity){.pf-ref} derive it from part (a) by the usual two-collinear-triples configuration. Recorded in COMPLAINTS for (b).
:::

::: {.remark title="Published solutions"}
Part (b) has published arguments. Algebraic Geometry II, National Taiwan University, 2020 Spring, *Chapter V Surfaces* homework, Exercise 4(b) (solution by Tzu-Yang Chou), PDF p. 16, takes three points $P,Q,U$, sets $PQ\cap C=P,Q,R$; $P_0R\cap C=P_0,R,T$; $TU\cap C=T,U,V$; $P_0V\cap C=P_0,V,W$; $QU\cap C=Q,U,X$; $PV\cap C=P,V,Y$, applies part (a) to the two triples of lines $PQR$ and $TUV$ to conclude that $P_0,X,Y$ are collinear, and reads off
$$(P+Q)+U=T+U=W=P+Y=P+(Q+U).$$
Yang Pi-Yeh, *Hartshorne Solutions*, text version `tmp/sources/lfwin-hartshorne-solutions.md`, exercise 5.4.4, printed p. 109, runs a different configuration for the same conclusion: with $PQ$ meeting $C$ at $R$, $P_0R$ at $T$, $ST$ at $U$ and $P_0U$ at $V$, it applies (a) to the lines $QPR$ and $SUT$ to get $P_0,B,A$ collinear, whence $S+Q=A$ and $P+A=V$, so $(P+Q)+S=P+(Q+S)$.
:::
