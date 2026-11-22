---
schema: qual/card@1
id: E-HAT-4.3-3
kind: problem
title: "Circle retract from direct summand on $H_1$"
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
- event: source-corrected
  by: claude
  date: 2026-11-20
  note: >-
    Citation corrected. The solution cited the exercise with a locator that did not name it; it
    is now cited as §4.3 Exercise 3. The mathematics is unchanged.
    The sentence that no retained set covers the exercise stands: Sam's §4.3 runs over
    exercises 1, 2, 4-9, 11-15, 17-20, 23 and skips 3.
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 4.3, Exercise 3; the stored statement matches.
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
  date: 2026-11-18
  note: >-
    Structured the existing argument into numbered steps without changing it, and supplied the
    hypotheses each cited theorem needs: the universal coefficient theorem in the form giving
    H^1(X;Z) = Hom(H_1(X),Z), whose Ext term vanishes because H_0(X) is free for a CW complex, so no
    connectivity of X is needed; Theorem 4.57 applied with K(Z,1) = S^1 and X a CW complex; and the
    homotopy extension property for the CW pair (X,S^1). Also supplied: that two self-maps of S^1 of
    equal degree are homotopic, and that the endpoint of the extended homotopy is a retraction.
    Not re-read this session: the theorem numbers are those the earlier reading recorded, and no
    printed page was checked.

- event: solution-reviewed
  by: claude
  date: 2026-11-22
  note: >-
    Read against Hatcher, §4.3 Exercise 3. The proof is correct: split $H_1(X)$ over the summand
    $i_*H_1(S^1)$, use the universal coefficient theorem in degree one — where $\operatorname{Ext}$
    of the free group $H_0(X)$ vanishes — to realize the projection as a class $u$, represent $u$ by
    $r\colon X\to S^1$ through Theorem 4.57, observe $\deg(ri)=1$, and extend the homotopy from $ri$
    to the identity over $X$ by the homotopy extension property of the CW pair to obtain an actual
    retraction. One correction: Theorem 4.57 is printed for based classes $\langle X,S^1\rangle$,
    and the step using it wrote unbased classes; the two coincide because $S^1$ is a topological
    group, and the step now says so.
---

::: {.problem}
Suppose that a CW complex $X$ contains a subcomplex $S^1$ such that the inclusion $S^1 \hookrightarrow X$ induces an injection $H_1(S^1; \ZZ) \to H_1(X; \ZZ)$ with image a direct summand of $H_1(X; \ZZ)$.
Show that $S^1$ is a retract of $X$.
:::

::: {.solution}

The argument is the card's own; no retained solution set in `tmp/sources` covers Section 4.3 Exercise 3. The statement was checked against Hatcher, *Algebraic Topology* (2002), §4.3 Exercise 3.

Let $i\colon S^{1}\hookrightarrow X$ be the inclusion of the given subcomplex and $i_{*}\colon H_{1}(S^{1};\ZZ)\to H_{1}(X;\ZZ)$ the induced map, which by hypothesis is injective with image a direct summand isomorphic to $\ZZ$. Fix a generator $\iota\in H^{1}(S^{1};\ZZ)$.

::: pf

::: {.pf-step #splitting}
There is a homomorphism $\lambda\colon H_{1}(X;\ZZ)\to\ZZ$ with $\lambda\circ i_{*}=\mathrm{id}$.

::: pf-proof
By hypothesis $H_{1}(X;\ZZ)=i_{*}\bigl(H_{1}(S^{1})\bigr)\oplus K$ for some subgroup $K$. Let $\lambda$ be the projection onto the first summand followed by the inverse of the isomorphism $i_{*}\colon\ZZ\to i_{*}(H_{1}(S^{1}))$, which exists because $i_{*}$ is injective. Then $\lambda(i_{*}(a))=a$ for every $a$.
:::

:::

::: {.pf-step #uct}
There is $u\in H^{1}(X;\ZZ)$ with $\langle u,i_{*}(a)\rangle=\lambda(i_{*}(a))$ for all $a\in H_{1}(S^{1};\ZZ)$.

::: pf-proof
The universal coefficient theorem gives the short exact sequence $0\to\operatorname{Ext}\bigl(H_{0}(X),\ZZ\bigr)\to H^{1}(X;\ZZ)\to\operatorname{Hom}\bigl(H_{1}(X),\ZZ\bigr)\to0$. For a CW complex $H_{0}(X)$ is free abelian, so the Ext term vanishes and the second map is an isomorphism; take $u$ to be the preimage of $\lambda$ from step [](#splitting){.pf-ref}. Under this isomorphism $\langle u,\alpha\rangle=\lambda(\alpha)$ for every $\alpha\in H_{1}(X;\ZZ)$, in particular for $\alpha=i_{*}(a)$.
:::

:::

::: {.pf-step #classifying}
There is a map $r\colon X\to S^{1}$ with $r^{*}(\iota)=u$.

::: pf-proof
$S^{1}$ is a $K(\ZZ,1)$, and for a CW complex $X$ the assignment $[f]\mapsto f^{*}(\iota)$ is a bijection $[X,S^{1}]\to H^{1}(X;\ZZ)$ — Hatcher's Theorem 4.57 with $n=1$ and $G=\ZZ$, which is printed for based classes $\langle X,S^{1}\rangle$; unbased and based classes coincide here because $S^{1}$ is a topological group. Hence $u$ is represented by some map $r$.
:::

:::

::: {.pf-step #degree-one}
$(ri)^{*}(\iota)=\iota$, so $ri\colon S^{1}\to S^{1}$ has degree $1$.

::: pf-proof
$(ri)^{*}(\iota)=i^{*}\bigl(r^{*}(\iota)\bigr)=i^{*}(u)$ by step [](#classifying){.pf-ref}; and $i^{*}(u)$ pairs with $a\in H_{1}(S^{1};\ZZ)$ as $\langle u,i_{*}(a)\rangle=\lambda(i_{*}(a))=a$ by steps [](#uct){.pf-ref} and [](#splitting){.pf-ref}, so $i^{*}(u)=\iota$. The degree of a self-map $f$ of $S^{1}$ is the integer $d$ with $f^{*}(\iota)=d\,\iota$, so $d=1$.
:::

:::

::: {.pf-step #homotopic}
$ri$ is homotopic to $\mathrm{id}_{S^{1}}$.

::: pf-proof
Self-maps of $S^{1}$ are classified up to homotopy by their degree: by step [](#classifying){.pf-ref} with $X=S^{1}$, homotopy classes correspond bijectively to $H^{1}(S^{1};\ZZ)\cong\ZZ$, and that correspondence is the degree. Since $\mathrm{id}_{S^{1}}$ has degree $1$ and $ri$ has degree $1$ by step [](#degree-one){.pf-ref}, the two are homotopic.
:::

:::

::: {.pf-step #extend}
There is a map $r'\colon X\to S^{1}$ with $r'\circ i=\mathrm{id}_{S^{1}}$.

::: pf-proof
$(X,S^{1})$ is a CW pair, hence has the homotopy extension property: a homotopy of $\restrictionof{r}{S^{1}}=ri$ on $S^{1}\times I$ extends to a homotopy $X\times I\to S^{1}$ starting at $r$. Apply this to a homotopy from $ri$ to $\mathrm{id}_{S^{1}}$, which exists by step [](#homotopic){.pf-ref}, and let $r'$ be its endpoint; then $\restrictionof{r'}{S^{1}}=\mathrm{id}_{S^{1}}$.
:::

:::

::: {.pf-step}
$S^{1}$ is a retract of $X$.

::: pf-proof
Step [](#extend){.pf-ref} produces $r'\colon X\to S^{1}$ with $r' i=\mathrm{id}_{S^{1}}$, which is precisely the definition of a retraction of $i$.
:::

:::

:::

:::
