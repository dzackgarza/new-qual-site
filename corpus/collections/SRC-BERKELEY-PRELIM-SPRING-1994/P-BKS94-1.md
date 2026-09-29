---
schema: qual/card@1
id: P-BKS94-1
kind: problem
title: Lebesgue number lemma for open covers of $[0,1]$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored UC Berkeley Spring 1994 preliminary examination.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-25
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-25
  note: >-
    Chose local radii whose doubled intervals remain inside cover members,
    extracted a finite subcover by compactness, and took the minimum radius.
---

::: {.problem}
Let the collection U of open subsets of R cover the interval [0, 1]. Prove that there is a positive number δ such that any two points x and y of [0, 1] satisfying $| x - y | < \delta$ belong together to some member of the cover U.
:::

::: {.solution}
Write the open cover as $\mathcal U$.

::: pf

::: {.pf-step #s1}

For every $t\in[0,1]$, there are
$U_t\in\mathcal U$ and $r_t>0$ such that
$$
(t-2r_t,t+2r_t)\subseteq U_t.
$$

::: pf-proof

Since $\mathcal U$ covers $[0,1]$, choose $U_t\in\mathcal U$ with
$t\in U_t$. Because $U_t$ is open in $\RR$, there is $\rho_t>0$ such that
$$
(t-\rho_t,t+\rho_t)\subseteq U_t.
$$
Take $r_t=\rho_t/2$.

:::

:::

::: {.pf-step #s2}

There are points $t_1,\ldots,t_m\in[0,1]$ such that
$$
[0,1]
\subseteq
\bigcup_{j=1}^m(t_j-r_{t_j},t_j+r_{t_j}).
$$

::: pf-proof

The intervals
$$
(t-r_t,t+r_t),
\qquad
t\in[0,1],
$$
form an open cover of the compact interval $[0,1]$. Compactness supplies a
finite subcover.

:::

:::

::: {.pf-step #s3}

Define
$$
\delta\coloneqq
\min_{1\leq j\leq m}r_{t_j}.
$$
Then $\delta>0$.

::: pf-proof

Every $r_{t_j}$ is positive, and the minimum is taken over finitely many
numbers.

:::

:::

::: {.pf-step #s4}

If $x,y\in[0,1]$ and
$$
\abs{x-y}<\delta,
$$
then $x$ and $y$ belong to a common member of $\mathcal U$.

::: pf-proof

By step [](#s2){.pf-ref}, choose $j$ such that
$$
\abs{x-t_j}<r_{t_j}.
$$
By step [](#s3){.pf-ref},
$$
\abs{x-y}<\delta\leq r_{t_j}.
$$
Therefore
$$
\abs{y-t_j}
\leq
\abs{y-x}+\abs{x-t_j}
<
2r_{t_j}.
$$
Thus both $x$ and $y$ lie in
$$
(t_j-2r_{t_j},t_j+2r_{t_j}),
$$
which is contained in $U_{t_j}$ by step [](#s1){.pf-ref}.

:::

:::

::: pf-qed

The positive number $\delta$ from step [](#s3){.pf-ref} has the required property by
step [](#s4){.pf-ref}.

:::

:::

:::
