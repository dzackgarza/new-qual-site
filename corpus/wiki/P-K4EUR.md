---
schema: qual/card@1
id: P-K4EUR
kind: problem
title: Riesz representation for $L^2$
classification:
  areas:
  - real-analysis
  topics:
  - Hilbert Spaces
  - Riesz Representation
  - L²
relations: []
review: draft
---

::: problem
> Note: (a) is a repeat.

- Let $\Lambda\in L^2(X)\dual$.

  - Show that $M\definedas \theset{f\in L^2(X) \suchthat \Lambda(f) = 0} \subseteq L^2(X)$ is a closed subspace, and $L^2(X) = M \oplus M\perp$.

  - Prove that there exists a unique $g\in L^2(X)$ such that $\Lambda(f) = \int_X g \bar f$.
:::
::: {.solution}
> **AI-Generated Solution**

<1>1. $M = \ker \Lambda = \{f \in L^2(X) : \Lambda(f) = 0\}$ is a closed subspace.
Proof: $\Lambda$ is a bounded linear functional, hence continuous, so its kernel is closed; it is a linear subspace as the kernel of a linear map.

<1>2. $L^2(X) = M \oplus M^\perp$.
Proof: $M$ is a closed subspace of the Hilbert space $L^2(X)$; the orthogonal decomposition theorem gives $L^2(X) = M \oplus M^\perp$ (every $f$ writes uniquely as $m + m^\perp$).

<1>3. Existence of $g$: there is $g \in L^2(X)$ with $\Lambda(f) = \int_X g\bar f$ for all $f \in L^2(X)$.
<2>1. If $\Lambda \equiv 0$, take $g = 0$.
Proof: trivial case.
<2>2. Otherwise $M^\perp \neq \{0\}$; pick $g_0 \in M^\perp$ with $\|g_0\| = 1$ (normalize a nonzero element).
Proof: $M^\perp \ne \{0\}$ since $L^2 = M \oplus M^\perp$ and $\Lambda \ne 0$ implies $M \ne L^2$.
<2>3. For $f \in L^2$, write $f = m + \langle f, g_0\rangle g_0$ (with $m \in M$): then $\Lambda(f) = \Lambda(\langle f, g_0\rangle g_0) = \langle f, g_0\rangle\Lambda(g_0)$.
Proof: $\Lambda(m) = 0$ by $m \in M$; decompose $f$'s component in $M^\perp = \span\{g_0\}$ as $\langle f, g_0\rangle g_0$ (the orthogonal projection onto a line).
<2>4. Set $g = \overline{\Lambda(g_0)}\,g_0$; then $\Lambda(f) = \langle f, g_0\rangle\Lambda(g_0) = \Lambda(g_0)\int_X f\overline{g_0} = \int_X f\,\overline{\overline{\Lambda(g_0)}g_0} = \int_X g\,\bar f$.
Proof: <2>3 and the computation $\overline{\overline{\Lambda(g_0)}g_0} = \Lambda(g_0)\bar g_0$-adjusted: $\int f\,\overline{g} = \int f\,\overline{\overline{\Lambda(g_0)}g_0} = \Lambda(g_0)\int f\bar g_0 = \langle f, g_0\rangle\Lambda(g_0)$.

<1>4. Uniqueness of $g$: if $\int_X (g - g')\bar f = 0$ for all $f \in L^2$, then $g = g'$ a.e. Proof: take $f = g - g'$: $\int |g - g'|^2 = 0$, so $g = g'$ a.e.

<1>5. Q.E.D. Proof: <1>1, <1>2, <1>3, <1>4 establish the claims.
(This is the Riesz representation theorem for $L^2$; the usual proof via $\bar g$ is equivalent.)
:::
