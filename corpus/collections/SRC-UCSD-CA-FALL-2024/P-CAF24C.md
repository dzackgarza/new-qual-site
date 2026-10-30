---
schema: qual/card@1
id: P-CAF24C
kind: problem
title: Bound and value at $1/3$ imply no zeros in $\abs{z}<1/7$
classification:
  areas:
  - complex-analysis
  topics:
  - Holomorphic Functions
  - Zeros
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
Let $f : \DD \to \CC$ be holomorphic.
Assume that

(i) $\abs{f(z)} < 2$ for all $z \in \DD$,

(ii) $f\!\left(\dfrac{1}{3}\right) = 1$.

Show that $f$ has no zeros in the disc $\abs{z} < \dfrac{1}{7}$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Suppose for contradiction that $f(a) = 0$ for some $a$ with $\abs{a} < 1/7$.

::: pf-proof

assume a zero exists in the given disc.

:::

:::

::: {.pf-step #s2}

Define the automorphism $\phi_a(z) = \frac{z - a}{1 - \bar a z}$ of $\DD$, and set $g = f \circ \phi_a^{-1}$.

::: pf-proof

$\phi_a$ is a disk automorphism sending $a$ to $0$.

:::

:::

::: {.pf-step #s3}

$g$ is holomorphic on $\DD$ with $\abs{g} < 2$ and $g(0) = 0$.

::: pf-proof

$g(0) = f(\phi_a^{-1}(0)) = f(a) = 0$, and $\abs{g} < 2$ since $\abs{f} < 2$.

:::

:::

::: {.pf-step #s4}

By the Schwarz lemma, $\abs{g(w)} \le 2\abs{w}$ for all $w \in \DD$.

::: pf-proof

apply the Schwarz lemma to $g/2$ (a holomorphic self-map of $\DD$ with $g(0)/2 = 0$).

:::

:::

::: {.pf-step #s5}

Let $w_0 = \phi_a(1/3) = \frac{1/3 - a}{1 - a/3}$.

::: pf-proof

definition.

:::

:::

::: {.pf-step #s6}

Then $1 = f(1/3) = g(w_0)$, so $\abs{g(w_0)} = 1 \le 2\abs{w_0}$, giving $\abs{w_0} \ge 1/2$.

::: pf-proof

Step [](#s4){.pf-ref} and the hypothesis $f(1/3) = 1$.

:::

:::

::: {.pf-step #s7}

But $\abs{w_0} = \abs{\frac{1/3 - a}{1 - a/3}} < \frac{1/3 + 1/7}{1 - 1/21} = \frac{10/21}{20/21} = \frac{1}{2}$.

::: pf-proof

$\abs{a} < 1/7$, so $\abs{1/3 - a} < 1/3 + 1/7 = 10/21$ and $\abs{1 - a/3} > 1 - 1/21 = 20/21$.

:::

:::

::: {.pf-step #s8}

Contradiction.

::: pf-proof

Step [](#s6){.pf-ref} says $\abs{w_0} \ge 1/2$ but step [](#s7){.pf-ref} says $\abs{w_0} < 1/2$.

:::

:::

::: {.pf-step #s9}

Hence $f$ has no zeros in $\abs{z} < 1/7$.

::: pf-proof

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref}, [](#s3){.pf-ref}, [](#s4){.pf-ref}, [](#s5){.pf-ref}, [](#s6){.pf-ref}, [](#s7){.pf-ref} and [](#s8){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s9){.pf-ref}.

:::

:::

:::
