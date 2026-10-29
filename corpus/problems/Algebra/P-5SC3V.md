---
schema: qual/card@1
id: P-5SC3V
kind: problem
title: A PID that is not Euclidean
classification:
  areas:
  - algebra
  topics:
  - Principal Ideal Domains
  - Euclidean Domains
  - Counterexamples
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
Do you know a Principal Ideal Domain (PID) that is not a Euclidean Domain?
:::

::: {.solution}
Let $\theta=\frac{1+\sqrt{-19}}2$ and $R=\ZZ[\theta]$, the ring of integers of $\QQ(\sqrt{-19})$. Its norm is
$$
N(x+y\theta)=x^2+xy+5y^2=\left(x+\frac y2\right)^2+\frac{19}{4}y^2 .
$$

::: pf

::: pf-step
$\boxed{R=\ZZ\left[\frac{1+\sqrt{-19}}2\right]}$ is a PID.

::: pf-proof
The discriminant of $R$ is $-19$, so the Minkowski bound for this imaginary quadratic field is $\frac{2}{\pi}\sqrt{19}<3$, and every ideal class contains an integral ideal of norm $1$ or $2$. The prime $2$ is inert, because the minimal polynomial $x^2-x+5$ of $\theta$ reduces to $x^2+x+1$, which has no root in $\FF_2$. Hence no ideal has norm $2$, every ideal class contains the unit ideal, and the class group is trivial.
:::

:::

::: {.pf-step #side-divisor}
If a Euclidean domain $D$ is not a field, it has a nonzero nonunit $\beta$ such that every class of $D/(\beta)$ is represented by $0$ or by a unit.

::: pf-proof
Let $\delta$ be a Euclidean function and choose a nonzero nonunit $\beta$ with $\delta(\beta)$ minimal. For every $a\in D$, division gives $a=q\beta+r$ with $r=0$ or $\delta(r)<\delta(\beta)$. By minimality, a nonzero remainder $r$ is a unit.
:::

:::

::: {.pf-step #small-norms}
No element of $R$ has norm $2$ or $3$.

::: pf-proof
If $y\ne0$, then $N(x+y\theta)\ge\frac{19}{4}>3$. If $y=0$, then $N(x)=x^2$, which is not $2$ or $3$.
:::

:::

::: pf-step
$R$ is not a Euclidean domain.

::: pf-proof
The units of $R$ are $\pm1$, because $N(u)=1$ forces $y=0$ and $x=\pm1$. If $R$ were Euclidean, step [](#side-divisor){.pf-ref} would give a nonzero nonunit $\beta$ such that $R/(\beta)$ has at most the three classes of $0,1,-1$. Since $\abs{R/(\beta)}=N(\beta)>1$, this gives $N(\beta)\in\{2,3\}$, which step [](#small-norms){.pf-ref} excludes.
:::

:::

:::

:::
