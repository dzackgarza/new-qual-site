---
schema: qual/card@1
id: P-BKF78-5
kind: problem
title: A contour integral involving the squared modulus of a polynomial
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 5 of the deterministic MinerU Flash extraction of the Berkeley Fall 1978 preliminary exam.
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    On the circle |z|=R, conjugation replaces z by R^2/z. Expanding
    z^{n-1}f(z)\overline{f(z)} as a Laurent polynomial shows that its
    z^{-1} coefficient can only come from the pair (a_0,\overline{a_n}),
    and contour integration extracts exactly that coefficient.
---

::: {.problem}
Let
\[
f(z)=a_0+a_1z+\cdots+a_nz^n
\]
be a complex polynomial of degree $n>0$.
Prove that
\[
\frac1{2\pi i}\int_{|z|=R} z^{n-1}|f(z)|^2\,dz
=a_0\overline{a_n}R^{2n}.
\]
:::

::: {.solution}
<1>1. On the circle $|z|=R$,
$$
\overline{f(z)}
=
\sum_{k=0}^n \overline{a_k}R^{2k}z^{-k}.
$$

::: {.proof}
If $|z|=R$, then
$$
z\overline z=R^2,
$$
so
$$
\overline z=\frac{R^2}{z}.
$$
Therefore
$$
\overline{f(z)}
=
\sum_{k=0}^n \overline{a_k}\,\overline z^{\,k}
=
\sum_{k=0}^n \overline{a_k}R^{2k}z^{-k}.
$$
:::

<1>2. The coefficient of $z^{-1}$ in the Laurent polynomial
$z^{n-1}|f(z)|^2$ is
$$
a_0\overline{a_n}R^{2n}.
$$

::: {.proof}
By step <1>1,
$$
z^{n-1}|f(z)|^2
=
\sum_{j=0}^n\sum_{k=0}^n
a_j\overline{a_k}R^{2k}z^{n-1+j-k}.
$$
A term has exponent $-1$ precisely when
$$
n-1+j-k=-1,
$$
equivalently when
$$
k=n+j.
$$
Since $0\leq j,k\leq n$, this forces $j=0$ and $k=n$. Hence the
unique $z^{-1}$ term is
$$
a_0\overline{a_n}R^{2n}z^{-1}.
$$
:::

<1>3. The required integral is
$$
\boxed{
\frac1{2\pi i}\int_{|z|=R} z^{n-1}|f(z)|^2\,dz
=
a_0\overline{a_n}R^{2n}
}.
$$

::: {.proof}
For every integer $m$,
$$
\frac1{2\pi i}\int_{|z|=R} z^m\,dz
=
\begin{cases}
1,&m=-1,\\
0,&m\neq-1.
\end{cases}
$$
Thus termwise integration of the finite Laurent expansion in step
<1>2 extracts exactly its $z^{-1}$ coefficient. Step <1>2 identifies
that coefficient as $a_0\overline{a_n}R^{2n}$.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 is the asserted identity.
:::
:::
