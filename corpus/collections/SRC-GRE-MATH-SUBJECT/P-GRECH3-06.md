---
schema: qual/card@1
id: P-GRECH3-06
kind: problem
title: External division point on a line
classification:
  areas:
  - real-analysis
  topics:
  - Lines and Planes
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Checked against Chapter 3 review Question 6 in both assets/attachments/extracted/chapter-3.md and the Mistral OCR extraction of the whole book, assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md, with the book's Chapter 8 solution where they disagree."
---

::: {.problem}
Let $P=(1,-1,1)$ and $Q=(-3,3,3)$. Find the point $R$ on the line containing $P$ and $Q$ whose distance from $P$ is $3$ times its distance from $Q$, given that $R$ is not between $P$ and $Q$.

(A) $\left(-4,4,\frac{7}{2}\right)$
(B) $(-5,5,4)$
(C) $\left(-\frac{13}{3},\frac{13}{3},\frac{11}{3}\right)$
(D) $\left(-\frac{15}{2},\frac{15}{2},\frac{11}{2}\right)$
(E) $(-9,9,6)$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Parametrize the line through $P$ and $Q$ by
$$
R(t)=P+t(Q-P)
=(1,-1,1)+t(-4,4,2).
$$


::: pf-proof

The direction vector is
$$
Q-P=(-3,3,3)-(1,-1,1)=(-4,4,2),
$$
which gives the displayed parametrization. Here $t=0$ gives $P$ and $t=1$ gives $Q$.

:::

:::

::: {.pf-step #s1-2}

The distance condition is equivalent to
$$
\abs{t}=3\abs{t-1}.
$$


::: pf-proof

By step [](#s1-1){.pf-ref},
$$
R(t)-P=t(Q-P),
$$
so
$$
\operatorname{dist}(R(t),P)=\abs{t}\norm{Q-P}.
$$
Also
$$
R(t)-Q=(t-1)(Q-P),
$$
so
$$
\operatorname{dist}(R(t),Q)=\abs{t-1}\norm{Q-P}.
$$
Since $P\ne Q$, the common factor $\norm{Q-P}$ is nonzero and cancels from the required relation
$\operatorname{dist}(R,P)=3\operatorname{dist}(R,Q)$.

:::

:::

::: pf-step

The solutions of the distance equation are
$$
t=\frac34
\qquad\text{and}\qquad
t=\frac32.
$$


::: pf-proof

Squaring the equation in step [](#s1-2){.pf-ref} gives
$$
t^2=9(t-1)^2,
$$
equivalently
$$
t=3(t-1)
\quad\text{or}\quad
t=-3(t-1).
$$
These equations yield $t=3/2$ and $t=3/4$, respectively.

:::

:::

::: {.pf-step #s1-4}

The condition that $R$ is not between $P$ and $Q$ forces
$$
t=\frac32.
$$


::: pf-proof

Points strictly between $P$ and $Q$ in the parametrization of step [](#s1-1){.pf-ref} are exactly those with $0<t<1$. Thus $t=3/4$ is excluded, while $t=3/2>1$ is admissible.

:::

:::

::: {.pf-step #s1-5}

Therefore
$$
\boxed{R=(-5,5,4)},
$$
so the answer is (B).


::: pf-proof

Substituting $t=3/2$ from step [](#s1-4){.pf-ref} into step [](#s1-1){.pf-ref} gives
$$
R
=(1,-1,1)+\frac32(-4,4,2)
=(-5,5,4).
$$

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} gives the requested point and corresponding choice.

:::

:::

:::
