---
schema: qual/card@1
id: E-AMD-DLD6LYAM
kind: problem
title: Groups of order $12$ with a normal subgroup of order $4$ are isomorphic to
  $A_4$
classification:
  areas:
  - algebra
  topics:
  - Classification
  - Normal Subgroups
  - Sylow Theory
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.exercise}
Show that if $\cardinality{G} = 12$ and $G$ is a non-abelian group with a normal subgroup of order $4$ (or equivalently, $n_3 = 4$), then $G \cong A_4$.
:::

::: {.solution}

The argument is the card's own: the counting that produces a unique Sylow $2$-subgroup, the splitting $G=V\rtimes P$, and the elimination of $V\cong C_{4}$.

Let $\abs{G}=12$ and let $n_{3}$ be the number of Sylow $3$-subgroups.

::: pf

::: {.pf-step #equivalent}
The two hypotheses are equivalent: $n_{3}=4$ holds if and only if $G$ has a normal subgroup of order $4$.

::: pf-proof
Suppose $n_{3}=4$. Distinct Sylow $3$-subgroups, being of prime order $3$, meet only in the identity, so the four of them contain $4\cdot(3-1)=8$ elements of order $3$. The remaining $12-8=4$ elements are the identity and the elements of order $2$ or $4$; every Sylow $2$-subgroup has $4$ elements, all of order $1,2$ or $4$, so it is contained in that set of $4$ elements and hence equals it. So there is a unique Sylow $2$-subgroup of order $4$, and a unique Sylow subgroup is normal. Conversely, if $G$ has a normal subgroup of order $4$ then $G\cong A_{4}$ by the argument below, and the eight $3$-cycles of $A_{4}$ give $n_{3}=4$.
:::

:::

::: {.pf-step #split}
If $V\trianglelefteq G$ has order $4$ and $P\in\Syl_{3}(G)$, then $G=VP\cong V\rtimes P$.

::: pf-proof
$V\cap P$ has order dividing both $4$ and $3$, so it is trivial, and
$$
\abs{VP}=\frac{\abs{V}\abs{P}}{\abs{V\cap P}}=\frac{4\cdot3}{1}=12=\abs{G},
$$
so $VP=G$. Since $V\trianglelefteq G$ and $V\cap P=1$, the group is the semidirect product $V\rtimes P$ with $P$ acting on $V$ by conjugation.
:::

:::

::: {.pf-step #not-cyclic}
$V\not\cong C_{4}$, hence $V\cong V_{4}$.

::: pf-proof
A group of order $4$ is $C_{4}$ or $V_{4}$. If $V\cong C_{4}$ then $\Aut(V)\cong C_{2}$, and every homomorphism $P\cong C_{3}\to C_{2}$ is trivial because $\gcd(3,2)=1$; so the action is trivial and $G\cong C_{4}\times C_{3}\cong C_{12}$, which is abelian, contradicting the hypothesis that $G$ is non-abelian. Hence $V\cong V_{4}$.
:::

:::

::: {.pf-step #action}
The conjugation action $P\to\Aut(V_{4})\cong S_{3}$ has image of order $3$, and the resulting semidirect product is unique up to isomorphism.

::: pf-proof
If the action were trivial then $G\cong V_{4}\times C_{3}$ would be abelian, so the image is a nontrivial subgroup of $S_{3}$ of order dividing $3$, that is the unique subgroup $A_{3}$ of order $3$, which acts cyclically on the three nonidentity elements of $V_{4}$. Any two nontrivial homomorphisms $C_{3}\to S_{3}$ have this same image, and they differ by composing with an element of $A_{3}\subseteq S_{3}=\Aut(V_{4})$, so the corresponding semidirect products are isomorphic; since $\gcd(3,4)=1$, the extension splits with vanishing cohomology and the isomorphism class depends only on the action up to this equivalence. So there is exactly one non-abelian possibility, $V_{4}\rtimes C_{3}$.
:::

:::

::: {.pf-step #a4}
$A_{4}$ realizes this semidirect product, so $G\cong A_{4}$.

::: pf-proof
In $A_{4}$ the subgroup $V=\{1,(12)(34),(13)(24),(14)(23)\}$ has order $4$, consists of the identity and the three double transpositions, and is normal because it is the union of conjugacy classes; conjugation by the $3$-cycle $(123)$ permutes the three double transpositions in a $3$-cycle. So $A_{4}\cong V_{4}\rtimes C_{3}$ with the action of step [](#action){.pf-ref}, and by the uniqueness there $G\cong A_{4}$.
:::

:::

:::
:::
