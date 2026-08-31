---
schema: qual/card@1
id: E-BRPKJ
kind: exercise
title: Where a proof about closures of unions fails
classification:
  areas:
  - topology
  topics:
  - Closure
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.exercise}

Criticize the following "proof" that $\overline{\bigcup A_\alpha} \subset \bigcup \overline{A}_\alpha$: if $\ts{A_\alpha}$ is a collection of sets in $X$ and if $x \in \overline{\bigcup A_\alpha}$, then every neighborhood $U$ of $x$ intersects $\bigcup A_\alpha$.
Thus $U$ must intersect some $A_\alpha$, so that $x$ must belong to the closure of some $A_\alpha$.
Therefore, $x \in \bigcup \overline{A}_\alpha$.
:::

::: {.solution}
<1>1. The error is in the step "so that $x$ must belong to the closure of some $A_\alpha$."
::: {.proof}
the fact that each neighborhood $U$ of $x$ intersects $\bigcup A_\alpha$ only shows that each $U$ intersects *some* $A_\alpha$, but the index $\alpha$ may depend on $U$.
:::

<1>2. To conclude $x \in \overline{A_\alpha}$ for a fixed $\alpha$, one would need a single $\alpha$ such that *every* neighborhood $U$ of $x$ intersects $A_\alpha$.
::: {.proof}
definition of closure: $x \in \overline{A_\alpha}$ iff every neighborhood of $x$ meets $A_\alpha$.
:::

<1>3. The proof only establishes the weaker statement that for each $U$ there is some $\alpha(U)$ with $U \cap A_{\alpha(U)} \neq \varnothing$, which does not imply any fixed $\alpha$ works for all $U$.
::: {.proof}
the index $\alpha$ is allowed to vary with $U$.
:::

<1>4. The claimed inclusion is in fact false in general.
::: {.proof}
e.g. in $\RR$, take $A_n = \{1/n\}$ for $n \ge 1$; then $\overline{\bigcup_n A_n} = \{0\} \cup \{1/n : n \ge 1\}$, while $\bigcup_n \overline{A_n} = \{1/n : n \ge 1\}$, so $0 \in \overline{\bigcup A_n}$ but $0 \notin \bigcup \overline{A_n}$.
:::

<1>5. Q.E.D.
::: {.proof}
<1>1–<1>4 identify the flaw and give a counterexample.
:::
:::
