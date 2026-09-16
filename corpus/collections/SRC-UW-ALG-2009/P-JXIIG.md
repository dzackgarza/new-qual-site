---
schema: qual/card@1
id: P-JXIIG
kind: problem
title: Quadratic extensions are $F(\sqrt{D})$ when $\operatorname{char} F\neq 2$,
  and $[F(\sqrt{D_1},\sqrt{D_2}):F]$
classification:
  areas:
  - algebra
  topics:
  - Field Extensions
  - Characteristic
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
---

::: {.problem}
Let $F$ be a field of characteristic not equal to 2.

- Prove that any extension $K$ of $F$ of degree 2 is of the form $F(\sqrt D)$ where $D\in F$ is not a square in $F$ and, conversely, that each such extension has degree 2 over $F$.

- Let $D_1,D_2\in F$ neither of which is a square in $F$.
  Prove that $[F(\sqrt{D_1},\sqrt{D_2}):F]=4$ if $D_1D_2$ is not a square in $F$ and is of degree 2 otherwise.
:::


::: {.solution}
<1>1. Let $K/F$ be an extension of degree $2$. Then $K=F(\sqrt D)$ for some nonsquare $D\in F$.
::: {.proof}
Choose $\alpha\in K\setminus F$. Since $[K:F]=2$, its minimal polynomial over $F$ has degree $2$, say
\[
m_\alpha(x)=x^2+bx+c.
\]
Because $\operatorname{char}F\ne2$, put
\[
\beta=\alpha+\frac b2.
\]
Then
\[
\beta^2=\alpha^2+b\alpha+\frac{b^2}{4}=\frac{b^2}{4}-c=:D\in F.
\]
Also $F(\beta)=F(\alpha)=K$. If $D$ were a square in $F$, then $\beta\in F$, hence $\alpha\in F$, contradiction. Thus $D$ is not a square and $K=F(\sqrt D)$.
:::

<1>2. Conversely, if $D\in F$ is not a square, then $[F(\sqrt D):F]=2$.
::: {.proof}
The polynomial $x^2-D$ has no root in $F$, so as a quadratic it is irreducible. Hence it is the minimal polynomial of $\sqrt D$ and the extension degree is $2$.
:::

<1>3. Let $D_1,D_2$ be nonsquares. Then
\[
[F(\sqrt{D_1},\sqrt{D_2}):F]
=[F(\sqrt{D_1},\sqrt{D_2}):F(\sqrt{D_1})]\cdot2.
\]
Thus the degree is $2$ or $4$ according as $\sqrt{D_2}$ does or does not lie in $F(\sqrt{D_1})$.
:::

<1>4. One has
\[
\sqrt{D_2}\in F(\sqrt{D_1})
\quad\Longleftrightarrow\quad
D_1D_2\text{ is a square in }F.
\]
::: {.proof}
Suppose first that $\sqrt{D_2}=a+b\sqrt{D_1}$ with $a,b\in F$. Squaring gives
\[
D_2=a^2+b^2D_1+2ab\sqrt{D_1}.
\]
Since $1,\sqrt{D_1}$ are linearly independent over $F$, $2ab=0$. Because $\operatorname{char}F\ne2$, either $a=0$ or $b=0$. The case $b=0$ would make $D_2=a^2$ a square, impossible. Hence $a=0$, so $D_2=b^2D_1$ and therefore
\[
D_1D_2=(bD_1)^2
\]
is a square in $F$.

Conversely, suppose $D_1D_2=c^2$ for some $c\in F$. Since $D_1\ne0$,
\[
D_2=\frac{c^2}{D_1^2}D_1,
\]
so
\[
\sqrt{D_2}=\frac{c}{D_1}\sqrt{D_1}
\]
for a suitable choice of square root inside an algebraic closure. Hence $F(\sqrt{D_2})\subseteq F(\sqrt{D_1})$.
:::

<1>5. Therefore
\[
[F(\sqrt{D_1},\sqrt{D_2}):F]
=\begin{cases}
4,&D_1D_2\text{ is not a square in }F,\\
2,&D_1D_2\text{ is a square in }F.
\end{cases}
\]
::: {.proof}
Combine <1>3 and <1>4.
:::
