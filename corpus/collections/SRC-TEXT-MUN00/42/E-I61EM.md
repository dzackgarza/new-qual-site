---
schema: qual/card@1
id: E-I61EM
kind: problem
title: Sections of the minimal uncountable well-ordered set are second countable
classification:
  areas:
  - topology
  topics:
  - Order Topology
  - Paracompactness
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
    Checked against Munkres, Topology (2000), Section 42 Exercise 2, printed p. 262, with Theorem 42.1 (Smirnov), Theorem 28.2 (in a metrizable space limit point compactness implies compactness) and the countability of the ordinals below $\Omega$. No correction was needed; part (a) is the countability of the section and part (b) derives a contradiction by metrizing $S_\Omega$ and then compactifying it.
- event: source-corrected
  by: claude
  date: 2026-11-10
  note: >-
    Part (b) concluded non-paracompactness from the assertion that a countably compact metrizable space is
    compact, which is not one of the book's numbered results; the card now uses limit point compactness,
    which is: an infinite subset of $S_\Omega$ contains an increasing sequence whose supremum is a countable
    ordinal below $\Omega$ and is a limit point of the subset. With Theorem 28.2 (a metrizable limit point
    compact space is compact) and the cover $\{[0,\alpha)\mid\alpha<\Omega\}$, which has no finite subcover,
    the contradiction is the one the exercise asks for. Checked against Theorem 42.1 (Smirnov), Theorem 28.2
    and the countability of the ordinals below $\Omega$.
- event: source-corrected
  by: claude
  date: 2026-11-10
  note: >-
    Part (a) said that an ordered space is regular without a reference; the section $S_x$ is a well-ordered
    set in the order topology, hence normal by Theorem 32.4 and regular, which is the hypothesis the Urysohn
    metrization theorem (Theorem 34.1) needs, its countable basis being the countability of $S_x$.
---

::: {.exercise}

(a) Show that for each $x \in S_\Omega$, the section of $S_\Omega$ by $x$ has a countable basis and hence is metrizable.

(b) Conclude that $S_\Omega$ is not paracompact.
:::

::: {.solution}

The argument is the card's own, built from the book's numbered results; no complete published solution of Munkres §42 Exercise 2 was located, and the sets searched are recorded in the audit trail of the §43--§50 entry of `COMPLAINTS.md`.

Let $S_{\Omega}=[0,\Omega)$ and, for $x\in S_{\Omega}$, let $S_{x}=\{y:y<x\}$ be the section of $S_{\Omega}$ by $x$.

::: pf

::: {.pf-step #section}
(a) For each $x\in S_{\Omega}$ the section $S_{x}$ has a countable basis and is metrizable.

::: pf-proof

::: {.pf-step #countable}
$S_{x}$ is countable and its subspace topology is its order topology.

::: pf-proof
By Lemma 10.2 (printed p. 66) every section of $S_{\Omega}$ other than the one by $\Omega$ is countable, and $S_{x}=[0,x)$ is the section of $S_{\Omega}$ by its element $x$; so $S_{x}$ is countable. The set $S_{x}=[0,x)$ is a ray of the ordered set $S_{\Omega}$, hence convex, so the order topology of $S_{x}$ is the topology it inherits as a subspace (Theorem 16.4, printed p. 91).
:::

:::

::: {.pf-step #basis}
$S_{x}$ has a countable basis.

::: pf-proof
The sets $(a,b)$, $[0,b)$ and $(a,x)$ with $a,b\in S_{x}$, together with $[0,x)=S_{x}$ itself, form a basis for the order topology on $S_{x}$ (§14, printed p. 84): $S_{x}$ is well ordered with least element $0$, so the rays $[0,b)$ are the neighbourhoods of the form $[a_0,b)$ and the intervals $(a,b)$, $(a,x)$ are the remaining basic sets, and $[0,x)$ is a basis element because $S_{x}$ is open in itself. The last one is needed: if $S_{x}=\{0\}$ then $[0,b)=(a,b)=(a,x)=\varnothing$ for every admissible $a,b$, and $[0,x)=\{0\}$ is the only member of the family that is nonempty. All these sets are determined by pairs $a,b\in S_{x}$, so there are countably many of them because $S_{x}$ is countable by step [](#countable){.pf-ref}; hence $S_{x}$ is second countable.
:::

:::

::: {.pf-step #metrizable}
$S_{x}$ is metrizable.

::: pf-proof
A well-ordered set is normal in its order topology (Theorem 32.4, printed p. 202), hence regular, and $S_{x}$ is a well-ordered set in the order topology by step [](#countable){.pf-ref}; with the countable basis of step [](#basis){.pf-ref} the Urysohn metrization theorem (Theorem 34.1, printed p. 215) gives a metric for $S_{x}$ that induces its topology.
:::

:::

:::

:::

::: {.pf-step #not-paracompact}
(b) $S_{\Omega}$ is not paracompact.

::: pf-proof

::: {.pf-step #locally-metrizable}
$S_{\Omega}$ is locally metrizable.

::: pf-proof
For $x\in S_{\Omega}$ the set $[0,x+1)=S_{x+1}$ is an open neighbourhood of $x$, and by step [](#section){.pf-ref} it is metrizable. So every point of $S_{\Omega}$ has a metrizable neighbourhood.
:::

:::

::: {.pf-step #limit-point-compact}
$S_{\Omega}$ is limit point compact and not compact.

::: pf-proof
This is Example 2 of §28: an infinite $A\subset S_{\Omega}$ contains a countably infinite subset $B$, which being countable has an upper bound $b\in S_{\Omega}$; then $B\subset[a_{0},b]$, where $a_{0}=0$ is the least element of $S_{\Omega}$, and $[a_{0},b]$ is compact because $S_{\Omega}$ has the least upper bound property, so $B$ has a limit point $x\in[a_{0},b]$, compactness implying limit point compactness (Theorem 28.1), and $x$ is a limit point of $A$ as well. Hence $S_{\Omega}$ is limit point compact. It is not compact: the sets $[0,\alpha)$ for $\alpha<\Omega$ are open in the order topology, they cover $S_{\Omega}$ since $\beta\in[0,\beta+1)$, and they are nested, so a finite subcollection is contained in its largest member $[0,\alpha_{0})$, which omits $\alpha_{0}$.
:::

:::

::: {.pf-step #contradiction}
If $S_{\Omega}$ were paracompact it would be metrizable, which is impossible.

::: pf-proof
By the Smirnov metrization theorem (Theorem 42.1, printed p. 261) a space is metrizable if and only if it is a paracompact Hausdorff space that is locally metrizable. The space $S_{\Omega}$ is Hausdorff in its order topology, being a simply ordered set (Theorem 17.11), and step [](#locally-metrizable){.pf-ref} gives local metrizability; so a paracompact $S_{\Omega}$ would be metrizable. Were $S_{\Omega}$ metrizable, it would be compact by Theorem 28.2 (printed p. 179), since it is limit point compact by step [](#limit-point-compact){.pf-ref}; but step [](#limit-point-compact){.pf-ref} also shows it is not compact. So $S_{\Omega}$ is not paracompact.
:::

:::

:::

:::

:::
:::
