---
schema: qual/card@1
id: P-BKS05-5B
kind: problem
title: Fixed field of $x\mapsto x^{-1}$ on $\QQ(x)$
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
    Independently checked the retained degree-two argument: y=x+x^{-1} is
    fixed, x satisfies T^2-yT+1, and x is not in Q(y), so the fixed
    intermediate field cannot be larger than Q(y).
---

::: {.problem}
Let $\mathbb { Q } ( x )$ be the field of rational functions in one variable over $\mathbb { Q }$ . Let $i \colon \mathbb { Q } ( x ) \to \mathbb { Q } ( x )$ be the unique field automorphism such that $i ( x ) = x ^ { - 1 }$ Prove that the fixed subfield $\{ r \in \mathbb { Q } ( x ) : i ( r ) = r \}$ is equal to $\mathbb { Q } ( x + x ^ { - 1 } )$
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

::: pf

::: {.pf-step #qy-in-fixed-field}
One has
$$
\QQ(y)\subseteq F.
$$

::: pf-proof
The automorphism fixes every element of $\QQ$, and
$$
i(y)
=
i(x)+i(x)^{-1}
=
x^{-1}+x
=y.
$$
Therefore it fixes every rational function in $y$ with rational
coefficients.
:::

:::

::: {.pf-step #degree-two}
The extension
$$
K/\QQ(y)
$$
has degree $2$.

::: pf-proof
The element $x$ satisfies
$$
x^2-yx+1=0,
$$
so
$$
[K:\QQ(y)]\leq2.
$$
It cannot have degree $1$. Indeed, if $x\in\QQ(y)$, then step [](#qy-in-fixed-field){.pf-ref}
would imply that $i(x)=x$. But
$$
i(x)=x^{-1}\neq x
$$
as elements of the rational function field $\QQ(x)$. Hence
$x\notin\QQ(y)$ and the degree is exactly $2$.
:::

:::

::: {.pf-step #fixed-field-proper}
The fixed field $F$ is a proper subfield of $K$.

::: pf-proof
The element $x$ is not fixed by $i$, since
$$
i(x)=x^{-1}\neq x.
$$
Thus $x\notin F$, so $F\neq K$.
:::

:::

::: {.pf-step #fixed-field-equals-qy}
One has
$$
F=\QQ(y)=\QQ(x+x^{-1}).
$$

::: pf-proof
By step [](#qy-in-fixed-field){.pf-ref},
$$
\QQ(y)\subseteq F\subseteq K.
$$
Step [](#degree-two){.pf-ref} gives
$$
[K:\QQ(y)]=2.
$$
The tower formula therefore gives
$$
2=[K:F][F:\QQ(y)].
$$
By step [](#fixed-field-proper){.pf-ref}, $F\neq K$, so $[K:F]>1$. Hence
$$
[K:F]=2
\qquad\text{and}\qquad
[F:\QQ(y)]=1.
$$
Thus $F=\QQ(y)$.
:::

:::

::: pf-qed
Step [](#fixed-field-equals-qy){.pf-ref} is the required description of the fixed subfield.
:::

:::

:::
