---
schema: qual/card@1
id: P-CASP13E
kind: problem
title: "Blaschke-type condition for zeros of holomorphic functions in the upper half-plane"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: The card text asked for some $f\in\operatorname{Hol}(\CC_+)$ vanishing at every $i+x_n$, which $f\equiv0$ always satisfies and which a nonzero Weierstrass product satisfies for $x_n=\sqrt n$. The statement now asks for a bounded, not identically zero $f$.
---

::: {.problem}
Let $x_n$ be a sequence of distinct real numbers.
Show that there exists a bounded holomorphic function $f\not\equiv0$ on the upper half-plane $\CC_+$ such that $f(i + x_n) = 0$ for all $n$ if and only if $$\sum_n \frac{1}{x_n^2 + 4} < \infty.$$
:::

::: {.solution}
Let
\[
\phi(z)=\frac{z-i}{z+i},
\qquad
w_n=\phi(x_n+i)=\frac{x_n}{x_n+2i}.
\]
The Cayley map $\phi$ is a biholomorphism of $\CC_+$ onto the unit disk $\mathbb D$, and the points $w_n$ are distinct because $\phi$ is injective.

::: pf

::: {.pf-step #series}
$\sum_n 1/(x_n^2+4)<\infty$ if and only if $\sum_n(1-|w_n|)<\infty$.

::: pf-proof
We have $|w_n|^2=x_n^2/(x_n^2+4)$, so
\[
1-|w_n|^2=\frac{4}{x_n^2+4}.
\]
Since $0\le|w_n|<1$,
\[
1-|w_n|\le(1-|w_n|)(1+|w_n|)=1-|w_n|^2\le2(1-|w_n|).
\]
Hence the two series converge or diverge together.
:::

:::

::: {.pf-step #transfer}
A bounded $f\not\equiv0$ on $\CC_+$ vanishes at every $x_n+i$ if and only if $g=f\circ\phi^{-1}$ is a bounded $g\not\equiv0$ on $\mathbb D$ vanishing at every $w_n$.

::: pf-proof
Composition with the biholomorphism $\phi$ or $\phi^{-1}$ preserves holomorphy, boundedness, and the property of not being identically zero, and $g(w_n)=f(x_n+i)$.
:::

:::

::: {.pf-step #sufficient}
If $\sum_n(1-|w_n|)<\infty$, such a $g$ exists.

::: pf-proof
Under the Blaschke condition, the Blaschke product
\[
B(w)=\prod_n\frac{|w_n|}{w_n}\,\frac{w_n-w}{1-\overline{w_n}w}
\]
(with the factor $w$ in place of the $n$-th factor when $w_n=0$) converges locally uniformly on $\mathbb D$, satisfies $|B|\le1$, is not identically zero, and vanishes exactly at the $w_n$. Take $g=B$.
:::

:::

::: {.pf-step #necessary}
If such a $g$ exists, then $\sum_n(1-|w_n|)<\infty$.

::: pf-proof
Dividing $g$ by a power of $w$, which keeps it bounded on $\mathbb D$ (it is bounded near $|w|=1$, and holomorphic at $0$), we may assume $g(0)\neq0$; this removes at most one point $w_n=0$ from the zero set. Let $|g|\le M$. For $r<1$ avoiding $|w_n|$, Jensen's formula gives
\[
\log|g(0)|+\sum_{|w_n|<r}\log\frac{r}{|w_n|}
\le\frac1{2\pi}\int_0^{2\pi}\log|g(re^{it})|\,dt\le\log M,
\]
where the sum runs over a subset of the zeros of $g$ and every term is nonnegative. Letting $r\to1$ gives $\sum_n\log(1/|w_n|)\le\log(M/|g(0)|)<\infty$. Since $\log(1/t)\ge1-t$ for $0<t\le1$, the Blaschke condition follows.
:::

:::

::: pf-qed
By steps [](#transfer){.pf-ref}, [](#sufficient){.pf-ref} and [](#necessary){.pf-ref}, the required $f$ exists if and only if $\sum_n(1-|w_n|)<\infty$, and by step [](#series){.pf-ref} this holds if and only if $\sum_n 1/(x_n^2+4)<\infty$.
:::

:::

:::
