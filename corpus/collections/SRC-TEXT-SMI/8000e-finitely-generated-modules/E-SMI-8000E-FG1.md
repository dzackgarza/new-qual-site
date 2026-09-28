---
schema: qual/card@1
id: E-SMI-8000E-FG1
kind: problem
title: Classifying groups, modules, and Jordan forms of one fixed type
classification:
  areas:
  - algebra
  topics:
  - Abelian Groups
  - Modules over PIDs
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-11
  note: "Checked the PDF text layer and local extraction. Both use an undefined v in the two primary-subspace annihilation conditions; corrected it to the bound variable x."
- event: solution-written
  by: chatgpt
  date: 2026-09-11
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-11
  note: "Classified the 2- and 3-primary parts by partitions of 3 and 4, then translated the same partition pairs into k[t]-primary modules and Jordan block decompositions, giving 3·5=15 classes in each part."
---

::: {.exercise}
(a) Write down one abelian group of order $n = 2^3 \cdot 3^4$, in each isomorphism class.
How many are there?

(b) Write down one $k[t]$ module $V$, in each $k[t]$ isomorphism class, of $k$-dimension 7, and such that the subspace

$$
V(2) = \ts{x \in V : \text{for some } r, \ (t - 2)^r \cdot x = 0}
$$

has $k$-dimension 3, and the subspace

$$
V(3) = \ts{x \in V : \text{for some } r, \ (t - 3)^r \cdot x = 0}
$$

has $k$-dimension 4. How many are there?

(c) Write down one Jordan matrix (over $\QQ$) in each conjugacy class with characteristic polynomial $(t - 2)^3 (t - 3)^4$.
How many are there?
:::


::: {.remark}
The source PDF writes the bound variable as $x$ in the definitions of $V(2)$
and $V(3)$ but then uses an undefined $v$ in both annihilation conditions.
The conditions above use the bound variable $x$.
:::

::: {.solution}
Let
$$
\mathcal P_3=\{(3),(2,1),(1,1,1)\}
$$
and
$$
\mathcal P_4=\{(4),(3,1),(2,2),(2,1,1),(1,1,1,1)\}
$$
be the partitions of $3$ and $4$.

For a partition $\lambda=(\lambda_1,\ldots,\lambda_r)$, write
$$
A_\lambda(p)=\bigoplus_{j=1}^r\mathbb Z/p^{\lambda_j}\mathbb Z,
$$
$$
M_\lambda(a)=\bigoplus_{j=1}^r
 k[t]/((t-a)^{\lambda_j}),
$$
and
$$
J_\lambda(a)=\bigoplus_{j=1}^r J_{\lambda_j}(a).
$$

<1>1. Classify the abelian groups in part (a).
::: {.proof}
A finite abelian group of order
$$
2^3 3^4
$$
splits uniquely as the direct product of its $2$-primary and $3$-primary
parts. By the classification theorem for finite abelian $p$-groups, the
isomorphism types of the $2$-primary part are indexed by the partitions of
$3$, namely
$$
\mathbb Z/8,
\qquad
\mathbb Z/4\oplus\mathbb Z/2,
\qquad
(\mathbb Z/2)^3,
$$
and the isomorphism types of the $3$-primary part are indexed by the
partitions of $4$, namely
$$
\mathbb Z/81,
\quad
\mathbb Z/27\oplus\mathbb Z/3,
\quad
\mathbb Z/9\oplus\mathbb Z/9,
\quad
\mathbb Z/9\oplus(\mathbb Z/3)^2,
\quad
(\mathbb Z/3)^4.
$$

Consequently the complete list is
$$
\boxed{
A_\lambda(2)\oplus A_\mu(3),
\qquad
(\lambda,\mu)\in\mathcal P_3\times\mathcal P_4.}
$$
Different pairs give nonisomorphic groups because the primary decomposition
and the partitions of the primary components are invariants. Hence there are
$$
\boxed{3\cdot5=15}
$$
isomorphism classes.
:::

<1>2. The two generalized eigenspaces in part (b) form a direct-sum decomposition of $V$.
::: {.proof}
If $x\in V(2)\cap V(3)$, then for some $r,s$,
$$
(t-2)^r x=0,
\qquad
(t-3)^s x=0.
$$
The polynomials $(t-2)^r$ and $(t-3)^s$ are relatively prime, so there are
$a(t),b(t)\in k[t]$ with
$$
a(t)(t-2)^r+b(t)(t-3)^s=1.
$$
Applying this identity to $x$ gives $x=0$. Thus
$$
V(2)\cap V(3)=0.
$$
Since their dimensions are $3$ and $4$ and $\dim_kV=7$,
$$
V=V(2)\oplus V(3).
$$
:::

<1>3. Classify the $k[t]$-modules in part (b).
::: {.proof}
The module $V(2)$ is $(t-2)$-primary and has $k$-dimension $3$. The structure
theorem for finitely generated modules over the PID $k[t]$ says that its
isomorphism type is uniquely
$$
M_\lambda(2)
$$
for a partition $\lambda$ of $3$. Similarly,
$$
V(3)\cong M_\mu(3)
$$
for a unique partition $\mu$ of $4$.

Therefore the complete list is
$$
\boxed{
M_\lambda(2)\oplus M_\mu(3),
\qquad
(\lambda,\mu)\in\mathcal P_3\times\mathcal P_4.}
$$
Again there are
$$
\boxed{15}
$$
isomorphism classes.
:::

<1>4. Classify the Jordan matrices in part (c).
::: {.proof}
Over $\mathbb Q$, a Jordan matrix with characteristic polynomial
$$
(t-2)^3(t-3)^4
$$
has Jordan block sizes at eigenvalue $2$ forming a partition of $3$, and
block sizes at eigenvalue $3$ forming a partition of $4$. Conversely every
such pair of partitions gives such a Jordan matrix.

Thus a complete set of representatives is
$$
\boxed{
J_\lambda(2)\oplus J_\mu(3),
\qquad
(\lambda,\mu)\in\mathcal P_3\times\mathcal P_4,}
$$
and the number of conjugacy classes is again
$$
\boxed{15}.
$$
:::
:::
