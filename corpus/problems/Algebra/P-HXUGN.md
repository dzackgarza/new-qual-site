---
schema: qual/card@1
id: P-HXUGN
kind: problem
title: Euclidean domains and PIDs
classification:
  areas:
  - algebra
  topics:
  - Euclidean Domains
  - Principal Ideal Domains
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: {.problem}
What is the relation between Euclidean domains and PIDs?
:::

::: {.solution}
Let $k$ be a field, and let $R=\ZZ[\theta]$ with $\theta=\frac{1+\sqrt{-19}}{2}$, the ring of integers of $\QQ(\sqrt{-19})$.
The norm on $R$ is
$$
N(a+c\theta)=a^2+ac+5c^2=\left(a+\frac c2\right)^2+\frac{19}{4}c^2\qquad(a,c\in\ZZ).
$$

::: pf

::: pf-step
Every Euclidean domain is a PID, and every PID is a UFD: $\boxed{\text{Euclidean domain}\Longrightarrow\text{PID}\Longrightarrow\text{UFD}}$, and neither implication reverses.

::: pf-proof

::: pf-step
Every Euclidean domain is a PID.

::: pf-proof
Let $R'$ be Euclidean with Euclidean function $\delta$, and let $0\ne I\triangleleft R'$. Choose $0\ne a\in I$ with $\delta(a)$ minimal. For $b\in I$, Euclidean division gives $b=qa+r$ with $r=0$ or $\delta(r)<\delta(a)$. Since $r=b-qa\in I$, minimality forces $r=0$. Hence $I=(a)$.
That a PID is a UFD is standard.
:::

:::

::: pf-step
$k[x,y]$ is a UFD and not a PID.

::: pf-proof
It is a UFD by Gauss's lemma. If $(x,y)=(d)$, then $d$ divides both $x$ and $y$, so $d$ is a unit, contradicting $(x,y)\ne k[x,y]$.
:::

:::

::: pf-step
$R$ is a PID.

::: pf-proof
The discriminant of $R$ is $-19$, so the Minkowski bound is $(2/\pi)\sqrt{19}<3$, and every ideal class contains an integral ideal of norm $1$ or $2$.
The polynomial $x^2-x+5$, the minimal polynomial of $\theta$, is irreducible modulo $2$, so $2$ is inert and no ideal has norm $2$.
Hence every ideal class is trivial.
:::

:::

::: pf-step
$R$ is not Euclidean for any Euclidean function.

::: pf-proof
Suppose $R$ is Euclidean, and choose a nonzero nonunit $b$ of minimal Euclidean value. Division by $b$ shows that every residue class modulo $(b)$ is represented by $0$ or a unit.
The units of $R$ are $\pm1$, since $N(a+c\theta)=1$ forces $c=0$ and $a=\pm1$. So $1<\abs{R/(b)}=N(b)\le3$.
But $N(a+c\theta)$ is $a^2\notin\{2,3\}$ when $c=0$ and at least $19/4>3$ when $c\ne0$, a contradiction.
:::

:::

:::

:::

:::

:::
