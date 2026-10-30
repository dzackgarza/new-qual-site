---
schema: qual/card@1
id: P-NORI-GT-3-06
kind: problem
title: Image of $x\mapsto x-x^p$ on $\FF_q$
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
Let $\FF _ { q }$ be a finite field of characteristic $p .$ How mny elements of $\FF _ { q }$ are of the type $x - x ^ { \bar { p } } , x \in \FF _ { q } ?$
:::

::: {.solution}

Interpret the extraction artifact $x^{\bar p}$ as $x^p$.

::: pf

::: pf-step

Define
$$
T:\FF_q\to\FF_q,
\qquad
T(x)=x-x^p.
$$
Then $T$ is linear over $\FF_p$.


::: pf-proof

For $x,y\in\FF_q$, the Frobenius identity in characteristic $p$ gives
$$
(x+y)^p=x^p+y^p,
$$
so $T(x+y)=T(x)+T(y)$. For $c\in\FF_p$, one has $c^p=c$, hence
$$
T(cx)=cx-c^px^p=c(x-x^p)=cT(x).
$$

:::

:::

::: pf-step

Its kernel is
$$
\ker T=\FF_p.
$$


::: pf-proof

One has
$$
T(x)=0
\iff x^p=x.
$$
The roots of $X^p-X$ in any field of characteristic $p$ are exactly the elements of its prime subfield $\FF_p$: all $p$ elements of $\FF_p$ are roots, and the polynomial has degree $p$. Thus the kernel is $\FF_p$.

:::

:::

::: {.pf-step #s1-3}

Hence
$$
\cardinality{\ker T}=p.
$$


::: pf-proof

The prime field $\FF_p$ has exactly $p$ elements.

:::

:::

::: {.pf-step #s1-4}

Every fiber of $T$ has either zero elements or exactly $p$ elements.


::: pf-proof

If $T(x)=y$ and $T(x')=y$, then
$$
T(x-x')=0,
$$
so $x-x'\in\ker T$. Conversely, if $c\in\ker T$, then
$$
T(x+c)=T(x)+T(c)=y.
$$
Thus every nonempty fiber is a coset of $\ker T$ and has $p$ elements by step [](#s1-3){.pf-ref}.

:::

:::

::: {.pf-step #s1-5}

Therefore
$$
\cardinality{\operatorname{im}T}=\frac qp.
$$


::: pf-proof

The $q$ elements of the domain are partitioned into the nonempty fibers over the image. Step [](#s1-4){.pf-ref} says every such fiber has exactly $p$ elements. Hence the number of fibers, equivalently the number of image elements, is $q/p$.

:::

:::

::: {.pf-step #s1-6}

Thus the number of elements of $\FF_q$ of the form
$$
x-x^p
$$
is
$$
\boxed{q/p}.
$$


::: pf-proof

These elements are precisely the image of $T$, whose cardinality was computed in step [](#s1-5){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} is the requested count.

:::

:::

:::
