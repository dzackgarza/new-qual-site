---
schema: qual/card@1
id: E-HAT-4.3-1
kind: problem
title: "Map $\\RP^\\infty \\to K(\\ZZ,2)$ trivial on homology"
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
  date: 2026-11-20
  note: >-
    Citation convention. Sources on this card are cited by chapter, section and numbered statement
    only, and the statement and solution above cite every source by its numbered statement. The
    events dated before today are left as their sessions wrote them, which QUAL-11 requires, so a
    locator in one of them stands as a historical record and is superseded by the citation now on
    the card. This event records the convention and claims no further reading: the
    mathematics of the card is as those events describe it.
- event: source-checked
  by: claude
  date: 2026-11-20
  note: >-
    The sentence in the 2026-11-20 solution-written event, that the §3.1 exercise Hatcher's
     pointer names was not located, is now resolved: it is §3.1 Exercise 11,
    the Moore space M(Z_m,n) version of this example, whose part (a) asks for the same conclusion,
    that the cohomology splitting cannot be natural, and whose part (b) is the dual statement for
    the inclusion of S^n. Read; the body now names it. Not checked: part (b)
    beyond its statement.
- event: source-corrected
  by: claude
  date: 2026-11-20
  note: >-
    The solution's provenance sentence, "No retained solution set covers this exercise", was
    false: Steven V. Sam, Solutions to Algebraic Topology (2008), covers §4.3 Exercise 1 on
    in tmp/sources/hatcher-solutions-sam-2008.pdf, where the section heading and Exercise 1 both
    sit. Read there: Sam computes both reduced homology groups,
    represents homotopy classes of maps into CP-infinity by H^2(RP-infinity;Z) through Theorem
    4.57, and states the consistency as Hom(Z/2,Z) = 0. He does not write out the naturality
    argument. The card now cites the set and says which part of the argument is its own.
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    Rebuilt under #2 with the universal coefficient question settled. The steps are now: the
    cellular homology of the two spaces (Example 0.5 and Example 2.42); the degree-two universal coefficient sequences (Theorem 3.2, with the
    paragraph after Corollary 3.3 recording that the sequence is natural and the
    splitting is not); the map f with f^*(c) = nu (Example 4.50, and Theorem 4.57,
    ); f_* = 0 on reduced integral homology; the diagram argument that a natural
    splitting would force f^*(c) = 0, since Hom(H_2(CP-infinity),Z) -> Hom(H_2(RP-infinity),Z) is
    zero and Ext(H_1(CP-infinity),Z) = 0, so no natural splitting exists; and the coefficient ring,
    where over a field the Ext term vanishes and the same f is nonzero on H_2(-;F_2). Checked
    against the numbered statements named. Not checked: no formal certificate, and the §3.1
    exercise Hatcher's sentence points to was not located or read; the example proved on the
    card is
    §4.3 Exercise 1 itself.
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 4.3, Exercise 1; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: claude
  date: 2026-11-02
  note: >-
    Cards read. Verdict record is m6__proofs-4-3-1-12.md (1-12: 10 correct, 5 a dimension slip, 9 a wrong assertion; both repaired) and m2__proofs-4-3-13-24.md (13-24: 10 correct, 20 a display misalignment repaired by identifying the principal fibration, 22 the missing converse of an iff, later restated and proved, and 24, whose whole proof was then written). No card in this slice has an unmet piece.

- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Restructured into a structured proof under #2. Re-checked: $\CP^\infty$ represents $H^2(-;\ZZ)$, so
    the nonzero class $\nu$ is $f^*(c)$ for some $f$; $\widetilde H_i(\RP^\infty)=\ZZ/2$ in odd degrees
    and $0$ in even, against free groups in even degrees for $\CP^\infty$, so every homology
    homomorphism out of a torsion group into a free group is zero; and in degree $2$ the two groups
    sit in different UCT summands, $\Ext(\ZZ/2,\ZZ)$ for the projective space and
    $\Hom(\ZZ,\ZZ)$ for the complex one, whose splitting is not natural. Repaired: the earlier text
    introduced the class as $\nu$ and then wrote $f^*(c)=u\ne0$, leaving $u$ undefined; the card now
    uses $\nu$ throughout. Added: the reason a map with the stated pullback exists, the cellular
    computation behind both homology groups, and the explicit identification of the two UCT summands
    as the resolution of the apparent contradiction. No defect found in the statement, §4.3 Exercise
    1. No retained solution set covers it.
---

::: {.solution}
Steven V. Sam's retained set covers this exercise: *Solutions to Algebraic Topology* (2008), §4.3 Exercise 1, in `tmp/sources/hatcher-solutions-sam-2008.pdf`. Sam computes both reduced homology groups, represents homotopy classes of maps into $\CP^\infty$ by $H^2(\RP^\infty;\ZZ)$ through Theorem 4.57, and states the consistency as $\Hom(\ZZ/2,\ZZ)=0$, that is, the class is seen by $\Ext$ and not by $\Hom$. He does not write out the naturality argument, which is the content of steps [](#natural){.pf-ref} and [](#coefficients){.pf-ref}; Hatcher's own pointer to an exercise at the end of §3.1 is to Exercise 11 there, the Moore-space version of this same example. Write $\nu$ for the nonzero class of $H^2(\RP^\infty;\ZZ)\cong\ZZ/2$ and $c$ for the generator of $H^2(\CP^\infty;\ZZ)\cong\ZZ$.

::: pf

::: {.pf-step #homology}
$\widetilde H_i(\RP^\infty;\ZZ)$ is $\ZZ/2$ for $i$ odd and $0$ for $i$ even, and $\widetilde H_i(\CP^\infty;\ZZ)$ is $\ZZ$ for $i$ even and positive and $0$ for $i$ odd.

::: pf-proof
$\RP^\infty$ has a CW structure with one cell in each dimension and $\CP^\infty$ one with a single cell in each even dimension (Example 0.5--7). For $\RP^\infty$ the cellular boundary is multiplication by $2$ in each even degree and zero in each odd degree, so the cellular chain complex is $\cdots\to\ZZ\xrightarrow{2}\ZZ\xrightarrow{0}\ZZ\xrightarrow{2}\ZZ\to0$, whose homology is $\ZZ/2$ in odd degrees and $0$ in even positive degrees; this is the computation of Example 2.42, for $\RP^n$, and $\RP^\infty$ is the union of the $\RP^n$. For $\CP^\infty$ there are no odd-dimensional cells, so every boundary map is zero and the homology is $\ZZ$ in each even positive degree. Both spaces are path connected, so $\widetilde H_0=0$ for both.
:::

:::

::: {.pf-step #uct}
In degree $2$ the universal coefficient sequence reads $0\to\ZZ/2\to H^2(\RP^\infty;\ZZ)\to0\to0$ and $0\to0\to H^2(\CP^\infty;\ZZ)\to\ZZ\to0$.

::: pf-proof
Theorem 3.2 gives the split exact sequence $0\to\Ext(H_{n-1}(X),G)\to H^n(X;G)\to\Hom(H_n(X),G)\to0$, and the paragraph following Corollary 3.3 records that the sequence is natural in $X$ while its splitting is not. Take $n=2$, $G=\ZZ$ and use step [](#homology){.pf-ref}: for $\RP^\infty$, $H_2=0$ and $H_1=\ZZ/2$, so the outer groups are $\Ext(\ZZ/2,\ZZ)\cong\ZZ/2$ and $\Hom(0,\ZZ)=0$; for $\CP^\infty$, $H_2=\ZZ$ and $H_1=0$, so they are $\Ext(0,\ZZ)=0$ and $\Hom(\ZZ,\ZZ)\cong\ZZ$. The class $c$ is the image of $\id_\ZZ$ under the surjection onto $\Hom(\ZZ,\ZZ)$, and $\nu$ generates the $\Ext$ group of $\RP^\infty$.
:::

:::

::: {.pf-step #map}
There is a map $f\colon\RP^\infty\to\CP^\infty$ with $f^*(c)=\nu\ne0$.

::: pf-proof
$\CP^\infty$ is a $K(\ZZ,2)$ (Example 4.50) and $\RP^\infty$ is a CW complex, so Theorem 4.57 gives a bijection $T\colon\langle\RP^\infty,\CP^\infty\rangle\to H^2(\RP^\infty;\ZZ)$ of the form $T([g])=g^*(\alpha)$ for a distinguished class $\alpha\in H^2(\CP^\infty;\ZZ)$. By step [](#uct){.pf-ref}, $H^2(\CP^\infty;\ZZ)\cong\ZZ$, so $\alpha=\pm c$; choose $f$ with $T([f])=\nu$, so that $f^*(c)=\pm\nu$, and replace $f$ by a representative of $T^{-1}(-\nu)$ if the sign is negative. Since $\nu\ne0$, this $f$ is nontrivial on integral cohomology in degree $2$.
:::

:::

::: {.pf-step #trivial}
$f_*=0$ on every reduced integral homology group.

::: pf-proof
By step [](#homology){.pf-ref}, in each degree the source is either $\ZZ/2$ and the target a free abelian group, or the source is $0$. Every homomorphism $\ZZ/2\to\ZZ$ is zero because $\ZZ$ is torsion free, and every homomorphism out of $0$ is zero, so $f_*=0$ in every reduced degree.
:::

:::

::: {.pf-step #natural}
No splitting of the universal coefficient sequence is natural in $X$, and this example proves it.

::: pf-proof
A natural splitting would give, for every space $X$, a homomorphism $s_X\colon\Hom(H_2(X),\ZZ)\to H^2(X;\ZZ)$ with $h_Xs_X=\id$ and $s$ natural in $X$. Apply naturality to $f$: the square relating $f^*$ on cohomology to precomposition with $f_*$ on $\Hom$ commutes. The map $\Hom(H_2(\CP^\infty),\ZZ)=\ZZ\to\Hom(H_2(\RP^\infty),\ZZ)=0$ is zero because $H_2(\RP^\infty)=0$ by step [](#homology){.pf-ref}. Naturality would therefore give $f^*(c)=f^*s_{\CP^\infty}(\id)=s_{\RP^\infty}(0)=0$, contradicting $f^*(c)=\nu\ne0$ from step [](#map){.pf-ref}. The other outer group gives the same conclusion: the natural map $\Ext(H_1(\CP^\infty),\ZZ)=\Ext(0,\ZZ)=0\to\Ext(\ZZ/2,\ZZ)$ is also zero, so under any splitting both components of $c$ would map to zero. What holds is naturality of the exact sequence, as Theorem 3.2 and the paragraph following Corollary 3.3 assert; what fails is naturality of any splitting, which is the topological example Hatcher promises at that point and which this exercise supplies.
:::

:::

::: {.pf-step #coefficients}
The statement is specific to $\ZZ$: over a field $F$ a map trivial on $H_*(-;F)$ is trivial on $H^*(-;F)$, whereas the map $f$ above is nontrivial on $H_2(-;\FF_2)$.

::: pf-proof
Over a field $F$ the group $\Ext_F$ vanishes on $F$-vector spaces, so the universal coefficient theorem is the natural isomorphism $H^n(X;F)\cong\Hom(H_n(X;F),F)$; a map inducing zero on $H_n(-;F)$ therefore induces zero on $H^n(-;F)$. For $F=\FF_2$ and the map $f$ of step [](#map){.pf-ref}, naturality of reduction modulo $2$ gives $f^*(c\otimes1)=(f^*c)\otimes1=\nu\otimes1\ne0$ in $H^2(\RP^\infty;\FF_2)\cong\FF_2$, since $\nu$ has order $2$. Under the field-coefficient duality this says $f_*\ne0$ on $H_2(-;\FF_2)$. So the reduced integral homology of $f$ vanishes while its homology with $\FF_2$ coefficients does not, and the coefficient ring is part of the statement.
:::

:::

::: {.pf-step}
$f_*=0$ on reduced integral homology, $f^*\ne0$ on reduced integral cohomology, and the universal coefficient theorem is consistent with this because its splitting is not natural.

::: pf-proof
Steps [](#homology){.pf-ref}, [](#uct){.pf-ref}, [](#map){.pf-ref} and [](#trivial){.pf-ref} give the two assertions; step [](#natural){.pf-ref} shows that no natural splitting exists, so the vanishing on homology does not force vanishing on cohomology; step [](#coefficients){.pf-ref} shows that the integral coefficient ring is essential to the example.
:::

:::

:::
:::
