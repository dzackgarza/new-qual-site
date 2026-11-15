---
schema: qual/card@1
id: E-TAVBI
kind: problem
title: Continuity characterized by nets
classification:
  areas:
  - topology
  topics:
  - Nets
  - Continuous Functions
relations: []
review: draft
audit:
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
    Transcribed from dbFin, "Supplementary Exercises*: Nets: Problem 7 Solution",
    https://dbfin.com/topology/munkres/chapter-3/supplementary-exercises-nets/problem-7-solution/,
    read 2026-11-15, text at tmp/sources/dbfin/supplementary-exercises-nets/problem-7.md: the
    continuous direction through f^{-1}(V) for V a neighborhood of f(x), and the converse by
    supposing that f^{-1}(V) is not a neighborhood of x, producing a net in X - f^{-1}(V)
    converging to x. The same two directions are proved by Ruy in answer 3958661 to Math
    StackExchange 3958660 (2020-12-22), text at tmp/sources/mse-3958660-munkres-29-net-7.md,
    which calls the continuous direction well known and proves only the converse; the card takes
    the continuous direction from dbFin, whose f^{-1}(V) is checked to be a neighborhood of x
    through its interior. This supersedes the 2026-11-10 note above.
---

::: {.exercise}

Theorem.
Let $f: X \to Y$.
Then $f$ is continuous if and only if for every convergent net $(x_\alpha)$ in $X$, converging to $x$, say, the net $(f(x_\alpha))$ converges to $f(x)$.
:::

::: {.solution}

::: pf

::: pf-step
If $f$ is continuous, then $x_\alpha \to x$ implies $f(x_\alpha) \to f(x)$.

::: pf-proof
Let $V$ be a neighborhood of $f(x)$, and let $V^\circ$ be its interior, an open set containing $f(x)$. By continuity $f^{-1}(V^\circ)$ is open and contains $x$, so it is a neighborhood of $x$ contained in $f^{-1}(V)$. Convergence of $(x_\alpha)$ gives $\beta \in J$ with $x_\alpha \in f^{-1}(V)$ whenever $\beta \preceq \alpha$, and then $f(x_\alpha) \in V$ for those $\alpha$. As $V$ was an arbitrary neighborhood of $f(x)$, $f(x_\alpha) \to f(x)$.
:::

:::

::: pf-step
If $f$ carries every convergent net to a convergent net with the corresponding limit, then $f$ is continuous.

::: pf-proof
Let $V \subset Y$ be open and put $U = f^{-1}(V)$. Let $x \in U$; it suffices to exhibit a neighborhood of $x$ contained in $U$. Suppose there is none. Then every neighborhood of $x$ meets $X - U$, so $x \in \overline{X - U}$, and by the closure theorem for nets there is a net $(x_\alpha)$ of points of $X - U$ converging to $x$. By hypothesis $f(x_\alpha) \to f(x)$. Each $f(x_\alpha)$ lies in $Y - V$, which is closed because $V$ is open, and a limit of a net of points of a closed set lies in that set; hence $f(x) \in Y - V$, contradicting $f(x) \in V$. So some neighborhood of $x$ lies in $U$, and $U$ is open.
:::

:::

::: pf-step
$f$ is continuous if and only if every convergent net $(x_\alpha)$ with $x_\alpha \to x$ has $f(x_\alpha) \to f(x)$. $\square$

::: pf-proof
The two implications are steps 1 and 2.
:::

:::

:::

:::
