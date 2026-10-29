---
schema: qual/card@1
id: P-TRIV-LA21
kind: problem
title: No commutator of real matrices is a nonzero multiple of the identity
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Linear Algebra, Problem 21, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: The source asks to prove [A, B] != cE for c in R, which fails for c = 0 when A and B commute. The statement now requires c != 0.
---

::: {.problem}
Consider the linear transformations $A$, $B$ of the vector space $\RR^{n}$, $n \geq 1$. Prove that $[A, B] \neq cE$, where $E$ is the identity matrix and $c \in \RR$, $c \neq 0$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For any two $n\times n$ matrices $A$ and $B$,
$$
\operatorname{Tr}(AB)=\operatorname{Tr}(BA).
$$


::: pf-proof

Writing entries,
$$
\operatorname{Tr}(AB)
=
\sum_{i=1}^n\sum_{j=1}^n a_{ij}b_{ji}.
$$
Interchanging the dummy indices $i$ and $j$ gives
$$
\sum_{j=1}^n\sum_{i=1}^n b_{ji}a_{ij}
=
\operatorname{Tr}(BA).
$$

:::

:::

::: {.pf-step #s1-2}

Every commutator has trace zero:
$$
\operatorname{Tr}[A,B]=0.
$$


::: pf-proof

By definition,
$$
[A,B]=AB-BA.
$$
Therefore, using step [](#s1-1){.pf-ref},
$$
\operatorname{Tr}[A,B]
=
\operatorname{Tr}(AB)-\operatorname{Tr}(BA)
=0.
$$

:::

:::

::: {.pf-step #s1-3}

If
$$
[A,B]=cI,
$$
then
$$
cn=0.
$$


::: pf-proof

Take traces and use step [](#s1-2){.pf-ref}:
$$
0
=
\operatorname{Tr}[A,B]
=
\operatorname{Tr}(cI)
=
cn.
$$

:::

:::

::: {.pf-step #s1-4}

Over $\RR$, if $n\geq1$, the equality
$$
[A,B]=cI
$$
forces
$$
c=0.
$$


::: pf-proof

Since $n$ is a positive integer, it is nonzero in $\RR$. Thus step
[](#s1-3){.pf-ref} implies $c=0$.

:::

:::

::: {.pf-step #s1-5}

Therefore no commutator of real matrices can be a nonzero scalar
multiple of the identity:
$$
\boxed{[A,B]\neq cI\quad\text{for every }c\neq0.}
$$


::: pf-proof

If such an equality held, step [](#s1-4){.pf-ref} would force $c=0$, a contradiction.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} is the required conclusion.

:::

:::

:::
