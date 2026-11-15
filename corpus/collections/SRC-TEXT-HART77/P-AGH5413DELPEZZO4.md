---
schema: qual/card@1
id: P-AGH5413DELPEZZO4
kind: problem
title: The 16 lines on the degree four Del Pezzo surface and its equations
classification:
  areas:
  - algebraic-geometry
  topics:
  - Cubic Surfaces
  - Blowups
  - Intersection Theory
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-19
  note: >-
    Read Hartshorne V.4.13, the retained Egbert solution, the degree-four
    Del Pezzo blowup model from V.4.7, and the immediately preceding Kodaira
    vanishing exercise V.4.12. Cross-checked the standard description against
    Dolgachev's treatment of quartic Del Pezzo surfaces. The 16 displayed
    lines are the five exceptional curves, ten transforms of pairwise joining
    lines, and the transform of the conic through all five points. For the
    equations, Riemann--Roch and V.4.12 give h^0(-2K_X)=13, so at least two
    independent quadrics contain the anticanonical image; their degree-four
    complete intersection must equal the degree-four surface X.
- event: solution-written
  by: chatgpt
  date: 2026-09-19
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-19
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Part (b) closed on a published proof, for issue #121. M. I. Dolgachev, Topics
    in Classical Algebraic Geometry (27 September 2010), the complete 524-page
    book in tmp/sources/dolgachev-topics-classical-ag.pdf with printed page =
    PDF page minus ten, states and proves at Theorem 8.5.1, printed p. 291 with
    the proof on pp. 291--292, that an anticanonical model of a weak Del Pezzo
    surface of degree 4 is a complete intersection of two quadrics in P^4,
    reducible to the diagonal pair sum t_i^2 = sum a_i t_i^2 with distinct a_i.
    Read that proof: the projective normality is his Theorem 8.4.5, printed
    p. 280, the dimension h^0(O_X(2)) = 13 his Lemma 8.3.1, printed p. 272, the
    pencil then has five singular members by the discriminant count, and the
    five singular points of those quadrics are the coordinate points. The
    exercise's surface is that model, the blow-up of five points of P^2
    anticanonically embedded in P^4 with K^2 = 4. His proof quotes Ramanujam's
    vanishing theorem in Lemma 8.3.1 and cites it as Lazarsfeld, Positivity in
    Algebraic Geometry I, Theorem 4.3.1; the card's own h^0 computation is
    Riemann-Roch on the blow-up and does not need it, so the card's proof and
    his agree. Part (a) is not covered: printed p. 293 uses "the 16 lines on X"
    without proving the count, so the card's own count stands for (a). Egbert's
    entry, cited before, stops in part (b) at the dimension count.
---

::: {.problem}
Let $X$ be the Del Pezzo surface of degree 4 in $\PP^4$ obtained by blowing up 5 points of $\PP^2$ (4.7).

(a) Show that $X$ contains 16 lines.

(b) Show that $X$ is a complete intersection of two quadric hypersurfaces in $\PP^4$ (the converse follows from (4.7.1)).
:::

::: {.solution}
Let
$$
\pi:X\longrightarrow\PP^2
$$
be the blowup of the five points $P_1,\ldots,P_5$ in general position. Write
$L$ for the pullback of a line and $E_i$ for the exceptional curves. The
anticanonical embedding of (4.7) is given by
$$
H=-K_X=3L-E_1-\cdots-E_5,
\qquad
H^2=4.
$$

::: pf

::: {.pf-step #exceptional-curves-lines}
The five exceptional curves $E_i$ are lines in the anticanonical
embedding.

::: pf-proof
The intersection form on the blowup is
$$
L^2=1,
\qquad
L\cdot E_i=0,
\qquad
E_i\cdot E_j=0\ (i\ne j),
\qquad
E_i^2=-1.
$$
Hence
$$
H\cdot E_i=1.
$$
Each $E_i\cong\PP^1$, and the very ample divisor $H$ embeds it as a curve of
degree one in $\PP^4$. Thus every $E_i$ is a line on $X$.
:::

:::

::: {.pf-step #pairwise-join-lines}
For every pair $1\le i<j\le5$, the strict transform of the line through
$P_i$ and $P_j$ is a line on $X$.

::: pf-proof
Because the five points are in general position, the line through $P_i,P_j$
contains none of the other three points. Its strict transform $L_{ij}$ has
class
$$
L-E_i-E_j.
$$
Therefore
$$
H\cdot L_{ij}
=(3L-E_1-\cdots-E_5)\cdot(L-E_i-E_j)
=3-1-1
=1.
$$
The curve $L_{ij}$ is isomorphic to $\PP^1$, so the anticanonical embedding
maps it to a line. There are
$$
\binom52=10
$$
such curves.
:::

:::

::: {.pf-step #conic-transform-line}
The strict transform of the conic through $P_1,\ldots,P_5$ is a line
on $X$.

::: pf-proof
Five points in general position determine a unique conic $Q$. It is
irreducible: if it were the union of two lines, one of those lines would
contain at least three of the five points, contrary to general position.
Thus $Q$ is a nonsingular conic and its strict transform $\widetilde Q$ has
class
$$
2L-E_1-\cdots-E_5.
$$
Consequently
$$
H\cdot\widetilde Q=6-5=1.
$$
Since $\widetilde Q\cong\PP^1$, it is mapped to a line by the anticanonical
embedding.
:::

:::

::: {.pf-step #sixteen-lines-total}
The surface $X$ contains 16 distinct lines.

::: pf-proof
Steps [](#exceptional-curves-lines){.pf-ref}, [](#pairwise-join-lines){.pf-ref} and [](#conic-transform-line){.pf-ref} give respectively
$$
5,
\qquad
10,
\qquad
1
$$
lines. Their divisor classes are respectively
$$
E_i,
\qquad
L-E_i-E_j,
\qquad
2L-E_1-\cdots-E_5,
$$
so they are distinct. Hence $X$ contains
$$
\boxed{5+10+1=16}
$$
lines, and by step [](#no-other-lines){.pf-ref} no further one. This proves part (a).
:::

:::

::: {.pf-step #no-other-lines}
Every line of $X$ is one of the $16$ listed in step [](#sixteen-lines-total){.pf-ref}.

::: pf-proof
A line $C\subseteq X$ satisfies $H\cdot C=1$ and $p_a(C)=0$, so adjunction
with $K_X=-H$ gives
$$
-2=C\cdot(C+K_X)=C^2-H\cdot C=C^2-1,
\qquad\text{hence}\qquad
C^2=-1 .
$$
Write $C\sim aL-\sum_ib_ie_i$. If $C$ is one of the exceptional curves then
$C\sim E_i$. Otherwise $C$ is the strict transform of an irreducible plane
curve of degree $a>0$ with multiplicity $b_i\ge0$ at $P_i$, so
$$
3a-\sum_i b_i=H\cdot C=1,
\qquad
a^2-\sum_i b_i^2=C^2=-1 .
$$
Cauchy--Schwarz for the five numbers $b_1,\ldots,b_5$ gives
$$
(3a-1)^2=\Bigl(\sum_i b_i\Bigr)^2\le5\sum_i b_i^2=5(a^2+1),
$$
that is $4a^2-6a-4\le0$, so $a\in\{1,2\}$ because $a>0$ is an integer.

If $a=1$, then $\sum b_i=2$ and $\sum b_i^2=2$, so exactly two of the $b_i$
equal $1$ and the rest vanish; then $C\sim L-E_i-E_j=L_{ij}$.

If $a=2$, then $\sum b_i=5$ and $\sum b_i^2=5$, whence
$$
\sum_i b_i(b_i-1)=\sum_i b_i^2-\sum_i b_i=0 .
$$
Each $b_i\ge0$ is an integer, so $b_i(b_i-1)\ge0$ with equality only for
$b_i\in\{0,1\}$; thus all five multiplicities equal $1$ and
$C\sim 2L-\sum_ie_i=\widetilde Q$.

Finally, two distinct irreducible curves never have equal class on a smooth
surface, because their intersection number would then be the negative number
$C^2=-1$. So each of these $16$ classes carries exactly one line, and there
are no others.
:::

:::

::: {.pf-step #h0-two-h-thirteen}
One has
$$
\boxed{h^0(X,\OO_X(2H))=13.}
$$

::: pf-proof
The surface $X$ is rational, so
$$
\chi(\OO_X)=1.
$$
Riemann--Roch on a nonsingular projective surface gives, for $D=2H=-2K_X$,
$$
\begin{aligned}
\chi(\OO_X(2H))
&=\chi(\OO_X)+\frac12(2H)\cdot(2H-K_X)\\
&=1+\frac12(2H)\cdot3H\\
&=1+3H^2\\
&=13.
\end{aligned}
$$

By Serre duality,
$$
H^2(X,\OO_X(2H))
\cong
H^0(X,\OO_X(K_X-2H))^*
=H^0(X,\OO_X(-3H))^*
=0,
$$
because $H$ is ample. Also
$$
H^1(X,\OO_X(2H))
\cong
H^1(X,\OO_X(-3H))^*
=0
$$
by [[P-AGH5412KODAIRAVANISH|Exercise V.4.12]], applied to the ample divisor
$3H$. Thus $h^0(X,\OO_X(2H))=\chi(\OO_X(2H))=13$.
:::

:::

::: {.pf-step #two-quadrics-contain-x}
At least two linearly independent quadric hypersurfaces of $\PP^4$
contain $X$.

::: pf-proof
The anticanonical embedding satisfies
$$
\OO_X(1)=\OO_X(H),
$$
so restriction of quadratic forms gives a linear map
$$
H^0(\PP^4,\OO_{\PP^4}(2))
\longrightarrow
H^0(X,\OO_X(2H)).
$$
The source has dimension
$$
\binom{4+2}{2}=15,
$$
whereas step [](#h0-two-h-thirteen){.pf-ref} gives dimension $13$ for the target. Hence the kernel has
dimension at least two. Choose linearly independent quadrics
$$
Q_1,Q_2
$$
from this kernel. Then
$$
X\subseteq Q_1\cap Q_2.
$$
:::

:::

::: {.pf-step #quadrics-no-common-component}
The quadrics $Q_1$ and $Q_2$ have no common hypersurface component.

::: pf-proof
If two independent quadrics in $\PP^4$ have a common hypersurface component,
that component is a hyperplane: their equations have a common linear factor.
Thus their intersection is the union of that hyperplane and a codimension-two
linear space. Since the irreducible surface $X$ is contained in this union, it
would be contained in one of those two linear subspaces. This is impossible:
the complete anticanonical linear system embeds $X$ nondegenerately in
$\PP^4$. Hence $Q_1,Q_2$ form a regular sequence and their intersection is a
pure surface complete intersection.
:::

:::

::: {.pf-step #x-is-complete-intersection}
One has
$$
\boxed{X=Q_1\cap Q_2}
$$
scheme-theoretically.

::: pf-proof
By step [](#quadrics-no-common-component){.pf-ref}, the complete intersection
$$
Y=Q_1\cap Q_2
$$
is a pure two-dimensional scheme of degree
$$
\deg Y=2\cdot2=4.
$$
On the other hand, the degree of the anticanonically embedded surface is
$$
\deg X=H^2=4.
$$
Step [](#two-quadrics-contain-x){.pf-ref} gives $X\subseteq Y$. Since $Y$ is pure of the same dimension as
the irreducible reduced surface $X$, the component of $Y$ supported on $X$
already contributes at least $\deg X=4$ to the degree of $Y$. Equality of the
degrees leaves neither another two-dimensional component nor a nonreduced
multiplicity along $X$. Thus $Y=X$ as schemes.

Therefore $X$ is the complete intersection of two quadric hypersurfaces in
$\PP^4$, proving part (b).
:::

:::

::: pf-qed
Steps [](#sixteen-lines-total){.pf-ref} and [](#no-other-lines){.pf-ref} prove part (a), and steps [](#h0-two-h-thirteen){.pf-ref}, [](#two-quadrics-contain-x){.pf-ref}, [](#quadrics-no-common-component){.pf-ref} and [](#x-is-complete-intersection){.pf-ref} prove part (b).
:::

:::
:::

::: {.remark title="Published solutions"}
M. I. Dolgachev, *Topics in Classical Algebraic Geometry* (27 September 2010), read in
`tmp/sources/dolgachev-topics-classical-ag.pdf`, whose printed page is its PDF page minus ten, §8.5.1,
Theorem 8.5.1, printed p. 291 with its proof on pp. 291--292, is a published complete proof of part (b).
The theorem: an anticanonical model $X$ of a weak Del Pezzo surface $S$ of degree $4$ is a complete
intersection of two quadrics in $\PP^4$, projectively normal by his Theorem 8.4.5 (printed p. 280), its
$h^0(\OO_X(2))=13$ by his Lemma 8.3.1 (printed p. 272), the pencil of quadrics through it having exactly
five singular members by the discriminant count, after which coordinates with the five singular points of
those quadrics as the coordinate points put the two equations in the diagonal form
$$
\sum_{i=0}^{4}t_i^2=\sum_{i=0}^{4}a_it_i^2=0,\qquad a_i\ne a_j\ (i\ne j).
$$
The surface of the exercise is that model: the blow-up of five points of $\PP^2$ embedded by
$\abs{-K}$ in $\PP^4$, with $K^2=9-5=4$, so his hypotheses hold and the card is closed on it for part (b). His
proof's one outside input is Ramanujam's vanishing theorem, quoted in the proof of Lemma 8.3.1 and cited
there as Lazarsfeld, *Positivity in Algebraic Geometry* I, Theorem 4.3.1; the card's own step
[](#h0-two-h-thirteen){.pf-ref} reaches the same $h^0=13$ by Riemann--Roch on the blow-up. Part (a), the
sixteen lines, is not proved there: his §8.5.2 uses "the 16 lines on $X$" at printed p. 293 without an
argument for the count, so part (a) rests on the card's steps
[](#sixteen-lines-total){.pf-ref} and [](#no-other-lines){.pf-ref}.

A. Egbert, *Solutions to Hartshorne's Algebraic Geometry* (2013), V.4.13, printed pp. 292--293, is
incomplete in both parts: part (a) at p. 292 lists the 16 classes and counts $4a^2-6a-4\le0$ but does not
exclude a class with three distinct intersection patterns, and part (b) at p. 293 stops at the dimension
count $h^0(\OO_X(2H))=13$ against $h^0(\OO_{\PP^4}(2))=15$ without the degree comparison that identifies
$X$ with the intersection.
:::
