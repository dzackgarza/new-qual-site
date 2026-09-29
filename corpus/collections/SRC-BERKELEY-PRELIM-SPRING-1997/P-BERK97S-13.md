---
schema: qual/card@1
id: P-BERK97S-13
kind: problem
title: Every injective entire function is affine linear
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-23
---

::: {.problem}
Suppose $f:\mathbb C\to\mathbb C$ is injective and entire. Prove that there are $a,b\in\mathbb C$ with $a\ne0$ such that
\[
f(z)=az+b
\]
for every $z\in\mathbb C$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

The derivative $f'(z)$ is nonzero for every $z\in\CC$.

::: pf-proof

Suppose $f'(z_0)=0$. Since $f$ is not constant, its Taylor expansion gives
an integer $m\geq2$ and a holomorphic function $u$ with $u(z_0)\neq0$
such that
$$
f(z)-f(z_0)=(z-z_0)^m u(z).
$$
On a sufficiently small disk about $z_0$, the nonvanishing function $u$
has a holomorphic $m$-th root $v$. Put
$$
H(z)\coloneqq(z-z_0)v(z).
$$
Then $H'(z_0)=v(z_0)\neq0$, so after shrinking the disk, $H$ is a
biholomorphism onto a neighborhood of $0$, while
$$
f(z)-f(z_0)=H(z)^m.
$$
Two sufficiently small numbers differing by a nontrivial $m$-th root of
unity have the same $m$-th power, and their distinct preimages under $H$
therefore have the same image under $f$. This contradicts injectivity.
Thus $f'(z_0)\neq0$.

:::

:::

::: pf-step

For
$$
g(\zeta)\coloneqq f(1/\zeta),
\qquad
\zeta\neq0,
$$
the isolated singularity at $0$ is a pole.

::: pf-proof

The map $g$ is injective on $\CC\sm\{0\}$.

Suppose first that $0$ were an essential singularity. Choose
$\zeta_0\neq0$. By step [](#s1){.pf-ref} and the chain rule, $g'(\zeta_0)\neq0$,
so the holomorphic inverse function theorem gives a neighborhood $U$ of
$\zeta_0$, with closure disjoint from $0$, such that $g(U)$ contains an
open neighborhood $V$ of $g(\zeta_0)$. By the Casorati--Weierstrass
theorem, the image under $g$ of every punctured neighborhood of $0$ is
dense in $\CC$. Taking such a punctured neighborhood disjoint from $U$,
there is a point $\zeta$ in it with $g(\zeta)\in V$. Since
$V\subseteq g(U)$, some $u\in U$ has $g(u)=g(\zeta)$, contradicting
injectivity of $g$.

Suppose instead that the singularity were removable. Then $g$ would be
bounded near $0$, so $f$ would be bounded outside a sufficiently large
disk. It is also bounded on that disk by continuity. Liouville's theorem
would make $f$ constant, contradicting injectivity. Hence the singularity
is neither essential nor removable, so it is a pole.

:::

:::

::: pf-step

The entire function $f$ is a polynomial.

::: pf-proof

If the pole of $g$ at $0$ has order $m$, then for some constants $C,R>0$,
$$
\abs{f(z)}\leq C\abs{z}^m
$$
whenever $\abs{z}\geq R$. Enlarging the constant gives
$$
\abs{f(z)}\leq C(1+\abs{z}^m)
$$
for all $z\in\CC$. Let
$$
f(z)=\sum_{k=0}^\infty a_kz^k.
$$
For $k>m$, Cauchy's estimate on the circle $\abs{z}=r$ gives
$$
\abs{a_k}
\leq
\frac{C(1+r^m)}{r^k}.
$$
Letting $r\to\infty$ yields $a_k=0$. Thus only finitely many Taylor
coefficients are nonzero.

:::

:::

::: {.pf-step #s4}

The polynomial $f$ has degree $1$.

::: pf-proof

It cannot have degree $0$ because it is injective. If
$\deg f=d\geq2$, then $f'$ is a nonconstant polynomial of degree $d-1$.
By the fundamental theorem of algebra, $f'$ has a zero, contradicting
step [](#s1){.pf-ref}. Hence $\deg f=1$.

:::

:::

::: {.pf-step #s5}

Therefore there are $a,b\in\CC$ with $a\neq0$ such that
$$
\boxed{f(z)=az+b}
$$
for every $z\in\CC$.

::: pf-proof

By step [](#s4){.pf-ref}, $f$ is a degree-one polynomial, so it has the displayed form
with nonzero leading coefficient.

:::

:::

::: pf-qed

Step [](#s5){.pf-ref} is the required conclusion.

:::

:::

:::
