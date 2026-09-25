---
schema: qual/card@1
id: P-BKS13-5B
kind: problem
title: Biholomorphic equivalence of the plane, the disk, and the upper half-plane
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-25
  note: Compared the authored statement with page 4 of the retained Spring 2013 solution PDF and independently reviewed the Cayley transform and Liouville obstruction.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked the explicit inverse map, its image in the upper half-plane, and non-equivalence of C with the bounded disk.
---

::: {.problem}
Which of the following domains are biholomorphically equivalent to each other: the complex plane $\mathbb { C } .$ , the unit disk $D \subset \mathbb { C }$ , the upper halfplane $\mathbb { H } \subset \mathbb { C } ?$ Write explicit biholomorphisms or prove they cannot exist.
:::

::: {.solution}
Let
$$
\DD\coloneqq\{w\in\CC:\abs{w}<1\}
$$
and
$$
\HH\coloneqq\{z\in\CC:\operatorname{Im}z>0\}.
$$

<1>1. Define
$$
\phi:\HH\longrightarrow\CC,
\qquad
\phi(z)
\coloneqq
\frac{z-i}{z+i}.
$$
Then
$$
\phi(\HH)\subseteq\DD.
$$

::: {.proof}
Write
$$
z=x+iy,
\qquad
y>0.
$$
Then
$$
\abs{z-i}^2
=
x^2+(y-1)^2
$$
and
$$
\abs{z+i}^2
=
x^2+(y+1)^2.
$$
Since $y>0$,
$$
\abs{z-i}<\abs{z+i}.
$$
Thus
$$
\abs{\phi(z)}<1.
$$
:::

<1>2. Define
$$
\psi:\DD\longrightarrow\CC,
\qquad
\psi(w)
\coloneqq
i\frac{1+w}{1-w}.
$$
Then
$$
\psi(\DD)\subseteq\HH.
$$

::: {.proof}
For $\abs{w}<1$, one has $w\neq1$, so $\psi$ is holomorphic. Multiply
numerator and denominator by $1-\overline w$:
$$
\psi(w)
=
i
\frac{(1+w)(1-\overline w)}
\abs{1-w}^2.
$$
The real part of
$$
(1+w)(1-\overline w)
$$
is
$$
1-\abs{w}^2.
$$
Therefore
$$
\operatorname{Im}\psi(w)
=
\frac{1-\abs{w}^2}{\abs{1-w}^2}
>
0.
$$
Hence $\psi(w)\in\HH$.
:::

<1>3. The maps $\phi$ and $\psi$ are mutual inverses.

::: {.proof}
Solving
$$
w=\frac{z-i}{z+i}
$$
for $z$ gives
$$
z=i\frac{1+w}{1-w}.
$$
Thus
$$
\psi(\phi(z))=z
$$
for $z\in\HH$, and
$$
\phi(\psi(w))=w
$$
for $w\in\DD$.
:::

<1>4. Therefore
$$
\boxed{\HH\cong_{\mathrm{bihol}}\DD}.
$$

::: {.proof}
Steps <1>1--<1>3 show that $\phi$ is a holomorphic bijection
$\HH\to\DD$ with holomorphic inverse $\psi$.
:::

<1>5. The complex plane $\CC$ is not biholomorphic to $\DD$.

::: {.proof}
Suppose
$$
F:\CC\longrightarrow\DD
$$
were a biholomorphism. Then $F$ would be an entire function satisfying
$$
\abs{F(z)}<1
$$
for every $z\in\CC$. By Liouville's theorem, $F$ would be constant,
contradicting bijectivity.
:::

<1>6. The complex plane $\CC$ is not biholomorphic to $\HH$.

::: {.proof}
If there were a biholomorphism
$$
G:\CC\longrightarrow\HH,
$$
then composing with the biholomorphism $\phi:\HH\to\DD$ from step <1>4
would give a biholomorphism
$$
\phi\circ G:\CC\longrightarrow\DD,
$$
contradicting step <1>5.
:::

<1>7. Thus the only biholomorphic equivalence among the three domains is
$$
\boxed{\DD\sim\HH},
$$
while $\CC$ is biholomorphic to neither.

::: {.proof}
Step <1>4 gives the equivalence of $\DD$ and $\HH$, and steps <1>5 and
<1>6 rule out the remaining pairs.
:::

<1>8. Q.E.D.

::: {.proof}
Step <1>7 is the requested classification.
:::
:::
