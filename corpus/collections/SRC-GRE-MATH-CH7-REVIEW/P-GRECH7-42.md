---
schema: qual/card@1
id: P-GRECH7-42
kind: problem
title: Lebesgue measure of $(-1,3]\cup[7,8)$
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Checked against Question 42 of the Chapter 7 review questions in assets/attachments/extracted/Chapter-7.md (Mistral OCR), compared with the same page in the Cracking the GRE Mathematics Subject Test book extraction.
---

::: {.problem}
If $M=(-1,3]\cup[7,8)$, what is the Lebesgue measure of $M$?

(A) $-5$
(B) $-1$
(C) $0$
(D) $5$
(E) $9$
:::

::: {.solution}
<1>1. The two intervals in $M$ are disjoint and have lengths $4$ and $1$.

::: {.proof}
The interval $(-1,3]$ has Lebesgue measure
$$
3-(-1)=4,
$$
and $[7,8)$ has measure
$$
8-7=1.
$$
They are disjoint because $3<7$.
:::

<1>2. Therefore
$$
\boxed{m(M)=5},
$$
so the answer is (D).

::: {.proof}
Lebesgue measure is finitely additive on disjoint measurable sets. By step <1>1,
$$
m(M)=m((-1,3])+m([7,8))=4+1=5.
$$
The inclusion or exclusion of interval endpoints does not affect their measure because singletons have measure zero.
:::

<1>3. Q.E.D.

::: {.proof}
Step <1>2 gives the requested measure.
:::
:::
