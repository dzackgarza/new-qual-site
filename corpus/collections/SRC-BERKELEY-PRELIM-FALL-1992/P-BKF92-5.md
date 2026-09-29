---
schema: qual/card@1
id: P-BKF92-5
kind: problem
title: Intersecting with a finite-index subgroup preserves finite index
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: >-
    Injected the left cosets of K intersection H in K into the left cosets of
    H in G.
---

::: {.problem}
Let $G$ be a group and let $H,K\le G$. Suppose $H$ has finite index in $G$. Prove that
\[
K\cap H
\]
has finite index in $K$.
:::

::: {.solution}

::: pf

::: pf-step

Define
$$
\Phi:K/(K\cap H)\longrightarrow G/H
$$
on left cosets by
$$
\Phi\bigl(k(K\cap H)\bigr)=kH.
$$

::: pf-proof

This gives a candidate map from the set of left cosets of $K\cap H$ in $K$ to the set of left cosets of $H$ in $G$.

:::

:::

::: pf-step

The map $\Phi$ is well-defined.

::: pf-proof

Suppose
$$
k_1(K\cap H)=k_2(K\cap H).
$$
Then
$$
k_2^{-1}k_1\in K\cap H\subseteq H,
$$
so
$$
k_1H=k_2H.
$$
Thus the value of $\Phi$ depends only on the coset.

:::

:::

::: {.pf-step #s3}

The map $\Phi$ is injective.

::: pf-proof

Suppose
$$
\Phi\bigl(k_1(K\cap H)\bigr)
=
\Phi\bigl(k_2(K\cap H)\bigr).
$$
Then $k_1H=k_2H$, so
$$
k_2^{-1}k_1\in H.
$$
Since $k_1,k_2\in K$, one also has $k_2^{-1}k_1\in K$. Hence
$$
k_2^{-1}k_1\in K\cap H,
$$
which means
$$
k_1(K\cap H)=k_2(K\cap H).
$$

:::

:::

::: {.pf-step #s4}

The index $[K:K\cap H]$ is finite.

::: pf-proof

By step [](#s3){.pf-ref},
$$
[K:K\cap H]
=
\abs{K/(K\cap H)}
\le
\abs{G/H}
=
[G:H].
$$
The right-hand side is finite by hypothesis. Therefore
$$
\boxed{[K:K\cap H]<\infty}.
$$

:::

:::

::: pf-qed

Step [](#s4){.pf-ref} is the required conclusion.

:::

:::

:::
