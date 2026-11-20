---
schema: qual/card@1
id: E-MUN-3-3
kind: problem
title: A symmetric transitive relation need not be reflexive
classification:
  areas:
  - topology
  topics:
  - Relations
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §3 Exercise 3, printed p. 28. The exercise
    prints the bogus argument about a relation C that is symmetric and transitive
    implying aCa, and asks for the flaw; the card states the argument as printed and
    answers it.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second
    Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 3.3,
    printed pp. 19-20 (tmp/sources/munkres-solutions-whitman.pdf). The diagnosis - the
    argument needs a b with aCb, so it proves only that a is related to itself when it
    is related to something - and the four-element counterexample are his.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Structured the transcribed answer into numbered steps, separating the valid implication
    (symmetry then transitivity give aCa from aCb) from the universal quantifier reflexivity
    demands, and verifying the three properties of the four-element example one by one. All
    mathematics is the earlier reading's; the counterexample is unchanged. Not re-read this
    session: the Whitman pages, and the printed page 28 of Munkres recorded in the source-check.
---

::: {.exercise}

Here is a "proof" that every relation $C$ that is both symmetric and transitive is also reflexive: "Since $C$ is symmetric, $aCb$ implies $bCa$. Since $C$ is transitive, $aCb$ and $bCa$ together imply $aCa$, as desired." Find the flaw in this argument.
:::

::: {.solution}

The diagnosis and the counterexample are those of **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 3.3** (`tmp/sources/munkres-solutions-whitman.pdf`); the quantifier analysis and the three verifications are written out below.

Throughout, $C$ is a relation on a set $A$, so $aCb$ means $(a,b)\in C$; $C$ is symmetric if $aCb$ implies $bCa$, transitive if $aCb$ and $bCc$ imply $aCc$, and reflexive if $aCa$ for every $a\in A$.

::: pf

::: {.pf-step #derivation}
If $aCb$ holds and $C$ is symmetric and transitive, then $aCa$ holds.

::: pf-proof
Symmetry applied to $aCb$ gives $bCa$; transitivity applied to the pair $aCb$, $bCa$ (with the common middle term $b$) gives $aCa$.
:::

:::

::: {.pf-step #what-it-proves}
The argument therefore establishes $\forall a\,\bigl(\exists b\colon aCb\ \Rightarrow\ aCa\bigr)$, and nothing more.

::: pf-proof
Step [](#derivation){.pf-ref} is a derivation with the hypothesis $aCb$, so what it yields is the implication "if $a$ is $C$-related to some $b$, then $aCa$". The variable $b$ is bound by that hypothesis: no choice of $b$ is produced and none is needed, but the implication says nothing about an $a$ for which no such $b$ exists.
:::

:::

::: {.pf-step #reflexivity}
Reflexivity of $C$ is the statement $\forall a\in A\colon aCa$, with no hypothesis on $a$.

::: pf-proof
This is the definition of a reflexive relation: every element of $A$ is related to itself. In particular an element related to nothing is still required to satisfy $aCa$.
:::

:::

::: {.pf-step #gap}
Step [](#what-it-proves){.pf-ref} does not yield step [](#reflexivity){.pf-ref}: the argument is valid as far as it goes and stops short of the universal statement, so the "proof" has a gap rather than a false step.

::: pf-proof
The implication of step [](#what-it-proves){.pf-ref} has the hypothesis $\exists b\colon aCb$; discharging it to obtain $aCa$ for an arbitrary $a$ would require producing such a $b$, which the hypotheses on $C$ do not supply. So the argument proves the weaker statement "every element that is related to something is related to itself", and the passage to "every element is related to itself" is the flaw.
:::

:::

::: {.pf-step #example-symmetric}
With $A=\{1,2,3,4\}$ and $C=\{(i,j)\mid i,j\in\{1,2,3\}\}$, the relation $C$ is symmetric.

::: pf-proof
$(i,j)\in C$ holds exactly when $i,j\in\{1,2,3\}$, a condition symmetric in $i$ and $j$; hence $(i,j)\in C$ if and only if $(j,i)\in C$, which is symmetry.
:::

:::

::: {.pf-step #example-transitive}
$C$ is transitive.

::: pf-proof
Let $iCj$ and $jCk$. Then $i,j,k\in\{1,2,3\}$, so $i,k\in\{1,2,3\}$ and therefore $iCk$.
:::

:::

::: {.pf-step #example-not-reflexive}
$C$ is not reflexive.

::: pf-proof
The element $4$ lies in $A$, but $(4,4)\notin C$ because $4\notin\{1,2,3\}$. So $4C4$ fails and $C$ is not reflexive.
:::

:::

::: {.pf-step}
The printed argument is flawed and its conclusion is false: a symmetric transitive relation need not be reflexive.

::: pf-proof
Steps [](#example-symmetric){.pf-ref}, [](#example-transitive){.pf-ref} and [](#example-not-reflexive){.pf-ref} exhibit a symmetric transitive non-reflexive relation on a four-element set, so the implication "symmetric and transitive implies reflexive" fails; the element $4$ of the example is related to nothing, which is precisely the case step [](#gap){.pf-ref} identified as unreachable by the printed argument.
:::

:::

:::

:::
