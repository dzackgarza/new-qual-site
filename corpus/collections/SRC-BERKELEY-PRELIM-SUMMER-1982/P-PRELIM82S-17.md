---
schema: qual/card@1
id: P-PRELIM82S-17
kind: problem
title: The complement of a regular level curve in $\mathbb R^3$ is path connected
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
    The regular-value theorem makes f^{-1}(0) a closed 1-dimensional
    embedded submanifold of R^3. Relative transversality perturbs the
    straight arc between two complementary points, fixing its ends, to
    an embedded arc transverse to that submanifold. A 1-dimensional arc
    cannot meet a 1-dimensional submanifold transversely in dimension 3,
    so the perturbed arc lies entirely in the complement.
---

::: {.problem}
Let $f:\mathbb R^3\to\mathbb R^2$, and suppose $0$ is a regular value of $f$; that is, $Df$ has rank $2$ at every point of $f^{-1}(0)$.
Prove that
\[
\mathbb R^3\setminus f^{-1}(0)
\]
is arcwise connected.
:::

::: {.solution}
Put
$$
Z=f^{-1}(0).
$$

<1>1. The set $Z$ is a closed smooth embedded submanifold of $\RR^3$
of dimension $1$.

::: {.proof}
The set $Z$ is closed because $f$ is continuous and $\{0\}$ is closed.
Since $0$ is a regular value and
$$
\operatorname{rank}Df_z=2
$$
for every $z\in Z$, the regular-level-set theorem gives
$$
\dim Z=3-2=1.
$$
If $Z$ is empty, its complement is $\RR^3$, which is arcwise connected.
:::

<1>2. Let $a,b\in\RR^3\setminus Z$ be distinct, and define the
straight arc
$$
\gamma_0(t)=(1-t)a+tb,
\qquad
0\leq t\leq1.
$$
There are neighborhoods of $0$ and $1$ in $[0,1]$ whose images under
$\gamma_0$ are disjoint from $Z$.

::: {.proof}
Since $Z$ is closed and $a,b\notin Z$, there are open balls about
$a$ and $b$ disjoint from $Z$. Continuity of $\gamma_0$ gives
intervals near $0$ and $1$ mapped into those balls.
:::

<1>3. There exists a smooth embedded arc
$$
\gamma:[0,1]\longrightarrow\RR^3
$$
with
$$
\gamma(0)=a,
\qquad
\gamma(1)=b,
$$
which agrees with $\gamma_0$ near the endpoints and is transverse to
$Z$.

::: {.proof}
Apply the relative transversality theorem to $\gamma_0$ and the
submanifold $Z$, keeping the map fixed on the endpoint neighborhoods
from step <1>2. It gives an arbitrarily small smooth perturbation
$\gamma$ that is transverse to $Z$ and agrees with $\gamma_0$ there.
The original map $\gamma_0$ is an embedding because $a\neq b$.
Embeddings of the compact interval into $\RR^3$ are open in the
$C^1$ topology, so the perturbation may be chosen small enough that
$\gamma$ is still an embedding.
:::

<1>4. The arc $\gamma$ does not meet $Z$.

::: {.proof}
Suppose instead that
$$
z=\gamma(t)\in Z
$$
for some $t\in[0,1]$. Transversality would require
$$
D\gamma_t(T_t[0,1])+T_zZ=T_z\RR^3.
$$
The first summand has dimension at most $1$, and step <1>1 gives
$$
\dim T_zZ=1.
$$
Hence the left-hand side has dimension at most $2$, whereas
$$
\dim T_z\RR^3=3.
$$
This is impossible. Therefore
$$
\gamma([0,1])\cap Z=\varnothing.
$$
:::

<1>5. Any two distinct points of $\RR^3\setminus Z$ are joined by an
arc contained in $\RR^3\setminus Z$.

::: {.proof}
For arbitrary distinct $a,b\in\RR^3\setminus Z$, step <1>3 gives an
embedded arc from $a$ to $b$, and step <1>4 shows that its image lies
entirely in the complement.
:::

<1>6. Therefore
$$
\boxed{\RR^3\setminus f^{-1}(0)\text{ is arcwise connected}}.
$$

::: {.proof}
Step <1>5 is exactly the defining property of arcwise connectedness.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>6 is the required conclusion.
:::
:::
