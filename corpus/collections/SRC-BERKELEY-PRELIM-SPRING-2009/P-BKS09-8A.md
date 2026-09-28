---
schema: qual/card@1
id: P-BKS09-8A
kind: problem
title: Fixed field of $x\mapsto x^{-1}$ on $\mathbb Q(x)$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Restored the lost arrow in the automorphism i against s09solutions.pdf page 3 problem 8A.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked the degree-two fixed-field argument against the retained Spring 2009 source solution.
---

::: {.problem}
Let $\mathbb{Q}(x)$ be the field of rational functions of one variable over $\mathbb{Q}$. Let $i \colon \mathbb{Q}(x) \to \mathbb{Q}(x)$ be the unique field automorphism such that $i(x) = x^{-1}$. Prove that the subfield of elements fixed by $i$ is equal to $\mathbb{Q}(x + x^{-1})$.
:::

::: {.solution}
Set
$$
K\coloneqq\QQ(x),
\qquad
y\coloneqq x+x^{-1},
$$
and let
$$
F\coloneqq\{r\in K:i(r)=r\}
$$
be the fixed field.

<1>1. One has $\QQ(y)\subseteq F$.

::: {.proof}
Since $i$ fixes $\QQ$ pointwise and
$$
i(y)
=
i(x)+i(x)^{-1}
=
x^{-1}+x
=
y,
$$
the automorphism $i$ fixes every rational function in $y$ with coefficients
in $\QQ$.
:::

<1>2. One has
$$
[K:\QQ(y)]=2.
$$

::: {.proof}
The element $x$ satisfies
$$
x^2-yx+1=0,
$$
so $[K:\QQ(y)]\leq2$. If the degree were $1$, then
$x\in\QQ(y)$. Step <1>1 would then imply $i(x)=x$, but
$$
i(x)=x^{-1}\neq x
$$
in the rational function field $\QQ(x)$. Hence the degree is exactly $2$.
:::

<1>3. The fixed field $F$ is a proper subfield of $K$.

::: {.proof}
The element $x$ is not fixed by $i$, because $i(x)=x^{-1}\neq x$. Thus
$x\notin F$, so $F\neq K$.
:::

<1>4. The fixed field is
$$
\boxed{F=\QQ(x+x^{-1})}.
$$

::: {.proof}
By step <1>1,
$$
\QQ(y)\subseteq F\subseteq K.
$$
Step <1>2 and the tower formula give
$$
2
=
[K:\QQ(y)]
=
[K:F][F:\QQ(y)].
$$
Step <1>3 gives $[K:F]>1$. Therefore
$$
[K:F]=2,
\qquad
[F:\QQ(y)]=1,
$$
and hence $F=\QQ(y)=\QQ(x+x^{-1})$.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is the required description of the fixed subfield.
:::
:::
