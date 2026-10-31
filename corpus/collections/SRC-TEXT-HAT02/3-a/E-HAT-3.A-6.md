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
    proofs/cards/TorTorsion.lean certifies the group-theoretic core: `ratchet_le` ($m\le k$),
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
    Exercise 4 of the same section. proofs/cards/TorReductions.lean formalizes the parts of (3),
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
    group. proofs/cards/TorReductions.lean certifies the pieces that are formalizable:
    `map_torKernel_mulByInt` (the kernel of $(n\cdot\mathrm{id})\otimes\mathrm{id}_B$ inside
    $\ZZ\otimes B$ is carried onto $B[n]$ by $\ZZ\otimes B\cong B$, that is
    $\operatorname{Tor}(\ZZ/n,B)\cong B[n]$ for this resolution),
    `torsionBy_pow_eq_bot_of_no_p_torsion` (no $p$-torsion gives $C[p^k]=0$), and
    `mem_of_p_smul_mem_of_pPrimary` ($B_p$ is saturated for multiplication by $p$, which is what
    "$B/B_p$ has no $p$-torsion" means). Additivity and the direct-limit step are cited, not
    formalized, and proofs/README.md lists that as an outstanding obligation rather than claiming
    the reduction is complete.
---

::: {.problem}
Show that $\operatorname{Tor}(A, B)$ is always a torsion group, and that $\operatorname{Tor}(A, B)$ contains an element of order $n$ iff both $A$ and $B$ contain elements of order $n$.
:::

::: {.solution}
First show that $\operatorname{Tor}(A,B)$ is torsion. Express $A$ as the directed union of its finitely generated subgroups $A_\alpha$. By Exercise 4,
$$
\operatorname{Tor}(A,B)
\cong\varinjlim_\alpha\operatorname{Tor}(A_\alpha,B).
$$
For each finitely generated $A_\alpha$, write
$$
A_\alpha\cong\ZZ^r\oplus\bigoplus_{j=1}^s\ZZ_{n_j}.
$$
Then
$$
\operatorname{Tor}(A_\alpha,B)
\cong\bigoplus_{j=1}^s B[n_j],
$$
which is a torsion group. Every element of the direct limit comes from one such torsion group, so it has finite order. Hence $\operatorname{Tor}(A,B)$ is torsion.

Now suppose $A$ and $B$ each contain an element of order exactly $n$. Let
$$
C\cong\ZZ_n
$$
be the cyclic subgroup of $A$ generated by such an element. From
$$
0\to C\to A\to A/C\to0
$$
the long exact Tor sequence begins
$$
\operatorname{Tor}_2(A/C,B)
\longrightarrow \operatorname{Tor}_1(C,B)
\longrightarrow \operatorname{Tor}_1(A,B).
$$
Over $\ZZ$, every abelian group has projective dimension at most $1$, so $\operatorname{Tor}_2=0$. Hence
$$
\operatorname{Tor}(C,B)\hookrightarrow\operatorname{Tor}(A,B).
$$
But
$$
\operatorname{Tor}(\ZZ_n,B)\cong B[n].
$$
Since $B$ contains an element of order exactly $n$, $B[n]$ contains an element of order $n$. Its image in $\operatorname{Tor}(A,B)$ still has order $n$, proving one direction.

Conversely, suppose $\operatorname{Tor}(A,B)$ has an element of order $n$, and write $n=\prod_p p^{m_p}$. Three rules of Proposition 3A.5 pass from the mixed groups to their primary parts. Rule (4) gives $\operatorname{Tor}(A,B)\cong\operatorname{Tor}(T(A),B)$, so the torsion subgroup, not the free part, carries all of $\operatorname{Tor}$. Rule (2) gives $\operatorname{Tor}(T(A),B)\cong\bigoplus_p\operatorname{Tor}(A_p,B)$ over the direct sum $T(A)=\bigoplus_pA_p$. Finally, rule (6) applied to $0\to B_p\to B\to B/B_p\to0$ gives an exact sequence whose last Tor term $\operatorname{Tor}(A_p,B/B_p)$ vanishes: $B/B_p$ has no $p$-torsion, and rule (5) gives $\operatorname{Tor}(\ZZ_{p^k},B/B_p)\cong (B/B_p)[p^k]=0$ for each $k$, so by rule (2) the same holds for every $p$-primary $A_p$, finite direct sums of cyclic ones first and then, by Exercise 4, for the group itself. Note that $B/B_p$ is *not* torsionfree in general — for $p=2$ and $B=\ZZ/2\oplus\ZZ/3$ the quotient is $\ZZ/3$ — so rule (3) does not apply here; the hypothesis in play is the absence of $p$-torsion. Hence $\operatorname{Tor}(A_p,B)\cong\operatorname{Tor}(A_p,B_p)$. Combining them,
$$
\operatorname{Tor}(A,B)\cong\bigoplus_p\operatorname{Tor}(A_p,B_p),
$$
so the given element has a component of order exactly $p^{m_p}$ in $\operatorname{Tor}(A_p,B_p)$ for each prime $p$ dividing $n$.

Fix such a $p$ and write $A_p$ as the directed union of its finitely generated subgroups $A_{p,\alpha}$, each of the form $\bigoplus_j\ZZ_{p^{k_j}}$. By Exercise 4 of the same section the component of the class already lies in some
$$
\operatorname{Tor}(A_{p,\alpha},B_p)\cong\bigoplus_j B_p[p^{k_j}],
$$
using rule (2) for the direct sum and rule (5) for each cyclic summand. Here the argument must use the coordinate and nothing more. Write the class as $x=(x_j)$ and let $x_j$ be a coordinate killed by $p^{k_j}$ on which $p^{m_p-1}x$ does not vanish, so that $x_j$ is killed by $p^{m_p}$ but not by $p^{m_p-1}$; such a coordinate exists because $x$ has order exactly $p^{m_p}$. Then $p^{m_p}\mid p^{k_j}$, so $k_j\ge m_p$, and $x_j$ is itself an element of $B$ of order $p^{m_p}$. The coordinate $x_j$ gives no element of order $p^{k_j}$ in $B$ — with $A=\ZZ/8$ and $B=\ZZ/2$ the coordinate lies in $B[8]$ and has order $2$ — so the element of order $p^{m_p}$ in $B$ is $x_j$ itself. On the other side $A_{p,\alpha}$ has an element of order $p^{k_j}$ in its $j$th summand, and multiplying it by $p^{k_j-m_p}$ gives an element of $A$ of order $p^{m_p}$. Summing the resulting elements over the primes dividing $n$ gives elements of order $n$ in $A$ and in $B$.
:::
