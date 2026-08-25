---
schema: qual/card@1
id: P-UCPPT
kind: problem
title: $m^*(E)=0$ iff $m^*(f(E))=0$ for $f(x)=x^2$ on $[0,\infty)$, and $E\mapsto
  f(E)$ bijects Lebesgue sets of $\RR^+$
classification:
  areas:
  - real-analysis
  topics:
  - Measure Theory
relations: []
review: draft
---

Let $f(x) = x^2$ and $E \subset [0, \infty) \definedas \RR^+$.

1. Show that
\[
m^*(E) = 0 \iff m^*(f(E)) = 0.
\]

2. Deduce that the map

\[
\phi: \mathcal{L}(\RR^+) &\to \mathcal{L}(\RR^+) \\
E &\mapsto f(E)
\]
  is a bijection from the class of Lebesgue measurable sets of $[0, \infty)$ to itself.

:::{.solution}
\envlist

a.

It suffices to consider the bounded case, i.e. $E \subseteq B_M(0)$ for some $M$.
Then write $E_n = B_n(0) \Intersect E$ and apply the theorem to $E_n$, and by subadditivity, $m^*(E) = m^*(\Union_n E_n) \leq \sum_n m^*(E_n) = 0$.

**Lemma:** 
$f(x) = x^2, f\inv(x) = \sqrt{x}$ are Lipschitz on any compact subset of $[0, \infty)$.
 
*Proof:*
Let $g = f$ or $f\inv$. 
Then $g\in C^1([0, M])$ for any $M$, so $g$ is differentiable and $g'$ is continuous.
Since $g'$ is continuous on a compact interval, it is bounded, so $\abs{g'(x)} \leq L$ for all $x$.
Applying the MVT,
\[
\abs{f(x) - f(y)} = f'(c) \abs{x-y} \leq L \abs{x-y}
.\]
  
**Lemma:** 
If $g$ is Lipschitz on $\RR^n$, then $m(E) = 0 \implies m(g(E)) = 0$.

*Proof:*
If $g$ is Lipschitz, then 
$$
g(B_r(x)) \subseteq B_{Lr}(x)
,$$ 
which is a dilated ball/cube, and so 
$$
m^*(B_{Lr}(x)) \leq L^n \cdot m^*(B_{r}(x))
.$$

Now choose $\theset{Q_j} \rightrightarrows E$; then $\theset{g(Q_j)} \rightrightarrows g(E)$.

By the above observation,
\[
\abs{g(Q_j)} \leq L^n \abs{Q_j}
,\]

and so 
\[
m^*(g(E)) \leq \sum_j \abs{g(Q_j)} \leq \sum_j L^n \abs{Q_j} = L^n \sum_j \abs{Q_j} \to 0 
.\]

Now just take $g(x) = x^2$ for one direction, and $g(x) = f\inv(x) = \sqrt{x}$ for the other.

b.

> Lemma: $E$ is measurable iff $E = K \disjoint N$ for some $K$ compact, $N$ null.

Write $E = K \disjoint N$ where $K$ is compact and $N$ is null.

Then $\phi\inv(E) = \phi\inv(K \disjoint N) = \phi\inv(K) \disjoint \phi\inv(N)$.

Since $\phi\inv(N)$ is null by part (a) and $\phi\inv(K)$ is the preimage of a compact set under a continuous map and thus compact, $\phi\inv(E) = K' \disjoint N'$ where $K'$ is compact and $N'$ is null, so $\phi\inv(E)$ is measurable.

So $\phi$ is a measurable function, and thus yields a well-defined map $\mathcal L(\RR) \to \mathcal L(\RR)$ since it preserves measurable sets.
Restricting to $[0, \infty)$, $f$ is bijection, and thus so is $\phi$.
:::

