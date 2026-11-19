---
schema: qual/card@1
id: E-SS4.EX-11
kind: problem
title: Entire functions of order 2 with Gaussian decay on the real line
classification:
  areas:
  - complex-analysis
  topics:
  - Entire Functions
  - Phragmén–Lindelöf
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-11
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Structured into Lamport steps from the card's own prose, and the sectorial lemma is now proved
    rather than quoted: in the sector |arg z| <= pi/8 one has cos(3 arg z) >= cos(3 pi/8) > 0, so
    h_delta = h exp(-delta z^3) is bounded by M on the large arc as well as on the rays, and the
    maximum principle followed by delta -> 0 gives |h| <= M. The two boundary-ray estimates for
    H_delta are computed explicitly (on the positive axis the exponential contributes
    e^{(c2 - delta) r^2}; on the ray arg = pi/4 one has z^2 = i r^2 and the contribution is
    e^{-(c1 + delta) r^2}, so both give C e^{-delta r^2} <= C), and the growth of H_delta is bounded
    by e^{K|z|^2} using |x^2 - y^2| <= |z|^2 and |2xy| <= |z|^2. The conclusion on the sector
    |y| <= x is then extended to the other three sectors by reflection (the hypotheses are
    invariant under z -> conj z, -conj z, -z) and to |y| >= |x| by the original growth bound, and
    the constants a, b are given explicitly. The converse is proved with c2 = a and c1 = b.
    Statement unchanged; no retained solution set covers the exercises of Stein-Shakarchi.
---

::: {.exercise}
One can give a neater formulation of the result in Exercise 10 by proving the following fact.

Suppose $f(z)$ is an entire function of strict order $2$, that is,
$$
f(z) = O(e^{c_1\abs{z}^2})
$$
for some $c_1 > 0$. Suppose also that for $x$ real,
$$
f(x) = O(e^{-c_2\abs{x}^2})
$$
for some $c_2 > 0$. Then
$$
\abs{f(x + iy)} = O(e^{-ax^2 + by^2})
$$
for some $a, b > 0$. The converse is obviously true.
:::

::: {.solution}
The proof is a Phragmén--Lindelöf argument on the sector $0\le\arg z\le\pi/4$: multiplying $f$ by the exponential $\exp\bigl((c_2-\delta+i(c_1+\delta))z^2\bigr)$ makes it bounded by $C$ on both boundary rays and still of growth $e^{K\abs z^2}$ inside, so the sectorial lemma gives the bound throughout the sector, and letting $\delta\downarrow0$ produces $\abs f\le Ce^{-c_2(x^2-y^2)+2c_1xy}$, which the elementary inequality $2xy\le\varepsilon x^2+y^2/\varepsilon$ turns into the required $-ax^2+by^2$. The argument is this card's own: no retained solution set covers the exercises of Stein--Shakarchi.

::: pf

::: {.pf-step #lemma}
Let $S=\{\abs{\arg z}\le\pi/8\}$. If $h$ is holomorphic on the interior of $S$, continuous on $S$, with $\abs{h(z)}\le e^{K\abs z^2}$ on $S$ and $\abs h\le M$ on the two boundary rays, then $\abs h\le M$ on $S$.

::: pf-proof
For $\delta>0$ put $h_\delta(z)=h(z)e^{-\delta z^3}$. On $S$ one has $\abs{e^{-\delta z^3}}=e^{-\delta\abs z^3\cos(3\arg z)}$ and $\cos(3\theta)\ge\cos(3\pi/8)>0$ for $\abs\theta\le\pi/8$, since $3\theta\in[-3\pi/8,3\pi/8]$. Hence $\abs{h_\delta(z)}\le e^{K\abs z^2-\delta\abs z^3\cos(3\pi/8)}$, which tends to $0$ as $\abs z\to\infty$ in $S$; so for $R$ large, $\abs{h_\delta}\le M$ on the arc $\abs z=R$ of $S$. On the two boundary rays, $\cos(3\theta)=\cos(\pm3\pi/8)>0$, so $\abs{e^{-\delta z^3}}\le1$ and $\abs{h_\delta}\le\abs h\le M$. The maximum modulus principle applied to $h_\delta$ on the truncated sector $\{\abs z<R\}\cap S$ gives $\abs{h_\delta}\le M$ there, hence on $S$; letting $\delta\downarrow0$ gives $\abs h\le M$ on $S$.
:::

:::


::: {.pf-step #sector}
Put $D=\{z=x+iy:x\ge y\ge0\}$, which is the sector $0\le\arg z\le\pi/4$ shifted by $\pi/8$ from $S$. For $\delta>0$ let $H_\delta(z)=f(z)\exp\bigl((c_2-\delta+i(c_1+\delta))z^2\bigr)$. Then $\abs{H_\delta}\le C$ on $D$.

::: pf-proof
The sector $D$ is obtained from $S$ by rotation through $\pi/8$, so step [](#lemma){.pf-ref} applies to $h=H_\delta\circ(\text{rotation})$ provided $H_\delta$ has growth $e^{K\abs z^2}$ on $D$ and is bounded by $C$ on the two boundary rays of $D$. Growth: $\abs{f(z)}\le Ce^{c_1\abs z^2}$ by hypothesis, and $\abs{\exp((c_2-\delta+i(c_1+\delta))z^2)}=e^{(c_2-\delta)(x^2-y^2)-2(c_1+\delta)xy}\le e^{(c_2+2c_1+2\delta)\abs z^2}$ using $\abs{x^2-y^2}\le\abs z^2$ and $\abs{2xy}\le\abs z^2$; so $\abs{H_\delta(z)}\le Ce^{K\abs z^2}$ with $K=c_1+c_2+2c_1+2\delta$.

Boundary ray $\arg z=0$: for $r>0$, $\abs{H_\delta(r)}=\abs{f(r)}e^{(c_2-\delta)r^2}\le Ce^{-c_2r^2}e^{(c_2-\delta)r^2}=Ce^{-\delta r^2}\le C$, using the real-axis hypothesis.

Boundary ray $\arg z=\pi/4$: for $z=re^{i\pi/4}$ one has $z^2=ir^2$, so $\abs{\exp((c_2-\delta+i(c_1+\delta))z^2)}=e^{-(c_1+\delta)r^2}$ and hence $\abs{H_\delta(re^{i\pi/4})}\le Ce^{c_1r^2}e^{-(c_1+\delta)r^2}=Ce^{-\delta r^2}\le C$. With both rays bounded by $C$, step [](#lemma){.pf-ref} gives $\abs{H_\delta}\le C$ on $D$.
:::

:::


::: {.pf-step #limit}
On $D$, $\abs{f(z)}\le Ce^{-c_2(x^2-y^2)+2c_1xy}$.

::: pf-proof
By step [](#sector){.pf-ref}, $\abs{f(z)}\le C\abs{\exp((c_2-\delta+i(c_1+\delta))z^2)}^{-1}=C\exp\bigl(-(c_2-\delta)(x^2-y^2)+2(c_1+\delta)xy\bigr)$ for every $\delta>0$ and every $z\in D$. Letting $\delta\downarrow0$ gives the display.
:::

:::


::: {.pf-step #squares}
On $D$, $\abs{f(x+iy)}\le Ce^{-ax^2+by^2}$ for constants $a,b>0$; for example $a=c_2-c_1\varepsilon$ and $b=c_2+c_1\varepsilon^{-1}$ for any $0<\varepsilon<c_2/c_1$.

::: pf-proof
By the elementary inequality $2c_1xy\le c_1\varepsilon x^2+c_1y^2/\varepsilon$, valid for all real $x,y$ and $\varepsilon>0$ (it follows from $2uv\le u^2+v^2$ with $u=\sqrt{\varepsilon}x$ and $v=y/\sqrt{\varepsilon}$), step [](#limit){.pf-ref} gives
$$
\abs{f(z)}\le C\exp\bigl((-c_2+c_1\varepsilon)x^2+(c_2+c_1\varepsilon^{-1})y^2\bigr).
$$
Choosing $\varepsilon<c_2/c_1$ makes $a=c_2-c_1\varepsilon>0$, and $b=c_2+c_1\varepsilon^{-1}>0$.
:::

:::


::: {.pf-step #all}
The bound $\abs{f(x+iy)}\le C'e^{-ax^2+by^2}$ with $a,b>0$ holds on all of $\CC$, after enlarging the constants.

::: pf-proof
The sector $D$ covers $0\le y\le x$. The reflections $z\mapsto\bar z$, $z\mapsto-\bar z$, $z\mapsto-z$ carry $D$ to the other three sectors with $0\le\abs y\le\abs x$, and $f$ composed with them satisfies the same hypotheses with $c_1,c_2$ unchanged (since $\abs{f(\pm\bar z)}$ and $\abs{f(\pm z)}$ obey the same bounds); so the same argument gives the estimate in each, with the same $a,b$ and possibly a larger $C$. On the remaining region $\abs y\ge\abs x$ the hypothesis $\abs{f(z)}\le Ce^{c_1\abs z^2}$ already gives
$$
\abs{f(z)}\le Ce^{c_1(x^2+y^2)}\le Ce^{-c_1x^2+3c_1y^2},
$$
the second inequality because $y^2\ge x^2$ makes $c_1(x^2+y^2)\le -c_1x^2+3c_1y^2$. Taking $a'=\min(a,c_1)$, $b'=\max(b,3c_1)$ and enlarging $C$ gives a single estimate on $\CC$.
:::

:::


::: {.pf-step #converse}
Conversely, if $\abs{f(x+iy)}\le C'e^{-ax^2+by^2}$ with $a,b>0$, then $\abs{f(x)}\le C'e^{-ax^2}$ on $\RR$ and $\abs{f(z)}\le C'e^{b\abs z^2}$, so $f$ has strict order at most $2$ and is bounded by $e^{-ax^2}$ on the real axis.

::: pf-proof
At $y=0$ the estimate reads $\abs{f(x)}\le C'e^{-ax^2}$, giving the decay with $c_2=a$. For general $z=x+iy$ one has $-ax^2+by^2\le b(x^2+y^2)=b\abs z^2$ because $-a\le b$, so $\abs{f(z)}\le C'e^{b\abs z^2}$, which is the growth hypothesis with $c_1=b$. So the converse implication in the statement holds with the same pairs $(a,b)$ and $(c_1,c_2)$ interchanged.
:::

:::


::: {.pf-step #conclusion}
The stated implication and its converse both hold.

::: pf-proof
Steps [](#sector){.pf-ref} to [](#all){.pf-ref} prove the nontrivial implication, with explicit $a=c_2-c_1\varepsilon$ and $b=c_2+c_1\varepsilon^{-1}$, and step [](#converse){.pf-ref} proves the converse.
:::

:::

:::
:::
