---
schema: qual/card@1
id: P-RAF06C
kind: problem
title: "Range and nullspace of T and T*: orthogonal complements and closed range"
classification:
  areas:
  - real-analysis
  topics:
  - Hilbert Spaces
  - Bounded Operators
  - Adjoints
  - Closed Range
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: problem
Let $H$ be a Hilbert space, $T : H \to H$ a bounded linear operator, $T^* : H \to H$ its adjoint (i.e. $(Tx, y) = (x, T^*y)$ for all $x, y \in H$), and $R(T)$, $N(T)$ its range and nullspace, respectively.

(a) Show that $N(T^*) = R(T)^\perp$ and $\overline{R(T^*)} = N(T)^\perp$.

(b) Show that $R(T^*)$ is closed if $R(T)$ is closed.

Hint for (b): Show that, for every $y \in N(T)^\perp$, there is a bounded linear functional $\Lambda : R(T) \to \mathbb{C}$ with the property that $\Lambda(Tx) = (x, y)$.
Use this to show that $N(T)^\perp \subset R(T^*)$.
:::

::: {.solution}
**(a).**

<1>1. $N(T^*)=\{y: T^*y=0\}$.
::: {.proof}
definition.
:::

<1>2. $y\in N(T^*)$ iff $(Tx,y)=0$ for all $x$, i.e. $y\perp R(T)$.
::: {.proof}
$(Tx,y)=(x,T^*y)$.
:::

<1>3. Hence $N(T^*)=R(T)^\perp$.
::: {.proof}
<1>2.
:::

<1>4. $N(T)=R(T^*)^\perp$, so $N(T)^\perp = \overline{R(T^*)}^{\perp\perp}= \overline{R(T^*)}$.
::: {.proof}
take orthogonals of <1>3 with $T$ replaced by $T^*$ and double orthogonal is closure.
:::

**(b).**

<1>1. Assume $R(T)$ closed.
::: {.proof}
hypothesis.
:::

<1>2. For $y\in N(T)^\perp =\overline{R(T^*)}$, define $\Lambda: R(T)\to\mathbb{C}$ by $\Lambda(Tx)=(x,y)$.
::: {.proof}
well-defined because if $Tx_1=Tx_2$ then $x_1-x_2\in N(T)\perp y$.
:::

<1>3. $\Lambda$ is bounded: $|\Lambda(Tx)|\le \|y\|\|P_{N(T)^\perp}x\|\le C\|Tx\|$ (closed range gives $c\|P_{N(T)^\perp}x\|\le\|Tx\|$).
::: {.proof}
closed range estimate.
:::

<1>4. Extend $\Lambda$ by Hahn–Banach and Riesz to $z$ with $(Tx,z)=\Lambda(Tx)=(x,y)$, so $y=T^*z$.
::: {.proof}
Riesz representation.
:::

<1>5. Hence $N(T)^\perp\subset R(T^*)$, so $R(T^*)=N(T)^\perp$ is closed.
::: {.proof}
<1>4 and <1>4(a) ($\overline{R(T^*)}\subset R(T^*)$).
:::

<1>6. Q.E.D.
::: {.proof}
<1>3 and <1>5.
:::
:::
