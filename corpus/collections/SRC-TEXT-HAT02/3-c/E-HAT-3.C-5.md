---
schema: qual/card@1
id: E-HAT-3.C-5
kind: problem
title: "Fundamental group of an H-space is abelian"
classification:
  areas:
  - topology
  topics:
  - Cohomology
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

Show that if $(X, e)$ is an H-space then $\pi_1(X, e)$ is abelian.
[Compare the usual composition $f \cdot g$ of loops with the product $\mu(f(t), g(t))$ coming from the H-space multiplication $\mu$.]

::: {.solution}
<1>1. Setup the two binary operations on the space of based loops $\Omega(X, e)$: <2>1. Let $(X, e, \mu)$ be an H-space with multiplication $\mu: X \times X \to X$, so $\mu(x, e) \simeq x$ and $\mu(e, x) \simeq x$ via homotopies fixing the basepoint $e$.
::: {.proof}
definition of an H-space.
:::
<2>2. Let $f, g: [0, 1] \to X$ be based loops ($f(0) = f(1) = g(0) = g(1) = e$).
::: {.proof}
setup.
:::
<2>3. Define standard loop concatenation $*$ and pointwise H-space product $\odot$:
\[
(f * g)(t) = \begin{cases} f(2t) & 0 \le t \le 1/2 \\ g(2t - 1) & 1/2 \le t \le 1, \end{cases} \qquad (f \odot g)(t) = \mu(f(t), g(t)).
\]
::: {.proof}
definitions of concatenation and induced pointwise multiplication.
:::
<2>4. Let $c_e$ denote the constant loop at $e$.
Then $f \simeq f * c_e \simeq c_e * f$ and $g \simeq c_e * g \simeq g * c_e$ relative to endpoints.
::: {.proof}
identity element properties in the fundamental group.
:::

<1>2. Show that $[f * g] = [f \odot g]$ in $\pi_1(X, e)$: <2>1. Using the homotopies $f \simeq f * c_e$ and $g \simeq c_e * g$, we have $f \odot g \simeq (f * c_e) \odot (c_e * g)$.
::: {.proof}
homotopy invariance of the induced map $\mu_*$.
:::
<2>2. For $t \in [0, 1/2]$:
\[
((f * c_e) \odot (c_e * g))(t) = \mu((f * c_e)(t), (c_e * g)(t)) = \mu(f(2t), e) \simeq f(2t) = (f * g)(t).
\]
::: {.proof}
definition of $*$ and unit axiom $\mu(x, e) \simeq x$.
:::
<2>3. For $t \in [1/2, 1]$:
\[
((f * c_e) \odot (c_e * g))(t) = \mu((f * c_e)(t), (c_e * g)(t)) = \mu(e, g(2t - 1)) \simeq g(2t - 1) = (f * g)(t).
\]
::: {.proof}
definition of $*$ and unit axiom $\mu(e, y) \simeq y$.
:::
<2>4. Gluing the two halves gives $[f \odot g] = [f * g]$.
::: {.proof}
<2>2 and <2>3.
:::

<1>3. Show that $[g * f] = [f \odot g]$ in $\pi_1(X, e)$: <2>1. Using the homotopies $f \simeq c_e * f$ and $g \simeq g * c_e$, we have $f \odot g \simeq (c_e * f) \odot (g * c_e)$.
::: {.proof}
homotopy invariance.
:::
<2>2. For $t \in [0, 1/2]$:
\[
((c_e * f) \odot (g * c_e))(t) = \mu(e, g(2t)) \simeq g(2t) = (g * f)(t).
\]
::: {.proof}
unit axiom $\mu(e, y) \simeq y$.
:::
<2>3. For $t \in [1/2, 1]$:
\[
((c_e * f) \odot (g * c_e))(t) = \mu(f(2t - 1), e) \simeq f(2t - 1) = (g * f)(t).
\]
::: {.proof}
unit axiom $\mu(x, e) \simeq x$.
:::
<2>4. Gluing the two halves gives $[f \odot g] = [g * f]$.
::: {.proof}
<2>2 and <2>3.
:::

<1>4. Conclusion: Combining <1>2 and <1>3 yields:
\[
[f][g] = [f * g] = [f \odot g] = [g * f] = [g][f].
\]
Thus $\pi_1(X, e)$ is an abelian group.
::: {.proof}
<1>2 and <1>3.
:::
Q.E.D.
:::
