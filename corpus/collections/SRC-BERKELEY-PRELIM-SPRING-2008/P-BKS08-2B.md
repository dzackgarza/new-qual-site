---
schema: qual/card@1
id: P-BKS08-2B
kind: problem
title: Products of elements in finite abelian groups and finite fields
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored UC Berkeley Spring 2008 preliminary-exam solution packet, which reproduces the problem statement with its solution.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked inverse-pair cancellation in the finite abelian
    group and the self-inverse elements of a finite field, including
    characteristic two.
---

::: {.problem}
(a) Let $G$ be a finite abelian group, and let $c$ be the product of all elements of $G$. Show that $c^2=1$.

(b) Let $F$ be a finite field, and let $c$ be the product of all nonzero elements of $F$. Show that $c=-1$.
:::

::: {.solution}

::: pf

::: {.pf-step #pairs-cancel}
Let
$$
Z\coloneqq\{g\in G:g\ne g^{-1}\}.
$$
Then
$$
\prod_{g\in Z}g=1.
$$

::: pf-proof
The map $g\mapsto g^{-1}$ partitions $Z$ into disjoint two-element
sets $\{g,g^{-1}\}$. Since $G$ is abelian, the product may be
rearranged into these pairs, each of which has product $1$.
:::

:::

::: {.pf-step #product-formula}
For the product $c$ of all elements of $G$,
$$
c=\prod_{\substack{g\in G\\g^2=1}}g.
$$

::: pf-proof
The elements outside $Z$ are exactly those satisfying $g=g^{-1}$, or
equivalently $g^2=1$. Step [](#pairs-cancel){.pf-ref} shows that the product of all elements
in $Z$ is $1$, leaving only the displayed product.
:::

:::

::: {.pf-step #abelian-square-identity}
In part (a),
$$
\boxed{c^2=1}.
$$

::: pf-proof
By step [](#product-formula){.pf-ref} and commutativity,
$$
c^2
=
\prod_{\substack{g\in G\\g^2=1}}g^2
=1.
$$
:::

:::

::: pf-step
In the multiplicative group $F^\times$, the self-inverse
elements are precisely the nonzero roots of
$$
x^2-1=(x-1)(x+1).
$$

::: pf-proof
An element $x\in F^\times$ is self-inverse exactly when $x^2=1$.
Because $F$ is a field,
$$
(x-1)(x+1)=0
$$
implies $x=1$ or $x=-1$. Conversely, both $1$ and $-1$ satisfy
$x^2=1$.
:::

:::

::: {.pf-step #field-product-value}
In part (b),
$$
\boxed{c=-1}.
$$

::: pf-proof
Apply step [](#product-formula){.pf-ref} to the finite abelian group $F^\times$. If
$\operatorname{char}F\ne2$, the self-inverse elements are the two
distinct elements $1$ and $-1$, so their product is $-1$. If
$\operatorname{char}F=2$, then $1=-1$, and the only self-inverse
element is $1$, whose product is again $1=-1$. Thus in every
characteristic, $c=-1$.
:::

:::

::: pf-qed
Steps [](#abelian-square-identity){.pf-ref} and [](#field-product-value){.pf-ref} prove parts (a) and (b), respectively.
:::

:::

:::
