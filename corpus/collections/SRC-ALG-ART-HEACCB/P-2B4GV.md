---
schema: qual/card@1
id: P-2B4GV
kind: problem
title: 'A basis for $N\subseteq\ZZ^3$ and the quotient $\ZZ^3/N$'
classification:
  areas:
  - algebra
  topics:
  - Structure Theorem
  - Smith Normal Form
  - Modules
relations: []
review: draft
audit:
- event: source-checked
  by: OpenAI
  date: 2026-09-09
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: problem
Consider the $\ZZ\dash$submodule $N$ of $\ZZ^3$ spanned by
\[
f_1 &= [-1, 0, 1], \\
f_2 &= [2,-3,1], \\
f_3 &= [0, 3, 1], \\
f_4 &= [3,1,5]
.\]
Find a basis for $N$ and describe $\ZZ^3/N$.
:::

::: {.solution}
<1>1. The standard basis vector $e_1=(1,0,0)$ belongs to $N$ because
\[
e_1=2f_1+6f_2+7f_3-3f_4.
\]
::: {.proof}
Direct substitution gives
\[
2(-1,0,1)+6(2,-3,1)+7(0,3,1)-3(3,1,5)=(1,0,0).
\]
:::

<1>2. The standard basis vector $e_2=(0,1,0)$ belongs to $N$ because
\[
e_2=-f_1-2f_2-2f_3+f_4.
\]
::: {.proof}
Direct substitution gives
\[
-(-1,0,1)-2(2,-3,1)-2(0,3,1)+(3,1,5)=(0,1,0).
\]
:::

<1>3. The standard basis vector $e_3=(0,0,1)$ belongs to $N$ because
\[
e_3=3f_1+6f_2+7f_3-3f_4.
\]
::: {.proof}
Direct substitution gives
\[
3(-1,0,1)+6(2,-3,1)+7(0,3,1)-3(3,1,5)=(0,0,1).
\]
:::

<1>4. Hence $N=\mathbb Z^3$.
::: {.proof}
By <1>1--<1>3, the standard basis of $\mathbb Z^3$ is contained in $N$, so $\mathbb Z^3\subseteq N$. The reverse inclusion is part of the definition of $N$.
:::

<1>5. Therefore one basis for $N$ is
\[
\{e_1,e_2,e_3\},
\]
and
\[
\mathbb Z^3/N=0.
\]
::: {.proof}
This follows immediately from <1>4.
:::
:::
