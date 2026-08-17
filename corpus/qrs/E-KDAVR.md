---
schema: qual/card@1
id: E-KDAVR
kind: exercise
title: "Show that if $X$ is compact and $A\\subseteq X$ is closed then $A$ is compact."
classification:
  areas:
  - topology
  topics:
  - compactness
relations: []
review: draft
---

::: exercise
Show that if $X$ is compact and $A\subseteq X$ is closed then $A$ is compact.
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** Show that if $X$ is compact and $A \subseteq X$ is closed, then $A$ is compact.

<1>1. Let $\theset{U_\alpha}$ be an open cover of $A$.
    Proof: Arbitrary open cover of $A$ (by open subsets of $X$).

<1>2. $X \setminus A$ is open in $X$.
    Proof: $A$ is closed.

<1>3. $\theset{U_\alpha} \cup \theset{X \setminus A}$ is an open cover of $X$.
    Proof: On $A$, the $U_\alpha$ cover; on $X \setminus A$, the set $X \setminus A$ covers.

<1>4. There is a finite subcover of $X$: some $U_{\alpha_1}, \ldots, U_{\alpha_n}$ together with (possibly) $X \setminus A$.
    Proof: $X$ is compact and <1>3 is an open cover.

<1>5. $\theset{U_{\alpha_1}, \ldots, U_{\alpha_n}}$ is a finite cover of $A$.
    Proof: The finite subcover from <1>4 covers $A$ after discarding $X \setminus A$ (which contains no points of $A$); the remaining $U_{\alpha_j}$ still cover $A$ since any $a \in A$ lies in one of the subcover members, which must be a $U_{\alpha_j}$ because $a \notin X \setminus A$.

<1>6. Q.E.D.
    Proof: <1>1--<1>5 show every open cover of $A$ has a finite subcover.

:::
