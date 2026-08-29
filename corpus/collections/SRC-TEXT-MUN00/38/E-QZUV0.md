---
schema: qual/card@1
id: E-QZUV0
kind: exercise
title: The Stone-Cech compactification is maximal among compactifications
classification:
  areas:
  - topology
  topics:
  - Compactness
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: {.exercise}

Let $Y$ be an arbitrary compactification of $X$; let $\beta(X)$ be the Stone-Čech compactification.
Show there is a continuous surjective closed map $g: \beta(X) \to Y$ that equals the identity on $X$.

[This exercise makes precise what we mean by saying that $\beta(X)$ is the "maximal" compactification of $X$. It shows that every compactification of $X$ is equivalent to a quotient space of $\beta(X)$.]
:::

::: {.solution}
<1>1. Let $i : X \to Y$ be the inclusion of $X$ into its compactification $Y$ (a continuous map into a compact Hausdorff space).
Proof: setup.

<1>2. By the universal property of the Stone–Čech compactification, $i$ extends uniquely to a continuous map $g : \beta(X) \to Y$.
Proof: the universal property of $\beta(X)$ (every continuous map from $X$ to a compact Hausdorff space extends to $\beta(X)$).

<1>3. $g$ equals the identity on $X$ (it extends $i$).
Proof: <1>2.

<1>4. $g$ is surjective: $g(\beta(X))$ is compact (hence closed in $Y$), and it contains $X$ (which is dense in $Y$), so $g(\beta(X)) = Y$.
Proof: <1>2 and <1>3 (the image is closed and contains the dense subset $X$).

<1>5. $g$ is closed: a continuous map from a compact space to a Hausdorff space is closed.
Proof: <1>2 (compactness of $\beta(X)$ and Hausdorffness of $Y$).

<1>6. Hence $g : \beta(X) \to Y$ is a continuous surjective closed map equal to the identity on $X$.
Proof: <1>2–<1>5.

<1>7. Q.E.D.
Proof: <1>6.
:::
:::
