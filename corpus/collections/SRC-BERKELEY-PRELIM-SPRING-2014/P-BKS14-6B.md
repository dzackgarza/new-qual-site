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

::: pf

::: {.pf-step #s1}

The map
$$
\Phi:M_n(\RR)\longrightarrow M_n(\RR),
\qquad
\Phi(A)=A^TA
$$
is continuous.

::: pf-proof

Every entry of $A^TA$ is a polynomial in the entries of $A$. Polynomial
maps between finite-dimensional Euclidean spaces are continuous.

:::

:::

::: {.pf-step #s2}

The orthogonal group is closed in $\RR^{n^2}$.

::: pf-proof

By definition,
$$
O(n)
=
\{A\in M_n(\RR):A^TA=I\}
=
\Phi^{-1}(\{I\}).
$$
The singleton $\{I\}$ is closed, and $\Phi$ is continuous by step [](#s1){.pf-ref}.
Therefore $O(n)$ is closed.

:::

:::

::: {.pf-step #s3}

Every matrix $A\in O(n)$ has Frobenius norm
$$
\norm{A}_{F}
=
\sqrt n.
$$

::: pf-proof

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

:::

::: {.pf-step #s4}

The set $O(n)$ is bounded in $\RR^{n^2}$.

::: pf-proof

Step [](#s3){.pf-ref} shows that every element lies on the Euclidean sphere of radius
$\sqrt n$ in matrix-entry coordinates.

:::

:::

::: {.pf-step #s5}

Therefore
$$
\boxed{O(n)\text{ is compact}}.
$$

::: pf-proof

By steps [](#s2){.pf-ref} and [](#s4){.pf-ref}, $O(n)$ is closed and bounded in the
finite-dimensional Euclidean space $\RR^{n^2}$. The Heine--Borel theorem
therefore gives compactness.

:::

:::

::: pf-qed

Step [](#s5){.pf-ref} is the required conclusion.

:::

:::

:::
