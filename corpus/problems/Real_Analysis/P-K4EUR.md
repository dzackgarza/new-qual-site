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
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: 'Source printed Lambda(f) = int_X g conj(f), which is conjugate-linear in f and fails for linear Lambda != 0 over C, and wrote M\perp; the statement now reads Lambda(f) = int_X f conj(g) and M^perp.'
- event: source-corrected
  by: claude-opus-5.5
  date: 2026-10-29
  note: "The source opens the statement with the line '> Note: (a) is a repeat.'; the line is removed, the two bullet items are labelled (a) and (b), and the statement declares X a measure space."
---

::: {.problem}
Let $X$ be a measure space and let $\Lambda\in \dualof{L^2(X)}$.

(a) Show that $M\coloneqq \theset{f\in L^2(X) \suchthat \Lambda(f) = 0} \subseteq L^2(X)$ is a closed subspace, and $L^2(X) = M \oplus M^\perp$.

(b) Prove that there exists a unique $g\in L^2(X)$ such that $\Lambda(f) = \int_X f \bar g$ for all $f \in L^2(X)$.
:::

::: {.solution}
Write $\langle f, h\rangle = \int_X f\bar h$, linear in $f$.
The required formula is $\Lambda(f) = \langle f, g\rangle$.

::: pf

::: {.pf-step #s1}

$M = \ker \Lambda$ is a closed subspace, and $L^2(X) = M \oplus M^\perp$.

::: pf-proof

$M$ is the kernel of the bounded linear functional $\Lambda$, so it is a subspace, and it is closed because $\Lambda$ is continuous.
In a Hilbert space every closed subspace $M$ satisfies $H = M \oplus M^\perp$ by the projection theorem.

:::

:::

::: {.pf-step #s2}

If $\Lambda \neq 0$, then $M^\perp = \operatorname{span}\theset{g_0}$ for some $g_0$ with $\norm{g_0} = 1$.

::: pf-proof

$M \neq L^2(X)$, so $M^\perp \neq \theset0$ by step [](#s1){.pf-ref}; choose $g_0 \in M^\perp$ with $\norm{g_0} = 1$, so $\Lambda(g_0) \neq 0$.
For $h \in M^\perp$, the vector $\Lambda(h)g_0 - \Lambda(g_0)h$ lies in $M^\perp$ and in $M$, hence is $0$, so $h$ is a multiple of $g_0$.

:::

:::

::: pf-step

There is $g \in L^2(X)$ with $\Lambda(f) = \langle f, g\rangle$ for all $f$.

::: pf-proof

If $\Lambda = 0$ take $g = 0$.
Otherwise, by steps [](#s1){.pf-ref} and [](#s2){.pf-ref}, $f = m + \langle f, g_0\rangle g_0$ with $m \in M$, so $\Lambda(f) = \langle f, g_0\rangle\Lambda(g_0) = \langle f, \overline{\Lambda(g_0)}\,g_0\rangle$.
Take $g = \overline{\Lambda(g_0)}\,g_0$.

:::

:::

::: pf-step

$g$ is unique in $L^2(X)$.

::: pf-proof

If $\langle f, g\rangle = \langle f, g'\rangle$ for all $f$, take $f = g - g'$ to get $\norm{g - g'}^2 = 0$.

:::

:::

:::

:::
