---
schema: qual/card@1
id: P-PRELIM82S-15
kind: problem
title: Every disk-holomorphic function is bounded along some sequence approaching the boundary
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
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    If no bounded sequence approached the boundary, then |f(z)| would
    tend uniformly to infinity as |z| tends to 1. The nonzero function
    f would then have only finitely many zeros. Dividing the polynomial
    carrying those zeros by f gives a holomorphic function tending
    uniformly to zero near the boundary; the maximum-modulus principle
    forces it to vanish identically, a contradiction.
---

::: {.problem}
Let $f$ be holomorphic on the open unit disk
\[
\mathbb D=\{z:|z|<1\}.
\]
Prove that there is a sequence $(z_n)$ in $\mathbb D$ such that
\[
|z_n|\to1
\]
and $(f(z_n))$ is bounded.
:::

::: {.solution}
<1>1. If $f\equiv0$, the conclusion holds.

::: {.proof}
Take
$$
z_n=1-\frac1n
$$
for $n\geq2$. Then $z_n\in\DD$, $\abs{z_n}\to1$, and
$f(z_n)=0$ for every $n$.
:::

<1>2. Assume henceforth that $f$ is not identically zero. If the desired
sequence does not exist, then for every $M>0$ there is $r_M<1$ such
that
$$
\abs{z}>r_M
\quad\Longrightarrow\quad
\abs{f(z)}>M.
$$

::: {.proof}
Suppose the displayed assertion failed for some $M>0$. Then for every
integer $n\geq2$ there would be a point $z_n\in\DD$ with
$$
\abs{z_n}>1-\frac1n
$$
and
$$
\abs{f(z_n)}\leq M.
$$
This would give $\abs{z_n}\to1$ while $(f(z_n))$ remained bounded,
contrary to the assumption that the desired sequence does not exist.
:::

<1>3. Under the assumption of step <1>2, the function $f$ has only
finitely many zeros in $\DD$.

::: {.proof}
Apply step <1>2 with $M=1$. There is $r_1<1$ such that
$$
\abs{z}>r_1
\quad\Longrightarrow\quad
\abs{f(z)}>1.
$$
Thus every zero of $f$ lies in the compact disk
$$
\{z:\abs{z}\leq r_1\}.
$$
Since $f$ is holomorphic and not identically zero, its zeros are
isolated. An infinite set of zeros in this compact disk would have an
accumulation point there, contradicting the identity theorem. Hence
there are only finitely many zeros.
:::

<1>4. Let $a_1,\ldots,a_k$ be the zeros of $f$ in $\DD$, with
multiplicities $m_1,\ldots,m_k$, and define
$$
P(z)=\prod_{j=1}^k(z-a_j)^{m_j},
$$
with $P=1$ if $f$ has no zeros. Then
$$
h(z)=\frac{P(z)}{f(z)}
$$
extends to a holomorphic function on $\DD$ that is not identically
zero.

::: {.proof}
At each zero $a_j$, the functions $P$ and $f$ vanish to the same order
$m_j$. Their quotient therefore has a removable singularity at $a_j$,
so $h$ extends holomorphically across all the zeros. At every point
where $f$ is nonzero, both $P$ and $f$ are nonzero, so $h$ is nonzero
there. Hence $h$ is not identically zero.
:::

<1>5. For every $\varepsilon>0$, there is $r_\varepsilon<1$ such that
$$
r_\varepsilon<\abs{z}<1
\quad\Longrightarrow\quad
\abs{h(z)}<\varepsilon.
$$

::: {.proof}
The polynomial $P$ is bounded on the closed unit disk. Put
$$
C=\max_{\abs{z}\leq1}\abs{P(z)}.
$$
Since $P$ is not the zero polynomial, $C>0$. Apply step <1>2 with
$$
M=\frac{C}{\varepsilon}.
$$
For $\abs{z}>r_M$,
$$
\abs{h(z)}
=
\frac{\abs{P(z)}}{\abs{f(z)}}
<
\frac{C}{C/\varepsilon}
=
\varepsilon.
$$
Take $r_\varepsilon=r_M$.
:::

<1>6. The function $h$ is identically zero on $\DD$.

::: {.proof}
Fix $w\in\DD$ and $\varepsilon>0$. By step <1>5, choose
$r_\varepsilon<1$ as there. Select
$$
\rho
\quad\text{with}\quad
\max\{\abs{w},r_\varepsilon\}<\rho<1.
$$
The maximum-modulus principle on the disk $\abs{z}\leq\rho$ gives
$$
\abs{h(w)}
\leq
\max_{\abs{z}=\rho}\abs{h(z)}
<
\varepsilon.
$$
Since $\varepsilon>0$ is arbitrary, $h(w)=0$. As $w$ was arbitrary,
$h\equiv0$ on $\DD$.
:::

<1>7. The assumption that no desired sequence exists is impossible.

::: {.proof}
Step <1>4 says that $h$ is not identically zero, whereas step <1>6 says
that $h$ is identically zero. This contradiction arose from the
assumption in step <1>2 that the desired sequence does not exist.
:::

<1>8. Therefore there is a sequence $(z_n)$ in $\DD$ such that
$$
\boxed{\abs{z_n}\to1}
$$
and $(f(z_n))$ is bounded.

::: {.proof}
The case $f\equiv0$ is step <1>1. If $f$ is not identically zero,
step <1>7 proves the conclusion by contradiction.
:::

<1>9. Q.E.D.

::: {.proof}
Step <1>8 is the required conclusion.
:::
:::
