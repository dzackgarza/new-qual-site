---
schema: qual/card@1
id: P-AMD-XBBANZ2H
kind: problem
title: $N_G(N_G(P))=N_G(P)$
classification:
  areas:
  - algebra
  topics:
  - Sylow Theory
  - Centralizers and Normalizers
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: >-
    Checked against UCSD Math 200A Fall 2016 Homework 4, Exercise 2(b). Restored
    the inherited source hypotheses that G is finite and P is a Sylow
    p-subgroup of G.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: >-
    Set H=N_G(P) and K=N_G(H). Then P normal H and H normal K. Exercise 2(a)
    gives P normal K, so every element of K normalizes P and K≤H. The reverse
    inclusion H≤N_G(H)=K is automatic, giving equality.
---

::: {.problem}
Let $G$ be finite and let
\[
P\in\operatorname{Syl}_p(G).
\]
Prove that
\[
N_G(N_G(P))=N_G(P).
\]
:::

::: {.solution}
Set
\[
H=N_G(P)
\qquad\text{and}\qquad
K=N_G(H).
\]

<1>1. We have $P\normal H$.
::: {.proof}
By definition,
\[
H=N_G(P)=\{g\in G:gPg^{-1}=P\}.
\]
Thus every element of $H$ conjugates $P$ to itself, which is exactly
\[
P\normal H.
\]
:::

<1>2. We have $H\normal K$.
::: {.proof}
By definition,
\[
K=N_G(H)=\{g\in G:gHg^{-1}=H\}.
\]
Hence
\[
H\normal K.
\]
:::

<1>3. We have $P\normal K$.
::: {.proof}
The subgroup chain is
\[
P\le H\le K\le G.
\]
The subgroup $P$ is Sylow in $G$, while <1>1 and <1>2 give
\[
P\normal H\normal K.
\]
By the Sylow-normality result of Exercise 2(a), it follows that
\[
P\normal K.
\]
:::

<1>4. We have $K\le H$.
::: {.proof}
By <1>3, every $k\in K$ satisfies
\[
kPk^{-1}=P.
\]
Thus every $k\in K$ lies in the normalizer of $P$, so
\[
K\le N_G(P)=H.
\]
:::

<1>5. We have $H\le K$.
::: {.proof}
Every subgroup normalizes itself: for $h\in H$,
\[
hHh^{-1}=H.
\]
Hence
\[
H\le N_G(H)=K.
\]
:::

<1>6. Therefore
\[
N_G(N_G(P))=N_G(P).
\]
::: {.proof}
Steps <1>4 and <1>5 give $K=H$.
Substituting the definitions of $H$ and $K$ gives the required equality.
:::
:::
