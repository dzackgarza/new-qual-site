---
schema: qual/card@1
id: E-SS9.PR-4
kind: problem
title: The Weierstrass function on a rectangular grid for purely imaginary periods
classification:
  areas:
  - complex-analysis
  topics:
  - Elliptic Functions
  - Conformal Mappings
relations: []
review: draft
audit:
- event: source-checked
  by: claude
  date: 2026-11-01
  note: >-
    Statement transcribed from Stein--Shakarchi, *Complex Analysis*, Chapter 9, §4, problem 4, read from
    `assets/attachments/Stein-Shakarchi-Complex-Analysis.pdf` (PDF page 300). This card did not
    exist before: it was found missing by a completeness audit of the collection against the book,
    which located every printed Exercises and Problems item and compared it with the cards on disk.
    The transcription was taken from the OCR text layer and cleaned of OCR errors; the asterisk marking a starred problem, and the
    printed wording, hypotheses and bracketed hints are preserved.
- event: solution-written
  by: claude
  date: 2026-11-01
  note: >-
    (a) from the two symmetries of the Weierstrass function for a rectangular lattice with purely
    imaginary period: conjugation in the lattice gives wp(conj z) = conj wp(z), and translation by the
    period it gives wp(z + it) = wp(z) = wp(conj z); combining them with the period relations makes wp
    real on the four families of grid lines. (b) the only critical points are the three half-periods,
    all of which lie on the grid, so the open rectangle carries no critical point and wp is a local
    homeomorphism there; its image is an open connected set whose boundary lies in the real axis, hence
    one of the two half-planes, and injectivity follows. Nothing is left in outline.
---

::: {.exercise}
Suppose $\tau$ is purely imaginary, say $\tau=it$ with $t>0$. Consider the division of the complex plane into congruent rectangles obtained by considering the lines $x=n/2$, $y=tm/2$ as $n$ and $m$ range over the integers. (An example is the rectangle whose vertices are $0$, $1/2$, $1/2+\tau/2$, and $\tau/2$.)

(a) Show that $\wp$ is real-valued on all these lines, and hence on the boundaries of all these rectangles.

(b) Prove that $\wp$ maps the interior of each rectangle conformally to the upper (or lower) half-plane.
:::

::: {.solution}

Let $\tau=it$ with $t>0$, $\Lambda=\ZZ+\ZZ it$, and $\wp$ the Weierstrass function of $\Lambda$.

::: pf

::: {.pf-step #s1}

$\wp(\bar z)=\overline{\wp(z)}$ and $\wp(z+it)=\wp(\bar z)$.

::: pf-proof

$\Lambda$ is invariant under conjugation, since $\overline{n+mit}=n-mit\in\Lambda$. Applying the conjugation to every term of
$$
\wp(z)=\frac{1}{z^2}+\sum_{\omega\in\Lambda\setminus\{0\}}\Bigl(\frac{1}{(z+\omega)^2}-\frac{1}{\omega^2}\Bigr)
$$
gives $\wp(\bar z)=\overline{\wp(z)}$, because $\overline{\Lambda}=\Lambda$ and the series converges absolutely.

$\wp$ is $\Lambda$-periodic, so $\wp(z+it)=\wp(z)$ since $it\in\Lambda$. Composing with the first identity, $\wp(z+it)=\wp(\bar z)$.

:::

:::

::: {.pf-step #s2}

$\wp$ is real-valued on the lines $x=n/2$ and $y=tm/2$.

::: pf-proof

*On $y=0$*, i.e. $z=x$ real: $\bar z=z$, so $\wp(x)=\overline{\wp(x)}$ by step [](#s1){.pf-ref}, hence $\wp(x)\in\RR$.

*On $x=0$*, i.e. $z=iy$: write $z+it=i(y+t)$. Then $z+it=\overline{z}$, so by step [](#s1){.pf-ref}
$$
\wp(iy)=\wp(i(y+t))=\wp(\overline{iy})=\overline{\wp(iy)},
$$
so $\wp(iy)\in\RR$.

*On $x=1/2$*: $\wp(x+iy)$ is $1$-periodic in $x$, so $\wp(1/2+iy)=\wp(-1/2+iy)$. Now $-1/2+iy=\overline{1/2+iy}-1$, so using periodicity and step [](#s1){.pf-ref},
$$
\wp(1/2+iy)=\wp(-1/2+iy)=\wp(\overline{1/2+iy})=\overline{\wp(1/2+iy)},
$$
hence real.

*On $y=t/2$*: $\wp(x+it/2)$ is $it$-periodic, so $\wp(x+it/2)=\wp(x-it/2)$, and $x-it/2=\overline{x+it/2}$, so $\wp(x+it/2)=\overline{\wp(x+it/2)}$ and the value is real.

The vertical lines $x=n/2$ follow by $1$-periodicity from $x=0$ and $x=1/2$, and the horizontal lines $y=tm/2$ by $it$-periodicity from $y=0$ and $y=t/2$; being real-valued on the four families of lines, $\wp$ is real on the boundary of every one of the rectangles they cut out.

:::

:::

::: {.pf-step #s3}

$\wp$ is a local homeomorphism at every point of the open rectangle $R=\{0<x<1/2,\ 0<y<t/2\}$.

::: pf-proof

$\wp'$ is holomorphic on $\CC\setminus\Lambda$ and its zeros are exactly the half-periods $\tfrac12,\ \tfrac{it}{2},\ \tfrac{1+it}{2}$ modulo $\Lambda$: these satisfy $2z\in\Lambda$ and are not in $\Lambda$, and $\wp'$ is odd and $\Lambda$-periodic with $\wp'$ vanishing exactly at the points of order $2$ (the $\wp$ function is a degree-$2$ map). All three lie on the boundary of $R$, since they have $x\in\{0,1/2\}$ or $y\in\{0,t/2\}$.

So $\wp'\ne0$ on the closed rectangle $\overline R$ off the boundary, in particular on $R$; a holomorphic function with non-vanishing derivative is a local homeomorphism, indeed locally conformal.

:::

:::

::: {.pf-step #s4}

$\wp$ maps $R$ bijectively onto either the upper or the lower half-plane, hence conformally.

::: pf-proof

$\wp(R)$ is open (step [](#s3){.pf-ref} and the open mapping theorem) and connected. Its boundary is contained in $\wp(\partial R)\subseteq\RR$ by step [](#s2){.pf-ref}: for a sequence $z_k\in R$ with $z_k\to z\in\partial R$, the values $\wp(z_k)$ have limit points in $\RR$ (including possibly $\infty$ at the corners, which are not in $\Lambda$, so the limit is finite unless $z\in\Lambda$; the corners $0,\tfrac12,\tfrac{it}{2},\tfrac{1+it}{2}$ are the half-periods and $0$, and $0\in\Lambda$ gives the pole).

An open connected subset of $\CC\setminus\RR$ whose boundary lies in $\RR$ is contained in, and hence equals, one of the two half-planes: it is a connected component of $\CC\setminus\RR$. Since $\wp$ is a local homeomorphism on $R$ and $R$ is simply connected without critical points, $\wp|_R$ is injective, so it is a conformal map onto that half-plane.

Which half-plane depends on the rectangle: adjacent rectangles give opposite signs, because the values on a shared edge are real and $\wp$ is a local homeomorphism there, so the images lie on opposite sides.

:::

:::

:::

:::
