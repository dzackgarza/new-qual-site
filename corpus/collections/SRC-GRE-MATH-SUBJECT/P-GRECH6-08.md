---
schema: qual/card@1
id: P-GRECH6-08
kind: problem
title: Subgroup orders forced in a group of order 12
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Re-transcribed from Chapter 6 review Question 8 in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR), compared with assets/attachments/chapter-6_extracted.md, replacing the earlier paraphrased transcription."
---

::: {.problem}
If $G$ is a group of order $12$, then $G$ must have a subgroup of all of the following orders EXCEPT

(A) $2$
(B) $3$
(C) $4$
(D) $6$
(E) $12$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Every group of order $12$ has subgroups of orders $2$, $3$, and $4$.


::: pf-proof

Since $2$ and $3$ divide $12$, Cauchy's theorem gives elements, and hence cyclic subgroups, of orders $2$ and $3$. Also $12=2^2\cdot3$, so Sylow's first theorem gives a Sylow $2$-subgroup of order $2^2=4$.

:::

:::

::: {.pf-step #s1-2}

Every group of order $12$ has a subgroup of order $12$.


::: pf-proof

The group is a subgroup of itself.

:::

:::

::: {.pf-step #s1-3}

A group of order $12$ need not have a subgroup of order $6$.


::: pf-proof

Consider $A_4$, which has order $12$. Suppose that $H\le A_4$ had order $6$. Then $H$ would have index $2$, hence would be normal, and the quotient map
$$
A_4\longrightarrow A_4/H\cong\ZZ_2
$$
would be a nontrivial homomorphism. Every $3$-cycle must map to the identity in $\ZZ_2$, because the order of its image divides both $3$ and $2$. But the $3$-cycles generate $A_4$: for example, $(123)$ and $(124)$ are $3$-cycles and their product is $(13)(24)$, and conjugating supplies the other double transpositions; together with the $3$-cycles these are all elements of $A_4$. Thus the quotient map would be trivial, a contradiction. Hence $A_4$ has no subgroup of order $6$.

:::

:::

::: {.pf-step #s1-4}

Therefore the subgroup order not forced by $\cardinality{G}=12$ is
$$
\boxed{6},
$$
so the answer is (D).


::: pf-proof

Steps [](#s1-1){.pf-ref} and [](#s1-2){.pf-ref} show that orders $2$, $3$, $4$, and $12$ are forced, while step [](#s1-3){.pf-ref} gives a group of order $12$ with no subgroup of order $6$.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} identifies the exceptional order.

:::

:::

:::
