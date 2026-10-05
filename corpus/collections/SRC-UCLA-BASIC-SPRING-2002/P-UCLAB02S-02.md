---
schema: qual/card@1
id: P-UCLAB02S-02
kind: problem
title: The rationals are not a G-delta subset of the real line
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 2 of the official UCLA Basic Exam Spring 2002 PDF.
---

::: {.problem}
Show that the set $\mathbb Q$ of rational numbers in $\mathbb R$ cannot be expressed as the intersection of a countable collection of open subsets of $\mathbb R$.
:::

::: {.solution}
Suppose, for contradiction, that
\[
\mathbb Q
=
\bigcap_{n=1}^{\infty}U_n
\]
with every $U_n\subseteq\mathbb R$ open.

<1>1. Every $U_n$ is dense in $\mathbb R$.

::: {.proof}
Since
\[
\mathbb Q\subseteq U_n
\]
for every $n$, and $\mathbb Q$ is dense in $\mathbb R$,
\[
\overline{U_n}
\supseteq
\overline{\mathbb Q}
=
\mathbb R.
\]
Hence
\[
\overline{U_n}=\mathbb R.
\]
:::

<1>2. Enumerate
\[
\mathbb Q=\{q_1,q_2,\ldots\}
\]
and define
\[
V_n=\mathbb R\setminus\{q_n\}.
\]
Then every $V_n$ is open and dense.

::: {.proof}
Each singleton
\[
\{q_n\}
\]
is closed and has empty interior.
Therefore its complement is open and dense.
:::

<1>3. The intersection
\[
\bigcap_{n=1}^{\infty}(U_n\cap V_n)
\]
is nonempty.

::: {.proof}
Each
\[
U_n\cap V_n
\]
is open and dense by steps <1>1--<1>2.

Apply the Baire category theorem to the complete metric space $\mathbb R$: the intersection of countably many open dense subsets of a nonempty complete metric space is dense, hence nonempty.
Thus the displayed intersection is nonempty.
:::

<1>4. On the other hand,
\[
\bigcap_{n=1}^{\infty}(U_n\cap V_n)
=
\varnothing.
\]

::: {.proof}
Distribute the intersection:
\[
\begin{aligned}
\bigcap_{n=1}^{\infty}(U_n\cap V_n)
&=
\left(\bigcap_{n=1}^{\infty}U_n\right)
\cap
\left(\bigcap_{n=1}^{\infty}V_n\right)\\
&=
\mathbb Q
\cap
\left(
\mathbb R\setminus\mathbb Q
\right)\\
&=
\varnothing.
\end{aligned}
\]
The second equality uses the assumed representation of $\mathbb Q$ and the definition of the $V_n$.
:::

<1>5. Therefore $\mathbb Q$ is not a countable intersection of open subsets of $\mathbb R$.

::: {.proof}
Steps <1>3 and <1>4 contradict each other.
Hence the assumed representation cannot exist.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 is the required conclusion.
:::
:::
