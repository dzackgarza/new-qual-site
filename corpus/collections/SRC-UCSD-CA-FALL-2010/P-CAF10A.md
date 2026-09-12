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

::: problem
Determine if the following statements are True or False.
If True, give a brief proof.
If False, give a counterexample or prove your assertion otherwise.

(a) Let $f(z) = \sum_{n=0}^{\infty} a_n z^n$ have radius of convergence $R$.
If $|a| = R$ and the power series does not converge at $z = a$, then $f(z)$ cannot be analytically continued to an open neighborhood of $a$.

(b) Let $f$ and $g$ be analytic functions defined in an open set $G \subset \mathbb{C}$.
If for some $a \in G$, $[f]_a = [g]_a$ (where $[f]_a$ and $[g]_a$ denote the germs of $f$ and $g$ at $a$ respectively), then $f(z) = g(z)$ for all $z \in G$.

(c) Let $(X, d)$ be a metric space, $x \in X$, and $\{x_n\}_{n=1}^{\infty}$ a sequence in $X$.
If every subsequence of $\{x_n\}_{n=1}^{\infty}$ has a subsequence that converges to $x$, then $\{x_n\}_{n=1}^{\infty}$ converges to $x$.

(d) Let $G$ denote the intersection between the disks given by $|z - 2| < 3$ and $|z + 2| < 3$.
For any two points $a, b \in G$, there exists an automorphism of $G$ (i.e.\ an analytic bijection of $G$ onto itself) sending $a$ to $b$.
:::

::: solution
**(a) False.** Consider
\[
f(z)=\frac1{1+z}=\sum_{n=0}^\infty(-1)^n z^n,
\qquad |z|<1.
\]
The radius of convergence is $R=1$. At $a=1$ the series
$\sum(-1)^n$ does not converge, but $1/(1+z)$ is analytic in a neighborhood
of $1$.

**(b) False.** Connectedness of $G$ is missing. For example, let
\[
G=B(0,1)\cup B(3,1),
\]
let $f\equiv0$, and define $g=0$ on $B(0,1)$ and $g=1$ on $B(3,1)$.
Then $f$ and $g$ are analytic on $G$ and have the same germ at $a=0$, but
$f\ne g$ on $G$.

**(c) True.** If $x_n$ did not converge to $x$, there would exist
$\varepsilon>0$ and a subsequence $(x_{n_k})$ with
\[
d(x_{n_k},x)\ge\varepsilon
\]
for every $k$. No subsequence of $(x_{n_k})$ could converge to $x$, contrary
to the hypothesis.

**(d) True.** The set $G$ is a nonempty simply connected proper domain: it is
the intersection of two convex disks, hence convex. By the Riemann mapping
theorem choose a biholomorphism
\[
\phi:G\to\mathbb D.
\]
The automorphism group of $\mathbb D$ acts transitively. Thus there is a disk
automorphism $T$ with $T(\phi(a))=\phi(b)$, and
\[
\phi^{-1}\circ T\circ\phi
\]
is an automorphism of $G$ sending $a$ to $b$.
:::
