---
schema: qual/card@1
id: P-BERK79S-16
kind: problem
title: Compact-uniform limits of entire functions with only real zeros
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
    The compact-uniform limit is entire. If g had a nonreal zero z_0,
    choose a small closed disk around z_0 disjoint from R and with no zeros
    of g on its boundary. Uniform convergence on the boundary makes
    |g_n-g|<|g| there for large n, so Rouche's theorem forces g_n to have a
    zero in the disk. This contradicts the hypothesis that every zero of
    g_n is real.
---

::: {.problem}
For each $n\ge1$, let $g_n$ be an entire function whose zeros are all real.
Suppose
\[
g_n\to g
\]
uniformly on compact subsets of $\mathbb C$, where $g$ is not identically zero.
Prove that every zero of $g$ is real.
:::

::: {.solution}
<1>1. The function $g$ is entire.

::: {.proof}
Each $g_n$ is entire and the sequence converges uniformly on compact
subsets of $\CC$. By the Weierstrass theorem on locally uniform limits of
holomorphic functions, the limit $g$ is holomorphic on all of $\CC$.
:::

<1>2. Suppose, toward a contradiction, that $g$ has a nonreal zero
$$
z_0\in\CC\sm\RR.
$$
There is an $r>0$ such that the closed disk
$$
\overline{D}
=
\{z:\abs{z-z_0}\leq r\}
$$
is disjoint from $\RR$ and $g$ has no zero on $\partial D$.

::: {.proof}
Since $z_0$ is nonreal,
$$
\abs{\operatorname{Im}z_0}>0.
$$
Choose first
$$
r<\abs{\operatorname{Im}z_0},
$$
so the closed disk is disjoint from the real axis.

By step <1>1, $g$ is entire, and by hypothesis it is not identically zero.
Therefore its zeros are isolated. Shrinking $r$ if necessary, one may
ensure that $g$ has no zero on the boundary circle $\partial D$.
:::

<1>3. There is a number $m>0$ such that
$$
\abs{g(z)}\geq m
$$
for every $z\in\partial D$.

::: {.proof}
The boundary $\partial D$ is compact. By step <1>2, the continuous
function
$$
z\longmapsto\abs{g(z)}
$$
is strictly positive there. It therefore attains a positive minimum:
$$
m
=
\min_{z\in\partial D}\abs{g(z)}
>
0.
$$
:::

<1>4. For all sufficiently large $n$,
$$
\abs{g_n(z)-g(z)}
<
\abs{g(z)}
$$
for every $z\in\partial D$.

::: {.proof}
The sequence $g_n\to g$ uniformly on the compact set $\partial D$. Thus
there is $N$ such that for every $n\geq N$,
$$
\abs{g_n(z)-g(z)}<m
$$
for all $z\in\partial D$. Step <1>3 gives
$$
m\leq\abs{g(z)},
$$
which proves the desired strict inequality.
:::

<1>5. For every sufficiently large $n$, the functions $g_n$ and $g$ have
the same number of zeros in $D$, counted with multiplicity.

::: {.proof}
Step <1>4 gives the hypothesis of Rouché's theorem on the boundary
$\partial D$. Therefore $g_n$ and $g$ have the same number of zeros inside
$D$, counted with multiplicity.
:::

<1>6. For every sufficiently large $n$, the function $g_n$ has a zero in
$D$.

::: {.proof}
The center $z_0$ lies in $D$ and satisfies
$$
g(z_0)=0.
$$
Thus $g$ has at least one zero in $D$. By step <1>5, $g_n$ has the same
positive number of zeros in $D$ for all sufficiently large $n$.
:::

<1>7. Step <1>6 contradicts the hypothesis on the zeros of $g_n$.

::: {.proof}
By step <1>2,
$$
D\cap\RR=\varnothing.
$$
But every zero of every $g_n$ is real. Hence no $g_n$ can have a zero in
$D$, contradicting step <1>6.
:::

<1>8. Every zero of $g$ is real:
$$
\boxed{
g(z)=0
\implies
z\in\RR.
}
$$

::: {.proof}
The assumption of a nonreal zero led to the contradiction in step <1>7.
Therefore no nonreal zero exists.
:::

<1>9. Q.E.D.

::: {.proof}
Step <1>8 is the required conclusion.
:::
:::
