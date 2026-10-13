---
schema: qual/card@1
id: P-NORI-GT-3-06
kind: problem
title: Image of $x\mapsto x-x^p$ on $\mathbb F_q$
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against problem 3.6 of the retained Nori Galois Theory Problems PDF.
---

::: {.problem}
Let $\mathbb { F } _ { q }$ be a finite field of characteristic $p .$ How mny elements of $\mathbb { F } _ { q }$ are of the type $x - x ^ { \bar { p } } , x \in \mathbb { F } _ { q } ?$
:::

::: {.solution}
Interpret the extraction artifact $x^{\bar p}$ as $x^p$.

<1>1. Define
\[
T:\mathbb F_q\to\mathbb F_q,
\qquad
T(x)=x-x^p.
\]
Then $T$ is linear over $\mathbb F_p$.

::: {.proof}
For $x,y\in\mathbb F_q$, the Frobenius identity in characteristic $p$ gives
\[
(x+y)^p=x^p+y^p,
\]
so $T(x+y)=T(x)+T(y)$. For $c\in\mathbb F_p$, one has $c^p=c$, hence
\[
T(cx)=cx-c^px^p=c(x-x^p)=cT(x).
\]
:::

<1>2. Its kernel is
\[
\ker T=\mathbb F_p.
\]

::: {.proof}
One has
\[
T(x)=0
\iff x^p=x.
\]
The roots of $X^p-X$ in any field of characteristic $p$ are exactly the elements of its prime subfield $\mathbb F_p$: all $p$ elements of $\mathbb F_p$ are roots, and the polynomial has degree $p$. Thus the kernel is $\mathbb F_p$.
:::

<1>3. Hence
\[
|\ker T|=p.
\]

::: {.proof}
The prime field $\mathbb F_p$ has exactly $p$ elements.
:::

<1>4. Every fiber of $T$ has either zero elements or exactly $p$ elements.

::: {.proof}
If $T(x)=y$ and $T(x')=y$, then
\[
T(x-x')=0,
\]
so $x-x'\in\ker T$. Conversely, if $c\in\ker T$, then
\[
T(x+c)=T(x)+T(c)=y.
\]
Thus every nonempty fiber is a coset of $\ker T$ and has $p$ elements by step <1>3.
:::

<1>5. Therefore
\[
|\operatorname{im}T|=\frac qp.
\]

::: {.proof}
The $q$ elements of the domain are partitioned into the nonempty fibers over the image. Step <1>4 says every such fiber has exactly $p$ elements. Hence the number of fibers, equivalently the number of image elements, is $q/p$.
:::

<1>6. Thus the number of elements of $\mathbb F_q$ of the form
\[
x-x^p
\]
is
\[
\boxed{q/p}.
\]

::: {.proof}
These elements are precisely the image of $T$, whose cardinality was computed in step <1>5.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>6 is the requested count.
:::
:::
