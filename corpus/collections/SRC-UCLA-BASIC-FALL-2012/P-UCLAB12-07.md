---
schema: qual/card@1
id: P-UCLAB12-07
kind: problem
title: Invertible matrices with bounded powers are diagonalizable
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
Let $A$ be an invertible $n$ by $n$ matrix with entries in $\CC$.
Suppose that the set of powers $A^n$ of $A$, for $n \in \ZZ$, is bounded.
Show that $A$ is diagonalizable.
:::

::: {.solution}

Fix any matrix norm on $M_n(\CC)$. By hypothesis there is $C>0$ such that
\[
\|A^k\|\le C
\]
for every $k\in\ZZ$.

::: pf

::: {.pf-step #s1-1}

Every eigenvalue $\lambda$ of $A$ satisfies
\[
|\lambda|=1.
\]


::: pf-proof

Let
\[
Av=\lambda v
\]
with $v\ne0$.
For every positive integer $k$,
\[
A^kv=\lambda^kv.
\]
Hence
\[
|\lambda|^k\|v\|
=
\|A^kv\|
\le
\|A^k\|\,\|v\|
\le
C\|v\|.
\]
Thus
\[
|\lambda|^k\le C
\]
for all $k\ge1$, which forces
\[
|\lambda|\le1.
\]

Since $A$ is invertible,
\[
A^{-1}v=\lambda^{-1}v.
\]
Applying the same argument to the bounded positive powers of $A^{-1}$ gives
\[
|\lambda^{-1}|\le1,
\]
so $|\lambda|\ge1$. Therefore $|\lambda|=1$.

:::

:::

::: {.pf-step #s1-2}

If $A$ were not diagonalizable, then there would exist an eigenvalue $\lambda$ and vectors $v,w$ with
\[
w\ne0,
\qquad
(A-\lambda I)v=w,
\qquad
(A-\lambda I)w=0.
\]


::: pf-proof

Over $\CC$, the minimal polynomial of $A$ splits into linear factors.
A matrix is diagonalizable if and only if its minimal polynomial has no repeated root.

For completeness, if the minimal polynomial has a repeated factor
\[
(t-\lambda)^r,
\qquad
r\ge2,
\]
let
\[
q(t)=\frac{m_A(t)}{(t-\lambda)^r}.
\]
Minimality of $m_A$ implies
\[
(A-\lambda I)^{r-1}q(A)\ne0.
\]
Choose $u$ such that
\[
w=(A-\lambda I)^{r-1}q(A)u\ne0.
\]
Set
\[
v=(A-\lambda I)^{r-2}q(A)u.
\]
Then
\[
(A-\lambda I)v=w,
\]
while
\[
(A-\lambda I)w
=
(A-\lambda I)^rq(A)u
=
m_A(A)u
=0.
\]
Thus the stated vectors exist whenever $A$ is not diagonalizable.

:::

:::

::: {.pf-step #s1-3}

For the vectors in step [](#s1-2){.pf-ref} and every integer $k\ge1$,
\[
A^kv
=
\lambda^kv
+
k\lambda^{k-1}w.
\]


::: pf-proof

On the span of $v,w$, write
\[
A=\lambda I+N,
\]
where
\[
Nv=w,
\qquad
Nw=0.
\]
Thus
\[
N^2v=0.
\]
The binomial theorem gives
\[
(\lambda I+N)^kv
=
\lambda^kv
+
k\lambda^{k-1}Nv,
\]
because all terms involving $N^j$ for $j\ge2$ vanish on $v$. Since $Nv=w$, the formula follows.

:::

:::

::: {.pf-step #s1-4}

The formula in step [](#s1-3){.pf-ref} contradicts boundedness of the powers of $A$.


::: pf-proof

By step [](#s1-1){.pf-ref},
\[
|\lambda|=1.
\]
Therefore step [](#s1-3){.pf-ref} gives
\[
\begin{aligned}
\|A^kv\|
&=
\|\lambda^kv+k\lambda^{k-1}w\|\\
&\ge
k\|w\|-\|v\|.
\end{aligned}
\]
Since $w\ne0$, the right side tends to $+\infty$ as $k\to\infty$.
On the other hand,
\[
\|A^kv\|
\le
\|A^k\|\,\|v\|
\le
C\|v\|,
\]
which is bounded independently of $k$. This is a contradiction.

:::

:::

::: {.pf-step #s1-5}

Therefore
\[
\boxed{A\text{ is diagonalizable over }\CC}.
\]


::: pf-proof

If $A$ were not diagonalizable, steps [](#s1-2){.pf-ref} through [](#s1-4){.pf-ref} would contradict the assumed boundedness of its integer powers. Hence $A$ must be diagonalizable.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} is the required conclusion.

:::

:::

:::
