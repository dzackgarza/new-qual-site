---
schema: qual/card@1
id: E-2BNJ6
kind: problem
title: Subnets of convergent nets converge
classification:
  areas:
  - topology
  topics:
  - Nets
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
    Transcribed from dbFin, "Supplementary Exercises*: Nets: Problem 8 Solution",
    https://dbfin.com/topology/munkres/chapter-3/supplementary-exercises-nets/problem-8-solution/,
    read 2026-11-15, text at tmp/sources/dbfin/supplementary-exercises-nets/problem-8.md, which is
    the same four lines as YuiTo Cheng's accepted answer to Math StackExchange 3198468
    (2019-04-23), https://math.stackexchange.com/questions/3198468, text at
    tmp/sources/mse-3198468-munkres-29-net-8.md: the index beta from convergence of the net, the
    index gamma of K with beta below g(gamma) from cofinality, and monotonicity of g beyond gamma.
    Nothing is corrected. This supersedes the 2026-11-10 note above.
---

::: {.exercise}

Let $f: J \to X$ be a net in $X$; let $f(\alpha) = x_\alpha$.
If $K$ is a directed set and $g: K \to J$ is a function such that

(i) $i \preceq j \implies g(i) \preceq g(j)$,

(ii) $g(K)$ is cofinal in $J$,

then the composite function $f \circ g: K \to X$ is called a subnet of $(x_\alpha)$.
Show that if the net $(x_\alpha)$ converges to $x$, so does any subnet.
:::

::: {.solution}

::: pf

::: pf-step
Let $g : K \to J$ be order preserving with $g(K)$ cofinal in $J$, and let the net $(x_\alpha)_{\alpha \in J}$ converge to $x$. Then the subnet $(x_{g(\kappa)})_{\kappa \in K}$ converges to $x$.

::: pf-proof
Let $U$ be a neighborhood of $x$. Convergence of $(x_\alpha)$ gives $\beta \in J$ with $x_\alpha \in U$ whenever $\beta \preceq \alpha$. Since $g(K)$ is cofinal in $J$, there is $\gamma \in K$ with $\beta \preceq g(\gamma)$. For $\kappa \in K$ with $\gamma \preceq \kappa$, order preservation gives $g(\gamma) \preceq g(\kappa)$, hence $\beta \preceq g(\kappa)$ and $x_{g(\kappa)} \in U$. So for each neighborhood $U$ of $x$ there is an index $\gamma$ of $K$ beyond which the subnet lies in $U$.
:::

:::

::: pf-step
If the net $(x_\alpha)$ converges to $x$, then every subnet of it converges to $x$. $\square$

::: pf-proof
A subnet of $(x_\alpha)$ is the composite $f \circ g$ for some directed set $K$ and some order preserving $g : K \to J$ whose image is cofinal, and step 1 shows that every such composite converges to $x$.
:::

:::

:::

:::
