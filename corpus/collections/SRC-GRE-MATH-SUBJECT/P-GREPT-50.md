---
schema: qual/card@1
id: P-GREPT-50
kind: problem
title: "Number of abelian groups of order $72$"
classification:
  areas: [algebra]
  topics:
  - Finite Abelian Groups
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Transcribed from Question 50 of the Practice Test (Chapter 9) in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR)."
---

::: {.problem}
How many structurally distinct Abelian groups have order $72$?

(A) $4$
(B) $6$
(C) $8$
(D) $9$
(E) $12$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Since
$$
72=2^3\cdot3^2,
$$
every finite Abelian group $G$ of order $72$ is uniquely a direct product
$$
G\cong G_{(2)}\times G_{(3)},
$$
where $\cardinality{G_{(2)}}=2^3$ and $\cardinality{G_{(3)}}=3^2$.


::: pf-proof

This is the primary decomposition in the fundamental theorem of finite
Abelian groups: the subgroups of elements of prime-power order are the unique
Sylow primary components, and their direct product is the whole group.

:::

:::

::: {.pf-step #s1-2}

There are exactly three Abelian groups of order $2^3$ up to
isomorphism:
$$
\ZZ_8,
\qquad
\ZZ_4\times\ZZ_2,
\qquad
\ZZ_2\times\ZZ_2\times\ZZ_2.
$$


::: pf-proof

By the classification theorem, such groups correspond to partitions of the
exponent $3$. The partitions
$$
3,
\qquad
2+1,
\qquad
1+1+1
$$
give exactly the three displayed groups.

:::

:::

::: {.pf-step #s1-3}

There are exactly two Abelian groups of order $3^2$ up to isomorphism:
$$
\ZZ_9
\qquad\text{and}\qquad
\ZZ_3\times\ZZ_3.
$$


::: pf-proof

The partitions of $2$ are $2$ and $1+1$, and the classification theorem
gives exactly the two displayed groups.

:::

:::

::: {.pf-step #s1-4}

Therefore the number of Abelian groups of order $72$ up to isomorphism
is
$$
3\cdot2=\boxed{6},
$$
so the answer is (B).


::: pf-proof

By step [](#s1-1){.pf-ref}, an isomorphism type is determined uniquely by choosing one of
the three $2$-primary types from step [](#s1-2){.pf-ref} and one of the two $3$-primary
types from step [](#s1-3){.pf-ref}. Hence there are $3\cdot2=6$ choices.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} gives the requested number of isomorphism classes.

:::

:::

:::
