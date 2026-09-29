---
schema: qual/card@1
id: P-BKS10-8A
kind: problem
title: Characteristic polynomial of an invariant-subspace restriction
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
  note: Checked against the vendored UC Berkeley Spring 2010 preliminary-exam solution packet, which reproduces the problem statement before its solution.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked the adapted-basis block decomposition and determinant factorization.
---

::: {.problem}
Let $V$ be a finite-dimensional vector space over a field $k$, let $T:V\to V$ be linear, and let $W\subseteq V$ be a $T$-invariant subspace.
Show that the characteristic polynomial of $T|_W$ divides the characteristic polynomial of $T$.
:::

::: {.solution}
Let
$$
m\coloneqq\dim W,
\qquad
n\coloneqq\dim V.
$$

::: pf

::: {.pf-step #extended-basis}
There is a basis
$$
v_1,\ldots,v_m,v_{m+1},\ldots,v_n
$$
of $V$ such that $v_1,\ldots,v_m$ is a basis of $W$.

::: pf-proof
Choose any basis $v_1,\ldots,v_m$ of the subspace $W$ and extend it to a
basis of the finite-dimensional space $V$.
:::

:::

::: {.pf-step #block-form}
Relative to the basis in step [](#extended-basis){.pf-ref}, the matrix of $T$ has block form
$$
[T]
=
\begin{pmatrix}
A&C\\
0&D
\end{pmatrix},
$$
where $A$ is the matrix of $T|_W$ in the basis
$v_1,\ldots,v_m$.

::: pf-proof
Because $W$ is $T$-invariant,
$$
T(v_j)\in W
$$
for $1\leq j\leq m$. Therefore the last $n-m$ coordinates of each of the
first $m$ columns of $[T]$ vanish, giving the zero lower-left block. The
upper-left block records exactly the coordinates of the restricted map
$T|_W$ in the chosen basis of $W$.
:::

:::

::: {.pf-step #characteristic-factorization}
The characteristic polynomial of $T$ factors as
$$
\chi_T(t)
=
\chi_{T|_W}(t)\det(tI_{n-m}-D).
$$

::: pf-proof
By step [](#block-form){.pf-ref},
$$
tI_n-[T]
=
\begin{pmatrix}
tI_m-A&-C\\
0&tI_{n-m}-D
\end{pmatrix}.
$$
The determinant of a block upper-triangular matrix is the product of the
determinants of its diagonal blocks. Hence
$$
\begin{aligned}
\chi_T(t)
&=
\det(tI_n-[T])\\
&=
\det(tI_m-A)\det(tI_{n-m}-D).
\end{aligned}
$$
Since $A$ represents $T|_W$,
$$
\det(tI_m-A)=\chi_{T|_W}(t).
$$
:::

:::

::: {.pf-step #divisibility}
The polynomial $\chi_{T|_W}$ divides $\chi_T$ in $k[t]$.

::: pf-proof
Step [](#characteristic-factorization){.pf-ref} expresses $\chi_T$ as $\chi_{T|_W}$ times a polynomial in
$k[t]$.
:::

:::

::: pf-qed
Step [](#divisibility){.pf-ref} is the required divisibility statement.
:::

:::

:::
