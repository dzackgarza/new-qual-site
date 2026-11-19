---
schema: qual/card@1
id: E-HAT-4.H-3
kind: problem
title: "Fiber-preserving homotopy equivalences are fiber homotopy equivalences"
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
  note: Checked against Hatcher, Algebraic Topology, Section 4.H, Exercise 3; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-corrected
  by: claude
  date: 2026-11-01
  note: >-
    Statement repaired against Hatcher's printed text: the card had dropped printed matter
    (a bracketed hint or pointer, or a printed sentence) that an audit located by word-by-word
    comparison with tmp/hat/AT.txt, and that this session re-verified at the cited lines before
    applying the repair. The restored text is the printed wording and the mathematics of the
    statement is otherwise unchanged.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Structured the argument into numbered steps, isolating the lemma it turns on and applying it
    twice. Supplied what the prose left to the reader: that the homotopy lifting property applied to
    the homotopy p_1 g = p_2 starting at g produces g' with p_1 g' = p_2; that the lifted homotopy
    k_t of the lemma exists because p h_t starts at p = p k_0 with k_0 the identity; and that l,
    being a g with a a fiber homotopy equivalence and g an ordinary one, is an ordinary homotopy
    equivalence, so the construction may be repeated with l in place of f. The two-parameter lifting
    inside the lemma is the one step kept as a citation of the standard argument, and the card says
    so at that step. Not re-read this session: printed pp. 16 and 375, cited by the statement and the
    argument.
---

::: {.problem}
For fibrations $E_1 \to B$ and $E_2 \to B$, show that a fiber-preserving map $E_1 \to E_2$ that is a homotopy equivalence is in fact a fiber homotopy equivalence.
[This is dual to Proposition 0.19.]
:::

::: {.solution}

The argument is the card's own, following the printed remark that the statement is Eckmann--Hilton dual to Proposition 0.19 (printed p. 16); no retained solution set in `tmp/sources` covers Section 4.H Exercise 3. A fibration is a map with the homotopy lifting property for all spaces (printed p. 375), and $\simeq_{B}$ denotes a homotopy through fiber-preserving maps.

Let $p_{1}\colon E_{1}\to B$ and $p_{2}\colon E_{2}\to B$ be fibrations and let $f\colon E_{1}\to E_{2}$ satisfy $p_{2}f=p_{1}$.

::: pf

::: {.pf-step #homotopy-inverse}
There is $g\colon E_{2}\to E_{1}$ with $fg\simeq\mathrm{id}_{E_{2}}$ and $gf\simeq\mathrm{id}_{E_{1}}$.

::: pf-proof
A homotopy equivalence has a homotopy inverse by definition.
:::

:::

::: {.pf-step #over-B}
$p_{1}g\simeq p_{2}$.

::: pf-proof
$p_{2}fg=p_{1}g$ since $p_{2}f=p_{1}$, and applying $p_{2}$ to $fg\simeq\mathrm{id}_{E_{2}}$ gives $p_{2}fg\simeq p_{2}$.
:::

:::

::: {.pf-step #deform}
There is a fiber-preserving $g'\colon E_{2}\to E_{1}$ with $p_{1}g'=p_{2}$, $g'f\simeq\mathrm{id}_{E_{1}}$ and $fg'\simeq\mathrm{id}_{E_{2}}$.

::: pf-proof
Apply the homotopy lifting property of $p_{1}$ to the homotopy $p_{1}g\simeq p_{2}$ of step [](#over-B){.pf-ref}, whose value at time $0$ lifts as $g$ on $E_{2}\times\{0\}$; get $G_{t}$ with $G_{0}=g$, $p_{1}G_{t}$ the given homotopy, hence $p_{1}G_{1}=p_{2}$. Put $g'=G_{1}$, which is fiber-preserving. Since $g'\simeq g$ and $f$ is fixed, $g'f\simeq gf\simeq\mathrm{id}_{E_{1}}$ and $fg'\simeq fg\simeq\mathrm{id}_{E_{2}}$.
:::

:::

::: {.pf-step #lemma}
Lemma. If $p\colon E\to B$ is a fibration and $u\colon E\to E$ is fiber-preserving with $u\simeq\mathrm{id}_{E}$, then there is a fiber-preserving $a$ with $au\simeq_{B}\mathrm{id}_{E}$.

:::: pf-proof

::: {.pf-step #lemma-lift}
Let $h_{t}\colon u\simeq\mathrm{id}_{E}$. There is a homotopy $k_{t}$ with $k_{0}=\mathrm{id}_{E}$, $pk_{t}=ph_{t}$ and $k_{1}$ fiber-preserving.

::: pf-proof
Lift the homotopy $ph_{t}$ of maps $E\to B$, which starts at $ph_{0}=p=p\,\mathrm{id}_{E}$, to a homotopy starting at $\mathrm{id}_{E}$; this is the homotopy lifting property of $p$. Then $pk_{1}=ph_{1}=p$, so $k_{1}$ preserves fibres.
:::

:::

::: {.pf-step #lemma-square}
The homotopy $J$ from $k_{1}u$ to $\mathrm{id}_{E}$ obtained by concatenating $k_{1}u\simeq u$, $h_{0}=u$, $h_{1}=\mathrm{id}_{E}$ has $pJ$ homotopic rel endpoints to the constant homotopy at $p$.

::: pf-proof
$k_{1}u\simeq k_{0}u=u$ and $h$ runs from $u$ to $\mathrm{id}_{E}$, so concatenation gives $J$. The two-parameter family made of $h_{t}$ and the lifted $k_{t}$ has both boundary homotopies equal to $ph_{t}$, so it provides a homotopy from $pJ$ to the constant homotopy at $p$ fixing the end maps. This is the one step taken as the standard two-parameter bookkeeping of the dual of Proposition 0.19 rather than expanded.
:::

:::

::: {.pf-step #lemma-end}
$k_{1}u\simeq_{B}\mathrm{id}_{E}$.

::: pf-proof
Lift the two-parameter homotopy of step [](#lemma-square){.pf-ref} using the fibration property of $p$, starting from $J$; reading along the opposite boundary gives a homotopy from $k_{1}u$ to $\mathrm{id}_{E}$ over $B$. With $a=k_{1}$, fiber-preserving by step [](#lemma-lift){.pf-ref}, this is $au\simeq_{B}\mathrm{id}_{E}$.
:::

:::

::::

:::

::: {.pf-step #left-inverse}
There is a fiber-preserving $\ell\colon E_{2}\to E_{1}$ with $\ell f\simeq_{B}\mathrm{id}_{E_{1}}$.

::: pf-proof
Apply step [](#lemma){.pf-ref} to $p_{1}$ and $u=gf\colon E_{1}\to E_{1}$, which is fiber-preserving and ordinarily homotopic to $\mathrm{id}_{E_{1}}$; get a fiber-preserving $a$ with $agf\simeq_{B}\mathrm{id}_{E_{1}}$. Put $\ell=ag$, fiber-preserving as a composite of such maps; then $\ell f=agf\simeq_{B}\mathrm{id}_{E_{1}}$.
:::

:::

::: {.pf-step #ell-equiv}
$\ell$ is an ordinary homotopy equivalence.

::: pf-proof
$\ell=ag\simeq g$, and $g$ is a homotopy equivalence; a map homotopic to a homotopy equivalence is one.
:::

:::

::: {.pf-step #right-inverse}
There is a fiber-preserving $m\colon E_{1}\to E_{2}$ with $m\ell\simeq_{B}\mathrm{id}_{E_{2}}$.

::: pf-proof
Repeat the construction of steps [](#deform){.pf-ref}, [](#lemma){.pf-ref} and [](#left-inverse){.pf-ref} with $\ell$ in place of $f$: $\ell$ is fiber-preserving and an ordinary homotopy equivalence, so it has an ordinary homotopy inverse whose composite with $\ell$ can be deformed to a fiber-preserving map and then corrected by the lemma, giving $m$ with $m\ell\simeq_{B}\mathrm{id}_{E_{2}}$.
:::

:::

::: {.pf-step #conclusion}
$f\ell\simeq_{B}\mathrm{id}_{E_{2}}$ and $\ell f\simeq_{B}\mathrm{id}_{E_{1}}$.

::: pf-proof
$\ell f\simeq_{B}\mathrm{id}_{E_{1}}$ is step [](#left-inverse){.pf-ref}. For the other: $m\ell\simeq_{B}\mathrm{id}_{E_{2}}$ by step [](#right-inverse){.pf-ref}, so composing on the right with $f\ell$ gives $m\ell f\ell\simeq_{B}f\ell$, while $m\ell f\ell=m(\ell f)\ell\simeq_{B}m\ell\simeq_{B}\mathrm{id}_{E_{2}}$ using $\ell f\simeq_{B}\mathrm{id}_{E_{1}}$ and then step [](#right-inverse){.pf-ref} again. Hence $f\ell\simeq_{B}\mathrm{id}_{E_{2}}$.
:::

:::

::: {.pf-step}
$f$ is a fiber homotopy equivalence.

::: pf-proof
Step [](#conclusion){.pf-ref} exhibits the fiber-preserving $\ell$ with $\ell f\simeq_{B}\mathrm{id}_{E_{1}}$ and $f\ell\simeq_{B}\mathrm{id}_{E_{2}}$, which is the definition.
:::

:::

:::

:::
