---
schema: qual/card@1
id: P-BKS80-3
kind: problem
title: Minimize the $L^2$ norm of a quadratic polynomial with prescribed endpoint value
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-13}
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked the Riesz representer of endpoint evaluation by its three moment
    identities, the sharp Cauchy--Schwarz lower bound, and the equality case
    determining the unique minimizing polynomial and minimum value.
---

::: {.problem}
Let $P_2$ be the real polynomials of degree at most two and define
\[
J(f)=\int_0^1 f(x)^2\,dx.
\]
Let
\[
Q=\{f\in P_2:f(1)=1\}.
\]
Show that $J$ attains a minimum on $Q$ and determine the minimizing polynomial.
:::

::: {.solution}
Equip $P_2$ with the inner product
$$
\langle p,q\rangle
\coloneqq
\int_0^1p(x)q(x)\,dx.
$$
Then $J(f)=\langle f,f\rangle$.

<1>1. For
$$
k(x)\coloneqq3-24x+30x^2,
$$
one has
$$
\langle q,k\rangle=q(1)
$$
for every $q\in P_2$.

::: {.proof}
It is enough to check the basis $1,x,x^2$. Directly,
$$
\int_0^1k(x)\,dx
=
3-12+10
=
1,
$$
$$
\int_0^1xk(x)\,dx
=
\frac32-8+\frac{15}{2}
=
1,
$$
and
$$
\int_0^1x^2k(x)\,dx
=
1-6+6
=
1.
$$
Thus the two linear functionals
$$
q\longmapsto\langle q,k\rangle
\qquad\text{and}\qquad
q\longmapsto q(1)
$$
agree on a basis of $P_2$, hence agree everywhere.
:::

<1>2. The squared norm of $k$ is
$$
\langle k,k\rangle=9.
$$

::: {.proof}
Apply step <1>1 with $q=k$. Then
$$
\langle k,k\rangle=k(1)=3-24+30=9.
$$
:::

<1>3. Every $f\in Q$ satisfies
$$
J(f)\ge\frac19.
$$

::: {.proof}
If $f\in Q$, then $f(1)=1$. By step <1>1,
$$
1
=
\langle f,k\rangle.
$$
Cauchy--Schwarz and step <1>2 give
$$
1
\le
\langle f,f\rangle^{1/2}\langle k,k\rangle^{1/2}
=
3J(f)^{1/2}.
$$
Squaring yields $J(f)\ge1/9$.
:::

<1>4. Equality in step <1>3 occurs for exactly one polynomial, namely
$$
f_0(x)
\coloneqq
\frac{k(x)}9
=
\boxed{\frac{10x^2-8x+1}{3}}.
$$

::: {.proof}
Equality in Cauchy--Schwarz holds exactly when $f$ and $k$ are linearly
dependent. Thus an equality case in $Q$ must have $f=ck$. The constraint
$f(1)=1$ and $k(1)=9$ force $c=1/9$, giving the displayed polynomial.
Conversely,
$$
f_0(1)=\frac{10-8+1}{3}=1,
$$
so $f_0\in Q$, and step <1>2 gives
$$
J(f_0)
=
\frac1{81}\langle k,k\rangle
=
\frac19.
$$
:::

<1>5. Therefore $J$ attains its minimum on $Q$, with
$$
\boxed{
\min_{f\in Q}J(f)=\frac19,
\qquad
f_{\min}(x)=\frac{10x^2-8x+1}{3}.
}
$$

::: {.proof}
Step <1>3 gives the universal lower bound, and step <1>4 gives the unique
element of $Q$ attaining it.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 gives both the existence and the location of the minimum.
:::
:::
