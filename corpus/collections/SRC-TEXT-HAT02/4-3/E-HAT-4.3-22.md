---
schema: qual/card@1
id: E-HAT-4.3-22
kind: problem
title: "Principal fibrations with sections split"
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
    Pages and one claim corrected, after an independent read. The sentence "a fiber-preserving map
    that is a homotopy equivalence is a fiber homotopy equivalence" is on printed p. 406, not
    p. 405, and its deferred proof is §4.H Exercise 3, printed p. 466; the event of 2026-11-19
    carries the old page and is left as written under QUAL-11. The claim that a fibration over a
    CW base has total space of CW type is false (B x Q -> B is a fibration and Q is not of CW
    type); the step now replaces by CW approximations, as Hatcher does on p. 412, before applying
    Whitehead's theorem. The statement is unchanged: the page image of printed p. 420 reads
    "iff", which the OCR of tmp/hat/AT.txt loses, and the card's "if and only if" is the printed
    wording.
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    Restructured under #2 into numbered steps. The printed statement was re-read on the page
    image: Exercise 22 on printed p. 420 reads "is fiber homotopy equivalent to the product
    Omega C x B iff it has a section", so the card's "if and only if" is the printed wording and
    is kept; the OCR text in tmp/hat/AT.txt prints "if" there, which is an extraction loss, and
    the page image decides it. No retained solution set covers §4.3 Exercise 22 (Sam's set has 17
    and 19-20, not 22), so the argument is the card's own. The two directions are now separated:
    the pullback model is shown to be fibre homotopy equivalent to the product by an explicit
    fibre-wise homeomorphism omega -> omega . gamma_b, and the converse reads a strict section off
    the fibre-preserving map back from the product, so no homotopy-lifting strictification is
    needed. Checked against the definition of a principal fibration, printed p. 412, Proposition
    4.62, printed p. 406, Proposition 4.65, printed p. 408, the remark on printed p. 405, and
    Theorem 4.5, printed p. 346. Not checked: no certificate, and the §4.H exercise proving the
    p. 405 remark was not read.
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Read against Hatcher, Algebraic Topology (2002), §4.3 Exercise 22, printed p. 420,
    against the definition of a principal fibration on printed p. 412, and against the
    remark on printed p. 405 that a fibre-preserving map which is a homotopy equivalence
    is a fibre homotopy equivalence. The card opened with "by definition, a principal
    fibration is fiber homotopy equivalent to the pullback", which the definition does not
    say: p. 412 asks only for weak homotopy equivalences in the comparison diagram. The
    gap is closable and is now closed: a weak homotopy equivalence of total spaces between
    fibrations with CW type is a homotopy equivalence by Whitehead, and a fibre-preserving
    homotopy equivalence is a fibre homotopy equivalence by the fact Hatcher states on
    p. 405; the two properties the exercise compares are invariant under fibre homotopy
    equivalence over B, so the pullback model may be used. The card also now cites
    Proposition 4.62 for the homotopy invariance of the pullback instead of Exercise 11.
    The converse direction and the product section were correct as written. Statement
    unchanged. Not checked: the §4.H exercise that proves the p. 405 fact.
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
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
  date: 2026-11-01
  note: >-
    Proof completed: the statement is an iff, and only the direction section => fibre homotopy equivalent to Omega C x B was proved. The converse is now supplied: a fibre homotopy equivalence over B contains a map r: B x Omega C -> E with p r = pr_B, and composing with the product's own section const_{c_0} gives a section of E -> B.
---

::: {.solution}
No retained solution set covers this exercise, so the argument is the card's own. The printed statement is an equivalence: a principal fibration $\Omega C\to E\xrightarrow{p}B$ is fibre homotopy equivalent to the product $\Omega C\times B$ if and only if it has a section. The proof reduces to the pullback model that the definition of a principal fibration provides, where both directions are explicit.

::: pf

::: {.pf-step #principal}
It suffices to prove the statement for the pullback $q\colon f^*(PC)\to B$ of the path fibration along a map $f\colon B\to C$.

::: pf-proof
By the definition of a principal fibration there is a commutative diagram whose second row is the fibration sequence $\Omega C\to PC\to C$ and whose vertical maps are weak homotopy equivalences; the map $E\to B$ therefore compares with $PC\to C$ over $C$, and the universal property of the pullback gives a map $E\to f^*(PC)$ over $B$, again a weak homotopy equivalence. Replacing the spaces by CW approximations as Hatcher does --- the CW hypothesis cannot be asserted of the total space of an arbitrary fibration over a CW base, since $B\times\QQ\to B$ is one and $\QQ$ is not of CW type --- a fibre-preserving weak homotopy equivalence of total spaces is a homotopy equivalence by Whitehead's theorem (Theorem 4.5) these vertical maps are homotopy equivalences; a fibre-preserving homotopy equivalence is a fibre homotopy equivalence by the fact recorded, whose deferred proof is §4.H Exercise 3. Both properties compared by the exercise --- having a section, and being fibre homotopy equivalent to the product --- are invariant under fibre homotopy equivalence over $B$, so it is enough to treat $q$.
:::

:::

::: {.pf-step #model}
A section $s(b)=(b,\gamma_b)$ of $q$ gives a fibre homotopy equivalence $\Phi\colon B\times\Omega C\to f^*(PC)$ over $B$.

::: pf-proof
Here $f^*(PC)=\{(b,\gamma):\gamma\colon I\to C,\ \gamma(0)=c_0,\ \gamma(1)=f(b)\}$ and $q(b,\gamma)=b$, so the fibre over $b$ is the space of paths from $c_0$ to $f(b)$, and a section is a continuous choice of such a path $\gamma_b$ for each $b$. Define $\Phi(b,\omega)=(b,\omega\cdot\gamma_b)$, the concatenation of the loop $\omega$ at $c_0$ with $\gamma_b$; this path starts at $c_0$ and ends at $f(b)$, and $q\Phi(b,\omega)=b$, so $\Phi$ is fibre preserving. On the fibre over $b$ it is the map $\omega\mapsto\omega\cdot\gamma_b$ from $\Omega C$ to the path space $P_{c_0,f(b)}C$, whose inverse up to homotopy is $\delta\mapsto\delta\cdot\gamma_b^{-1}$, concatenation with the reverse path; both composites are homotopic to the identity through maps that keep the fibre fixed. Hence $\Phi$ is a fibre homotopy equivalence over $B$.
:::

:::

::: {.pf-step #forward}
If the principal fibration has a section, it is fibre homotopy equivalent to $\Omega C\times B$.

::: pf-proof
A section of $E\to B$ gives a section of the pullback model by step [](#principal){.pf-ref}, hence a fibre homotopy equivalence $\Phi$ as in step [](#model){.pf-ref}, and $\Phi$ is a fibre homotopy equivalence between $E\to B$ and the product by step [](#principal){.pf-ref}. The product here is $\Omega C\times B\to B$, the projection.
:::

:::

::: {.pf-step #backward}
If the principal fibration is fibre homotopy equivalent to $\Omega C\times B\to B$, it has a section.

::: pf-proof
The product carries the section $s_0(b)=(b,\mathrm{const}_{c_0})$. Let $\Psi\colon\Omega C\times B\to E$ be a fibre-preserving map that is a homotopy inverse to the given fibre homotopy equivalence over $B$; being fibre preserving, it satisfies $p\Psi=\operatorname{pr}_B$. Then $s=\Psi\circ s_0$ is a map $B\to E$ with $p\,s=\operatorname{pr}_B s_0=\id_B$, a strict section.
:::

:::

::: {.pf-step}
A principal fibration $\Omega C\to E\to B$ is fibre homotopy equivalent to $\Omega C\times B$ if and only if it has a section.

::: pf-proof
Step [](#forward){.pf-ref} gives the implication from a section to the product, and step [](#backward){.pf-ref} the converse.
:::

:::

:::
:::
