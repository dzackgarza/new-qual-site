---
schema: qual/card@1
id: P-UCLAB02W-08
kind: problem
title: Rank bounds for a composition of linear maps
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 8 of the official UCLA Basic Examination, Winter 2002 PDF. The source asks for the upper bound by the maximum of the two ranks, not the sharper standard bound by their minimum.
---

::: {.problem}
Let $T:V\to W$ and $S:W\to X$ be linear maps between finite-dimensional real vector spaces.
Prove that
\[
\operatorname{rank}(T)+\operatorname{rank}(S)-\dim W
\leq
\operatorname{rank}(S\circ T)
\leq
\max\{\operatorname{rank}(T),\operatorname{rank}(S)\}.
\]

Here the rank of a linear transformation is the dimension of its image.
:::

Let
$$
R=\operatorname{im}T\subseteq W.
$$

::: pf

::: pf-step

One has
$$
\operatorname{rank}(S\circ T)
=\dim S(R).
$$


::: pf-proof

By definition,
$$
\operatorname{im}(S\circ T)
=S(T(V))
=S(R).
$$
Taking dimensions gives the equality.

:::

:::

::: pf-step

The restriction
$$
S|_R:R\to X
$$
satisfies
$$
\dim S(R)
=\dim R-\dim(R\cap\ker S).
$$


::: pf-proof

The image of $S|_R$ is $S(R)$, and its kernel is
$$
\ker(S|_R)=R\cap\ker S.
$$
Applying the rank-nullity theorem to $S|_R$ gives the formula.

:::

:::

::: pf-step

The lower bound
$$
\operatorname{rank}(S\circ T)
\ge
\operatorname{rank}(T)+\operatorname{rank}(S)-\dim W
$$
holds.


::: pf-proof

By steps <1>1--<1>2,
$$
\operatorname{rank}(S\circ T)
=\dim R-\dim(R\cap\ker S).
$$
Since
$$
\dim(R\cap\ker S)\le\dim\ker S,
$$
one obtains
$$
\operatorname{rank}(S\circ T)
\ge
\dim R-\dim\ker S.
$$
Now
$$
\dim R=\operatorname{rank}(T),
$$
and rank-nullity for $S:W\to X$ gives
$$
\dim\ker S
=
\dim W-\operatorname{rank}(S).
$$
Substitution yields the required lower bound.

:::

:::

::: pf-step

One has
$$
\operatorname{rank}(S\circ T)
\le
\operatorname{rank}(T).
$$


::: pf-proof

By step <1>1,
$$
\operatorname{rank}(S\circ T)=\dim S(R).
$$
The image of a linear map on the finite-dimensional space $R$ has dimension at most $\dim R$. Hence
$$
\dim S(R)\le\dim R=\operatorname{rank}(T).
$$

:::

:::

::: pf-step

One also has
$$
\operatorname{rank}(S\circ T)
\le
\operatorname{rank}(S).
$$


::: pf-proof

Since
$$
\operatorname{im}(S\circ T)
=S(R)
\subseteq
S(W)=\operatorname{im}S,
$$
taking dimensions gives the inequality.

:::

:::

::: pf-step

Therefore
$$
\operatorname{rank}(S\circ T)
\le
\min\{\operatorname{rank}(T),\operatorname{rank}(S)\}
\le
\max\{\operatorname{rank}(T),\operatorname{rank}(S)\}.
$$


::: pf-proof

The first inequality is the conjunction of steps <1>4 and <1>5. The second is immediate for two real numbers.

:::

:::

::: pf-qed

Step <1>3 proves the required lower bound, and step <1>6 proves the requested upper bound.

:::

:::
