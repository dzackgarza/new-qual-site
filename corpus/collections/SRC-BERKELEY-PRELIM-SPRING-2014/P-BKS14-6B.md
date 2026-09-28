---
schema: qual/card@1
id: P-BKS14-6B
kind: problem
title: Compactness of the orthogonal group
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored UC Berkeley Spring 2014 preliminary examination PDF.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked closedness of A^T A=I and the uniform Frobenius-norm bound.
---

::: {.problem}
Let $O(n)$ be the group of $n\times n$ orthogonal matrices, with the subspace topology inherited from $\RR^{n^2}$ via matrix entries.
Show that $O(n)$ is compact.
:::

::: {.solution}
Identify the vector space of real $n\times n$ matrices with
$$
\RR^{n^2}
$$
using their entries.

<1>1. The map
$$
\Phi:M_n(\RR)\longrightarrow M_n(\RR),
\qquad
\Phi(A)=A^TA
$$
is continuous.

::: {.proof}
Every entry of $A^TA$ is a polynomial in the entries of $A$. Polynomial
maps between finite-dimensional Euclidean spaces are continuous.
:::

<1>2. The orthogonal group is closed in $\RR^{n^2}$.

::: {.proof}
By definition,
$$
O(n)
=
\{A\in M_n(\RR):A^TA=I\}
=
\Phi^{-1}(\{I\}).
$$
The singleton $\{I\}$ is closed, and $\Phi$ is continuous by step <1>1.
Therefore $O(n)$ is closed.
:::

<1>3. Every matrix $A\in O(n)$ has Frobenius norm
$$
\norm{A}_{F}
=
\sqrt n.
$$

::: {.proof}
The squared Frobenius norm is
$$
\norm{A}_{F}^2
=
\operatorname{tr}(A^TA).
$$
If $A\in O(n)$, then
$$
A^TA=I.
$$
Hence
$$
\norm{A}_{F}^2
=
\operatorname{tr}(I)
=
n.
$$
:::

<1>4. The set $O(n)$ is bounded in $\RR^{n^2}$.

::: {.proof}
Step <1>3 shows that every element lies on the Euclidean sphere of radius
$\sqrt n$ in matrix-entry coordinates.
:::

<1>5. Therefore
$$
\boxed{O(n)\text{ is compact}}.
$$

::: {.proof}
By steps <1>2 and <1>4, $O(n)$ is closed and bounded in the
finite-dimensional Euclidean space $\RR^{n^2}$. The Heine--Borel theorem
therefore gives compactness.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 is the required conclusion.
:::
:::
