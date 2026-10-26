---
schema: qual/card@1
id: P-BKS21-9A
kind: problem
title: A finite group is not the union of conjugates of a proper subgroup
classification:
  areas:
  - prelim
  topics:
  - Abstract Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: {.problem}
Let $G$ be finite and $H<G$ proper. Show that
$$
G\ne\bigcup_{g\in G}gHg^{-1}.
$$
:::

Let
$$
N\coloneqq N_G(H)
=
\{g\in G:gHg^{-1}=H\},
$$
and let
$$
\mathcal C\coloneqq\{gHg^{-1}:g\in G\}
$$
be the set of distinct conjugates of $H$.

::: pf

::: pf-step

The number of distinct conjugates of $H$ is
$$
|\mathcal C|=[G:N].
$$


::: pf-proof

The group $G$ acts on its subgroups by conjugation. The stabilizer of $H$ for this action is exactly $N_G(H)=N$. By the orbit-stabilizer theorem, the orbit of $H$, namely $\mathcal C$, has cardinality $[G:N]$.

:::

:::

::: pf-step

One has
$$
|\mathcal C|\leq [G:H].
$$


::: pf-proof

Since every element of $H$ normalizes $H$,
$$
H\subseteq N.
$$
Hence
$$
[G:N]\leq [G:H].
$$
Apply step <1>1.

:::

:::

::: pf-step

The union of all conjugates satisfies
$$
\left|
\bigcup_{K\in\mathcal C}K
\right|
\leq
1+|\mathcal C|(|H|-1).
$$


::: pf-proof

Every $K\in\mathcal C$ is conjugate to $H$, so $|K|=|H|$. Also every subgroup $K$ contains the identity element $e$. Thus, after counting $e$ once, each of the $|\mathcal C|$ conjugates can contribute at most $|H|-1$ further elements. This gives the stated bound.

:::

:::

::: pf-step

The union of the conjugates has strictly fewer than $|G|$ elements.


::: pf-proof

By steps <1>2--<1>3,
$$
\begin{aligned}
\left|
\bigcup_{g\in G}gHg^{-1}
\right|
&\leq
1+[G:H](|H|-1)\\
&=
1+\frac{|G|}{|H|}(|H|-1)\\
&=
|G|-[G:H]+1.
\end{aligned}
$$
Since $H$ is proper, $[G:H]\geq2$. Therefore
$$
|G|-[G:H]+1\leq |G|-1<|G|.
$$

:::

:::

::: pf-step

Therefore
$$
\boxed{
G\ne\bigcup_{g\in G}gHg^{-1}
}.
$$


::: pf-proof

If the union were all of $G$, its cardinality would be $|G|$, contradicting step <1>4.

:::

:::

::: pf-qed

Step <1>5 is the required conclusion.

:::

:::
