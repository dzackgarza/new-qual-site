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
<1>1. In a noetherian topological space, every nonempty collection of closed subsets has a minimal element under inclusion.
::: {.proof}
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

<1>2. Suppose, for contradiction, that $\mcp$ does not hold for every closed subset of $X$.
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
::: {.proof}
Under the contradictory assumption, $\mathcal B$ is nonempty.  Step <1>1 therefore supplies a minimal member.
:::

<1>3. Every proper closed subset
\[
Z\subsetneq Y
\]
satisfies $\mcp$.
::: {.proof}
If some proper closed $Z\subsetneq Y$ failed $\mcp$, then $Z\in\mathcal B$, contradicting minimality of $Y$ in $\mathcal B$.
:::

<1>4. The property $\mcp$ holds for $Y$, a contradiction.
::: {.proof}
By <1>3, $\mcp$ holds for every proper closed subset of $Y$.  The induction hypothesis stated in the problem therefore implies that $\mcp$ holds for $Y$ itself.  This contradicts $Y\in\mathcal B$.
:::

<1>5. Hence $\mcp$ holds for every closed subset of $X$, in particular for $X$.
::: {.proof}
Step <1>4 shows that the family $\mathcal B$ of counterexamples must be empty.  Since $X$ is a closed subset of itself, $\mcp(X)$ holds.
:::

<1>6. Q.E.D.
::: {.proof}
Step <1>5 is the desired conclusion.
:::
:::
