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
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Jesper Michael Møller, "Solutions to exercises in Munkres", file S38.pdf,
    Exercise 38.4, page 1 of the file (tmp/sources/munkres-solutions-poulsen-S38.pdf; the PDF metadata names
    Jesper Michael Møller and the sheet is dated 2 April 2005, and its section-38 items carry no
    per-exercise attribution; Internet Archive snapshot 20181222125939 of web.math.ku.dk/~moller/e02/3gt/opg/S38.pdf).
    Checked against Munkres, Topology (2000), Section 38 Exercise 4, printed p. 241. The sheet's argument
    is the one on this card: the inclusion X -> Y is a continuous map into the compact Hausdorff space Y,
    so by Theorem 38.4 it has a unique continuous extension g (Lemma 38.3 is uniqueness); a continuous map
    of the compact space beta(X) into a Hausdorff space is closed (Theorems 26.5 and 17.11); the image
    contains X, which is dense in Y, so g is onto. No correction was needed. Not checked here: nothing in
    the exercise is left out; the exercise's bracketed remark is the printed one.
---

::: {.exercise}

Let $Y$ be an arbitrary compactification of $X$; let $\beta(X)$ be the Stone-Čech compactification.
Show there is a continuous surjective closed map $g: \beta(X) \to Y$ that equals the identity on $X$.

[This exercise makes precise what we mean by saying that $\beta(X)$ is the "maximal" compactification of $X$. It shows that every compactification of $X$ is equivalent to a quotient space of $\beta(X)$.]
:::

::: {.solution}

::: pf

::: {.pf-step #inclusion-into-y}
Let $i : X \to Y$ be the inclusion of $X$ into its compactification $Y$ (a continuous map into a compact Hausdorff space).

::: pf-proof
A compactification $Y$ of $X$ is a compact Hausdorff space containing $X$ as a dense subspace, so $i$ is continuous.
:::

:::

::: {.pf-step #g-exists}
By the universal property of the Stone–Čech compactification, $i$ extends uniquely to a continuous map $g : \beta(X) \to Y$.

::: pf-proof
Every continuous map from $X$ to a compact Hausdorff space extends uniquely to a continuous map on $\beta(X)$; step [](#inclusion-into-y){.pf-ref} supplies such a map.
:::

:::

::: {.pf-step #g-extends-identity}
$g$ equals the identity on $X$.

::: pf-proof
By step [](#g-exists){.pf-ref}, $g$ extends the inclusion $i$.
:::

:::

::: pf-step
$g$ is surjective.

::: pf-proof
The image $g(\beta(X))$ is compact because $\beta(X)$ is compact and $g$ is continuous, so it is closed in the Hausdorff space $Y$. By step [](#g-extends-identity){.pf-ref} it contains $X$, which is dense in $Y$. Hence $g(\beta(X)) = Y$.
:::

:::

::: {.pf-step #g-closed}
$g$ is closed.

::: pf-proof
A closed subset of the compact space $\beta(X)$ is compact, its image under $g$ is compact, and a compact subset of the Hausdorff space $Y$ is closed.
:::

:::

::: pf-qed
Steps [](#g-exists){.pf-ref} through [](#g-closed){.pf-ref} show that $g : \beta(X) \to Y$ is a continuous surjective closed map equal to the identity on $X$.
:::

:::

:::
