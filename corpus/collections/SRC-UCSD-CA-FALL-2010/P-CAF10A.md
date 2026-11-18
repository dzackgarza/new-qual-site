---
schema: qual/card@1
id: P-CAF10A
kind: problem
title: "True or False: analytic continuation, germs, subsequences, and domain automorphisms"
classification:
  areas:
  - complex-analysis
  topics:
  - Analytic Continuation
  - Radius of Convergence
  - Point-Set Topology
  - Automorphisms
relations: []
review: draft
---

::: {.problem}
Determine if the following statements are True or False.
If True, give a brief proof.
If False, give a counterexample or prove your assertion otherwise.

(a) Let $f(z) = \sum_{n=0}^{\infty} a_n z^n$ have radius of convergence $R$.
If $\abs{a} = R$ and the power series does not converge at $z = a$, then $f(z)$ cannot be analytically continued to an open neighborhood of $a$.

(b) Let $f$ and $g$ be analytic functions defined in an open set $G \subset \CC$.
If for some $a \in G$, $[f]_a = [g]_a$ (where $[f]_a$ and $[g]_a$ denote the germs of $f$ and $g$ at $a$ respectively), then $f(z) = g(z)$ for all $z \in G$.

(c) Let $(X, d)$ be a metric space, $x \in X$, and $\{x_n\}_{n=1}^{\infty}$ a sequence in $X$.
If every subsequence of $\{x_n\}_{n=1}^{\infty}$ has a subsequence that converges to $x$, then $\{x_n\}_{n=1}^{\infty}$ converges to $x$.

(d) Let $G$ denote the intersection between the disks given by $\abs{z - 2} < 3$ and $\abs{z + 2} < 3$.
For any two points $a, b \in G$, there exists an automorphism of $G$ (i.e.\ an analytic bijection of $G$ onto itself) sending $a$ to $b$.
:::

::: {.solution}

No retained solution set covers this exercise: the card's own four answers are checked here, with the counterexamples verified and the two proofs completed.

::: pf

::: {.pf-step #a}
(a) False.

::: pf-proof
$f(z)=1/(1+z)=\sum(-1)^{n}z^{n}$ has radius of convergence $R=1$ by the ratio test, and at $a=1$, with $\abs a=R$, the series $\sum(-1)^{n}$ diverges since its terms do not tend to $0$. Yet $1/(1+z)$ is holomorphic on $\CC\setminus\{-1\}$, which is a neighbourhood of $1$. So the failure of convergence at $a$ does not prevent analytic continuation across $a$.
:::

:::

::: {.pf-step #b}
(b) False, unless $G$ is a region.

::: pf-proof
Take $G=B(0,1)\cup B(3,1)$, which is open but not connected, and let $f\equiv0$ and $g=0$ on $B(0,1)$, $g=1$ on $B(3,1)$; both are analytic on $G$, since $G$ is a disjoint union of two open discs and each piece is constant. At $a=0$ the germs agree because $f=g$ on $B(0,1)$, but $f\ne g$ on $B(3,1)$. The identity theorem applies only on a connected $G$, which is exactly the missing hypothesis.
:::

:::

::: {.pf-step #c}
(c) True.

::: pf-proof
Suppose $x_{n}\not\to x$. Then there is $\varepsilon>0$ such that for every $N$ there is $n\ge N$ with $d(x_{n},x)\ge\varepsilon$; choosing such $n_{k}$ inductively with $n_{k+1}>n_{k}$ gives a subsequence $(x_{n_{k}})$ with $d(x_{n_{k}},x)\ge\varepsilon$ for all $k$. Every subsequence of $(x_{n_{k}})$ stays at distance $\ge\varepsilon$ from $x$, so none converges to $x$, contradicting the hypothesis.
:::

:::

::: {.pf-step #d}
(d) True.

::: pf-proof
$G$ is the intersection of the open discs $B(2,3)$ and $B(-2,3)$, hence open, convex (an intersection of convex sets) and nonempty ($0\in G$). It is proper (not all of $\CC$): if $z\in G$ then $2\abs z=\abs{(z-2)+(z+2)}<6$, so $G\subseteq B(0,3)$ is bounded, and a bounded domain is a proper subset of $\CC$. Being open, convex and nonempty, $G$ is a simply connected domain, so by the Riemann mapping theorem there is a biholomorphism $\phi:G\to\DD$. By the Riemann mapping theorem there is a biholomorphism $\phi:G\to\DD$; for $a\in G$ compose with the disc automorphism $w\mapsto(w-\phi(a))/(1-\overline{\phi(a)}w)$ so that some biholomorphism sends $a$ to $0$. Then for $a,b\in G$ the map $\phi^{-1}\circ T\circ\phi$, where $T$ is the disc automorphism sending $\phi(a)$ to $\phi(b)$, is an automorphism of $G$ sending $a$ to $b$; $T$ exists since $w\mapsto(w-\phi(a))/(1-\overline{\phi(a)}w)$ followed by a rotation $w\mapsto e^{i\theta}w$ can be arranged to hit any prescribed point of $\DD$.
:::

:::

::: {.pf-qed}
(a) is false by step [](#a){.pf-ref}, (b) false by step [](#b){.pf-ref}, (c) true by step [](#c){.pf-ref}, (d) true by step [](#d){.pf-ref}.
:::

:::

:::
