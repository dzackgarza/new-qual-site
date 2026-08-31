---
schema: qual/card@1
id: E-HAT-1.A-11
kind: exercise
title: Free groups are residually finite
classification:
  areas:
  - topology
  topics:
  - Free Groups
  - Covering Spaces
  - Finite Quotients
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

Apply the two preceding problems to show that if $F$ is a finitely generated free group and $x \in F$ is not the identity element, then there is a normal subgroup $H \subset F$ of finite index such that $x \notin H$.
Hence $x$ has nontrivial image in a finite quotient group of $F$.
In this situation one says $F$ is residually finite.

::: {.solution}
<1>1. Topological representation of $F$:
<2>1. Let $F = F_n$ be the free group of rank $n \ge 1$, and let $X = \bigvee_{i=1}^n S^1$ be a wedge sum of $n$ circles with basepoint $x_0$, so that $\pi_1(X, x_0) \cong F$.
::: {.proof}
fundamental group of a bouquet of circles.
:::
<2>2. Let $x \in F \setminus \{1\}$ be a non-trivial element, written as a non-empty reduced word $w = s_1 s_2 \cdots s_k$ in the generators and their inverses ($s_j \in \{a_1^{\pm 1}, \dots, a_n^{\pm 1}\}$ with $s_{j+1} \neq s_j^{-1}$).
::: {.proof}
reduced words in free groups.
:::

<1>2. Construction of a finite covering space separating $x$:
<2>1. Construct an initial directed labeled graph $\Gamma_0$ consisting of $k+1$ vertices $v_0, v_1, \dots, v_k$, with an edge labeled $s_j$ directed from $v_{j-1}$ to $v_j$ for each $j = 1, \dots, k$.
::: {.proof}
path graph realization of word $w$.
:::
<2>2. In $\Gamma_0$, the path from $v_0$ reading word $w$ terminates at $v_k \neq v_0$.
Since $w$ is reduced, at each vertex there is at most one incoming and one outgoing edge with each generator label $a_i$.
::: {.proof}
reduced word has no backtracking.
:::
<2>3. Complete $\Gamma_0$ to a finite regular $2n$-valent graph $\widetilde{X}$ by adding edges so that every vertex has exactly one incoming and one outgoing edge labeled by each generator $a_i$.
::: {.proof}
Hall's Marriage Theorem / permutation completion on finite bipartite deficiency graphs.
:::
<2>4. The graph $\widetilde{X}$ is a finite $d$-sheeted covering space $p: \widetilde{X} \to X$ with basepoint $\tilde{x}_0 = v_0$.
::: {.proof}
covering projection mapping edges of label $a_i$ to circle $a_i$.
:::
<2>5. The unique lift of the loop $x$ starting at $v_0$ terminates at $v_k \neq v_0$, which is not a closed loop.
Thus $x \notin K = p_*(\pi_1(\widetilde{X}, v_0))$.
Since $\widetilde{X}$ is a $d$-sheeted covering, $[F : K] = d < \infty$.
::: {.proof}
unique path lifting theorem.
:::

<1>3. Construction of a finite-index normal subgroup:
<2>1. Define the normal core of $K$ in $F$:
\[
H = \operatorname{Core}_F(K) = \bigcap_{g \in F} g K g^{-1}.
\]
::: {.proof}
definition of normal core.
:::
<2>2. $H$ is a normal subgroup of $F$, and by Poincaré’s Theorem on finite index subgroups:
\[
[F : H] \le [F : K]! = d! < \infty.
\]
::: {.proof}
action of $F$ by left multiplication on the cosets $F/K$.
:::
<2>3. Since $H \subseteq K$ and $x \notin K$, we have $x \notin H$.
::: {.proof}
subset containment.
:::
<2>4. In the finite quotient group $G = F/H$, the coset $xH \neq e_{F/H}$, so $x$ has non-trivial image in a finite quotient.
::: {.proof}
$x \notin H \iff xH \neq H$.
:::

<1>4. Conclusion:
For every $x \in F \setminus \{1\}$, there exists a finite-index normal subgroup $H \trianglelefteq F$ with $x \notin H$.
Thus every finitely generated free group is residually finite. Q.E.D.
::: {.proof}
<1>1 through <1>3.
:::
:::
