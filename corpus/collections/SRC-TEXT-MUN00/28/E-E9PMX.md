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
<1>1. Definition of Countable Compactness:
<2>1. A topological space $X$ is **countably compact** if every countable open cover of $X$ has a finite subcover.
::: {.proof}
standard definition of countable compactness.
:::

<1>2. Forward direction ($\implies$): Countable compactness implies nested intersection property:
<2>1. Let $C_1 \supseteq C_2 \supseteq C_3 \supseteq \cdots$ be a nested sequence of non-empty closed subsets of $X$.
::: {.proof}
setup.
:::
<2>2. Suppose for contradiction that $\bigcap_{n=1}^\infty C_n = \emptyset$.
::: {.proof}
assumption for contradiction.
:::
<2>3. By De Morgan’s laws, the complements $U_n = X \setminus C_n$ form a countable collection of open sets satisfying:
\[
\bigcup_{n=1}^\infty U_n = \bigcup_{n=1}^\infty (X \setminus C_n) = X \setminus \left(\bigcap_{n=1}^\infty C_n\right) = X \setminus \emptyset = X.
\]
Thus $\{U_n\}_{n=1}^\infty$ is a countable open cover of $X$.
::: {.proof}
De Morgan's laws.
:::
<2>4. Since $X$ is countably compact, there exists a finite subcover: $X = U_{n_1} \cup \cdots \cup U_{n_k}$.
Let $N = \max(n_1, \dots, n_k)$.
Since the sequence $\{C_n\}$ is nested ($C_N \subseteq C_n$ for all $n \le N$), the complements are nested ($U_n \subseteq U_N$ for all $n \le N$), so:
\[
X = \bigcup_{j=1}^k U_{n_j} = U_N = X \setminus C_N.
\]
::: {.proof}
monotonicity of nested sets.
:::
<2>5. Taking complements gives $C_N = X \setminus U_N = \emptyset$, which contradicts the hypothesis that each $C_n$ is non-empty.
Thus $\bigcap_{n=1}^\infty C_n \neq \emptyset$.
::: {.proof}
proof by contradiction.
:::

<1>3. Reverse direction ($\impliedby$): Nested intersection property implies countable compactness:
<2>1. Let $\{V_n\}_{n=1}^\infty$ be an arbitrary countable open cover of $X$.
::: {.proof}
setup.
:::
<2>2. Suppose for contradiction that no finite subcollection covers $X$.
Then for every $n \ge 1$, $\bigcup_{k=1}^n V_k \neq X$.
::: {.proof}
assumption for contradiction.
:::
<2>3. Define $C_n = X \setminus \bigcup_{k=1}^n V_k$.
Each $C_n$ is non-empty and closed (as the complement of a finite union of open sets).
::: {.proof}
<2>2.
:::
<2>4. For each $n \ge 1$:
\[
C_{n+1} = X \setminus \left(\bigcup_{k=1}^{n+1} V_k\right) = \left(X \setminus \bigcup_{k=1}^n V_k\right) \setminus V_{n+1} = C_n \setminus V_{n+1} \subseteq C_n.
\]
Thus $C_1 \supseteq C_2 \supseteq C_3 \supseteq \cdots$ is a nested sequence of non-empty closed sets.
::: {.proof}
monotonicity of unions.
:::
<2>5. By the nested intersection hypothesis, there exists $x \in \bigcap_{n=1}^\infty C_n$.
::: {.proof}
hypothesis.
:::
<2>6. For this $x$, $x \in C_n = X \setminus \bigcup_{k=1}^n V_k$ for all $n \ge 1$, which means $x \notin V_k$ for all $k \ge 1$.
Thus $x \notin \bigcup_{k=1}^\infty V_k = X$, a contradiction.
::: {.proof}
$\{V_n\}$ covers $X$.
:::
<2>7. Thus some finite subcollection must cover $X$, so $X$ is countably compact.
::: {.proof}
proof by contradiction.
:::

<1>4. Conclusion:
$X$ is countably compact if and only if every nested sequence of non-empty closed sets has non-empty intersection. Q.E.D.
::: {.proof}
<1>2 and <1>3.
:::
:::
