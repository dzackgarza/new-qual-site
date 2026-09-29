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
Which of the following domains are biholomorphically equivalent to each other: the complex plane $\CC$, the unit disk $D \subset \CC$, the upper halfplane $\HH \subset \CC$? Write explicit biholomorphisms or prove they cannot exist.
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

::: pf

::: {.pf-step #s1}

Define
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

::: pf-proof

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

:::

::: {.pf-step #s2}

Define
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

::: pf-proof

For $\abs{w}<1$, one has $w\neq1$, so $\psi$ is holomorphic. Multiply
numerator and denominator by $1-\overline w$:
$$
\psi(w)
=
i
\frac{(1+w)(1-\overline w)}
{\abs{1-w}^2}.
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

:::

::: {.pf-step #s3}

The maps $\phi$ and $\psi$ are mutual inverses.

::: pf-proof

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

:::

::: {.pf-step #s4}

Therefore
$$
\boxed{\HH\cong_{\mathrm{bihol}}\DD}.
$$

::: pf-proof

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref} and [](#s3){.pf-ref} show that $\phi$ is a holomorphic bijection
$\HH\to\DD$ with holomorphic inverse $\psi$.

:::

:::

::: {.pf-step #s5}

The complex plane $\CC$ is not biholomorphic to $\DD$.

::: pf-proof

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

:::

::: {.pf-step #s6}

The complex plane $\CC$ is not biholomorphic to $\HH$.

::: pf-proof

If there were a biholomorphism
$$
G:\CC\longrightarrow\HH,
$$
then composing with the biholomorphism $\phi:\HH\to\DD$ from step [](#s4){.pf-ref}
would give a biholomorphism
$$
\phi\circ G:\CC\longrightarrow\DD,
$$
contradicting step [](#s5){.pf-ref}.

:::

:::

::: {.pf-step #s7}

Thus the only biholomorphic equivalence among the three domains is
$$
\boxed{\DD\sim\HH},
$$
while $\CC$ is biholomorphic to neither.

::: pf-proof

Step [](#s4){.pf-ref} gives the equivalence of $\DD$ and $\HH$, and steps [](#s5){.pf-ref} and [](#s6){.pf-ref} rule out the remaining pairs.

:::

:::

::: pf-qed

Step [](#s7){.pf-ref} is the requested classification.

:::

:::

:::
