---
schema: qual/card@1
id: P-TRIV-PR02
kind: problem
title: Birthday problem
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Probability, Problem 2, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Find the least number of students in a group such that the probability that at least two students have the same birthday is not less than $\frac { 1 } { 2 }$
:::

::: {.solution}
Assume 365 equally likely birthdays and ignore leap day.

<1>1. For $n\leq365$, the probability that all $n$ birthdays are distinct is
\[
q_n=\prod_{k=0}^{n-1}\frac{365-k}{365}.
\]

::: {.proof}
The first student may have any birthday. Conditional on the first $k$ birthdays being distinct, the next student must avoid those $k$ days, which has probability $(365-k)/365$. Multiplying these conditional probabilities gives the formula.
:::

<1>2. Hence the probability of at least one shared birthday is
\[
p_n=1-q_n.
\]

::: {.proof}
The event that at least two students share a birthday is the complement of the event that all birthdays are distinct.
:::

<1>3. For $n=22$,
\[
q_{22}\approx0.524305,
\qquad
p_{22}\approx0.475695<\frac12.
\]

::: {.proof}
Evaluate the finite product in step <1>1 through $k=21$ and use step <1>2.
:::

<1>4. For $n=23$,
\[
q_{23}\approx0.492703,
\qquad
p_{23}\approx0.507297>\frac12.
\]

::: {.proof}
From step <1>3,
\[
q_{23}=q_{22}\frac{343}{365}\approx0.492703,
\]
and step <1>2 gives $p_{23}\approx0.507297$.
:::

<1>5. Therefore the least number of students is
\[
\boxed{23}.
\]

::: {.proof}
The sequence $q_n$ is decreasing, hence $p_n=1-q_n$ is increasing. Step <1>3 shows that 22 students are insufficient, while step <1>4 shows that 23 suffice.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 establishes the required minimum.
:::
:::
