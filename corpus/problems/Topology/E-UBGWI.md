---
schema: qual/card@1
id: E-UBGWI
kind: problem
title: The closure is the smallest closed set containing $A$
classification:
  areas:
  - topology
  topics:
  - Closure
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: exercise
Let $X$ be a topological space and $A \subseteq X$ an arbitrary subset.
Prove that the topological closure $\operatorname{cl}_X(A)$ (or $\overline{A}$) is the smallest closed subset of $X$ containing $A$:
$$\overline{A} = \bigcap \{F \subseteq X \mid F \text{ is closed and } A \subseteq F\}.$$
:::

::: solution
Let
$$
K=\bigcap\{F\subseteq X:F\text{ is closed and }A\subseteq F\}.
$$

<1>1. The set $K$ is closed and contains $A$.
::: proof
Arbitrary intersections of closed sets are closed, and every set in the intersection contains $A$.
:::

<1>2. The closure $\overline A$ is closed and contains $A$.
::: proof
Certainly $A\subseteq\overline A$. If $x\notin\overline A$, some open neighborhood of $x$ misses $A$; the same neighborhood lies in $X\setminus\overline A$. Thus $X\setminus\overline A$ is open.
:::

<1>3. Since $\overline A$ is one of the closed supersets occurring in the definition of $K$,
$$
K\subseteq\overline A.
$$
Conversely, every closed set containing $A$ contains $\overline A$, by minimality of closure under the neighborhood characterization. Hence
$$
\overline A\subseteq K.
$$
Therefore
$$
\overline A=K.
$$
:::
