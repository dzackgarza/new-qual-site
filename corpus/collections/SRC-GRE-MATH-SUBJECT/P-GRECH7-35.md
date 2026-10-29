---
schema: qual/card@1
id: P-GRECH7-35
kind: problem
title: Splitting twelve employees into four committees of three
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked against Question 35 of the Chapter 7 review questions in assets/attachments/extracted/Chapter-7.md (Mistral OCR), compared with the same page in the Cracking the GRE Mathematics Subject Test book extraction.
---

::: {.problem}
In how many ways can a company separate its 12 employees into 4 equally-sized committees?

(A) 369,600
(B) 184,800
(C) 61,600
(D) 384
(E) 48
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

If the four committees are distinguished, the number of assignments is
$$
\binom{12}{3}\binom{9}{3}\binom{6}{3}\binom{3}{3}
=\frac{12!}{(3!)^4}
=369{,}600.
$$


::: pf-proof

Choose the three employees for the first committee, then three of the remaining nine for the second, then three of the remaining six for the third; the last three form the fourth committee. Because the committees are distinguished, no further quotient is taken.

:::

:::

::: {.pf-step #s1-2}

If the four committees are not distinguished, the number of partitions is
$$
\frac{12!}{(3!)^4 4!}=15{,}400.
$$


::: pf-proof

The construction in step [](#s1-1){.pf-ref} orders the four three-person blocks by committee. If the committees have no labels, each partition into four blocks is counted once for each of the $4!$ permutations of its blocks. Dividing the count in step [](#s1-1){.pf-ref} by $4!$ gives
$$
\frac{369{,}600}{24}=15{,}400.
$$

:::

:::

::: {.pf-step #s1-3}

The wording “separate its 12 employees into 4 equally-sized committees” does not specify whether the four committees are distinguished, so the literal statement does not determine a unique count.


::: pf-proof

Steps [](#s1-1){.pf-ref} and [](#s1-2){.pf-ref} give different counts under the two standard conventions. The problem statement supplies no committee names, tasks, or other labels that choose between them, and $15{,}400$ is not among the answer choices.

:::

:::

::: {.pf-step #s1-4}

Under the convention explicitly used by the source solution, the answer is
$$
\boxed{369{,}600},
$$
which is choice (A).


::: pf-proof

The source solution states that it matters which committee each employee is placed into and uses exactly the distinguished-committee count proved in step [](#s1-1){.pf-ref}. Thus choice (A) is the intended answer under that convention.

:::

:::

::: pf-qed

Steps [](#s1-3){.pf-ref} and [](#s1-4){.pf-ref} record the ambiguity in the printed statement and the answer under the source's intended convention.

:::

:::

:::
