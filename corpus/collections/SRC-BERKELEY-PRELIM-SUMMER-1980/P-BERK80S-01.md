---
schema: qual/card@1
id: P-BERK80S-01
kind: problem
title: Real matrix with prescribed invariant subspaces and minimal polynomial
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 1 of the vendored Berkeley Preliminary Exam, Summer 1980.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Verified the invariant line and perpendicular plane explicitly and computed the minimal polynomial from the two invariant restrictions.
---

::: {.problem}
Exhibit a real $3\times3$ matrix having minimal polynomial $(t^2+1)(t-10)$ which, as a linear transformation of $\mathbb R^3$, leaves invariant the line $L$ through $(0,0,0)$ and $(1,1,1)$ and the plane through $(0,0,0)$ perpendicular to $L$.
:::

::: {.solution}
Let
$$
e=(1,1,1),\qquad u=(1,-1,0),\qquad v=(1,1,-2).
$$
Then $L=\operatorname{span}(e)$ and
$$
L^\perp=\operatorname{span}(u,v),
$$
since $u\cdot e=v\cdot e=0$ and $u,v$ are linearly independent.
Define $T:\RR^3\to\RR^3$ on the basis $e,u,v$ by
$$
T(e)=10e,\qquad T(u)=v,\qquad T(v)=-u.
$$

::: pf

::: {.pf-step #s1}

The line $L$ and the plane $L^\perp$ are $T$-invariant.

::: pf-proof

Because $T(e)=10e$, the line $L=\operatorname{span}(e)$ is invariant.
Also $T(u)=v$ and $T(v)=-u$, so $T$ maps the spanning set $\{u,v\}$ of
$L^\perp$ into $L^\perp$. Hence $L^\perp$ is invariant.

:::

:::

::: {.pf-step #s2}

In the standard basis, $T$ has matrix
$$
\boxed{
A=\frac13
\begin{pmatrix}
11&8&11\\
12&9&9\\
7&13&10
\end{pmatrix}.}
$$

::: pf-proof

Every $x=(x_1,x_2,x_3)$ has the unique decomposition
$$
x=a e+b u+c v,
$$
where
$$
a=\frac{x_1+x_2+x_3}{3},\qquad
b=\frac{x_1-x_2}{2},\qquad
c=\frac{x_1+x_2-2x_3}{6}.
$$
Therefore
$$
T(x)=10a e+bv-cu.
$$
Substituting the expressions for $a,b,c$ gives $T(x)=Ax$.

:::

:::

::: {.pf-step #s3}

The minimal polynomial of $A$ is $(t^2+1)(t-10)$.

::: pf-proof

On $L$, the restriction of $T$ is multiplication by $10$, so its minimal
polynomial is $t-10$. On $L^\perp$, relative to the basis $(u,v)$, the
restriction has matrix
$$
\begin{pmatrix}0&-1\\1&0\end{pmatrix},
$$
whose square is $-I$ and which is not a scalar matrix. Hence its minimal
polynomial is $t^2+1$.

Since
$$
\RR^3=L\oplus L^\perp
$$
and both summands are invariant by step [](#s1){.pf-ref}, the minimal polynomial of $T$
is the least common multiple of the minimal polynomials of the two
restrictions. The polynomials $t-10$ and $t^2+1$ are coprime over $\RR$, so
$$
\mu_A(t)=\operatorname{lcm}(t-10,t^2+1)=(t-10)(t^2+1).
$$

:::

:::

::: pf-qed

Step [](#s2){.pf-ref} exhibits the matrix $A$, step [](#s1){.pf-ref} shows that it leaves $L$ and
$L^\perp$ invariant, and step [](#s3){.pf-ref} gives its minimal polynomial.

:::

:::

:::
