---
schema: qual/card@1
id: P-AGH2316NOETHINDUCT
kind: problem
title: Noetherian induction on closed subsets
classification:
  areas:
  - algebraic-geometry
  topics:
  - Noetherian Spaces
  - Induction
  - Closed Subsets
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-17
  note: Checked against the collection's Hartshorne II.3.16 statement.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-17
---

::: {.problem}
Let $X$ be a noetherian topological space and let $\mcp$ be a property of closed subsets of $X$.
Assume that for any closed subset $Y$ of $X$, if $\mcp$ holds for every proper closed subset of $Y$ then $\mcp$ holds for $Y$.
In particular, $\mcp$ must hold for the empty set.
Then $\mcp$ holds for $X$.
:::

::: {.solution}

::: pf

::: {.pf-step #noetherian-has-minimal-closed}
In a noetherian topological space, every nonempty collection of closed subsets has a minimal element under inclusion.

::: pf-proof
A topological space is noetherian exactly when every descending chain of closed subsets stabilizes.

Let $\mathcal C$ be a nonempty collection of closed subsets.  If it had no minimal element, choose
\[
Y_0\in\mathcal C.
\]
Since $Y_0$ is not minimal, choose
\[
Y_1\in\mathcal C,
\qquad
Y_1\subsetneq Y_0.
\]
Inductively one obtains a strictly descending chain
\[
Y_0\supsetneq Y_1\supsetneq Y_2\supsetneq\cdots,
\]
contradicting noetherianity.  Hence a minimal member exists.
:::

:::

::: pf-step
Suppose, for contradiction, that $\mcp$ does not hold for every closed subset of $X$.
Let
\[
\mathcal B
=
\{Y\subseteq X:Y\text{ closed and }\mcp(Y)\text{ fails}\}.
\]
Choose a minimal member
\[
Y\in\mathcal B.
\]

::: pf-proof
Under the contradictory assumption, $\mathcal B$ is nonempty.  Step [](#noetherian-has-minimal-closed){.pf-ref} therefore supplies a minimal member.
:::

:::

::: {.pf-step #proper-subsets-of-y-satisfy-p}
Every proper closed subset
\[
Z\subsetneq Y
\]
satisfies $\mcp$.

::: pf-proof
If some proper closed $Z\subsetneq Y$ failed $\mcp$, then $Z\in\mathcal B$, contradicting minimality of $Y$ in $\mathcal B$.
:::

:::

::: {.pf-step #p-holds-for-y-contradiction}
The property $\mcp$ holds for $Y$, a contradiction.

::: pf-proof
By step [](#proper-subsets-of-y-satisfy-p){.pf-ref}, $\mcp$ holds for every proper closed subset of $Y$.  The induction hypothesis stated in the problem therefore implies that $\mcp$ holds for $Y$ itself.  This contradicts $Y\in\mathcal B$.
:::

:::

::: {.pf-step #p-holds-for-x}
Hence $\mcp$ holds for every closed subset of $X$, in particular for $X$.

::: pf-proof
Step [](#p-holds-for-y-contradiction){.pf-ref} shows that the family $\mathcal B$ of counterexamples must be empty.  Since $X$ is a closed subset of itself, $\mcp(X)$ holds.
:::

:::

::: pf-qed
Step [](#p-holds-for-x){.pf-ref} is the desired conclusion.
:::

:::

:::
