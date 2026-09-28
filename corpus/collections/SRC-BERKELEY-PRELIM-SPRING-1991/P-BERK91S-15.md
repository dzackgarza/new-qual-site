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

<1>1. $a^G=G\setminus\{e\}$.

::: {.proof}
The identity is not conjugate to $a$, since $c^{-1}ac=e$ would imply
$a=e$. Conversely, the hypothesis says that every nonidentity element of
$G$ is conjugate to $a$. Thus the conjugacy class of $a$ consists exactly
of the nonidentity elements.
:::

<1>2. $|G|-1$ divides $|G|$.

::: {.proof}
Under the conjugation action of $G$ on itself, the orbit of $a$ is $a^G$
and its stabilizer is the centralizer $C_G(a)$. Hence the
orbit-stabilizer theorem gives
$$
|a^G|=[G:C_G(a)].
$$
In particular, $|a^G|$ divides $|G|$. By step <1>1,
$|a^G|=|G|-1$, proving the claim.
:::

<1>3. $|G|=\boxed{2}$.

::: {.proof}
Put $n\coloneqq |G|$. Since $G$ is nontrivial, $n>1$. By step <1>2,
$n-1$ divides $n$, and therefore it divides
$$
n-(n-1)=1.
$$
The positive integer $n-1$ must therefore equal $1$, so $n=2$.
:::

<1>4. Q.E.D.

::: {.proof}
Step <1>3 proves the required order of $G$.
:::
:::
