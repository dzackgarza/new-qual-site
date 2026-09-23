---
schema: qual/card@1
id: P-BERK91S-10
kind: problem
title: The additive group $\QQ$ is indecomposable as a direct sum
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: source-checked
  by: chatgpt
  date: 2026-09-23
  note: Compared the additive group of rational numbers and the exclusion of a direct sum of two nontrivial subgroups with Problem 10 in the retained MinerU Flash extraction of Spring91.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-23
---

::: {.problem}
Prove that the additive group $\QQ$ cannot be written as the direct sum of two nontrivial subgroups.
:::

::: {.hint}
Let $A$ and $B$ be nontrivial subgroups of $(\QQ,+)$, and choose
nonzero elements $a\in A$ and $b\in B$. Write $a/b=m/n$ with
nonzero integers $m,n$. The equality $na=mb$ gives a nonzero
element of $A\cap B$. An internal direct sum requires this
intersection to be $\{0\}$.
:::

::: {.solution}
Let $A$ and $B$ be nontrivial [[D-IQ4OX|subgroups]] of $(\QQ,+)$.

<1>1. The intersection $A\cap B$ contains a nonzero element.

::: {.proof}
Choose $a\in A\setminus\{0\}$ and $b\in B\setminus\{0\}$.
Since $a/b$ is a nonzero rational number, there are nonzero
integers $m,n$ such that $a/b=m/n$. Hence
$$
na=mb.
$$
A [[D-IQ4OX|subgroup]] of an additive group is closed under integer
multiples, so $na\in A$ and $mb\in B$. Their common value is
nonzero because $n\ne0$ and $a\ne0$. Thus $na=mb$ is a nonzero
element of $A\cap B$.
:::

<1>2. The group $(\QQ,+)$ is not the internal direct sum of
$A$ and $B$.

::: {.proof}
In an internal direct sum, every element has a unique expression
as the sum of an element of $A$ and an element of $B$.
For any $c\in A\cap B$, the expressions
$$
c=c+0=0+c
$$
would therefore force $c=0$. This contradicts step <1>1.
:::

<1>3. Q.E.D.

::: {.proof}
Step <1>2 excludes every pair of nontrivial [[D-IQ4OX|subgroups]] $A,B$.
An isomorphism from a direct sum of two nontrivial groups onto
$(\QQ,+)$ would send its summands to such an internal direct sum,
so no abstract direct-sum decomposition exists either.
:::
:::
