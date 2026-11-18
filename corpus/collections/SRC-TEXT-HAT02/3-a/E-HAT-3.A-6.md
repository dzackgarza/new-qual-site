---
schema: qual/card@1
id: E-HAT-3.A-6
kind: problem
title: "Tor is always a torsion group"
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
  note: Checked against Hatcher, Algebraic Topology, Section 3.A, Exercise 6; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.A, Exercise 6; it matches the printed text. The card stated only the "if" half of the printed "iff"; the other half is restored.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read the first half: writing $A$ as a direct limit of finitely generated pieces reduces
    $\operatorname{Tor}$ to $\bigoplus_jB[n_j]$, which is torsion; and the injection of a cyclic
    subgroup $C=\ZZ_n\subset A$ embeds $\operatorname{Tor}(C,B)=B[n]$ in $\operatorname{Tor}(A,B)$.
    The converse that the restored statement needs is added here: the class splits over the primary
    decomposition, and a finitely generated $p$-primary stage
    $A_{p,\alpha}=\bigoplus_j\ZZ_{p^{k_j}}$ has
    $\operatorname{Tor}(A_{p,\alpha},B_p)=\bigoplus_jB_p[p^{k_j}]$, which forces elements of order
    $p^{m_p}$ in both $A$ and $B$.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Correction to the converse added in the earlier review, and its certificate. The first version
    concluded that a coordinate of order $p^{m_p}$ in $B_p[p^{k_j}]$ gives an element of order
    $p^{k_j}$ in $B$; that inference is false, as $A=\ZZ/8$, $B=\ZZ/2$, $n=2$ shows, where the
    coordinate lies in $B[8]$ and has order $2$. The step now reads only $p^{m_p}\mid p^{k_j}$,
    hence $k_j\ge m_p$, and takes $x_j$ itself as the element of $B$ of order $p^{m_p}$; the
    element of order $p^{m_p}$ in $A$ is the $p^{k_j-m_p}$-th multiple of the generator of the
    $j$th summand. The reduction to the primary parts is now justified for mixed groups:
    $\operatorname{Tor}(A,B)\cong\operatorname{Tor}(T(A),B)$ because $A/T(A)$ is torsion-free hence
    flat, $\operatorname{Tor}$ commutes with direct sums, and
    $\operatorname{Tor}(A_p,B)\cong\operatorname{Tor}(A_p,B_p)$ because $B/B_p$ has no $p$-torsion.
    <https://github.com/dzackgarza/new-qual-site/blob/16c09abaa4/proofs/cards/TorTorsion.lean> certifies the group-theoretic core: `ratchet_le` ($m\le k$),
    `exact_order_smul`, `exists_coord`, the refutation `zmod_two_no_exact_order_eight`, and
    `zmod_eight_order_four`; the Tor-theoretic reductions themselves are cited, not formalized.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    The reductions in the converse are now citations of the section's own Proposition 3A.5, checked
    against the printed statement: (4) gives
    $\operatorname{Tor}(A,B)\cong\operatorname{Tor}(T(A),B)$, (2) gives the split over the primary
    components, (6) applied to $0\to B_p\to B\to B/B_p\to0$ with (3) gives
    $\operatorname{Tor}(A_p,B)\cong\operatorname{Tor}(A_p,B_p)$, and (2) with (5) gives
    $\operatorname{Tor}(\ZZ_{p^{k_j}},B_p)\cong B_p[p^{k_j}]$; commutation with the direct limit is
    Exercise 4 of the same section. <https://github.com/dzackgarza/new-qual-site/blob/16c09abaa4/proofs/cards/TorReductions.lean> formalizes the parts of (3),
    (5) and (6) that are statements about torsion, flatness and tensor products, reusing Mathlib's
    torsion-free-is-flat instance and its flatness form of tensor exactness; the comparison theorem
    (Lemma 3A.2), additivity (2), the torsion reduction (4) and the direct-limit statement are
    cited, and the file records that Mathlib's `CategoryTheory.Tor` has no long exact sequence or
    comparison API to reuse.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Correction of the previous review's step, which invoked rule (3) of Proposition 3A.5 on the
    false premise that $B/B_p$ is torsion-free: it is not, since with $p=2$ and
    $B=\ZZ/2\oplus\ZZ/3$ the quotient is $\ZZ/3$. The step now uses rule (5), which gives
    $\operatorname{Tor}(\ZZ_{p^k},B/B_p)\cong(B/B_p)[p^k]=0$ because $B/B_p$ has no $p$-torsion,
    with rule (2) for finite direct sums and Exercise 4 for the passage to an arbitrary $p$-primary
    group. <https://github.com/dzackgarza/new-qual-site/blob/16c09abaa4/proofs/cards/TorReductions.lean> certifies the pieces that are formalizable:
    `map_torKernel_mulByInt` (the kernel of $(n\cdot\mathrm{id})\otimes\mathrm{id}_B$ inside
    $\ZZ\otimes B$ is carried onto $B[n]$ by $\ZZ\otimes B\cong B$, that is
    $\operatorname{Tor}(\ZZ/n,B)\cong B[n]$ for this resolution),
    `torsionBy_pow_eq_bot_of_no_p_torsion` (no $p$-torsion gives $C[p^k]=0$), and
    `mem_of_p_smul_mem_of_pPrimary` ($B_p$ is saturated for multiplication by $p$, which is what
    "$B/B_p$ has no $p$-torsion" means). Additivity and the direct-limit step are cited, not
    formalized, and proofs/README.md lists that as an outstanding obligation rather than claiming
    the reduction is complete.
- event: solution-reviewed
  by: claude
  date: 2026-11-01
  note: >-
    Formalization-corpus lookup before further authorship, and a port that follows from it. The
    corpus was searched through its live API (OpenAPI 1.1.0) under several formulations (Tor,
    torFunctor, leftDerived tensor, torsion product, Tor of cyclic module, derived tensor torsion,
    `file:Tor.lean`, `content:"torOneIsoKernel"`, `content:"Tor' C"`); the earlier `403` was a client
    user-agent artefact and not an access denial, so no coverage was lost. Result: the first claim's
    torsion case is already formalized, and by a different route. `TauCeti.isAddTorsion_Tor_left`
    (TauCetiProject/TauCeti at commit 67e852853c5192ec69775bb7ef417fc199e4190e, Apache-2.0,
    `TauCeti/AlgebraicTopology/SerreClass/TensorTor.lean`) proves that `Tor_n(M,N)` is torsion
    whenever `M` is, for arbitrary `N` and over any commutative ring, via `ObjectProperty.prop_leftDerived_obj`
    (a class closed under subobjects and quotients is closed under left derived functors whose
    projective values lie in it). <https://github.com/dzackgarza/new-qual-site/blob/16c09abaa4/proofs/cards/TorTorsionClass.lean> ports that argument and its
    three dependencies and compiles on the canonical baseline with no `sorryAx`, axioms only
    `propext`, `Classical.choice`, `Quot.sound`. What this does **not** do, stated so it is not read
    as the card: the card says `Tor(A,B)` is torsion for all `A`, and the file proves the case where
    `A` is torsion. The remaining reduction `Tor_n(A,B) ≅ Tor_n(T(A),B)` needs flat ⇒ Tor-acyclic and
    the long exact sequence of Tor, both of which exist upstream as TauCeti's `isZero_Tor_succ_of_flat`
    and `isZero_Tor_X₂`/`isZero_Tor_succ_X₃` and neither of which is in the pinned Mathlib; that is a
    port, not research, and proofs/README.md §7b records it as the next step. The converse half of the
    card is untouched by this event and no located formalization proves it. The finite-stage witness
    demanded for the presentation-level route is not supplied here and is not needed for this case,
    because `Tor` is defined as a left derived functor and `ProjectiveResolution.isoLeftDerivedObj`
    already removes the choice of resolution.
- event: solution-reviewed
  by: claude
  date: 2026-11-01
  note: >-
    Correction to the previous event's framing, which treated a port as a step toward a card
    obligation. It is neither. The repository's criterion is `certify-card-corrections`: a
    *corrected* claim is settled only with a certificate of that claim. The claims corrected on this
    card were the restored printed `iff` and the replacement of the false `B/B_p` torsion-free premise
    by the absence of `p`-torsion; those are settled by the source text and by
    <https://github.com/dzackgarza/new-qual-site/blob/16c09abaa4/proofs/cards/TorReductions.lean> (`torsionBy_pow_eq_bot_of_no_p_torsion`,
    `mem_of_p_smul_mem_of_pPrimary`, `map_torKernel_mulByInt`), with the converse's group-theoretic
    core in <https://github.com/dzackgarza/new-qual-site/blob/16c09abaa4/proofs/cards/TorTorsion.lean>. That "$\operatorname{Tor}(A,B)$ is a torsion group" was
    *not* a corrected claim, so no node requires a local formalization of it, and
    <https://github.com/dzackgarza/new-qual-site/blob/16c09abaa4/proofs/cards/TorTorsionClass.lean> is recorded in proofs/README.md §1 and §7c as a supplement
    with no obligation attached rather than as progress on one. The card's requirement — a correct,
    sourced solution — is met by citation, and the citation is
    `TauCeti.isAddTorsion_Tor_left` at
    https://github.com/TauCetiProject/TauCeti/blob/67e852853c5192ec69775bb7ef417fc199e4190e/TauCeti/AlgebraicTopology/SerreClass/TensorTor.lean
    (Apache-2.0), statement verbatim: for `{R} [CommRing R] {M N : ModuleCat R}`,
    `IsAddTorsion M → (n : ℕ) → IsAddTorsion (((Tor (ModuleCat R) n).obj M).obj N)`, proved via
    `ObjectProperty.prop_leftDerived_obj` and the subobject/quotient closure of the torsion class.
    What that citation covers, stated exactly: it gives the case in which the first variable is
    already torsion, over any commutative ring. It does **not** give this card as printed, which
    quantifies over all `A`; the passage from `A` to its torsion subgroup is not covered by it and is
    not claimed here. The alternative route the card writes out — finitely generated stages,
    $\operatorname{Tor}(A_\alpha,B)\cong\bigoplus_j B[n_j]$, then the direct limit — is Hatcher's own
    and remains the card's displayed proof; the citation is corroboration, not a replacement of it.
- event: source-corrected
  by: claude
  date: 2026-11-07
  note: >-
    Statement restored to the printed text of p.267, which reads "contains an element of order $n$
    if both $A$ and $B$ contain elements of order $n$" — the stored card had widened it to "iff"
    without saying so. The converse is true and is kept, now explicitly labelled as the direction the
    print does not ask for. The rambling passage that carried the converse was rewritten: the
    vanishing of $\operatorname{Tor}(A_p,B/B_p)$ is now displayed inside the exact sequence of rule
    (6) where it is used, the false intermediate remark about coordinates was removed (the argument
    needs only that the order of a tuple is the largest coordinate order), and the statement that
    $B/B_p$ need not be torsionfree stays, since it is why rule (3) does not apply. The first
    direction and the torsion-group claim are unchanged.
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    The card's certificate, and where it is. Everything this page proves is proved for all abelian
    groups $A$ and $B$ at
    <https://github.com/dzackgarza/lean-categories/blob/5848f0f2f881ba032eb8bb69baa051300498ba6b/LeanCategories/Homological/TorExercise3A6.lean>:
    `isAddTorsion_torOne` is "$\operatorname{Tor}_1^\ZZ(A,B)$ is a torsion group for all $A$ and
    $B$", and `torOne_exists_addOrderOf_iff` is, for every positive $n$,
    "$\operatorname{Tor}_1^\ZZ(A,B)$ has an element of order $n$ if and only if both $A$ and $B$
    do" --- the direction the printed exercise asks for and the converse this card proves in
    addition. The route is the presentation bridge `torOneTorKernelAddEquiv`
    ($\operatorname{Tor}_1(A,B)\cong\ker((\ker\pi)\otimes B\to F\otimes B)$ for any surjection from
    a free $F$), the stage descent `exists_fg_stage`, Smith normal form
    (`exists_nsmul_eq_zero_of_stage`) and the purity of the syzygy's cyclic subgroup
    (`exists_torOne_of_addOrderOf`); it uses no filtered colimit, so the Exercise-4 step this page's
    first argument takes is not what the certificate rests on. Checked in this pass by reading that
    file at that commit rather than the row's description of it: every declaration named on the row
    and in this note is defined there, the file contains no `sorry` and no `axiom`, and the printed
    statement on the card is the direction that `iff` yields. Not checked in this pass: the file was
    not re-elaborated here, and the elaboration recorded for it --- Lean 4.36.0 at Mathlib
    `6d97e8ad`, axioms `propext`, `Classical.choice`, `Quot.sound`, no `sorryAx` --- is the one
    section 1's row records. The page's own direct-limit argument stays the displayed proof; the
    certificate settles the corrected claims without following it.
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    The finitely generated stage this page's first argument passes through has its own certificate
    on `lean-categories` main, and the declaration to cite is
    `LeanCategories.Homological.TorFiniteStage.isAddTorsion_torOne_of_finiteStage` in
    <https://github.com/dzackgarza/lean-categories/blob/9b7b06781f2aec8ab6d19790e03d7af8ddb96986/LeanCategories/Homological/TorFiniteStage.lean>:
    for a finitely generated abelian group $A$ and an arbitrary abelian group $B$,
    $\operatorname{Tor}_1^\ZZ(A,B)$ is a torsion group. It rests on `isAddTorsion_ker_stage` in the
    same file, the torsion statement at a finitely generated stage --- the kernel of
    $(R\sqcap F')\otimes B\to F\otimes B$ for finitely generated $F'\le F$ --- whose killing
    integer is the Smith-normal-form product of `TorExercise3A6.exists_nsmul_eq_zero_of_stage`, and
    on `exists_fin_free_presentation`, which gives a finitely generated $A$ a finite free
    presentation with finitely generated syzygy, the two-term resolution at which `Tor` is computed
    there. No filtered colimit is used: the passage to a stage that this page takes by Exercise 4 is
    certified by descent instead, and Exercise 4 itself remains uncertified at the pin. Axioms
    `propext`, `Classical.choice`, `Quot.sound`; no `sorryAx`;
    `lake build LeanCategories.Homological.TorFiniteStage` succeeds at that commit. Not claimed: the
    filtered-colimit statement, and nothing here alters the proof displayed above.
---

::: {.problem}
Show that $\operatorname{Tor}(A, B)$ is always a torsion group, and that $\operatorname{Tor}(A, B)$ contains an element of order $n$ if both $A$ and $B$ contain elements of order $n$.
:::

::: {.solution}

The two assertions of the exercise are proved first, and the converse of the second is added and proved as well, because the first part is otherwise easy to misread; the rule numbers are those of Proposition 3A.5.

Write $\operatorname{Tor}=\operatorname{Tor}_{1}^{\ZZ}$ and $B[n]=\{b\in B:nb=0\}$.

::: pf

::: {.pf-step #finitely-generated}
$\operatorname{Tor}(A,B)$ is a torsion group when $A$ is finitely generated.

::: pf-proof
Write $A\cong\ZZ^{r}\oplus\bigoplus_{j=1}^{s}\ZZ_{n_{j}}$, the classification of finitely generated abelian groups. Since $\operatorname{Tor}(\ZZ,B)=0$ and Tor is additive in the first variable over direct sums, $\operatorname{Tor}(A,B)\cong\bigoplus_{j=1}^{s}\operatorname{Tor}(\ZZ_{n_{j}},B)$, and the free part contributes nothing. The resolution $0\to\ZZ\xrightarrow{\ n\ }\ZZ\to\ZZ_{n}\to0$ tensored with $B$ gives $\operatorname{Tor}(\ZZ_{n},B)=\ker(B\xrightarrow{n}B)=B[n]$, all of whose elements have order dividing $n$. So $\operatorname{Tor}(A,B)\cong\bigoplus_{j}B[n_{j}]$ is a torsion group.
:::

:::

::: {.pf-step #direct-limit}
$\operatorname{Tor}(A,B)$ is a torsion group for every abelian group $A$.

::: pf-proof
$A$ is the directed union of its finitely generated subgroups $A_{\alpha}$, and Tor commutes with direct limits in the first variable (Exercise 4), so $\operatorname{Tor}(A,B)\cong\varinjlim_{\alpha}\operatorname{Tor}(A_{\alpha},B)$. An element of the direct limit is represented by an element of some $\operatorname{Tor}(A_{\alpha},B)$, which has finite order by step [](#finitely-generated){.pf-ref}, and its class in the colimit has the same finite order because the transition maps are group homomorphisms. Hence every element of $\operatorname{Tor}(A,B)$ has finite order.
:::

:::

::: {.pf-step #injection}
If $A$ contains an element of order exactly $n$ and $C\cong\ZZ_{n}$ is the cyclic subgroup it generates, then $\operatorname{Tor}(C,B)\to\operatorname{Tor}(A,B)$ is injective.

::: pf-proof
The short exact sequence $0\to C\to A\to A/C\to0$ gives the long exact Tor sequence
$$
\operatorname{Tor}_{2}(A/C,B)\to\operatorname{Tor}_{1}(C,B)\to\operatorname{Tor}_{1}(A,B)\to\cdots
$$
Over $\ZZ$ every abelian group has projective dimension at most $1$ — subgroups of free abelian groups are free, so a two-step free resolution exists — hence $\operatorname{Tor}_{2}(A/C,B)=0$ and the map $\operatorname{Tor}(C,B)\to\operatorname{Tor}(A,B)$ is injective.
:::

:::

::: {.pf-step #order-n}
If $A$ and $B$ both contain elements of order exactly $n$, then $\operatorname{Tor}(A,B)$ does.

::: pf-proof
With $C\cong\ZZ_{n}\subseteq A$ as in step [](#injection){.pf-ref}, $\operatorname{Tor}(C,B)\cong B[n]$, which contains the element of order $n$ that $B$ is assumed to have, and that element has order $n$ in $B[n]$ exactly when it has order $n$ in $B$ because its order divides $n$. By injectivity of step [](#injection){.pf-ref} its image in $\operatorname{Tor}(A,B)$ has order $n$.
:::

:::

::: {.pf-step #primary}
Conversely, $\operatorname{Tor}(A,B)\cong\bigoplus_{p}\operatorname{Tor}(A_{p},B_{p})$, where $A_{p}$ and $B_{p}$ are the $p$-primary parts of the torsion subgroups and $p$ runs over the primes.

::: pf-proof
Rule (4) of Proposition 3A.5 gives $\operatorname{Tor}(A,B)\cong\operatorname{Tor}(T(A),B)$ with $T(A)$ the torsion subgroup, so only $T(A)$ matters; rule (2) gives $\operatorname{Tor}(\bigoplus_{p}A_{p},B)\cong\bigoplus_{p}\operatorname{Tor}(A_{p},B)$ since Tor is additive in the first variable. For the second variable, apply rule (6) to $0\to B_{p}\to B\to B/B_{p}\to0$: it gives an exact sequence
$$
0\to\operatorname{Tor}(A_{p},B_{p})\to\operatorname{Tor}(A_{p},B)\to\operatorname{Tor}(A_{p},B/B_{p})\to A_{p}\otimes B_{p},
$$
and the third term vanishes. Indeed $B/B_{p}$ has no $p$-torsion, so rule (5) gives $\operatorname{Tor}(\ZZ_{p^{k}},B/B_{p})\cong(B/B_{p})[p^{k}]=0$ for every $k$; rule (2) and Exercise 4 extend this vanishing from finite direct sums of cyclic groups to an arbitrary $p$-primary $A_{p}$. Note that $B/B_{p}$ need not be torsionfree — for $p=2$ and $B=\ZZ/2\oplus\ZZ/3$ the quotient is $\ZZ/3$ — so rule (3) is not what applies here; the hypothesis really used is the absence of $p$-torsion. Hence $\operatorname{Tor}(A_{p},B)\cong\operatorname{Tor}(A_{p},B_{p})$ and the displayed decomposition holds.
:::

:::

::: {.pf-step #component}
Let $x\in\operatorname{Tor}(A,B)$ have order $n=\prod_{p}p^{m_{p}}$. Then for each $p\mid n$ the component $x_{p}$ of $x$ in $\operatorname{Tor}(A_{p},B_{p})$ has order exactly $p^{m_{p}}$, and $x_{p}$ lies in $\operatorname{Tor}(A_{p,\alpha},B_{p})$ for some finitely generated subgroup $A_{p,\alpha}=\bigoplus_{j}\ZZ_{p^{k_{j}}}$ of $A_{p}$, where it has a coordinate of order $p^{m_{p}}$.

::: pf-proof
In a direct sum the order of a tuple is the least common multiple of the orders of its coordinates, and $p^{m_{p}}$ is the exact power of $p$ in $n$, so the component $x_{p}$ has order exactly $p^{m_{p}}$. $A_{p}$ is the directed union of its finitely generated subgroups $A_{p,\alpha}$, each of the form $\bigoplus_{j}\ZZ_{p^{k_{j}}}$ since it is a finitely generated $p$-group; by Exercise 4 and step [](#primary){.pf-ref} the element $x_{p}$ is represented in some $\operatorname{Tor}(A_{p,\alpha},B_{p})\cong\bigoplus_{j}B_{p}[p^{k_{j}}]$, the isomorphism by rule (2) and rule (5). Since the order of the tuple is $p^{m_{p}}$ and equals the largest of the orders of its coordinates, some coordinate $x_{j}$ has order exactly $p^{m_{p}}$.
:::

:::

::: {.pf-step #converse}
If $\operatorname{Tor}(A,B)$ has an element of order $n$, then $A$ and $B$ each have an element of order $n$.

::: pf-proof
Let $n=\prod_{p\mid n}p^{m_{p}}$ and, for each such $p$, take $x_{p}$, $A_{p,\alpha}$ and a coordinate $x_{j}\in B_{p}[p^{k_{j}}]$ of order $p^{m_{p}}$ as in step [](#component){.pf-ref}. That $x_{j}$ is an element of $B$ of order $p^{m_{p}}$, and since $x_{j}\in B[p^{k_{j}}]$ one has $p^{m_{p}}\mid p^{k_{j}}$, that is $k_{j}\ge m_{p}$. On the other side $A_{p,\alpha}$ has a generator $g$ of order $p^{k_{j}}$ in its $j$-th summand, and $p^{k_{j}-m_{p}}g$ is an element of $A$ of order $p^{m_{p}}$. Summing the elements obtained for the various $p$ gives an element of $A$ of order $\prod_{p}p^{m_{p}}=n$, because the summands have pairwise coprime orders and the order of a sum of commuting elements of coprime orders is the product; summing the corresponding elements $x_{j}$ of $B$ gives an element of $B$ of order $n$ in the same way.
:::

:::

:::
:::
