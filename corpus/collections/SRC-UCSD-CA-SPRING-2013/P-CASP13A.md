---
schema: qual/card@1
id: P-CASP13A
kind: problem
title: 'Classical complex-analysis theorems: statements and proof sketches'
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: {.problem}
Choose 4 of the following theorems, and write out their statements carefully and completely.
From among these, choose 2, and sketch their proofs.

- The Cauchy Estimates and Liouville's Theorem

- Rouché's Theorem

- Hurwitz's Theorem

- The Riemann Mapping Theorem

- Runge's Theorem

- The Open Mapping Theorem

- The Mittag-Leffler Theorem

- The Maximum Modulus Principle

- The Monodromy Theorem

- The Great Picard Theorem

- Carathéodory's Theorem

- The Poisson Integral Formula
:::

::: {.solution}

The four statements are the standard ones and are quoted as the exercise asks; the two sketches are the card's own write-ups, and the Rouché step used inside the second is stated among the four, so it is not borrowed from outside the card.

This is a different examination question from the one on [[P-CAF13A]]: the candidate list differs, and so do the four results chosen.

::: pf

::: {.pf-step #rouche}
Statement, Rouché's theorem. Let $D$ be a bounded domain whose boundary is a finite union of positively oriented simple closed curves, and let $f,g$ be holomorphic on a neighbourhood of $\overline D$. If $\abs{g(z)}<\abs{f(z)}$ for $z\in\partial D$, then $f$ and $f+g$ have the same number of zeros in $D$, counted with multiplicity.

::: pf-proof
Quoted, as asked. The boundary condition makes $f$ zero-free on $\partial D$, so both zero counts are finite and defined; the strict inequality is on the boundary only, and multiplicities are counted.
:::

:::

::: {.pf-step #hurwitz}
Statement, Hurwitz's theorem. Let $G$ be a domain and $f_{n}$ holomorphic and zero-free on $G$. If $f_{n}\to f$ uniformly on compact subsets of $G$, then $f$ is either zero-free or identically zero.

::: pf-proof
Quoted, as asked, with the equivalent form it is usually used in: if $f\not\equiv0$ has a zero at $a\in G$, then every sufficiently small disc about $a$ contains a zero of $f_{n}$ for all sufficiently large $n$. Local uniform convergence makes $f$ holomorphic and gives both statements at once, since $f$ is the locally uniform limit and the two alternatives are exactly "no zeros" or "the zero set of a holomorphic function".
:::

:::

::: {.pf-step #riemann}
Statement, the Riemann mapping theorem. Every nonempty simply connected proper domain $G\subsetneq\CC$ is conformally equivalent to $\DD$; and for $a\in G$ there is a unique conformal $F:G\to\DD$ with $F(a)=0$ and $F'(a)>0$.

::: pf-proof
Quoted, as asked. "Proper" means $G\ne\CC$, which is necessary since $\CC$ is simply connected and not conformally equivalent to $\DD$ (Liouville); the normalisation $F(a)=0$, $F'(a)>0$ pins the map among the many that exist.
:::

:::

::: {.pf-step #open-mapping}
Statement, the open mapping theorem. A nonconstant holomorphic function on a domain maps open sets to open sets.

::: pf-proof
Quoted, as asked. Nonconstancy is essential — a constant map has image a point — and the conclusion is that the image of every open subset is open, which for a holomorphic map on a domain is equivalent to $f(G)$ being open.
:::

:::

::: {.pf-step #sketch-rouche}
Sketch of Rouché's theorem: the homotopy $f_{t}=f+tg$ stays zero-free on $\partial D$, so the winding number of $f_{t}(\partial D)$ about $0$ is constant, and the argument principle identifies it with the zero count.

::: pf-proof
For $0\le t\le1$ and $z\in\partial D$,
$$
\abs{f_{t}(z)}=\abs{f(z)+tg(z)}\ge\abs{f(z)}-t\abs{g(z)}\ge\abs{f(z)}-\abs{g(z)}>0,
$$
so $f_{t}$ has no zero on $\partial D$ and $f_{t}$ is holomorphic on a neighbourhood of $\overline D$. The winding number $n(t)$ of the closed curve $f_{t}\circ\gamma$ about $0$, for $\gamma$ traversing $\partial D$ positively, depends continuously on $t$ and is integer valued, hence is constant: $n(0)=n(1)$. By the argument principle applied to $f_{t}$ on $D$,
$$
n(t)=\frac{1}{2\pi i}\int_{\partial D}\frac{f_{t}'(z)}{f_{t}(z)}\,dz=N(t)-P(t)=N(t),
$$
$f_{t}$ having no poles, where $N(t)$ is the number of zeros of $f_{t}$ in $D$ counted with multiplicity. Hence $N(0)=N(1)$, that is $f=f_{0}$ and $f+g=f_{1}$ have the same number of zeros in $D$.
:::

:::

::: {.pf-step #sketch-open-mapping}
Sketch of the open mapping theorem: the local normal form together with Rouché's theorem about a circle.

::: pf-proof
Let $z_{0}\in G$. Since $f$ is nonconstant and holomorphic, $f(z)-f(z_{0})$ has a zero of finite order $m\ge1$ at $z_{0}$, so $f(z)-f(z_{0})=(z-z_{0})^{m}h(z)$ with $h(z_{0})\ne0$. Choose $r>0$ with $\overline{B(z_{0},r)}\subset G$ and $h$ zero-free there; then $f(z)-f(z_{0})$ vanishes on that disc only at $z_{0}$. On the circle $\abs{z-z_{0}}=r$ the continuous function $\abs{f(z)-f(z_{0})}$ attains a minimum $\delta>0$. If $\abs{w-f(z_{0})}<\delta$, then on that circle
$$
\abs{(f(z)-w)-\big(f(z)-f(z_{0})\big)}=\abs{w-f(z_{0})}<\delta\le\abs{f(z)-f(z_{0})},
$$
so step [](#rouche){.pf-ref} applies on the domain $D=B(z_{0},r)$ with $f$ replaced by $f-f(z_{0})$ and $g$ replaced by $f(z_{0})-w$: the functions $f-w$ and $f-f(z_{0})$ have the same number of zeros in $D$, namely $m\ge1$. Hence $w=f(z)$ for some $z\in D$, so $B(f(z_{0}),\delta)\subset f(G)$ and $f(G)$ is open.
:::

:::

:::
:::
