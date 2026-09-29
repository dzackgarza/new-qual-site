---
schema: qual/card@1
id: E-E9PMX
kind: problem
title: Nested closed sets in countably compact spaces
classification:
  areas:
  - topology
  topics:
  - Compactness
relations: []
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
review: draft
---

::: {.exercise}

Show that $X$ is countably compact if and only if every nested sequence $C_1 \supset C_2 \supset \cdots$ of closed nonempty sets of $X$ has a nonempty intersection.
:::

::: {.solution}

::: pf

::: pf-step
Definition of Countable Compactness:

::: pf-proof

::: pf-step
A topological space $X$ is **countably compact** if every countable open cover of $X$ has a finite subcover.

::: pf-proof
standard definition of countable compactness.
:::

:::

:::

:::

::: {.pf-step #forward-direction}
Forward direction ($\implies$): Countable compactness implies nested intersection property:

::: pf-proof

::: pf-step
Let $C_1 \supseteq C_2 \supseteq C_3 \supseteq \cdots$ be a nested sequence of non-empty closed subsets of $X$.

::: pf-proof
setup.
:::

:::

::: pf-step
Suppose for contradiction that $\bigcap_{n=1}^\infty C_n = \emptyset$.

::: pf-proof
assumption for contradiction.
:::

:::

::: pf-step
By De Morgan’s laws, the complements $U_n = X \setminus C_n$ form a countable collection of open sets satisfying:
\[
\bigcup_{n=1}^\infty U_n = \bigcup_{n=1}^\infty (X \setminus C_n) = X \setminus \left(\bigcap_{n=1}^\infty C_n\right) = X \setminus \emptyset = X.
\]
Thus $\{U_n\}_{n=1}^\infty$ is a countable open cover of $X$.

::: pf-proof
De Morgan's laws.
:::

:::

::: pf-step
Since $X$ is countably compact, there exists a finite subcover: $X = U_{n_1} \cup \cdots \cup U_{n_k}$.
Let $N = \max(n_1, \dots, n_k)$.
Since the sequence $\{C_n\}$ is nested ($C_N \subseteq C_n$ for all $n \le N$), the complements are nested ($U_n \subseteq U_N$ for all $n \le N$), so:
\[
X = \bigcup_{j=1}^k U_{n_j} = U_N = X \setminus C_N.
\]

::: pf-proof
monotonicity of nested sets.
:::

:::

::: pf-step
Taking complements gives $C_N = X \setminus U_N = \emptyset$, which contradicts the hypothesis that each $C_n$ is non-empty.
Thus $\bigcap_{n=1}^\infty C_n \neq \emptyset$.

::: pf-proof
proof by contradiction.
:::

:::

:::

:::

::: {.pf-step #reverse-direction}
Reverse direction ($\impliedby$): Nested intersection property implies countable compactness:

::: pf-proof

::: pf-step
Let $\{V_n\}_{n=1}^\infty$ be an arbitrary countable open cover of $X$.

::: pf-proof
setup.
:::

:::

::: {.pf-step #assume-no-finite-subcover}
Suppose for contradiction that no finite subcollection covers $X$.
Then for every $n \ge 1$, $\bigcup_{k=1}^n V_k \neq X$.

::: pf-proof
assumption for contradiction.
:::

:::

::: pf-step
Define $C_n = X \setminus \bigcup_{k=1}^n V_k$.
Each $C_n$ is non-empty and closed (as the complement of a finite union of open sets).

::: pf-proof
Step [](#assume-no-finite-subcover){.pf-ref}.
:::

:::

::: pf-step
For each $n \ge 1$:
\[
C_{n+1} = X \setminus \left(\bigcup_{k=1}^{n+1} V_k\right) = \left(X \setminus \bigcup_{k=1}^n V_k\right) \setminus V_{n+1} = C_n \setminus V_{n+1} \subseteq C_n.
\]
Thus $C_1 \supseteq C_2 \supseteq C_3 \supseteq \cdots$ is a nested sequence of non-empty closed sets.

::: pf-proof
monotonicity of unions.
:::

:::

::: pf-step
By the nested intersection hypothesis, there exists $x \in \bigcap_{n=1}^\infty C_n$.

::: pf-proof
hypothesis.
:::

:::

::: pf-step
For this $x$, $x \in C_n = X \setminus \bigcup_{k=1}^n V_k$ for all $n \ge 1$, which means $x \notin V_k$ for all $k \ge 1$.
Thus $x \notin \bigcup_{k=1}^\infty V_k = X$, a contradiction.

::: pf-proof
$\{V_n\}$ covers $X$.
:::

:::

::: pf-step
Thus some finite subcollection must cover $X$, so $X$ is countably compact.

::: pf-proof
proof by contradiction.
:::

:::

:::

:::

::: pf-step
Conclusion:
$X$ is countably compact if and only if every nested sequence of non-empty closed sets has non-empty intersection. Q.E.D.

::: pf-proof
Steps [](#forward-direction){.pf-ref} and [](#reverse-direction){.pf-ref}.
:::

:::

:::

:::
