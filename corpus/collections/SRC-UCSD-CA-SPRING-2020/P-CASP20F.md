---
schema: qual/card@1
id: P-CASP20F
kind: problem
title: 'An entire function with bounded derivative and zeros at $\sqrt n$ is identically zero'
classification:
  areas:
  - complex-analysis
  topics:
  - Entire Functions
  - Identity Theorem
  - Growth Estimates
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Rewritten as a Lamport structured proof of the argument already on the card, correct as it
    stood. Added: the segment integral giving |f(z) - f(0)| <= |z| e^{|z|}; the exact relation
    M_g(R) = M_f(R)/R^m and hence log M_g(R) = O(R); the observation that none of the zeros
    sqrt n is the origin, so all survive the division by z^m; the lower bound on the Jensen sum
    from the first floor(R^2/4) zeros, with nonnegativity of the remaining terms; Jensen's
    formula written in full with the integral bounded by log M_g(R); and the resulting
    R^2 <= cR contradiction. Not claimed: a retained solution set; the provenance names the
    examination paper.
---

::: {.problem}
Let $f : \CC \to \CC$ be an entire function such that $\abs{f'(z)} \leq e^{\abs{z}}$ and $f\!\left(\sqrt{n}\right) = 0$ for all positive integers $n > 0$.
Show that $f = 0$.
:::

::: {.solution}
No retained solution set covers this problem: the collection's `provenance` names the Spring 2020 complex-analysis examination paper, which carries no solutions. The argument below is the card's own and follows the card's previous prose: a growth estimate of order $R$ together with Jensen's formula and the sequence of zeros $\sqrt n$, whose first $R^2/4$ terms force a growth of order $R^2$.

Throughout $f$ is entire with $\abs{f'(z)}\le e^{\abs z}$ and $f(\sqrt n)=0$ for every positive integer $n$, and $M_g(R)=\max_{\abs z=R}\abs g$.

::: pf

::: {.pf-step #growth}
$\abs{f(z)}\le\abs{f(0)}+\abs z e^{\abs z}$, hence $\log M_f(R)=O(R)$.

::: pf-proof
$f(z)-f(0)=\int_0^1f'(tz)z\,dt$ along the segment from $0$ to $z$, so $\abs{f(z)-f(0)}\le\abs z\max_{0\le t\le1}\abs{f'(tz)}\le\abs z e^{\abs z}$. For $\abs z=R$ this gives $\log M_f(R)\le\log\bigl(\abs{f(0)}+Re^{R}\bigr)=O(R)$.

:::

:::

::: {.pf-step #reduce}
If $f\not\equiv0$, write $f(z)=z^mg(z)$ with $m\ge0$, $g$ entire and $g(0)\ne0$; then $\log M_g(R)=O(R)$ and $g$ vanishes at every $\sqrt n$.

::: pf-proof
$m$ is the order of the zero of $f$ at $0$ (possibly $0$), and $g=f/z^m$ is entire with $g(0)\ne0$. For $\abs z=R\ge1$, $\abs{g(z)}=\abs{f(z)}/R^m$, so $M_g(R)=M_f(R)/R^m$ and $\log M_g(R)=\log M_f(R)-m\log R=O(R)$. Since $\sqrt n\ge1\ne0$, none of these zeros is the origin, so all of them are zeros of $g$.

:::

:::

::: {.pf-step #jensen-lower}
For large $R$ the Jensen sum over the zeros $a_k$ of $g$ satisfies
$$
\sum_{\abs{a_k}<R}\log\frac{R}{\abs{a_k}}\ge\Bigl\lfloor\frac{R^2}{4}\Bigr\rfloor\log2 .
$$

::: pf-proof
The zeros include every $\sqrt n$ with $n\ge1$. If $\sqrt n\le R/2$, that is $n\le R^2/4$, then $R/\sqrt n\ge2$ and the corresponding term is at least $\log2$. The number of such $n$ is $\lfloor R^2/4\rfloor$, and all terms are nonnegative (for $\abs{a_k}<R$), so the sum is at least that many times $\log 2$.

:::

:::

::: {.pf-step #jensen-upper}
$\log\abs{g(0)}+\displaystyle\sum_{\abs{a_k}<R}\log\frac{R}{\abs{a_k}}\le\log M_g(R)=O(R)$.

::: pf-proof
Jensen's formula for a function holomorphic on a neighbourhood of the closed disk of radius $R$ reads
$$
\log\abs{g(0)}+\sum_{\abs{a_k}<R}\log\frac{R}{\abs{a_k}}=\frac1{2\pi}\int_0^{2\pi}\log\abs{g(Re^{i\theta})}\,d\theta,
$$
and the right side is at most $\log M_g(R)$, which is $O(R)$ by step [](#reduce){.pf-ref}.

:::

:::

::: {.pf-step #contradiction}
$f\equiv0$.

::: pf-proof
Combining steps [](#jensen-lower){.pf-ref} and [](#jensen-upper){.pf-ref}, $\lfloor R^2/4\rfloor\log2\le\log M_g(R)-\log\abs{g(0)}=O(R)$, that is $R^2\lesssim cR$ for a constant $c$ and all large $R$ — impossible. So the assumption $f\not\equiv0$ fails, and $f$ is identically zero.

:::

:::

:::
:::
