---
schema: qual/card@1
id: P-LARQ10
kind: problem
title: The second isomorphism theorem for rings
classification:
  areas: [algebra]
  topics: [Ring Theory]
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared all four parts of the second-isomorphism-theorem exercise with Lerman practice problem 10."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked additive and multiplicative closure of A+I, both-sided ideal closure where relevant, and the kernel and surjectivity of the canonical quotient map."
---

::: {.problem}
Let $A$ be a subring of a ring $R$, and let $I$ be an ideal of $R$.
Prove that:

1. $A+I=\{a+i:a\in A,\ i\in I\}$ is a subring of $R$.

2. $A\cap I$ is an ideal of $A$.

3. $I$ is an ideal of $A+I$.

4. $(A+I)/I\cong A/(A\cap I)$.
:::

::: {.solution}
<1>1. The set $A+I$ is a subring of $R$.
::: {.proof}
It is nonempty because $0=0+0\in A+I$. If $a+i,b+j\in A+I$, then
$$
(a+i)-(b+j)=(a-b)+(i-j)\in A+I
$$
because $A$ is a subring and $I$ is an additive subgroup. Also
$$
(a+i)(b+j)=ab+(aj+ib+ij).
$$
Here $ab\in A$, while $aj,ib,ij\in I$ because $I$ is a two-sided ideal of $R$. Hence the product lies in $A+I$. Thus $A+I$ is a subring.
:::

<1>2. The intersection $A\cap I$ is an ideal of $A$.
::: {.proof}
The intersection is an additive subgroup of $A$. If $a\in A$ and $x\in A\cap I$, then $ax,xa\in A$ because $A$ is a subring, and $ax,xa\in I$ because $I$ is an ideal of $R$. Therefore
$$
ax,xa\in A\cap I,
$$
so $A\cap I$ is an ideal of $A$.
:::

<1>3. The set $I$ is an ideal of $A+I$.
::: {.proof}
Certainly $I\subset A+I$, since $i=0+i$. It is already an additive subgroup. If $r=a+j\in A+I$ and $i\in I$, then
$$
ri=ai+ji\in I,
\qquad
ir=ia+ij\in I,
$$
again because $I$ is a two-sided ideal of $R$. Hence $I\triangleleft A+I$.
:::

<1>4. The canonical map gives the quotient isomorphism.
::: {.proof}
Define
$$
\Phi:A\to(A+I)/I,
\qquad
\Phi(a)=a+I.
$$
This is a ring homomorphism. It is surjective because every class in $(A+I)/I$ has a representative $a+i$, and
$$
(a+i)+I=a+I=\Phi(a).
$$
Its kernel is
$$
\ker\Phi=\{a\in A:a\in I\}=A\cap I.
$$
The first isomorphism theorem therefore yields
$$
A/(A\cap I)\cong(A+I)/I.
$$
Reversing the displayed sides gives the required form.
:::
:::
