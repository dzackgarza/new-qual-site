---
schema: qual/card@1
id: E-FB9OZ
kind: problem
title: Closure of the eventually-zero sequences in the uniform topology
classification:
  areas:
  - topology
  topics:
  - Closure
  - Metric Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §20 Exercise 5, printed p. 127, with the uniform
    metric of printed p. 124; the stored statement is the printed question.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: "positron0802", "Solutions to Topology,
    Chapter 2" (1 January 2021), Exercise 20.5, PDF p. 19. The closure of the eventually-
    zero sequences in the uniform topology is the set of sequences converging to 0: a
    sequence not converging to 0 has infinitely many entries bounded away from 0, no
    eventually-zero sequence can come within epsilon of it, and a sequence converging to 0
    is approximated by its truncation. (tmp/sources/munkres-solutions-positron-ch2.pdf).
---

::: {.exercise}

Let $\RR^\infty$ be the subset of $\RR^\omega$ consisting of all sequences that are eventually zero.
What is the closure of $\RR^\infty$ in $\RR^\omega$ in the uniform topology?
Justify your answer.
:::

::: {.solution}

The answer and both inclusions are those of **"positron0802"**, *Solutions to Topology, Chapter 2* (1 January 2021), Exercise 20.5, PDF p. 19 (`tmp/sources/munkres-solutions-positron-ch2.pdf`); its converse inclusion is written there with a radius $\varepsilon<1$, and the forward inclusion is reorganised below as a statement about a single ball missing $\RR^{\infty}$. The statement was checked against Munkres, *Topology* (2000), §20 Exercise 5, with the uniform metric on printed p. 124, the basis of balls on printed p. 119, and Theorem 17.5(a) on printed p. 96.

Throughout, $\RR^{\infty}$ is the set of sequences $\mathbf{y}\in\RR^{\omega}$ with $y_{i}=0$ for all but finitely many $i$,
$$
\bar\rho(\mathbf{x},\mathbf{y})\coloneqq\sup_{i}\min\theset{\abs{x_{i}-y_{i}},1}
$$
is the uniform metric, and $Z\coloneqq\theset{\mathbf{x}\in\RR^{\omega}\mid x_{i}\to0}$ is the set of sequences converging to $0$.

::: pf

::: {.pf-step #balls}
For every $\mathbf{x}$ and $\varepsilon>0$ the ball $B_{\bar\rho}(\mathbf{x},\varepsilon)$ is open, and every open set containing $\mathbf{x}$ contains such a ball.

::: pf-proof
The collection of $\varepsilon$-balls of a metric is by definition a basis for the metric topology (§20); a basis element is open, and every open set containing a point contains a basis element containing that point.
:::

:::

::: {.pf-step #forward}
If $\mathbf{x}\in\overline{\RR^{\infty}}$, then $x_{i}\to0$.

:::: pf-proof

::: {.pf-step #not-null}
If $x_{i}$ does not converge to $0$, there are $\delta>0$ and infinitely many indices $i$ with $\abs{x_{i}}\geq\delta$.

::: pf-proof
Convergence to $0$ says that for every $\delta>0$ there is $N$ with $\abs{x_{i}}<\delta$ for all $i\geq N$. Its negation is that for some $\delta>0$ no such $N$ works, that is, for every $N$ there is $i\geq N$ with $\abs{x_{i}}\geq\delta$; choosing such an index for $N=1,2,\ldots$ successively and always larger than the previous one gives an infinite strictly increasing family.
:::

:::

::: {.pf-step #empty-ball}
There is $\varepsilon>0$ with $B_{\bar\rho}(\mathbf{x},\varepsilon)\cap\RR^{\infty}=\varnothing$.

::: pf-proof
Take $\delta$ as in step [](#not-null){.pf-ref} and put $\varepsilon\coloneqq\min\theset{\delta,1}/2$, which is positive. Let $\mathbf{y}\in\RR^{\infty}$ and choose $N$ with $y_{i}=0$ for all $i\geq N$; by step [](#not-null){.pf-ref} there is $i\geq N$ with $\abs{x_{i}}\geq\delta$, and for that $i$
$$
\min\theset{\abs{x_{i}-y_{i}},1}=\min\theset{\abs{x_{i}},1}\geq\min\theset{\delta,1}=2\varepsilon>\varepsilon,
$$
so $\bar\rho(\mathbf{x},\mathbf{y})>\varepsilon$ and $\mathbf{y}$ is not in the ball.
:::

:::

::: {.pf-step}
$\mathbf{x}\notin\overline{\RR^{\infty}}$.

::: pf-proof
The open set $B_{\bar\rho}(\mathbf{x},\varepsilon)$ of step [](#empty-ball){.pf-ref} contains $\mathbf{x}$ and meets $\RR^{\infty}$ in no point; by Theorem 17.5(a) a point of the closure has every open set about it meeting the set, so $\mathbf{x}$ is not in the closure.
:::

:::

::::

:::

::: {.pf-step #backward}
If $x_{i}\to0$, then $\mathbf{x}\in\overline{\RR^{\infty}}$.

:::: pf-proof

::: {.pf-step #truncation}
For every $\varepsilon$ with $0<\varepsilon<1$ there is $\mathbf{y}\in\RR^{\infty}$ with $\bar\rho(\mathbf{x},\mathbf{y})<\varepsilon$.

::: pf-proof
Choose $N$ with $\abs{x_{i}}<\varepsilon/2$ for all $i\geq N$, possible because $x_{i}\to0$. Define $y_{i}\coloneqq x_{i}$ for $i<N$ and $y_{i}\coloneqq0$ for $i\geq N$; then $\mathbf{y}$ has only finitely many nonzero coordinates, so $\mathbf{y}\in\RR^{\infty}$, and $\min\theset{\abs{x_{i}-y_{i}},1}=0$ for $i<N$ while $\min\theset{\abs{x_{i}-y_{i}},1}=\min\theset{\abs{x_{i}},1}=\abs{x_{i}}<\varepsilon/2$ for $i\geq N$, the last equality because $\varepsilon<1$. Hence every term of the supremum is below $\varepsilon/2$, so $\bar\rho(\mathbf{x},\mathbf{y})\leq\varepsilon/2<\varepsilon$.
:::

:::

::: {.pf-step}
Every open set containing $\mathbf{x}$ meets $\RR^{\infty}$.

::: pf-proof
Let $U$ be open with $\mathbf{x}\in U$. By step [](#balls){.pf-ref} there is $\varepsilon>0$ with $B_{\bar\rho}(\mathbf{x},\varepsilon)\subset U$; shrinking $\varepsilon$ if necessary we may take $\varepsilon<1$, and then step [](#truncation){.pf-ref} gives a point of $\RR^{\infty}$ inside that ball, hence inside $U$.
:::

:::

::: {.pf-step}
$\mathbf{x}\in\overline{\RR^{\infty}}$.

::: pf-proof
Theorem 17.5(a) says that a point lies in the closure of a set exactly when every open set containing it meets that set, which is step [](#truncation){.pf-ref} together with the preceding step.
:::

:::

::::

:::

::: pf-step
Therefore the closure asks for exactly the sequences converging to $0$:
$$
\boxed{\overline{\RR^{\infty}}=\theset{\mathbf{x}\in\RR^{\omega}\mid x_{i}\to0}}
$$
in the uniform topology.

::: pf-proof
Step [](#forward){.pf-ref} gives $\overline{\RR^{\infty}}\subset Z$ and step [](#backward){.pf-ref} gives $Z\subset\overline{\RR^{\infty}}$, so the two sets are equal.
:::

:::

:::

:::
