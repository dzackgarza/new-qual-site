---
schema: qual/card@1
id: E-HAT-4.2-26
kind: problem
title: "Isomorphic homotopy but different homotopy type"
classification:
  areas:
  - topology
  topics:
  - Higher Homotopy Groups
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: {.problem}
Generalizing the example of $\mathbb{RP}^2$ and $S^2 \times \mathbb{RP}^\infty$, show that if $X$ is a connected finite-dimensional CW complex with universal cover $\tilde{X}$, then $X$ and $\tilde{X} \times K(\pi_1(X), 1)$ have isomorphic homotopy groups but are not homotopy equivalent if $\pi_1(X)$ contains elements of finite order.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

$X$ and $\tilde X \times K(\pi_1(X), 1)$ have isomorphic homotopy groups.

::: pf-proof

::: {.pf-step #s1-1}

$\pi_1(\tilde X \times K(\pi_1(X),1)) = \pi_1(\tilde X) \times \pi_1(K(\pi_1(X),1)) = 1 \times \pi_1(X) = \pi_1(X)$.

::: pf-proof

$\tilde X$ is simply connected and $K(\pi_1(X),1)$ has fundamental group $\pi_1(X)$.

:::

:::

::: {.pf-step #s1-2}

For $n \ge 2$, $\pi_n(\tilde X \times K(\pi_1(X),1)) = \pi_n(\tilde X) \times \pi_n(K(\pi_1(X),1)) = \pi_n(\tilde X) \times 0 = \pi_n(\tilde X)$.

::: pf-proof

$K(\pi_1(X),1)$ has vanishing higher homotopy groups.

:::

:::

::: {.pf-step #s1-3}

$\pi_n(X) = \pi_n(\tilde X)$ for $n \ge 2$.

::: pf-proof

the universal cover $\tilde X \to X$ induces isomorphisms on $\pi_n$ for $n \ge 2$.

:::

:::

::: pf-step

Hence $\pi_n(X) \cong \pi_n(\tilde X \times K(\pi_1(X),1))$ for all $n$.

::: pf-proof

Steps [](#s1-1){.pf-ref}, [](#s1-2){.pf-ref} and [](#s1-3){.pf-ref}.

:::

:::

:::

:::

::: {.pf-step #s2}

$X$ and $\tilde X \times K(\pi_1(X),1)$ are not homotopy equivalent if $\pi_1(X)$ has an element of finite order.

::: pf-proof

::: {.pf-step #s2-1}

$X$ is finite-dimensional, so $\pi_n(X) = 0$ for all sufficiently large $n$.

::: pf-proof

a finite-dimensional CW complex has finitely many nonzero homotopy groups in the sense that $\pi_n(X) = 0$ for $n > \dim X$ (by cellular approximation, since $S^n$ has no cells below dimension $n$... more precisely, $\pi_n(X) = 0$ for $n > \dim X$).

:::

:::

::: {.pf-step #s2-2}

But $K(\pi_1(X),1)$ has infinitely many nonzero homotopy groups when $\pi_1(X)$ has an element of finite order.

::: pf-proof

if $\pi_1(X)$ has an element of finite order, then $K(\pi_1(X),1)$ has nonzero homology (hence nonzero homotopy) in infinitely many dimensions (e.g. $\ZZ/m$ has $H_{2k+1}(K(\ZZ/m,1)) = \ZZ/m$ for all $k$).

:::

:::

::: {.pf-step #s2-3}

Hence $\tilde X \times K(\pi_1(X),1)$ has nonzero homotopy groups in infinitely many dimensions.

::: pf-proof

Step [](#s2-2){.pf-ref} and the product structure.

:::

:::

::: pf-step

Therefore $X$ and $\tilde X \times K(\pi_1(X),1)$ are not homotopy equivalent.

::: pf-proof

homotopy equivalence preserves homotopy groups, but steps [](#s2-1){.pf-ref} and [](#s2-3){.pf-ref} contradict.

:::

:::

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref} and [](#s2){.pf-ref}.

:::

:::

:::
