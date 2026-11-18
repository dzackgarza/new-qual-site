---
schema: qual/card@1
id: P-CAS24C
kind: problem
title: Schwarz–Pick type bound for positive real part on the disc
classification:
  areas:
  - complex-analysis
  topics:
  - Schwarz Lemma
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Lamport structure, and the Möbius map's two properties proved. The prose said the map Phi(w) = (w-a)/(w-abar) "maps the right half-plane to the unit disk and sends a to 0" without proof; the card now computes |w-a|^2 - |w+abar|^2 = -4 Re(w) Re(a) < 0 on the right half-plane, which is the inequality behind that claim, and notes that the pole -abar has negative real part so Phi is holomorphic there. It also computes Phi'(a) = 1/(2 Re a) and states the Schwarz lemma step. The collection's provenance is the examination paper alone, so no retained solution set covers the exercise and the card says the argument is its own. No statement repair; the bound is correct.
---

::: {.problem}
Let $f : \DD \to \CC$ be holomorphic.
Assume $\operatorname{Re} f(z) > 0$ for all $z \in \DD$.
Show that
$$
\abs{f'(0)} \le 2\operatorname{Re} f(0).
$$
:::

::: {.solution}
The collection's provenance is the examination paper alone, so no retained solution set covers this exercise; the argument is the card's own.

Put $a=f(0)$, so that $\operatorname{Re}a>0$ because $f$ maps $\DD$ into the right half-plane.

::: pf

::: {.pf-step #mobius}
$\Phi(w)=\dfrac{w-a}{w+\overline a}$ is holomorphic on the right half-plane $H=\{\operatorname{Re}w>0\}$, and $\abs{\Phi(w)}<1$ for every $w\in H$.

::: pf-proof
The denominator vanishes only at $w=-\overline a$, and $\operatorname{Re}(-\overline a)=-\operatorname{Re}a<0$, so $-\overline a\notin H$ and $\Phi$ is holomorphic on $H$.
For $w\in H$,
$$
\abs{w-a}^2=\abs{w}^2-2\operatorname{Re}(w\overline a)+\abs{a}^2,
\qquad
\abs{w+\overline a}^2=\abs{w}^2+2\operatorname{Re}(wa)+\abs{a}^2,
$$
because $\abs{w-a}^2=(w-a)(\overline w-\overline a)$ and $2\operatorname{Re}(w\overline a)=w\overline a+\overline w a$, and similarly for the sum. Hence
$$
\abs{w-a}^2-\abs{w+\overline a}^2=-2\operatorname{Re}\bigl(w\overline a+wa\bigr)=-2\operatorname{Re}\bigl(w(a+\overline a)\bigr)=-4\operatorname{Re}w\,\operatorname{Re}a<0,
$$
using $a+\overline a=2\operatorname{Re}a$, $\operatorname{Re}w>0$ and $\operatorname{Re}a>0$. So $\abs{w-a}<\abs{w+\overline a}$, the denominator being nonzero, and $\abs{\Phi(w)}<1$.
:::

:::

::: {.pf-step #cayley}
$\Phi(a)=0$ and $\Phi'(a)=\dfrac1{2\operatorname{Re}a}$.

::: pf-proof
$\Phi(a)=(a-a)/(a+\overline a)=0$. By the quotient rule,
$$
\Phi'(w)=\frac{(w+\overline a)-(w-a)}{(w+\overline a)^2}=\frac{a+\overline a}{(w+\overline a)^2},
$$
and $a+\overline a=2\operatorname{Re}a$, so $\Phi'(a)=\frac{2\operatorname{Re}a}{(2\operatorname{Re}a)^2}=\frac1{2\operatorname{Re}a}$; here $2\operatorname{Re}a\ne0$ because $\operatorname{Re}a>0$.
:::

:::

::: {.pf-step #schwarz}
$g=\Phi\circ f$ maps $\DD$ holomorphically into $\DD$ with $g(0)=0$, so $\abs{g'(0)}\le1$.

::: pf-proof
$f(\DD)\subseteq H$ by hypothesis, so $g$ is defined on $\DD$ and holomorphic as a composite of holomorphic maps, and $g(\DD)\subseteq\DD$ by step [](#mobius){.pf-ref}. Moreover $g(0)=\Phi(f(0))=\Phi(a)=0$ by step [](#cayley){.pf-ref}. Schwarz's lemma, applied to the holomorphic $g:\DD\to\DD$ with $g(0)=0$, gives $\abs{g'(0)}\le1$.
:::

:::

::: {.pf-step #conclusion}
$\abs{f'(0)}\le2\operatorname{Re}f(0)$.

::: pf-proof
By the chain rule $g'(0)=\Phi'(a)f'(0)$, so by step [](#cayley){.pf-ref}
$$
\abs{g'(0)}=\frac{\abs{f'(0)}}{2\operatorname{Re}a},
$$
and step [](#schwarz){.pf-ref} bounds the left side by $1$. Multiplying by the positive number $2\operatorname{Re}a=2\operatorname{Re}f(0)$ gives $\abs{f'(0)}\le2\operatorname{Re}f(0)$.
:::

:::

:::
:::
