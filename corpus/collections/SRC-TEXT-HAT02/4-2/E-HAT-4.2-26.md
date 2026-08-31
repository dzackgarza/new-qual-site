---
schema: qual/card@1
id: E-HAT-4.2-26
kind: exercise
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

Generalizing the example of $\mathbb{RP}^2$ and $S^2 \times \mathbb{RP}^\infty$, show that if $X$ is a connected finite-dimensional CW complex with universal cover $\tilde{X}$, then $X$ and $\tilde{X} \times K(\pi_1(X), 1)$ have isomorphic homotopy groups but are not homotopy equivalent if $\pi_1(X)$ contains elements of finite order.

::: {.solution}
<1>1. $X$ and $\tilde X \times K(\pi_1(X), 1)$ have isomorphic homotopy groups.
<2>1. $\pi_1(\tilde X \times K(\pi_1(X),1)) = \pi_1(\tilde X) \times \pi_1(K(\pi_1(X),1)) = 1 \times \pi_1(X) = \pi_1(X)$.
::: {.proof}
$\tilde X$ is simply connected and $K(\pi_1(X),1)$ has fundamental group $\pi_1(X)$.
:::
<2>2. For $n \ge 2$, $\pi_n(\tilde X \times K(\pi_1(X),1)) = \pi_n(\tilde X) \times \pi_n(K(\pi_1(X),1)) = \pi_n(\tilde X) \times 0 = \pi_n(\tilde X)$.
::: {.proof}
$K(\pi_1(X),1)$ has vanishing higher homotopy groups.
:::
<2>3. $\pi_n(X) = \pi_n(\tilde X)$ for $n \ge 2$.
::: {.proof}
the universal cover $\tilde X \to X$ induces isomorphisms on $\pi_n$ for $n \ge 2$.
:::
<2>4. Hence $\pi_n(X) \cong \pi_n(\tilde X \times K(\pi_1(X),1))$ for all $n$.
::: {.proof}
<2>1–<2>3.
:::

<1>2. $X$ and $\tilde X \times K(\pi_1(X),1)$ are not homotopy equivalent if $\pi_1(X)$ has an element of finite order.
<2>1. $X$ is finite-dimensional, so $\pi_n(X) = 0$ for all sufficiently large $n$.
::: {.proof}
a finite-dimensional CW complex has finitely many nonzero homotopy groups in the sense that $\pi_n(X) = 0$ for $n > \dim X$ (by cellular approximation, since $S^n$ has no cells below dimension $n$... more precisely, $\pi_n(X) = 0$ for $n > \dim X$).
:::
<2>2. But $K(\pi_1(X),1)$ has infinitely many nonzero homotopy groups when $\pi_1(X)$ has an element of finite order.
::: {.proof}
if $\pi_1(X)$ has an element of finite order, then $K(\pi_1(X),1)$ has nonzero homology (hence nonzero homotopy) in infinitely many dimensions (e.g. $\ZZ/m$ has $H_{2k+1}(K(\ZZ/m,1)) = \ZZ/m$ for all $k$).
:::
<2>3. Hence $\tilde X \times K(\pi_1(X),1)$ has nonzero homotopy groups in infinitely many dimensions.
::: {.proof}
<2>2 and the product structure.
:::
<2>4. Therefore $X$ and $\tilde X \times K(\pi_1(X),1)$ are not homotopy equivalent.
::: {.proof}
homotopy equivalence preserves homotopy groups, but <2>1 and <2>3 contradict.
:::

<1>3. Q.E.D.
::: {.proof}
<1>1 and <1>2.
:::
:::
