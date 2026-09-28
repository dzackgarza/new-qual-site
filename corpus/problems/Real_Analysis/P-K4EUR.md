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
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: {.problem}
> Note: (a) is a repeat.

- Let $\Lambda\in L^2(X)\dual$.

  - Show that $M\definedas \theset{f\in L^2(X) \suchthat \Lambda(f) = 0} \subseteq L^2(X)$ is a closed subspace, and $L^2(X) = M \oplus M\perp$.

  - Prove that there exists a unique $g\in L^2(X)$ such that $\Lambda(f) = \int_X g \bar f$.
:::
::: {.solution}
Write $\langle f, h\rangle = \int_X f\bar h$, linear in $f$. For a linear $\Lambda$ the representing formula is $\Lambda(f) = \langle f, g\rangle = \int_X f\bar g$; see the remark below.

<1>1. $M = \ker \Lambda$ is a closed subspace, and $L^2(X) = M \oplus M^\perp$.

::: {.proof}
$M$ is the kernel of the bounded linear functional $\Lambda$, so it is a subspace, and it is closed because $\Lambda$ is continuous. In a Hilbert space every closed subspace $M$ satisfies $H = M \oplus M^\perp$ by the projection theorem.
:::

<1>2. If $\Lambda \neq 0$, then $M^\perp = \operatorname{span}\theset{g_0}$ for some $g_0$ with $\|g_0\| = 1$.

::: {.proof}
$M \neq L^2(X)$, so $M^\perp \neq \theset0$ by step <1>1; choose $g_0 \in M^\perp$ with $\|g_0\| = 1$, so $\Lambda(g_0) \neq 0$. For $h \in M^\perp$, the vector $\Lambda(h)g_0 - \Lambda(g_0)h$ lies in $M^\perp$ and in $M$, hence is $0$, so $h$ is a multiple of $g_0$.
:::

<1>3. There is $g \in L^2(X)$ with $\Lambda(f) = \langle f, g\rangle$ for all $f$.

::: {.proof}
If $\Lambda = 0$ take $g = 0$. Otherwise, by steps <1>1 and <1>2, $f = m + \langle f, g_0\rangle g_0$ with $m \in M$, so $\Lambda(f) = \langle f, g_0\rangle\Lambda(g_0) = \langle f, \overline{\Lambda(g_0)}\,g_0\rangle$. Take $g = \overline{\Lambda(g_0)}\,g_0$.
:::

<1>4. $g$ is unique in $L^2(X)$.

::: {.proof}
If $\langle f, g\rangle = \langle f, g'\rangle$ for all $f$, take $f = g - g'$ to get $\|g - g'\|^2 = 0$.
:::
:::

::: {.remark}
Erratum: since $\Lambda$ is linear and $f \mapsto \int_X g\bar f$ is conjugate-linear, the formula in the statement holds only for $\Lambda = 0$ over $\CC$. The representation is $\Lambda(f) = \int_X f\bar g$; equivalently, $\int_X g\bar f$ represents the conjugate-linear functional $\overline{\Lambda}$. Over $\RR$ the two formulas agree.
:::
