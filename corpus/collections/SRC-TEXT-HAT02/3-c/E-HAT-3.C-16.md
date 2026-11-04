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
- event: solution-reviewed
  by: claude
  date: 2026-11-01
  note: >-
    Second correction to the reduction analysis, and the exercise text itself is now read: Hatcher
    printed p.292 (PDF page 301) reads "Classify algebraically the Hopf algebras A over Z such that A_n
    is free for each n and A (x) Q ~ Q[alpha]. In particular, determine which Hopf algebras A (x) Z_p
    arise from such A's." The earlier note's Theorem 6 -- that for p = 2 the support classifies the
    reductions because F_2^x = {1} -- was false, and it is replaced. The mistake was to justify
    reducing the isomorphism condition to product constants: an isomorphism must satisfy both
    m'_ij u_i u_j = m_ij u_{i+j} and c'_ij u_{i+j} = c_ij u_i u_j, and these are equivalent only where
    the constants are non-zero. Where m vanishes the product equation is vacuous while the coproduct
    equation is not, and c_ij = b_ij/m_ij is zero or non-zero according to the exact valuation, not
    merely its vanishing. Verified concretely: with d even and m_ij = p^{f_ij}, f_ij = v_p(binomial) =
    s_p(i)+s_p(j)-s_p(i+j) is a valuation cocycle (checked for i,j,k <= 6), b_13 = 4, and forms
    differing only in v_2(m_13) in {1,2} have the same support but coproduct constants 0 and 1, so they
    are non-isomorphic. What the card now asserts: Theorem 6, the two-operation criterion, with the
    three consequences (equivalence only off the zero constants; the support is insufficient; the
    reduction depends on the valuation vector through the two bits per pair); Theorem 7, that for a
    fixed pair of forms the question is the solvability of an explicit system over F_p, decidable.
    What remains open and is stated as open: whether the valuation vector is a complete invariant. The
    finite search on this card is labelled a bounded-degree check, not an all-degree classification.
- event: solution-written
  by: claude
  date: 2026-11-01
  note: >-
    The open question is settled. Theorem 8: if v_p(m_ij) = v_p(m'_ij) for all i,j then the reductions are
    isomorphic, with an explicit isomorphism phi(x_n) = omega_n y_n where omega_n is the unit part of
    q_n/q'_n; the proof checks both the multiplication and the comultiplication equations at every pair,
    splitting into the three cases e_ij = 0, 0 < e_ij = v_p(b_ij) and 0 < e_ij < v_p(b_ij), the last being
    vacuous on both sides. Theorem 9: conversely an isomorphism forces the two bits
    [v_p(m_ij) > 0] and [v_p(m_ij) = v_p(b_ij)] to agree, since the u_n are units and each equation is
    homogeneous. Corollary: the reductions are classified by those two bits per pair, i.e. by the flag
    (delta, epsilon); the valuation vector determines the reduction but is not injective on classes.
    Corroborated numerically on the pair (Gamma, p^{v_p(binomial)}) at p = 3, 5, 7, with u_n = omega_n
    satisfying every constraint; an earlier run of that check reported violations and the fault was the
    reciprocal convention in the script, not the theorem. Also removed from this card: the paragraph
    headed "A second, independent way the residues can matter", which asserted that the product system
    could be unsolvable -- false, by Theorem 8 -- and the earlier "open" status paragraph.
- event: solution-reviewed
  by: claude
  date: 2026-11-01
  note: >-
    Consolidated the reduction analysis into a single development and renumbered it, so that the
    historical notes above do not compete with what the card now says. The live statements are now:
    Lemma 1 (the two-operation criterion, both equations needed and why), Lemma 2 (which of the two
    equations bites, in the three cases e=0, 0<e=f, 0<e<f), Theorem 3 (the valuation vector determines
    the reduction), Theorem 4 (the reduction sees exactly the two bits), Corollary 5 (reductions are
    isomorphic iff the least degrees agree and the flags (delta, epsilon) agree). Four defects found
    while consolidating and fixed. (i) Corollary 5 was stated as an iff over ALL forms of Q[alpha], but
    the flag does not determine the least degree d: the polynomial forms with d=1 and with d=2 have
    identical flags on every pair and yet their reductions have different graded dimensions (B_1 = Z/2
    for d=1, B_1 = 0 for d=2). Proved, not sampled: for p=2 Kummer's formula gives
    v_2(C(n,k)) = s_2(k)+s_2(n-k)-s_2(n), and with i=2a+eps, j=2b+eta the two families
    C(i+j,i) and C(floor((i+j)/2), floor(i/2)) have the same 2-adic valuation in each of the three
    parity cases, while for i,j both odd the d=1 coefficient is 0 and C(i+j,i) is even, so both second
    bits are 0 there. Checked the valuation identity by machine for a,b<400 as well. The corollary, Theorem 3 and
    Theorem 4 now carry the hypothesis that the two forms share d, and a sentence states why that
    loses nothing. (ii) The card asserted the polynomial form has delta=epsilon=0 for all i,j. The
    second bit is [e_ij = f_ij] = [0 = v_p(b_ij)] = [p does not divide b_ij], which is NOT identically
    zero: for d even and p=2, b_12 = 3 so epsilon_12 = 1. Corrected, with that example recorded.
    (iii) The divided-power form was described as m_ij = b_ij without restricting d; for d odd, b_ij = 0
    whenever i and j are both odd, so m_ij = b_ij is not a positive integer and no such form exists.
    The item now says the divided-power form is the d even case only. (iv) Lemma 2(a) said both
    equations "reduce to" the same thing when e_ij = 0; that is right only when b_ij is a p-unit, since
    when b_ij = 0 mod p the coproduct equation is vacuous while the product equation is not. Both
    the lemma and its proof now say which of the two happens. Also checked and NOT changed: the
    three case computations of Theorem 3 (each verified by hand), the cocycle and divisor conditions
    of the classification of forms, the vanishing b_ij for i,j both odd when d is odd, and the
    non-isomorphism of the divided-power reduction to F_p[alpha] via x_1^p = p! x_p = 0. Not claimed
    and said so on the card: no realisation theorem for every flag pattern, and no decision
    procedure -- Corollary 5 is a criterion, and the underlying equation system is infinite.
    Not checked: no independent source beyond Hatcher p.292 (PDF page 301), which was read again.
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

Now fix a prime $p$, put $B=A\otimes\FF_p$, and write $\bar x_n$ for the image of $x_n$; the $\bar x_n$ are an $\FF_p$-basis of $B$, one vector in each degree $nd$. The structure constants of $B$ are
$$
\bar x_i\bar x_j=\bar m_{ij}\,\bar x_{i+j},
\qquad
\Delta(\bar x_n)=\sum_{i+j=n}\bar c_{ij}\,\bar x_i\otimes\bar x_j,
\qquad
\bar c_{ij}=\overline{\frac{b_{ij}}{m_{ij}}},
$$
where $\bar m_{ij}=m_{ij}\bmod p$ and $\bar c_{ij}$ is the reduction of the integer $c_{ij}=b_{ij}/m_{ij}$. Throughout, $e_{ij}:=v_p(m_{ij})$ and $f_{ij}:=v_p(b_{ij})$, with $v_p(0)=\infty$; the divisibility $m_{ij}\mid b_{ij}$ gives $e_{ij}\le f_{ij}$ always, and $b_{ij}=0$ (which happens only when $d$ is odd and $i,j$ are both odd) gives $f_{ij}=\infty$ and no condition.

Two forms are only compared when they share their least degree $d$, hence their $b_{ij}$ and their $f_{ij}$. Nothing is lost: a form whose least degree is $d$ has $B=0$ in every degree that is not a multiple of $d$, so reductions of forms with different $d$ are already non-isomorphic as graded vector spaces. The hypothesis is not vacuous bookkeeping. The two polynomial forms with $d=1$ and $d=2$ have *identical* flags, and their reductions are not isomorphic. Their flags agree: both have $\delta\equiv0$, and for $p=2$ the second bit is $[\,v_2(b_{ij})=0\,]$, where $b_{ij}=\binom{i+j}{i}$ for $d=2$ and $b_{ij}=0$ for $i,j$ both odd and $\binom{\lfloor (i+j)/2\rfloor}{\lfloor i/2\rfloor}$ otherwise for $d=1$; Kummer's formula gives $v_2\binom{n}{k}=s_2(k)+s_2(n-k)-s_2(n)$, and writing $i=2a+\epsilon$, $j=2b+\eta$ it gives the same value $s_2(a)+s_2(b)-s_2(a+b)$ for both families in each of the three parity cases, while for $i,j$ both odd the $d=1$ coefficient vanishes and $\binom{i+j}{i}$ is even. Yet $B_1=\ZZ/2$ for $d=1$ and $B_1=0$ for $d=2$.

**Lemma 1 (the two-operation criterion).** *A graded linear map $\phi(\bar x_n)=u_n\bar y_n$ with $u_n\in\FF_p^\times$ between two such reductions is an isomorphism of Hopf algebras if and only if, for all $i,j$,*
$$
\bar m'_{ij}\,u_iu_j=\bar m_{ij}\,u_{i+j}
\qquad\text{and}\qquad
\bar c'_{ij}\,u_{i+j}=\bar c_{ij}\,u_iu_j .
$$
*Proof.* The first equation is $\phi(x_ix_j)=\phi(x_i)\phi(x_j)$ and the second is $(\phi\otimes\phi)\Delta=\Delta\phi$; a map of graded Hopf algebras preserves the unit, the counit, the product and the coproduct, and a graded linear map carrying basis vector to basis vector does this exactly when both families of structure constants agree after transport. Both equations are needed: where $\bar m_{ij}=0$ the first is vacuous while the second need not be. $\square$

**Lemma 2 (which of the two equations bites).** *Assume $e_{ij}=e'_{ij}$ for all $i,j$, so that $\bar m_{ij}=0\iff\bar m'_{ij}=0$ and $\bar c_{ij}=0\iff\bar c'_{ij}=0$.*
*(a) If $e_{ij}=0$ both equations are satisfied by $u_{i+j}=(\bar m'_{ij}/\bar m_{ij})u_iu_j$; where $\bar b_{ij}\ne0$ the second is equivalent to the first, and where $\bar b_{ij}=0$ the second is vacuous and only the first bites.*
*(b) If $0<e_{ij}=f_{ij}$ then $\bar m_{ij}=\bar m'_{ij}=0$ and the second equation reduces to $u_{i+j}=(\bar c_{ij}/\bar c'_{ij})u_iu_j$, both coproduct constants being non-zero.*
*(c) If $0<e_{ij}<f_{ij}$ then $\bar m_{ij}=\bar m'_{ij}=0$ and $\bar c_{ij}=\bar c'_{ij}=0$, so both equations are vacuous.*

*Proof.* In (a), $m_{ij}$ and $m'_{ij}$ are $p$-units so the coproduct constants are $\bar b_{ij}/\bar m_{ij}$ and $\bar b_{ij}/\bar m'_{ij}$ with the same $\bar b_{ij}$ — both forms are forms of the same $\QQ[\alpha]$ with the same $b_{ij}$ — and the two equations are then equivalent when $\bar b_{ij}\ne0$ (dividing by $\bar b_{ij}$) and the second is vacuous when $\bar b_{ij}=0$. In (b), $c_{ij}=b_{ij}/m_{ij}$ has $v_p(c_{ij})=f_{ij}-e_{ij}=0$, so $\bar c_{ij}\ne0$ and likewise $\bar c'_{ij}\ne0$, while both product constants vanish. In (c), $f_{ij}>e_{ij}>0$ gives $v_p(c_{ij})>0$ and the same for $c'_{ij}$. Finally $e_{ij}\le f_{ij}$ always, so these are the only cases. $\square$

**Theorem 3 (the valuation vector determines the reduction).** *Let $A,A'$ be forms with the same least degree $d$. If $v_p(m_{ij})=v_p(m'_{ij})$ for all $i,j$ then $B\cong B'$ as graded Hopf algebras.*

*Proof.* Write $q_n=p^{\tau_n}\sigma_n$ and $q'_n=p^{\tau'_n}\sigma'_n$ with $\sigma_n,\sigma'_n\in\ZZ_p^\times$, the exponents possibly negative, and set
$$
\omega_n:=\frac{\sigma_n}{\sigma'_n}\bmod p\ \in\FF_p^\times,
\qquad\text{so that}\qquad
\mu_{ij}:=\frac{m_{ij}}{p^{e_{ij}}}=\frac{\sigma_i\sigma_j}{\sigma_{i+j}},\quad
\mu'_{ij}=\frac{\sigma'_i\sigma'_j}{\sigma'_{i+j}} .
$$
Take $u_n=\omega_n$ in Lemma 1 and go through Lemma 2's cases.

*Case (a), $e_{ij}=0$.* Then
$$
\bar m'_{ij}\omega_i\omega_j=\frac{\sigma'_i\sigma'_j}{\sigma'_{i+j}}\cdot\frac{\sigma_i\sigma_j}{\sigma'_i\sigma'_j}=\frac{\sigma_i\sigma_j}{\sigma'_{i+j}}
=\frac{\sigma_i\sigma_j}{\sigma_{i+j}}\cdot\frac{\sigma_{i+j}}{\sigma'_{i+j}}=\bar m_{ij}\omega_{i+j}.
$$
*Case (b), $0<e_{ij}=f_{ij}$.* Put $\beta_{ij}=b_{ij}/p^{f_{ij}}\bmod p\ne0$, so $\bar c_{ij}=\beta_{ij}/\mu_{ij}$ and $\bar c'_{ij}=\beta_{ij}/\mu'_{ij}$. Then
$$
\bar c'_{ij}\omega_{i+j}=\frac{\beta_{ij}\sigma'_{i+j}}{\sigma'_i\sigma'_j}\cdot\frac{\sigma_{i+j}}{\sigma'_{i+j}}=\frac{\beta_{ij}\sigma_{i+j}}{\sigma'_i\sigma'_j}
=\frac{\beta_{ij}\sigma_{i+j}}{\sigma_i\sigma_j}\cdot\frac{\sigma_i\sigma_j}{\sigma'_i\sigma'_j}=\bar c_{ij}\omega_i\omega_j .
$$
*Case (c)* is vacuous on both sides. Hence the single choice $u_n=\omega_n$ satisfies every constraint, and $\phi$ preserves multiplication and comultiplication. $\square$

**Theorem 4 (what the reduction sees).** *Let $A,A'$ be forms with the same least degree $d$. If $B\cong B'$ as graded Hopf algebras then for every pair $i,j$,*
$$
[\,v_p(m_{ij})>0\,]=[\,v_p(m'_{ij})>0\,]
\qquad\text{and}\qquad
[\,v_p(m_{ij})=v_p(b_{ij})\,]=[\,v_p(m'_{ij})=v_p(b_{ij})\,].
$$

*Proof.* In any isomorphism the $u_n$ are units, so in Lemma 1's first equation $\bar m_{ij}=0\iff\bar m'_{ij}=0$, giving the first equality; and in the second $\bar c_{ij}=0\iff\bar c'_{ij}=0$, which by $e_{ij}\le f_{ij}$ and $v_p(c_{ij})=f_{ij}-e_{ij}$ is the second. $\square$

Define the **flag** of a form to be the pair of bits
$$
\delta_{ij}(A)=[\,e_{ij}>0\,],
\qquad
\varepsilon_{ij}(A)=[\,e_{ij}=f_{ij}\,],
\qquad i,j\ge1 .
$$

**Corollary 5 (the classification).** *For forms $A,A'$ of $\QQ[\alpha]$ with least degrees $d,d'$: there is an isomorphism of graded Hopf algebras $A\otimes\FF_p\cong A'\otimes\FF_p$ if and only if $d=d'$, $\delta(A)=\delta(A')$ and $\varepsilon(A)=\varepsilon(A')$.*

*Proof.* If the reductions are isomorphic as graded vector spaces then $d=d'$, since $d$ is the least positive degree in which $B$ is nonzero; and given that, the flags agree by Theorem 4. Conversely, if $d=d'$ and the flags agree, then at every pair the trichotomy of Lemma 2 falls in the same case for both forms, and the computation of Theorem 3 — which uses only the case, not the size of $e_{ij}$ — supplies an isomorphism. $\square$

**Which flag patterns are classified, and what realises them.** The corollary classifies reductions by flags, so the answer to the exercise's second question is: *the Hopf algebras $A\otimes\ZZ_p$ arising are one isomorphism class for each flag pattern that is realised by an integral form, and no claim is made that every pattern is realised.* Three families are realised explicitly.

1. *The polynomial form*, $m_{ij}=1$ for all $i,j$: here $e_{ij}=0$, so $\delta_{ij}=0$ for every $i,j$, while $\varepsilon_{ij}=[\,0=f_{ij}\,]=[\,p\nmid b_{ij}\,]$ is **not** identically zero — for $d$ even and $p=2$ one has $b_{12}=3$, so $\varepsilon_{12}=1$. The reduction is $B=\FF_p[\bar x_1]$, a polynomial algebra on the generator $\bar x_1$, since $\bar x_i\bar x_j=\bar x_{i+j}$.

2. *The divided-power form*, which exists when $d$ is even: $m_{ij}=b_{ij}=\binom{i+j}{i}>0$, so $e_{ij}=f_{ij}$ and $\varepsilon_{ij}=1$ for all $i,j$, while $\delta_{ij}=[\,p\mid\binom{i+j}{i}\,]$. (For $d$ odd there is no such form: $b_{ij}=0$ whenever $i,j$ are both odd, and $m_{ij}$ must be a positive integer.) This is not isomorphic to $\FF_p[\alpha]$: here $\bar x_1^{\,p}=p!\,\bar x_p=0$ while $\bar x_p\ne0$, whereas in $\FF_p[\alpha]$ the $p$-th power map is injective.

3. *The whole family $m_{ij}=p^{e_{ij}}$*, for any non-negative integers $e_{ij}$ with $e_{ij}\le f_{ij}$ satisfying the valuation cocycle $e_{ij}+e_{i+j,k}=e_{jk}+e_{i,j+k}$ and $e_{i0}=e_{0i}=0$: these are admissible integral data, by the divisor and cocycle conditions of the classification of forms, and they realise exactly the patterns $\delta_{ij}=[e_{ij}>0]$, $\varepsilon_{ij}=[e_{ij}=f_{ij}]$ that arise from such a valuation cocycle. Item 1 is the member $e\equiv0$ of this family; item 2 is *not* a member, since its $m_{ij}=\binom{i+j}{i}$ need not be a power of $p$.

**What is not claimed.** Three things, stated so that no later reader takes them from this card. First, no claim that *every* flag pattern is realised: what is proved is that a realised pattern determines the class, and that the patterns in item 3 are realised; characterising the realisable patterns among all pairs of bits is left open. Some patterns are certainly not realisable — at a pair with $p\nmid b_{ij}$ one has $f_{ij}=0$, so $e_{ij}\le f_{ij}$ forces $e_{ij}=0$ and hence the flag $(0,1)$ at that pair, and at a pair with $b_{ij}=0$ one has $f_{ij}=\infty$ and hence $\varepsilon_{ij}=0$; but no full characterisation is given. Second, no decision procedure is claimed for comparing two reductions: Corollary 5 gives a *condition* — equality of flags — and the flags form an infinite family of bits, which is not an algorithm. Third, reductions are compared only between forms with the same least degree $d$; across different $d$ nothing is claimed beyond the observation recorded before Lemma 1, that the graded dimensions already differ. The parity hypothesis is kept as the book's: for $d$ even all $b_{ij}=\binom{i+j}{i}$ are non-zero, while for $d$ odd the pairs with $i,j$ both odd have $b_{ij}=0$, hence $f_{ij}=\infty$, hence $\varepsilon_{ij}=0$ there for every form, so those pairs contribute only $\delta_{ij}$ to the flag.


:::
