---
schema: qual/card@1
id: P-CASP04D
kind: problem
title: "Basin of attraction of a fixed point with contraction coefficient"
classification:
  areas:
    - complex-analysis
  topics:
    - Iteration
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured the prose solution into a Lamport proof, re-deriving each step: the
    contraction estimate on a disc, invariance of that disc, the iterate bound by
    induction, Montel normality from boundedness of G, the identity theorem on the
    connected G, and the contradiction that upgrades every convergent subsequence to
    the whole sequence. The collection's provenance is the examination paper only, so
    no retained solution set covers the exercise and the argument is the card's own.
    Not verified: whether a published solution exists outside the repository.
---

::: {.problem}
Let $G$ be an open connected and bounded subset of $\CC$, and $f: G \to \CC$ an analytic function with $f(G) \subset G$.
Let $f^n$ denote the $n$th iterate of $f$.
Suppose that $a \in G$ is a fixed point of $f$ (i.e.\ $f(a) = a$) and $\abs{f'(a)} < 1$.
Define the basin of attraction of $z = a$ to be the set $$\Omega := \{z \in G : \lim_{n \to \infty} f^n(z) = a\}.$$

(a) Show that there is a $\delta > 0$ such that $\{z : \abs{z - a} < \delta\} \subset \Omega$.

(b) Show, using part (a), that in fact $\Omega = G$.
:::

::: {.solution}
The collection's provenance is the examination paper alone, so no retained solution set covers this exercise; the argument is the card's own.

::: pf

::: {.pf-step #contraction}
There are $q$ with $\abs{f'(a)}<q<1$ and $\delta>0$ with $B(a,\delta)\subset G$ such that
$$
\abs{f(z)-a}\le q\abs{z-a}\qquad\text{whenever}\qquad \abs{z-a}<\delta .
$$

::: pf-proof
Choose $q$ with $\abs{f'(a)}<q<1$. Since $f(a)=a$, the difference quotient at $a$ is $\frac{f(z)-a}{z-a}$, and it tends to $f'(a)$ as $z\to a$ because $f$ is analytic on the open set $G\ni a$. So there is $\delta_1>0$ with
$$
\abs{\frac{f(z)-a}{z-a}-f'(a)}<q-\abs{f'(a)}
$$
for $0<\abs{z-a}<\delta_1$, whence $\abs{f(z)-a}\le q\abs{z-a}$ on that punctured disc; the inequality also holds at $z=a$, where both sides vanish. Finally $G$ is open, so $\delta\coloneqq\min\{\delta_1,\delta_2\}$ works for any $\delta_2>0$ with $B(a,\delta_2)\subset G$.
:::

:::

::: {.pf-step #invariant}
$f\bigl(B(a,\delta)\bigr)\subset B(a,\delta)$.

::: pf-proof
For $\abs{z-a}<\delta$, step [](#contraction){.pf-ref} gives $\abs{f(z)-a}\le q\abs{z-a}<q\delta<\delta$.
:::

:::

::: {.pf-step #iterates}
For every $n\ge0$ and every $z$ with $\abs{z-a}<\delta$ the iterate $f^n(z)$ is defined and
$$
\abs{f^n(z)-a}\le q^n\abs{z-a}.
$$

::: pf-proof
Induction on $n$. For $n=0$ the assertion is an equality. If $\abs{f^n(z)-a}\le q^n\abs{z-a}<\delta$, then $f^n(z)\in B(a,\delta)$, so $f^{n+1}(z)=f\bigl(f^n(z)\bigr)$ is defined and, by step [](#contraction){.pf-ref},
$$
\abs{f^{n+1}(z)-a}\le q\abs{f^n(z)-a}\le q^{n+1}\abs{z-a}.
$$
:::

:::

::: {.pf-step}
(a) With $\delta$ as in step [](#contraction){.pf-ref}, $B(a,\delta)\subset\Omega$.

::: pf-proof
Let $\abs{z-a}<\delta$. Then $z\in B(a,\delta)\subset G$, so $z$ lies in the domain of every iterate, and by step [](#iterates){.pf-ref}
$$
\abs{f^n(z)-a}\le q^n\abs{z-a}\longrightarrow0
$$
because $0<q<1$. Hence $f^n(z)\to a$, that is $z\in\Omega$.
:::

:::

::: {.pf-step #normal}
The family of iterates $\{f^n:n\ge0\}$ is normal on $G$.

::: pf-proof
$f(G)\subset G$ by hypothesis, so $f^n(G)\subset G$ for every $n$ by induction. Since $G$ is bounded there is $M$ with $\abs{w}\le M$ for $w\in G$, so $\abs{f^n(z)}\le M$ for all $n$ and all $z\in G$. The family is thus uniformly bounded, hence locally bounded, and Montel's theorem makes a locally bounded family of holomorphic functions on the open set $G$ normal.
:::

:::

::: {.pf-step #limit-is-a}
If a subsequence $(f^{n_j})$ converges locally uniformly on $G$ to a function $F$, then $F\equiv a$.

::: pf-proof
Local uniform convergence preserves holomorphy, so $F$ is holomorphic on $G$. On the disc of step [](#contraction){.pf-ref} the whole sequence converges: by step [](#iterates){.pf-ref}, $\abs{f^n(z)-a}\le q^n r$ for $\abs{z-a}\le r<\delta$, so $f^n\to a$ uniformly on each compact subset of $B(a,\delta)$, and therefore $F=a$ on $B(a,\delta)$. That disc is a nonempty open subset of the connected set $G$, so the identity theorem gives $F\equiv a$ on $G$.
:::

:::

::: {.pf-step #converges}
$f^n\to a$ locally uniformly on $G$.

::: pf-proof

::: pf-step
Suppose not. There are then a compact $K\subset G$, an $\varepsilon>0$ and indices $n_j\to\infty$ with $\sup_{z\in K}\abs{f^{n_j}(z)-a}\ge\varepsilon$ for all $j$.
:::

::: pf-step
That is impossible.

::: pf-proof
By step [](#normal){.pf-ref} the subsequence $(f^{n_j})$ has a further subsequence converging locally uniformly on $G$ to a holomorphic $F$, and by step [](#limit-is-a){.pf-ref} that limit is $F\equiv a$. Uniform convergence on the compact set $K$ then gives $\sup_{z\in K}\abs{f^{n_{j}}(z)-a}\to0$ along the further subsequence, contradicting the bound $\varepsilon$.
:::

:::

:::

:::

::: {.pf-step}
(b) $\Omega=G$.

::: pf-proof
$\Omega\subset G$ by definition. Conversely let $z\in G$. By step [](#converges){.pf-ref} the sequence $f^n$ converges to $a$ locally uniformly on $G$, hence converges at the point $z$; that is $f^n(z)\to a$ and $z\in\Omega$. Therefore $\boxed{\Omega=G}$.
:::

:::

:::

:::
