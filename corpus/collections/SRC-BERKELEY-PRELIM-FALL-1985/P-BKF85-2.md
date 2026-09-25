---
schema: qual/card@1
id: P-BKF85-2
kind: problem
title: A unique real root of $ze^{\lambda-z}=1$ in the unit disk
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 2 in the deterministic MinerU Flash extraction assets/attachments/Fall85_extracted.md.
---

::: {.problem}
Prove that for every $\lambda>1$, the equation
\[
ze^{\lambda-z}=1
\]
has exactly one root in the disk $|z|<1$, and that this root is real.
:::

::: {.solution}
Define
$$
G(z)\coloneqq z-e^{z-\lambda}.
$$
The equation in the problem is equivalent to $G(z)=0$.

<1>1. The function $G$ has exactly one zero in the disk $\abs{z}<1$, counted with multiplicity.

::: {.proof}
On the circle $\abs{z}=1$,
$$
\abs{e^{z-\lambda}}
=
e^{\operatorname{Re}z-\lambda}
\leq
e^{1-\lambda}
<1
=
\abs{z},
$$
because $\lambda>1$. Hence, by Rouché's theorem, the functions
$$
z
\qquad\text{and}\qquad
z-e^{z-\lambda}=G(z)
$$
have the same number of zeros in $\abs{z}<1$, counted with multiplicity. The function $z$ has exactly one such zero, namely $0$ with multiplicity one. Therefore $G$ also has exactly one zero in the disk.
:::

<1>2. The equation $G(x)=0$ has a real solution $x\in(0,1)$.

::: {.proof}
For real $x$,
$$
G(x)=x-e^{x-\lambda}
$$
is continuous. Moreover,
$$
G(0)=-e^{-\lambda}<0
$$
and
$$
G(1)=1-e^{1-\lambda}>0,
$$
since $\lambda>1$. The intermediate value theorem therefore gives some $x\in(0,1)$ with $G(x)=0$.
:::

<1>3. The equation
$$
ze^{\lambda-z}=1
$$
has exactly one root in $\abs{z}<1$, and that root is real.

::: {.proof}
The equations
$$
ze^{\lambda-z}=1
\qquad\Longleftrightarrow\qquad
z=e^{z-\lambda}
\qquad\Longleftrightarrow\qquad
G(z)=0
$$
are equivalent. Step <1>1 gives exactly one zero of $G$ in the disk, while step <1>2 exhibits a real zero there. Hence the unique root is real.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 is the required conclusion.
:::
:::
