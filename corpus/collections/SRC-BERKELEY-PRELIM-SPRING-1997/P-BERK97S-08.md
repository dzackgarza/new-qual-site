---
schema: qual/card@1
id: P-BERK97S-08
kind: problem
title: Classify abelian groups of order $80$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-23
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-23
---

::: {.problem}
Classify all abelian groups of order $80$ up to isomorphism.
:::

::: {.solution}
For a finite abelian group $G$, write $G_{(p)}$ for its $p$-primary
subgroup.

<1>1. If $G$ is an abelian group of order $80=2^4\cdot 5$, then
$$
G\cong G_{(2)}\times G_{(5)},
$$
where $\abs{G_{(2)}}=16$ and $G_{(5)}\cong \ZZ/5\ZZ$.

::: {.proof}
This is the primary decomposition from the fundamental theorem of finite
abelian groups. The $5$-primary part has order $5$, hence is cyclic.
:::

<1>2. The possibilities for the $2$-primary part are exactly
$$
\ZZ/16\ZZ,\qquad
\ZZ/8\ZZ\times\ZZ/2\ZZ,\qquad
\ZZ/4\ZZ\times\ZZ/4\ZZ,
$$
$$
\ZZ/4\ZZ\times(\ZZ/2\ZZ)^2,\qquad
(\ZZ/2\ZZ)^4.
$$

::: {.proof}
By the fundamental theorem of finite abelian groups, the isomorphism types
of abelian groups of order $2^4$ correspond to the partitions of $4$:
$$
4,\qquad 3+1,\qquad 2+2,\qquad 2+1+1,\qquad 1+1+1+1.
$$
These give precisely the five groups displayed in the claim.
:::

<1>3. Therefore the abelian groups of order $80$, up to isomorphism, are
exactly
$$
\boxed{
\begin{gathered}
\ZZ/16\ZZ\times\ZZ/5\ZZ,\\
\ZZ/8\ZZ\times\ZZ/2\ZZ\times\ZZ/5\ZZ,\\
\ZZ/4\ZZ\times\ZZ/4\ZZ\times\ZZ/5\ZZ,\\
\ZZ/4\ZZ\times(\ZZ/2\ZZ)^2\times\ZZ/5\ZZ,\\
(\ZZ/2\ZZ)^4\times\ZZ/5\ZZ.
\end{gathered}
}
$$

::: {.proof}
Step <1>1 reduces the classification to the $2$-primary part together with
the unique $5$-primary part, and step <1>2 lists every possible
$2$-primary part. The uniqueness clause in the fundamental theorem shows
that the five displayed groups are pairwise nonisomorphic.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 gives the complete classification.
:::
:::
