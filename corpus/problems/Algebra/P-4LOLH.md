---
schema: qual/card@1
id: P-4LOLH
kind: problem
title: Noetherian rings and $\bigcap I^n$
classification:
  areas:
  - algebra
  topics:
  - Noetherian Rings
  - Ideals
  - Nakayama's Lemma
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
What is a Noetherian ring?
If $I$ is an ideal in a Noetherian ring with a unit, what is the intersection of $I^n$ over all positive integers $n$?
:::

::: solution
**Goal:** Define a Noetherian ring and characterize $\bigcap_{n=1}^\infty I^n$ via the Krull Intersection Theorem.

<1>1. Definition of a Noetherian ring:
::: {.proof}
<2>1. A ring $R$ is **Noetherian** if it satisfies any of the following equivalent conditions:
- (ACC) Every ascending chain of ideals $I_1 \subseteq I_2 \subseteq I_3 \subseteq \cdots$ eventually stabilizes (there exists $N$ such that $I_n = I_N$ for all $n \ge N$).
- Every non-empty set of ideals of $R$ has a maximal element with respect to inclusion.
- Every ideal of $R$ is finitely generated.
:::

<1>2. The Krull Intersection Theorem for general commutative Noetherian rings:
::: {.proof}
<2>1. Let $R$ be a commutative Noetherian ring and $I$ an ideal. Let $J = \bigcap_{n=1}^\infty I^n$.
<2>2. By the Artin-Rees lemma, there exists an integer $k \ge 1$ such that $I(J \cap I^k) = J \cap I^{k+1}$.
<2>3. Since $J \subseteq I^m$ for all $m$, $J \cap I^k = J$ and $J \cap I^{k+1} = J$.
<2>4. Thus $IJ = J$.
<2>5. By Nakayama's Lemma (or the determinantal trick) applied to the finitely generated ideal $J$, there exists an element $x \in I$ such that $(1 - x)J = 0$.
<2>6. Hence $J = \{a \in R \mid (1 - x)a = 0 \text{ for some } x \in I\}$.
:::

<1>3. Special Cases:
::: {.proof}
<2>1. **Domain case:** If $R$ is an integral domain and $I \ne R$ is a proper ideal, then $1 - x \ne 0$ for all $x \in I$ (since $x \in I \subsetneq R \implies x \ne 1$). Since $R$ has no zero divisors, $(1-x)a = 0 \implies a = 0$. Thus:
$$\bigcap_{n=1}^\infty I^n = (0).$$
<2>2. **Local ring case:** If $(R, \mathfrak{m})$ is a Noetherian local ring and $I \subseteq \mathfrak{m}$ is a proper ideal, then for every $x \in I \subseteq \mathfrak{m}$, the element $1 - x$ is a unit in $R$. Therefore $(1-x)J = 0 \implies J = 0$, so:
$$\bigcap_{n=1}^\infty I^n = (0).$$
:::

<1>4. Conclusion:
::: {.proof}
In general, $\bigcap_{n=1}^\infty I^n = \{a \in R \mid (1-x)a = 0 \text{ for some } x \in I\}$. In particular, if $R$ is an integral domain or a local ring and $I$ is proper, the intersection is $(0)$.
:::
:::
