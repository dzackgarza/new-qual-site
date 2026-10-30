---
schema: qual/card@1
id: P-GRECH6-16
kind: problem
title: Idempotents in $\ZZ_{20}$
classification:
  areas:
  - algebra
  topics:
  - Idempotents
  - Modular Arithmetic
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Re-transcribed from Chapter 6 review Question 16 in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR), compared with assets/attachments/chapter-6_extracted.md, replacing the earlier paraphrased transcription."
---

::: {.problem}
Let $R$ be a ring; an element $x$ in $R$ is said to be idempotent if $x^2 = x$. How many idempotent elements does the ring $\ZZ_{20}$ contain?

(A) $2$
(B) $4$
(C) $5$
(D) $8$
(E) $10$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

By the Chinese remainder theorem,
$$
\ZZ_{20}\cong\ZZ_4\times\ZZ_5,
$$
and idempotents correspond under this isomorphism.


::: pf-proof

Since $\gcd(4,5)=1$, reduction modulo $4$ and modulo $5$ gives a ring isomorphism
$$
\ZZ_{20}\longrightarrow\ZZ_4\times\ZZ_5.
$$
Ring homomorphisms preserve the equation $x^2=x$, so an element of $\ZZ_{20}$ is idempotent exactly when both of its components are idempotent.

:::

:::

::: {.pf-step #s1-2}

Each of $\ZZ_4$ and $\ZZ_5$ has exactly two idempotents, $0$ and $1$.


::: pf-proof

In either ring, idempotence is equivalent to
$$
x(x-1)=0.
$$
Modulo $5$, which is a field, this forces $x=0$ or $x=1$. Modulo $4$, the integers $x$ and $x-1$ are coprime; if $4\mid x(x-1)$, the full factor $4$ must divide one of them, so again $x\equiv0$ or $1\pmod4$.

:::

:::

::: {.pf-step #s1-3}

Hence $\ZZ_{20}$ has exactly four idempotents, represented by
$$
0,\quad1,\quad5,\quad16.
$$


::: pf-proof

Steps [](#s1-1){.pf-ref} and [](#s1-2){.pf-ref} give $2\cdot2=4$ possible pairs of idempotent components. Solving the four pairs of congruences modulo $4$ and $5$ gives respectively $0,1,5,16$ modulo $20$.

:::

:::

::: {.pf-step #s1-4}

Therefore the number of idempotents is
$$
\boxed{4},
$$
so the answer is (B).


::: pf-proof

This is the count established in step [](#s1-3){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} gives the requested number.

:::

:::

:::
