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
---

::: problem
State and prove the Jordan-Holder theorem for finite groups.
:::

::: solution
**Jordan--Hölder theorem.** If
\[
1=G_0\triangleleft G_1\triangleleft\cdots\triangleleft G_m=G
\]
and
\[
1=H_0\triangleleft H_1\triangleleft\cdots\triangleleft H_n=G
\]
are composition series of a finite group $G$, then $m=n$ and, after reordering, the factors $G_i/G_{i-1}$ are isomorphic to the factors $H_j/H_{j-1}$.

We prove this by induction on $|G|$. The result is trivial for $G=1$. Let
\[
M=G_{m-1},\qquad N=H_{n-1}.
\]
These are maximal proper normal subgroups of $G$.

If $M=N$, apply induction to the two composition series of $M$ obtained by deleting the final term $G$; adjoining the common simple factor $G/M$ proves the result.

Assume $M\ne N$. Since $MN$ is a normal subgroup properly containing $M$, maximality gives $MN=G$; similarly $M\cap N$ is proper in both $M$ and $N$. The second isomorphism theorem gives
\[
G/M\cong N/(M\cap N),\qquad
G/N\cong M/(M\cap N).
\]
Choose a composition series of $M\cap N$. Extending it to $M$ and to $N$ using the two displayed simple quotients gives composition series of $M$ and $N$. By induction, the original composition series of $M$ has the same factors as this refined series of $M$, and likewise for $N$.

Consequently the factors below $M\cap N$ agree, while the two remaining factors are exchanged by
\[
G/M\cong N/(M\cap N),\qquad
G/N\cong M/(M\cap N).
\]
Thus the two composition series of $G$ have the same multiset of composition factors, and hence the same length.
:::
