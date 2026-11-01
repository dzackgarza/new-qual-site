---
schema: qual/card@1
id: E-HAT-3.C-16
kind: problem
title: Classification of Hopf algebras over $\ZZ$
classification:
  areas:
  - topology
  topics:
  - H-Spaces
  - Hopf Algebras
  - Cohomology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.C, Exercise 16; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.C, Exercise 16; it matches the printed text.
- event: source-corrected
  by: claude
  date: 2026-10-31
  note: >-
    The book writes the homogeneous component $A_n$ with a subscript; the card had $A^n$.
    The printed grading is restored.
- event: solution-reviewed
  by: claude
  date: 2026-11-01
  note: >-
    Proof read and checked against both parities of $d$. The table of $b_{ij}$ is right: for even
    $d$ it is $\binom{i+j}{i}$, and for odd $d$ the two middle terms of $\Delta(t)^2$ cancel
    instead of adding, so $b_{ij}=0$ when $i$ and $j$ are both odd and
    $\binom{\lfloor(i+j)/2\rfloor}{\lfloor i/2\rfloor}$ otherwise — checked on $(x+y)^3$ with
    $x=t\otimes1$ and $y=1\otimes t$ of odd degree, which is $x^3+x^2y+xy^2+y^3$. The reduction to
    a positive-integer cocycle $(m_{ij})$ on a rank-one basis is correct, as are the recursion
    $q_{n+1}=q_n/m_{n,1}$, the two examples $\ZZ[t]$ and $\Gamma_{\ZZ}[t]$, and the criterion
    $m_{ij}\mid b_{ij}$ with the cocycle $m_{ij}m_{i+j,k}=m_{jk}m_{i,j+k}$. Repaired: the criterion
    now carries the normalizations $m_{i0}=m_{0i}=1$ and says why multiplicativity and
    coassociativity of $\Delta$ are automatic, both targets being free and hence torsionfree,
    rather than conditions to impose; and the solution wrote $A^{nd}$ where the corrected statement
    has $A_{nd}$. Corrected over-claim: the paragraph on $A\otimes\FF_p$ asserted that the mod-$p$
    Hopf algebra is determined by the valuations $v_p(m_{ij})$. It is not: $v_p$ records only
    whether a structure constant vanishes, and the reduction also depends on the residues, modulo
    the unit action $\overline{m_{ij}}\mapsto\overline{m_{ij}}u_iu_j/u_{i+j}$. The paragraph now
    states the valuations as a necessary invariant with $e_{i0}=e_{0i}=0$, and keeps the correct
    converse — any divisor cocycle of valuations lifts to an integral form whose reduction vanishes
    exactly where $e_{ij}>0$. The classification of the reductions up to unit rescaling is recorded
    as open, not as proved.
- event: solution-reviewed
  by: claude
  date: 2026-11-01
  note: >-
    The reduction question left open by the previous note is now settled for the family the card
    constructs, and the residual is stated exactly. Added: Proposition 1, that the isomorphism classes
    of reductions are the orbits of (F_p^x)^N acting by m_ij -> m_ij u_i u_j / u_{i+j}, with the support
    of the reduced structure constants an invariant (zeros cannot be rescaled away); Proposition 2,
    that if no m_ij is divisible by p then a rescaling by u_n = q_n^{-1} makes every structure constant
    1, so the reduction is the polynomial Hopf algebra F_p[x], and that p | m_ij forces p | binom(i+j,i),
    so nothing vanishes in degrees below p*d; Proposition 3, that the divided-power reduction is not
    isomorphic to F_p[x], since gamma_1^p = p! gamma_p = 0 there while x^p is nonzero; Proposition 4,
    that for m_ij = p^{e_ij} the reductions are classified by the support S = {e_ij > 0}, one for each
    admissible S. Still open and said so: for a general form the residues off the support need not be
    normalisable to 1 -- the constraints u_{i+j} = m_ij u_i u_j on the complement graph are satisfiable
    exactly when the product of the residues around each cycle is 1 -- so deciding the orbit set for a
    fixed support is a 1-cocycle computation not carried out here. The refuted claim remains refuted:
    the valuations determine the support, not the reduction.
- event: source-corrected
  by: claude
  date: 2026-11-01
  note: >-
    Correction to the previous note on this card, which asserted that the residues off the support "need
    not be normalisable to 1" and that the valuations therefore do not determine the mod-p Hopf algebra.
    Neither assertion is supported: no counterexample is known and no proof was given. What is now on the
    card is what can be proved. Proposition 5: after taking logarithms in F_p^x, an isomorphism between
    two reductions with the same support is exactly a solution of the triangular system
    v_{i+j} = c_ij + v_i + v_j over Z/(p-1), so the classification is a finite linear problem, consistent
    iff the values proposed at each level agree. Theorem 6: for p = 2 the reduced constants are already
    0 or 1 because F_2^x = {1}, so the support alone classifies the reductions and the valuation claim is
    TRUE there. Proposition 4: for m_ij = p^{e_ij} the support classifies. The residual is stated as open
    for odd p, with the mechanism named: when the auxiliary pairs are singular the integral cocycle
    relates the residues off the support to the unit parts of the singular constants, which the
    valuations cannot see. The search recorded on the card (all forms with m_{1j} <= 24, j <= 6) found no
    pair of equal support with non-isomorphic reductions, and that is reported as a finite check, not a
    theorem.
---

::: {.problem}
Classify algebraically the Hopf algebras $A$ over $\ZZ$ such that $A_n$ is free for each $n$ and $A \otimes \QQ \approx \QQ[\alpha]$.
In particular, determine which Hopf algebras $A \otimes \ZZ_p$ arise from such $A$'s.
:::

::: {.solution}
We classify these Hopf algebras as integral Hopf lattices in a rational polynomial Hopf algebra.

Let $A$ satisfy the hypotheses and let $d>0$ be the least positive degree in which $A\otimes\QQ$ is nonzero. Since
$$
A\otimes\QQ\cong\QQ[t]
$$
as a graded algebra, $\gradeddegree{t}=d$ is positive. Hatcher's Hopf algebra need not be graded-commutative, so $d$ may be odd. In degree $d$ there are no positive-degree decomposable terms, so the Hopf axioms force
$$
\Delta(t)=t\otimes1+1\otimes t.
$$
Consequently $\Delta(t^n)=\sum_{i+j=n}b_{ij}t^i\otimes t^j$. If $d$ is even, $b_{ij}=\binom{i+j}{i}$. If $d$ is odd, the two terms of $\Delta(t)$ anticommute in the graded tensor product, giving
$$
b_{ij}=\begin{cases}
0&i,j\text{ both odd},\\
\displaystyle\binom{\lfloor(i+j)/2\rfloor}{\lfloor i/2\rfloor}&\text{otherwise}.
\end{cases}
$$

Since each $A_{nd}$ is a free rank-one subgroup of $\QQ t^n$, choose generators
$$
x_n=q_nt^n,
\qquad q_n\in\QQ_{>0},
\qquad q_0=q_1=1,
$$
where rescaling $t$ has been used to normalize $q_1=1$. Then
$$
x_ix_j=m_{ij}x_{i+j},
\qquad
m_{ij}=\frac{q_iq_j}{q_{i+j}},
$$
and
$$
\Delta(x_n)
=\sum_{i+j=n}c_{ij}x_i\otimes x_j,
\qquad
c_{ij}=b_{ij}\frac{q_{i+j}}{q_iq_j}.
$$
Thus $A$ is an integral Hopf algebra exactly when, for every $i,j\ge0$,
$$
\boxed{m_{ij}\in\ZZ_{>0},\qquad
c_{ij}=\frac{b_{ij}}{m_{ij}}\in\ZZ,}
$$
with $m_{i0}=m_{0i}=1$ for all $i$.
Equivalently, $m_{ij}$ divides $b_{ij}$ whenever $b_{ij}\ne0$; a zero $b_{ij}$ imposes no divisibility condition.

Two of the Hopf axioms need no further condition, and it is worth saying why. Multiplicativity and coassociativity of $\Delta$ are identities between elements of $A\otimes A$ and of $A\otimes A\otimes A$; they hold for the corresponding rational map, and both targets are free, hence torsionfree, so they hold integrally. The counit is $\varepsilon(x_0)=1$, $\varepsilon(x_n)=0$. What the displayed conditions encode is closure under multiplication and the coproduct formula, together with associativity of the multiplication, which is the cocycle relation below.
Associativity is exactly the cocycle relation
$$
\boxed{m_{ij}m_{i+j,k}=m_{jk}m_{i,j+k}}
$$
with $m_{i0}=m_{0i}=1$. Conversely, any positive-integer system $(m_{ij})$ satisfying these divisor and cocycle conditions determines $q_n$ recursively by
$$
q_0=q_1=1,
\qquad
q_{n+1}=\frac{q_n}{m_{n,1}},
$$
and the cocycle identity then gives
$$
m_{ij}=q_iq_j/q_{i+j}
$$
for all $i,j$. The formulas above define a Hopf-stable lattice
$$
A=\bigoplus_{n\ge0}\ZZ\,q_nt^n\subset\QQ[t].
$$
This proves the classification. When $d$ is even, two examples are
$$
m_{ij}=1,
$$
which gives the polynomial Hopf algebra $\ZZ[t]$, and
$$
m_{ij}=\binom{i+j}{i},
$$
which gives the divided-power Hopf algebra $\Gamma_{\ZZ}[t]$. For odd $d$, the polynomial form still has $m_{ij}=1$, while the vanishing $b_{ij}$ allow further integral forms.

Now fix a prime $p$ and reduce modulo $p$. With $\bar x_n$ denoting the image of $x_n$, every reduction arising from an integral form above has
$$
\bar x_i\bar x_j=\overline{m_{ij}}\,\bar x_{i+j},
$$
$$
\Delta(\bar x_n)
=\sum_{i=0}^n
\overline{\frac{b_{i,n-i}}{m_{i,n-i}}}
\,\bar x_i\otimes\bar x_{n-i}.
$$
The $p$-adic valuations
$$
e_{ij}=v_p(m_{ij})
$$
satisfy
$$
0\le e_{ij}\le v_p(b_{ij}),
\qquad
e_{i0}=e_{0i}=0,
$$
and the additive cocycle relation
$$
e_{ij}+e_{i+j,k}=e_{jk}+e_{i,j+k},
$$
because divisibility and the product cocycle pass to valuations. Here $v_p(0)=\infty$, so a zero coproduct coefficient imposes no upper bound. But $e_{ij}$ records only whether $\overline{m_{ij}}$ vanishes: $m_{ij}=p$ and $m_{ij}=p^2$ reduce alike, and when $e_{ij}=0$ the reduction still depends on the residue in $\FF_p^\times$. Likewise a rescaling $x_n\mapsto u_nx_n$ with $u_n\in\FF_p^\times$ changes $\overline{m_{ij}}$ to $\overline{m_{ij}}u_iu_j/u_{i+j}$, so forms with different residues can have isomorphic reductions. The valuations therefore give the *vanishing pattern* of the reduction, a necessary invariant, not the mod-$p$ Hopf algebra itself.

### The classification of the reductions

Write $\bar x_n$ for the image of $x_n=q_nt^n$ in $B=A\otimes\FF_p$, so that $\{\bar x_n\}$ is an $\FF_p$-basis with $\deg\bar x_n=nd$ and $\bar x_0=1$. Since $A_n$ is free of rank one, $B$ has one basis vector in each degree $nd$ and none elsewhere. An isomorphism of graded Hopf algebras $B\to B'$ is therefore given by $\bar x_n\mapsto u_n\bar y_n$ with $u_n\in\FF_p^\times$ and $u_0=1$, and it carries the structure constants to
$$
\bar m_{ij}\longmapsto \bar m_{ij}\,\frac{u_iu_j}{u_{i+j}},
\qquad
\overline{b_{ij}/m_{ij}}\longmapsto \overline{b_{ij}/m_{ij}}\,\frac{u_{i+j}}{u_iu_j},
$$
the two transformations being inverse, so it is enough to record the product constants. Normalise the basis once and for all by $q_1=1$, which leaves every $m_{ij}$ unchanged because $q_n\mapsto q_nc^n$ does not move $m_{ij}=q_iq_j/q_{i+j}$.

**Proposition 1 (the orbit space).** *The isomorphism classes of reductions are the orbits of the action of $(\FF_p^\times)^{\NN}$ on the reduced cocycles $(\bar m_{ij})$, and the support $\{(i,j):\bar m_{ij}=0\}$ is an isomorphism invariant.*

*Proof.* The action displayed above is the action of the change of basis, and two bases of $B$ differ by such a $(u_n)$, so the orbits are exactly the isomorphism classes. If $\bar m_{ij}=0$ then $\bar m_{ij}u_iu_j/u_{i+j}=0$ for every choice of units, so a zero structure constant cannot be removed; hence the support is invariant. $\square$

**Proposition 2 (no vanishing below degree $p$).** *If $p\nmid m_{ij}$ for all $i,j$ then $B\cong\FF_p[x]$ with $x=\bar x_1$ of degree $d$. More generally $p\mid m_{ij}$ forces $p\mid b_{ij}$, so for $i+j<p$ no $m_{ij}$ is divisible by $p$; consequently every reduction agrees with $\FF_p[x]$ in degrees $<pd$.*

*Proof.* From $m_{1,j}=q_1q_j/q_{1+j}$ and $q_1=1$ we get $q_n=\prod_{j=1}^{n-1}m_{1,j}^{-1}$. If all $m_{ij}$ are $p$-units then every $q_n$ is a $p$-unit, so $u_n:=q_n^{-1}\bmod p$ is a well-defined unit and $\bar m_{ij}u_iu_j/u_{i+j}=\bar m_{ij}\bar m_{ij}^{-1}=1$: after this rescaling all structure constants are $1$, and the coproduct constants become $\overline{b_{ij}/m_{ij}}\cdot1=\overline{b_{ij}}$, which is the coproduct of the polynomial Hopf algebra. For the second statement, integrality of the coproduct says $m_{ij}\mid b_{ij}$ in $\ZZ$, so $p\mid m_{ij}$ implies $p\mid b_{ij}$; and for $i+j<p$ the binomial coefficient $b_{ij}=\binom{i+j}{i}$ is not divisible by $p$ (no carry occurs in adding $i$ and $j$ in base $p$, by Lucas' theorem), so $p\nmid m_{ij}$. $\square$

**Proposition 3 (the two extremes differ).** *For $d$ even, $\Gamma_{\ZZ}[t]\otimes\FF_p$ is not isomorphic to $\FF_p[t]$ as a graded algebra.*

*Proof.* In $\Gamma_{\ZZ}[t]$ one has $\gamma_1^n=n!\,\gamma_n$, so in $\Gamma_{\ZZ}[t]\otimes\FF_p$ the element $\bar\gamma_1$ satisfies $\bar\gamma_1^{\,p}=\overline{p!}\,\bar\gamma_p=0$, while $\bar\gamma_p\neq0$ because $\gamma_p$ is a basis vector and $\Gamma_{\ZZ}$ is free. In $\FF_p[t]$ the $p$-th power map from degree $d$ to degree $pd$ is injective. A graded isomorphism preserves support of elements and $p$-th powers, so none exists. $\square$

**Proposition 4 (the reductions with entries in $\{0,1\}$).** *Let $e_{ij}$ satisfy the conditions recorded above, let $m_{ij}=p^{e_{ij}}$ with valuation $0$ at every other prime, and let $S=\{(i,j):e_{ij}>0\}$. The reduction of the resulting form has $\bar m_{ij}=0$ on $S$ and $\bar m_{ij}=1$ off $S$, and two such reductions are isomorphic if and only if $S=S'$.*

*Proof.* $\bar m_{ij}$ is $0$ or $1$ by construction, and the coproduct constant is $\overline{b_{ij}/m_{ij}}=\overline{b_{ij}/m_{ij}}$, an integer by the criterion. Proposition 1 gives that the support is an invariant; conversely, if $S=S'$ then the identity rescaling $u_n=1$ already makes the two reduced cocycles equal. $\square$

So for this family the answer to the exercise's second question is complete: the reductions are exactly the $\FF_p$-Hopf algebras with $\bar x_i\bar x_j=\bar x_{i+j}$ off an admissible $S$ and $\bar x_i\bar x_j=0$ on $S$, one for each admissible $S$, and admissible $S$ are those of the form $\{e_{ij}>0\}$ for a divisor cocycle $e$ with $e_{ij}\le v_p(b_{ij})$ and $e_{i0}=e_{0i}=0$ — the converse construction recorded below shows every such $S$ occurs.

**Proposition 5 (the general normalisation problem is a linear system).** *Let $g$ generate $\FF_p^\times$ and write $\bar m_{ij}=g^{c_{ij}}$ for $(i,j)\notin S$. A rescaling $(u_n)$ exists if and only if there are $v_n\in\ZZ/(p-1)$ with $u_n=g^{v_n}$ satisfying*
$$
v_{i+j}\equiv c_{ij}+v_i+v_j \pmod{p-1}\qquad\text{for every }(i,j)\notin S .
$$
*This system is triangular: each equation has index $i+j$ exceeding both $i$ and $j$, so it determines $v_{i+j}$ from earlier values and the system is solvable if and only if, for every $n$ and every two pairs $(i,n-i),(j,n-j)\notin S$, the two resulting values of $v_n$ agree.*

*Proof.* $u_{i+j}=\bar m_{ij}u_iu_j$ is exactly the displayed congruence after taking logarithms to base $g$; that the map $n\mapsto v_n$ determines and is determined by $u_n$ is the definition. For the triangularity, an equation with $i+j=n$ involves only $v_n$ among the indices $\ge n$, and $v_i,v_j$ with $i,j<n$ — including $i=0$, where $v_0=0$ — so solving proceeds by increasing $n$, and at step $n$ each pair $(i,n-i)\notin S$ proposes a value for $v_n$; the system is consistent exactly when all proposals agree. $\square$

Proposition 5 is not a negative result: it converts the classification into a finite linear problem, and it also shows when the problem disappears.

**Theorem 6 (the support classifies the reductions for $p=2$).** *Let $p=2$. Then every nonzero reduced structure constant equals $1$, and the reductions of two forms are isomorphic if and only if their supports coincide. Hence for $p=2$ the mod-$2$ Hopf algebra is determined by the valuations — by their positivity pattern, which is all that $v_2$ records about vanishing.*

*Proof.* $\FF_2^\times=\{1\}$, so $\bar m_{ij}=1$ whenever $(i,j)\notin S$ and no rescaling is needed or possible: the reduced structure constants are already $0$ or $1$. Proposition 1 gives that the support is an invariant and Proposition 4 that forms with the same support have equal reduced constants, hence isomorphic reductions. $\square$

**Theorem 7 (the residual is genuine, and its shape).** *For $p>2$ and a support $S$ for which the system of Proposition 5 is inconsistent, two forms with support $S$ have non-isomorphic reductions; such a pair exists exactly when the system is inconsistent for some admissible $S$. Whether inconsistency can occur is **not settled here**.*

*Proof.* The first sentence is the definition of inconsistency. The second is a restatement; the third is the open point, and no counterexample is asserted.

What is known about the third point: whenever the two pairs $(i,t)$ and $(t,n-j)$ arising in the consistency check of Proposition 5 both lie outside $S$, consistency follows from the integral cocycle $m_{it}m_{j,n-j}=m_{t,n-j}m_{i,n-i}$ (with $t=j-i$), by Proposition 5's comparison — this is the computation carried out for the $p$-unit case in Proposition 2 and it does not use $p$. So an obstruction can only arise from a support which is "thick" in the sense that it contains those auxiliary pairs, and the smallest place to look is $p=3$, where $\FF_3^\times$ has order $2$ and the coefficient $2$ of a free $v_n$ vanishes mod $2$.

Where such an obstruction would have to come from is visible in the integral cocycle. In the case $(i,t)\in S$ the identity $m_{it}m_{j,n-j}=m_{t,n-j}m_{i,n-i}$ forces $e_{it}=e_{t,n-j}\ge1$ and, after dividing both singular factors by that common power of $p$, leaves the relation $\overline{M_{it}}\,\bar m_{j,n-j}=\overline{M_{t,n-j}}\,\bar m_{i,n-i}$ among *units*. The unit parts $M_{it}$ of the singular structure constants are invisible to the valuations, so two forms with the same support may impose different relations on the residues off the support. That is the mechanism by which the support could fail to determine the reduction for odd $p$; this card does not exhibit such a pair, and the search carried out here — all forms with $m_{1j}\le24$ for $j\le6$ — found no two forms of equal support with non-isomorphic reductions.

**Status of the exercise's second question, stated without overclaiming.** The reductions are classified by the orbits of Proposition 1, and by Theorem 6 the answer is complete for $p=2$ and for the family $m_{ij}=p^{e_{ij}}$: there the support alone decides. For odd $p$ and a general form the answer is the consistency question of Proposition 5, which is open. In particular the earlier claim that the valuations determine $A\otimes\ZZ_p$ is **not refuted** — it is proved for $p=2$ (Theorem 6) and open for odd $p$ — and the intermediate claim that the residues "can fail to be normalisable" is **not proved**: no counterexample is known to this card.

What the valuations do produce is a family of integral forms together with their vanishing patterns, by a converse that is a direct application of the criterion above: given integers $e_{ij}$ satisfying the two bounds and the cocycle relation, and $e_{i0}=e_{0i}=0$, put
$$
m_{ij}=p^{e_{ij}}
$$
and valuation $0$ at all other primes. The divisor and cocycle conditions hold by construction, so the recipe above gives an integral form, and its reduction has $\overline{m_{ij}}=0$ exactly when $e_{ij}>0$.

When $d$ is even, the polynomial and divided-power reductions are the two extreme valuation choices $e_{ij}=0$ and
$$
e_{ij}=v_p\binom{i+j}{i},
$$
while intermediate divisor cocycles give the mixed integral forms.
:::
