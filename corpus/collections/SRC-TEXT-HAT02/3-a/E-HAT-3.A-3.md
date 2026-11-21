---
schema: qual/card@1
id: E-HAT-3.A-3
kind: problem
title: "Rational and mod-$p$ cohomology determine integral homology"
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
  note: Checked against Hatcher, Algebraic Topology, Section 3.A, Exercise 3; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.A, Exercise 3; it matches the printed text.
- event: solution-reviewed
  by: claude
  date: 2026-11-07
  note: >-
    Read against Hatcher, Algebraic Topology (2002), §3.A Exercise 3, printed p. 267; the statement
    matches the print, reduced groups and all. The exercise is Hatcher's Corollary 3A.7(a) and the
    book prints its proof on pp. 266-267; the card now cites that proof, follows it, and derives the
    two steps that were assertions: $A_n[p]=0$ comes from the universal coefficient sequence in
    degree $n+1$ with Proposition 3A.5(5), where the card had read both $A_n/pA_n=0$ and $A_n[p]=0$
    off the single degree-$n$ sequence, and $\widetilde H_n(X;\QQ)\cong A_n\otimes\QQ$ is Corollary
    3A.6(a) with the Tor term killed by Proposition 3A.5(3). One false step of my own was caught in
    the same pass and is not on the card: $\operatorname{Ext}_\ZZ(H,F)$ does not vanish for a field
    $F$ — $\operatorname{Ext}(\ZZ_p,\FF_p)\cong\FF_p$ — so the first step uses the $F$-dual of the
    complex $C_*(X;F)$ of vector spaces instead, which is where the vanishing of the $\operatorname{Ext}$
    term on p. 197 really applies.
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    The coverage claim is now stated where the proof begins: the exercise is Hatcher's Corollary
    3A.7(a) word for word and the book prints its complete proof on pp. 266--267, so the card's
    proof is a published argument rather than an assembly. Re-read the printed proof against the
    card; every step of the card corresponds to a printed sentence, and the two steps the card
    derives that the print compresses ($A_n[p]=0$ from the degree-$(n+1)$ sequence, and the $F$-dual
    form of the coefficient-field isomorphism) are expansions, not substitutions.
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    The card's four numbered paragraphs are turned into Lamport steps without change of substance,
    since the argument is Hatcher's printed proof of Corollary 3A.7(a) and the card says so. Each
    step now separates the claim from its justification: the exactness of vector-space duality giving
    H^n(X;F) = Hom_F(H_n(X;F),F), the two universal coefficient sequences over Z_p that show
    multiplication by p is both surjective and injective, the identification of A_n with A_n tensor Q
    over a Q-vector space, and the final Ext-Hom sequence whose outer terms vanish. Checked the one
    implication the prose compresses: that A_n tensor Z_p = A_n / pA_n and Tor(A_n, Z_p) = A_n[p] are
    the two facts that make divisibility and torsionfreeness come out. The page numbers were then checked
    against the retained PDF at tmp/sources/hatcher-2002-algebraic-topology.pdf, printed page = PDF
    page - 9: Theorem 3A.3 on p. 264 (PDF 273), Proposition 3A.5 on p. 265 (PDF 274) and Corollary
    3A.6 on p. 266 (PDF 275), each as cited. The universal coefficient theorem's own page was
    then located: the card cited p. 197, but the page search puts the algebraic form of the theorem,
    with its sequence 0 -> Ext(H_{n-1}(C),G) -> H^n(C;G) -> Hom(H_n(C),G) -> 0, on printed p. 195
    (PDF 204) and the topological form for a space X on printed p. 198 (PDF 207), while printed
    p. 197 (PDF 206) is the section's title page and states nothing. The citation is corrected to
    those two pages.
- event: source-checked
  by: claude
  date: 2026-11-20
  note: >-
    Issue #184: the page locators in the card's text are removed; Corollary 3A.7(a), Theorem 3A.3, Proposition 3A.5(3) and Corollary 3A.6(a) are cited
    by number (or, where Hatcher prints none, by the section that carries them), each read in
    `tmp/sources/hatcher-2002-algebraic-topology.md`. The earlier events keep their text
    (QUAL-11); these citations supersede their page locators. No step changes.

---

::: {.problem}
Show that if $\tilde{H}^n(X; \QQ)$ and $\tilde{H}^n(X; \ZZ_p)$ are zero for all $n$ and all primes $p$, then $\tilde{H}_n(X; \ZZ) = 0$ for all $n$, and hence $\tilde{H}^n(X; G) = 0$ for all $G$ and $n$.
:::

::: {.solution}
The exercise is Hatcher's Corollary 3A.7(a) verbatim, and the book prints a complete proof of that corollary; the four steps below are that proof, with each step's reference supplied. This is the complete published argument the card relies on, not an independently assembled proof.

::: pf

::: {.pf-step #fields}
For a field $F$ one has $H^{n}(X;F)\cong\Hom_{F}(H_{n}(X;F),F)$; hence the hypothesis of the exercise implies $\widetilde H_{n}(X;\QQ)=0$ and $\widetilde H_{n}(X;\ZZ_{p})=0$ for every $n$ and every prime $p$.

::: pf-proof
For a field $F$, $C^{n}(X;F)=\Hom_{\ZZ}(C_{n}(X),F)\cong\Hom_{F}(C_{n}(X)\otimes_{\ZZ}F,F)=\Hom_{F}(C_{n}(X;F),F)$, so the cochain complex over $F$ is the $F$-dual of the chain complex of $F$-vector spaces. Dualizing vector spaces is exact, so taking homology commutes with the duality and $H^{n}(X;F)\cong\Hom_{F}(H_{n}(X;F),F)$; this is the module-coefficient universal coefficient theorem over a field, where the $\Ext$ term vanishes (printed p. 195 for the algebraic form, printed p. 198 for the topological one). A vector space with trivial dual is trivial, so vanishing of the cohomology over $F=\QQ$ and over $F=\ZZ_{p}$ forces the corresponding homology to vanish.
:::
:::

::: {.pf-step #divisible}
For $A_{n}=\widetilde H_{n}(X;\ZZ)$, multiplication by every nonzero integer is bijective; hence $A_{n}$ is a vector space over $\QQ$.

::: pf-proof
The universal coefficient theorem, Theorem 3A.3, applied to the augmented singular chain complex, which is a complex of free abelian groups, gives for each prime $p$ the exact sequence
$$0\to A_{n}\otimes\ZZ_{p}\to\widetilde H_{n}(X;\ZZ_{p})\to\Tor(A_{n-1},\ZZ_{p})\to0 .$$
Since $A_{n}\otimes\ZZ_{p}=A_{n}/pA_{n}$ and the middle term vanishes by step [](#fields){.pf-ref}, the sequence in degree $n$ gives $A_{n}/pA_{n}=0$, so multiplication by $p$ is surjective; the sequence in degree $n+1$ gives $\Tor(A_{n},\ZZ_{p})=A_{n}[p]=0$ by Proposition 3A.5(5) (p. 265), so multiplication by $p$ is injective. Hence multiplication by $p$ is bijective for every prime, and therefore by every nonzero integer. A torsionfree divisible abelian group is a vector space over $\QQ$: divisibility supplies the rational scalars and torsionfreeness makes them well defined.
:::
:::

::: {.pf-step #vanish}
$A_{n}=0$ for every $n$.

::: pf-proof
By the universal coefficient theorem with $\QQ$ coefficients, whose $\Tor$ term vanishes by Proposition 3A.5(3), $\widetilde H_{n}(X;\QQ)\cong A_{n}\otimes\QQ$, which is Corollary 3A.6(a) in unreduced form. For a $\QQ$-vector space $A_{n}$ the map $a\mapsto a\otimes1$ is an isomorphism $A_{n}\to A_{n}\otimes\QQ$, and $\widetilde H_{n}(X;\QQ)=0$ by step [](#fields){.pf-ref}; so $A_{n}=0$.
:::
:::

::: {.pf-step #coefficients}
$\widetilde H^{n}(X;G)=0$ for every abelian group $G$ and every $n$.

::: pf-proof
The universal coefficient theorem for cohomology with arbitrary coefficients gives the exact sequence
$$0\to\Ext(A_{n-1},G)\to\widetilde H^{n}(X;G)\to\Hom(A_{n},G)\to0 .$$
Both outer groups vanish by step [](#vanish){.pf-ref}, so the middle one does too.
:::
:::
:::

:::
