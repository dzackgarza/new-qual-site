---
schema: qual/card@1
id: E-4S8XS
kind: problem
title: Nets in Hausdorff spaces have at most one limit
classification:
  areas:
  - topology
  topics:
  - Nets
  - Hausdorff Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    No published set for this exercise was located. The sources searched, the pages they
    cover and the conclusion are recorded in COMPLAINTS.md under the entry for the net
    exercises of §29; the card's own proof is kept. The statement was read against Munkres,
    Topology (2000), §29 supplementary exercises on nets, printed pp. 187-188.
- event: solution-written
  by: claude
  date: 2026-11-15
  note: >-
    Transcribed from the answer by Antonio Maria Di Mauro to Math StackExchange 3743525,
    "X is Hausdorff iff a net converges to at most one point" (2020-07-03, answer 3743595),
    https://math.stackexchange.com/questions/3743525, text at
    tmp/sources/mse-3743525-munkres-29-net-5c.md: disjoint neighborhoods of two supposed limits,
    the two indices given by convergence, a third dominating both, and a point of the empty
    intersection. The accepted answer 3743601 by Mittens on the same page makes the same argument
    in its second paragraph. dbFin's solution to this exercise makes the same argument; what is
    wrong with its writing is the separation, which reads "two non-intersecting neighborhoods x in X
    and y in Y", using the letter X, the space, for a neighborhood of x where U containing x and V
    containing y are meant. Its index variables are j, k and gamma and are not confused with
    neighborhoods, so the slip is one of naming and not the one recorded here before. This
    supersedes the 2026-11-10 note above.
---

::: {.exercise}

Show that if $X$ is Hausdorff, a net in $X$ converges to at most one point.
:::

::: {.solution}

::: pf

::: pf-step
Suppose the net $(x_\alpha)_{\alpha \in J}$ converges to both $x$ and $y$ in the Hausdorff space $X$. Then $x = y$.

::: pf-proof
Assume $x \ne y$. By the Hausdorff condition there are disjoint neighborhoods $U$ of $x$ and $V$ of $y$. Since $x_\alpha \to x$ there is $\alpha_0 \in J$ with $x_\alpha \in U$ whenever $\alpha_0 \preceq \alpha$, and since $x_\alpha \to y$ there is $\beta_0 \in J$ with $x_\alpha \in V$ whenever $\beta_0 \preceq \alpha$. As $J$ is directed, choose $\gamma \in J$ with $\alpha_0 \preceq \gamma$ and $\beta_0 \preceq \gamma$. Then $x_\gamma \in U$ and $x_\gamma \in V$, so $x_\gamma \in U \cap V$, which is empty. This contradiction shows $x = y$.
:::

:::

::: pf-step
A net in a Hausdorff space converges to at most one point. $\square$

::: pf-proof
Two limits of one net are equal by step 1, so the set of limits of the net is a single point, possibly absent.
:::

:::

:::

:::
