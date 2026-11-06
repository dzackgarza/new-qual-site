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
---

::: {.problem}
Define what a composition series is, and state what it means for a group to be simple, solvable, or nilpotent.

How are the derived and lower/upper central series defined?
What type(s) of the groups above does each series correspond to?
:::

::: {.solution}
Let $G$ be a group. A nontrivial group is \dfn{simple} if its only normal subgroups are $1$ and itself.

A \dfn{composition series} of a finite group $G$ is a subnormal series
$$G=G_0\triangleright G_1\triangleright\cdots\triangleright G_n=1$$
in which each factor $G_i/G_{i+1}$ is simple; equivalently, each $G_{i+1}$ is a maximal proper normal subgroup of $G_i$.
By the Jordan–Hölder theorem, the multiset of composition factors, up to isomorphism, does not depend on the composition series.

The \dfn{derived series} is $G^{(0)}=G$, $G^{(i+1)}=[G^{(i)},G^{(i)}]$, and $G$ is \dfn{solvable} if $G^{(n)}=1$ for some $n$.
Each $G^{(i)}/G^{(i+1)}$ is abelian; conversely, if $G=H_0\trianglerighteq H_1\trianglerighteq\cdots\trianglerighteq H_r=1$ has abelian factors, induction gives $G^{(i)}\le H_i$, so $G^{(r)}=1$.
Thus $G$ is solvable exactly when it has a finite subnormal series with abelian factors.

The \dfn{lower central series} is $\gamma_1(G)=G$, $\gamma_{i+1}(G)=[\gamma_i(G),G]$, and the \dfn{upper central series} is $Z_0(G)=1$, $Z_{i+1}(G)/Z_i(G)=Z(G/Z_i(G))$.
The group $G$ is \dfn{nilpotent} if $\gamma_{c+1}(G)=1$ for some $c$; equivalently, $Z_c(G)=G$ for some $c$, and the least such $c$ is the same for both series, the nilpotency class.

Thus composition series record the simple factors, the derived series detects solvability, and the lower and upper central series detect nilpotence.
Every nilpotent group is solvable, since $G^{(i)}\le\gamma_{i+1}(G)$; the converse fails for $S_3$, which is solvable with trivial center.
:::
