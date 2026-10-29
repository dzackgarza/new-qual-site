---
schema: qual/card@1
id: P-HHEF6
kind: problem
title: Jordan–Hölder theorem
classification:
  areas:
  - algebra
  topics:
  - Subgroup Series
  - Simple Groups
  - Classification
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: Source printed "Jordan-Holder"; the statement now reads "Jordan--Hölder".
---

::: {.problem}

State and prove the Jordan--Hölder theorem for finite groups.

:::

::: {.solution}

The Jordan--Hölder theorem states: if
$$
1=G_0\triangleleft G_1\triangleleft\cdots\triangleleft G_m=G
\quad\text{and}\quad
1=H_0\triangleleft H_1\triangleleft\cdots\triangleleft H_n=G
$$
are composition series of a finite group $G$, then $m=n$ and the multisets of isomorphism classes of the factors $G_i/G_{i-1}$ and $H_j/H_{j-1}$ agree. We prove it by induction on $\abs{G}$; the case $G=1$ is trivial. Let $M=G_{m-1}$ and $N=H_{n-1}$. Since $G/M$ and $G/N$ are simple, $M$ and $N$ are maximal proper normal subgroups of $G$.

::: pf

::: pf-step

If $M=N$, the theorem holds for $G$.

::: pf-proof

Deleting the final term $G$ gives two composition series of $M$. By induction they have the same length and factors; adjoining the common factor $G/M$ gives the result for $G$.

:::

:::

::: {.pf-step #iso}

If $M\ne N$, then $MN=G$ and
$$
G/M\cong N/(M\cap N),\qquad G/N\cong M/(M\cap N).
$$

::: pf-proof

The product $MN$ of normal subgroups is normal. Since $M$ and $N$ are distinct maximal proper normal subgroups, $N\not\subseteq M$, so $MN$ properly contains $M$ and maximality gives $MN=G$. The second isomorphism theorem gives $MN/M\cong N/(M\cap N)$ and $MN/N\cong M/(M\cap N)$.

:::

:::

::: pf-qed

Assume $M\ne N$. Choose a composition series of $M\cap N$. By step [](#iso){.pf-ref}, $M/(M\cap N)$ and $N/(M\cap N)$ are simple, so appending $M$, respectively $N$, gives composition series of $M$ and $N$. By induction, the series $G_0,\ldots,G_{m-1}$ of $M$ has the same length and factors as this series of $M$, whose factors are those of $M\cap N$ together with $M/(M\cap N)\cong G/N$. Likewise the series $H_0,\ldots,H_{n-1}$ of $N$ has the factors of $M\cap N$ together with $N/(M\cap N)\cong G/M$. Adjoining $G/M$ to the first and $G/N$ to the second, both composition series of $G$ have the factors of $M\cap N$ together with $G/M$ and $G/N$. Hence they have the same factors and the same length.

:::

:::

:::
