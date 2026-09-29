---
schema: qual/card@1
id: P-BKS13-9A
kind: problem
title: Finite-dimensional domains over a field are fields
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-25
  note: Compared the authored statement with page 3 of the retained Spring 2013 solution PDF and independently reviewed the multiplication-map argument.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked K-linearity, injectivity from the domain hypothesis, and surjectivity in finite dimension.
---

::: {.problem}
Let K be a field. Let R be an integral domain which contains K and is finite-dimensional (as a vector space) over K. Prove that R is a field.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Let
$$
x\in R,
\qquad
x\neq0.
$$
The map
$$
m_x:R\longrightarrow R,
\qquad
m_x(r)=xr,
$$
is $K$-linear.

::: pf-proof

For $r,s\in R$ and $a,b\in K$,
$$
\begin{aligned}
m_x(ar+bs)
&=
x(ar+bs)\\
&=
a(xr)+b(xs)\\
&=
am_x(r)+bm_x(s).
\end{aligned}
$$
Thus $m_x$ is a linear endomorphism of the finite-dimensional
$K$-vector space $R$.

:::

:::

::: {.pf-step #s2}

The map $m_x$ is injective.

::: pf-proof

If
$$
m_x(r)=0,
$$
then
$$
xr=0.
$$
Since $R$ is an integral domain and $x\neq0$, one must have
$$
r=0.
$$
Hence the kernel is trivial.

:::

:::

::: {.pf-step #s3}

The map $m_x$ is surjective.

::: pf-proof

The domain and codomain are the same finite-dimensional vector space.
Every injective linear endomorphism of a finite-dimensional vector space
is surjective. Apply step [](#s2){.pf-ref}.

:::

:::

::: {.pf-step #s4}

The element $x$ has a multiplicative inverse in $R$.

::: pf-proof

By step [](#s3){.pf-ref}, the element
$$
1\in R
$$
lies in the image of $m_x$. Thus there is some $y\in R$ such that
$$
m_x(y)=xy=1.
$$
Since $R$ is commutative, this $y$ is the inverse of $x$.

:::

:::

::: {.pf-step #s5}

Every nonzero element of $R$ is invertible, so
$$
\boxed{R\text{ is a field}}.
$$

::: pf-proof

The element $x\neq0$ in step [](#s1){.pf-ref} was arbitrary. Step [](#s4){.pf-ref} therefore
shows that every nonzero element of $R$ has an inverse in $R$.

:::

:::

::: pf-qed

Step [](#s5){.pf-ref} is the required conclusion.

:::

:::

:::
