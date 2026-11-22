---
schema: qual/card@1
id: E-HAT-4.1-21
kind: problem
title: "Postnikov towers and covering spaces commute"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 4.1, Exercise 21; the stored statement matches.
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
    Read against the book (AT.txt:17900-17906 for the statement). Two things were asserted and are now
    stated. First, the notation X_m itself carries a hypothesis the card did not record: an
    (m-1)-connected covering exists only when pi_i(X) = 0 for 2 <= i <= m-1, because a covering has
    pi_i(X_m) isomorphic to pi_i(X) for i >= 2; the card now says so and notes that for m = 2 it is
    vacuous and X_2 is the universal cover, while for X = S^2 and m = 3 the symbol denotes nothing. This
    corrects the earlier audit note on this card, which gave the range as 2 <= i <= m-2; the correct
    upper end is m-1, since (m-1)-connectedness of X_m makes pi_{m-1}(X_m) vanish, and that group is
    pi_{m-1}(X). Second, the final "(X^n)_m is an nth Postnikov stage of X_m, hence (X^n)_m ~ (X_m)^n"
    used uniqueness of Postnikov stages without saying so; the card now names it and cites Hatcher
    Section 4.3, together with the reason the hypothesis applies (both spaces are built from CW complexes
    by homotopy fibres and by attaching killing cells). The homotopy-group bookkeeping and the degenerate
    cases n < m-1 and n = m-1 were checked and are unchanged. Not checked: no re-reading of Hatcher's
    §4.3 beyond the statement of uniqueness.

- event: source-corrected
  by: claude
  date: 2026-11-02
  note: >-
    Corrects the immediately preceding event, which introduced a hypothesis the exercise does not have.
    That note claimed an (m-1)-connected covering X_m exists only when pi_i(X) = 0 for 2 <= i <= m-1,
    on the reasoning of an ordinary covering space, for which pi_i(X_m) is isomorphic to pi_i(X) for
    i >= 2. The reasoning is sound for a covering map but the premise is wrong: Hatcher's
    "(m-1)-connected covering" is the (m-1)-connected cover in the Whitehead tower (Example 4.20,
    AT.txt:17730-17747, where the map Z_n -> X is described as an "n connected cover" and the case n = 1
    is only the universal cover by analogy), realized as the homotopy fibre of X -> X^{m-1} (Section 4.3,
    AT.txt:20576-20579: "The n connected covering of Y can also be obtained as the homotopy fiber of the
    nth stage Y -> Y^n of a Postnikov tower for Y"). It therefore exists for every connected CW complex,
    it is generally not a covering map when m > 1 (the Hopf map S^3 -> S^2 is the 2 connected cover of
    S^2, the book's own example), and no vanishing hypothesis on pi_i(X) is needed. The card now says
    this, and deduces pi_i(X_m) = 0 for i <= m-1 and pi_i(X_m) = pi_i(X) for i >= m from the long exact
    sequence of that homotopy fibration, which is the property the rest of the proof uses. The exercise
    is not false and X_m is not undefined; the audit note this event replaces said otherwise and was
    wrong. The earlier audit report on this card carries the same error (it restricted existence to
    2 <= i <= m-2 and called X_m the universal cover for m >= 2); a correction is appended to that report.
    Not checked: nothing beyond the cited spans; no independent verification of the Whitehead-tower
    construction.

- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Read against Hatcher, Exercise 21 of §4.1, printed p. 359, checked at PDF page 368 of the held
    book. Checked the comparison: $\pi_i(X^n)=\pi_i(X)$ for $i\le n$ and $0$ above, and
    $\pi_i(X_m)=0$ for $i\le m-1$ with $\pi_i(X_m)\cong\pi_i(X)$ for $i\ge m$, the latter from the
    long exact sequence of the homotopy fibration $X_m\to X\to X^{m-1}$, not from any vanishing
    hypothesis; $(X^n)^{m-1}\simeq X^{m-1}$ for $n\ge m-1$, so
    $(X^n)_m\simeq\operatorname{hofib}(X^n\to X^{m-1})$; the comparison map
    $X_m\to(X^n)_m$ is an isomorphism on $\pi_i$ for $i\le n$ and the target has no homotopy above
    $n$, so the target is an $n$-th Postnikov stage of $X_m$, as is $(X_m)^n$, and uniqueness gives the
    equivalence. The degenerate cases were checked: for $n<m-1$ both sides have all homotopy groups
    zero, and for $n=m-1$ both are contractible. No defect. The printed page is added, the card having
    had none.
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    The card stood in queue D: its solution was prose with no numbered step. It is now a `pf` with
    seven steps, each carrying a `pf-proof`, and the two claims are unchanged. Cited by number
    only: Example 4.20 and §4.3 of the book for the identification of the $(m-1)$-connected cover
    with the homotopy fibre of $X\to X^{m-1}$, the long exact homotopy sequence of that
    fibration, and Whitehead's theorem with the uniqueness of $n$th Postnikov stages from §4.3.
    Checked: that $(X^n)^{m-1}\simeq X^{m-1}$ for $n\ge m-1$, which is what makes the two
    homotopy fibres comparable over one base; that the comparison map is an isomorphism on
    $\pi_i$ for $i\le n$; and that both iterands are CW complexes with no homotopy groups when
    $n<m-1$, hence contractible. No vanishing hypothesis on $\pi_i(X)$ is used or needed.
- event: solution-reviewed
  by: claude
  date: 2026-11-22
  note: >-
    Read against Hatcher, §4.1 Exercise 21. The mathematics is correct: the $(m-1)$-connected cover is
    the homotopy fibre of $X\to X^{m-1}$ (§4.3), which exists for every connected CW complex; a
    Postnikov stage is an isomorphism on $\pi_i$ up to $n$ with nothing above; the long exact
    sequences give the vanishing and the isomorphisms in the two ranges; both iterands therefore have
    $\pi_i(X)$ for $m\le i\le n$ and nothing else; the comparison map between the two fibres over
    $X^{m-1}$ is an isomorphism on $\pi_i$ for $i\le n$ and the target vanishes above $n$, so
    $(X^n)_m$ and $(X_m)^n$ are two $n$th Postnikov stages of $X_m$ and agree by uniqueness; and for
    $n<m-1$ both are contractible. Two corrections. (1) The live text said Example 4.20 constructs the
    cover as a homotopy fibre; Example 4.20 constructs the Whitehead tower, and the homotopy-fibre
    description is the one in §4.3, so the sentence now separates the two. (2) The retained sets'
    state is recorded. Left as it stands: the steps are cited by hand-typed numbers ("step 1",
    "step 2"), which STYLE-08 forbids; replacing them by step references is a separate pass over this
    card and is not done here.
- event: solution-reviewed
  by: claude
  date: 2026-11-22
  note: >-
    One correction after an independent reading, in step `ranges`: it said that for $n<m-1$ both
    iterands "are CW complexes, being built from CW complexes by homotopy fibres". A homotopy fibre of
    CW complexes is only of CW homotopy type, not a CW complex, so the step now says that both have
    the homotopy type of CW complexes, and applies Whitehead's theorem to a space of CW homotopy type
    with vanishing homotopy groups.
---

::: {.problem}
For this problem it is convenient to use the notations $X^n$ for the $n$th stage in a Postnikov tower for $X$ and $X_m$ for an $(m-1)$-connected covering of $X$, where $X$ is a connected CW complex.
Show that $(X^n)_m \simeq (X_m)^n$, so the notation $X_m^n$ is unambiguous.
Thus $\pi_i(X_m^n) \approx \pi_i(X)$ for $m \leq i \leq n$ and all other homotopy groups of $X_m^n$ are zero.
:::

::: {.solution}

The exercise is §4.1 Exercise 21. No retained solution set holds a solution: Sam's §4.1 has no entry for the exercise, and Proudfoot's Homework #6 covers Exercises 4, 11, 12, 14 and 15. Throughout $X$ is a connected CW complex, $X^n$ is the $n$th stage of a Postnikov tower for $X$, and $X_m$ is the $(m-1)$-connected cover of $X$.

::: pf

::: pf-step
The word "covering" names the $(m-1)$-connected cover in the Whitehead tower, not an ordinary covering space: for every connected CW complex $X$ it is the homotopy fibre of $X\to X^{m-1}$.

::: pf-proof
Hatcher's Example 4.20 constructs the Whitehead tower, in which $Z_n$ is $n$-connected and $Z_n\to X$ is an isomorphism on $\pi_i$ for $i>n$; §4.3 identifies the $n$-connected covering of $Y$ with the homotopy fibre of $Y\to Y^n$. So $X_m\simeq\operatorname{hofib}(X\to X^{m-1})$ exists for every connected CW complex. For $m=2$ this is the universal cover; for $m>1$ it need not be a covering map at all, the Hopf map $S^3\to S^2$ being the $2$-connected cover of $S^2$. No vanishing hypothesis on the homotopy groups of $X$ is needed for its existence.
:::

:::

::: pf-step
$\pi_i(X^n)\cong\pi_i(X)$ for $i\le n$, and $\pi_i(X^n)=0$ for $i>n$.

::: pf-proof
An $n$th Postnikov stage of $X$ is a space under $X$ whose structure map $X\to X^n$ is an isomorphism on $\pi_i$ for $i\le n$ and whose homotopy groups vanish above $n$ (Hatcher, §4.3, where the stages are built by attaching cells killing the higher homotopy groups); those two properties are exactly the two clauses.
:::

:::

::: pf-step
$\pi_i(X_m)=0$ for $i\le m-1$, and $\pi_i(X_m)\cong\pi_i(X)$ for $i\ge m$.

::: pf-proof
By step 1 and step 2, the map $X\to X^{m-1}$ is an isomorphism on $\pi_i$ for $i\le m-1$ and its target has no homotopy in degrees $\ge m$. The long exact homotopy sequence of the fibration $X_m\to X\to X^{m-1}$ then gives $\pi_i(X_m)=0$ for $i\le m-1$ and $\pi_i(X_m)\cong\pi_i(X)$ for $i\ge m$, since the two neighbouring groups in the sequence are respectively equal, in the range where the connecting map does not intervene. In particular no vanishing of $\pi_i(X)$ enters.
:::

:::

::: pf-step
Both iterated constructions have
$$
\pi_i\cong\begin{cases}\pi_i(X),&m\le i\le n,\\0,&i<m\text{ or }i>n.\end{cases}
$$

::: pf-proof
Apply step 2 to $X_m$ and step 3 to $X^n$: $(X_m)^n$ has the homotopy groups of $X_m$ up to degree $n$ and none above, and those are $\pi_i(X)$ for $m\le i$ and $0$ below; $(X^n)_m$ has the homotopy groups of $X^n$ from degree $m$ up and $0$ below $m$, and those are $\pi_i(X)$ for $i\le n$ and $0$ above. Both descriptions give the displayed groups.
:::

:::

::: pf-step
For $n\ge m-1$ one has $(X^n)_m\simeq\operatorname{hofib}(X^n\to X^{m-1})$, and this is the same model as $X_m\simeq\operatorname{hofib}(X\to X^{m-1})$, so the map $X\to X^n$ induces a comparison map $X_m\to(X^n)_m$.

::: pf-proof
The $(m-1)$th stage of a Postnikov tower for $X^n$ is $X^{m-1}$ when $n\ge m-1$, since the two towers agree through degree $m-1$ and the stages below are unchanged; so by step 1 applied to $X^n$ the object $(X^n)_m$ is the homotopy fibre of $X^n\to X^{m-1}$. A map of homotopy fibrations over the same base, here $X\to X^n$ over $X^{m-1}$, induces a map of the fibres, which is the comparison map. For $n<m-1$ this step is not used; step 7 treats that range.
:::

:::

::: pf-step
The comparison map $X_m\to(X^n)_m$ is an isomorphism on $\pi_i$ for $i\le n$, and the target has no homotopy above $n$; hence $(X^n)_m$ is an $n$th Postnikov stage of $X_m$, as is $(X_m)^n$, and by uniqueness
$$
(X^n)_m\simeq(X_m)^n.
$$

::: pf-proof
Both sides are homotopy fibres of maps out of $X$ and $X^n$ over the common base $X^{m-1}$, whose homotopy groups vanish above $m-1$; the long exact sequences of the two fibrations, compared through the map $X\to X^n$ which is an isomorphism on $\pi_i$ for $i\le n$, give that the comparison map is an isomorphism on $\pi_i$ for $i\le n$. The target has no homotopy above $n$ by step 4. A space under $X_m$ whose structure map is an isomorphism on $\pi_i$ for $i\le n$ and whose higher homotopy vanishes is an $n$th Postnikov stage of $X_m$; $(X_m)^n$ is one by definition, and $(X^n)_m$ is one by what was just shown. Two $n$th Postnikov stages of the same space are homotopy equivalent under it, by Whitehead's theorem applied to the map of towers (Hatcher, §4.3).
:::

:::

::: pf-step
For $n<m-1$ both iterands are contractible, and for $n=m-1$ the fibre model of step 5 applies; so the notation $X_m^n$ is unambiguous up to homotopy, with the homotopy groups of step 4.

::: pf-proof
If $n<m-1$ then both $(X^n)_m$ and $(X_m)^n$ have all homotopy groups zero by step 4, and both have the homotopy type of CW complexes, a homotopy fibre of CW complexes having CW homotopy type and a Postnikov stage being a CW complex; a space of CW homotopy type with no homotopy groups is contractible by Whitehead's theorem. If $n=m-1$ then $n\ge m-1$, so steps 5 and 6 apply and give the equivalence. The homotopy groups are those of step 4 in every case, which is the second assertion of the exercise.
:::

:::

:::
:::
