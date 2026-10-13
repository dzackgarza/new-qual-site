---
schema: qual/card@1
id: P-AMH-ALG-SG16-07
kind: problem
title: The product $NH$ of a normal subgroup and a subgroup is a subgroup
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored Amherst College Study Guide for Algebra (September 2016).
---

::: {.problem}
(February 2013) Let $G$ be a group, let $H\subseteq G$ be a subgroup, and let $N\trianglelefteq G$ be a normal subgroup.
Define
\[
NH=\{xh:x\in N\text{ and }h\in H\}.
\]
Prove that $NH$ is a subgroup of $G$.
:::

::: {.solution}
<1>1. The set $NH$ is nonempty.
::: {.proof}
Since $e\in N$ and $e\in H$,
$$
e=ee\in NH.
$$
:::

<1>2. The set $NH$ is closed under products.
::: {.proof}
Take
$$
x=n_1h_1,
\qquad
y=n_2h_2
$$
in $NH$, with $n_1,n_2\in N$ and $h_1,h_2\in H$. Then
$$
\begin{aligned}
xy
&=n_1h_1n_2h_2\\
&=n_1(h_1n_2h_1^{-1})h_1h_2.
\end{aligned}
$$
Because $N\trianglelefteq G$,
$$
h_1n_2h_1^{-1}\in N.
$$
Hence
$$
n_1(h_1n_2h_1^{-1})\in N
$$
and
$$
h_1h_2\in H,
$$
so $xy\in NH$.
:::

<1>3. The set $NH$ is closed under inverses.
::: {.proof}
Let
$$
x=nh\in NH
$$
with $n\in N$ and $h\in H$. Then
$$
x^{-1}
=h^{-1}n^{-1}
=(h^{-1}n^{-1}h)h^{-1}.
$$
Normality of $N$ gives
$$
h^{-1}n^{-1}h\in N,
$$
and $h^{-1}\in H$. Hence $x^{-1}\in NH$.
:::

<1>4. Therefore
$$
\boxed{NH\le G}.
$$
::: {.proof}
Step <1>1 gives nonemptiness, step <1>2 gives closure under products, and step <1>3 gives closure under inverses. Hence $NH$ is a subgroup of $G$.
:::

<1>5. Q.E.D.
::: {.proof}
Step <1>4 is the required conclusion.
:::
:::
