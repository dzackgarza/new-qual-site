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

::: {.problem}
Let $n$ be a squarefree integer greater than 3. Let $R$ denote the subring $\mathbb{Z}[\sqrt{-n}] = \{a + b\sqrt{-n} \mid a, b \in \mathbb{Z}\}$ of the field of complex numbers $\mathbb{C}$.

(a) Show that $\sqrt{-n}$ and $1 + \sqrt{-n}$ are irreducible in $R$.

(b) Prove that $R$ is not a unique factorization domain (UFD).

(c) Construct an ideal in $R$ which is not principal.

Hint: In a UFD, an element is irreducible if and only if it is prime.
:::

::: {.solution}
Put $s=\sqrt{-n}$ and define the norm
\[
N(a+bs)=(a+bs)(a-bs)=a^2+nb^2.
\]
It is multiplicative and takes positive integer values on nonzero elements.

::: pf

::: pf-step

The element $s$ is irreducible.

::: pf-proof

Suppose
\[
s=\alpha\beta
\]
with nonzero $\alpha,\beta\in R$. Then
\[
n=N(s)=N(\alpha)N(\beta).
\]
If both factors were nonunits, then
\[
1<N(\alpha)<n.
\]
Write $\alpha=a+bs$. Since $N(\alpha)<n$, necessarily $b=0$, so $N(\alpha)=a^2$. Thus a square $a^2>1$ divides the squarefree integer $n$, impossible. Hence one factor is a unit and $s$ is irreducible.

:::

:::

::: pf-step

The element $1+s$ is irreducible.

::: pf-proof

Suppose
\[
1+s=\alpha\beta
\]
with both factors nonzero. If both were nonunits, then
\[
1<N(\alpha)<N(1+s)=n+1.
\]
Write $\alpha=a+bs$. If $b\ne0$, then $N(\alpha)\ge n$. Because $N(\alpha)$ divides $n+1$, the only possibility with $n\le N(\alpha)<n+1$ is impossible. Hence $b=0$ and $\alpha=a\in\mathbb Z$.

But an integer $a$ divides $1+s$ in $R$ only if it divides both coefficients $1$ and $1$, so $a=\pm1$. Thus $\alpha$ is a unit, a contradiction. Hence $1+s$ is irreducible.

:::

:::

::: {.pf-step #s3}

For an integer $k$, one has
\[
s\mid k\quad\Longleftrightarrow\quad n\mid k.
\]

::: pf-proof

Since
\[
\frac{k}{s}=-\frac{k}{n}s,
\]
the quotient lies in $R$ exactly when $k/n\in\mathbb Z$.

:::

:::

::: {.pf-step #s4}

For an integer $k$, one has
\[
1+s\mid k\quad\Longleftrightarrow\quad n+1\mid k.
\]

::: pf-proof

Since
\[
\frac{k}{1+s}=\frac{k(1-s)}{n+1},
\]
the quotient belongs to $R$ exactly when both coefficients $k/(n+1)$ and $-k/(n+1)$ are integers, equivalently when $n+1\mid k$.

:::

:::

::: {.pf-step #s5}

If $n$ is even, then the irreducible element $s$ is not prime.

::: pf-proof

Because $n>3$ and is even,
\[
n=2\cdot\frac n2
\]
with $0<2<n$ and $0<n/2<n$. Also
\[
n=-s^2,
\]
so $s\mid 2(n/2)$. By step [](#s3){.pf-ref}, $s$ divides neither $2$ nor $n/2$. Thus $s$ is irreducible but not prime.

:::

:::

::: {.pf-step #s6}

If $n$ is odd, then the irreducible element $1+s$ is not prime.

::: pf-proof

Since $n>3$ is odd,
\[
n+1=2\cdot\frac{n+1}{2}
\]
with both positive factors strictly smaller than $n+1$. Moreover
\[
n+1=(1+s)(1-s),
\]
so $1+s$ divides their product. By step [](#s4){.pf-ref}, it divides neither factor. Hence $1+s$ is irreducible but not prime.

:::

:::

::: pf-step

The ring $R$ is not a UFD.

::: pf-proof

If $n$ is even, step [](#s5){.pf-ref} gives an irreducible element that is not prime. If $n$ is odd, step [](#s6){.pf-ref} does so. In a UFD every irreducible element is prime, so in either case $R$ is not a UFD. This proves part (b).

:::

:::

::: {.pf-step #s8}

If $n$ is even, the ideal
\[
I=(s,2)
\]
is not principal.

::: pf-proof

Suppose $I=(d)$. Then $d\mid s$. Since $s$ is irreducible, either $d$ is a unit or $d$ is associate to $s$.

If $d$ is associate to $s$, then $s\mid2$, contradicting step [](#s3){.pf-ref}. If $d$ is a unit, then $I=R$, so
\[
1=rs+2t
\]
for some $r,t\in R$. Multiplying by $n/2$ gives
\[
\frac n2=r\frac n2s+nt.
\]
Both terms on the right are divisible by $s$ because $s\mid n$, so $s\mid n/2$, contradicting step [](#s3){.pf-ref}. Hence $I$ is not principal.

:::

:::

::: {.pf-step #s9}

If $n$ is odd, the ideal
\[
J=(1+s,2)
\]
is not principal.

::: pf-proof

Suppose $J=(d)$. Since $d\mid1+s$ and $1+s$ is irreducible, either $d$ is a unit or is associate to $1+s$.

If $d$ is associate to $1+s$, then $1+s\mid2$, contradicting step [](#s4){.pf-ref}. If $d$ is a unit, then $J=R$, so
\[
1=r(1+s)+2t
\]
for some $r,t\in R$. Multiplying by $(n+1)/2$ gives
\[
\frac{n+1}{2}=r\frac{n+1}{2}(1+s)+(n+1)t.
\]
Both terms on the right are divisible by $1+s$ because $1+s\mid n+1$, so $1+s\mid(n+1)/2$, contradicting step [](#s4){.pf-ref}. Hence $J$ is not principal.

:::

:::

::: pf-step

Thus part (c) is solved by $(\sqrt{-n},2)$ when $n$ is even and by $(1+\sqrt{-n},2)$ when $n$ is odd.

::: pf-proof

This is exactly steps [](#s8){.pf-ref} and [](#s9){.pf-ref}.

:::

:::

:::

:::
