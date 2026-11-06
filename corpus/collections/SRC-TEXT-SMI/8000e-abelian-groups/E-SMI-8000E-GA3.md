---
schema: qual/card@1
id: E-SMI-8000E-GA3
kind: problem
title: An extension of $\ZZ$ by $\ZZ^s$ is free of rank $s+1$
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
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against the printed problem, Smith Math 8000 packet 8000e.pdf page 1,
    abelian-groups (generators) problem 3: "prove if 0-->Z^s-->K-->Z-->0 is an
    exact sequence, then there is a linearly independent generating set
    consisting of s+1 elements for K, and hence K is isomorphic to Z^(s+1)." The
    card states exactly this. The proof was checked: t with p(t) = 1 exists by
    surjectivity; for x in K the element x - p(x)t lies in ker p = im i, so the
    images of the standard basis together with t generate; and a relation
    sum a_j i(e_j) + n t = 0 gives n = 0 after applying p and then all a_j = 0 by
    injectivity of i together with independence of the e_j. A linearly independent
    generating set of s + 1 elements is a basis, so K ≅ Z^{s+1}. Complete; no
    defect.
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
0\longrightarrow \ZZ^s\xrightarrow{i}K\xrightarrow{p}\ZZ\longrightarrow0.
$$
Let $e_1,\ldots,e_s$ be the standard basis of $\ZZ^s$. Since $p$ is
surjective, choose $t\in K$ with
$$
p(t)=1.
$$

::: pf

::: pf-step

The elements $i(e_1),\ldots,i(e_s),t$ generate $K$.

::: pf-proof

Let $x\in K$. Put
$$
n=p(x)\in\ZZ.
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
z=\sum_{j=1}^s a_j e_j\in\ZZ^s
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

:::

::: pf-step

These $s+1$ generators are linearly independent over $\ZZ$.

::: pf-proof

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
Exactness at $\ZZ^s$ says that $i$ is injective, so
$$
\sum_{j=1}^s a_j e_j=0.
$$
The standard basis is independent, hence every $a_j=0$. Thus the $s+1$
generators are independent.

:::

:::

::: pf-step

Conclude the isomorphism type of $K$.

::: pf-proof

A linearly independent generating set of $s+1$ elements is a basis of the
abelian group $K$. Therefore
$$
\boxed{K\cong\ZZ^{s+1}.}
$$

:::

:::

:::

:::
