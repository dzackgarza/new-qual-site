---
schema: qual/card@1
id: P-ALGQUAL18W-II3
kind: problem
title: Adjoints to the inclusion of integer and real posets
classification: {areas: [algebra], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Part II, Problem 3 in the deterministic MinerU Flash extraction assets/attachments/qual18wintersol_extracted.md.
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Independently derived both adjunctions from the defining Hom-set
    inequalities in the two poset categories, then compared them with the
    worked source solution. Ceiling gives the left adjoint and floor gives the
    right adjoint; naturality follows because all Hom-sets are empty or
    singletons.
---

::: {.problem}
For a partially ordered set $(X,\le)$, let $\mathcal C_X$ be the category whose objects are the elements of $X$ and with a unique morphism $x\to y$ exactly when $x\le y$.
For an order-preserving map $f:X\to Y$, let $F_f:\mathcal C_X\to\mathcal C_Y$ be the corresponding functor.

View $\mathbb Z$ and $\mathbb R$ with their usual orders, and let $i:\mathbb Z\hookrightarrow\mathbb R$ be the inclusion.
Find the left and right adjoints of
\[
F_i:\mathcal C_{\mathbb Z}\longrightarrow\mathcal C_{\mathbb R},
\]
and justify your answer carefully.
:::

::: {.solution}
Define order-preserving maps
$$
c:\RR\longrightarrow\ZZ,
\qquad
c(x)=\lceil x\rceil,
$$
and
$$
p:\RR\longrightarrow\ZZ,
\qquad
p(x)=\lfloor x\rfloor.
$$

<1>1. For every $x\in\RR$ and $n\in\ZZ$,
$$
\lceil x\rceil\leq n
\quad\Longleftrightarrow\quad
x\leq n.
$$

::: {.proof}
If $\lceil x\rceil\leq n$, then
$$
x\leq\lceil x\rceil\leq n.
$$
Conversely, if $x\leq n$ and $n$ is an integer, then $\lceil x\rceil$, the
least integer greater than or equal to $x$, satisfies
$$
\lceil x\rceil\leq n.
$$
:::

<1>2. The functor $F_c:\mathcal C_{\RR}\to\mathcal C_{\ZZ}$ is left
adjoint to $F_i$.

::: {.proof}
For $x\in\RR$ and $n\in\ZZ$,
$$
\Hom_{\mathcal C_{\ZZ}}(F_c x,n)\neq\varnothing
\quad\Longleftrightarrow\quad
\lceil x\rceil\leq n,
$$
whereas
$$
\Hom_{\mathcal C_{\RR}}(x,F_i n)\neq\varnothing
\quad\Longleftrightarrow\quad
x\leq n.
$$
These conditions are equivalent by step <1>1. Each Hom-set in a poset
category is either empty or a singleton, so there is a unique bijection
$$
\Hom_{\mathcal C_{\ZZ}}(F_c x,n)
\cong
\Hom_{\mathcal C_{\RR}}(x,F_i n).
$$
The bijections are natural in both variables because every map between such
Hom-sets is a map between sets of cardinality at most one, so every naturality
square commutes. Hence
$$
F_c\dashv F_i.
$$
:::

<1>3. For every $x\in\RR$ and $n\in\ZZ$,
$$
n\leq\lfloor x\rfloor
\quad\Longleftrightarrow\quad
n\leq x.
$$

::: {.proof}
If $n\leq\lfloor x\rfloor$, then
$$
n\leq\lfloor x\rfloor\leq x.
$$
Conversely, if $n\leq x$ and $n$ is an integer, then $\lfloor x\rfloor$,
the greatest integer less than or equal to $x$, satisfies
$$
n\leq\lfloor x\rfloor.
$$
:::

<1>4. The functor $F_p:\mathcal C_{\RR}\to\mathcal C_{\ZZ}$ is right
adjoint to $F_i$.

::: {.proof}
For $n\in\ZZ$ and $x\in\RR$,
$$
\Hom_{\mathcal C_{\RR}}(F_i n,x)\neq\varnothing
\quad\Longleftrightarrow\quad
n\leq x,
$$
whereas
$$
\Hom_{\mathcal C_{\ZZ}}(n,F_p x)\neq\varnothing
\quad\Longleftrightarrow\quad
n\leq\lfloor x\rfloor.
$$
Step <1>3 makes these conditions equivalent. As in step <1>2, the resulting
unique bijections
$$
\Hom_{\mathcal C_{\RR}}(F_i n,x)
\cong
\Hom_{\mathcal C_{\ZZ}}(n,F_p x)
$$
are automatically natural. Hence
$$
F_i\dashv F_p.
$$
:::

<1>5. The two adjoints are therefore
$$
\boxed{
F_{\lceil\,\cdot\,\rceil}
\dashv
F_i
\dashv
F_{\lfloor\,\cdot\,\rfloor}
}.
$$

::: {.proof}
This is exactly the combination of steps <1>2 and <1>4.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 identifies and justifies both requested adjoints.
:::
:::
