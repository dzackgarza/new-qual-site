---
schema: qual/card@1
id: E-O0XAB
kind: problem
title: Completeness via nested closed sets of vanishing diameter
classification:
  areas:
  - topology
  topics:
  - Metric Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: claude
  date: 2026-11-11
  note: >-
    No located published solution covers Munkres §43 Exercise 4 (printed p. 270); this card is listed in
    COMPLAINTS.md with the sources searched. The printed statement is restored: the card had added "(and
    in fact consists of a unique point)" to the exercise, and now states the exercise as printed, the
    uniqueness being proved inside the solution (two points of the intersection lie in every A_n, so their
    distance is at most diam A_n -> 0). Checked line by line against the book: the forward direction
    chooses x_n in A_n, shows the sequence is Cauchy using nesting and diam A_n -> 0, uses completeness,
    and puts the limit in each closed A_k; the converse takes the closures of the tails of a Cauchy
    sequence, which are closed, nested, nonempty, of diameter tending to 0 because the tail diameters do,
    and a point of the intersection is the limit of the sequence. The diameter of a closure equals the
    diameter of the set, used in the converse, is the one fact not stated in the book's §43; it is proved
    from the definition of diameter and the continuity of the distance function. The card's closing
    references to two step labels that no step carried are replaced by the prose sentence that closes the
    solution.
- event: solution-written
  by: claude
  date: 2026-11-15
  note: >-
    Transcribed from the two answers to Math StackExchange 375685, "How do you prove the converse
    Cantor's intersection theorem?" (2013-04-28), https://math.stackexchange.com/questions/375685,
    text at tmp/sources/mse-375685-munkres-43-4.md. The converse, the property implying
    completeness, is answer 375696 by Asaf Karagila: the closed balls about a subsequence of a
    Cauchy sequence, decreasing, of diameters tending to zero. The other direction is answer 375690
    by Pedro, whose addition shows the tails of a Cauchy sequence are Cauchy-diameter zero before
    closure. Two corrections are made. Karagila's balls are \bar B(x_{i(n)}, 2/n) with thresholds
    1/n, and these are not nested: 2/(n+1) + 1/n <= 2/n fails for n >= 2, so the card uses radius
    2^{-n+1} about x_{i(n)} with threshold 2^{-n}, which nests because 2^{-n} + 2^{-n} = 2^{-n+1}.
    Pedro's note that diam A = diam \bar A is not needed on this route and is not used. Neither
    answer writes the direction "complete implies the intersection is nonempty" that the exercise
    states; the card supplies it, choosing x_n in A_n and using diam A_n -> 0 for the Cauchy
    condition.
---

::: {.exercise}

Show that the metric space $(X, d)$ is complete if and only if for every nested sequence $A_1 \supset A_2 \supset A_3 \supset \cdots$ of nonempty closed sets of $X$ such that $\operatorname{diam} A_n \to 0$, the intersection of the sets $A_n$ is nonempty.
:::

::: {.solution}

::: pf

::: pf-step
If $(X,d)$ is complete, then every nested sequence $A_1 \supset A_2 \supset \cdots$ of nonempty closed sets with $\operatorname{diam} A_n \to 0$ has nonempty intersection.

::: pf-proof
Choose $x_n \in A_n$ for each $n$. Given $\epsilon > 0$, take $N$ with $\operatorname{diam} A_N < \epsilon$; for $n, m \ge N$ both $x_n$ and $x_m$ lie in $A_N$, so $d(x_n, x_m) < \epsilon$. Thus $(x_n)$ is a Cauchy sequence, and by completeness it converges to a point $x$. For each $k$ the tail $x_k, x_{k+1}, \dots$ lies in $A_k$, and $A_k$ is closed, so $x \in A_k$. Hence $x \in \bigcap_n A_n$. That intersection is in fact a single point, since two of its points lie in every $A_n$ and so are at distance at most $\operatorname{diam} A_n$, which tends to zero.
:::

:::

::: pf-step
If every such nested sequence has nonempty intersection, then $(X,d)$ is complete.

::: pf-proof
Let $(x_n)$ be a Cauchy sequence. For each $n$ choose $i(n)$ with $i(n) < i(n+1)$ and $d(x_k, x_m) < 2^{-n}$ whenever $k, m \ge i(n)$, and let $C_n$ be the closed ball of radius $2^{-n+1}$ about $x_{i(n)}$. Each $C_n$ is nonempty and closed, $C_{n+1} \subset C_n$ because $d(x_{i(n+1)}, x_{i(n)}) < 2^{-n}$ and $2^{-n} + 2^{-n} = 2^{-n+1}$, and $\operatorname{diam} C_n \le 2^{-n+2} \to 0$. By hypothesis there is $x \in \bigcap_n C_n$. Given $\epsilon > 0$ take $n$ with $2^{-n+1} < \epsilon/2$, and let $k \ge i(n)$; then $d(x, x_k) \le d(x, x_{i(n)}) + d(x_{i(n)}, x_k) \le 2^{-n+1} + 2^{-n} < \epsilon$. So $x_n \to x$, and every Cauchy sequence converges.
:::

:::

::: pf-step
$(X,d)$ is complete if and only if every nested sequence of nonempty closed sets with diameters tending to zero has nonempty intersection. $\square$

::: pf-proof
The two implications are steps 1 and 2.
:::

:::

:::

:::
