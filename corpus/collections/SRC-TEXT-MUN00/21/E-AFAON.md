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
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Restructured as a Lamport proof of the same argument, with one circular citation removed: the
    continuity of the reciprocal was taken from Exercise 21.12(c), which is where Lemma 21.4 is proved,
    so the solution now uses Lemma 21.4 as the book states it on printed p. 131, whose quotient clause
    is exactly the continuity needed, and follows the exercise's own hint. Subtraction is now taken
    from Lemma 21.4 rather than composed from addition and negation. The quotient step also records
    that the pairs lie in the subspace R x (R - {0}) and converge there, which the earlier prose left
    implicit. The statement was checked against Munkres, Topology (2000), Section 21 Exercise 5,
    printed p. 134.
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

The complete published solution is **"positron0802", *Solutions to Topology, Chapter 2* (1 January 2021), Exercise 21.5, PDF p. 25** (`tmp/sources/munkres-solutions-positron-ch2.pdf`); the route through Lemma 21.4 and Theorem 21.3 is that solution's and is the book's own hint. One citation is corrected and one hypothesis made explicit: the card earlier obtained the continuity of $t\mapsto 1/t$ from Exercise 21.12(c), which is the exercise in which Lemma 21.4 itself is proved, so citing it would argue in a circle, whereas Lemma 21.4 as the book states it (printed p. 131) includes the quotient operation; and the quotient step now records that the pairs $(x_{n},y_{n})$ lie in the subspace $\RR\times(\RR-\theset{0})$ in which the quotient is continuous.

The statement was checked against Munkres, *Topology* (2000), §21 Exercise 5, printed p. 134, with Theorem 21.3 on printed p. 130, Lemma 21.4 on printed p. 131 and Exercise 19.6 on printed p. 118. Throughout, $x_{n}\to x$ and $y_{n}\to y$ in $\RR$, and the four operations are written as maps of the product,
$$
\alpha(x,y)\coloneqq x+y,\qquad \delta(x,y)\coloneqq x-y,\qquad \mu(x,y)\coloneqq xy,\qquad \kappa(x,y)\coloneqq x/y,
$$
the last defined on $\RR\times(\RR-\theset{0})$.

::: pf

::: {.pf-step #pair}

$(x_{n},y_{n})\to(x,y)$ in $\RR^{2}$.

::: pf-proof

By Exercise 19.6 (printed p. 118) a sequence in a product space converges to a point exactly when each of its coordinate sequences converges to the corresponding coordinate of that point. With the two-point index set this says that $(x_{n},y_{n})\to(x,y)$ in $\RR\times\RR$ because $x_{n}\to x$ and $y_{n}\to y$; and the topology of $\RR^{2}$ is that of $\RR\times\RR$ (Theorem 20.3, printed p. 123).

:::

:::

::: {.pf-step #sum}

$x_{n}+y_{n}\to x+y$.

::: pf-proof

Addition is a continuous map $\RR\times\RR\to\RR$ (Lemma 21.4, printed p. 131), and a continuous map carries a convergent sequence to the sequence of the images of its limit (Theorem 21.3, printed p. 130). Applied to the sequence of step [](#pair){.pf-ref} this gives $x_{n}+y_{n}=\alpha(x_{n},y_{n})\to\alpha(x,y)=x+y$.

:::

:::

::: {.pf-step #difference}

$x_{n}-y_{n}\to x-y$.

::: pf-proof

The same argument with the subtraction operation, which Lemma 21.4 (printed p. 131) lists among the continuous maps $\RR\times\RR\to\RR$: $x_{n}-y_{n}=\delta(x_{n},y_{n})\to\delta(x,y)=x-y$ by Theorem 21.3 (printed p. 130) and step [](#pair){.pf-ref}.

:::

:::

::: {.pf-step #product}

$x_{n}y_{n}\to xy$.

::: pf-proof

Multiplication is a continuous map $\RR\times\RR\to\RR$ (Lemma 21.4, printed p. 131); so Theorem 21.3 (printed p. 130) applied to step [](#pair){.pf-ref} gives $x_{n}y_{n}=\mu(x_{n},y_{n})\to\mu(x,y)=xy$.

:::

:::

::: {.pf-step #quotient}

If $y_{n}\neq0$ for every $n$ and $y\neq0$, then $x_{n}/y_{n}\to x/y$.

::: pf-proof

The pairs $(x_{n},y_{n})$ all lie in the subspace $Z\coloneqq\RR\times(\RR-\theset{0})$ of $\RR^{2}$, and $(x,y)\in Z$ by the hypothesis $y\neq0$; since a neighbourhood of a point of a subspace is the trace on it of a neighbourhood of the point in the larger space, and $(x_{n},y_{n})\to(x,y)$ in $\RR^{2}$ by step [](#pair){.pf-ref}, the sequence converges to $(x,y)$ in $Z$ as well.

The quotient operation is a continuous map $Z\to\RR$ (Lemma 21.4, printed p. 131). So Theorem 21.3 (printed p. 130) applies to it and to the convergent sequence of $Z$, giving
$$
x_{n}/y_{n}=\kappa(x_{n},y_{n})\longrightarrow \kappa(x,y)=x/y.
$$

:::

:::

::: pf-step

All four conclusions hold: $x_{n}+y_{n}\to x+y$, $x_{n}-y_{n}\to x-y$, $x_{n}y_{n}\to xy$, and $x_{n}/y_{n}\to x/y$ when each $y_{n}$ and $y$ are nonzero.

::: pf-proof

These are steps [](#sum){.pf-ref}, [](#difference){.pf-ref}, [](#product){.pf-ref} and [](#quotient){.pf-ref}, each obtained from the convergence of the pairs by the continuity of the corresponding operation of Lemma 21.4 (printed p. 131) through Theorem 21.3 (printed p. 130). That is the theorem stated in the exercise.

:::

:::

:::

:::
