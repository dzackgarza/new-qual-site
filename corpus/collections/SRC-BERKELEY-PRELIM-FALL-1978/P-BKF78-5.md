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

::: pf

::: {.pf-step #conjugate-on-circle}
On the circle $|z|=R$,
$$
\overline{f(z)}
=
\sum_{k=0}^n \overline{a_k}R^{2k}z^{-k}.
$$

::: pf-proof
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

:::

::: {.pf-step #laurent-coefficient}
The coefficient of $z^{-1}$ in the Laurent polynomial
$z^{n-1}|f(z)|^2$ is
$$
a_0\overline{a_n}R^{2n}.
$$

::: pf-proof
By step [](#conjugate-on-circle){.pf-ref},
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

:::

::: {.pf-step #integral-value}
The required integral is
$$
\boxed{
\frac1{2\pi i}\int_{|z|=R} z^{n-1}|f(z)|^2\,dz
=
a_0\overline{a_n}R^{2n}
}.
$$

::: pf-proof
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
[](#laurent-coefficient){.pf-ref} extracts exactly its $z^{-1}$ coefficient. Step [](#laurent-coefficient){.pf-ref} identifies
that coefficient as $a_0\overline{a_n}R^{2n}$.
:::

:::

::: pf-qed
Step [](#integral-value){.pf-ref} is the asserted identity.
:::

:::
:::
