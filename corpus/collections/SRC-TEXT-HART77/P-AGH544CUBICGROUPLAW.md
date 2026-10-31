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
Fix regular points $P,Q,R$ and define
$$
A=P*Q,
\qquad
B=Q*R,
$$
and
$$
S=P+Q=\iota(A),
\qquad
T=Q+R=\iota(B).
$$
Then the triples
$$
P,Q,A
$$
and
$$
T,B,P_0
$$
are collinear triples on $C$.

::: pf-proof
The first triple is collinear by the definition of $A=P*Q$. For the second,
$T=\iota(B)=P_0*B$ is by definition the third point on the line through
$P_0$ and $B$. Hence
$$
T,B,P_0
$$
are collinear as well.
:::

:::

::: {.pf-step #v-r-s-collinear}
Let
$$
V=P*T
$$
be the third point on $PT$. Then
$$
\boxed{V,R,S\text{ are collinear}.}
$$

::: pf-proof
Apply part (a) to the two collinear triples from step [](#two-collinear-triples){.pf-ref}, pairing them as
$$
(P,Q,A)
\qquad\text{and}\qquad
(T,B,P_0).
$$

The line joining the first pair $P,T$ has third point
$$
P''=V.
$$
The line joining the second pair $Q,B$ is the same line as $QR$, because
$B=Q*R$; its third point is therefore
$$
Q''=R.
$$
Finally, the line joining $A$ and $P_0$ has third point
$$
R''=S,
$$
because $S=\iota(A)=P_0*A$.

Part (a) now gives the asserted collinearity of
$$
V,R,S.
$$
:::

:::

::: {.pf-step #v-equals-s-star-r}
The point $V$ is also the third point on the line $SR$:
$$
\boxed{V=S*R.}
$$

::: pf-proof
Step [](#v-r-s-collinear){.pf-ref} says that $S,R,V$ lie on one line. A line meets the cubic in a
degree-three divisor, counted with multiplicity. Since $S$ and $R$ are the
first two intersections in the chord-and-tangent convention, its third
intersection is exactly $S*R$. Hence
$$
V=S*R.
$$
:::

:::

::: {.pf-step #associativity}
The operation is associative:
$$
\boxed{(P+Q)+R=P+(Q+R).}
$$

::: pf-proof
Using step [](#group-law-via-star-and-iota){.pf-ref} and the definitions of $S,T,V$,
$$
\begin{aligned}
(P+Q)+R
&=S+R\\
&=\iota(S*R)\\
&=\iota(V)
\end{aligned}
$$
by step [](#v-equals-s-star-r){.pf-ref}. On the other hand,
$$
\begin{aligned}
P+(Q+R)
&=P+T\\
&=\iota(P*T)\\
&=\iota(V).
\end{aligned}
$$
Therefore
$$
(P+Q)+R=P+(Q+R).
$$

The tangent interpretation covers the cases in which some of the regular
points coincide; step [](#collinear-with-multiplicity){.pf-ref} proves part (a) with precisely those intersection
multiplicities, so the same calculation remains valid.
This proves part (b).
:::

:::

::: pf-qed
Steps [](#nine-point-divisor){.pf-ref}, [](#eight-points-on-reducible-cubic){.pf-ref}, [](#cayley-bacharach-collinear-reduced){.pf-ref}, [](#collinear-with-multiplicity){.pf-ref}, and [](#singular-intersections-by-specialization){.pf-ref} prove the cubic lemma whenever its joining lines are defined, and steps [](#group-law-via-star-and-iota){.pf-ref}, [](#two-collinear-triples){.pf-ref}, [](#v-r-s-collinear){.pf-ref}, [](#v-equals-s-star-r){.pf-ref} and [](#associativity){.pf-ref} use
that lemma to prove associativity of the chord-and-tangent law.
:::

:::
:::
