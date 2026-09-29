---
schema: qual/card@1
id: P-AZOFF-A05
kind: problem
title: Uniform differentiability is equivalent to continuity of $f'$
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Compactness, connectedness, and functions of one real variable, Problem 5, in the deterministic MinerU Flash extraction assets/attachments/Azoff Problems by Topic_extracted.md. Flash emits a control character where the prime in $f'$ occurs in the final sentence; the correction is determined by the displayed uniform-differentiability definition and the stated equivalence.
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Checked both recorded source appearances. For continuous f', compactness
    gives uniform continuity of f' and the mean value theorem controls every
    difference quotient uniformly. Conversely, applying uniform
    differentiability to (x,y) and to (y,x) makes the same difference
    quotient approximate both f'(y) and f'(x), proving f' uniformly
    continuous. Neither source supplies a worked proof.
---

::: {.problem}
Let $f$ be differentiable on $[a,b]$.
Say that $f$ is *uniformly differentiable* if for every $\varepsilon>0$ there exists $\delta>0$ such that
\[
\left|\frac{f(x)-f(y)}{x-y}-f'(y)\right|<\varepsilon
\]
whenever $x,y\in[a,b]$, $x\ne y$, and $|x-y|<\delta$.

Prove that $f$ is uniformly differentiable on $[a,b]$ if and only if $f'$ is continuous on $[a,b]$.
:::

::: {.solution}
For distinct $x,y\in[a,b]$, write
$$
Q(x,y)=\frac{f(x)-f(y)}{x-y}.
$$
Then
$$
Q(y,x)=Q(x,y).
$$

::: pf

::: {.pf-step #s1}

If $f'$ is continuous on $[a,b]$, then $f'$ is uniformly continuous
on $[a,b]$.

::: pf-proof

The interval $[a,b]$ is compact. Hence the Heine--Cantor theorem applied to
the continuous function $f'$ shows that $f'$ is uniformly continuous.

:::

:::

::: {.pf-step #s2}

If $f'$ is continuous on $[a,b]$, then $f$ is uniformly
differentiable on $[a,b]$.

::: pf-proof

Let $\varepsilon>0$. By step [](#s1){.pf-ref}, choose $\delta>0$ such that
$$
\abs{u-v}<\delta
\quad\Longrightarrow\quad
\abs{f'(u)-f'(v)}<\varepsilon
$$
for all $u,v\in[a,b]$.

Take distinct $x,y\in[a,b]$ with
$$
\abs{x-y}<\delta.
$$
The mean value theorem applied to the interval with endpoints $x$ and $y$
gives a point $c$ strictly between them such that
$$
Q(x,y)=f'(c).
$$
Since $c$ lies between $x$ and $y$,
$$
\abs{c-y}<\abs{x-y}<\delta.
$$
Therefore
$$
\abs{Q(x,y)-f'(y)}
=
\abs{f'(c)-f'(y)}
<
\varepsilon.
$$
The same $\delta$ works for every such pair $x,y$, so $f$ is uniformly
differentiable.

:::

:::

::: {.pf-step #s3}

If $f$ is uniformly differentiable on $[a,b]$, then $f'$ is uniformly
continuous on $[a,b]$.

::: pf-proof

Let $\varepsilon>0$. By uniform differentiability, choose $\delta>0$ such
that for distinct $x,y\in[a,b]$ with $\abs{x-y}<\delta$,
$$
\abs{Q(x,y)-f'(y)}<\frac{\varepsilon}{2}.
$$
Apply the same estimate to the ordered pair $(y,x)$. Since
$$
Q(y,x)=Q(x,y),
$$
we also have
$$
\abs{Q(x,y)-f'(x)}<\frac{\varepsilon}{2}.
$$
Hence
$$
\begin{aligned}
\abs{f'(x)-f'(y)}
&\leq
\abs{f'(x)-Q(x,y)}
+
\abs{Q(x,y)-f'(y)}\\
&<
\varepsilon.
\end{aligned}
$$
If $x=y$, the same conclusion is immediate. Hence the estimate holds for
all $x,y\in[a,b]$ with $\abs{x-y}<\delta$.
Thus $f'$ is uniformly continuous on $[a,b]$.

:::

:::

::: {.pf-step #s4}

If $f$ is uniformly differentiable on $[a,b]$, then $f'$ is
continuous on $[a,b]$.

::: pf-proof

Every uniformly continuous function is continuous. Apply this to $f'$ using
step [](#s3){.pf-ref}.

:::

:::

::: {.pf-step #s5}

Therefore
$$
\boxed{
f\text{ is uniformly differentiable on }[a,b]
\quad\Longleftrightarrow\quad
f'\text{ is continuous on }[a,b]
}.
$$

::: pf-proof

Step [](#s2){.pf-ref} proves the reverse implication, and step [](#s4){.pf-ref} proves the forward
implication.

:::

:::

::: pf-qed

Step [](#s5){.pf-ref} is the required equivalence.

:::

:::

:::
