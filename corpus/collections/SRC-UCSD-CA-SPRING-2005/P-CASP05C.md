---
schema: qual/card@1
id: P-CASP05C
kind: problem
title: "Schwarz lemma variants: identity for simply connected and bounded domains"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
  - event: solution-reviewed
    by: claude
    date: 2026-11-18
    note: >-
      Restructured into Lamport steps, and the audit list this card lacked is created here. The
      source is a course examination, so there is no retained solution set behind the card and the
      problem statement is the source. Each part re-read: in (a) the Riemann map is normalised at
      0, the conjugated map has derivative 1 at 0 by the chain rule, and the equality case of
      Schwarz forces the identity; the case G = CC is refuted by z + z^2. In (b) the iterate
      formula f^n(z) = z + n a_m z^m + O(z^{m+1}) is proved by induction, and the uniform Cauchy
      estimate on the coefficient of z^m over the bounded domain gives the contradiction. The
      bound is uniform because every iterate maps G into the bounded set G. Not claimed: any
      statement for unbounded non-simply-connected G, where neither argument applies.
---

::: {.problem}
Let $G \subset \CC$ be a connected open set with $0 \in G$, and $f \in H(G)$, with $f(0) = 0$, $f'(0) = 1$ and $f(G) \subset G$.

(a) Show that if $G \neq \CC$ and $G$ is simply connected (not necessarily bounded) then $f(z) \equiv z$.
Does the same conclusion hold for $G = \CC$?

(b) Show that if $G$ is bounded (not necessarily simply connected) then $f(z) \equiv z$.

Hint for (b): Prove by contradiction.
Consider the $n$th iterate $f_n := f \circ f \circ \cdots \circ f$ ($n$ times), and compute the first non-vanishing coefficient of the Taylor series of $f_n(z) - z$ at 0 in terms of that of $f(z) - z$.
:::

::: {.solution}
The argument is the card's own; the collection is a course examination, so there is no printed solution set behind the card and the problem statement is the source.

::: pf

::: {.pf-step #parta}
If $G\ne\CC$ is simply connected and $f(G)\subseteq G$ with $f(0)=0$, $f'(0)=1$, then $f=\mathrm{id}$.

:::: pf-proof

::: {.pf-step #riemann}
There is a biholomorphism $\phi:G\to\DD$ with $\phi(0)=0$.

::: pf-proof
The Riemann mapping theorem gives a biholomorphism onto $\DD$; composing it with an automorphism of the disc sending the image of $0$ to $0$ gives one with $\phi(0)=0$.
:::

:::

::: {.pf-step #schwarz}
$F=\phi\circ f\circ\phi^{-1}$ is a self-map of $\DD$ fixing $0$ with $F'(0)=1$.

::: pf-proof
$F$ is holomorphic on $\DD$ with values in $\DD$, and $F(0)=\phi(f(0))=\phi(0)=0$. By the chain rule $F'(0)=\phi'(f(0))\,f'(0)\,(\phi^{-1})'(0)=\phi'(0)\cdot1\cdot\frac{1}{\phi'(0)}=1$.
:::

:::

::: {.pf-step #identity}
$F=\mathrm{id}$ and hence $f=\mathrm{id}$.

::: pf-proof
Schwarz's lemma gives $\abs{F(w)}\le\abs{w}$, and its equality case applies at the point $w=0$ because $\abs{F'(0)}=1$: a self-map of the disc fixing $0$ with derivative of modulus $1$ there is a rotation, and the rotation is trivial since $F'(0)=1$. So $F(w)=w$ for all $w$, and $f=\phi^{-1}\circ F\circ\phi=\mathrm{id}$.
:::

:::

:::

:::

::: {.pf-step #wholeplane}
For $G=\CC$ the conclusion fails.

::: pf-proof
$f(z)=z+z^{2}$ is entire, satisfies $f(0)=0$ and $f'(0)=1$, maps $\CC$ into $\CC$, and is not the identity. So the hypothesis $G\ne\CC$ in part (a) cannot be dropped.
:::

:::

::: {.pf-step #partb}
If $G$ is bounded and $f(G)\subseteq G$ with $f(0)=0$, $f'(0)=1$, then $f=\mathrm{id}$.

:::: pf-proof

::: {.pf-step #expansion}
If $f\ne\mathrm{id}$ then $f(z)=z+a_{m}z^{m}+O(z^{m+1})$ near $0$ with $m\ge2$ and $a_{m}\ne0$.

::: pf-proof
$f$ is holomorphic at $0$ with $f(0)=0$ and $f'(0)=1$, so its Taylor series is $z+\sum_{j\ge2}a_{j}z^{j}$; if all $a_{j}$ with $j\ge2$ vanished then $f=\mathrm{id}$ near $0$ and, $G$ being connected, everywhere. So some first index $m\ge2$ has $a_{m}\ne0$.
:::

:::

::: {.pf-step #iterates}
$f^{\circ n}(z)=z+n\,a_{m}z^{m}+O(z^{m+1})$ near $0$, for every $n\ge1$.

::: pf-proof
Induction on $n$. The case $n=1$ is step [](#expansion){.pf-ref}. If $g(z)=z+n a_{m}z^{m}+O(z^{m+1})$ then $f(g(z))=g(z)+a_{m}g(z)^{m}+O(g(z)^{m+1})=z+n a_{m}z^{m}+a_{m}z^{m}+O(z^{m+1})$, since $g(z)^{m}=z^{m}+O(z^{m+1})$; this is the formula for $n+1$.
:::

:::

::: {.pf-step #bounded}
The coefficients of the iterates are uniformly bounded.

::: pf-proof
Choose $r>0$ with $\overline{D(0,r)}\subset G$, and $M$ with $\abs{w}\le M$ for all $w\in G$, which exists because $G$ is bounded. Each iterate maps $G$ into $G$, so $\abs{f^{\circ n}(z)}\le M$ for $\abs{z}\le r$. Cauchy's estimate for the coefficient of $z^{m}$ in a function bounded by $M$ on $D(0,r)$ gives $\abs{n a_{m}}\le M/r^{m}$ for every $n$, independently of $n$.
:::

:::

::: {.pf-step #contradiction}
This is impossible for $a_{m}\ne0$.

::: pf-proof
$\abs{a_{m}}\le M/(n r^{m})$ for every $n\ge1$, so letting $n\to\infty$ gives $a_{m}=0$, contradicting step [](#expansion){.pf-ref}. Hence $f=\mathrm{id}$.
:::

:::

:::

:::

::: {.pf-step}
Parts (a) and (b) hold.

::: pf-proof
Steps [](#parta){.pf-ref} and [](#partb){#partb} give:
$$
\boxed{G\ne\CC\text{ simply connected}\implies f=\mathrm{id};\qquad G\text{ bounded}\implies f=\mathrm{id};\qquad G=\CC:\text{ false}.}
$$
Boundedness replaces simple connectivity in (b); neither hypothesis implies the other, and $\CC$ itself is the case where both the conclusion and boundedness fail.
:::

:::

:::
:::
