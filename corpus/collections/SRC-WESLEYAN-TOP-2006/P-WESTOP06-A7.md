---
schema: qual/card@1
id: P-WESTOP06-A7
kind: problem
title: A locally compact dense subspace of a Hausdorff space is open
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-14}
---

::: {.problem}
Prove that if $X$ is locally compact and dense in a Hausdorff space $Y$, then $X$ is open in $Y$.
:::

::: {.solution}
<1>1. For every \(x\in X\), there is an open set \(U\subseteq X\) with \(x\in U\) such that \(\overline U^{\,X}\) is compact.

::: {.proof}
Because \(Y\) is Hausdorff, its subspace \(X\) is Hausdorff. In a locally compact Hausdorff space, every point has an open neighborhood with compact closure. Apply this to \(x\in X\).
:::

<1>2. If \(K=\overline U^{\,X}\), then \(K\) is closed in \(Y\).

::: {.proof}
By step <1>1, \(K\) is compact as a subspace of \(X\). The inclusion \(X\hookrightarrow Y\) is continuous, so \(K\) is compact as a subspace of \(Y\). Since \(Y\) is Hausdorff, every compact subset of \(Y\) is closed.
:::

<1>3. There is an open set \(V\subseteq Y\) such that
\[
x\in V
\qquad\text{and}\qquad
V\subseteq K\subseteq X.
\]

::: {.proof}
Since \(U\) is open in the subspace \(X\), there is an open set \(V\subseteq Y\) with
\[
U=V\cap X.
\]
Because \(X\) is dense in \(Y\), the set \(V\cap X\) is dense in \(V\). Indeed, every nonempty open subset of \(V\) is also open in \(Y\) and therefore meets \(X\).

By construction,
\[
V\cap X=U\subseteq K.
\]
Step <1>2 shows that \(K\) is closed in \(Y\), so it contains the closure in \(Y\) of \(V\cap X\). Since \(V\cap X\) is dense in \(V\),
\[
V\subseteq \overline{V\cap X}^{\,Y}\subseteq K.
\]
Also \(x\in U=V\cap X\), so \(x\in V\). Thus \(x\in V\subseteq K\subseteq X\).
:::

<1>4. \(X\) is open in \(Y\).

::: {.proof}
By step <1>3, every \(x\in X\) lies in an open subset \(V\) of \(Y\) contained in \(X\). Hence \(X\) is the union of open subsets of \(Y\), so \(X\) is open in \(Y\).
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is the required conclusion.
:::
:::
