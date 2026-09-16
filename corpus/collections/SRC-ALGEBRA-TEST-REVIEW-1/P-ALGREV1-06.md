---
schema: qual/card@1
id: P-ALGREV1-06
kind: problem
title: The additive quotient by the center is not cyclic
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
  note: "Compared the card with Review1.md, open-ended question 6."
- event: solution-written
  by: chatgpt
  date: 2026-09-11
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-11
  note: "Showed a cyclic additive quotient would force every two ring elements to commute modulo central corrections, contradicting noncommutativity."
---

::: {.problem}
Let $R$ be a noncommutative ring and let $Z(R)$ be its center. Prove that the additive group of $R/Z(R)$ is not cyclic.
:::

::: {.solution}
Suppose for contradiction that the additive quotient $R/Z(R)$ is cyclic.

<1>1. Choose a representative of an additive generator.
::: {.proof}
There is some $a\in R$ such that
$$
R/Z(R)=\langle a+Z(R)\rangle.
$$
Thus for every $x\in R$ there are an integer $m$ and an element
$z\in Z(R)$ such that
$$
x=ma+z.
$$
:::

<1>2. Any two elements of $R$ then commute.
::: {.proof}
Take arbitrary $x,y\in R$. By step <1>1 write
$$
x=ma+z,
\qquad
y=na+w,
$$
with $m,n\in\mathbb Z$ and $z,w\in Z(R)$. Since $z$ and $w$ commute with
every element of $R$,
$$
\begin{aligned}
xy
&=(ma+z)(na+w)\\
&=mn a^2+maw+nza+zw,
\end{aligned}
$$
while
$$
\begin{aligned}
yx
&=(na+w)(ma+z)\\
&=mn a^2+naz+mwa+wz.
\end{aligned}
$$
Using $aw=wa$, $za=az$, and $zw=wz$, the two expressions are equal.
Hence $xy=yx$.
:::

<1>3. This contradicts the hypothesis that $R$ is noncommutative.
::: {.proof}
Step <1>2 shows that every pair of elements of $R$ commutes, so $R$ would be
commutative. Therefore the assumption that $R/Z(R)$ is cyclic is impossible:
$$
\boxed{(R/Z(R),+)\text{ is not cyclic}.}
$$
:::
:::
