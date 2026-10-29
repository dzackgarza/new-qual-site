---
schema: qual/card@1
id: P-TIE-S15-16
kind: problem
title: Analytic functions mapping a closed curve into $\RR$ are constant
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against the retained Questions_from_Tie.pdf compilation, section Spring 2015, question 16.
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: The source does not require the interior of the curve to lie in the region, which makes the claim false (z + 1/z on an annulus around the unit circle). The statement now requires the interior of the curve to lie in the region.
---

::: {.problem}
Let $f$ be an analytic function on a region $\Omega$. Show that $f$ is a constant if there is a simple closed curve $\gamma$ in $\Omega$, whose interior is contained in $\Omega$, such that its image $f(\gamma)$ is contained in the real axis.
:::

::: {.solution}

Let $D$ be the Jordan interior of $\gamma$, so that $\overline D=D\cup\gamma\subset\Omega$.
Write
$$
f=u+iv.
$$

::: pf

::: {.pf-step #s1-1}

The harmonic function $v$ vanishes on $\gamma$.


::: pf-proof

The hypothesis
$$
f(\gamma)\subset\RR
$$
means exactly that
$$
\operatorname{Im}f(z)=0
$$
for every $z\in\gamma$. Since $v=\operatorname{Im}f$, one has
$$
v=0
$$
on $\partial D=\gamma$.

:::

:::

::: {.pf-step #s1-2}

One has
$$
v\equiv0
$$
on $D$.


::: pf-proof

Because $f$ is holomorphic on a neighborhood of $\overline D$, the function $v$ is harmonic on $D$ and continuous on $\overline D$. By step [](#s1-1){.pf-ref},
$$
v=0
$$
on the boundary.

The maximum principle applied to $v$ gives
$$
v\le0
$$
on $D$, while the maximum principle applied to $-v$ gives
$$
v\ge0.
$$
Therefore
$$
v\equiv0
$$
on $D$.

:::

:::

::: {.pf-step #s1-3}

The function $f$ is constant on $D$.


::: pf-proof

By step [](#s1-2){.pf-ref},
$$
f(D)\subset\RR.
$$
If $f$ were nonconstant on the open connected set $D$, the open mapping theorem would imply that $f(D)$ is open in $\CC$. But no nonempty subset of $\RR$ is open in $\CC$. Hence $f$ is constant on $D$.

:::

:::

::: {.pf-step #s1-4}

The function $f$ is constant on all of $\Omega$.


::: pf-proof

Let
$$
f|_D\equiv c.
$$
Then the holomorphic function
$$
f-c
$$
vanishes on the nonempty open subset $D$ of the region $\Omega$. By the identity theorem,
$$
f-c\equiv0
$$
throughout $\Omega$.

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} through [](#s1-4){.pf-ref} prove that $f$ is constant.

:::

:::

:::
