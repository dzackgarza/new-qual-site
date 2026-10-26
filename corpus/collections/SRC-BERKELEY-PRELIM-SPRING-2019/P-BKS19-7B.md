---
schema: qual/card@1
id: P-BKS19-7B
kind: problem
title: Conjugacy in $\GL_2^+(\RR)$ versus $\GL_2(\RR)$
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
  note: Checked against the vendored UC Berkeley Spring 2019 Graduate Preliminary Examination.
- event: source-checked
  by: chatgpt
  date: 2026-10-02
  note: Independently reviewed the supplied Berkeley Spring 2019 clockwise-versus-counterclockwise rotation counterexample. It is correct; the solution below proves algebraically that every conjugating matrix reverses orientation.
- event: solution-written
  by: chatgpt
  date: 2026-10-02
- event: solution-reviewed
  by: chatgpt
  date: 2026-10-02
  note: Verified similarity via an explicit reflection and solved the anticommutation equation to show that every conjugator has negative determinant.
---

::: {.problem}
Is it true that elements of the group $\GL_2^+(\RR)$ of real $2\times2$ matrices with positive determinant are conjugate in $\GL_2^+(\RR)$ if and only if the matrices are similar (conjugate in $\GL_2(\RR)$)? Either prove this or give a counterexample.
:::

Define
$$
J\coloneqq
\begin{pmatrix}
0&-1\\
1&0
\end{pmatrix}.
$$
Then $J$ is rotation through $\pi/2$ and $-J$ is rotation through $-\pi/2$.

::: pf

::: pf-step

Both $J$ and $-J$ lie in $GL_2^+(\mathbb R)$.


::: pf-proof

One has
$$
\det J=1
\qquad\text{and}\qquad
\det(-J)=(-1)^2\det J=1.
$$

:::

:::

::: pf-step

The matrices $J$ and $-J$ are similar in $GL_2(\mathbb R)$.


::: pf-proof

Let
$$
S\coloneqq
\begin{pmatrix}
1&0\\
0&-1
\end{pmatrix}.
$$
Then $S^{-1}=S$ and direct multiplication gives
$$
SJS^{-1}=-J.
$$
Thus $J$ and $-J$ are conjugate in $GL_2(\mathbb R)$. Notice that $\det S=-1$.

:::

:::

::: pf-step

Every $P\in GL_2(\mathbb R)$ satisfying
$$
PJP^{-1}=-J
$$
has negative determinant.


::: pf-proof

The conjugacy equation is equivalent to
$$
PJ=-JP.
$$
Write
$$
P=
\begin{pmatrix}
a&b\\
c&d
\end{pmatrix}.
$$
Then
$$
PJ=
\begin{pmatrix}
b&-a\\
d&-c
\end{pmatrix},
\qquad
-JP=
\begin{pmatrix}
c&d\\
-a&-b
\end{pmatrix}.
$$
Equality forces
$$
c=b,
\qquad
d=-a.
$$
Hence
$$
P=
\begin{pmatrix}
a&b\\
b&-a
\end{pmatrix},
$$
so
$$
\det P=-a^2-b^2.
$$
Since $P$ is invertible, $(a,b)\neq(0,0)$, and therefore $\det P<0$.

:::

:::

::: pf-step

Thus
$$
\boxed{J\ \text{and}\ -J}
$$
form a counterexample: they are similar in $GL_2(\mathbb R)$ but are not conjugate in $GL_2^+(\mathbb R)$.


::: pf-proof

Similarity is step <1>2. If they were conjugate in $GL_2^+(\mathbb R)$, there would be a conjugator $P$ of positive determinant, contradicting step <1>3.

:::

:::

::: pf-qed

Step <1>4 disproves the proposed equivalence.

:::

:::
