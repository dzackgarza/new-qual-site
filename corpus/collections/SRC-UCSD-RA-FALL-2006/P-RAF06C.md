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
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Problem 3 of the official UCSD Fall 2006 real-analysis qualifying exam.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Existing closed-range/Hahn-Banach proof reviewed as correct; normalized legacy solution/proof block syntax.
---

::: {.problem}
Let $H$ be a Hilbert space, $T : H \to H$ a bounded linear operator, $T^* : H \to H$ its adjoint (i.e. $(Tx, y) = (x, T^*y)$ for all $x, y \in H$), and $R(T)$, $N(T)$ its range and nullspace, respectively.

(a) Show that $N(T^*) = R(T)^\perp$ and $\overline{R(T^*)} = N(T)^\perp$.

(b) Show that $R(T^*)$ is closed if $R(T)$ is closed.

Hint for (b): Show that, for every $y \in N(T)^\perp$, there is a bounded linear functional $\Lambda : R(T) \to \mathbb{C}$ with the property that $\Lambda(Tx) = (x, y)$.
Use this to show that $N(T)^\perp \subset R(T^*)$.
:::

::: {.solution}
**(a).**

::: pf

::: pf-step
$N(T^*)=\{y: T^*y=0\}$.

::: pf-proof
definition.
:::

:::

::: {.pf-step #p1-s2}
$y\in N(T^*)$ iff $(Tx,y)=0$ for all $x$, i.e. $y\perp R(T)$.

::: pf-proof
$(Tx,y)=(x,T^*y)$.
:::

:::

::: {.pf-step #p1-s3}
Hence $N(T^*)=R(T)^\perp$.

::: pf-proof
step [](#p1-s2){.pf-ref}.
:::

:::

::: {.pf-step #p1-s4}
$N(T)=R(T^*)^\perp$, so $N(T)^\perp = \overline{R(T^*)}^{\perp\perp}= \overline{R(T^*)}$.

::: pf-proof
take orthogonals of step [](#p1-s3){.pf-ref} with $T$ replaced by $T^*$ and double orthogonal is closure.
:::

:::

:::

**(b).**

::: pf

::: pf-step
Assume $R(T)$ closed.

::: pf-proof
hypothesis.
:::

:::

::: pf-step
For $y\in N(T)^\perp =\overline{R(T^*)}$, define $\Lambda: R(T)\to\mathbb{C}$ by $\Lambda(Tx)=(x,y)$.

::: pf-proof
well-defined because if $Tx_1=Tx_2$ then $x_1-x_2\in N(T)\perp y$.
:::

:::

::: {.pf-step #p2-s3}
$\Lambda$ is bounded: $|\Lambda(Tx)|\le \|y\|\|P_{N(T)^\perp}x\|\le C\|Tx\|$ (closed range gives $c\|P_{N(T)^\perp}x\|\le\|Tx\|$).

::: pf-proof
closed range estimate.
:::

:::

::: {.pf-step #p2-s4}
Extend $\Lambda$ by Hahn–Banach and Riesz to $z$ with $(Tx,z)=\Lambda(Tx)=(x,y)$, so $y=T^*z$.

::: pf-proof
Riesz representation.
:::

:::

::: {.pf-step #p2-s5}
Hence $N(T)^\perp\subset R(T^*)$, so $R(T^*)=N(T)^\perp$ is closed.

::: pf-proof
step [](#p2-s4){.pf-ref} and step [](#p1-s4){.pf-ref}(a) ($\overline{R(T^*)}\subset R(T^*)$).
:::

:::

::: pf-qed
step [](#p2-s3){.pf-ref} and step [](#p2-s5){.pf-ref}.
:::

:::
:::
