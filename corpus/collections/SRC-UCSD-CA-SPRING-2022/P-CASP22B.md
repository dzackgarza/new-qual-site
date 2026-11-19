---
schema: qual/card@1
id: P-CASP22B
kind: problem
title: "Schwarz lemma for polynomial preimages: zeros, bounds, and equality cases"
classification:
  areas:
  - complex-analysis
  topics:
  - Schwarz Lemma
  - Polynomials
  - Holomorphic Functions
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Read against the exam paper retained at assets/attachments/SP22-220ABC-Complex.pdf, Problem 2
    (10 points; 4, 4, 2), parts (a), (b) and (c), including the hypothesis that f vanishes at every
    zero of p to at least the order of p. The card's three parts are the printed three.
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Structured into Lamport steps, and the boundary step repaired. The card had written that 1/p
    equals 1 on the boundary of G and that q = f/p is bounded by 1 there, then applied the maximum
    modulus principle; but G is only a component of {|p| < 1}, and neither function is known to
    extend continuously to the whole of the boundary, so the boundary values quoted were not
    available. Both arguments now use G_delta = {z in G : |p| < 1 - delta}, whose boundary satisfies
    |p| = 1 - delta, and which is relatively compact in G -- that last point proved, since it is what
    makes the maximum modulus principle applicable. Checked also that the quotient q = f/p extends
    across the zeros, with q(a) = f^(k)(a)/p^(k)(a) at a zero of order k, and that both equality
    cases of (c) put |q(a)| = 1 at an interior point. No retained published solution covers this
    problem.
---

::: {.problem}
Let $p(z)$ be a nonconstant polynomial.
Let $G \subset \CC$ be a component of the set $\{z : \abs{p(z)} < 1\}$.

(a) Show that $p$ has at least one zero in $G$.

(b) Let $f$ be analytic in $G$ with $\abs{f} \leq 1$.
Assume that $f$ has a zero at every zero of $p$ such that the order of vanishing of $f$ is at least that of $p$.
Show that $\abs{f(z)} \leq \abs{p(z)}$ and if $z = a$ is a zero of $p$ of order $k$, then $\abs{f^{(k)}(a)} \leq \abs{p^{(k)}(a)}$.

(c) If either $\abs{f(a)} = \abs{p(a)}$ for some $z = a$ that is not a zero of $p$ or if $\abs{f^{(k)}(a)} = \abs{p^{(k)}(a)}$ for some $z = a$ that is a zero of $p$ of order $k$, then $f(z) = cp(z)$ for some constant $c$.
:::

::: {.solution}
This is Problem 2 (10 points; 4, 4, 2) of the UCSD complex-analysis qualifying exam of Spring 2022 (`assets/attachments/SP22-220ABC-Complex.pdf`). No published solution set is transcribed: the argument is the card's own, and it is the maximum-modulus argument the problem is built around.

What was repaired: the card applied the maximum modulus principle to $1/p$ on $G$ and to $q=f/p$ on $G$ with the boundary values taken on $\partial G$, but $G$ is only a component of $\theset{\abs{p}<1}$ and neither $1/p$ nor $q$ need extend continuously to all of $\partial G$. Both uses now run on the relatively compact subdomains $G_{\delta}=\theset{z\in G\mid\abs{p(z)}<1-\delta}$, on whose boundaries $\abs{p}$ is the constant $1-\delta$, and pass to the limit $\delta\downarrow0$.

::: pf

::: {.pf-step #geometry}
$G$ is bounded, every boundary point of $G$ satisfies $\abs{p}=1$, and for $0<\delta<1$ the set $G_{\delta}=\theset{z\in G\mid\abs{p(z)}<1-\delta}$ is relatively compact in $G$, with $\bigcup_{0<\delta<1}G_{\delta}=G$.

::: pf-proof
$\abs{p(z)}\to\infty$ as $\abs{z}\to\infty$, so $\theset{\abs{p}<1}$ is bounded and so is its component $G$. A component $G$ of the open set $U=\theset{\abs{p}<1}$ has $\partial G\subset\partial U$: a point of $\partial G$ is not in $G$ and every neighbourhood of it meets $G\subset U$, so it is not in $U$ either, and it is a limit point of $U$; hence $\partial U=\theset{\abs{p}=1}$ contains $\partial G$. Now let $z$ lie in the closure of $G_{\delta}$. Then $\abs{p(z)}\leq1-\delta<1$, and $\abs{p}<1$ is open, so a neighbourhood of $z$ lies in $U$ and meets $G$; that neighbourhood is connected into the component of $z$ in $U$, which must then be $G$. So $z\in G$ and $\overline{G_{\delta}}\subset G$, which with boundedness gives relative compactness. Finally $G=\bigcup_{\delta}G_{\delta}$ because $\abs{p(z)}<1$ for $z\in G$.
:::
:::

::: {.pf-step #parta}
(a) $p$ has at least one zero in $G$.

::: pf-proof
Suppose $p$ has no zero in $G$; then $h=1/p$ is holomorphic on $G$, and on $\partial G_{\delta}$ one has $\abs{h}=1/\abs{p}=1/(1-\delta)$, while at every point of $G_{\delta}$ one has $\abs{h}>1/(1-\delta)$ because $\abs{p}<1-\delta$ there. For $G_{\delta}\neq\varnothing$ this contradicts the maximum modulus principle applied to $h$ on the relatively compact domain $G_{\delta}$, whose boundary is contained in $\theset{\abs{p}=1-\delta}$. Since some $G_{\delta}$ is nonempty, $p$ has a zero in $G$.
:::
:::

::: {.pf-step #quotient}
$q=f/p$ extends from $G\setminus Z$ to a holomorphic function on $G$, where $Z$ is the finite set of zeros of $p$ in $G$, and $\abs{q(a)}=\abs{f^{(k)}(a)}/\abs{p^{(k)}(a)}$ at a zero $a$ of order $k$.

::: pf-proof
At $a\in Z$ of order $k$ write $p(z)=(z-a)^{k}P(z)$ and $f(z)=(z-a)^{k}F(z)$ with $P,F$ holomorphic near $a$ and $P(a)\neq0$; this is possible because $f$ vanishes at $a$ to order at least $k$. Then $q=F/P$ near $a$ is holomorphic, so $q$ extends across $a$, and $q(a)=F(a)/P(a)=f^{(k)}(a)/p^{(k)}(a)$, since $f^{(k)}(a)=k!F(a)$ and $p^{(k)}(a)=k!P(a)$. Outside $Z$ the quotient of holomorphic functions with nonvanishing denominator is holomorphic.
:::
:::

::: {.pf-step #bound}
(b) $\abs{f(z)}\leq\abs{p(z)}$ on $G$, and $\abs{f^{(k)}(a)}\leq\abs{p^{(k)}(a)}$ at a zero $a$ of $p$ of order $k$.

::: pf-proof
On $\partial G_{\delta}$ one has $\abs{p}=1-\delta$ by step [](#geometry){.pf-ref}, so $\abs{q}=\abs{f}/\abs{p}\leq1/(1-\delta)$ there, using the hypothesis $\abs{f}\leq1$ on $G$. The maximum modulus principle on the relatively compact domain $G_{\delta}$ gives $\abs{q}\leq1/(1-\delta)$ on $G_{\delta}$, and letting $\delta\downarrow0$ gives $\abs{q}\leq1$ on $G$, which is $\abs{f}\leq\abs{p}$. At a zero $a$ of order $k$ step [](#quotient){.pf-ref} gives $\abs{q(a)}=\abs{f^{(k)}(a)}/\abs{p^{(k)}(a)}\leq1$.
:::
:::

::: {.pf-step #partc}
(c) If $\abs{f(a)}=\abs{p(a)}$ at some $a$ with $p(a)\neq0$, or $\abs{f^{(k)}(a)}=\abs{p^{(k)}(a)}$ at a zero $a$ of $p$ of order $k$, then $f=cp$ with $\abs{c}=1$.

::: pf-proof
Either hypothesis says $\abs{q(a)}=1$ at an interior point $a$ of $G$: in the first case because $q=f/p$ there, in the second by step [](#quotient){.pf-ref}. By step [](#bound){.pf-ref} the maximum of $\abs{q}$ on $G$ is $1$, so $\abs{q}$ attains its maximum at the interior point $a$, and the maximum modulus principle forces $q$ to be constant on the domain $G$, say $q\equiv c$ with $\abs{c}=1$. Then $f=cp$ on $G\setminus Z$ and, both sides being holomorphic on $G$, on all of $G$.
:::
:::
:::

:::
