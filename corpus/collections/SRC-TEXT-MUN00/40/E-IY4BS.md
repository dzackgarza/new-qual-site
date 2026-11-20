---
schema: qual/card@1
id: E-IY4BS
kind: problem
title: Complements of $F_\sigma$ sets are $G_\delta$ sets
classification:
  areas:
  - topology
  topics:
  - Topological Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    No complete published solution was located for this exercise, so the proof is checked line by line
    against the book and the search is recorded in the COMPLAINTS.md entry for §39--§42 of SRC-TEXT-MUN00.
    Searched: the sets listed in that entry --- Aleksey Zinger's MAT 530 sheets, the *Praying For Stockholm*
    posts, Moller's S38, the Riverside Math 205A solutions, Orellana, Doug's World, Whitman,
    "positron0802", "shenapse", "9beach", "kyp44", the seven further GitHub manuals, dbfin and Gardner's
    ETSU notes --- none of which solves this exercise.
    Checked against Munkres, Topology (2000), Section 40 Exercise 2, printed p. 251, with the definitions of $F_\sigma$ and $G_\delta$ and De Morgan's laws (§1). No correction was needed.
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps; checked both De Morgan identities and the openness or
    closedness of the complementary sets. The argument is the card's own; no retained set is
    cited. Munkres §40, printed p. 246. The printed statement needed no repair.
- event: solution-reviewed
  by: claude
  date: 2026-11-20
  note: >-
    Issue #169 correctness read, with the #184 citation repair. Both directions are the two
    De Morgan identities, stated correctly: $\bigcup_n F_n$ has complement $\bigcap_n(X-F_n)$
    with each $X-F_n$ open, and $\bigcap_n U_n$ has complement $\bigcup_n(X-U_n)$ with each
    $X-U_n$ closed. The closing step applies the second implication with $X-W$ in place of $W$,
    which is legitimate because $X-W$ is an arbitrary subset. Nothing else is used. Citation by
    number: §40 Exercise 2; the phrase "printed p. 246" is removed from the solution, and the
    earlier events' page locators are superseded, their text kept as written (QUAL-11).

- event: source-corrected
  by: claude
  date: 2026-11-20
  note: >-
    Issue #169 second read, on the verification member's report of this card. The closing step
    said the two implications were #f-sigma and #g-delta "the second applied to the set X-W in
    place of W", which is the wrong direction: with $X-W$ substituted for $W$, #g-delta concludes
    that $X-W$ is an $F_\sigma$ from $W$ a $G_\delta$, not that $W$ is an $F_\sigma$ from $X-W$ a
    $G_\delta$. The two implications are #f-sigma and #g-delta as they stand, and the step now
    states both. The mathematics of the two steps was already right; only this sentence changed.

---

::: {.exercise}

A subset $W$ of $X$ is said to be an "$F_\sigma$ set" in $X$ if $W$ equals a countable union of closed sets of $X$.
Show that $W$ is an $F_\sigma$ set in $X$ if and only if $X - W$ is a $G_\delta$ set in $X$.

[The terminology comes from the French. The "F" stands for "fermé," which means "closed," and the "σ" for "somme," which means "union."]
:::

::: {.solution}
The argument is the card's own; no retained solution set is cited on the card. It is the two De Morgan identities behind the definitions of $F_\sigma$ and $G_\delta$ sets in Munkres §40.

::: pf

::: {.pf-step #f-sigma}
If $W=\bigcup_{n}F_{n}$ with each $F_{n}$ closed in $X$, then $X-W$ is a $G_{\delta}$ set in $X$.

::: pf-proof
By De Morgan's law, $X-W=X-\bigcup_{n}F_{n}=\bigcap_{n}(X-F_{n})$. Each complement $X-F_{n}$ is open in $X$, because $F_{n}$ is closed, so $X-W$ is a countable intersection of open sets, that is a $G_{\delta}$ set.
:::

:::

::: {.pf-step #g-delta}
If $X-W=\bigcap_{n}U_{n}$ with each $U_{n}$ open in $X$, then $W$ is an $F_{\sigma}$ set in $X$.

::: pf-proof
By De Morgan's law, $W=X-\bigcap_{n}U_{n}=\bigcup_{n}(X-U_{n})$. Each complement $X-U_{n}$ is closed in $X$, because $U_{n}$ is open, so $W$ is a countable union of closed sets, that is an $F_{\sigma}$ set.
:::

:::

::: {.pf-step}
$W$ is $F_{\sigma}$ in $X$ if and only if $X-W$ is $G_{\delta}$ in $X$.

::: pf-proof
Assume $W=\bigcup_nF_n$ with every $F_n$ closed; step [](#f-sigma){.pf-ref} makes $X-W$ a $G_\delta$. Conversely, if $X-W=\bigcap_nU_n$ with every $U_n$ open, that is the hypothesis of step [](#g-delta){.pf-ref}, which makes $W$ an $F_\sigma$.
:::

:::

:::
:::
