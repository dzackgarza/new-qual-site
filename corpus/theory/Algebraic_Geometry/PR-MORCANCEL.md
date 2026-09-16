---
schema: qual/card@1
id: PR-MORCANCEL
kind: proposition
title: The cancellation theorem for properties of morphisms
classification:
  areas:
  - algebraic-geometry
  topics:
  - Morphisms
  - Base Change
  - Diagonal Morphism
relations:
- kind: uses
  target: D-MORLOCAL
- kind: uses
  target: D-T2J3Q
- kind: related-to
  target: PR-MORBC
review: draft
prompts:
- If $\rho \circ \pi$ has a property $P$ stable under base change and composition, when does $\pi$ have $P$?
- Why is a morphism between proper $k$-schemes proper?
---

::: {.proposition title="Cancellation"}
Let $P$ be a class of morphisms of schemes stable under base change and composition ([[D-MORLOCAL]]).
Let $\pi \colon X \to Y$ and $\rho \colon Y \to Z$ be morphisms and $\tau = \rho \circ \pi$.
If $\tau \in P$ and the diagonal $\delta_\rho \colon Y \to Y \times_Z Y$ is in $P$, then $\pi \in P$.
:::

<1>1. The graph $\Gamma_\pi = (\id_X, \pi) \colon X \to X \times_Z Y$ is the base change of $\delta_\rho$ along $\pi \times \id_Y \colon X \times_Z Y \to Y \times_Z Y$, so $\Gamma_\pi \in P$.

::: {.proof}
The square

\begin{tikzcd}
	X & {X \times_Z Y} \\
	Y & {Y \times_Z Y}
	\arrow["{\Gamma_\pi}", from=1-1, to=1-2]
	\arrow["\pi"', from=1-1, to=2-1]
	\arrow["{\pi \times \id_Y}", from=1-2, to=2-2]
	\arrow["{\delta_\rho}"', from=2-1, to=2-2]
\end{tikzcd}

is Cartesian: for a scheme $T$, a morphism $(x, y') \colon T \to X \times_Z Y$ and a morphism $y \colon T \to Y$ with $(\pi \circ x, y') = (y, y)$ are the same as a single morphism $x \colon T \to X$, with $y = y' = \pi \circ x$.
:::

<1>2. The projection $p_2 \colon X \times_Z Y \to Y$ is the base change of $\tau \colon X \to Z$ along $\rho$, so $p_2 \in P$.

::: {.proof}
$X \times_Z Y \to Y$ is by definition the base change of $X \to Z$ along $Y \to Z$.
:::

<1>3. Q.E.D.

::: {.proof}
$\pi = p_2 \circ \Gamma_\pi$ is a composite of morphisms in $P$ by steps <1>1 and <1>2.
:::

::: {.corollary}
Let $P$ be stable under base change and composition, and $\rho \circ \pi \in P$.

1. If $P$ contains all locally closed immersions, then $\pi \in P$.

2. If $P$ contains all closed immersions and $\rho$ is separated, then $\pi \in P$.

3. If $P$ contains all quasicompact morphisms and $\rho$ is quasiseparated, then $\pi \in P$.
:::

::: {.proof}
The diagonal of any morphism is a locally closed immersion, it is a closed immersion exactly when $\rho$ is separated, and it is quasicompact exactly when $\rho$ is quasiseparated ([[D-T2J3Q]]); apply the proposition.
:::

::: {.example}
Proper morphisms are stable under base change and composition and contain the closed immersions.
If $X$ and $Y$ are proper over a field $k$, with structure morphisms $\tau \colon X \to \Spec k$ and $\rho \colon Y \to \Spec k$, then every $k$-morphism $\pi \colon X \to Y$ is proper, by part 2 of the corollary, since $\rho$ is separated.
:::
