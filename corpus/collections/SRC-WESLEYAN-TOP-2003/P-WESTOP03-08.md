---
schema: qual/card@1
id: P-WESTOP03-08
kind: problem
title: Are maps from a simply connected space to $S^1$ nullhomotopic?
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- {event: source-checked, by: gpt-5.6-sol, date: 2026-09-14}
---

::: {.problem}
Suppose $X$ is simply connected. Prove or give a counterexample to the assertion that every map
\[
X\to S^1
\]
is homotopic to a constant map.
:::

::: {.solution}
The assertion is true under the standard meaning of simply connected: $X$ is path connected and $\pi_1(X)=0$.

<1>1. Let
\[
p:\mathbb R\to S^1,
\qquad
p(t)=e^{2\pi it},
\]
be the universal covering map, and let $f:X\to S^1$ be continuous.

::: {.proof}
The exponential map displayed above is the standard universal cover of the circle.
:::

<1>2. Fix $x_0\in X$ and choose $t_0\in\mathbb R$ such that
\[
p(t_0)=f(x_0).
\]

::: {.proof}
The covering map $p$ is surjective, so such a lift of the basepoint value exists.
:::

<1>3. The map $f$ admits a lift
\[
\widetilde f:X\to\mathbb R
\]
with
\[
\widetilde f(x_0)=t_0,
\qquad
p\circ\widetilde f=f.
\]

::: {.proof}
The lifting criterion for the covering $p:\mathbb R\to S^1$ says that a based map $f:(X,x_0)\to(S^1,f(x_0))$ lifts precisely when
\[
f_*\pi_1(X,x_0)
\subseteq
p_*\pi_1(\mathbb R,t_0).
\]
Since $X$ is simply connected,
\[
\pi_1(X,x_0)=0.
\]
Also $\mathbb R$ is simply connected, so the right side is zero. Thus the inclusion holds and the lift exists.
:::

<1>4. Since $\mathbb R$ is contractible, $\widetilde f$ is homotopic to the constant map with value $t_0$.

::: {.proof}
An explicit homotopy is
\[
\widetilde H(x,s)=(1-s)\widetilde f(x)+st_0,
\qquad 0\leq s\leq1.
\]
At $s=0$ this is $\widetilde f$, and at $s=1$ it is the constant map $t_0$.
:::

<1>5. Composing this homotopy with $p$ gives a homotopy
\[
H=p\circ\widetilde H:X\times I\to S^1
\]
from $f$ to the constant map with value $f(x_0)$.

::: {.proof}
At $s=0$,
\[
H(x,0)=p(\widetilde f(x))=f(x).
\]
At $s=1$,
\[
H(x,1)=p(t_0)=f(x_0),
\]
independent of $x$.
:::

<1>6. Therefore
\[
\boxed{\text{every continuous map }X\to S^1\text{ is nullhomotopic}.}
\]

::: {.proof}
Step <1>5 explicitly constructs a homotopy from an arbitrary $f$ to a constant map.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>6 proves the assertion.
:::
:::
