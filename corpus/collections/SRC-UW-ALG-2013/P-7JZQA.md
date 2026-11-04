---
schema: qual/card@1
id: P-7JZQA
kind: problem
title: The additive group of $\QQ$ has no maximal proper subgroups, and the same question for $\QQ^\times$
classification:
  areas:
  - algebra
  topics:
  - Abelian Groups
  - Subgroups
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-01
  note: >-
    Statement read from the card in `corpus/collections/SRC-UW-ALG-2013`; no correction is claimed.
- event: solution-written
  by: claude
  date: 2026-11-01
  note: >-
    (a) $\QQ$ is divisible and divisibility passes to quotients, so a quotient $\QQ/H$ is a divisible
    abelian group; a simple abelian group is $\ZZ/p$, which is not divisible, so no proper $H$ is
    maximal. (b) Yes: $\QQ^\times\cong\{\pm1\}\times\bigoplus_p\ZZ$, and the parity of the
    exponent of $2$ is a surjection onto $\ZZ/2$, whose kernel has index $2$ and is therefore maximal.
    Nothing is left in outline.
---

::: {.problem}
Let $\QQ^\times$ be the nonzero elements of $\QQ$, a group under multiplication.

(a) Prove that the additive group of $\QQ$ has no maximal proper subgroups.

(b) Is the same statement true for the multiplicative group $\QQ^\times$?
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

The additive group $\QQ$ is divisible: for $x\in\QQ$ and an integer $m\ge1$ there is $y\in\QQ$ with $my=x$. Divisibility passes to quotients.

::: pf-proof

Take $y=x/m$, an element of $\QQ$. If $\pi:G\to G/H$ is a quotient and $G$ is divisible, then for $\pi(x)\in G/H$ and $m$ choose $y$ with $my=x$; then $m\pi(y)=\pi(x)$, so $G/H$ is divisible.

:::

:::

::: {.pf-step #s2}

A simple abelian group is $\ZZ/p$ for some prime $p$.

::: pf-proof

Let $A\ne0$ be simple and take $0\ne a\in A$. The cyclic subgroup $\langle a\rangle$ is normal (the group is abelian) and nonzero, so it equals $A$; being simple and abelian, $A$ has no proper nontrivial subgroup, and a cyclic group with no proper nontrivial subgroup is $\ZZ/p$ for a prime $p$.

:::

:::

::: {.pf-step #s3}

Part (a): $\QQ$ has no maximal proper subgroup.

::: pf-proof

Suppose $H\subsetneq\QQ$ is maximal. Then $\QQ/H\ne0$ is simple, hence $\QQ/H\cong\ZZ/p$ by step [](#s2){.pf-ref}. By step [](#s1){.pf-ref} the group $\QQ/H$ is divisible, so for the element $\bar1\in\ZZ/p$ and the integer $p$ there is $\bar y$ with $p\bar y=\bar1$; but $p\bar y=\bar0$ in $\ZZ/p$. This contradiction shows that no such $H$ exists.

:::

:::

::: {.pf-step #s4}

Part (b): yes, $\QQ^\times$ does have maximal proper subgroups.

::: pf-proof

Every nonzero rational has a unique factorisation $q=\pm\prod_p p^{v_p(q)}$ with integers $v_p(q)$, all but finitely many zero, so
$$
\QQ^\times\cong\{\pm1\}\times\bigoplus_{p}\ZZ,
\qquad
q\longmapsto\Bigl(\operatorname{sgn}q,\ (v_p(q))_p\Bigr).
$$
The map $\varphi(q)=v_2(q) \bmod 2$ is a surjective homomorphism $\QQ^\times\to\ZZ/2$ (it is a homomorphism because $v_2$ is, and it is onto because $\varphi(2)=1$). Its kernel
$$
H=\{q\in\QQ^\times : v_2(q)\ \text{is even}\}
$$
has index $2$, and a subgroup of index $2$ is normal with quotient of order $2$, which is simple; so $H$ is a maximal proper subgroup of $\QQ^\times$.

So the answer to (b) is no, the statement is not true for $\QQ^\times$: unlike the additive group, the multiplicative group has maximal proper subgroups.

:::

:::

:::

:::
