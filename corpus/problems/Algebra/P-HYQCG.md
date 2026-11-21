---
schema: qual/card@1
id: P-HYQCG
kind: problem
title: Composition series, solvability, and nilpotence
classification:
  areas:
  - algebra
  topics:
  - Subgroup Series
  - Nilpotent Groups
  - Solvable Groups
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: claude
  date: 2026-11-06
  note: >-
    Reviewed against the Lamport standard. What was found: the question asks for a
    definition (composition series), for the meanings of three adjectives, for the
    definitions of three series, and for which class of groups each series detects —
    statements throughout, so there is no proof obligation and no pf block was added.
    What was checked, by reading against a fresh derivation: the definition of simple
    and of composition series, including the equivalence of simple factors with
    maximal proper normal subgroups and the Jordan-Holder independence of the factor
    multiset; the derived series with solvability, and the claim that abelian-factor
    subnormal series characterise solvability, whose induction step (G^(i) <= H_i
    implies G^(i+1) <= [H_i, H_i] <= H_(i+1) when H_i/H_(i+1) is abelian) is correct;
    the lower and upper central series with nilpotency and the coincidence of the
    two classes; and the two concluding claims, that G^(i) <= gamma_(i+1)(G) gives
    nilpotent implies solvable (G^(i+1) = [G^(i), G^(i)] <= [gamma_(i+1), G] =
    gamma_(i+2)), and that S_3 is a solvable non-nilpotent group (A_3 is normal with
    abelian factors of order 2 and 3, while the centre is trivial and a nilpotent
    group of order 6 would have nontrivial centre). All correct. What was not checked:
    no source solution is retained for this card, so no source comparison was made,
    and none of the quoted theorems (Jordan-Holder) is proved here.
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into numbered steps. The card is a definitions-and-equivalences question from a
    qualifying examination compilation, so the question is the source and the text is the card's
    own exposition. Each step re-read: the composition-series condition on factors is equivalent to
    maximality of each term, which the step proves; Jordan-Holder is cited for independence of the
    series; the derived series has abelian factors by construction and the converse direction of
    the solvability criterion is an induction using [H_i, H_i] <= H_{i+1}; the equivalence of the
    two nilpotence conditions is stated with the induction that proves it; and nilpotent implies
    solvable from G^(i) <= gamma_{i+1}(G), with S_3 as the counterexample to the converse, its
    centre being trivial. Not claimed: any proof of Jordan-Holder or of the agreement of the
    nilpotency classes beyond the induction sketch.
---

::: {.problem}
Define what a composition series is, and state what it means for a group to be simple, solvable, or nilpotent.

How are the derived and lower/upper central series defined?
What type(s) of the groups above does each series correspond to?
:::

::: {.solution}
The argument is the card's own; the collection is a qualifying examination compilation, so the question is the source. The card is a definitions-and-equivalences question, so the steps are the definitions, the series, and the two implications between them that the question asks for.

::: pf

::: {.pf-step #simple}
Definitions: $G\ne1$ is **simple** if its only normal subgroups are $1$ and $G$; a **composition series** of a finite group $G$ is a subnormal series $G=G_{0}\triangleright G_{1}\triangleright\cdots\triangleright G_{n}=1$ whose factors $G_{i}/G_{i+1}$ are simple.

::: pf-proof
These are the definitions asked for. The condition on factors says exactly that each $G_{i+1}$ is a maximal proper normal subgroup of $G_{i}$: a normal subgroup $N$ with $G_{i+1}<N<G_{i}$ would give a nontrivial proper normal subgroup $N/G_{i+1}$ of the simple $G_{i}/G_{i+1}$.
:::

:::

::: {.pf-step #jordanholder}
The multiset of composition factors of a finite group does not depend on the series.

::: pf-proof
This is the Jordan--Hölder theorem; it is what makes the composition factors an invariant of $G$ rather than of a chosen series.
:::

:::

::: {.pf-step #derived}
The **derived series** is $G^{(0)}=G$, $G^{(i+1)}=[G^{(i)},G^{(i)}]$, and $G$ is **solvable** if $G^{(n)}=1$ for some $n$.

::: pf-proof
This is the definition. Each $G^{(i)}/G^{(i+1)}$ is abelian because $G^{(i+1)}$ contains the commutator subgroup of $G^{(i)}$, so the derived series is a subnormal series with abelian factors.
:::

:::

::: {.pf-step #solvableiff}
$G$ is solvable if and only if it has a finite subnormal series with abelian factors.

::: pf-proof
One direction is step [](#derived){.pf-ref}. Conversely let $G=H_{0}\trianglerighteq H_{1}\trianglerighteq\cdots\trianglerighteq H_{r}=1$ with abelian factors. Induction on $i$: $G^{(0)}=G=H_{0}$; if $G^{(i)}\le H_{i}$ then $G^{(i+1)}=[G^{(i)},G^{(i)}]\le[H_{i},H_{i}]\le H_{i+1}$, the last inclusion because $H_{i}/H_{i+1}$ is abelian. Hence $G^{(r)}\le H_{r}=1$.
:::

:::

::: {.pf-step #central}
The **lower central series** is $\gamma_{1}(G)=G$, $\gamma_{i+1}(G)=[\gamma_{i}(G),G]$; the **upper central series** is $Z_{0}(G)=1$ with $Z_{i+1}(G)/Z_{i}(G)=Z(G/Z_{i}(G))$. $G$ is **nilpotent** if $\gamma_{c+1}(G)=1$ for some $c$, equivalently $Z_{c}(G)=G$ for some $c$.

::: pf-proof
These are the definitions. The two conditions are equivalent and the least such $c$ agrees, since $\gamma_{i+1}(G)=1$ iff $Z_{i}(G)=G$ for each $i$: both express that $i$-fold commutators vanish, and each is proved by induction on $i$ using the identification of $Z(G/Z_{i})$ with the preimage of the centre. That common least $c$ is the nilpotency class.
:::

:::

::: {.pf-step #nilpsolv}
Every nilpotent group is solvable, and the converse fails.

::: pf-proof
$G^{(i)}\le\gamma_{i+1}(G)$ by induction: $G^{(0)}=G=\gamma_{1}(G)$, and $G^{(i+1)}=[G^{(i)},G^{(i)}]\le[G^{(i)},G]=[\gamma_{i+1}(G),G]=\gamma_{i+2}(G)$ using the inductive hypothesis in the left factor. So $\gamma_{c+1}(G)=1$ forces $G^{(c)}=1$. The converse fails for $S_{3}$: it is solvable ($1\trianglelefteq A_{3}\trianglelefteq S_{3}$ with abelian factors of orders $2$ and $3$), but its centre is trivial, so $Z_{1}(S_{3})=1$ and the upper central series never reaches $S_{3}$.
:::

:::

::: {.pf-step}
The definitions and the correspondences hold as stated.

::: pf-proof
Steps [](#simple){.pf-ref} to [](#nilpsolv){.pf-ref} give
$$
\boxed{\text{composition series}\leftrightarrow\text{simple factors};\quad \text{derived series}\leftrightarrow\text{solvable};\quad \text{lower and upper central series}\leftrightarrow\text{nilpotent};\quad \text{nilpotent}\implies\text{solvable}.}
$$
The two series detect genuinely different classes: solvability permits the abelian factors of $S_{3}$, nilpotence requires the centre to grow.
:::

:::

:::
:::
