---
schema: qual/card@1
id: P-BKF09-6B
kind: problem
title: The numerical range of a normal matrix is a convex polygon
classification:
  areas:
  - prelim
  topics:
  - Linear Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Structured the two-line argument into numbered steps, and supplied both directions of the
    identification, which the prose asserted in one sentence: that every value of the quadratic form
    is a convex combination of the eigenvalues with weights |z_i|^2, and conversely that every such
    convex combination is attained (choose the coordinates with those squared moduli). Also supplied
    the spectral theorem input (a normal operator has an orthonormal basis of eigenvectors) and the
    degenerate cases: the convex hull of finitely many points is a convex polygon, possibly a
    segment or a point when the eigenvalues are collinear or all equal. Every macro used is one the
    preamble defines. No source text is retained for this examination.
---

::: {.problem}
Let $\langle z,w\rangle=\sum z_i\bar{w}_i$ be the Hermitian dot product on $\CC^n$, and let $A$ be a *normal* linear operator on $\CC^n$, i.e. $A^*A=AA^*$ where $A^*=\bar{A}^t$ is Hermitian adjoint to $A$. Prove that the set of complex numbers
$$
\Lambda_A\coloneqq\{\langle Az,z\rangle\mid z\in\CC^n,\ \langle z,z\rangle=1\}
$$
is a convex polygon.
:::

::: {.solution}

The argument is the card's own; the card is an examination problem and no published solution is retained for it.

Let $\langle z,w\rangle=\sum_{i}z_{i}\overline{w_{i}}$, let $A$ be normal, and let $\Lambda_{A}=\{\langle Az,z\rangle\mid\norm{z}=1\}$.

::: pf

::: {.pf-step #spectral}
There is an orthonormal basis $e_{1},\dots,e_{n}$ of $\CC^{n}$ consisting of eigenvectors of $A$, with eigenvalues $\lambda_{1},\dots,\lambda_{n}$.

::: pf-proof
This is the spectral theorem for normal operators, the complex version of orthogonal diagonalisation: $A$ is unitarily diagonalisable, so in a suitable orthonormal basis it is $\operatorname{diag}(\lambda_{1},\dots,\lambda_{n})$. (The hypothesis $A^{*}A=AA^{*}$ is exactly what makes the eigenvectors complete and mutually orthogonal.)
:::

:::

::: {.pf-step #value}
For $z=\sum_{i}z_{i}e_{i}$ with $\norm{z}=1$, $\langle Az,z\rangle=\sum_{i}\lambda_{i}\abs{z_{i}}^{2}$ and $\sum_{i}\abs{z_{i}}^{2}=1$.

::: pf-proof
$Az=\sum_{i}z_{i}\lambda_{i}e_{i}$ by linearity and $Ae_{i}=\lambda_{i}e_{i}$. Since the basis is orthonormal, $\langle\sum_{i}\lambda_{i}z_{i}e_{i},\sum_{j}z_{j}e_{j}\rangle=\sum_{i}\lambda_{i}z_{i}\overline{z_{i}}=\sum_{i}\lambda_{i}\abs{z_{i}}^{2}$, and $\langle z,z\rangle=\sum_{i}\abs{z_{i}}^{2}=1$ is the normalisation.
:::

:::

::: {.pf-step #into}
$\Lambda_{A}\subset\operatorname{conv}\{\lambda_{1},\dots,\lambda_{n}\}$.

::: pf-proof
By step [](#value){.pf-ref} each $\langle Az,z\rangle$ is $\sum_{i}t_{i}\lambda_{i}$ with $t_{i}=\abs{z_{i}}^{2}\geq0$ and $\sum_{i}t_{i}=1$, which is a convex combination of the eigenvalues.
:::

:::

::: {.pf-step #onto}
Every convex combination of $\lambda_{1},\dots,\lambda_{n}$ lies in $\Lambda_{A}$.

::: pf-proof
Let $t_{i}\geq0$ with $\sum_{i}t_{i}=1$, and set $z_{i}=\sqrt{t_{i}}$ (a nonnegative real square root) and $z=\sum_{i}z_{i}e_{i}$. Then $\norm{z}^{2}=\sum_{i}t_{i}=1$, and by step [](#value){.pf-ref} $\langle Az,z\rangle=\sum_{i}\lambda_{i}t_{i}$. So every convex combination is attained.
:::

:::

::: {.pf-step #finite}
$\operatorname{conv}\{\lambda_{1},\dots,\lambda_{n}\}$ is a convex polygon.

::: pf-proof
A convex polygon is the convex hull of a finite set of points in the plane, so the convex hull of the finite set $\{\lambda_{1},\dots,\lambda_{n}\}$ is one by definition; when the points are collinear the hull is a segment and when they coincide it is a point, both read as degenerate polygons. Distinct eigenvalues give the vertices; repeated ones contribute nothing new.
:::

:::

::: {.pf-step}
$\Lambda_{A}$ is a convex polygon.

::: pf-proof
Steps [](#into){.pf-ref} and [](#onto){.pf-ref} give $\Lambda_{A}=\operatorname{conv}\{\lambda_{1},\dots,\lambda_{n}\}$, and step [](#finite){.pf-ref} identifies that set as a convex polygon.
:::

:::

:::

:::
