---
schema: qual/card@1
id: P-KSRING17-037
kind: problem
title: Irreducibility of $x^2+1$ over $\mathbb Z_p$ for $p\equiv 3 \pmod 4$
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 37 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
---

::: {.problem}
Show that if p is a prime such that $p \equiv 3 ( { \bmod { 4 } } )$ , then $x ^ { 2 } + 1$ is irreducible in $\mathbb { Z } _ { p } [ x ]$
:::

::: {.solution}
<1>1. The prime $p$ is odd, and
$$
\frac{p-1}{2}
$$
is odd.

::: {.proof}
The congruence
$$
p\equiv3\pmod4
$$
implies
$$
p=4m+3
$$
for some integer $m$. Hence $p$ is odd and
$$
\frac{p-1}{2}
=
2m+1,
$$
which is odd.
:::

<1>2. There is no element
$$
a\in\FF_p
$$
satisfying
$$
a^2=-1.
$$

::: {.proof}
Suppose, for contradiction, that
$$
a^2=-1.
$$
Then
$$
a\ne0.
$$
By Fermat's little theorem,
$$
a^{p-1}=1.
$$
On the other hand,
$$
\begin{aligned}
a^{p-1}
&=
\left(a^2\right)^{(p-1)/2}\\
&=
(-1)^{(p-1)/2}\\
&=
-1,
\end{aligned}
$$
because $(p-1)/2$ is odd by step <1>1.
This gives
$$
1=-1
$$
in $\FF_p$, impossible because $p$ is odd.
:::

<1>3. The polynomial
$$
x^2+1
$$
has no root in $\FF_p$.

::: {.proof}
A root
$$
a\in\FF_p
$$
would satisfy
$$
a^2+1=0,
$$
equivalently
$$
a^2=-1,
$$
which is impossible by step <1>2.
:::

<1>4. Therefore
$$
\boxed{
x^2+1
\text{ is irreducible in }\FF_p[x].
}
$$

::: {.proof}
A polynomial of degree $2$ over a field is reducible if and only if it has a root in that field. Step <1>3 shows that $x^2+1$ has no root in $\FF_p$, so it is irreducible.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is the required conclusion.
:::
:::
