---
schema: qual/card@1
id: P-CASP18F
kind: problem
title: "Pointwise convergence with bounded derivatives implies uniform convergence on compact subsets"
classification:
  areas:
  - complex-analysis
  topics:
  - Normal Families
  - Uniform Convergence
  - Holomorphic Functions
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Rewritten as a Lamport structured proof of the argument already on the card, correct as it
    stood. Added: the integral of f_n' along the segment giving the Lipschitz bound on each
    covering disk, with the maximum of the finitely many bounds; the sharpened continuity step,
    which computes |f(w) - f(w')| as the limit of |f_n(w) - f_n(w')| so that f inherits the
    Lipschitz bound (the prose's epsilon/3 argument chose n depending on the point w, which is
    not a proof); and the subsequence-and-limit-point contradiction for uniform convergence on a
    compact, with each of the three terms bounded by equicontinuity, pointwise convergence and
    continuity of f. Not claimed: a retained solution set; the provenance names the examination
    paper.
---

::: {.problem}
Let $\{f_n\}$ be a sequence in $H(G)$ such that $f_n(z)$ converges for every $z \in G$ to a complex value $f(z)$, i.e. $\lim_{n \to \infty} f_n(z) = f(z) \in \CC$.
Assume that $\abs{f_n'(z)} \leq h(z)$ for some continuous real-valued function $h$ in $G$.
Show that $f(z)$ is analytic in $G$ and $f_n \to f$ in $H(G)$.
:::

::: {.solution}
No retained solution set covers this problem: the collection's `provenance` names the Spring 2018 complex-analysis examination paper, which carries no solutions. The argument below is the card's own and follows the card's previous prose.

Throughout $G\subseteq\CC$ is open, $f_n\in H(G)$ converge pointwise to $f$, and $h$ is a continuous real-valued function on $G$ with $\abs{f_n'}\le h$ for every $n$.

::: pf

::: {.pf-step #equicontinuous}
For each compact $K\Subset G$ there is $M$ with $\abs{f_n(z)-f_n(w)}\le M\abs{z-w}$ whenever $z,w\in K$; hence the family is equicontinuous on $K$.

::: pf-proof
Since $K$ is compact and $G$ is open, finitely many closed disks $\overline{D_j}\Subset G$ cover $K$. The continuous $h$ is bounded on each compact $\overline{D_j}$, say by $M_j$. For $z,w\in D_j$ the segment $[z,w]$ lies in $D_j$, so
$$
\abs{f_n(z)-f_n(w)}=\Bigl|\int_0^1f_n'(w+t(z-w))(z-w)\,dt\Bigr|\le M_j\abs{z-w}
$$
for every $n$. Taking $M=\max_jM_j$ and shrinking the cover slightly so that the pieces remain at distance $>0$ from $\partial G$ gives the bound for $z,w\in K$; a uniform Lipschitz bound is equicontinuity.

:::

:::

::: {.pf-step #continuous}
$f$ is continuous.

::: pf-proof
Let $K\Subset G$ be a compact neighbourhood of $z$ and $M$ the constant of step [](#equicontinuous){.pf-ref}. For $w,w'\in K$,
$$
\abs{f(w)-f(w')}=\lim_{n\to\infty}\abs{f_n(w)-f_n(w')}\le M\abs{w-w'},
$$
because the bound of step [](#equicontinuous){.pf-ref} holds for every $n$ and limits preserve non-strict inequalities; so $f$ is Lipschitz, hence continuous, on $K$, and $z$ is an interior point of $K$.
:::

:::

::: {.pf-step #uniform}
$f_n\to f$ uniformly on every compact $K\Subset G$.

::: pf-proof
Suppose not. Then there are $\varepsilon>0$, a subsequence $f_{n_k}$ and points $z_k\in K$ with $\abs{f_{n_k}(z_k)-f(z_k)}\ge\varepsilon$. Passing to a subsequence, $z_k\to z\in K$ (compactness). Then
$$
\abs{f_{n_k}(z_k)-f(z_k)}\le\abs{f_{n_k}(z_k)-f_{n_k}(z)}+\abs{f_{n_k}(z)-f(z)}+\abs{f(z)-f(z_k)},
$$
where the first term is at most $M\abs{z_k-z}\to0$ by step [](#equicontinuous){.pf-ref}, the second tends to $0$ by pointwise convergence at $z$, and the third tends to $0$ by continuity of $f$ at $z$; the whole right side tends to $0$, contradicting the lower bound $\varepsilon$.

:::

:::

::: {.pf-step #analytic}
$f\in H(G)$, and $f_n\to f$ in $H(G)$.

::: pf-proof
By step [](#uniform){.pf-ref} the convergence is uniform on every compact subset of $G$; the Weierstrass theorem on locally uniform limits of holomorphic functions then gives that $f$ is holomorphic on $G$, and $f_n\to f$ uniformly on compacts is precisely convergence in $H(G)$.

:::

:::

:::
:::
