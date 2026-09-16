---
schema: qual/card@1
id: E-LS2QW
kind: problem
title: The Stone-Cech construction is a functor
classification:
  areas:
  - topology
  topics:
  - Compactness
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}

We have constructed a correspondence $X \to \beta(X)$ that assigns, to each completely regular space, its Stone-Čech compactification.
Now let us assign, to each continuous map $f: X \to Y$ of completely regular spaces, the unique continuous map $\beta(f): \beta(X) \to \beta(Y)$ that extends the map $i \circ f$, where $i: Y \to \beta(Y)$ is the inclusion map.
Verify the following:

(i) If $\mathsf{l}_X: X \to X$ is the identity map of $X$, then $\beta(\mathsf{l}_X)$ is the identity map of $\beta(X)$.

(ii) If $f: X \to Y$ and $g: Y \to Z$, then $\beta(g \circ f) = \beta(g) \circ \beta(f)$.

These properties tell us that the correspondence we have constructed is what is called a functor; it is a functor from the "category" of completely regular spaces and continuous maps of such spaces, to the "category" of compact Hausdorff spaces and continuous maps of such spaces.
:::

::: {.solution}
Let \(i_X:X\hookrightarrow\beta X\) denote the canonical embedding.

(i) Both \(\beta(\mathsf l_X)\) and \(\mathsf l_{\beta X}\) are continuous maps \(\beta X\to\beta X\) whose restriction to the dense subspace \(X\) is \(i_X\). By uniqueness in the Stone--Čech extension property,
\[
\beta(\mathsf l_X)=\mathsf l_{\beta X}.
\]

(ii) Let \(f:X\to Y\) and \(g:Y\to Z\). The maps
\[
\beta(g\circ f),\qquad \beta(g)\circ\beta(f):\beta X\longrightarrow\beta Z
\]
are continuous. For \(x\in X\),
\[
(\beta(g)\circ\beta(f))(i_X(x))
 =\beta(g)(i_Y(f(x)))
 =i_Z(g(f(x))),
\]
which is also the value of \(\beta(g\circ f)\) at \(i_X(x)\). Since \(X\) is dense in \(\beta X\) and \(\beta Z\) is Hausdorff, two continuous maps \(\beta X\to\beta Z\) agreeing on \(X\) agree everywhere. Therefore
\[
\beta(g\circ f)=\beta(g)\circ\beta(f).
\]
Thus \(\beta\) preserves identities and composition, so it is a functor.
:::
