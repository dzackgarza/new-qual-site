---
schema: qual/card@1
id: P-CAF11A
kind: problem
title: "True or False: infinite products, bounded functions on punctured plane, essential singularities, growth rates, and Schwarz lemma"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: problem
For each of the following, determine if the statement is always true or if it is false.
If true, give a proof.
If false, give a counterexample.

(a) The infinite product $\prod_{n=1}^{\infty}\left(1 + \frac{i}{n}\right)$ converges absolutely.

(b) Let $G = \mathbb{C} \setminus (\mathbb{R} \cap \mathbb{Z})$.
Suppose $f \in H(G)$ such that $|f(z)| \leq 1$ for all $z \in G$.
Then $f$ is constant.

(c) There exists a function $f$ analytic in $B(1; 2) \setminus \{1\}$ such that $$\lim_{z \to 1} (z-1)^k f(z) = \infty, \quad \forall k \in \mathbb{Z},\; k \geq 1.$$

(d) There exists an entire function $f$ for which $\lim_{|z| \to \infty} \left|\frac{f(z)}{z^k}\right|$ does not exist for any positive $k \in \mathbb{Z}$.

(e) Let $f$ be an analytic function defined in a simply connected bounded domain $G \subset \mathbb{C}$ with $i \in G$.
If $f(G) \subset G$ and $f(i) = i$, then $|f'(i)| \leq 1$.
:::

::: solution
**(a) False.** Absolute convergence of an infinite product
$\prod(1+a_n)$ requires $\sum |a_n|<\infty$. Here
\[
\sum_{n=1}^\infty\left|\frac{i}{n}\right|
=\sum_{n=1}^\infty\frac1n
\]
diverges, so the product is not absolutely convergent.

**(b) True.** The omitted points are the integers. Since $f$ is bounded near
each integer, every singularity there is removable. Thus $f$ extends to a
bounded entire function on $\mathbb C$, and Liouville's theorem makes it
constant.

**(c) False.** Suppose such an $f$ existed. The condition with $k=1$ implies
that $f$ has no zeros sufficiently near $1$, so $g=1/f$ is holomorphic in a
punctured neighborhood of $1$ there. Moreover, for every $k\ge1$,
\[
\frac{g(z)}{(z-1)^k}=\frac{1}{(z-1)^k f(z)}\longrightarrow0.
\]
In particular $g$ is bounded and extends holomorphically across $1$ with
$g(1)=0$. The displayed limits imply that every derivative of the extension at
$1$ is zero. Hence its Taylor series is identically zero, so $g$ vanishes near
$1$, impossible because $g=1/f$ there.

**(d) True.** Take $f(z)=e^z$. For every positive integer $k$,
\[
\left|\frac{e^x}{x^k}\right|\to\infty
\qquad (x\to+\infty),
\]
whereas
\[
\left|\frac{e^{-x}}{(-x)^k}\right|\to0
\qquad (x\to+\infty).
\]
Thus no limit exists as $|z|\to\infty$.

**(e) True.** Since $G$ is bounded, it is a proper simply connected domain.
Choose a conformal map $\phi:G\to\mathbb D$ with $\phi(i)=0$. Then
\[
F=\phi\circ f\circ\phi^{-1}:\mathbb D\to\mathbb D
\]
fixes $0$. Schwarz's lemma gives $|F'(0)|\le1$. By the chain rule,
\[
F'(0)=\phi'(i)f'(i)(\phi^{-1})'(0)=f'(i),
\]
so $|f'(i)|\le1$.
:::
