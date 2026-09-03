---
schema: qual/card@1
id: E-MUN-9-4
kind: problem
title: Identifying implicit use of the axiom of choice
classification:
  areas:
  - topology
  topics:
  - Infinite Sets and the Axiom of Choice
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.exercise}

There was a theorem in §7 whose proof involved an infinite number of arbitrary choices.
Which one was it?
Rewrite the proof so as to make explicit the use of the choice axiom.
(Several of the earlier exercises have used the choice axiom also.)
:::

::: {.solution}
<1>1. The theorem is Theorem 7.5: a countable union of countable sets is countable.
::: {.proof}
this is the theorem in §7 whose proof requires infinitely many arbitrary choices.
:::

<1>2. The proof requires choosing, for each countable set $A_n$, an enumeration (a surjection or bijection from a subset of $\ZZ_+$ onto $A_n$).
::: {.proof}
to write $\bigcup_n A_n$ as a countable list, one must pick a specific enumeration of each $A_n$, and there are infinitely many such choices (one per $n$).
:::

<1>3. Rewritten proof making the choice explicit: let $\{A_n\}_{n \in \ZZ_+}$ be a countable family of countable sets.
::: {.proof}
setup.
:::

<1>4. By the axiom of choice, choose for each $n$ a surjection $f_n: \ZZ_+ \to A_n$.
::: {.proof}
this is the single application of the axiom of choice (a choice function on the family of nonempty sets of surjections $\ZZ_+ \to A_n$).
:::

<1>5. Define $g: \ZZ_+ \times \ZZ_+ \to \bigcup_n A_n$ by $g(n, m) = f_n(m)$.
::: {.proof}
definition.
:::

<1>6. $g$ is surjective.
::: {.proof}
every element of $\bigcup_n A_n$ lies in some $A_n$, hence is $f_n(m)$ for some $m$.
:::

<1>7. Since $\ZZ_+ \times \ZZ_+$ is countable, $\bigcup_n A_n$ is countable.
::: {.proof}
<1>6 and the countability of $\ZZ_+ \times \ZZ_+$.
:::

<1>8. Q.E.D.
::: {.proof}
<1>7; the axiom of choice is used exactly once, in <1>4.
:::
:::
