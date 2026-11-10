---
schema: qual/card@1
id: E-AFAON
kind: problem
title: Arithmetic of convergent sequences
classification:
  areas:
  - topology
  topics:
  - Convergence
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §21 Exercise 5, printed p. 134, with Lemma 21.4,
    Theorem 21.3 and Exercise 19.6; the four conclusions and the hint are stored as printed.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 2" (1 January 2021), Exercise 21.5, PDF p. 25. The sequence (x_n, y_n) converges
    in the product, so its image under the continuous addition, subtraction (via negation)
    and multiplication converges, and the quotient follows from the continuity of the
    reciprocal on R - {0}. (tmp/sources/munkres-solutions-positron-ch2.pdf).
---

::: {.exercise}

Theorem.
Let $x_n \to x$ and $y_n \to y$ in the space $\RR$.
Then

$$
\begin{array}{c}
x_n + y_n \to x + y, \\
x_n - y_n \to x - y, \\
x_n y_n \to xy,
\end{array}
$$

and provided that each $y_n \neq 0$ and $y \neq 0$,

$$
x_n / y_n \to x/y.
$$

[Hint: Apply Lemma 21.4; recall from the exercises of §19 that if $x_n \to x$ and $y_n \to y$, then $x_n \times y_n \to x \times y$.]
:::

::: {.solution}
The complete published solution is **"positron0802", *Solutions to Topology, Chapter 2* (1 January 2021), Exercise 21.5, PDF p. 25** (`tmp/sources/munkres-solutions-positron-ch2.pdf`); the argument is theirs, following the book's hint.

By Exercise 19.6, $x_{n}\to x$ and $y_{n}\to y$ in $\RR$ give $(x_{n},y_{n})\to(x,y)$ in $\RR\times\RR$. By Lemma 21.4 (printed p. 130) the maps $+:*\RR\times\RR\to\RR$ and $\cdot:\RR\times\RR\to\RR$ are continuous, and by Theorem 21.3 (sequences are preserved by continuous maps into a metric space) applied to the sequence $(x_{n},y_{n})$ of $\RR^{2}$,
$$
x_{n}+y_{n}=+\big((x_{n},y_{n})\big)\longrightarrow +\big((x,y)\big)=x+y,\qquad
x_{n}y_{n}=\cdot\big((x_{n},y_{n})\big)\longrightarrow xy .
$$
For the difference, $y\mapsto-y$ is continuous, so $(-y_{n})\to-y$ and $x_{n}-y_{n}=x_{n}+(-y_{n})\to x-y$ by the addition case.

For the quotient, suppose $y_{n}\ne0$ for all $n$ and $y\ne0$. The map $t\mapsto1/t$ is continuous on $\RR-\{0\}$ (Exercise 21.12(c), or Lemma 21.4 if quoted in that form), so $1/y_{n}\to1/y$; then $x_{n}\cdot(1/y_{n})\to x\cdot(1/y)$ by the product case, that is $x_{n}/y_{n}\to x/y$.
:::
