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
<1>1. Let
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

::: {.proof}
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

<1>2. The map $m_x$ is injective.

::: {.proof}
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

<1>3. The map $m_x$ is surjective.

::: {.proof}
The domain and codomain are the same finite-dimensional vector space.
Every injective linear endomorphism of a finite-dimensional vector space
is surjective. Apply step <1>2.
:::

<1>4. The element $x$ has a multiplicative inverse in $R$.

::: {.proof}
By step <1>3, the element
$$
1\in R
$$
lies in the image of $m_x$. Thus there is some $y\in R$ such that
$$
m_x(y)=xy=1.
$$
Since $R$ is commutative, this $y$ is the inverse of $x$.
:::

<1>5. Every nonzero element of $R$ is invertible, so
$$
\boxed{R\text{ is a field}}.
$$

::: {.proof}
The element $x\neq0$ in step <1>1 was arbitrary. Step <1>4 therefore
shows that every nonzero element of $R$ has an inverse in $R$.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 is the required conclusion.
:::
:::
