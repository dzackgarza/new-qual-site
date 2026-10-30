---
schema: qual/card@1
id: P-BKS17-9A
kind: problem
title: Bell numbers grow slower than $n!$
classification:
  areas:
  - prelim
  topics:
  - Abstract Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Restored the lost arrow in P_n/n! -> 0 and inline-math spacing against Sp17_Exam_0.pdf page 10 problem 9A.
- event: source-checked
  by: chatgpt
  date: 2026-10-02
  note: Independently reviewed the supplied Berkeley Spring 2017 recurrence argument. The recurrence is correct; the solution below makes explicit why the running maximum is bounded and therefore why the displayed estimate forces convergence to zero.
- event: solution-written
  by: chatgpt
  date: 2026-10-02
- event: solution-reviewed
  by: chatgpt
  date: 2026-10-02
  note: Verified the Bell-number recurrence by the block containing 1, the normalized recurrence, the running-maximum estimate, and the final squeeze.
---

::: {.problem}
The Bell number $P_n$ is the number of partitions of a set of $n$ elements into disjoint nonempty subsets, so for example $\{1, 2, 3\} = \{1\} \cup \{2\} \cup \{3\} = \{1, 2\} \cup \{3\} = \{2, 3\} \cup \{1\} = \{1, 3\} \cup \{2\}$ and $P_3 = 5$. Show that

$$
\frac{P_n}{n!} \to 0
$$

as $n \to \infty$.
:::

::: {.solution}

Set $P_0\coloneqq1$ and
$$
Q_n\coloneqq\frac{P_n}{n!}
\qquad(n\geq0).
$$

::: pf

::: {.pf-step #s1-1}

For every $n\geq1$,
$$
P_n
=
\sum_{k=1}^n \binom{n-1}{k-1}P_{n-k}.
$$


::: pf-proof

Consider the block containing the element $1$. If this block has cardinality $k$, its other $k-1$ elements can be chosen in
$$
\binom{n-1}{k-1}
$$
ways. The remaining $n-k$ elements can then be partitioned in $P_{n-k}$ ways. Summing over the possible values $1\leq k\leq n$ counts every set partition exactly once.

:::

:::

::: {.pf-step #s1-2}

For every $n\geq0$,
$$
Q_{n+1}
=
\frac{1}{n+1}\sum_{k=0}^n\frac{Q_{n-k}}{k!}.
$$


::: pf-proof

Applying step [](#s1-1){.pf-ref} with $n+1$ in place of $n$ gives
$$
P_{n+1}
=
\sum_{k=0}^n\binom{n}{k}P_{n-k}.
$$
After division by $(n+1)!$,
$$
\begin{aligned}
Q_{n+1}
&=\sum_{k=0}^n
\frac{n!}{k!(n-k)!}\frac{P_{n-k}}{(n+1)!}\\
&=\frac{1}{n+1}\sum_{k=0}^n\frac{Q_{n-k}}{k!}.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-3}

If
$$
M_n\coloneqq\max_{0\leq j\leq n}Q_j,
$$
then $M_n=1$ for every $n\geq2$.


::: pf-proof

All $Q_j$ are nonnegative. By step [](#s1-2){.pf-ref},
$$
Q_{n+1}
\leq
\frac{M_n}{n+1}\sum_{k=0}^n\frac1{k!}
\leq
\frac{e}{n+1}M_n.
$$
For $n\geq2$, one has $e<n+1$, hence $Q_{n+1}<M_n$ whenever $M_n>0$. Therefore
$$
M_{n+1}=M_n
\qquad(n\geq2).
$$
Moreover,
$$
Q_0=1,
\qquad
Q_1=1,
\qquad
Q_2=\frac{2}{2!}=1,
$$
so $M_2=1$. Induction gives $M_n=1$ for all $n\geq2$.

:::

:::

::: {.pf-step #s1-4}

One has
$$
\boxed{\displaystyle \lim_{n\to\infty}\frac{P_n}{n!}=0}.
$$


::: pf-proof

Combining steps [](#s1-2){.pf-ref} and [](#s1-3){.pf-ref}, for every $n\geq2$,
$$
0\leq Q_{n+1}\leq\frac{e}{n+1}M_n=\frac{e}{n+1}.
$$
The right-hand side tends to $0$, so the squeeze theorem gives $Q_n\to0$. By definition of $Q_n$, this is exactly the asserted limit.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} proves the required limit.

:::

:::

:::
