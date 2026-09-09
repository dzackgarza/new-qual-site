---
schema: qual/card@1
id: P-ALGS06G
kind: problem
title: "Irreducibles and non-UFD structure in Z[sqrt(-n)] for squarefree n > 3"
classification:
  areas:
  - algebra
  topics:
  - Commutative Algebra
  - Number Theory
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
Let $n$ be a squarefree integer greater than 3. Let $R$ denote the subring $\mathbb{Z}[\sqrt{-n}] = \{a + b\sqrt{-n} \mid a, b \in \mathbb{Z}\}$ of the field of complex numbers $\mathbb{C}$.

(a) Show that $\sqrt{-n}$ and $1 + \sqrt{-n}$ are irreducible in $R$.

(b) Prove that $R$ is not a unique factorization domain (UFD).

(c) Construct an ideal in $R$ which is not principal.

Hint: In a UFD, an element is irreducible if and only if it is prime.
:::

::: {.solution}
<1>1. For $\alpha=a+b\sqrt{-n}\in R$, define
\[
N(\alpha)=\alpha\overline\alpha=a^2+nb^2.
\]
Then $N(\alpha\beta)=N(\alpha)N(\beta)$, and $α$ is a unit exactly when $N(\alpha)=1$.
::: {.proof}
The formula is the usual complex norm. It is multiplicative, takes nonnegative integer values, and $a^2+nb^2=1$ forces $b=0$ and $a=\pm1$ because $n>3$.
:::

<1>2. The element $\sqrt{-n}$ is irreducible.
::: {.proof}
Its norm is $n$. Suppose $\sqrt{-n}=\alpha\beta$ with both factors nonunits. Then
\[
1<N(\alpha),N(\beta)<n,\qquad N(\alpha)N(\beta)=n.
\]
If an element of $R$ has norm strictly less than $n$, its coefficient of $\sqrt{-n}$ must be $0$, so its norm is a perfect square. Hence $N(\alpha)$ and $N(\beta)$ are nontrivial square divisors of the squarefree integer $n$, impossible.
:::

<1>3. The element $1+\sqrt{-n}$ is irreducible.
::: {.proof}
Its norm is $n+1$. If
\[
1+\sqrt{-n}=\alpha\beta
\]
with both factors nonunits, each norm is a proper divisor of $n+1$ and hence is at most $(n+1)/2<n$. By the argument in <1>2, both $\alpha$ and $\beta$ are ordinary integers. Their product is then an integer, contradicting the nonzero $\sqrt{-n}$ coefficient of $1+\sqrt{-n}$.
:::

<1>4. If $n$ is even, then $\sqrt{-n}$ is irreducible but not prime.
::: {.proof}
Since $n>3$ is even,
\[
n=2\cdot\frac n2=-\big(\sqrt{-n}\big)^2,
\]
so $\sqrt{-n}$ divides $2(n/2)$. If $\sqrt{-n}$ divides an integer $k$, writing
\[
k=\sqrt{-n}(a+b\sqrt{-n})=a\sqrt{-n}-bn
\]
forces $a=0$ and therefore $n\mid k$. Thus $\sqrt{-n}$ divides neither $2$ nor $n/2$.
:::

<1>5. If $n$ is odd, then $1+\sqrt{-n}$ is irreducible but not prime.
::: {.proof}
One has
\[
n+1=(1+\sqrt{-n})(1-\sqrt{-n})=2\cdot\frac{n+1}{2}.
\]
Moreover
\[
R/(1+\sqrt{-n})\cong\mathbb Z/(n+1)\mathbb Z,
\]
so $1+\sqrt{-n}$ divides an integer $k$ exactly when $n+1$ divides $k$. It therefore divides neither $2$ nor $(n+1)/2$.
:::

<1>6. The ring $R$ is not a UFD.
::: {.proof}
If $n$ is even, <1>2 and <1>4 give an irreducible element that is not prime. If $n$ is odd, <1>3 and <1>5 do the same. In a UFD every irreducible element is prime, so $R$ cannot be a UFD.
:::

<1>7. If an irreducible element $\pi$ divides $ab$ but divides neither $a$ nor $b$, then the ideal $(\pi,a)$ is proper and nonprincipal.
::: {.proof}
If $(\pi,a)=(d)$ were principal, then $d\mid\pi$. Since $\pi$ is irreducible, either $d$ is a unit or $d$ is associate to $\pi$. The second possibility would imply $\pi\mid a$, so $d$ must be a unit and $(\pi,a)=R$.
But if $1=r\pi+sa$, multiplying by $b$ gives
\[
b=r\pi b+sab,
\]
and both terms on the right are divisible by $\pi$, forcing $\pi\mid b$, a contradiction. Thus the ideal is proper and cannot be principal.
:::

<1>8. Therefore an explicit nonprincipal ideal is
\[
(\sqrt{-n},2)\quad\text{if $n$ is even},
\qquad
(1+\sqrt{-n},2)\quad\text{if $n$ is odd}.
\]
::: {.proof}
Apply <1>7 to the witnesses from <1>4 and <1>5, respectively.
:::
:::
