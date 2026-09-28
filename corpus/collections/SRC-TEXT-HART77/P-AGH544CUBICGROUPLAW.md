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
    The hyperplane-divisor calculation P''+Q''+R''~H, together with
    H^0(P^2,O(1))~=H^0(C,O_C(1)), supplies the tangent/coincident completion.
    For associativity, write A for the third point on PQ, B for the third
    point on QR, S=P+Q for the third point on P_0A, and T=Q+R for the third
    point on P_0B. Applying part (a) to the collinear triples (P,Q,A) and
    (T,B,P_0) shows that the third point on PT, the point R, and S are
    collinear; hence that third point equals the third point on SR. Applying
    the P_0-reflection gives associativity.
- event: solution-written
  by: chatgpt
  date: 2026-09-19
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-19
  note: >-
    Re-read the full Cayley--Bacharach and associativity argument. The
    reduced nine-point proof is supplemented by the line-section divisor
    argument so that tangent and coincident intersections are covered with
    multiplicity; all shifted Lamport references in part (b) were checked.
---

::: {.problem}
a. Use (4.5) to prove the following lemma on cubics: If $C$ is an irreducible plane cubic curve, if $L$ is a line meeting $C$ in points $P, Q, R$, and $L^{\prime}$ is a line meeting $C$ in points $P^{\prime}, Q^{\prime}, R^{\prime}$, let $P^{\prime \prime}$ be the third intersection of the line $P P^{\prime}$ with $C$, and define $Q^{\prime \prime}, R^{\prime \prime}$ similarly.
Then $P^{\prime \prime}, Q^{\prime \prime}, R^{\prime \prime}$ are collinear.

b. Let $P_0$ be an inflection point of $C$, and define the group operation on the set of regular points of $C$ by the geometric recipe "let the line $P Q$ meet $C$ at $R$, and let $P_0 R$ meet $C$ at $T$, then $P+Q=T$" as in (II, 6.10.2) and (II, 6.11.4). Use (a) to show that this operation is associative.
:::

::: {.solution}
All intersections with the cubic are counted with multiplicity. Thus when
two named points coincide, the corresponding secant line is interpreted as
the tangent line at that regular point. This is exactly the usual
chord-and-tangent convention.

<1>1. For part (a), let
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
meets $C$ in the degree-nine divisor
$$
P+P'+P''+Q+Q'+Q''+R+R'+R''.
$$

::: {.proof}
Each line $M_P$ meets the irreducible plane cubic $C$ in a divisor of degree
$3$:
$$
M_P|_C=P+P'+P''.
$$
The same statement holds for $M_Q$ and $M_R$. Since $C$ is irreducible of
degree $3$, no line is a component of $C$. Therefore the product cubic $D$
has no common component with $C$, and Bezout gives the displayed total
intersection divisor of degree $9$.
:::

<1>2. Assume first that the nine intersections displayed in step <1>1 are
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

::: {.proof}
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

<1>3. Under the reducedness hypothesis of step <1>2, the ninth point $R''$
lies on $N$. Hence
$$
P'',Q'',R''
$$
are collinear.

::: {.proof}
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

<1>4. The conclusion of part (a) remains valid with arbitrary intersection
multiplicities, including tangent and coincident-point cases.

::: {.proof}
Write $H$ for the hyperplane divisor class on the integral plane cubic $C$.
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

Step <1>3 is the Cayley--Bacharach proof requested in (4.5); the present
argument supplies the scheme-theoretic completion when points coalesce or a
line becomes tangent.
:::

<1>5. For regular points $X,Y\in C$, write
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

::: {.proof}
By definition, the line $XY$ meets $C$ a third time at $X*Y$. The line
$P_0(X*Y)$ then meets $C$ a third time at $\iota(X*Y)$. This is exactly the
two-line recipe defining $X+Y$.
:::

<1>6. Fix regular points $P,Q,R$ and define
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

::: {.proof}
The first triple is collinear by the definition of $A=P*Q$. For the second,
$T=\iota(B)=P_0*B$ is by definition the third point on the line through
$P_0$ and $B$. Hence
$$
T,B,P_0
$$
are collinear as well.
:::

<1>7. Let
$$
V=P*T
$$
be the third point on $PT$. Then
$$
\boxed{V,R,S\text{ are collinear}.}
$$

::: {.proof}
Apply part (a) to the two collinear triples from step <1>6, pairing them as
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

<1>8. The point $V$ is also the third point on the line $SR$:
$$
\boxed{V=S*R.}
$$

::: {.proof}
Step <1>7 says that $S,R,V$ lie on one line. A line meets the cubic in a
degree-three divisor, counted with multiplicity. Since $S$ and $R$ are the
first two intersections in the chord-and-tangent convention, its third
intersection is exactly $S*R$. Hence
$$
V=S*R.
$$
:::

<1>9. The operation is associative:
$$
\boxed{(P+Q)+R=P+(Q+R).}
$$

::: {.proof}
Using step <1>5 and the definitions of $S,T,V$,
$$
\begin{aligned}
(P+Q)+R
&=S+R\\
&=\iota(S*R)\\
&=\iota(V)
\end{aligned}
$$
by step <1>8. On the other hand,
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

The tangent interpretation covers the cases in which some of the points
coincide; step <1>4 proves part (a) with precisely those intersection
multiplicities, so the same calculation remains valid.
This proves part (b).
:::

<1>10. Q.E.D.

::: {.proof}
Steps <1>1--<1>4 prove the cubic lemma in part (a), and steps <1>5--<1>9 use
that lemma to prove associativity of the chord-and-tangent law.
:::
:::
