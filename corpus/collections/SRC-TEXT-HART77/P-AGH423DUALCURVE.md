---
schema: qual/card@1
id: P-AGH423DUALCURVE
kind: problem
title: The dual curve, its class $d(d-1)$, and the counts of inflection points and bitangents
classification:
  areas:
  - algebraic-geometry
  topics:
  - Riemann-Hurwitz
  - Genus
  - Embeddings
  - Linear Systems
relations: []
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Hartshorne IV.2.3 in the original text. The setup tacitly needs d>=2.
    More seriously, part (b) defines a bitangent as tangent at exactly two
    points, while part (h) counts hyperflex lines among the 28 bitangents; its
    parenthetical also misidentifies the dual singularity of a four-fold
    contact as a tacnode. The erratum below gives the corrected statement and
    an explicit smooth quartic counterexample to the literal convention.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-18
review: draft
---

::: {.problem}
Let $X$ be a curve of degree $d$ in $\PP^2$.
For each point $P \in X$, let $T_P(X)$ be the tangent line to $X$ at $P$ (I, Ex.
7.3). Considering $T_P(X)$ as a point of the dual projective plane $(\PP^2)^*$, the map $P \mapsto T_P(X)$ gives a morphism of $X$ to its **dual curve** $X^*$ in $(\PP^2)^*$ (I, Ex.
7.3).

Note that even though $X$ is nonsingular, $X^*$ in general will have singularities.
We assume $\characteristic k=0$ below.

a. Fix a line $L \subseteq \PP^2$ which is not tangent to $X$.
Define a morphism $\varphi: X \to L$ by $\varphi(P)=T_P(X) \intersect L$, for each point $P \in X$.
Show that $\varphi$ is ramified at $P$ if and only if either (1) $P \in L$, or (2) $P$ is an inflection point of $X$, which means that the intersection multiplicity (I, Ex.
5.4) of $T_P(X)$ with $X$ at $P$ is $\geq 3$.
Conclude that $X$ has only finitely many inflection points.

b. A line of $\PP^2$ is a **multiple tangent** of $X$ if it is tangent to $X$ at more than one point.
It is a **bitangent** if it is tangent to $X$ at exactly two points.
If $L$ is a multiple tangent of $X$, tangent to $X$ at the points $P_1, \ldots, P_r$, and if none of the $P_i$ is an inflection point, show that the corresponding point of the dual curve $X^*$ is an ordinary $r$-fold point, which means a point of multiplicity $r$ with distinct tangent directions (I, Ex.
5.3). Conclude that $X$ has only finitely many multiple tangents.

c. Let $O \in \PP^2$ be a point which is not on $X$, nor on any inflectional or multiple tangent of $X$.
Let $L$ be a line not containing $O$.
Let $\psi: X \to L$ be the morphism defined by projection from $O$.
Show that $\psi$ is ramified at a point $P \in X$ if and only if the line $OP$ is tangent to $X$ at $P$, and in that case the ramification index is 2. Use Hurwitz's theorem and (I, Ex.
7.2) to conclude that there are exactly $d(d-1)$ tangents of $X$ passing through $O$.
Hence the degree of the dual curve (sometimes called the **class** of $X$) is $d(d-1)$.

d. Show that for all but a finite number of points of $X$, a point $O$ of $X$ lies on exactly $(d+1)(d-2)$ tangents of $X$, not counting the tangent at $O$.

e. Show that the degree of the morphism $\varphi$ of a. is $d(d-1)$.
Conclude that if $d \geq 2$, then $X$ has $3d(d-2)$ inflection points, properly counted.
(If $T_P(X)$ has intersection multiplicity $r$ with $X$ at $P$, then $P$ should be counted $r-2$ times as an inflection point.
If $r=3$ we call it an ordinary inflection point.)
Show that an ordinary inflection point of $X$ corresponds to an ordinary cusp of the dual curve $X^*$.

f. Now let $X$ be a plane curve of degree $d \geq 2$, and assume that the dual curve $X^*$ has only nodes and ordinary cusps as singularities (which should be true for sufficiently general $X$). Then show that $X$ has exactly $\frac{1}{2} d(d-2)(d-3)(d+3)$ bitangents.
Hint: Show that $X$ is the normalization of $X^*$.
Then calculate $p_a(X^*)$ two ways: once as a plane curve of degree $d(d-1)$, and once using (Ex.
1.8).

g. For example, a plane cubic curve has exactly 9 inflection points, all ordinary.
The line joining any two of them intersects the curve in a third one.

h. A plane quartic curve has exactly 28 bitangents.
(This holds even if the curve has a tangent with four-fold contact, in which case the dual curve $X^*$ has a tacnode.)
:::

::: {.remark title="Erratum to the degree-one setup and part (h)"}
The setup should assume $d\geq2$.  For $d=1$ the Gauss map has a point as
its image and the map $\varphi$ in part (a) is constant, so the ramification
and degree assertions are not statements about a finite morphism of curves.

There is also a genuine inconsistency between parts (b) and (h).  Part (b)
defines a bitangent to be tangent at **two distinct points**.  With that
definition, part (h) is false for quartics having a hyperflex.  The invariant
statement is:

> Every nonsingular plane quartic in characteristic $0$ has exactly $28$
> generalized bitangent lines, where a line with section $4P$ is counted as
> a degenerate bitangent $2P+2P$.  If $h$ is the number of hyperflex lines,
> then there are exactly $28-h$ bitangents in the strict sense of part (b).

For a concrete counterexample to the literal statement, take the Fermat
quartic
$$
X=V(x^4+y^4+z^4)
$$
over $\CC$.  If $\zeta^4=-1$, then
$$
P=[0:1:\zeta]\in X
$$
has tangent line
$$
y+\zeta^3z=0.
$$
Restricting the quartic equation to this line gives $x^4=0$, so the tangent
section is $4P$.  Permuting the zero coordinate and choosing the four values
of $\zeta$ gives $12$ hyperflexes.  Step [](#s14){.pf-ref} below shows that this quartic
therefore has $16$, not $28$, strict bitangents.

The final parenthetical in the source is also incorrect: the dual germ of a
four-fold contact is unibranch of multiplicity $3$, with local leading
parametrization $(t^3,t^4)$ and $\delta=3$.  It is an $E_6$ cusp, not a
tacnode.  A tacnode has two branches.  This local calculation is included in
step [](#s11){.pf-ref}.
:::

::: {.solution}
Assume throughout that $d\geq2$.  Let
$$
\gamma:X\longrightarrow X^*\subset(\PP^2)^*
$$
denote the Gauss map $P\mapsto T_P(X)$.

::: pf

::: {.pf-step #s1}
If $P\in X$ and
$$
r=I_P\bigl(X,T_P(X)\bigr),
$$
then, in suitable local coordinates, the Gauss map is
$$
t\longmapsto
\bigl(-h'(t),\,t h'(t)-h(t)\bigr),
\qquad
h(t)=a_rt^r+O(t^{r+1}),\quad a_r\ne0.
$$

::: pf-proof
Choose affine coordinates with
$$
P=(0,0),
\qquad
T_P(X)=V(y).
$$
Since $X$ is nonsingular at $P$, a local parameter $t=x$ writes the curve as
$$
y=h(t),
$$
where $h(0)=h'(0)=0$.  The order of $h$ is precisely the intersection
multiplicity with the tangent line, so
$$
h(t)=a_rt^r+O(t^{r+1}),
\qquad
r\geq2.
$$

The tangent line at $(t,h(t))$ is
$$
y-h(t)=h'(t)(x-t),
$$
or
$$
-h'(t)x+y+t h'(t)-h(t)=0.
$$
In the dual affine chart where the coefficient of $y$ is $1$, this is exactly
the displayed parametrization of $\gamma$.
:::

:::

::: {.pf-step #s2}
The morphism $\varphi:X\to L$ of part (a) is ramified at $P$ if and
only if $P\in L$ or $P$ is an inflection point.

::: pf-proof
Keep the notation of step [](#s1){.pf-ref}.

First suppose $P\notin L$.  Apply a projective change of coordinates sending
$L$ to the line at infinity.  The tangent line in step [](#s1){.pf-ref} meets $L$ at
$$
[1:h'(t):0].
$$
Thus a local parameter on the target is $h'(t)$, and, because
$\operatorname{char}k=0$,
$$
e_P(\varphi)
=
\operatorname{ord}_t h'(t)
=r-1.
$$
Hence $\varphi$ is ramified at such a point exactly when $r\geq3$, i.e. when
$P$ is an inflection point.

Now suppose $P\in L$.  Since $L$ is not tangent to $X$, choose the local
coordinates so that
$$
L=V(x),
\qquad
T_P(X)=V(y).
$$
The tangent line at $(t,h(t))$ meets $L$ at
$$
(0,h(t)-t h'(t)).
$$
Since
$$
h(t)-t h'(t)
=(1-r)a_rt^r+O(t^{r+1})
$$
and $1-r\ne0$ in characteristic $0$,
$$
e_P(\varphi)=r\geq2.
$$
Thus every point of $X\cap L$ is ramified.  These two cases prove the stated
criterion.
:::

:::

::: {.pf-step #s3}
The curve $X$ has only finitely many inflection points.

::: pf-proof
The map $\varphi$ is nonconstant.  Indeed, if it were constant with value
$Q\in L$, every tangent line to $X$ would pass through $Q$.  Projection from
$Q$ gives a nonconstant map from $X$ to $\PP^1$: it has degree $d$ if
$Q\notin X$, and after removing the base point it has degree $d-1$ if
$Q\in X$.  Away from $Q$, its differential would vanish everywhere because
the tangent line at every point passes through the centre of projection.
That would make the projection inseparable, which is impossible in
characteristic $0$.

Hence $\varphi$ is a nonconstant morphism of projective curves and therefore
finite and separable.  Its ramification locus is finite.  By step [](#s2){.pf-ref} every
inflection point outside the finite set $X\cap L$ lies in that ramification
locus, so the set of inflection points is finite.
:::

:::

::: {.pf-step #s4}
If a line $M$ is tangent to $X$ at distinct non-inflection points
$P_1,\ldots,P_s$, then the corresponding point $[M]\in X^*$ is an ordinary
$s$-fold point.  Consequently $X$ has only finitely many multiple tangents.

::: pf-proof
At a non-inflection point, step [](#s1){.pf-ref} has $r=2$, so
$$
h(t)=a_2t^2+O(t^3),
\qquad a_2\ne0.
$$
Writing the dual coordinates in step [](#s1){.pf-ref} as $(u,v)$ gives
$$
u=-2a_2t+O(t^2),
\qquad
v=a_2t^2+O(t^3).
$$
Thus the image of a neighbourhood of $P_i$ is a nonsingular branch of $X^*$.
Its tangent line is $v=0$, which intrinsically is the line
$$
P_i^*\subset(\PP^2)^*
$$
parametrizing all primal lines through $P_i$.  Since the $P_i$ are distinct,
the dual lines $P_i^*$ are distinct.  Therefore the $s$ branches through
$[M]$ are smooth and have pairwise distinct tangent directions, which is
exactly an ordinary $s$-fold point in the sense of
[[P-AGH53MULTIPLICITY|Exercise I.5.3]].

By step [](#s3){.pf-ref} there are only finitely many inflectional tangent lines.  Every
other multiple tangent gives a singular point of the projective curve $X^*$
by the preceding paragraph.  A projective curve has only finitely many
singular points, hence there are only finitely many multiple tangents.
:::

:::

::: {.pf-step #s5}
Let $O\notin X$ lie on no inflectional or multiple tangent.  Projection
from $O$ gives a degree-$d$ morphism
$$
\psi:X\longrightarrow\PP^1
$$
whose ramification points are exactly the points $P$ for which $OP=T_P(X)$,
and each has ramification index $2$.

::: pf-proof
A fibre of the projection is the intersection of $X$ with a line through
$O$.  At a point $P$, choose a local coordinate on the pencil of lines through
$O$ whose value at $P$ corresponds to the line $OP$.  The difference from
that target value is, up to a unit, a local equation for $OP$ restricted to
$X$.  Hence
$$
e_P(\psi)=I_P(X,OP).
$$
It follows that $e_P(\psi)>1$ exactly when $OP=T_P(X)$.  Since $O$ lies on no
inflectional tangent, the contact order is then exactly $2$.  The hypothesis
that $O$ lies on no multiple tangent ensures that different ramification
points give different tangent lines through $O$.

Because $O\notin X$, a general line through $O$ meets $X$ in $d$ points,
counted with multiplicity, so $\deg\psi=d$.
:::

:::

::: {.pf-step #s6}
Exactly $d(d-1)$ tangent lines to $X$ pass through such a point $O$,
and
$$
\deg X^*=d(d-1).
$$

::: pf-proof
By [[P-AGH72ARITHGENUS|Exercise I.7.2]],
$$
g(X)=\frac{(d-1)(d-2)}2,
$$
so
$$
2g(X)-2=d^2-3d.
$$
Apply Riemann--Hurwitz to the degree-$d$ map of step [](#s5){.pf-ref}.  Its ramification
divisor has degree
$$
\deg R_\psi
=2g(X)-2+2d
=d^2-d
=d(d-1).
$$
Every ramification point is simple and corresponds to exactly one tangent
through $O$, so this is the desired number of tangents.

In the dual plane, the lines through $O$ form a line $O^*$.  Its intersection
with $X^*$ consists of the tangent lines to $X$ passing through $O$.  At each
of the $d(d-1)$ points just found, $X^*$ is smooth by step [](#s4){.pf-ref}, and its
tangent line is $P^*$ for the corresponding tangency point $P$.  Since
$O\ne P$, the lines $O^*$ and $P^*$ are distinct, so the intersection is
transverse.  Therefore
$$
O^*\cdot X^*=d(d-1),
$$
which is the degree of $X^*$.
:::

:::

::: {.pf-step #s7}
For all but finitely many $O\in X$, exactly
$$
(d+1)(d-2)
$$
tangent lines to $X$, other than $T_O(X)$, pass through $O$.

::: pf-proof
By steps [](#s3){.pf-ref} and [](#s4){.pf-ref} there are only finitely many inflectional and multiple
tangent lines.  Exclude from $X$ all inflection points and all points lying on
one of those finitely many exceptional lines.  This removes only finitely
many points.

Fix a remaining point $O$.  The pencil of lines through $O$, after removing
the fixed point $O$ from each line section, defines a morphism
$$
\psi_O:X\longrightarrow\PP^1
$$
of degree $d-1$.  It is unramified at $O$: in coordinates
$$
O=(0,0),\qquad T_O(X)=V(y),\qquad y=a_2x^2+O(x^3),
$$
a local coordinate on the pencil is the slope
$$
\frac yx=a_2x+O(x^2),
$$
which has order $1$.

At a point $P\ne O$, the same argument as in step [](#s5){.pf-ref} shows that $\psi_O$
is ramified exactly when $OP=T_P(X)$.  By the choice of $O$, such a tangent
is neither inflectional nor multiple, so every ramification index is $2$ and
distinct ramification points give distinct tangent lines.  Riemann--Hurwitz
therefore gives
$$
\begin{aligned}
\#\{\text{tangents through }O\text{ other than }T_O(X)\}
&=2g(X)-2+2(d-1)\\
&=d^2-d-2\\
&=(d+1)(d-2).
\end{aligned}
$$
:::

:::

::: {.pf-step #s8}
The morphism $\varphi:X\to L$ of part (a) has degree
$$
d(d-1).
$$

::: pf-proof
Choose a general point $Q\in L$.  We may arrange that $Q\notin X$ and that
$Q$ lies on no inflectional or multiple tangent.  By step [](#s6){.pf-ref} there are
exactly $d(d-1)$ tangent lines to $X$ through $Q$.

The fibre $\varphi^{-1}(Q)$ consists exactly of their tangency points, since
$$
\varphi(P)=Q
\quad\Longleftrightarrow\quad
Q\in T_P(X).
$$
The choice of $Q$ makes those points distinct and unramified in this fibre.
Thus a general fibre has $d(d-1)$ points and
$$
\deg\varphi=d(d-1).
$$
:::

:::

::: {.pf-step #s9}
The inflection points of $X$, counted with weight
$$
I_P(X,T_P(X))-2,
$$
have total weight
$$
3d(d-2).
$$

::: pf-proof
Choose the line $L$ in part (a) generally enough that it contains no
inflection point.  Since it is not tangent to $X$, it meets $X$ transversely
in exactly $d$ points.  At each $P\in X\cap L$, step [](#s2){.pf-ref} gives
$$
e_P(\varphi)=2,
$$
so these points contribute $d$ to the ramification divisor.

If $P\notin L$ is an inflection point with
$$
r=I_P(X,T_P(X))\geq3,
$$
step [](#s2){.pf-ref} gives
$$
e_P(\varphi)=r-1,
$$
so its ramification contribution is $r-2$.  Step [](#s2){.pf-ref} shows that there is no
other ramification.

By step [](#s8){.pf-ref} and Riemann--Hurwitz,
$$
\begin{aligned}
\deg R_\varphi
&=2g(X)-2+2d(d-1)\\
&=d^2-3d+2d^2-2d\\
&=3d^2-5d.
\end{aligned}
$$
Subtracting the $d$ contributions from $X\cap L$ leaves
$$
3d^2-6d=3d(d-2),
$$
which is exactly the asserted weighted inflection count.
:::

:::

::: {.pf-step #s10}
An ordinary inflection point of $X$ maps to an ordinary cusp of
$X^*$.

::: pf-proof
At an ordinary inflection point, step [](#s1){.pf-ref} has
$$
h(t)=a_3t^3+O(t^4),
\qquad a_3\ne0.
$$
Hence the local parametrization of the dual branch is
$$
u=-3a_3t^2+O(t^3),
\qquad
v=2a_3t^3+O(t^4).
$$
Thus the branch has multiplicity $2$ and its tangent line meets it with
multiplicity $3$.  Equivalently, after formal changes of local coordinates it
has parametrization $(t^2,t^3)$, the ordinary cusp.
:::

:::

::: {.pf-step #s11}
The Gauss map $\gamma:X\to X^*$ is the normalization of $X^*$.
If $P$ is a hyperflex, then $\gamma(P)$ is a unibranch multiplicity-$3$
singularity with $\delta=3$, not a tacnode.

::: pf-proof
The Gauss map is nonconstant by the argument of step [](#s3){.pf-ref}, hence finite onto
its image.  By step [](#s4){.pf-ref} there are only finitely many multiple tangents, so a
general point of $X^*$ is the tangent line at exactly one point of $X$.
Therefore $\gamma$ is generically one-to-one and hence birational.  Since
$X$ is nonsingular and thus normal, the finite birational map
$$
\gamma:X\longrightarrow X^*
$$
is the normalization morphism.

Now suppose
$$
I_P(X,T_P(X))=4.
$$
Step [](#s1){.pf-ref} gives
$$
h(t)=a_4t^4+O(t^5),
\qquad a_4\ne0,
$$
and hence
$$
u=-4a_4t^3+O(t^4),
\qquad
v=3a_4t^4+O(t^5).
$$
This is one branch, of multiplicity $3$.  Its value semigroup has initial
values $3$ and $4$.  Hence it contains the numerical semigroup
$\langle3,4\rangle$, which contains every integer at least $6$.  Conversely,
no element of the completed local ring can have valuation $1$ or $2$, and an
element of valuation $5$ cannot occur: below valuation $6$, the only
nonconstant monomials in the two local coordinates have the distinct
valuations $3$ and $4$, so there are no equal leading terms whose
cancellation could create valuation $5$.  Thus the only gaps are
$$
1,2,5,
$$
and the normalization quotient has length
$$
\delta=3.
$$
This is the $E_6$ cusp (characteristic parametrization $(t^3,t^4)$).  In
particular it cannot be a tacnode, because a tacnode has two branches.
:::

:::

::: {.pf-step #s12}
If $X^*$ has only nodes and ordinary cusps, then the number $b$ of
bitangents in the strict sense of part (b) is
$$
b=\frac12d(d-2)(d-3)(d+3).
$$

::: pf-proof
Under the stated hypothesis every inflection point is ordinary.  Indeed, if
its tangent contact had order $r\geq4$, step [](#s1){.pf-ref} would give a dual branch of
multiplicity $r-1\geq3$, which is neither a node nor an ordinary cusp.
Therefore step [](#s9){.pf-ref} shows that the number of cusps of $X^*$ is
$$
\kappa=3d(d-2).
$$

Under the stated singularity hypothesis, a multiple tangent cannot contain
an inflection point: otherwise the corresponding point of $X^*$ would have
at least one singular branch together with another branch, hence would be
neither a node nor an ordinary cusp.  It also cannot be tangent at three or
more distinct points, because step [](#s4){.pf-ref} would give an ordinary multiple
point with at least three branches.  Thus every multiple tangent is tangent
at exactly two non-inflection points, i.e. is a strict bitangent, and step
[](#s4){.pf-ref} shows that it gives an ordinary node of $X^*$.  Conversely, by step
[](#s11){.pf-ref} the two branches of a node lift under the normalization to two distinct
points of $X$ having the same tangent line.  Hence the number of nodes is
exactly $b$.

Put
$$
m=\deg X^*=d(d-1).
$$
The arithmetic genus of the plane curve $X^*$ is
$$
p_a(X^*)=\frac{(m-1)(m-2)}2.
$$
Since $X$ is its normalization, [[P-AGH418ARITHGENUSSINGULAR|Exercise
IV.1.8]] gives
$$
g(X)=p_a(X^*)-b-\kappa,
$$
because a node and an ordinary cusp each have $\delta$-invariant $1$.
Substituting
$$
g(X)=\frac{(d-1)(d-2)}2,
\qquad
m=d(d-1),
\qquad
\kappa=3d(d-2)
$$
gives
$$
\begin{aligned}
2b
&=(m-1)(m-2)-(d-1)(d-2)-6d(d-2)\\
&=d^4-2d^3-9d^2+18d\\
&=d(d-2)(d-3)(d+3).
\end{aligned}
$$
Dividing by $2$ proves part (f).
:::

:::

::: {.pf-step #s13}
A plane cubic has exactly nine inflection points, all ordinary, and
the line through any two of them meets the cubic in a third inflection point.

::: pf-proof
For $d=3$, step [](#s9){.pf-ref} gives total inflection weight
$$
3\cdot3\cdot(3-2)=9.
$$
A tangent line to a nonsingular cubic cannot have contact order greater than
$3$ by Bézout, so every inflection has contact order exactly $3$ and weight
$1$.  Hence there are exactly nine of them, all ordinary.

Let $P$ and $Q$ be distinct inflection points, and let a line through them
meet $X$ in the divisor
$$
P+Q+R.
$$
The third point is distinct from $P,Q$: if the line were tangent at either,
then because that point is a flex its intersection multiplicity there would
already be $3$, leaving no room for the other point.

Let $H$ denote a line section.  The flex tangents give
$$
3P\sim H,
\qquad
3Q\sim H,
$$
while the line through $P,Q$ gives
$$
P+Q+R\sim H.
$$
Therefore
$$
3R
\sim3H-3P-3Q
\sim H.
$$
For a plane cubic, $g=1$ and $\deg H=3$, so Riemann--Roch gives
$\ell(H)=3$.  The three-dimensional space of ambient linear forms restricts
injectively to $H^0(X,\OO_X(H))$, hence it is the complete linear system
$|H|$.  Thus the effective divisor $3R\in|H|$ is cut out by a line, and that
line has contact order $3$ at $R$.  Hence $R$ is also an inflection point.
:::

:::

::: {.pf-step #s14}
For an arbitrary nonsingular plane quartic, if $h$ is the number of
hyperflex lines and $b$ the number of strict bitangents, then
$$
b=28-h.
$$
Consequently there are always exactly $28$ generalized bitangent lines when
hyperflexes are included.

::: pf-proof
For a quartic, every tangent contact has order at most $4$.  Let $f$ be the
number of ordinary flexes and $h$ the number of hyperflexes.  Step [](#s9){.pf-ref} gives
the weighted relation
$$
f+2h=24.
$$

By step [](#s6){.pf-ref}, the dual curve has degree
$$
4(4-1)=12,
$$
so
$$
p_a(X^*)=\frac{(12-1)(12-2)}2=55.
$$
Its normalization is the genus-$3$ curve $X$ by step [](#s11){.pf-ref}.  A singular
point of $X^*$ with at least two normalization preimages is a line tangent
to $X$ at at least two distinct points; Bézout forces the contact divisor to
be $2P+2Q$, so it is a strict bitangent.  A singular point with one
normalization preimage comes from a point where the local Gauss
parametrization of step [](#s1){.pf-ref} is singular, hence from contact order $3$ or
$4$.  Therefore the singularities of $X^*$ are exactly:

- the $b$ nodes coming from strict bitangents, each with $\delta=1$;
- the $f$ ordinary cusps coming from ordinary flexes, each with $\delta=1$;
- the $h$ hyperflex cusps of step [](#s11){.pf-ref}, each with $\delta=3$.

The genus formula of [[P-AGH418ARITHGENUSSINGULAR|Exercise IV.1.8]] now gives
$$
3
=55-(b+f+3h),
$$
so
$$
b+f+3h=52.
$$
Using $f=24-2h$ yields
$$
b=52-(24-2h)-3h=28-h.
$$
Thus $b+h=28$, proving the corrected form of part (h).

For the Fermat quartic in the erratum, the $12$ displayed hyperflexes already
contribute total inflection weight $24$, so step [](#s9){.pf-ref} shows there are no
others.  Hence $h=12$ and
$$
b=28-12=16,
$$
which explicitly disproves the literal strict-bitangent reading of part (h).
:::

:::

::: pf-qed
Steps [](#s1){.pf-ref}, [](#s2){.pf-ref}, and [](#s3){.pf-ref} prove part (a), step [](#s4){.pf-ref} proves part (b), steps [](#s5){.pf-ref} and [](#s6){.pf-ref}
prove part (c), step [](#s7){.pf-ref} proves part (d), steps [](#s8){.pf-ref}, [](#s9){.pf-ref}, and [](#s10){.pf-ref} prove part (e),
step [](#s12){.pf-ref} proves part (f), step [](#s13){.pf-ref} proves part (g), and step [](#s14){.pf-ref} proves
the corrected form of part (h).  Step [](#s11){.pf-ref} supplies the local correction to
the source's four-fold-contact parenthetical.
:::

:::
:::
