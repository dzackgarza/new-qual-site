---
schema: qual/card@1
id: P-CASP12D
kind: problem
title: "Real-valued analytic functions on radii and conditions for existence"
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
    Structured into Lamport steps from the card's own prose. Checked: z -> conj(f(conj z)) is holomorphic with coefficients conj(a_n), it agrees with f on [0,1), and the identity theorem then gives a_n = conj(a_n). For (ii) the prose's 'so every a_n omega^n is real' is now its own step, applying part (i) to r -> f(r omega), which is holomorphic on the disc with coefficients a_n omega^n; the nonzero coefficient with n >= 1 gives omega^n = +-1 and hence omega^{2n} = 1; and the converse is f(z) = z^m with omega^m = 1. The statement, including the quantifier |omega| = 1, is unchanged.
---

::: {.problem}
(i) Prove that if $f(z) = \sum_{n=0}^{\infty} a_n z^n$ is analytic on $\DD$ and $f(z) \in \RR$ whenever $z \in [0, 1)$, then $a_n \in \RR$ for all $n$.

(ii) Find necessary and sufficient conditions on a constant $\omega$ with $\abs{\omega} = 1$ for there to exist a nonconstant analytic function $f$ on $\DD$ that is real valued on the radii $[0, 1)$ and $[0, \omega)$.
:::

::: {.solution}
Part (i) is the identity theorem applied to $f$ and to $z\mapsto\overline{f(\overline z)}$: they agree on a set with accumulation points, namely $[0,1)$, so all Taylor coefficients are real. Part (ii) then applies (i) twice, to $f$ and to $r\mapsto f(r\omega)$, so that each $a_n\omega^n$ is real; since some $a_n\ne0$ this forces $\omega$ to be a root of unity, and conversely a root of unity works with $f(z)=z^n$. The argument is this card's own: the checkout retains no solution set for this exam.

::: pf

::: {.pf-step #reflection}
(i) If $f(z)=\sum_{n\ge0}a_nz^n$ is holomorphic on $\DD$ and $f(x)\in\RR$ for $0\le x<1$, then $z\mapsto\overline{f(\overline z)}$ is holomorphic on $\DD$ and equals $f$ there.

::: pf-proof
Since $\overline{z}$ is not holomorphic, define $g(z)=\overline{f(\overline z)}$: the partial sums of $f$ at $\overline z$ give $g(z)=\sum_n\overline{a_n}z^n$, a power series with the same radius of convergence $1$, so $g$ is holomorphic on $\DD$. For real $x\in[0,1)$ one has $g(x)=\overline{f(x)}=f(x)$, because $f(x)$ is real by hypothesis.
:::

:::


::: {.pf-step #parti}
(i) All the coefficients $a_n$ are real.

::: pf-proof
By step [](#reflection){.pf-ref}, the two holomorphic functions $f$ and $g$ agree on $[0,1)$, a subset of the disc with accumulation points in the disc (every point of $[0,1)$ is such a point). The identity theorem then gives $f=g$ on all of $\DD$. Comparing coefficients of the power series $\sum a_nz^n$ and $\sum\overline{a_n}z^n$, which are unique, gives $a_n=\overline{a_n}$ for every $n$, so $a_n\in\RR$.
:::

:::


::: {.pf-step #secondradius}
(ii) If $f$ is nonconstant, holomorphic on $\DD$, real on $[0,1)$ and real on $[0,\omega)$ with $\abs\omega=1$, then $a_n\omega^n\in\RR$ for every $n$.

::: pf-proof
Fix $\omega$ with $\abs\omega=1$ and consider $h(r)=f(r\omega)$ for $\abs r<1$; this is holomorphic in $r$ on the disc, since $r\mapsto r\omega$ maps $\DD$ into $\DD$. Its power series is $h(r)=\sum_n(a_n\omega^n)r^n$. By hypothesis $h(r)=f(r\omega)\in\RR$ for real $r\in[0,1)$, so part (i) applied to $h$ gives that every coefficient $a_n\omega^n$ is real.
:::

:::


::: {.pf-step #necessary}
(ii) Necessarily $\omega$ is a root of unity.

::: pf-proof
By part (i) the coefficients $a_n$ are real. Since $f$ is nonconstant, some $a_n$ with $n\ge1$ is nonzero. By step [](#secondradius){.pf-ref} the product $a_n\omega^n$ is real and nonzero, so $\omega^n$ is real; and $\abs{\omega^n}=1$, so $\omega^n=\pm1$ and hence $\omega^{2n}=1$. Thus $\omega$ is a root of unity, and a primitive such root has order dividing $2n$.
:::

:::


::: {.pf-step #sufficient}
(ii) If $\omega$ is a root of unity then such an $f$ exists.

::: pf-proof
Let $\omega^m=1$ with $m\ge1$ and take $f(z)=z^m$, which is nonconstant and holomorphic on $\DD$. For real $x\in[0,1)$ one has $f(x)=x^m\in\RR$, and for real $r\in[0,1)$ one has $f(r\omega)=r^m\omega^m=r^m\in\RR$. So $f$ is real valued on both radii.
:::

:::


::: {.pf-step #conclusion}
The necessary and sufficient condition is that $\omega$ be a root of unity.

::: pf-proof
Step [](#necessary){.pf-ref} shows the condition is necessary and step [](#sufficient){.pf-ref} that it is sufficient, for $\omega$ with $\abs\omega=1$ as the problem requires.
:::

:::

:::
:::
