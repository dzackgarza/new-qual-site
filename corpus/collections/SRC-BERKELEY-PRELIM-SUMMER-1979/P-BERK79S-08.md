---
schema: qual/card@1
id: P-BERK79S-08
kind: problem
title: A uniformly continuous homeomorphism onto $\RR^n$ has full domain
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Showed U is closed. A sequence in U converging to a point of closure is
    Cauchy; uniform continuity sends it to a Cauchy sequence in R^n, hence
    to a limit y. Surjectivity gives y=h(u) for u in U, and continuity of
    h^{-1} forces the original sequence to converge to u. Thus the closure
    point already lies in U. Since U is nonempty, open, and closed in
    connected R^n, it equals R^n.
---

::: {.problem}
Let $U\subseteq\mathbb R^n$ be open.
Suppose $h:U\to\mathbb R^n$ is a uniformly continuous homeomorphism from $U$ onto $\mathbb R^n$.
Prove that
\[
U=\mathbb R^n.
\]
:::

::: {.solution}
<1>1. Let $x\in\overline U$. There is a sequence $(x_k)$ in $U$ such that
$$
x_k\longrightarrow x.
$$

::: {.proof}
This is the sequential characterization of closure in the metric space
$\RR^n$.
:::

<1>2. The sequence $(x_k)$ from step <1>1 is Cauchy.

::: {.proof}
Every convergent sequence in a metric space is Cauchy.
:::

<1>3. The sequence
$$
\bigl(h(x_k)\bigr)
$$
is Cauchy in $\RR^n$.

::: {.proof}
Let $\varepsilon>0$. Since $h$ is uniformly continuous, there is
$\delta>0$ such that
$$
\norm{u-v}<\delta
\implies
\norm{h(u)-h(v)}<\varepsilon
$$
for all $u,v\in U$.

By step <1>2, there is $N$ such that
$$
\norm{x_k-x_\ell}<\delta
$$
whenever $k,\ell\geq N$. Therefore
$$
\norm{h(x_k)-h(x_\ell)}<\varepsilon
$$
for all $k,\ell\geq N$. Hence $(h(x_k))$ is Cauchy.
:::

<1>4. There is a point $y\in\RR^n$ such that
$$
h(x_k)\longrightarrow y.
$$

::: {.proof}
Euclidean space $\RR^n$ is complete. Step <1>3 therefore implies
convergence of the Cauchy sequence $(h(x_k))$.
:::

<1>5. There is a point $u\in U$ such that
$$
h(u)=y.
$$

::: {.proof}
The map
$$
h:U\longrightarrow\RR^n
$$
is onto by hypothesis. Apply surjectivity to the point $y$ from step
<1>4.
:::

<1>6. The sequence $(x_k)$ converges to $u$.

::: {.proof}
Because $h$ is a homeomorphism, its inverse
$$
h^{-1}:\RR^n\longrightarrow U
$$
is continuous. Step <1>4 gives
$$
h(x_k)\longrightarrow h(u).
$$
Applying the continuous map $h^{-1}$ yields
$$
x_k
=
h^{-1}(h(x_k))
\longrightarrow
h^{-1}(h(u))
=
u.
$$
:::

<1>7. Every point of $\overline U$ lies in $U$.

::: {.proof}
Fix $x\in\overline U$ and choose $(x_k)$ as in step <1>1. Step <1>1 gives
$$
x_k\longrightarrow x,
$$
while step <1>6 gives
$$
x_k\longrightarrow u.
$$
Limits in $\RR^n$ are unique, so
$$
x=u\in U.
$$
Thus
$$
\overline U\subseteq U.
$$
The reverse inclusion always holds, hence
$$
\overline U=U.
$$
:::

<1>8. The set $U$ is both open and closed in $\RR^n$, and it is nonempty.

::: {.proof}
It is open by hypothesis and closed by step <1>7. It is nonempty because
there is a surjective map
$$
h:U\to\RR^n,
$$
and $\RR^n$ is nonempty.
:::

<1>9. One has
$$
\boxed{
U=\RR^n.
}
$$

::: {.proof}
Euclidean space $\RR^n$ is connected. By step <1>8, $U$ is a nonempty
subset which is both open and closed. The only such subset of a connected
space is the whole space.
:::

<1>10. Q.E.D.

::: {.proof}
Step <1>9 is the required conclusion.
:::
:::
