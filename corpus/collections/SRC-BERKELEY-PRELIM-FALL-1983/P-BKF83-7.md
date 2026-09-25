---
schema: qual/card@1
id: P-BKF83-7
kind: problem
title: If $G\times G$ has exactly four normal subgroups then $G$ is simple nonabelian
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: Checked the four unavoidable normal subgroups, exclusion of proper nontrivial normal subgroups of G, and the diagonal-subgroup obstruction to abelianness.
---

::: {.problem}
Let $G$ be a finite group. Suppose $G\times G$ has exactly four normal subgroups. Prove that $G$ is simple and nonabelian.
:::

::: {.solution}
<1>1. The group $G$ is nontrivial, and the following four normal
subgroups of $G\times G$ are distinct:
$$
\{1\}\times\{1\},
\qquad
G\times\{1\},
\qquad
\{1\}\times G,
\qquad
G\times G.
$$

::: {.proof}
If $G$ were trivial, then $G\times G$ would be trivial and would have only
one normal subgroup, contrary to the hypothesis.

For nontrivial $G$, the four displayed subgroups are pairwise distinct.
Each is normal because each is a direct product of normal subgroups of the
two factors.
:::

<1>2. The group $G$ is simple.

::: {.proof}
Let
$$
N\trianglelefteq G.
$$
Then
$$
N\times\{1\}\trianglelefteq G\times G.
$$
By step <1>1, the four displayed subgroups already account for all normal
subgroups of $G\times G$. Hence $N\times\{1\}$ must be one of them.

Because its second coordinate is always $1$, it cannot equal
$\{1\}\times G$ or $G\times G$ unless $G$ is trivial, which step <1>1
excludes. Therefore
$$
N\times\{1\}
=
\{1\}\times\{1\}
\quad\text{or}\quad
N\times\{1\}
=
G\times\{1\}.
$$
Thus
$$
N=\{1\}
\quad\text{or}\quad
N=G.
$$
So $G$ has no proper nontrivial normal subgroup and is simple.
:::

<1>3. The group $G$ is nonabelian.

::: {.proof}
Suppose instead that $G$ were abelian. Then $G\times G$ would be abelian,
so every subgroup would be normal. In particular, the diagonal subgroup
$$
\Delta
\coloneqq
\{(g,g):g\in G\}
$$
would be normal.

Since $G$ is nontrivial, $\Delta$ is neither
$\{1\}\times\{1\}$ nor $G\times G$. It is also distinct from each
coordinate subgroup: if $g\ne1$, then
$$
(g,g)\in\Delta
$$
has both coordinates nontrivial, whereas elements of
$G\times\{1\}$ or $\{1\}\times G$ have one coordinate equal to $1$.
Thus $\Delta$ would be a fifth normal subgroup of $G\times G$, a
contradiction.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>2 proves that $G$ is simple, and step <1>3 proves that it is
nonabelian.
:::
:::
