---
schema: qual/card@1
id: P-BKS05-3A
kind: problem
title: The punctured disk is not biholomorphic to an annulus
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against fresh deterministic MinerU Flash extractions of the UC Berkeley Spring 2005 exam and its companion solution packet; unambiguous duplicated-statement extraction defects were normalized.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: >-
    Independently checked and completed the retained removable-singularity
    argument: the extended value lies strictly inside the annulus by the
    maximum-modulus principle for F and 1/F, and openness then contradicts
    injectivity on the punctured disk.
---

::: {.problem}
Prove that there is no holomorphic bijection from the punctured disk $0 < | z | < 1$ in $\mathbb { C }$ onto the annulus $r < | z | < R$ , where $0 < r < R < \infty$
:::

::: {.solution}
Let
$$
D\coloneqq\{z\in\CC:|z|<1\},
\qquad
A\coloneqq\{w\in\CC:r<|w|<R\}.
$$
Suppose for contradiction that
$$
f:D\setminus\{0\}\longrightarrow A
$$
is a holomorphic bijection.

::: pf

::: pf-step

The function $f$ extends to a holomorphic function
$$
F:D\longrightarrow\CC.
$$

::: pf-proof

Since $f(D\setminus\{0\})\subseteq A$, one has
$$
|f(z)|<R
$$
for every $0<|z|<1$. Thus $f$ is bounded near $0$, so the removable
singularity theorem gives a holomorphic extension $F$ across $0$.

:::

:::

::: {.pf-step #s2}

The extended value satisfies
$$
r<|F(0)|<R.
$$

::: pf-proof

Continuity at $0$ and
$$
r<|F(z)|<R
$$
for $z\neq0$ give
$$
r\leq|F(0)|\leq R.
$$
The function $F$ is nonconstant because its restriction $f$ is
surjective onto the nontrivial annulus $A$.

If $|F(0)|=R$, then $|F|$ attains its maximum at the interior point
$0$, so the maximum-modulus principle makes $F$ constant, a
contradiction.

Also $F$ has no zero on $D$: it has none on $D\setminus\{0\}$ because
$|f|>r>0$, and $|F(0)|\geq r>0$. Hence $1/F$ is holomorphic on $D$.
If $|F(0)|=r$, then
$$
\left|\frac1{F(z)}\right|\leq\frac1r
$$
on $D$, with equality at $0$. The maximum-modulus principle would make
$1/F$, and therefore $F$, constant. Thus both inequalities are strict.

:::

:::

::: pf-step

There is $z_0\in D\setminus\{0\}$ such that
$$
F(z_0)=F(0).
$$

::: pf-proof

By step [](#s2){.pf-ref}, the point $F(0)$ belongs to $A$. Since the original map
$f:D\setminus\{0\}\to A$ is surjective, some
$z_0\in D\setminus\{0\}$ satisfies
$$
f(z_0)=F(0).
$$
Because $F=f$ away from $0$, this is the stated equality.

:::

:::

::: {.pf-step #s4}

The restriction of $F$ to $D\setminus\{0\}$ is not injective.

::: pf-proof

Choose disjoint open neighborhoods $U$ of $0$ and $V$ of $z_0$ whose
closures lie in $D$. The nonconstant holomorphic function $F$ cannot
be constant on either neighborhood, so the open mapping theorem shows
that $F(U)$ and $F(V)$ are open neighborhoods of the common value
$$
p\coloneqq F(0)=F(z_0).
$$
Their intersection therefore contains a point $q\neq p$. Choose
$u\in U$ and $v\in V$ with
$$
F(u)=q=F(v).
$$
Since $q\neq F(0)$, one has $u\neq0$. Also $v\neq0$ because
$0\notin V$. Thus $u,v\in D\setminus\{0\}$, and they are distinct
because $U\cap V=\varnothing$. Hence $f(u)=f(v)$ with $u\neq v$.

:::

:::

::: {.pf-step #s5}

No holomorphic bijection from the punctured disk onto $A$ exists.

::: pf-proof

Step [](#s4){.pf-ref} contradicts the assumed injectivity of $f$.

:::

:::

::: pf-qed

Step [](#s5){.pf-ref} proves the required assertion.

:::

:::

:::
