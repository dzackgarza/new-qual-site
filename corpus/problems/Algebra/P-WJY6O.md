---
schema: qual/card@1
id: P-WJY6O
kind: problem
title: Nilpotent groups are solvable
classification:
  areas:
  - algebra
  topics:
  - Nilpotent Groups
  - Solvable Groups
relations: []
review: draft
audit:
  - event: solution-reviewed
    by: claude
    date: 2026-11-18
    note: >-
      Restructured into numbered steps, and the audit list this card lacked is created here. The collection is a qualifying examination compilation, so the statement is the source and the argument is the card's own. Each step re-read: the induction G^(i) <= gamma_{i+1}(G) is carried out with the monotonicity of the commutator in both variables, and the card now states that monotonicity explicitly, since the earlier prose passed from [G^(i),G^(i)] to gamma_{i+2}(G) in one step; and the conclusion is read off at i = c. The failure of the converse, with S_3 as the example, is recorded as a remark and not used. Not claimed: any statement about solvable non-nilpotent groups beyond that example.
---

::: {.problem}
Show that every nilpotent group is solvable.
:::

::: {.solution}
The argument is the card's own; the collection is a qualifying examination compilation, so the statement is the source.

::: pf

::: {.pf-step #lower}
The lower central series is $\gamma_{1}(G)=G$, $\gamma_{i+1}(G)=[\gamma_{i}(G),G]$, and $G$ is nilpotent when $\gamma_{c+1}(G)=1$ for some $c$.

::: pf-proof
This is the definition of nilpotence used here; the hypothesis of the exercise supplies such a $c$.
:::

:::

::: {.pf-step #derived}
The derived series is $G^{(0)}=G$, $G^{(i+1)}=[G^{(i)},G^{(i)}]$, and $G$ is solvable when $G^{(n)}=1$ for some $n$.

::: pf-proof
This is the definition of solvability; what has to be shown is that the nilpotence hypothesis forces the derived series to terminate.
:::

:::

::: {.pf-step #compare}
$G^{(i)}\le\gamma_{i+1}(G)$ for every $i\ge0$.

::: pf-proof
Induction on $i$. For $i=0$: $G^{(0)}=G=\gamma_{1}(G)$. For the step, if $G^{(i)}\le\gamma_{i+1}(G)$ then
$$
G^{(i+1)}=[G^{(i)},G^{(i)}]\le[G^{(i)},G]=\gamma_{i+2}(G),
$$
using monotonicity of the commutator in each variable: $[H,K]\le[H',K']$ whenever $H\le H'$ and $K\le K'$. The last inclusion is the inductive hypothesis $G^{(i)}\le\gamma_{i+1}(G)$ applied in the first variable, together with $\gamma_{i+2}(G)=[\gamma_{i+1}(G),G]$ by definition.
:::

:::

::: {.pf-step #terminate}
$G^{(c)}=1$.

::: pf-proof
Put $i=c$ in step [](#compare){.pf-ref}: $G^{(c)}\le\gamma_{c+1}(G)=1$ by step [](#lower){.pf-ref}. A subgroup of the trivial group is trivial.
:::

:::

::: {.pf-step}
$G$ is solvable.

::: pf-proof
Step [](#terminate){.pf-ref} shows the derived series reaches $1$ at $n=c$, which is solvability by step [](#derived){.pf-ref}:
$$
\boxed{G\text{ nilpotent}\implies G^{(c)}=1\implies G\text{ solvable}.}
$$
The converse fails, $S_{3}$ being solvable with trivial centre; that is not needed here.
:::

:::

:::
:::
