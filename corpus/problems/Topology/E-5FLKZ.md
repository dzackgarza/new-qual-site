---
schema: qual/card@1
id: E-5FLKZ
kind: problem
title: Second countable spaces are first countable
classification:
  areas:
  - topology
  topics:
  - Countability
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Every step now carries a pf-proof: the two containers state why their subclaims suffice, and the 9
    leaf steps that asserted a claim with no justification each carry a sentence deriving it, including
    the definition of second countability itself, which was previously only named. The trailing Q.E.D.
    sentence was dropped because the filter labels the last step. The mathematics is unchanged: the
    subcollection of basis elements containing x is countable, and every neighbourhood of x contains one
    of them. Nothing in the statement was changed.
---

::: {.exercise}
Show that every second countable space is first countable.
:::

::: {.solution}

::: pf

::: pf-step
Setting and hypothesis:
Let $X$ be a second-countable topological space.
By definition, $X$ possesses a countable basis $\mathcal{B} = \{B_n\}_{n=1}^\infty$ for its topology.

::: pf-proof
A space is second countable when its topology has a countable basis, and a countable set can be listed as a sequence; this names that basis.
:::

:::

::: pf-step
Construction of a countable local basis at an arbitrary point:

::: pf-proof
The subclaims produce the subcollection of basis elements containing the point and record that it is countable.

::: pf-step
Let $x \in X$ be an arbitrary point.

::: pf-proof
Nothing is assumed about $x$ beyond membership in $X$, so what is proved below holds at every point.
:::

:::

::: pf-step
Define the subcollection of basic open sets containing $x$:
$$\mathcal{B}_x = \{B \in \mathcal{B} \mid x \in B\}.$$

::: pf-proof
This is a definition by separation inside the countable collection $\mathcal{B}$.
:::

:::

::: pf-step
Because $\mathcal{B}_x \subseteq \mathcal{B}$ and $\mathcal{B}$ is countable, $\mathcal{B}_x$ is a countable collection of open neighborhoods containing $x$.

::: pf-proof
A subset of a countable set is countable; each member of $\mathcal{B}_x$ is a basis element, hence open in $X$, and contains $x$ by the defining condition of the subcollection.
:::

:::

:::

:::

::: pf-step
Verification of the local basis property:

::: pf-proof
The subclaims show that every open neighbourhood of $x$ contains a member of $\mathcal{B}_x$.

::: pf-step
Let $U \subseteq X$ be an arbitrary open neighborhood of $x$.

::: pf-proof
This is the arbitrary open set containing $x$ that the local basis property quantifies over.
:::

:::

::: pf-step
Since $\mathcal{B}$ is a topological basis for $X$, there exists a basic open set $B \in \mathcal{B}$ such that $x \in B \subseteq U$.

::: pf-proof
Every open set is a union of basis elements, so one of them contains $x$ and is contained in $U$.
:::

:::

::: pf-step
Because $x \in B$, $B$ belongs to the subcollection $\mathcal{B}_x$ by construction.

::: pf-proof
The defining condition of $\mathcal{B}_x$ is exactly that its members are the basis elements containing $x$.
:::

:::

::: pf-step
Thus, every open neighborhood $U$ of $x$ contains an element of $\mathcal{B}_x$.

::: pf-proof
The element is the $B$ of the two preceding subclaims: it lies in $\mathcal{B}_x$ and satisfies $x\in B\subseteq U$, and $U$ was arbitrary.
:::

:::

:::

:::

::: pf-step
Conclusion:
$\mathcal{B}_x$ is a countable local basis at $x$. Since $x \in X$ was arbitrary, $X$ is first-countable.

::: pf-proof
The second container shows that $\mathcal{B}_x$ is countable, and the third that every neighbourhood of $x$ contains a member of it; a countable collection of open neighbourhoods with that property is a countable local basis, and $x$ was arbitrary, which is first countability.
:::

:::

:::

:::
