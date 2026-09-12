---
schema: qual/card@1
id: P-ALGS08E
kind: problem
title: "Solvability by radicals for polynomials with V4 and S3 Galois groups"
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Compared both Galois-group cases with Problem 5 of the official UCSD Spring 2008 algebra qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Applied the solvability-by-radicals criterion and exhibited solvable normal series for both V4 and S3.
---

::: problem
Let $p(x)$ be a polynomial over $\mathbb{Q}$ with Galois group $\mathbb{Z}_2 \times \mathbb{Z}_2$.
What can be said about the solvability of $p(x)$ by radicals?
What if the Galois group is $S_3$?
:::

::: {.solution}
<1>1. A polynomial over $\mathbb{Q}$ is solvable by radicals if its Galois group is a solvable group.
::: {.proof}
Over a field of characteristic $0$, the Galois-theoretic criterion for solvability by radicals says that a polynomial is solvable by radicals if and only if the Galois group of its splitting field is solvable.
:::

<1>2. If the Galois group is $\mathbb{Z}_2\times\mathbb{Z}_2$, then $p(x)$ is solvable by radicals.
::: {.proof}
The group $\mathbb{Z}_2\times\mathbb{Z}_2$ is abelian, hence solvable.
For example, if $H$ is any subgroup of order $2$, then
\[
1\triangleleft H\triangleleft \mathbb{Z}_2\times\mathbb{Z}_2
\]
has abelian quotients.
By <1>1, $p(x)$ is solvable by radicals.
:::

<1>3. If the Galois group is $S_3$, then $p(x)$ is also solvable by radicals.
::: {.proof}
The alternating subgroup $A_3$ is normal in $S_3$, and
\[
1\triangleleft A_3\triangleleft S_3
\]
has quotients
\[
A_3\cong C_3,
\qquad
S_3/A_3\cong C_2.
\]
Thus $S_3$ is solvable.
By <1>1, $p(x)$ is solvable by radicals in this case as well.
:::
:::
