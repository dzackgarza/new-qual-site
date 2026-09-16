---
schema: qual/card@1
id: E-SMI-8000E-GA3
kind: problem
title: Kernels of maps onto Z are free abelian of rank one higher
classification:
  areas:
  - algebra
  topics:
  - Abelian Groups
  - Free Modules
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-11
  note: "Compared the exact-sequence statement with the local 8000e extraction, generators exercise 3."
- event: solution-written
  by: chatgpt
  date: 2026-09-11
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-11
  note: "Lifted 1 in Z, adjoined that lift to the injected standard basis of Z^s, and proved generation and independence by applying the quotient map."
---

::: {.exercise}
Prove that if

$$
0 \to \ZZ^s \to K \to \ZZ \to 0
$$

is an exact sequence, then there is a linearly independent generating set consisting of $s + 1$ elements for $K$, and hence $K$ is isomorphic to $\ZZ^{s+1}$.
:::


::: {.solution}
Write the exact sequence as
$$
0\longrightarrow \mathbb Z^s\xrightarrow{i}K\xrightarrow{p}\mathbb Z\longrightarrow0.
$$
Let $e_1,\ldots,e_s$ be the standard basis of $\mathbb Z^s$. Since $p$ is
surjective, choose $t\in K$ with
$$
p(t)=1.
$$

<1>1. The elements $i(e_1),\ldots,i(e_s),t$ generate $K$.
::: {.proof}
Let $x\in K$. Put
$$
n=p(x)\in\mathbb Z.
$$
Then
$$
p(x-nt)=p(x)-n p(t)=n-n=0,
$$
so
$$
x-nt\in\ker p.
$$
Exactness gives
$$
\ker p=\operatorname{im}i.
$$
Hence there is some
$$
z=\sum_{j=1}^s a_j e_j\in\mathbb Z^s
$$
with
$$
x-nt=i(z)=\sum_{j=1}^s a_j i(e_j).
$$
Therefore
$$
x=\sum_{j=1}^s a_j i(e_j)+nt,
$$
so the displayed $s+1$ elements generate $K$.
:::

<1>2. These $s+1$ generators are linearly independent over $\mathbb Z$.
::: {.proof}
Suppose
$$
\sum_{j=1}^s a_j i(e_j)+nt=0.
$$
Applying $p$ gives
$$
n=0,
$$
because $p(i(e_j))=0$ and $p(t)=1$. Thus
$$
i\left(\sum_{j=1}^s a_j e_j\right)=0.
$$
Exactness at $\mathbb Z^s$ says that $i$ is injective, so
$$
\sum_{j=1}^s a_j e_j=0.
$$
The standard basis is independent, hence every $a_j=0$. Thus the $s+1$
generators are independent.
:::

<1>3. Conclude the isomorphism type of $K$.
::: {.proof}
A linearly independent generating set of $s+1$ elements is a basis of the
abelian group $K$. Therefore
$$
\boxed{K\cong\mathbb Z^{s+1}.}
$$
:::
:::
