---
schema: qual/card@1
id: P-GRECH6-12
kind: problem
title: Abelian groups of order $p^2q^4$
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
  note: "Re-transcribed from Chapter 6 review Question 12 in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR), compared with assets/attachments/extracted/chapter-6.md, replacing the earlier paraphrased transcription."
---

::: {.problem}
Let $p$ and $q$ be distinct primes. How many (mutually nonisomorphic) Abelian groups are there of order $p^2 q^4$?

(A) $6$
(B) $8$
(C) $10$
(D) $12$
(E) $16$
:::

::: {.solution}
<1>1. There are exactly two isomorphism types of Abelian groups of order $p^2$.

::: {.proof}
By the classification theorem for finite Abelian groups, the isomorphism types of Abelian $p$-groups of order $p^2$ correspond to the partitions of $2$. The partitions are
$$
2,
\qquad
1+1,
$$
giving $\ZZ_{p^2}$ and $\ZZ_p\oplus\ZZ_p$.
:::

<1>2. There are exactly five isomorphism types of Abelian groups of order $q^4$.

::: {.proof}
The partitions of $4$ are
$$
4,
\quad
3+1,
\quad
2+2,
\quad
2+1+1,
\quad
1+1+1+1.
$$
By the same classification theorem, these give exactly five Abelian $q$-groups of order $q^4$, up to isomorphism.
:::

<1>3. The choices of the $p$-primary and $q$-primary factors are independent, so there are $2\cdot5=10$ isomorphism types of Abelian groups of order $p^2q^4$.

::: {.proof}
For an Abelian group $G$ of order $p^2q^4$, primary decomposition gives
$$
G\cong G_{(p)}\oplus G_{(q)},
$$
where $|G_{(p)}|=p^2$ and $|G_{(q)}|=q^4$. These primary subgroups are determined intrinsically as the elements of prime-power order for the respective primes, so two such direct sums are isomorphic exactly when their $p$-primary factors are isomorphic and their $q$-primary factors are isomorphic. Steps <1>1 and <1>2 therefore give $2\cdot5=10$ possibilities.
:::

<1>4. Hence the number of mutually nonisomorphic Abelian groups is
$$
\boxed{10},
$$
so the answer is (C).

::: {.proof}
This is the count established in step <1>3.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 gives the requested number.
:::
:::
