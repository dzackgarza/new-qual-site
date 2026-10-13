---
schema: qual/card@1
id: P-BKS21-2A
kind: problem
title: Nested compact connected sets have connected intersection
classification:
  areas:
  - prelim
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
- event: source-checked
  by: chatgpt
  date: 2026-10-02
  note: Independently reviewed the supplied Berkeley Spring 2021 compactness-and-separation argument. The proof is correct; the solution below makes the finite-intersection and relative-separation steps explicit.
- event: solution-written
  by: chatgpt
  date: 2026-10-02
- event: solution-reviewed
  by: chatgpt
  date: 2026-10-02
  note: Verified nonemptiness by compactness, disjoint neighborhoods of a hypothetical separation, eventual containment in those neighborhoods, and the resulting contradiction to connectedness of one $X_i$.
---

::: {.problem}
Let
$$
\cdots\subset X_2\subset X_1
$$
be a nested sequence of closed nonempty connected subsets of a compact metric space $X$. Prove that $\bigcap_{i=1}^{\infty}X_i$ is nonempty and connected.
:::

::: {.solution}
Set
$$
K\coloneqq\bigcap_{i=1}^{\infty}X_i.
$$

<1>1. The set $K$ is nonempty.

::: {.proof}
Each $X_i$ is closed in the compact space $X$, hence compact. The family $\{X_i\}$ has the finite-intersection property: because the sets are nested,
$$
X_{i_1}\cap\cdots\cap X_{i_r}
=
X_{\max\{i_1,\ldots,i_r\}},
$$
which is nonempty. Compactness of $X$ therefore implies
$$
\bigcap_{i=1}^{\infty}X_i\neq\varnothing.
$$
:::

<1>2. Suppose, for contradiction, that $K$ is disconnected. Then there are disjoint nonempty compact sets $A,B\subset K$ such that
$$
K=A\cup B,
$$
and there are disjoint open sets $U,V\subset X$ with
$$
A\subset U,
\qquad
B\subset V.
$$

::: {.proof}
If $K$ is disconnected, it has a separation $K=A\cup B$ into disjoint nonempty sets that are both open and closed in $K$. Since $K$ is closed in $X$, it is compact, and therefore the closed subsets $A$ and $B$ are compact. In a metric space, disjoint compact sets have positive distance, so they admit disjoint open neighborhoods $U$ and $V$.
:::

<1>3. Under the assumption of step <1>2, there is an index $N$ such that
$$
X_N\subset U\cup V.
$$

::: {.proof}
For each $i$, define
$$
F_i\coloneqq X_i\setminus(U\cup V).
$$
Each $F_i$ is compact, and the sequence is nested. Moreover,
$$
\bigcap_{i=1}^{\infty}F_i
=
K\setminus(U\cup V)
=\varnothing
$$
because $K=A\cup B\subset U\cup V$. If every $F_i$ were nonempty, step <1>1 applied to the nested compact sets $F_i$ would force their intersection to be nonempty. Hence some $F_N$ is empty, which is exactly $X_N\subset U\cup V$.
:::

<1>4. The containment in step <1>3 contradicts connectedness of $X_N$.

::: {.proof}
Because $A,B\subset K\subset X_N$ and $A\subset U$, $B\subset V$, both
$$
X_N\cap U
\qquad\text{and}\qquad
X_N\cap V
$$
are nonempty. They are disjoint relatively open subsets of $X_N$, and step <1>3 says their union is all of $X_N$. Thus they form a separation of $X_N$, contradicting the hypothesis that $X_N$ is connected.
:::

<1>5. Therefore $K$ is nonempty and connected.

::: {.proof}
Nonemptiness is step <1>1. Steps <1>2--<1>4 rule out disconnectedness.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 is the desired conclusion.
:::
:::
