---
schema: qual/card@1
id: P-ALGREV1-05
kind: problem
title: The center of a ring is a subring
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-11
  note: "Compared the card with Review1.md, open-ended question 5."
- event: solution-written
  by: chatgpt
  date: 2026-09-11
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-11
  note: "Verified closure under subtraction and multiplication directly from commutation with every ring element."
---

::: {.problem}
Prove that the center of a ring is a subring.
:::

::: {.solution}
Let
$$
Z(R)=\{z\in R:zr=rz\text{ for every }r\in R\}
$$
be the center of the ring $R$.

<1>1. The center is nonempty and closed under subtraction.
::: {.proof}
The element $0$ commutes with every $r\in R$, so $0\in Z(R)$.

If $a,b\in Z(R)$ and $r\in R$, then
$$
\begin{aligned}
(a-b)r
&=ar-br\\
&=ra-rb\\
&=r(a-b).
\end{aligned}
$$
Thus $a-b\in Z(R)$.
:::

<1>2. The center is closed under multiplication.
::: {.proof}
If $a,b\in Z(R)$ and $r\in R$, then
$$
\begin{aligned}
(ab)r
&=a(br)\\
&=a(rb)\\
&=(ar)b\\
&=(ra)b\\
&=r(ab).
\end{aligned}
$$
Hence $ab\in Z(R)$.
:::

<1>3. Therefore $Z(R)$ is a subring of $R$.
::: {.proof}
By step <1>1, $Z(R)$ is an additive subgroup of $R$, and by step <1>2 it
is closed under multiplication. Therefore
$$
\boxed{Z(R)\le R\text{ as a subring}.}
$$
If $R$ has an identity and subrings are required to share it, then
$1r=r=r1$ for every $r$, so $1\in Z(R)$ as well.
:::
:::
