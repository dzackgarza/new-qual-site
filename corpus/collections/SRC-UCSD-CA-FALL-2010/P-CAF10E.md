---
schema: qual/card@1
id: P-CAF10E
kind: problem
title: "Zeros of a polynomial in a sublevel set and Schwarz lemma-type inequality"
classification:
  areas:
  - complex-analysis
  topics:
  - Maximum Modulus Principle
  - Zeros of Polynomials
  - Schwarz Lemma
relations: []
review: draft
---

::: {.problem}
Let $p(z)$ be a nonconstant polynomial and let $G$ be a connected component of the open set $\{z : \abs{p(z)} < 1\}$.

(a) Show that $p(z)$ must have at least one zero in $G$.

(b) Let $f(z)$ be analytic in $G$, satisfying $\abs{f(z)} \leq 1$ there.
Assume that $f(z)$ vanishes at every zero of $p(z)$ in $G$ and that the vanishing order of $f(z)$ at each such zero is at least that of $p(z)$.
Show that:

(i) $\abs{f(z)} \leq \abs{p(z)}$ in $G$.

(ii) If $a \in G$ is a zero of $p(z)$ of order $k$, then $\abs{f^{(k)}(a)} \leq \abs{p^{(k)}(a)}$.

Moreover, if for some such $a$ we have equality in (ii), then $f(z) = cp(z)$ for some unimodular constant $c$.
:::

::: {.solution}

The argument is the card's own: the maximum modulus principle on the component and on its sublevel pieces, and the comparison of the two Taylor coefficients at a zero. No retained set solves this exercise, and the sets searched are recorded in the audit trail.

Let $p$ be a nonconstant polynomial and $G$ a connected component of $\Omega=\{z:\abs{p(z)}<1\}$.

::: pf

::: {.pf-step #boundary}
$G$ is bounded and $\partial G\subseteq\{\abs{p}=1\}$.

::: pf-proof
$\abs{p(z)}\to\infty$ as $\abs{z}\to\infty$, so $\Omega\subseteq\{\abs{p}\le1\}$ is bounded and $G$ is bounded; its closure is then closed and bounded, hence compact, and the maximum modulus principle applies on it. For $z\in\partial G$: if $\abs{p(z)}<1$ then $z\in\Omega$, and $\Omega$ is open, so a neighbourhood of $z$ lies in $\Omega$ and meets $G$, putting $z$ in the open set $G$ and contradicting $z\in\partial G$; if $\abs{p(z)}>1$ then by continuity a neighbourhood of $z$ satisfies $\abs p>1$, so $z$ is not in the closure of $G$ (whose points have $\abs{p}\le1$) and again $z\notin\partial G$. Hence $\abs{p(z)}=1$.
:::

:::

::: {.pf-step #a}
(a) $p$ has at least one zero in $G$.

::: pf-proof
Suppose $p$ has no zero in $G$. Then $1/p$ is holomorphic on $G$ and continuous on $\overline G$, because $\abs p=1$ on $\partial G$ by step [](#boundary){.pf-ref}, so $p$ does not vanish there either. On $\partial G$ we have $\abs{1/p}=1$, while on $G$ we have $\abs p<1$, that is $\abs{1/p}>1$. But for a holomorphic function on a bounded domain continuous on the closure, the maximum modulus principle gives $\sup_{G}\abs{1/p}\le\sup_{\partial G}\abs{1/p}=1$. That contradicts $\abs{1/p}>1$ on the nonempty set $G$.
:::

:::

::: {.pf-step #h-extends}
(b) $h=f/p$, defined off the zeros of $p$ in $G$, extends holomorphically to $G$.

::: pf-proof
The zeros of $p$ in $G$ are isolated, so $h$ is holomorphic off them. At a zero $a$ of $p$ of order $k$ the hypothesis gives $f=(z-a)^{k}s$ with $s$ holomorphic near $a$, and $p=(z-a)^{k}q$ with $q(a)\ne0$; hence $h=s/q$ near $a$, a quotient of holomorphic functions with nonvanishing denominator, so $h$ has a removable singularity at $a$. So $h$ extends holomorphically to all of $G$.
:::

:::

::: {.pf-step #sublevel}
(b) For $0<r<1$, every component $G_{r}$ of $G\cap\{\abs p<r\}$ is relatively compact in $G$ and satisfies $\abs{h}\le1/r$ on $G_{r}$.

::: pf-proof
$\overline{G_{r}}$ is contained in $\{\abs p\le r\}$, which is compact. A point of $\overline{G_{r}}$ lies in $\partial G$ only if $\abs p=1$ by step [](#boundary){.pf-ref}, which is impossible since $\abs p\le r<1$ there; so $\overline{G_{r}}\subseteq G$, and $G_{r}$ is relatively compact in $G$. On $\partial G_{r}$ we have either $\abs p=r$, when $\abs h=\abs f/\abs p\le1/r$ because $\abs f\le1$, or $z\in\partial G$, when $\abs p=1$ and $\abs h\le1\le1/r$ because $r<1$. So $\abs h\le1/r$ on $\partial G_{r}$, and the maximum modulus principle on the relatively compact domain $G_{r}$ gives $\abs h\le1/r$ throughout $G_{r}$.
:::

:::

::: {.pf-step #i}
(b)(i) $\abs{f(z)}\le\abs{p(z)}$ for every $z\in G$.

::: pf-proof
Let $z\in G$ and choose $r$ with $\abs{p(z)}<r<1$. Then $z\in G\cap\{\abs p<r\}$, so $z$ lies in one of its components $G_{r}$, and step [](#sublevel){.pf-ref} gives $\abs{h(z)}\le1/r$, that is $\abs{f(z)}\le\abs{p(z)}/r$. Letting $r\uparrow1$ along such radii gives $\abs{f(z)}\le\abs{p(z)}$.
:::

:::

::: {.pf-step #ii}
(b)(ii) If $a\in G$ is a zero of $p$ of order $k$, then $\abs{f^{(k)}(a)}\le\abs{p^{(k)}(a)}$.

::: pf-proof
Write $p(z)=(z-a)^{k}q(z)$ with $q(a)\ne0$ and $f(z)=(z-a)^{k}s(z)$, which is possible because the vanishing order of $f$ at $a$ is at least $k$; then $p^{(k)}(a)=k!\,q(a)$ and $f^{(k)}(a)=k!\,s(a)$, since all terms of the Taylor expansions of order below $k$ vanish at $a$. And $h=s/q$ near $a$ by step [](#h-extends){.pf-ref}, so $h(a)=s(a)/q(a)$ and
$$
\abs{\frac{f^{(k)}(a)}{p^{(k)}(a)}}=\abs{\frac{s(a)}{q(a)}}=\abs{h(a)}\le1
$$
by step [](#i){.pf-ref}.
:::

:::

::: {.pf-step #equality}
(b) If equality holds in (ii) for some such $a$, then $f=cp$ for a unimodular constant $c$.

::: pf-proof
Equality gives $\abs{h(a)}=1$. Now $h$ is holomorphic on the connected domain $G$ and satisfies $\abs h\le1$ there by step [](#i){.pf-ref}, so $\abs h$ attains its maximum at the interior point $a$; by the maximum modulus principle $h$ is constant, $h\equiv c$, and $\abs c=\abs{h(a)}=1$. Then $f=hp=cp$ on $G$, which is the assertion.
:::

:::

:::
:::
