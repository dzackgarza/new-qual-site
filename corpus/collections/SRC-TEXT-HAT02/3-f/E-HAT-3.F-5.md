---
schema: qual/card@1
id: E-HAT-3.F-5
kind: problem
title: "$\\operatorname{Ext}(A, \\ZZ)$ as a cokernel"
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
  note: Checked against Hatcher, Algebraic Topology, Section 3.F, Exercise 5; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against Hatcher, Algebraic Topology (2002), §3.F Exercise 5, printed page
    320; the statement matches word for word. Checked: applying Hom(A,−) and Ext(A,−)
    to 0 → Z → Q → Q/Z → 0 and using Ext(A,Q) = 0 (Exercise 3) identifies Ext(A,Z)
    with the cokernel of Hom(A,Q) → Hom(A,Q/Z); for A = Z_p^∞ the map is
    Hom(Z_p^∞,Q) = 0 → Hom(Z_p^∞,Q/Z) = Ẑ_p, giving Ext(Z_p^∞,Z) ≅ Ẑ_p, as computed
    by the other route on p. 317. No defect.
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Structured into Lamport steps from the card's own prose. Checked each input: the sequence
    0 -> Z -> Q -> Q/Z -> 0 is exact; Q is injective (Baer's criterion, using divisibility), so
    Ext(A,Q) = 0 and the long exact sequence ends with Ext(A,Z) as the cokernel of
    Hom(A,Q) -> Hom(A,Q/Z). For A = Z_{p^inf}: Hom(A,Q) = 0 because A is torsion and Q torsionfree;
    a homomorphism out of Z_{p^inf} has image of p-power order, so it lands in the p-primary
    subgroup of Q/Z, which is Z_{p^inf}, giving Hom = End; and an endomorphism is a compatible
    family of multipliers a_n mod p^n on the unique cyclic subgroup of order p^n, which is now
    proved in both directions (injective since a map out of the union is determined by its
    restrictions, surjective since compatibility makes the family well defined on the union).
    The card's prose asserted the last equivalence without the two directions. Statement
    unchanged; no retained solution set covers this exercise.
- event: solution-reviewed
  by: claude
  date: 2026-11-22
  note: >-
    Read again against Hatcher, §3.F Exercise 5. The proof is correct: $\QQ$ is injective, so
    $\operatorname{Ext}(A,\QQ)=0$ and the long exact sequence of $\operatorname{Hom}(A,-)$ makes
    $\operatorname{Ext}(A,\ZZ)$ the cokernel of $\operatorname{Hom}(A,\QQ)\to
    \operatorname{Hom}(A,\QQ/\ZZ)$; for $A=\ZZ_{p^\infty}$ the first term vanishes because $A$ is
    torsion and $\QQ$ torsionfree, a map out of $A$ has $p$-power order image and so lands in the
    $p$-primary part $\ZZ_{p^\infty}$ of $\QQ/\ZZ$, and an endomorphism is a compatible family of
    multipliers $a_n$ modulo $p^n$ on the cyclic subgroup of order $p^n$, giving
    $\varprojlim\ZZ/p^n=\widehat\ZZ_p$ in both directions. Two corrections, neither of mathematics:
    the preamble carried a printed page in its citation, now removed, and its "no retained solution
    set covers this exercise" is replaced by what the retained sets contain — Koukpari's §3.F
    heading with nothing under it, Sam beginning at §4.1, the others stopping earlier.
---

::: {.problem}
Show that $\operatorname{Ext}(A, \ZZ)$ is isomorphic to the cokernel of $\operatorname{Hom}(A, \QQ) \to \operatorname{Hom}(A, \QQ/\ZZ)$, the map induced by the quotient map $\QQ \to \QQ/\ZZ$.
Use this to get another proof that $\operatorname{Ext}(\ZZ_{p^\infty}, \ZZ) \approx \widehat{\ZZ}_p$ for $p$ prime.
:::

::: {.solution}
The statement is Hatcher, §3.F Exercise 5. The argument is the card's own: no retained solution set holds a solution of any exercise of §3.F — Koukpari's set carries the §3.F heading *Limits and Ext* with nothing under it, Sam's begins at §4.1, and the others stop earlier — so there is no published proof of this exercise to transcribe.
Apply $\operatorname{Hom}(A,-)$ to $0\to\ZZ\to\QQ\to\QQ/\ZZ\to0$: the resulting long exact sequence ends $\operatorname{Hom}(A,\QQ)\to\operatorname{Hom}(A,\QQ/\ZZ)\to\operatorname{Ext}(A,\ZZ)\to\operatorname{Ext}(A,\QQ)$, and $\QQ$ being divisible (equivalently, injective) kills the last term, so $\operatorname{Ext}(A,\ZZ)$ is the cokernel. For $A=\ZZ_{p^\infty}$ the first Hom vanishes because $\QQ$ is torsionfree while $A$ is torsion, and the second is $\operatorname{End}(\ZZ_{p^\infty})\cong\varprojlim\ZZ/p^n$ because an endomorphism of the Prüfer group is exactly a compatible family of residues.

::: pf

::: {.pf-step #les}
$\operatorname{Ext}(A,\QQ)=0$ for every $A$, since $\QQ$ is divisible, and the long exact sequence of $\operatorname{Hom}(A,-)$ applied to the short exact sequence of step [](#ses){.pf-ref} gives
$$
\operatorname{Hom}(A,\QQ)\to\operatorname{Hom}(A,\QQ/\ZZ)\to\operatorname{Ext}(A,\ZZ)\to\operatorname{Ext}(A,\QQ)\to\cdots
$$

::: pf-proof
The short exact sequence $0\to\ZZ\to\QQ\to\QQ/\ZZ\to0$ is exact because $\QQ/\ZZ$ is by definition the quotient. An injective object $I$ satisfies $\operatorname{Ext}^1(-,I)=0$; the divisible group $\QQ$ is injective (Baer's criterion: a homomorphism from an ideal $n\ZZ$ of $\ZZ$ into $\QQ$ extends, since $\QQ$ is divisible), so $\operatorname{Ext}(A,\QQ)=0$. The long exact sequence of the derived functors of $\operatorname{Hom}(A,-)$ is the displayed one.
:::

:::


::: {.pf-step #ses}
$0\longrightarrow\ZZ\longrightarrow\QQ\longrightarrow\QQ/\ZZ\longrightarrow0$ is short exact.

::: pf-proof
The inclusion $\ZZ\to\QQ$ is injective and the quotient is $\QQ/\ZZ$ by definition, so the sequence is exact at each term.
:::

:::


::: {.pf-step #coker}
$\operatorname{Ext}(A,\ZZ)\cong\operatorname{coker}\bigl(\operatorname{Hom}(A,\QQ)\to\operatorname{Hom}(A,\QQ/\ZZ)\bigr)$.

::: pf-proof
By step [](#les){.pf-ref} the sequence $\operatorname{Hom}(A,\QQ)\to\operatorname{Hom}(A,\QQ/\ZZ)\to\operatorname{Ext}(A,\ZZ)\to0$ is exact, because $\operatorname{Ext}(A,\QQ)=0$. Exactness at $\operatorname{Ext}(A,\ZZ)$ says precisely that $\operatorname{Ext}(A,\ZZ)$ is the cokernel of the preceding map.
:::

:::


::: {.pf-step #prufer}
For $A=\ZZ_{p^\infty}$ one has $\operatorname{Hom}(A,\QQ)=0$, so $\operatorname{Ext}(\ZZ_{p^\infty},\ZZ)\cong\operatorname{Hom}(\ZZ_{p^\infty},\QQ/\ZZ)$.

::: pf-proof
Every element of $\ZZ_{p^\infty}$ is killed by some power of $p$, so $A$ is a torsion group; $\QQ$ is torsionfree, so the image of any homomorphism $A\to\QQ$ is both torsion and torsionfree, hence $0$. Substituting into step [](#coker){.pf-ref} gives the isomorphism.
:::

:::


::: {.pf-step #primary}
$\operatorname{Hom}(\ZZ_{p^\infty},\QQ/\ZZ)\cong\operatorname{End}(\ZZ_{p^\infty})$.

::: pf-proof
The torsion subgroup of $\QQ/\ZZ$ is the direct sum of its $p$-primary parts, the Prüfer groups $\ZZ_{q^\infty}$ for primes $q$, and $\ZZ_{p^\infty}$ is itself the $p$-primary part. A homomorphism $\varphi\colon\ZZ_{p^\infty}\to\QQ/\ZZ$ has image a quotient of a group all of whose elements have $p$-power order, so every element of the image has $p$-power order; hence the image lies in the $p$-primary subgroup. So $\operatorname{Hom}(\ZZ_{p^\infty},\QQ/\ZZ)=\operatorname{Hom}(\ZZ_{p^\infty},\ZZ_{p^\infty})$, which is $\operatorname{End}(\ZZ_{p^\infty})$.
:::

:::


::: {.pf-step #end}
$\operatorname{End}(\ZZ_{p^\infty})\cong\varprojlim_n\ZZ/p^n\ZZ=\widehat\ZZ_p$.

::: pf-proof
Let $C_n\le\ZZ_{p^\infty}$ be the unique cyclic subgroup of order $p^n$, so that $C_1\subset C_2\subset\cdots$ and $\ZZ_{p^\infty}=\bigcup_nC_n$. An endomorphism $\varphi$ is determined by the family of its restrictions, and $\restrictionof{\varphi}{C_n}$ is multiplication by some $a_n\in\ZZ/p^n$; restriction from $C_{n+1}$ to $C_n$ being compatible forces $a_{n+1}\equiv a_n\pmod{p^n}$. This gives a map $\operatorname{End}(\ZZ_{p^\infty})\to\varprojlim_n\ZZ/p^n$; it is injective because a homomorphism out of a union is determined by its restrictions to the $C_n$. It is surjective: given a compatible family $(a_n)$, define $\varphi$ on $C_n$ as multiplication by $a_n$; compatibility makes this well defined on the union, since $C_n\subset C_{n+1}$ and the two definitions agree there, and it is a homomorphism on each $C_n$, hence on the union. So the ring of endomorphisms is the inverse limit, which is the ring $\widehat\ZZ_p$ of $p$-adic integers.
:::

:::


::: {.pf-step #conclusion}
$\operatorname{Ext}(\ZZ_{p^\infty},\ZZ)\cong\widehat\ZZ_p$.

::: pf-proof
Chaining steps [](#prufer){.pf-ref}, [](#primary){.pf-ref} and [](#end){.pf-ref} gives $\operatorname{Ext}(\ZZ_{p^\infty},\ZZ)\cong\operatorname{End}(\ZZ_{p^\infty})\cong\widehat\ZZ_p$, which is the second assertion of the exercise; the first is step [](#coker){.pf-ref}.
:::

:::

:::
:::
