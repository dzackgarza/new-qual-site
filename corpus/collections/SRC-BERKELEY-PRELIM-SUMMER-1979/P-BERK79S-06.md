---
schema: qual/card@1
id: P-BERK79S-06
kind: problem
title: A circle integral extracting the extreme coefficients of a polynomial
classification:
  areas: [prelim]
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
    On |z|=R used conjugate(z)=R^2/z to expand
    |f(z)|^2 as sum_{j,k} a_j conjugate(a_k) R^{2k} z^{j-k}.
    After multiplication by z^{n-1}, the contour integral extracts the
    z^{-1} coefficient. The exponent condition forces j=0 and k=n, giving
    exactly a_0 conjugate(a_n) R^{2n}.
---

::: {.problem}
Let
\[
f(z)=a_0+a_1z+\cdots+a_nz^n
\]
be a complex polynomial of degree $n>0$.
Prove that
\[
\frac1{2\pi i}\int_{|z|=R}z^{n-1}|f(z)|^2\,dz
=a_0\overline{a_n}\,R^{2n}.
\]
:::

::: {.solution}
<1>1. On the circle
$$
\abs{z}=R,
$$
one has
$$
\bar z=\frac{R^2}{z}.
$$

::: {.proof}
On this circle,
$$
z\bar z=\abs{z}^2=R^2.
$$
Since $R>0$ on a nondegenerate contour, $z\neq0$, so division by $z$
gives the formula.
:::

<1>2. On $\abs{z}=R$,
$$
\overline{f(z)}
=
\sum_{k=0}^n
\overline{a_k}R^{2k}z^{-k}.
$$

::: {.proof}
Conjugating the polynomial gives
$$
\overline{f(z)}
=
\sum_{k=0}^n
\overline{a_k}\,\bar z^{\,k}.
$$
Substitute the identity from step <1>1:
$$
\bar z^{\,k}
=
\left(\frac{R^2}{z}\right)^k
=
R^{2k}z^{-k}.
$$
:::

<1>3. On $\abs{z}=R$,
$$
z^{n-1}\abs{f(z)}^2
=
\sum_{j=0}^n
\sum_{k=0}^n
a_j\overline{a_k}R^{2k}
z^{n-1+j-k}.
$$

::: {.proof}
Since
$$
\abs{f(z)}^2
=
f(z)\overline{f(z)},
$$
multiply
$$
f(z)=\sum_{j=0}^n a_jz^j
$$
by the expression from step <1>2 and then by $z^{n-1}$.
:::

<1>4. Among the monomials in step <1>3, the exponent of $z$ equals
$-1$ if and only if
$$
j=0
\qquad\text{and}\qquad
k=n.
$$

::: {.proof}
The exponent is
$$
n-1+j-k.
$$
It equals $-1$ exactly when
$$
k=n+j.
$$
But
$$
0\leq j\leq n
\qquad\text{and}\qquad
0\leq k\leq n.
$$
Thus $k=n+j\leq n$ forces $j=0$, and then $k=n$.
:::

<1>5. The coefficient of $z^{-1}$ in the Laurent expression from step
<1>3 is
$$
a_0\overline{a_n}R^{2n}.
$$

::: {.proof}
By step <1>4, only the term with $(j,k)=(0,n)$ contributes to the
$z^{-1}$ coefficient. Substituting these indices into its coefficient
gives the displayed value.
:::

<1>6. One has
$$
\boxed{
\frac1{2\pi i}
\int_{\abs{z}=R}
z^{n-1}\abs{f(z)}^2\,dz
=
a_0\overline{a_n}R^{2n}.
}
$$

::: {.proof}
For every integer $m$,
$$
\frac1{2\pi i}
\int_{\abs{z}=R}z^m\,dz
=
\begin{cases}
1,&m=-1,\\
0,&m\neq-1.
\end{cases}
$$
Therefore integrating the finite Laurent sum in step <1>3 term by term
extracts precisely its $z^{-1}$ coefficient, which step <1>5 computes.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>6 is the required identity.
:::
:::
