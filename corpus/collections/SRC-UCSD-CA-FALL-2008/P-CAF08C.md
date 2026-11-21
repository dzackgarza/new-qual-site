---
schema: qual/card@1
id: P-CAF08C
kind: problem
title: "Pointwise limit of analytic functions with uniformly bounded derivatives is analytic"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Lamport structure. The chain is now: local bound from continuity of h on a compact closed disc, the mean value inequality for the Lipschitz bound (using convexity of the ball), uniform boundedness from the boundedness of the sequence at one point, Montel for the subsequential holomorphic limit, and the identification of that limit with the pointwise limit f. The prose asserted equicontinuity and uniform boundedness in words; both are now inequalities with the constants named. No retained solution set covers the exercise; the card says the argument is its own.
---

::: {.problem}
Let $G \subset \CC$ be open and connected, and let $h \in H(G)$.
Suppose that $\{f_n(z)\} \subset H(G)$ is a sequence of analytic functions for which $\lim_{n \to \infty} f_n(z)$ exists (and is finite) for every $z \in G$.
Put $f(z) := \lim_{n \to \infty} f_n(z)$.
Suppose that $\abs{f_n'(z)} \leq \abs{h(z)}$ for all $z \in G$.
Prove that $f \in H(G)$.
:::

::: {.solution}
The collection's provenance is the examination paper alone, so no retained solution set covers this exercise; the argument is the card's own.

::: pf

::: {.pf-step #localbounds}
Fix $z_0\in G$ and $r>0$ with $\overline{B(z_0,r)}\subseteq G$. There is $M<\infty$ with $\abs{f_n'(z)}\le M$ for all $n$ and all $z\in\overline{B(z_0,r)}$.

::: pf-proof
$G$ is open, so $r>0$ exists. $h$ is holomorphic hence continuous on $G$, so $\abs h$ attains a maximum $M$ on the compact set $\overline{B(z_0,r)}$. Then $\abs{f_n'(z)}\le\abs{h(z)}\le M$ by hypothesis.
:::

:::

::: {.pf-step #equicont}
$\abs{f_n(z)-f_n(w)}\le M\abs{z-w}$ for all $n$ and all $z,w\in\overline{B(z_0,r)}$.

::: pf-proof
The segment joining $z,w$ lies in $\overline{B(z_0,r)}$ because a ball is convex, so the mean value inequality applied to $f_n$ on that segment gives the bound.
:::

:::

::: {.pf-step #bounded}
$(f_n)$ is uniformly bounded on $\overline{B(z_0,r)}$.

::: pf-proof
The sequence $(f_n(z_0))$ converges, hence is bounded by some $C$. For $z\in\overline{B(z_0,r)}$, $\abs{f_n(z)}\le\abs{f_n(z_0)}+\abs{f_n(z)-f_n(z_0)}\le C+Mr$ by step [](#equicont){.pf-ref}.
:::

:::

::: {.pf-step #montel}
Every subsequence of $(f_n)$ has a further subsequence converging uniformly on compact subsets of $B(z_0,r)$ to a holomorphic function.

::: pf-proof
The family $(f_n)$ is holomorphic and uniformly bounded on $B(z_0,r)$ by step [](#bounded){.pf-ref}, so it is normal there: Montel's theorem gives, for each subsequence, a further subsequence converging uniformly on every compact subset of $B(z_0,r)$; the limit is holomorphic because a locally uniform limit of holomorphic functions is holomorphic.
:::

:::

::: {.pf-step #holomorphic}
$f$ is holomorphic on $B(z_0,r)$, hence on $G$.

::: pf-proof
Let $K\subseteq B(z_0,r)$ be compact and take the subsequence of step [](#montel){.pf-ref} converging uniformly on $K$ to a holomorphic $F$. Since $f_n\to f$ pointwise, $F=f$ on $K$; so $f$ agrees on a neighbourhood of each point of $B(z_0,r)$ with a holomorphic function, and is therefore holomorphic there. As $z_0\in G$ was arbitrary and the balls $B(z_0,r)$ cover $G$, $f$ is holomorphic on $G$.
:::

:::

:::
:::
