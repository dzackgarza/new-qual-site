---
schema: qual/card@1
id: P-GRECH6-15
kind: problem
title: Impossible property of a group of order 9
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
  note: "Re-transcribed from Chapter 6 review Question 15 in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR), compared with assets/attachments/chapter-6_extracted.md, replacing the earlier paraphrased transcription."
---

::: {.problem}
Let $G$ be a group of order $9$, and let $e$ denote the identity of $G$. Which one of the following statements about $G$ CANNOT be true?

(A) There exists an element $x$ in $G$ such that $x \neq e$ and $x^{-1} = x$.
(B) There exists an element $x$ in $G$ such that $x \neq e$ and $x^2 = x^5$.
(C) There exists an element $x$ in $G$ such that $\langle x \rangle$ has order $3$.
(D) $G$ is cyclic.
(E) $G$ is Abelian.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

No group of order $9$ can contain a nonidentity element $x$ satisfying $x^{-1}=x$.


::: pf-proof

If $x^{-1}=x$, then multiplying by $x$ gives $x^2=e$. Since $x\ne e$, the order of $x$ would therefore be $2$. The cyclic subgroup $\langle x\rangle$ would have order $2$, contradicting Lagrange's theorem because $2\nmid9$.

:::

:::

::: {.pf-step #s1-2}

Each of statements (B)--(E) can hold for a group of order $9$.


::: pf-proof

Take the additive group $G=\ZZ_9$. It is cyclic and Abelian, so (D) and (E) hold. The element $\overline3$ generates the subgroup
$$
\{\overline0,\overline3,\overline6\},
$$
which has order $3$, so (C) holds. In additive notation, the equation $x^2=x^5$ becomes $2x=5x$; for $x=\overline3\ne\overline0$,
$$
2\overline3=\overline6=5\overline3,
$$
so (B) also holds.

:::

:::

::: {.pf-step #s1-3}

Therefore the statement that cannot be true is
$$
\boxed{\text{(A)}},
$$
namely the existence of a nonidentity element satisfying $x^{-1}=x$.


::: pf-proof

Step [](#s1-1){.pf-ref} proves that (A) is impossible for every group of order $9$, while step [](#s1-2){.pf-ref} exhibits a group of order $9$ for which each of (B)--(E) is true.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} identifies the required statement.

:::

:::

:::
