---
schema: qual/card@1
id: P-AZOFF-E06
kind: problem
title: Entire functions with $|f(z)|\ge|z|$
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Liouville, FTA, and power series, Problem 6, in the deterministic MinerU Flash extraction assets/attachments/Azoff Problems by Topic_extracted.md.
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    First forced f(0)=0 using Liouville on z/f(z) under the contrary
    assumption. Then f(z)/z extends to an entire function bounded away from
    zero, so its reciprocal is bounded entire and hence constant. The
    resulting functions are exactly cz with |c| at least one.
---

::: {.problem}
Find all entire functions $f$ which satisfy $\abs{f(z)} \geq \abs{z}$ for all $z \in \CC$. Be sure to prove your list is complete.
:::

::: {.solution}
<1>1. One has
$$
f(0)=0.
$$

::: {.proof}
Suppose instead that $f(0)\neq0$. For every $z\neq0$, the hypothesis gives
$$
\abs{f(z)}\geq\abs{z}>0,
$$
so together with $f(0)\neq0$, the function $f$ has no zeros on $\CC$.
Hence
$$
g(z)=\frac{z}{f(z)}
$$
is entire. For $z\neq0$,
$$
\abs{g(z)}
=
\frac{\abs{z}}{\abs{f(z)}}
\leq1,
$$
and $g(0)=0$. Thus $g$ is bounded and entire. By Liouville's theorem, $g$
is constant, and since $g(0)=0$, one has $g\equiv0$. This is impossible
for any $z\neq0$, because $z/f(z)\neq0$. Therefore $f(0)=0$.
:::

<1>2. Define
$$
h(z)
=
\begin{cases}
\dfrac{f(z)}{z},&z\neq0,\\
f'(0),&z=0.
\end{cases}
$$
Then $h$ is entire and
$$
\abs{h(z)}\geq1
$$
for every $z\in\CC$.

::: {.proof}
By step <1>1, $f(0)=0$. The quotient $f(z)/z$ therefore has a removable
singularity at $0$, and its limiting value there is
$$
\lim_{z\to0}\frac{f(z)}z=f'(0).
$$
Thus the displayed definition makes $h$ entire.

For $z\neq0$, the given inequality yields
$$
\abs{h(z)}
=
\frac{\abs{f(z)}}{\abs{z}}
\geq1.
$$
Taking $z\to0$ and using continuity of $h$ gives
$\abs{h(0)}\geq1$ as well.
:::

<1>3. The function $h$ is constant.

::: {.proof}
Step <1>2 shows that $h$ has no zeros. Hence $1/h$ is entire, and
$$
\abs{\frac1{h(z)}}\leq1
$$
for every $z\in\CC$. Liouville's theorem implies that $1/h$ is constant.
Therefore $h$ is constant.
:::

<1>4. Every function satisfying the hypothesis has the form
$$
f(z)=cz
$$
for some $c\in\CC$ with $\abs{c}\geq1$.

::: {.proof}
By step <1>3, write $h\equiv c$. Step <1>2 gives $\abs{c}\geq1$, and the
definition of $h$ gives $f(z)=zh(z)=cz$ for $z\neq0$. The same formula also
holds at $z=0$ by step <1>1.
:::

<1>5. Conversely, every function $f(z)=cz$ with $\abs{c}\geq1$ satisfies
the required inequality.

::: {.proof}
Such a function is entire, and
$$
\abs{f(z)}
=
\abs{c}\abs{z}
\geq
\abs{z}
$$
for every $z\in\CC$.
:::

<1>6. The complete list is
$$
\boxed{
f(z)=cz,
\qquad
c\in\CC,
\qquad
\abs{c}\geq1.
}
$$

::: {.proof}
Step <1>4 proves that every solution is on this list, and step <1>5 proves
that every function on the list is a solution.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>6 is the requested complete classification.
:::
:::
