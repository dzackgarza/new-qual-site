---
schema: qual/card@1
id: P-UMNCP-S11-04
kind: problem
title: Second derivative equality case in Schwarz lemma
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Spring 2011, 4 as reproduced in Cihan Bahran's vendored 2013 University of Minnesota complex-prelim solution compilation. The source notes identify the omitted self-map hypothesis and explain that the printed statement is false without it; the card includes that necessary correction.
---

::: {.problem}
Let \(f:\DD\to\DD\) be holomorphic and suppose
\[
f(0)=f'(0)=0.
\]
Prove that \(|f''(0)|\le2\), and describe all such \(f\) for which \(|f''(0)|=2\).

The retained solution notes explicitly record that the printed exam omitted the necessary hypothesis \(f(\DD)\subseteq\DD\); it is included here because without it the assertion is false.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Schwarz's lemma gives
$$
|f(z)|\le |z|
$$
for every $z\in\DD$.


::: pf-proof

The function $f$ maps the unit disk to itself and satisfies $f(0)=0$, so Schwarz's lemma applies.

:::

:::

::: pf-step

The function
$$
g(z)=
\begin{cases}
f(z)/z,&z\ne0,\\
f'(0),&z=0
\end{cases}
$$
is holomorphic on $\DD$, maps $\DD$ into the closed unit disk, and satisfies $g(0)=0$.


::: pf-proof

Since $f(0)=0$, the quotient $f(z)/z$ has a removable singularity at $0$ with value $f'(0)$. Thus $g$ is holomorphic. Step [](#s1-1){.pf-ref} gives
$$
|g(z)|\le1
$$
for $z\ne0$, and continuity gives the same bound at $0$. The hypothesis $f'(0)=0$ gives $g(0)=0$.

:::

:::

::: {.pf-step #s1-3}

A second application of Schwarz's lemma gives
$$
|g(z)|\le |z|
$$
for every $z\in\DD$.


::: pf-proof

If $g$ were a unimodular constant then $g(0)$ would have modulus $1$, contrary to $g(0)=0$. Hence in fact $|g(z)|<1$ throughout the disk, and Schwarz's lemma applies to $g$.

:::

:::

::: {.pf-step #s1-4}

There is a holomorphic function $h:\DD\to\overline{\DD}$ such that
$$
\boxed{f(z)=z^2h(z)}.
$$


::: pf-proof

By step [](#s1-3){.pf-ref}, the function
$$
h(z)=
\begin{cases}
g(z)/z,&z\ne0,\\
g'(0),&z=0
\end{cases}
$$
has a removable singularity at $0$ and is holomorphic there. Moreover,
$$
|h(z)|\le1.
$$
Since $g(z)=zh(z)$ and $f(z)=zg(z)$, one gets $f(z)=z^2h(z)$.

:::

:::

::: {.pf-step #s1-5}

One has
$$
f''(0)=2h(0).
$$


::: pf-proof

Differentiate
$$
f(z)=z^2h(z)
$$
twice:
$$
f''(z)=2h(z)+4zh'(z)+z^2h''(z).
$$
Evaluating at $z=0$ gives the formula.

:::

:::

::: {.pf-step #s1-6}

Therefore
$$
\boxed{|f''(0)|\le2}.
$$


::: pf-proof

By steps [](#s1-4){.pf-ref} through [](#s1-5){.pf-ref},
$$
|f''(0)|=2|h(0)|\le2.
$$

:::

:::

::: {.pf-step #s1-7}

Equality
$$
|f''(0)|=2
$$
holds if and only if
$$
\boxed{f(z)=e^{i\theta}z^2}
$$
for some $\theta\in\RR$.


::: pf-proof

If equality holds, then step [](#s1-5){.pf-ref} gives
$$
|h(0)|=1.
$$
Since $|h|\le1$ on the disk, the maximum-modulus principle forces $h$ to be constant:
$$
h(z)=e^{i\theta}
$$
for some real $\theta$. Hence
$$
f(z)=e^{i\theta}z^2.
$$

Conversely, every function of this form maps the disk into itself, satisfies
$$
f(0)=f'(0)=0,
$$
and has
$$
f''(0)=2e^{i\theta},
$$
whose modulus is $2$.

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} proves the bound, and step [](#s1-7){.pf-ref} gives the complete equality case.

:::

:::

:::
