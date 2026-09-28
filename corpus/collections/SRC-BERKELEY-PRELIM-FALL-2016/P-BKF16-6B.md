---
schema: qual/card@1
id: P-BKF16-6B
kind: problem
title: Dimension of the solution space of $AXB=0$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the retained Fall 2016 solution packet: AXB=0 is
    equivalent to X mapping the column space of B into the nullspace of A,
    reducing the count to a single forced zero block.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked the image/kernel reformulation, their dimensions from the rank
    hypotheses, the adapted-basis matrix form, and the resulting np-rs free
    parameters.
---

::: {.problem}
Let A be an $m \times n$ matrix of rank r and B a $p \times q$ matrix of rank s. Find the dimension of the vector space of $n \times p$ matrices X such that $A X B = 0$
:::

::: {.solution}
<1>1. The condition
$$
AXB=0
$$
is equivalent to
$$
X(\operatorname{im}B)\subseteq\ker A.
$$

::: {.proof}
Regard
$$
B:\mathbb R^q\to\mathbb R^p,
\qquad
X:\mathbb R^p\to\mathbb R^n,
\qquad
A:\mathbb R^n\to\mathbb R^m
$$
as linear maps. Then
$$
AXB=0
$$
means that for every $v\in\mathbb R^q$,
$$
A(X(Bv))=0.
$$
This holds exactly when
$$
X(Bv)\in\ker A
$$
for every $v$, which is equivalent to
$$
X(\operatorname{im}B)\subseteq\ker A.
$$
:::

<1>2. The two distinguished subspaces have dimensions
$$
\dim(\operatorname{im}B)=s,
\qquad
\dim(\ker A)=n-r.
$$

::: {.proof}
The first equality is the definition of the rank of $B$. The second is
the rank-nullity theorem applied to
$$
A:\mathbb R^n\to\mathbb R^m.
$$
:::

<1>3. Choose a basis
$$
e_1,\ldots,e_p
$$
of $\mathbb R^p$ such that
$$
\operatorname{im}B
=
\operatorname{span}(e_1,\ldots,e_s),
$$
and a basis
$$
u_1,\ldots,u_n
$$
of $\mathbb R^n$ such that
$$
\ker A
=
\operatorname{span}(u_{r+1},\ldots,u_n).
$$

::: {.proof}
By step <1>2, a basis of $\operatorname{im}B$ has $s$ vectors and may be
extended to a basis of $\mathbb R^p$. Likewise, a basis of $\ker A$ has
$n-r$ vectors and may be extended by $r$ further vectors to a basis of
$\mathbb R^n$; relabel the latter so that the kernel basis is
$u_{r+1},\ldots,u_n$.
:::

<1>4. In the bases from step <1>3, the matrices $X$ satisfying $AXB=0$
are exactly the $n\times p$ matrices whose upper-left $r\times s$
block is zero.

::: {.proof}
By step <1>1, the condition is that
$$
X(e_j)\in\ker A
$$
for every $1\le j\le s$. By step <1>3, this says precisely that the
coefficients of
$$
u_1,\ldots,u_r
$$
in each of the first $s$ columns of the matrix of $X$ vanish. These are
exactly the $rs$ entries in the upper-left $r\times s$ block.

There is no condition on the remaining matrix entries: the first $s$
columns may have arbitrary components along
$u_{r+1},\ldots,u_n$, and the remaining $p-s$ columns are unrestricted.
:::

<1>5. The vector space of solutions has dimension
$$
\boxed{np-rs}.
$$

::: {.proof}
An arbitrary $n\times p$ matrix has $np$ independent entries. Step
<1>4 imposes exactly $rs$ independent zero-coordinate conditions and no
others. Hence the solution space has
$$
np-rs
$$
free coordinates.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 gives the requested dimension.
:::
:::
