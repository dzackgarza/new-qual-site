---
schema: qual/card@1
id: E-MUN-4-3
kind: problem
title: Inductive sets and basic properties of $\ZZ_+$
classification:
  areas:
  - topology
  topics:
  - Integers and Real Numbers
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Munkres, Topology, 2nd ed., Chapter 1, Section 4, Exercise 3; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §4 Exercise 3, printed p. 34; (a) is the
    intersection of a collection of inductive sets and (b) asks for the basic
    properties (1) and (2) of Z_+, which are the statements proved below: Z_+ is
    inductive, and an inductive subset of Z_+ equals Z_+.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second
    Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 4.3,
    printed p. 50 (tmp/sources/munkres-solutions-whitman.pdf). His argument for (a) is
    the card's; for (b) the card reads property (1) off the definition of Z_+ as the
    intersection of all inductive subsets of R together with (a), and property (2) as
    the resulting principle of induction, which is his.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Structured both parts into numbered steps with the definition of an inductive set stated first,
    and supplied the two cases the prose left out: the empty collection in (a), whose intersection is
    the ambient space R and is inductive, and the fact that the collection of all inductive subsets
    of R is nonempty (R itself is one), which (b)(1) needs before (a) can be applied. Checked: the
    containment of 1 and the closure under x |-> x + 1, and that (b)(2) is the defining property of
    the intersection Z_+. Not re-read this session: the Whitman page and Munkres printed p. 34.
---

::: {.exercise}

(a) Show that if $\mathcal{A}$ is a collection of inductive sets, then the intersection of the elements of $\mathcal{A}$ is an inductive set.

(b) Prove the basic properties (1) and (2) of $\ZZ_{+}$ .
:::

::: {.solution}

The argument for (a) is that of **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 4.3** (`tmp/sources/munkres-solutions-whitman.pdf`); part (b) is read off the definition of $\ZZ_{+}$ as the intersection of all inductive subsets of $\RR$, with the empty-collection case and the nonemptiness of that family supplied below.

A subset $A\subset\RR$ is inductive when $1\in A$ and $x\in A$ implies $x+1\in A$. By definition $\ZZ_{+}$ is the intersection of all inductive subsets of $\RR$.

::: pf

::: {.pf-step #a}
If $\mathcal{A}$ is a nonempty collection of inductive sets, then $\bigcap_{A\in\mathcal{A}}A$ is inductive.

::: pf-proof
Each $A\in\mathcal{A}$ contains $1$, so $1$ lies in the intersection. If $x$ lies in the intersection then $x\in A$ for every $A\in\mathcal{A}$; each such $A$ is inductive, so $x+1\in A$ for every $A$, that is $x+1$ lies in the intersection.
:::

:::

::: {.pf-step #a-empty}
If $\mathcal{A}$ is empty, the intersection of its elements is $\RR$, which is inductive.

::: pf-proof
The intersection of an empty family of subsets of $\RR$ is $\RR$ by convention, since every real number satisfies the condition vacuously. $\RR$ contains $1$ and is closed under $x\mapsto x+1$, so it is inductive.
:::

:::

::: {.pf-step #family}
The collection of all inductive subsets of $\RR$ is nonempty.

::: pf-proof
$\RR$ is an inductive subset of $\RR$ by step [](#a-empty){.pf-ref}, so the collection contains at least one member.
:::

:::

::: {.pf-step #b1}
$\ZZ_{+}$ is inductive.

::: pf-proof
By step [](#family){.pf-ref} $\ZZ_{+}$ is the intersection of a nonempty collection of inductive sets, so step [](#a){.pf-ref} applies and gives that $\ZZ_{+}$ is inductive. This is property (1).
:::

:::

::: {.pf-step #b2}
If $A\subset\ZZ_{+}$ is inductive, then $A=\ZZ_{+}$.

::: pf-proof
An inductive subset of $\ZZ_{+}$ is an inductive subset of $\RR$, so it is one of the sets intersected to form $\ZZ_{+}$; hence $\ZZ_{+}\subset A$ by the definition of intersection. The hypothesis gives $A\subset\ZZ_{+}$, so the two inclusions give equality. This is property (2), the principle of induction.
:::

:::

::: {.pf-step}
Both parts hold: an intersection of inductive sets is inductive, and the two basic properties of $\ZZ_{+}$ follow from that and from the definition of $\ZZ_{+}$.

::: pf-proof
Part (a) is steps [](#a){.pf-ref} and [](#a-empty){.pf-ref}, and part (b) is steps [](#b1){.pf-ref} and [](#b2){.pf-ref}.
:::

:::

:::

:::
