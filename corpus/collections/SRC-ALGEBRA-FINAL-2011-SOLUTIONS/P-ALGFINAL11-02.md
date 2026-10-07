---
schema: qual/card@1
id: P-ALGFINAL11-02
kind: problem
title: Norms and prime elements in quadratic integer rings
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
---

::: {.problem}
Let $n > 1$ be in $\mathbb { Z } ,$ and let $R { : = } \mathbb { Z } [ { \sqrt { - n } } ]$

For $x = a + b { \sqrt { - n } } \in R \left( a , b \in \mathbb { Z } \right)$ , set ${ \bar { x } } = a - b { \sqrt { - n } } .$ , and define the norm

$$
N ( x ) = x \bar { x } = a ^ { 2 } + n b ^ { 2 } .
$$

(a) Assuming $x \neq 0$ , describe group isomorphisms $R / x R \cong R / \bar { x } R \cong x R / x \bar { x } R .$

[4]

$$
( \mathrm { b } ) \mathrm { \ D e d u c e \ f r o m \ ( a ) \ t h a t \ } N ( x ) ^ { 2 } = [ R : x R ] [ x R : x \bar { x } R ] = [ R : x R ] ^ { 2 } .\tag{[3]}
$$

(c) Deduce from (b) that if N (x) is prime in $\mathbb { Z }$ then x is prime in R. [4]

(d) Deduce from (c) that if p is a prime in $\mathbb { Z }$ then there is at most one way to represent p in the form $p = a ^ { 2 } + n b ^ { 2 }$ where a and b are positive integers.
[4]
:::

::: {.solution}
<1>1. Conjugation induces an additive-group isomorphism
$$
\boxed{R/xR\xrightarrow{\sim}R/\bar xR},
\qquad
y+xR\longmapsto \bar y+\bar xR.
$$
::: {.proof}
Complex conjugation restricts to a ring automorphism of $R$ and carries the ideal $xR$ onto $\bar xR$. Hence it induces the displayed quotient isomorphism.
:::

<1>2. Multiplication by $x$ induces an additive-group isomorphism
$$
\boxed{R/\bar xR\xrightarrow{\sim}xR/x\bar xR},
\qquad
y+\bar xR\longmapsto xy+x\bar xR.
$$
::: {.proof}
The map is well-defined and surjective. If
$$
xy\in x\bar xR,
$$
then
$$
xy=x\bar xz
$$
for some $z\in R$. Since $R$ is an integral domain and $x\ne0$, cancellation gives
$$
y=\bar xz,
$$
so the kernel is exactly $\bar xR$.
:::

<1>3. Hence
$$
\boxed{R/xR\cong R/\bar xR\cong xR/x\bar xR}
$$
as additive groups.
::: {.proof}
Combine step <1>1 and step <1>2.
:::

<1>4. For every positive integer $m$,
$$
[R:mR]=m^2.
$$
::: {.proof}
As an additive group,
$$
R\cong\ZZ\oplus\ZZ\sqrt{-n}\cong\ZZ^2.
$$
Therefore
$$
R/mR\cong(\ZZ/m\ZZ)^2,
$$
which has $m^2$ elements.
:::

<1>5. For $x\ne0$,
$$
\boxed{N(x)^2=[R:xR]\,[xR:x\bar xR]=[R:xR]^2},
$$
and therefore
$$
\boxed{[R:xR]=N(x)}.
$$
::: {.proof}
Since
$$
x\bar x=N(x)\in\ZZ_{>0},
$$
step <1>4 gives
$$
[R:x\bar xR]=N(x)^2.
$$
Index multiplicativity gives
$$
[R:x\bar xR]
=[R:xR]\,[xR:x\bar xR].
$$
By step <1>3,
$$
[xR:x\bar xR]=[R:\bar xR]=[R:xR].
$$
Thus
$$
N(x)^2=[R:xR]^2.
$$
Both sides are positive integers, so $[R:xR]=N(x)$.
:::

<1>6. If $N(x)$ is prime in $\ZZ$, then
$$
\boxed{x\text{ is prime in }R}.
$$
::: {.proof}
By step <1>5,
$$
|R/xR|=N(x).
$$
If $N(x)=p$ is prime, then the quotient ring $R/xR$ has exactly $p$ elements. Its additive group is cyclic of prime order, so its identity is nonzero and every nonzero element is a nonzero multiple of $1$; hence $R/xR\cong\FF_p$ is a field. Therefore $xR$ is maximal, hence prime, so $x$ is a prime element.
:::

<1>7. The only units of $R$ are $\pm1$.
::: {.proof}
If $u\in R^\times$, then
$$
1=N(1)=N(u)N(u^{-1}).
$$
The norm takes nonnegative integer values, so $N(u)=1$. Writing
$$
u=a+b\sqrt{-n},
$$
one has
$$
a^2+nb^2=1.
$$
Since $n>1$, this forces $b=0$ and $a=\pm1$.
:::

<1>8. If a rational prime $p$ admits two representations
$$
p=a^2+nb^2=c^2+nd^2
$$
with $a,b,c,d>0$, then
$$
\boxed{a=c,\qquad b=d}.
$$
::: {.proof}
Put
$$
x=a+b\sqrt{-n},
\qquad
y=c+d\sqrt{-n}.
$$
Then
$$
p=x\bar x=y\bar y
$$
and
$$
N(x)=N(y)=p.
$$
By step <1>6, $x$ is prime in $R$. Since
$$
x\mid y\bar y,
$$
primality gives
$$
x\mid y
\qquad\text{or}\qquad
x\mid\bar y.
$$

If $x\mid y$, write $y=xu$. Taking norms gives
$$
p=pN(u),
$$
so $N(u)=1$. By step <1>7, $u=\pm1$. Positivity of $a,b,c,d$ forces $u=1$, hence $y=x$ and therefore $a=c$, $b=d$.

If $x\mid\bar y$, the same norm argument gives $\bar y=\pm x$. But
$$
\bar y=c-d\sqrt{-n}
$$
cannot equal either $x=a+b\sqrt{-n}$ or $-x=-a-b\sqrt{-n}$ when all four integers are positive. Thus this case is impossible.
:::

<1>9. Q.E.D.
::: {.proof}
Step <1>3 proves part (a), step <1>5 proves part (b), step <1>6 proves part (c), and step <1>8 proves part (d).
:::
:::
