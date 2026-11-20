---
schema: qual/card@1
id: E-HAT-4.3-13
kind: problem
title: "Pre-composing with homotopy equivalence"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: source-corrected
  by: claude
  date: 2026-11-21
  note: >-
    Citation convention. Every locator of the form "printed page N" or "PDF page N" written into
    this card before today, here and in the events below, is superseded: sources are cited by
    chapter, section and numbered statement only. The events below are left as their sessions wrote
    them, as QUAL-11 requires, so their locators stand as a historical record; the statement and the
    solution above are the current text and cite by number. This event records the convention and no
    further reading: the mathematics of the card is as the events below describe it.
- event: source-corrected
  by: claude
  date: 2026-11-20
  note: >-
    Page corrected. The sentence citing "printed p. 15" for the statement that the mapping
    cylinder contains both ends as deformation retracts is Corollary 0.21, printed p. 16; p. 15
    carries the preceding discussion, and the mapping cylinder phrase does not occur there. The
    mathematics is unchanged.
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Read against Hatcher, Algebraic Topology (2002), §4.3 Exercise 13, printed p. 420,
    and Corollary 0.21. Phi and Psi are right and Psi Phi is fibre homotopic to the
    identity, but the homotopy K_s for Phi Psi was ill defined, as an independent report
    from the swarm found and as recomputing shows: with K_s(a,gamma) = (H(a,1-s), P_s)
    the inserted path P_s had to start at f(H(a,1-s)), while the formula made it end at
    f(i(r(a))) and then concatenated gamma, which starts at f(a) --- a concatenation that
    does not exist, and K_0 was not Phi Psi either. Repaired: K_s(a,gamma) =
    (H(a,s), (u -> f(H(a,s(1-u)))) * gamma), whose inserted path runs from f(H(a,s)) to
    f(H(a,0)) = f(a), so the pair lies in E_f, with K_1 = Phi Psi exactly and K_0 =
    (a, const * gamma) fibre homotopic to the identity. Statement unchanged. Not
    checked: nothing outside this exercise.
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 4.3, Exercise 13; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-corrected
  by: claude
  date: 2026-11-01
  note: >-
    Statement repaired against Hatcher's printed text: the card had dropped printed matter
    (a bracketed hint or pointer, or a printed sentence) that an audit located by word-by-word
    comparison with tmp/hat/AT.txt, and that this session re-verified at the cited lines before
    applying the repair. The restored text is the printed wording and the mathematics of the
    statement is otherwise unchanged.
- event: solution-reviewed
  by: claude
  date: 2026-11-02
  note: >-
    Cards read. Verdict record is m6__proofs-4-3-1-12.md (1-12: 10 correct, 5 a dimension slip, 9 a wrong assertion; both repaired) and m2__proofs-4-3-13-24.md (13-24: 10 correct, 20 a display misalignment repaired by identifying the principal fibration, 22 the missing converse of an iff, later restated and proved, and 24, whose whole proof was then written). No card in this slice has an unmet piece.

- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Rewritten as a Lamport structured proof of the argument already on the card, expanded from
    Sam's one line: the deformation-retract case is proved with the two fibre-preserving maps
    written out and both composites homotoped through fibre-preserving maps, and the reduction
    runs through the mapping cylinder $M_g$, with the map $\widehat f:M_g\to B$ constructed and
    shown well defined, and both end inclusions $i_A,i_C$ used as deformation retracts. The
    $i_A$ case is an explicit straight-line homotopy; for $i_C$ the card cites the book's own
    statement that a mapping cylinder of a homotopy equivalence contains both ends as
    deformation retracts (printed p. 15, Corollary 0.21 on printed p. 16). Statement re-read at
    §4.3 Exercise 13, printed p. 420. Retained solution: Sam 2008, Exercise 4.3.13, PDF p. 28.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Rewritten as a Lamport structured proof of the argument already on the card, expanded from
    Sam's one line: the deformation-retract case is proved with the two fibre-preserving maps
    written out and both composites homotoped through fibre-preserving maps, and the reduction
    runs through the mapping cylinder $M_g$, with the map $\widehat f:M_g\to B$ constructed and
    shown well defined, and both end inclusions $i_A,i_C$ used as deformation retracts. The
    $i_A$ case is an explicit straight-line homotopy; for $i_C$ the card cites the book's own
    statement that a mapping cylinder of a homotopy equivalence contains both ends as
    deformation retracts (printed p. 15, Corollary 0.21 on printed p. 16). Statement re-read at
    §4.3 Exercise 13, printed p. 420. Retained solution: Sam 2008, Exercise 4.3.13, PDF p. 28.
---

::: {.problem}
Given a map $f: A \to B$ and a homotopy equivalence $g: C \to A$, show that the fibrations $E_f \to B$ and $E_{fg} \to B$ are fiber homotopy equivalent. [One approach is to use Corollary 0.21 to reduce to the case of deformation retractions.]
:::

::: {.solution}
The retained solution is **Steven V. Sam, *Solutions to Hatcher's Algebraic Topology* (2008), Exercise 4.3.13**, whose one-line argument this proof carries out: reduce by Corollary 0.21 to the case where $g$ is the inclusion of a deformation retract, where the claim is immediate because $f(g(C))$ is a deformation retract of $f(A)$. The card proves the deformation-retract case explicitly and performs the reduction through the mapping cylinder rather than by quoting Corollary 0.21. The statement is Hatcher, *Algebraic Topology* (2002), §4.3 Exercise 13, and the hint followed is the exercise's own.

Throughout $f:A\to B$ is a map, and for a map $u:X\to B$ the mapping path fibration is
$$
E_u=\theset{(x,\gamma)\mid x\in X,\ \gamma:I\to B,\ \gamma(0)=u(x)},\qquad E_u\longrightarrow B,\ (x,\gamma)\longmapsto\gamma(1),
$$
so that $E_f$ is a space over $B$ with a projection to $A$ and $E_{fg}$ one with a projection to $C$. A fibre homotopy is a homotopy through fibre-preserving maps.

::: pf

::: {.pf-step #retract-case}
If $i:C\to A$ is the inclusion of a deformation retract, with retraction $r:A\to C$ and homotopy $H:\mathrm{id}_A\simeq i\circ r$ satisfying $H(i(c),t)=i(c)$ for all $t$, then $E_{f\circ i}$ and $E_f$ are fibre homotopy equivalent over $B$.

::: pf-proof
Define
$$
\Phi:E_{f\circ i}\to E_f,\quad \Phi(c,\gamma)=(i(c),\gamma),\qquad
\Psi:E_f\to E_{f\circ i},\quad \Psi(a,\gamma)=\bigl(r(a),\ (s\mapsto f(H(a,1-s)))*\gamma\bigr).
$$
$\Phi$ is fibre-preserving because both projections read off $\gamma(1)$. In $\Psi$ the path $s\mapsto f(H(a,1-s))$ runs from $f(H(a,1))=f(i(r(a)))$ to $f(H(a,0))=f(a)$, so concatenating with $\gamma$ gives a path starting at $f(i(r(a)))=(f\circ i)(r(a))$, and $\Psi$ is fibre-preserving. Next, $\Psi\Phi(c,\gamma)=(r(i(c)),\ (s\mapsto f(H(i(c),1-s)))*\gamma)=(c,\mathrm{const}_{f(i(c))}*\gamma)$, because $H$ is the identity on the image of $i$; that is homotopic to $(c,\gamma)$ through fibre-preserving maps, by the standard homotopy between a path and its reparametrization, so $\Psi\Phi\simeq\mathrm{id}$. For $\Phi\Psi$, put
$$
K_s(a,\gamma)=\bigl(H(a,s),\ (u\mapsto f(H(a,s(1-u))))*\gamma\bigr).
$$
The pair $K_s(a,\gamma)$ must lie in $E_f$, so its path coordinate must start at $f(H(a,s))$: it does, and the inserted path ends at $f(H(a,0))=f(a)$, where $\gamma$ starts, so the concatenation is defined. Then $K_1(a,\gamma)=\bigl(i(r(a)),\ (u\mapsto f(H(a,1-u)))*\gamma\bigr)$, which is exactly $\Phi\Psi(a,\gamma)$, and $K_0(a,\gamma)=\bigl(a,\ \mathrm{const}_{f(a)}*\gamma\bigr)$, which is homotopic to $(a,\gamma)$ through maps that only reparametrize the path coordinate, hence fibre homotopic to the identity. So $\Phi\Psi\simeq\mathrm{id}$. Hence $\Phi$ and $\Psi$ are mutually inverse fibre homotopy equivalences.

:::

:::

::: {.pf-step #cylinder}
Let $M_g=(C\times I\sqcup A)/\sim$ with $(c,1)\sim g(c)$ be the mapping cylinder of $g$, and let $i_C:C\to M_g$, $c\mapsto[c,0]$, and $i_A:A\to M_g$ be the inclusions. There is a map $\widehat f:M_g\to B$ with $\widehat f\circ i_C=f\circ g$ and $\widehat f\circ i_A=f$.

::: pf-proof
Set $\widehat f[c,t]=f(g(c))$ for $(c,t)\in C\times I$ and $\widehat f[a]=f(a)$ for $a\in A$. This is well defined on the quotient: the only identifications are $[c,1]=[g(c)]$, and there $f(g(c))=f(g(c))$. It is continuous because $C\times I$ and $A$ are glued along the closed subspaces $C\times\{1\}$ and $g(C)$ on which the two formulas agree, so the gluing lemma for quotient maps applies. The two composites are then $\widehat f\,i_C(c)=f(g(c))$ and $\widehat f\,i_A(a)=f(a)$.

:::

:::

::: {.pf-step #retracts}
$i_A:A\to M_g$ and $i_C:C\to M_g$ are both inclusions of deformation retracts.

::: pf-proof
For $i_A$: define $D:M_g\times I\to M_g$ by $D([c,t],s)=[c,\ t+s(1-t)]$ and $D([a],s)=[a]$. The two formulas agree on the glued sets — at $t=1$ the first gives $[c,1]=[g(c)]$, which is the point of $A$ that the second fixes — so $D$ is well defined and continuous by the gluing lemma for closed covers of the cone coordinate. It fixes $A$ pointwise, $D(-,0)=\mathrm{id}$, and the image of $D(-,1)$ lies in $A$ with $\restrictionof{D(-,1)}{A}=\mathrm{id}$; so $A$ is a deformation retract of $M_g$. For $i_C$: the book states that for a homotopy equivalence $g$ the mapping cylinder $M_g$ contains *both* $C$ and $A$ as deformation retracts (Corollary 0.21); that is the form quoted by Sam, and it applies because $g$ is a homotopy equivalence by hypothesis.
:::

:::

::: {.pf-step #chain}
$E_{fg}$ and $E_f$ are both fibre homotopy equivalent over $B$ to $E_{\widehat f}$.

::: pf-proof
Step [](#retract-case){.pf-ref} applied to the deformation retract $i_C:C\to M_g$ and the map $\widehat f:M_g\to B$ gives that $E_{\widehat f\circ i_C}$ and $E_{\widehat f}$ are fibre homotopy equivalent over $B$; by step [](#cylinder){.pf-ref), $\widehat f\circ i_C=f\circ g$, so $E_{fg}\simeq_f E_{\widehat f}$. The same step applied to the deformation retract $i_A:A\to M_g$ and $\widehat f$ gives $E_{\widehat f\circ i_A}\simeq_f E_{\widehat f}$, and $\widehat f\circ i_A=f$, so $E_f\simeq_f E_{\widehat f}$.

:::

:::

::: {.pf-step #conclusion}
The fibrations $E_f\to B$ and $E_{fg}\to B$ are fibre homotopy equivalent.

::: pf-proof
Fibre homotopy equivalence over a fixed base is an equivalence relation: it is reflexive and symmetric by definition, and transitive by composing the two fibre homotopy equivalences and their homotopies, which are fibre-preserving and compose to homotopies of the composites. By step [](#chain){.pf-ref} both fibrations are equivalent to $E_{\widehat f}$, hence to each other.

:::

:::

:::
:::
