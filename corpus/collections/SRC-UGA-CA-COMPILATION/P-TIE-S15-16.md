---
schema: qual/card@1
id: P-TIE-S15-16
kind: problem
title: Analytic functions mapping a closed curve into $\mathbb R$ are constant
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
---

::: {.problem}
Let f be an analytic function on a region Ω. Show that f is a constant if there is a simple closed curve γ in Ω such that its image $f ( \gamma )$ is contained in the real axis.
:::

::: {.remark}
Erratum: as printed, the statement is false unless the Jordan interior of $\gamma$ is contained in $\Omega$.
For example, on
$$
\Omega=\{z:1/2<\abs{z}<2\},
$$
the function
$$
f(z)=z+z^{-1}
$$
is holomorphic and nonconstant, while on the unit circle
$$
f(e^{i\theta})=2\cos\theta\in\RR.
$$
The intended statement is correct when the closed interior bounded by $\gamma$ lies in $\Omega$.
:::

::: {.solution}
Assume the corrected hypothesis that the closure of the Jordan interior $D$ of $\gamma$ is contained in $\Omega$.
Write
$$
f=u+iv.
$$

<1>1. The harmonic function $v$ vanishes on $\gamma$.

::: {.proof}
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

<1>2. One has
$$
v\equiv0
$$
on $D$.

::: {.proof}
Because $f$ is holomorphic on a neighborhood of $\overline D$, the function $v$ is harmonic on $D$ and continuous on $\overline D$. By step <1>1,
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

<1>3. The function $f$ is constant on $D$.

::: {.proof}
By step <1>2,
$$
f(D)\subset\RR.
$$
If $f$ were nonconstant on the open connected set $D$, the open mapping theorem would imply that $f(D)$ is open in $\CC$. But no nonempty subset of $\RR$ is open in $\CC$. Hence $f$ is constant on $D$.
:::

<1>4. The function $f$ is constant on all of $\Omega$.

::: {.proof}
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

<1>5. Q.E.D.

::: {.proof}
Steps <1>1--<1>4 prove the corrected theorem. The remark gives a counterexample to the uncorrected source statement.
:::
:::
