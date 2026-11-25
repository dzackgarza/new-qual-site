---
schema: qual/card@1
id: E-HAT-3.F-9
kind: problem
title: "Spliced exact sequences for $p$-primary components"
classification:
  areas:
  - topology
  topics:
  - Cohomology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.F, Exercise 9; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-11-01
  note: >-
    Statement compared with Hatcher, Algebraic Topology, Sec. 3.F, AT.txt:16022, which prints
    "(a) Ext(A, Z) is divisible iff A is torsionfree." The card previously read "is divisible if A is
    torsionfree": the only-if half was dropped and unproved, and the earlier source-checked note
    claiming that the stored statement matched was false. Both are repaired: the iff is restored and
    the missing direction is proved from the card's own spliced sequence, since surjectivity of
    multiplication by p forces Ext(_p A, Z) = 0, which is impossible for a nonzero Z/p-vector space.
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against Hatcher, Algebraic Topology (2002), §3.F Exercise 9, printed page
    320, whose (a) reads "Ext(A, Z) is divisible if A is torsionfree" — one
    implication. The earlier correction on this card had replaced it by an "if and
    only if"; the printed implication is restored here, since a card's statement
    follows the printed exercise. The splicing argument and both directions of the
    printed (b), including the converse under Hom(A,Z) = 0, were checked: exactness at
    Ext(A,Z) reads divisibility as surjectivity and torsionfreeness as injectivity of
    multiplication by p, and Ext(A_p,Z) ≅ Hom(A_p,Q/Z) from Exercise 5 detects
    A_p = 0. What this note does not do: it does not certify the converse of (a),
    which the printed exercise does not ask for.
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    The 2026-11-06 note on this card is wrong about the source and reversed a correct
    repair. Hatcher, Algebraic Topology (2002), §3.F Exercise 9(a), printed p. 321,
    reads "Ext(A, Z) is divisible iff A is torsionfree", read from the PDF page itself
    and not from the extracted text alone. The iff is therefore restored in the
    statement, and its converse proved in step #s2. That step was also defective as
    written: it showed Ext(V,Z) nonzero only for finite-dimensional V, while _pA can be
    infinite dimensional. Replaced by a direct-summand argument: a nonzero element of
    _pA spans a Z_p summand, so Ext(_pA,Z) has the nonzero summand Ext(Z_p,Z) = Z_p.
    The splicing, the identification of the composite with multiplication by p, and
    (b) with its converse were rechecked and are correct. Not checked: nothing outside
    this exercise.

- event: solution-reviewed
  by: claude
  date: 2026-11-22
  note: >-
    Read against Hatcher, §3.F Exercise 9, whose printed display was checked on a 220 dpi render of
    the page: the row $\operatorname{Hom}(pA,\ZZ)\to\operatorname{Ext}(A_p,\ZZ)\to
    \operatorname{Ext}(A,\ZZ)\to^p\operatorname{Ext}(A,\ZZ)\to\operatorname{Ext}({}_pA,\ZZ)\to0$
    is printed with $\operatorname{Ext}(pA,\ZZ)$ drawn beneath it, joined to the two copies of
    $\operatorname{Ext}(A,\ZZ)$, and with the arrow labelled $p$. The statement matches. The proof of
    (a) and (b) is correct: $\operatorname{Hom}$ and $\operatorname{Ext}$ of ${}_pA$ and $A_p$ into
    $\ZZ$ vanish, the two six-term sequences splice, and the composite through
    $\operatorname{Ext}(pA,\ZZ)$ is multiplication by $p$; torsionfreeness of $A$ makes ${}_pA=0$ and
    so makes $p$ onto, a nonzero ${}_pA$ contains a $\ZZ_p$ direct summand whose $\operatorname{Ext}$
    is nonzero, divisibility makes $A_p=0$ and so makes $p$ injective, and the converse uses
    Exercise 5 to turn $\operatorname{Ext}(A_p,\ZZ)=0$ into $A_p=0$. One addition: the step that
    abbreviates the middle term away now says why it may — the map
    $\operatorname{Ext}(A,\ZZ)\to\operatorname{Ext}(pA,\ZZ)$ is onto because the first sequence ends
    there, so the kernel and image of the composite are those of that map. The citation of the
    printed page is removed and the retained sets' state recorded.
- event: solution-reviewed
  by: claude
  date: 2026-11-22
  note: >-
    Correction to the preceding event. Its added sentence reversed the contravariant composition and
    credited surjectivity to the wrong map: the two maps of the composite are
    $\operatorname{Ext}(i)\colon\operatorname{Ext}(A,\ZZ)\to\operatorname{Ext}(pA,\ZZ)$ for the
    inclusion $i\colon pA\to A$ and
    $\operatorname{Ext}(q)\colon\operatorname{Ext}(pA,\ZZ)\to\operatorname{Ext}(A,\ZZ)$ for
    multiplication $q\colon A\to pA$. The second six-term sequence ends with $\operatorname{Ext}(i)$
    and makes it onto; the first begins with $\operatorname{Ext}(q)$ and makes it injective. The
    passage now names both maps and both sequences, writes the composite as
    $\operatorname{Ext}(q)\circ\operatorname{Ext}(i)=\operatorname{Ext}(i\circ q)$, and reads the
    kernel of the composite off exactness of the second sequence at $\operatorname{Ext}(A,\ZZ)$ and
    its image off exactness of the first sequence there.
---

::: {.problem}
For an abelian group $A$ let $p: A \to A$ be multiplication by $p$, and let ${}_pA = \ker p$, $pA = \operatorname{im} p$, and $A_p = \operatorname{coker} p$ as in the proof of Proposition 3F.12. Show that the six-term exact sequences involving $\operatorname{Hom}(-, \ZZ)$ and $\operatorname{Ext}(-, \ZZ)$ associated to the short exact sequences $0 \to {}_pA \to A \to pA \to 0$ and $0 \to pA \to A \to A_p \to 0$ can be spliced together to yield an exact sequence

$$\operatorname{Hom}(pA, \ZZ) \to \operatorname{Ext}(A_p, \ZZ) \to \operatorname{Ext}(A, \ZZ) \xrightarrow{p} \operatorname{Ext}(A, \ZZ) \to \operatorname{Ext}({}_pA, \ZZ) \to 0$$

where the map labeled "$p$" is multiplication by $p$.
Use this to show:

(a) $\operatorname{Ext}(A, \ZZ)$ is divisible if and only if $A$ is torsionfree.

(b) $\operatorname{Ext}(A, \ZZ)$ is torsionfree if $A$ is divisible, and the converse holds if $\operatorname{Hom}(A, \ZZ) = 0$.
:::

::: {.solution}
The statement is Hatcher, §3.F Exercise 9, and the argument is the card's own: no retained solution set holds a solution of any exercise of §3.F — Koukpari's set carries the §3.F heading *Limits and Ext* with nothing under it, Sam's begins at §4.1, and the others stop earlier.

Consider the two short exact sequences
$$
0\to{}_pA\to A\xrightarrow{p}pA\to0,
\qquad
0\to pA\to A\to A_p\to0.
$$
Since ${}_pA$ and $A_p$ are killed by $p$, every homomorphism from either group to the torsionfree group $\ZZ$ is zero.

Applying $\operatorname{Hom}(-,\ZZ)$ and $\operatorname{Ext}(-,\ZZ)$ to the first sequence gives the tail
$$
0\to\operatorname{Ext}(pA,\ZZ)
\to\operatorname{Ext}(A,\ZZ)
\to\operatorname{Ext}({}_pA,\ZZ)\to0.
$$
Applying them to the second gives
$$
0\to\operatorname{Hom}(A,\ZZ)\to\operatorname{Hom}(pA,\ZZ)
\to\operatorname{Ext}(A_p,\ZZ)
\to\operatorname{Ext}(A,\ZZ)
\to\operatorname{Ext}(pA,\ZZ)\to0.
$$
Splicing at $\operatorname{Ext}(pA,\ZZ)$ yields
$$
\operatorname{Hom}(pA,\ZZ)\to\operatorname{Ext}(A_p,\ZZ)\to
\operatorname{Ext}(A,\ZZ)\to\operatorname{Ext}(A,\ZZ)\to
\operatorname{Ext}({}_pA,\ZZ)\to0.
$$
Write $q\colon A\to pA$ for multiplication by $p$, which is onto $pA$, and $i\colon pA\to A$ for the inclusion, so that $i\circ q$ is multiplication by $p$ on $A$. Since Ext is contravariant, $q$ induces $\operatorname{Ext}(q)\colon\operatorname{Ext}(pA,\ZZ)\to\operatorname{Ext}(A,\ZZ)$ and $i$ induces $\operatorname{Ext}(i)\colon\operatorname{Ext}(A,\ZZ)\to\operatorname{Ext}(pA,\ZZ)$, so the composite of the two middle maps is $\operatorname{Ext}(q)\circ\operatorname{Ext}(i)=\operatorname{Ext}(i\circ q)$, which is multiplication by $p$ on $\operatorname{Ext}(A,\ZZ)$. The second sequence ends $\operatorname{Ext}(A,\ZZ)\xrightarrow{\operatorname{Ext}(i)}\operatorname{Ext}(pA,\ZZ)\to0$, so $\operatorname{Ext}(i)$ is onto, and the first begins $0\to\operatorname{Ext}(pA,\ZZ)\xrightarrow{\operatorname{Ext}(q)}\operatorname{Ext}(A,\ZZ)$, so $\operatorname{Ext}(q)$ is injective. Hence the kernel of the composite is $\ker\operatorname{Ext}(i)$, which is the image of $\operatorname{Ext}(A_p,\ZZ)\to\operatorname{Ext}(A,\ZZ)$ by exactness of the second sequence at $\operatorname{Ext}(A,\ZZ)$, and its image is $\operatorname{im}\operatorname{Ext}(q)$, which is the kernel of $\operatorname{Ext}(A,\ZZ)\to\operatorname{Ext}({}_pA,\ZZ)$ by exactness of the first sequence at $\operatorname{Ext}(A,\ZZ)$. Those are the two subgroups that exactness of the printed row requires at its two copies of $\operatorname{Ext}(A,\ZZ)$, so the middle term $\operatorname{Ext}(pA,\ZZ)$ may be abbreviated away, as the printed statement does. Hence the spliced sequence is precisely
$$
\boxed{
\operatorname{Hom}(pA,\ZZ)\to\operatorname{Ext}(A_p,\ZZ)\to
\operatorname{Ext}(A,\ZZ)\xrightarrow{p}
\operatorname{Ext}(A,\ZZ)\to
\operatorname{Ext}({}_pA,\ZZ)\to0.}
$$

::: pf

::: {.pf-step #s1}

If $A$ is torsionfree, then $\operatorname{Ext}(A,\ZZ)$ is divisible.

::: pf-proof

Torsionfreeness gives ${}_pA=0$. Exactness at the second copy of $\operatorname{Ext}(A,\ZZ)$ says multiplication by $p$ is surjective for every prime $p$. Therefore multiplication by every positive integer is surjective, so $\operatorname{Ext}(A,\ZZ)$ is divisible.

:::

:::

::: {.pf-step #s2}

Conversely, if $\operatorname{Ext}(A,\ZZ)$ is divisible then $A$ is torsionfree.

::: pf-proof

Suppose ${}_pA\ne0$ for some prime $p$; then ${}_pA$ is a nonzero vector space over $\ZZ_p$, since $p\,{}_pA=0$.

Divisibility makes multiplication by $p$ surjective on $\operatorname{Ext}(A,\ZZ)$, so in the spliced sequence $\operatorname{Ext}(A,\ZZ)\xrightarrow{p}\operatorname{Ext}(A,\ZZ)\to\operatorname{Ext}({}_pA,\ZZ)\to0$ the map into $\operatorname{Ext}({}_pA,\ZZ)$ is zero, whence $\operatorname{Ext}({}_pA,\ZZ)=0$.

But $\operatorname{Ext}({}_pA,\ZZ)\ne0$: a nonzero element of ${}_pA$ spans a subgroup isomorphic to $\ZZ_p$ that is a direct summand of ${}_pA$ over $\ZZ_p$, so ${}_pA\cong\ZZ_p\oplus W$ and $\operatorname{Ext}(-,\ZZ)$, additive on direct sums, gives $\operatorname{Ext}({}_pA,\ZZ)\cong\operatorname{Ext}(\ZZ_p,\ZZ)\oplus\operatorname{Ext}(W,\ZZ)$; and $\operatorname{Ext}(\ZZ_p,\ZZ)\cong\ZZ_p$ is nonzero, computed from the resolution $0\to\ZZ\xrightarrow{p}\ZZ\to\ZZ_p\to0$. This contradicts $\operatorname{Ext}({}_pA,\ZZ)=0$, so ${}_pA=0$ for every prime $p$, that is, $A$ is torsionfree.

:::

:::

::: {.pf-step #s3}

If $A$ is divisible, then $\operatorname{Ext}(A,\ZZ)$ is torsionfree.

::: pf-proof

Divisibility gives $A_p=0$ for every prime $p$. Exactness at the first copy of $\operatorname{Ext}(A,\ZZ)$ then says multiplication by $p$ has zero kernel. Thus the Ext group has no $p$-torsion for any prime $p$, hence is torsionfree.

:::

:::

::: {.pf-step #s4}

Conversely, if $\operatorname{Hom}(A,\ZZ)=0$ and $\operatorname{Ext}(A,\ZZ)$ is torsionfree, then $A$ is divisible.

::: pf-proof

Precomposition with the surjection $A\xrightarrow p pA$ injects
$$
\operatorname{Hom}(pA,\ZZ)\hookrightarrow\operatorname{Hom}(A,\ZZ)=0,
$$
so $\operatorname{Hom}(pA,\ZZ)=0$. The spliced exact sequence therefore identifies
$$
\operatorname{Ext}(A_p,\ZZ)
$$
with the kernel of multiplication by $p$ on $\operatorname{Ext}(A,\ZZ)$. This kernel is zero by torsionfreeness.

But $A_p$ is a vector space over $\ZZ_p$, and if it were nonzero it would admit a nonzero homomorphism to the subgroup $\ZZ_p\subset\QQ/\ZZ$. Using
$$
\operatorname{Ext}(A_p,\ZZ)
\cong\operatorname{Hom}(A_p,\QQ/\ZZ)
$$
from Exercise 5 (since $\operatorname{Hom}(A_p,\QQ)=0$), this would contradict $\operatorname{Ext}(A_p,\ZZ)=0$. Hence $A_p=0$, i.e. $pA=A$, for every prime $p$. Therefore $A$ is divisible.

:::

:::

:::

:::
