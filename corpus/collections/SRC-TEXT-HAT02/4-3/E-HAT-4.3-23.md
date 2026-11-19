---
schema: qual/card@1
id: E-HAT-4.3-23
kind: problem
title: "Uniqueness of Quillen plus construction"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Read against Hatcher, Algebraic Topology (2002), §4.3 Exercise 23, printed p. 420,
    and Corollary 4.73, printed p. 417. The obstruction argument is right, but the card
    described the mapping cylinder wrongly: it said the deformation retraction r: W -> Y
    restricts to "the identity on X", while on X subset W it restricts to i, since X
    meets Y only in i(X); and it then wrote the pair as (Y, X), which needs X subset Y.
    Repaired to (Y, i(X)) at both places, which is the pair the retraction really
    collapses onto and the pair whose exact sequence has i_* in it. An independent report
    from the swarm flagged the same sentence. Statement unchanged. Not checked: the
    rest of the card beyond the two sentences and the extension step.
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 4.3, Exercise 23; the stored statement matches.
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
    Restructured as a Lamport proof of the argument already on the card, which follows the
    exercise's hint and is correct. Added: the identification (W,X) ~ (Y,X) as pairs, which is
    what makes H_*(W,X) vanish and which the card compressed into 'since i is a homology
    isomorphism'; the universal coefficient sequence written out, so that both the Ext and the
    Hom term are seen to vanish; the coefficient group named in Corollary 4.73 as pi_n(Y') with
    the hypothesis 'abelian' entering exactly as the triviality of the local system; the
    explicit construction of f as the composite of the extension with a homotopy inverse of the
    retraction, and the homotopy fi ~ i' spelled out; and the algebraic identity f_* =
    i'_*(i_*)^-1 that makes f a homology isomorphism. No statement was changed. Not claimed: a
    retained solution set; the collection's provenance is the Hatcher textbook, whose text is
    not retained here, so Corollary 4.73 and Proposition 4.74 are cited by number as the card
    cites them.

---

::: {.problem}
Prove the following uniqueness result for the Quillen plus construction: Given a connected CW complex $X$, if there is an abelian CW complex $Y$ and a map $X \to Y$ inducing an isomorphism $H_*(X; \ZZ) \approx H_*(Y; \ZZ)$, then such a $Y$ is unique up to homotopy equivalence. [Use Corollary 4.73 with $W$ the mapping cylinder of $X \to Y$.]
:::

::: {.solution}
Throughout $X$ is a connected CW complex, $Y$ and $Y'$ are connected abelian CW complexes — connected CW complexes on which $\pi_{1}$ acts trivially on every homotopy group — and $i\colon X \to Y$, $i'\colon X \to Y'$ induce isomorphisms on integral homology. $W \coloneqq M_{i}$ is the mapping cylinder of $i$, with $X \subseteq W$ and $Y \subseteq W$; the deformation retraction $r\colon W \to Y$ restricts on $X$ to $i$, not to the identity, since $X$ meets $Y$ only in $i(X)$, so the pair it collapses onto is $(Y,i(X))$ and a map out of $(W,X)$ is the same thing as a map out of $(Y,i(X))$. The exercise is Hatcher, *Algebraic Topology*, §4.3 Exercise 23.

::: pf

::: {.pf-step #cylinder}
$W \simeq Y$ and $H_{n}(W, X; \ZZ) = 0$ for every $n$.

::: pf-proof
The mapping cylinder contains $Y$ as its top and deformation retracts onto it through maps that fix $X$, so $W \simeq Y$ and even $(W, X) \simeq (Y, i(X))$. The exact sequence of the pair $(Y, i(X))$ is $\cdots \to H_{n}(X) \xrightarrow{i_{*}} H_{n}(Y) \to H_{n}(Y,i(X)) \to H_{n-1}(X) \to \cdots$, and $i_{*}$ is an isomorphism in every degree, so each group $H_{n}(Y,i(X))$ is squeezed between two isomorphisms and vanishes. Since $(W,X) \simeq (Y,i(X))$, $H_{n}(W,X) = 0$ for all $n$.

:::

:::

::: {.pf-step #cohomology}
$H^{n+1}(W, X; A) = 0$ for every abelian group $A$ and every $n$.

::: pf-proof
The universal coefficient theorem expresses $H^{n+1}(W,X;A)$ in the short exact sequence $0 \to \operatorname{Ext}\bigl(H_{n}(W,X), A\bigr) \to H^{n+1}(W,X;A) \to \Hom\bigl(H_{n+1}(W,X), A\bigr) \to 0$. Both abelian groups fed into it vanish by step [](#cylinder){.pf-ref}, so $\operatorname{Ext}$ and $\Hom$ of the zero group vanish and the middle term is $0$.

:::

:::

::: {.pf-step #obstruction}
The map $i'\colon X \to Y'$ extends over $W$: there is $F\colon W \to Y'$ with $F$ restricting to $i'$ on $X$.

::: pf-proof
This is the obstruction-theoretic extension theorem, Corollary 4.73 of the book, for the CW pair $(W, X)$ and the abelian CW complex $Y'$: the obstructions to extending a map on $X$ over the cells of $W$ lie in the groups $H^{n+1}(W,X; \pi_{n}(Y'))$, with constant coefficients because $Y'$ is abelian, and every one of those groups vanishes by step [](#cohomology){.pf-ref} with $A = \pi_{n}(Y')$. Hence no obstruction remains and the extension exists.

:::

:::

::: {.pf-step #f}
There is $f\colon Y \to Y'$ with $f i \simeq i'$.

::: pf-proof
Take $F$ from step [](#obstruction){.pf-ref} and compose with the homotopy inverse $s\colon Y \to W$ of the deformation retraction: $f \coloneqq F s$. Then $f i = F s i \simeq F i = i'$, because $s i \simeq \operatorname{incl}_{X}$ and $F$ restricts to $i'$ on $X$.

:::

:::

::: {.pf-step #homology-iso}
$f$ induces an isomorphism on integral homology.

::: pf-proof
$f_{*} i_{*} = (fi)_{*} = i'_{*}$ because $fi \simeq i'$, and both $i_{*}$ and $i'_{*}$ are isomorphisms; hence $f_{*} = i'_{*}(i_{*})^{-1}$ is an isomorphism in every degree.

:::

:::

::: pf-step
$f\colon Y \to Y'$ is a homotopy equivalence, and the abelian target of the plus construction is unique up to homotopy equivalence.

::: pf-proof
Step [](#homology-iso){.pf-ref} gives a map between connected CW complexes inducing isomorphisms on all integral homology groups. The homology Whitehead theorem in the form of Proposition 4.74 of the book applies because both spaces are abelian CW complexes — that hypothesis is what upgrades a homology isomorphism to a homotopy equivalence for spaces with possibly nontrivial fundamental group. So $f$ is a homotopy equivalence, and any two abelian CW complexes receiving a homology isomorphism from $X$ are homotopy equivalent.

:::

:::

:::
:::
