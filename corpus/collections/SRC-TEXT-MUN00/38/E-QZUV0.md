---
schema: qual/card@1
id: E-QZUV0
kind: problem
title: The Stone--Čech compactification is maximal among compactifications
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
::: {.proof}
A compactification $Y$ of $X$ is a compact Hausdorff space containing $X$ as a dense subspace, so $i$ is continuous.
:::

<1>2. By the universal property of the Stone–Čech compactification, $i$ extends uniquely to a continuous map $g : \beta(X) \to Y$.
::: {.proof}
Every continuous map from $X$ to a compact Hausdorff space extends uniquely to a continuous map on $\beta(X)$; step <1>1 supplies such a map.
:::

<1>3. $g$ equals the identity on $X$.

::: {.proof}
By step <1>2, $g$ extends the inclusion $i$.
:::

<1>4. $g$ is surjective.

::: {.proof}
The image $g(\beta(X))$ is compact because $\beta(X)$ is compact and $g$ is continuous, so it is closed in the Hausdorff space $Y$. By step <1>3 it contains $X$, which is dense in $Y$. Hence $g(\beta(X)) = Y$.
:::

<1>5. $g$ is closed.

::: {.proof}
A closed subset of the compact space $\beta(X)$ is compact, its image under $g$ is compact, and a compact subset of the Hausdorff space $Y$ is closed.
:::

<1>6. Q.E.D.

::: {.proof}
Steps <1>2 through <1>5 show that $g : \beta(X) \to Y$ is a continuous surjective closed map equal to the identity on $X$.
:::
:::
