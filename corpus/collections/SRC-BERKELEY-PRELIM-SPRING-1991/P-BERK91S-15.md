---
schema: qual/card@1
id: P-BERK91S-15
kind: problem
title: If all nonidentity elements of a finite group are conjugate, the group has order two
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-23
---

::: {.problem}
Let $G$ be a finite nontrivial group such that any two nonidentity elements of $G$ are conjugate. Prove that
\[
|G|=2.
\]
:::

::: {.solution}
Fix a nonidentity element $a\in G$, and write $a^G$ for its conjugacy class.

::: pf

::: {.pf-step #s1}

$a^G=G\setminus\{e\}$.

::: pf-proof

The identity is not conjugate to $a$, since $c^{-1}ac=e$ would imply
$a=e$. Conversely, the hypothesis says that every nonidentity element of
$G$ is conjugate to $a$. Thus the conjugacy class of $a$ consists exactly
of the nonidentity elements.

:::

:::

::: {.pf-step #s2}

$|G|-1$ divides $|G|$.

::: pf-proof

Under the conjugation action of $G$ on itself, the orbit of $a$ is $a^G$
and its stabilizer is the centralizer $C_G(a)$. Hence the
orbit-stabilizer theorem gives
$$
|a^G|=[G:C_G(a)].
$$
In particular, $|a^G|$ divides $|G|$. By step [](#s1){.pf-ref},
$|a^G|=|G|-1$, proving the claim.

:::

:::

::: {.pf-step #s3}

$|G|=\boxed{2}$.

::: pf-proof

Put $n\coloneqq |G|$. Since $G$ is nontrivial, $n>1$. By step [](#s2){.pf-ref},
$n-1$ divides $n$, and therefore it divides
$$
n-(n-1)=1.
$$
The positive integer $n-1$ must therefore equal $1$, so $n=2$.

:::

:::

::: pf-qed

Step [](#s3){.pf-ref} proves the required order of $G$.

:::

:::

:::
