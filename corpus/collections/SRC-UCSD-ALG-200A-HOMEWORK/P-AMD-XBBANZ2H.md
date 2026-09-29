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

::: pf

::: {.pf-step #p-normal-h}
We have $P\normal H$.

::: pf-proof
By definition,
\[
H=N_G(P)=\{g\in G:gPg^{-1}=P\}.
\]
Thus every element of $H$ conjugates $P$ to itself, which is exactly
\[
P\normal H.
\]
:::

:::

::: {.pf-step #h-normal-k}
We have $H\normal K$.

::: pf-proof
By definition,
\[
K=N_G(H)=\{g\in G:gHg^{-1}=H\}.
\]
Hence
\[
H\normal K.
\]
:::

:::

::: {.pf-step #p-normal-k}
We have $P\normal K$.

::: pf-proof
The subgroup chain is
\[
P\le H\le K\le G.
\]
The subgroup $P$ is Sylow in $G$, while steps [](#p-normal-h){.pf-ref} and [](#h-normal-k){.pf-ref} give
\[
P\normal H\normal K.
\]
By the Sylow-normality result of Exercise 2(a), it follows that
\[
P\normal K.
\]
:::

:::

::: {.pf-step #k-le-h}
We have $K\le H$.

::: pf-proof
By step [](#p-normal-k){.pf-ref}, every $k\in K$ satisfies
\[
kPk^{-1}=P.
\]
Thus every $k\in K$ lies in the normalizer of $P$, so
\[
K\le N_G(P)=H.
\]
:::

:::

::: {.pf-step #h-le-k}
We have $H\le K$.

::: pf-proof
Every subgroup normalizes itself: for $h\in H$,
\[
hHh^{-1}=H.
\]
Hence
\[
H\le N_G(H)=K.
\]
:::

:::

::: pf-step
Therefore
\[
N_G(N_G(P))=N_G(P).
\]

::: pf-proof
Steps [](#k-le-h){.pf-ref} and [](#h-le-k){.pf-ref} give $K=H$.
Substituting the definitions of $H$ and $K$ gives the required equality.
:::

:::

:::
:::
