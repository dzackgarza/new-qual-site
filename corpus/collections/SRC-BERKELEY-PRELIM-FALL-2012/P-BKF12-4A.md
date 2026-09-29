---
schema: qual/card@1
id: P-BKF12-4A
kind: problem
title: The sum $\sum(-1)^k/(2k+1)^3$ via residues of $1/(z^3\cos z)$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked against Problem 4A in the retained Fall 2012 Berkeley prelim exam
    and its retained solution packet F12_Solutions.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked every residue, the uniform contour bound on all four square
    edges, and the symmetric pairing that yields the alternating odd-cube sum.
---

::: {.problem}
(a) Find the poles and residues of
$$
\frac{1}{z^3\cos z}.
$$

(b) Show that the integral of the function above over a square contour
centered at the origin with side $2\pi N$ tends to zero as the integer
$N$ tends to infinity.

(c) Find the sum
$$
1-\frac1{3^3}+\frac1{5^3}-\frac1{7^3}+\cdots.
$$
:::

::: {.solution}
Put
$$
F(z)\coloneqq\frac1{z^3\cos z},
$$
and, for $N\ge1$, let $C_N$ be the positively oriented boundary of
the square
$$
\{z\in\CC:\abs{\Re z}\le\pi N,
                 \abs{\Im z}\le\pi N\}.
$$

::: pf

::: {.pf-step #s1}

The function $F$ has a pole of order $3$ at $0$, with
$$
\operatorname*{Res}_{z=0}F=\frac12.
$$

::: pf-proof

Near $0$,
$$
\cos z=1-\frac{z^2}{2}+O(z^4),
$$
so
$$
\frac1{\cos z}=1+\frac{z^2}{2}+O(z^4).
$$
Hence
$$
F(z)
=\frac1{z^3}+\frac1{2z}+O(z),
$$
which proves both the pole order and the residue.

:::

:::

::: {.pf-step #s2}

For every $n\in\ZZ$, the point
$$
z_n\coloneqq\left(n+\frac12\right)\pi
$$
is a simple pole of $F$, and
$$
\operatorname*{Res}_{z=z_n}F
=\frac{(-1)^{n+1}}{z_n^3}.
$$
These, together with $0$, are all the poles of $F$.

::: pf-proof

The zeros of $\cos z$ are exactly the points $z_n$, and they are
simple because
$$
-\sin z_n=-(-1)^n=(-1)^{n+1}\ne0.
$$
Since $z_n\ne0$, the corresponding pole of $F$ is simple. Thus
$$
\operatorname*{Res}_{z=z_n}F
=\frac{1}{z_n^3(-\sin z_n)}
=\frac{(-1)^{n+1}}{z_n^3}.
$$
The factor $z^3$ contributes only the pole at $0$, so the list is
complete.

:::

:::

::: {.pf-step #s3}

On $C_N$,
$$
\frac1{\abs{\cos z}}\le1
$$
and
$$
\abs z\ge\pi N.
$$

::: pf-proof

Write $z=x+iy$. The identity
$$
\abs{\cos(x+iy)}^2
=\cos^2x+\sinh^2y
$$
follows from
$$
\cos(x+iy)=\cos x\cosh y-i\sin x\sinh y.
$$

On a vertical edge, $x=\pm\pi N$, so
$$
\abs{\cos z}=\cosh y\ge1.
$$
On a horizontal edge, $y=\pm\pi N$, so
$$
\abs{\cos z}^2
\ge\sinh^2(\pi N)>1.
$$
Thus the first bound holds on every edge. Every point of $C_N$ has
either $\abs x=\pi N$ or $\abs y=\pi N$, which gives
$\abs z\ge\pi N$.

:::

:::

::: {.pf-step #s4}

The contour integrals satisfy
$$
\lim_{N\to\infty}\int_{C_N}F(z)\,dz=0.
$$

::: pf-proof

The length of $C_N$ is $8\pi N$. By step [](#s3){.pf-ref},
$$
\abs{F(z)}
\le\frac1{(\pi N)^3}
$$
on $C_N$. Hence the ML estimate gives
$$
\abs{\int_{C_N}F(z)\,dz}
\le
8\pi N\frac1{(\pi N)^3}
=\frac{8}{\pi^2N^2},
$$
which tends to $0$.

:::

:::

::: {.pf-step #s5}

The poles of $F$ inside $C_N$ are $0$ and
$$
z_n=\left(n+\frac12\right)\pi,
\qquad
-N\le n\le N-1.
$$
Their total residue is
$$
\frac12
-\frac{16}{\pi^3}
\sum_{k=0}^{N-1}\frac{(-1)^k}{(2k+1)^3}.
$$

::: pf-proof

The real pole $z_n$ lies inside the square exactly when
$$
\abs{n+\tfrac12}<N,
$$
which is equivalent to $-N\le n\le N-1$.

For $k=0,\ldots,N-1$, the poles with indices $k$ and $-k-1$ are
opposites, and step [](#s2){.pf-ref} gives the same residue at both:
$$
\operatorname*{Res}_{z=z_k}F
=\operatorname*{Res}_{z=z_{-k-1}}F
=\frac{(-1)^{k+1}}{((k+\frac12)\pi)^3}.
$$
Therefore the sum of all nonzero residues inside $C_N$ is
$$
2\sum_{k=0}^{N-1}
\frac{(-1)^{k+1}}{((k+\frac12)\pi)^3}
=-\frac{16}{\pi^3}
\sum_{k=0}^{N-1}\frac{(-1)^k}{(2k+1)^3}.
$$
Adding the residue $1/2$ from step [](#s1){.pf-ref} gives the claim.

:::

:::

::: {.pf-step #s6}

One has
$$
\boxed{
1-\frac1{3^3}+\frac1{5^3}-\frac1{7^3}+\cdots
=\frac{\pi^3}{32}
}.
$$

::: pf-proof

By the residue theorem and step [](#s5){.pf-ref},
$$
\frac{1}{2\pi i}\int_{C_N}F(z)\,dz
=\frac12
-\frac{16}{\pi^3}
\sum_{k=0}^{N-1}\frac{(-1)^k}{(2k+1)^3}.
$$
Step [](#s4){.pf-ref} shows that the left side tends to $0$. Therefore
$$
\lim_{N\to\infty}
\sum_{k=0}^{N-1}\frac{(-1)^k}{(2k+1)^3}
=\frac{\pi^3}{32},
$$
which is the displayed series.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref} and [](#s2){.pf-ref} answer part (a), step [](#s4){.pf-ref} answers part (b), and
step [](#s6){.pf-ref} answers part (c).

:::

:::

:::
