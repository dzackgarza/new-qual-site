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

::: {.solution}

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

::: {.pf-step #s1-1}

The number of distinct conjugates of $H$ is
$$
\cardinality{\mathcal C}=[G:N].
$$


::: pf-proof

The group $G$ acts on its subgroups by conjugation. The stabilizer of $H$ for this action is exactly $N_G(H)=N$. By the orbit-stabilizer theorem, the orbit of $H$, namely $\mathcal C$, has cardinality $[G:N]$.

:::

:::

::: {.pf-step #s1-2}

One has
$$
\cardinality{\mathcal C}\leq [G:H].
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
Apply step [](#s1-1){.pf-ref}.

:::

:::

::: {.pf-step #s1-3}

The union of all conjugates satisfies
$$
\cardinality{
\bigcup_{K\in\mathcal C}K
}
\leq
1+\cardinality{\mathcal C}(\cardinality{H}-1).
$$


::: pf-proof

Every $K\in\mathcal C$ is conjugate to $H$, so $\cardinality{K}=\cardinality{H}$. Also every subgroup $K$ contains the identity element $e$. Thus, after counting $e$ once, each of the $\cardinality{\mathcal C}$ conjugates can contribute at most $\cardinality{H}-1$ further elements. This gives the stated bound.

:::

:::

::: {.pf-step #s1-4}

The union of the conjugates has strictly fewer than $\cardinality{G}$ elements.


::: pf-proof

By steps [](#s1-2){.pf-ref} through [](#s1-3){.pf-ref},
$$
\begin{aligned}
\cardinality{
\bigcup_{g\in G}gHg^{-1}
}
&\leq
1+[G:H](\cardinality{H}-1)\\
&=
1+\frac{\cardinality{G}}{\cardinality{H}}(\cardinality{H}-1)\\
&=
\cardinality{G}-[G:H]+1.
\end{aligned}
$$
Since $H$ is proper, $[G:H]\geq2$. Therefore
$$
\cardinality{G}-[G:H]+1\leq \cardinality{G}-1<\cardinality{G}.
$$

:::

:::

::: {.pf-step #s1-5}

Therefore
$$
\boxed{
G\ne\bigcup_{g\in G}gHg^{-1}
}.
$$


::: pf-proof

If the union were all of $G$, its cardinality would be $\cardinality{G}$, contradicting step [](#s1-4){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} is the required conclusion.

:::

:::

:::
