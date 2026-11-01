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

**What is still open, stated exactly.** For a general form the residues $\bar m_{ij}\in\FF_p^\times$ off $S$ need not be normalisable to $1$: the constraints $u_{i+j}=\bar m_{ij}u_iu_j$, imposed only for $(i,j)\notin S$, form a graph on $\NN$, and a rescaling exists if and only if the product of the $\bar m$'s around every cycle of that graph is $1$. Deciding the orbit set for a fixed support is therefore a $1$-cocycle computation on that graph; it is not carried out here, and in particular the claim that the valuations alone classify the reductions remains false: the support is determined by the valuations, and the finer orbits are not.

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
