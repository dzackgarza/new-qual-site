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

::: {.problem}
For each of the following, determine if the statement is always true or if it is false.
If true, give a proof.
If false, give a counterexample.

(a) The infinite product $\prod_{n=1}^{\infty}\left(1 + \frac{i}{n}\right)$ converges absolutely.

(b) Let $G = \CC \setminus (\RR \cap \ZZ)$.
Suppose $f \in H(G)$ such that $\abs{f(z)} \leq 1$ for all $z \in G$.
Then $f$ is constant.

(c) There exists a function $f$ analytic in $B(1; 2) \setminus \{1\}$ such that $$\lim_{z \to 1} (z-1)^k f(z) = \infty, \quad \forall k \in \ZZ,\; k \geq 1.$$

(d) There exists an entire function $f$ for which $\lim_{\abs{z} \to \infty} \abs{\frac{f(z)}{z^k}}$ does not exist for any positive $k \in \ZZ$.

(e) Let $f$ be an analytic function defined in a simply connected bounded domain $G \subset \CC$ with $i \in G$.
If $f(G) \subset G$ and $f(i) = i$, then $\abs{f'(i)} \leq 1$.
:::

::: {.solution}

The five verdicts and their witnesses are the card's own; no retained set solves this exercise, and the sets searched are recorded in the audit trail.

::: pf

::: {.pf-step #a}
(a) False: $\prod_{n\ge1}\big(1+\tfrac{i}{n}\big)$ does not converge absolutely.

::: pf-proof
An infinite product $\prod_{n}(1+a_{n})$ with $1+a_{n}\ne0$ converges absolutely exactly when $\sum_{n}\abs{a_{n}}$ converges, by the comparison of $\abs{\log(1+a_{n})}$ with $\abs{a_{n}}$ for small $\abs{a_{n}}$ and the divergence of the product when $\abs{a_{n}}\ge1/2$ infinitely often. Here $a_{n}=i/n$, so $\sum_{n}\abs{a_{n}}=\sum_{n}1/n=\infty$, and the product is not absolutely convergent.
:::

:::

::: {.pf-step #b}
(b) True: if $f\in H(\CC\setminus\ZZ)$ and $\abs{f}\le1$ then $f$ is constant.

::: pf-proof
Each integer $m$ is an isolated point of the complement $\ZZ$, so $m$ is an isolated singularity of $f$, and $f$ is bounded in a punctured neighbourhood of $m$ because $\abs f\le1$ on the domain. A bounded isolated singularity is removable (Riemann's removable singularity theorem), so $f$ extends to an entire function $\widetilde f$ with $\abs{\widetilde f}\le1$ everywhere. A bounded entire function is constant (Liouville's theorem), so $f$ is constant.
:::

:::

::: {.pf-step #c}
(c) False: there is no $f$ analytic on $B(1;2)\setminus\{1\}$ with $\lim_{z\to1}(z-1)^{k}f(z)=\infty$ for every $k\ge1$.

::: pf-proof
Suppose $f$ were such a function. With $k=1$, $\abs{(z-1)f(z)}\to\infty$, so for $z$ close enough to $1$, $z\ne1$, one has $\abs{(z-1)f(z)}>1$, in particular $f(z)\ne0$; hence $g=1/f$ is holomorphic on a punctured neighbourhood of $1$. For every $k\ge1$,
$$
\frac{g(z)}{(z-1)^{k}}=\frac{1}{(z-1)^{k}f(z)}\longrightarrow0\qquad(z\to1),
$$
so in particular $g(z)/(z-1)\to0$: $g$ is bounded near $1$ and extends holomorphically across $1$ with $g(1)=0$. Writing $g(z)=\sum_{j\ge0}c_{j}(z-1)^{j}$ for the extension, the limit $\abs{g(z)/(z-1)^{k}}\to0$ for $k=1,2,\ldots$ forces $c_{k-1}=0$ for every $k\ge1$, so every $c_{j}=0$ and $g$ vanishes identically near $1$. But $g=1/f$ is nowhere zero on the punctured neighbourhood, a contradiction.
:::

:::

::: {.pf-step #d}
(d) True: for $f(z)=e^{z}$ the limit $\lim_{\abs{z}\to\infty}\abs{f(z)/z^{k}}$ fails to exist for every positive integer $k$.

::: pf-proof
Fix $k\ge1$ and take $z=x>0$ real: $\abs{e^{x}/x^{k}}=e^{x}/x^{k}\to\infty$ as $x\to+\infty$. Take $z=-x$ with $x>0$: $\abs{e^{-x}/(-x)^{k}}=e^{-x}/x^{k}\to0$ as $x\to+\infty$. Both families run off to $\abs{z}\to\infty$, so the expression is unbounded along one and tends to $0$ along the other; a limit as $\abs{z}\to\infty$ would have to be approached along every such family, so no limit exists, neither finite nor infinite.
:::

:::

::: {.pf-step #e}
(e) True: for a bounded simply connected domain $G$, $f(G)\subset G$ analytic and $f(i)=i$, one has $\abs{f'(i)}\le1$.

::: pf-proof
A bounded simply connected proper domain is conformally equivalent to $\DD$ (Riemann mapping theorem), so choose a biholomorphism $\phi:G\to\DD$ with $\phi(i)=0$. Then $F=\phi\circ f\circ\phi^{-1}$ is holomorphic on $\DD$ with values in $\phi(G)\subset\DD$ and $F(0)=\phi(f(i))=\phi(i)=0$; Schwarz's lemma gives $\abs{F'(0)}\le1$. By the chain rule
$$
F'(0)=\phi'(i)\,f'(i)\,(\phi^{-1})'(0)=\phi'(i)\,f'(i)\cdot\frac{1}{\phi'(i)}=f'(i),
$$
using $(\phi^{-1})'(0)=1/\phi'(\phi^{-1}(0))=1/\phi'(i)$, which is legitimate because a biholomorphism has nonvanishing derivative. Hence $\abs{f'(i)}=\abs{F'(0)}\le1$.
:::

:::

:::
:::
