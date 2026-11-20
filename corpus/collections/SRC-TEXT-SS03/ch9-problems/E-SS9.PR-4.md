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
- event: source-checked
  by: claude
  date: 2026-11-20
  note: >-
    Two corrections to the first event above. Its locator "(PDF page 300)" is wrong: Problem 4 is on
    PDF p. 301, printed p. 282; PDF p. 300 is printed p. 281 and carries Problems 1--3. And its
    sentence that "the asterisk marking a starred problem ... [is] preserved" is wrong: nothing on
    the card recorded the mark, which the remark below now does. Re-read on printed p. 282 today,
    the statement is the print's, both parts and the parenthetical example of the rectangle; the
    asterisk stands before "4." Not checked: the two parts of the argument were read for sense (the
    conjugation symmetry $\wp(\bar z)=\overline{\wp(z)}$ for a real lattice, the period $\tau$
    giving $\wp(z+\tau)=\wp(z)$, the critical points at the three half-periods lying on the grid,
    and the image open with boundary in $\mathbb{R}$) but were not re-derived in this pass.
- event: solution-reviewed
  by: claude
  date: 2026-11-20
  note: >-
    Repair of step s4 on the reader's report. It concluded injectivity of $\restrictionof{\wp}{R}$
    from "$\wp$ is a local homeomorphism on $R$ and $R$ is simply connected without critical points",
    which is false as an inference: $\exp$ is a local biholomorphism on the simply connected $\CC$
    and is not injective. The step now argues that $\restrictionof{\wp}{R}$ is proper — a compact
    $K\subseteq\wp(R)$ has $\wp^{-1}(K)\cap R$ closed in the bounded $R$ and at positive distance
    from $\partial R$, since $\wp(\partial R)\subseteq\RR\cup\{\infty\}$ misses $K$ — and that a
    proper local homeomorphism onto the simply connected half-plane $\wp(R)$ is a homeomorphism.
    Steps s1--s3 are unchanged. Provenance: no published solution set covers this Problem (Rhoades,
    *Solutions/Hints to the Exercises*, 2006, covers a selection of the Exercises), so the argument
    is the card's own.
- event: solution-reviewed
  by: claude
  date: 2026-11-20
  note: >-
    Second component of step s4 repaired, on a referee's report of this session: the properness
    argument, and the identification of $\wp(R)$ with a half-plane before it, presupposed that
    $\wp(R)$ meets neither the real axis nor infinity, which the card had not proved. A connected
    open subset of $\CC\setminus\RR$ whose boundary lies in $\RR$ is a half-plane, but only under
    that disjointness, which fails for $\CC\setminus[0,\infty)$. The step now proves it: if
    $\wp(z)\in\RR$ then $\wp(z)=\wp(\bar z)$ by step s1, and $\wp(z)=\wp(w)$ forces
    $z\equiv\pm w\pmod\Lambda$ since $\wp$ is even with a double pole at $0$ as its only pole, so
    $2\operatorname{Im}z\in t\ZZ$ or $2\operatorname{Re}z\in\ZZ$, neither of which holds on $R$.
    The rest of the step is unchanged.
---

::: {.exercise}
Suppose $\tau$ is purely imaginary, say $\tau=it$ with $t>0$. Consider the division of the complex plane into congruent rectangles obtained by considering the lines $x=n/2$, $y=tm/2$ as $n$ and $m$ range over the integers. (An example is the rectangle whose vertices are $0$, $1/2$, $1/2+\tau/2$, and $\tau/2$.)

(a) Show that $\wp$ is real-valued on all these lines, and hence on the boundaries of all these rectangles.

(b) Prove that $\wp$ maps the interior of each rectangle conformally to the upper (or lower) half-plane.
:::

::: {.remark}
The book marks this problem with an asterisk (Chapter 9, Problem 4, printed p. 282).
:::

::: {.solution}
No published solution set covers the end-of-chapter Problems of Stein--Shakarchi: the set of R. C. Rhoades, *Solutions/Hints to the Exercises from Complex Analysis by Stein and Shakarchi* (2006), covers a selection of the chapter Exercises and not the Problems, and no other set was located. The argument is the card's own.

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

An open connected subset of $\CC\setminus\RR$ whose boundary lies in $\RR$ is contained in, and hence equals, one of the two half-planes: it is a connected component of $\CC\setminus\RR$.

It remains to see that $\restrictionof{\wp}{R}$ is injective, which does not follow from local injectivity alone: $\exp$ is a local biholomorphism on the simply connected $\CC$ and is not injective. First, $\wp$ takes no real value on $R$. If $\wp(z)\in\RR$, then $\wp(z)=\overline{\wp(z)}=\wp(\bar z)$ by step [](#s1){.pf-ref}; and $\wp(z)=\wp(w)$ forces $z\equiv\pm w\pmod\Lambda$, because for fixed $w$ the function $\wp(z)-\wp(w)$ has its only pole at $0$, of order $2$, and therefore exactly two zeros counted with multiplicity, at $z=w$ and $z=-w$. Hence $z\equiv\bar z$ or $z\equiv-\bar z\pmod\Lambda$, that is $2\operatorname{Im}z\in t\ZZ$ or $2\operatorname{Re}z\in\ZZ$, and neither holds on $R$. So $\wp(R)\subseteq\CC\setminus\RR$.

What is needed next is properness. Let $K\subseteq\wp(R)$ be compact. Then $\wp^{-1}(K)\cap R$ is closed in $R$, and it stays at a positive distance from $\partial R$: if $z_k\in\wp^{-1}(K)\cap R$ tended to $z\in\partial R$, then $\wp(z_k)\in K$ would converge to $\wp(z)\in\RR$ by continuity of $\wp$ on $\overline R\setminus\Lambda$, or to $\infty$ at the corner $0\in\Lambda$, and either is impossible because $K$ is a compact subset of a half-plane. Since $\overline R$ is bounded, $\wp^{-1}(K)\cap R$ is compact, so $\restrictionof{\wp}{R}$ is proper. A proper local homeomorphism is a covering map, and a covering of the simply connected $\wp(R)$ by the connected $R$ is trivial, so $\restrictionof{\wp}{R}$ is a homeomorphism onto $\wp(R)$: it is injective and conformal.

Which half-plane depends on the rectangle: adjacent rectangles give opposite signs, because the values on a shared edge are real and $\wp$ is a local homeomorphism there, so the images lie on opposite sides.

:::

:::

:::

:::
