---
schema: qual/card@1
id: P-BKF12-7B
kind: problem
title: If $AB-BA=A$ then $A$ is nilpotent
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
    Checked against Problem 7B in the retained Fall 2012 Berkeley prelim exam.
    The retained solution packet's final quotient induction is not valid; the
    authored proof below replaces it by a generalized-eigenspace argument.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked the eigenvalue shift, the generalized-eigenspace intertwining
    identity, and the uniform nilpotence exponent dim V.
---

::: {.problem}
Suppose that A and B are linear transformations of a finite dimensional complex vector space such that $A B - B A = A$ . If v is an eigenvector of B with eigenvalue λ, show that Av is zero or an eigenvector of B and find its eigenvalue.
Prove that A is nilpotent.
:::

::: {.solution}
Let $V$ be the underlying complex vector space and put
$$
d\coloneqq\dim_{\CC}V.
$$
If $d=0$, then $A=0$, so nilpotence is immediate. Hence assume
$d\ge1$. Let $\Lambda\subseteq\CC$ be the set of eigenvalues of $B$,
and for $\mu\in\CC$ write
$$
V_\mu\coloneqq\ker(B-\mu I)^d.
$$

<1>1. If $v$ is a $B$-eigenvector with eigenvalue $\lambda$, then
$Av=0$ or $Av$ is a $B$-eigenvector with eigenvalue
$$
\boxed{\lambda-1}.
$$

::: {.proof}
The relation $AB-BA=A$ gives
$$
BA=AB-A.
$$
Hence, if $Bv=\lambda v$,
$$
B(Av)
=(AB-A)v
=(\lambda-1)Av.
$$
Thus either $Av=0$ or it is an eigenvector of $B$ with eigenvalue
$\lambda-1$.
:::

<1>2. For every $\mu\in\CC$,
$$
(B-(\mu-1)I)A=A(B-\mu I),
$$
and therefore, for every integer $r\ge1$,
$$
(B-(\mu-1)I)^rA=A(B-\mu I)^r.
$$

::: {.proof}
Using $BA=AB-A$,
$$
\begin{aligned}
(B-(\mu-1)I)A
&=BA-(\mu-1)A\\
&=AB-A-\mu A+A\\
&=A(B-\mu I).
\end{aligned}
$$
The formula for the $r$th powers follows by induction on $r$ from this
intertwining identity.
:::

<1>3. For every $\mu\in\CC$ and every integer $k\ge0$,
$$
A^k(V_\mu)\subseteq V_{\mu-k}.
$$

::: {.proof}
If $w\in V_\mu$, then step <1>2 with $r=d$ gives
$$
(B-(\mu-1)I)^dAw
=A(B-\mu I)^dw
=0.
$$
Thus $Aw\in V_{\mu-1}$. Repeating this inclusion gives
$A^k(V_\mu)\subseteq V_{\mu-k}$ for every $k\ge0$.
:::

<1>4. One has
$$
\boxed{A^d=0};
$$
in particular, $A$ is nilpotent.

::: {.proof}
Since $B$ is a complex linear operator on a finite-dimensional space,
the generalized eigenspace decomposition gives
$$
V=\bigoplus_{\lambda\in\Lambda}V_\lambda.
$$
Fix $\lambda\in\Lambda$. The $d+1$ scalars
$$
\lambda,\lambda-1,\ldots,\lambda-d
$$
are distinct, whereas $B$ has at most $d$ distinct eigenvalues. Hence
there is some $k\in\{1,\ldots,d\}$ for which $\lambda-k$ is not an
eigenvalue of $B$. Then $B-(\lambda-k)I$ is invertible, so
$$
V_{\lambda-k}=0.
$$
By step <1>3,
$$
A^k(V_\lambda)\subseteq V_{\lambda-k}=0.
$$
Consequently $A^d$ also vanishes on $V_\lambda$. This holds for every
generalized eigenspace in the displayed direct sum, so $A^d=0$ on $V$.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>1 proves the eigenvector assertion, and step <1>4 proves that
$A$ is nilpotent.
:::
:::
