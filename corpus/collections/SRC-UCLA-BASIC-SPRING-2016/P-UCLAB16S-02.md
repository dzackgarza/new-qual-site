---
schema: qual/card@1
id: P-UCLAB16S-02
kind: problem
title: Riemann integrability after changing a convergent sequence
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
  note: Checked against the vendored UCLA Basic Examination, Spring 2016, `assets/attachments/basic-16S.pdf`.
---

::: {.problem}
Let $a<b$ be real numbers.

1. Define what it means for a function $f:[a,b]\to\RR$ to be Riemann integrable on $[a,b]$.

2. Let $\{x_n\}_{n=1}^{\infty}\subset[a,b]$ be a sequence such that $\lim_{n\to\infty}x_n$ exists, and define
$$
f(x)=\begin{cases}
1,&x\notin\{x_n:n\ge1\},\\
0,&x\in\{x_n:n\ge1\}.
\end{cases}
$$
Using your definition, prove that $f$ is Riemann integrable on $[a,b]$.
:::

::: {.solution}

::: pf

::: pf-step

For a bounded function
$$
f:[a,b]\to\RR
$$
and a partition
$$
P:\quad a=t_0<t_1<\cdots<t_m=b,
$$
define
$$
M_i
=
\sup_{x\in[t_{i-1},t_i]}f(x),
\qquad
m_i
=
\inf_{x\in[t_{i-1},t_i]}f(x),
$$
and the Darboux sums
$$
U(f,P)
=
\sum_{i=1}^m
M_i(t_i-t_{i-1}),
$$
$$
L(f,P)
=
\sum_{i=1}^m
m_i(t_i-t_{i-1}).
$$


::: pf-proof

These are the standard upper and lower Darboux sums.

:::

:::

::: {.pf-step #s1-2}

The function $f$ is Riemann integrable on $[a,b]$ if
$$
\boxed{
\inf_P U(f,P)
=
\sup_P L(f,P).
}
$$
Equivalently, for every $\varepsilon>0$ there exists a partition $P$ such that
$$
U(f,P)-L(f,P)<\varepsilon.
$$


::: pf-proof

The equality of the upper and lower Darboux integrals is the definition.
The equivalent criterion follows by taking common refinements of partitions, which decrease upper sums and increase lower sums.
This answers part 1.

:::

:::

::: pf-step

Let
$$
\ell=\lim_{n\to\infty}x_n.
$$
Fix
$$
\varepsilon>0.
$$
Choose $\delta>0$ so small that
$$
2\delta<\frac{\varepsilon}{2}.
$$


::: pf-proof

For example, one may take
$$
\delta=\frac{\varepsilon}{8}.
$$

:::

:::

::: {.pf-step #s1-4}

There exists $N$ such that
$$
x_n\in(\ell-\delta,\ell+\delta)
$$
for every
$$
n\ge N.
$$


::: pf-proof

This is the definition of convergence of the sequence $(x_n)$ to $\ell$.

:::

:::

::: {.pf-step #s1-5}

The finitely many points
$$
x_1,\ldots,x_{N-1}
$$
can be covered by finitely many open intervals whose total length is less than
$$
\frac{\varepsilon}{2}.
$$


::: pf-proof

For each
$$
1\le j<N,
$$
choose an open interval $I_j$ centered at $x_j$ of length less than
$$
\frac{\varepsilon}{2N}.
$$
Then
$$
\sum_{j=1}^{N-1}|I_j|
<
(N-1)\frac{\varepsilon}{2N}
<
\frac{\varepsilon}{2}.
$$
If some $x_j$ coincide, this only makes the cover more redundant.

:::

:::

::: pf-step

Let
$$
J
=
(\ell-\delta,\ell+\delta)
\cap[a,b],
$$
and let
$$
\mathcal U
=
J
\cup
\bigcup_{j=1}^{N-1}(I_j\cap[a,b]).
$$
Then every point
$$
x_n
$$
lies in $\mathcal U$, and the total length of these finitely many intervals is less than $\varepsilon$.


::: pf-proof

By step [](#s1-4){.pf-ref}, every tail point
$$
x_n,\quad n\ge N,
$$
lies in $J$.
The earlier points lie in the intervals from step [](#s1-5){.pf-ref}.

The interval $J$ has length at most
$$
2\delta<\frac{\varepsilon}{2},
$$
and the remaining intervals have total length less than
$$
\frac{\varepsilon}{2}.
$$
Thus the total is less than $\varepsilon$.

:::

:::

::: {.pf-step #s1-7}

Choose a partition $P$ containing all endpoints of the finitely many intervals occurring in $\mathcal U$.
Then every partition subinterval that meets
$$
\{x_n:n\ge1\}
$$
is contained in $\mathcal U$.


::: pf-proof

Every exceptional point $x_n$ belongs to one of the finitely many intervals forming $\mathcal U$.
Because the partition contains all their endpoints, a partition cell containing such a point cannot cross from the inside of that interval to the outside without meeting one of those endpoints.
Thus every cell that contains an exceptional point lies inside the union $\mathcal U$.

:::

:::

::: {.pf-step #s1-8}

If a partition subinterval contains no point $x_n$, then
$$
M_i=m_i=1.
$$


::: pf-proof

By definition,
$$
f(x)=1
$$
at every point outside the set
$$
\{x_n:n\ge1\}.
$$
Thus $f$ is identically $1$ on any such subinterval.

:::

:::

::: {.pf-step #s1-9}

If a partition subinterval contains at least one point $x_n$, then
$$
0\le M_i-m_i\le1.
$$


::: pf-proof

The function takes only the values
$$
0
\quad\text{and}\quad
1.
$$
Therefore every oscillation is at most $1$.

:::

:::

::: {.pf-step #s1-10}

For the partition $P$ from step [](#s1-7){.pf-ref},
$$
U(f,P)-L(f,P)
<
\varepsilon.
$$


::: pf-proof

By step [](#s1-8){.pf-ref}, cells containing no exceptional point contribute zero to
$$
U-L.
$$
By step [](#s1-9){.pf-ref}, each remaining cell contributes at most its length.
By step [](#s1-7){.pf-ref}, all such cells lie in $\mathcal U$.
Hence
$$
U(f,P)-L(f,P)
\le
\operatorname{length}(\mathcal U)
<
\varepsilon.
$$

:::

:::

::: {.pf-step #s1-11}

Therefore $f$ is Riemann integrable on $[a,b]$.


::: pf-proof

The function is bounded, since
$$
0\le f\le1.
$$
For every $\varepsilon>0$, step [](#s1-10){.pf-ref} constructs a partition with upper-minus-lower sum less than $\varepsilon$.
Apply the criterion from step [](#s1-2){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-2){.pf-ref} gives the definition requested in part 1, and step [](#s1-11){.pf-ref} proves part 2.

:::

:::

:::
