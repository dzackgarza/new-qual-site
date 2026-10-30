---
schema: qual/card@1
id: P-UCLARA14F-12
kind: problem
title: Maximum principle for bounded subharmonic functions outside the unit disk
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Transcribed from the retained UCLA Analysis Qualifying Exam Solutions compendium, Fall 2014 section; the official exam PDF is image-only.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Retranscribed the font-garbled statement in LaTeX from Problem 12 on page 2 of the official analysis-14F.pdf exam, checked against the Fall 2014 section of UCLA_Solutions.pdf.
---

::: {.problem}
Let $\Omega = \{ z \in \CC ; \abs{z} > 1 \}$. Suppose $u : \overline{\Omega} \to \RR$ is bounded and continuous on $\overline{\Omega}$ and that it is subharmonic on $\Omega$. Prove the following: If $u(z) \leq 0$ for all $\abs{z} = 1$ then $u(z) \leq 0$ for all $z \in \Omega$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Since $u$ is bounded on $\overline\Omega$, there is $M>0$ such that
$$
\abs{u(z)}\le M
\qquad(z\in\overline\Omega).
$$


::: pf-proof

This is the boundedness hypothesis.

:::

:::

::: pf-step

Fix $\varepsilon>0$ and define
$$
v_\varepsilon(z)
=
u(z)-\varepsilon\log\abs{z}.
$$
Then $v_\varepsilon$ is subharmonic on $\Omega$ and continuous on
$\overline\Omega$.


::: pf-proof

The function
$$
z\longmapsto\log\abs{z}
$$
is harmonic on $\Omega$, since $0\notin\Omega$. The difference of a
subharmonic function and a harmonic function is subharmonic. Continuity is
immediate from the continuity of the two summands.

:::

:::

::: {.pf-step #s1-3}

On the inner boundary,
$$
v_\varepsilon(z)\le0
\qquad(\abs{z}=1).
$$


::: pf-proof

If $\abs{z}=1$, then
$$
\log\abs{z}=0.
$$
Hence
$$
v_\varepsilon(z)=u(z)\le0
$$
by hypothesis.

:::

:::

::: {.pf-step #s1-4}

Choose $R>1$ so large that
$$
M-\varepsilon\log R<0.
$$
Then
$$
v_\varepsilon(z)<0
\qquad(\abs{z}\ge R).
$$


::: pf-proof

For $\abs{z}\ge R$, step [](#s1-1){.pf-ref} gives
$$
v_\varepsilon(z)
\le
M-\varepsilon\log\abs{z}
\le
M-\varepsilon\log R
<0.
$$

:::

:::

::: {.pf-step #s1-5}

On the closed annulus
$$
A_R=\{z:1\le\abs{z}\le R\},
$$
one has
$$
v_\varepsilon\le0.
$$


::: pf-proof

The function $v_\varepsilon$ is continuous on $A_R$ and subharmonic in its
interior. By steps [](#s1-3){.pf-ref} and [](#s1-4){.pf-ref}, it is nonpositive on both boundary circles
$$
\abs{z}=1
\qquad\text{and}\qquad
\abs{z}=R.
$$
The maximum principle for subharmonic functions therefore gives
$$
v_\varepsilon(z)\le0
$$
throughout the annulus.

:::

:::

::: {.pf-step #s1-6}

In fact,
$$
v_\varepsilon(z)\le0
\qquad(z\in\overline\Omega).
$$


::: pf-proof

Step [](#s1-5){.pf-ref} covers the region
$$
1\le\abs{z}\le R.
$$
Step [](#s1-4){.pf-ref} covers
$$
\abs{z}\ge R.
$$
Together they cover $\overline\Omega$.

:::

:::

::: {.pf-step #s1-7}

For every $z\in\Omega$ and every $\varepsilon>0$,
$$
u(z)\le\varepsilon\log\abs{z}.
$$


::: pf-proof

Step [](#s1-6){.pf-ref} says
$$
u(z)-\varepsilon\log\abs{z}\le0.
$$
Rearrange.

:::

:::

::: {.pf-step #s1-8}

Therefore
$$
\boxed{u(z)\le0\qquad(z\in\Omega)}.
$$


::: pf-proof

Fix $z\in\Omega$. Since
$$
\log\abs{z}>0
$$
is finite, step [](#s1-7){.pf-ref} holds for every $\varepsilon>0$. Letting
$$
\varepsilon\downarrow0
$$
gives
$$
u(z)\le0.
$$

:::

:::

::: pf-qed

Step [](#s1-8){.pf-ref} is the required conclusion.

:::

:::

:::
